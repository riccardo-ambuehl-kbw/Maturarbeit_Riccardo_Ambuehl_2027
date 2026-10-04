"""Common strategy result and invariants for every exported portfolio history."""
from dataclasses import dataclass
import numpy as np
import pandas as pd
from ..funktionen import WEIGHT_TOLERANCE, CAPITAL_TOLERANCE
from ..data.macro import select_gdp_targets

HISTORY_COLUMNS = ["date", "strategy", "portfolio_value", "period_return", "drawdown"]
WEIGHTS_COLUMNS = ["date", "strategy", "asset_id", "weight_before", "target_weight", "weight_after"]
TRADES_COLUMNS = ["date", "strategy", "asset_id", "value_before", "target_value", "transaction_value"]
SIGNALS_COLUMNS = ["date", "strategy", "asset_id", "signal", "position", "signal_value", "sma_short", "sma_long"]


def annual_rebalance_dates(dates):
    """Last shared valuation of a year, with an earned and a following interval."""
    return tuple(dates[i] for i in range(1, len(dates) - 1) if dates[i].year != dates[i + 1].year)


@dataclass(frozen=True)
class StrategyResult:
    strategy: str
    portfolio_history: pd.DataFrame
    weights_history: pd.DataFrame | None = None
    trades: pd.DataFrame | None = None
    signals: pd.DataFrame | None = None
    macro_decisions: tuple[dict, ...] | None = None

    def validate(self, start_capital):
        h = self.portfolio_history
        if list(h.columns) != HISTORY_COLUMNS or len(h) < 2:
            raise ValueError("Invalid common portfolio history.")
        if not h.date.is_unique or not h.date.is_monotonic_increasing or h.date.isna().any():
            raise ValueError("History dates must be unique, ordered and complete.")
        if not (h.strategy == self.strategy).all():
            raise ValueError("Strategy names must be consistent.")
        if h.portfolio_value.iloc[0] != start_capital or not pd.isna(h.period_return.iloc[0]) or h.drawdown.iloc[0] != 0:
            raise ValueError("Invalid explicit initial valuation.")
        if not np.isfinite(h[["portfolio_value", "drawdown"]].to_numpy()).all() or (h.portfolio_value <= 0).any():
            raise ValueError("Portfolio values/drawdowns must be finite, with positive wealth.")
        if not np.isfinite(h.period_return.iloc[1:].to_numpy()).all():
            raise ValueError("Observed returns must be complete and finite.")
        expected = h.portfolio_value.iloc[1:].to_numpy() / h.portfolio_value.iloc[:-1].to_numpy() - 1
        if not np.allclose(expected, h.period_return.iloc[1:], rtol=1e-12, atol=1e-14):
            raise ValueError("History returns disagree with wealth ratios.")
        self._validate_allocations()
        self._validate_signals()
        return self

    def _validate_signals(self):
        s = self.signals
        if s is None:
            if self.strategy == "trend":
                raise ValueError("Trend requires a signals table.")
            return
        if (list(s.columns) != SIGNALS_COLUMNS or len(s) != len(self.portfolio_history)
                or not pd.DatetimeIndex(s.date).equals(pd.DatetimeIndex(self.portfolio_history.date))
                or not (s.strategy == self.strategy).all() or s.asset_id.nunique() != 1
                or not s.asset_id.map(lambda a: isinstance(a, str) and bool(a.strip())).all()):
            raise ValueError("Signals must cover the complete ordered history for one asset.")
        if (not np.isfinite(s[["signal", "signal_value", "sma_short", "sma_long"]].to_numpy(dtype=float)).all()
                or not s.signal.isin([0, 1]).all()
                or not np.array_equal(s.signal.to_numpy(), (s.sma_short > s.sma_long).astype(int).to_numpy())
                or not pd.isna(s.position.iloc[0])
                or not np.array_equal(s.position.iloc[1:].to_numpy(), s.signal.iloc[:-1].to_numpy())):
            raise ValueError("Invalid complete SMA signals or one-period positions.")

    def _validate_allocations(self):
        w, t, h = self.weights_history, self.trades, self.portfolio_history
        if w is None and t is None:
            if self.strategy in {"rebalance", "country_weighting"}:
                raise ValueError("Rebalancing requires weights and trades tables.")
            return
        if w is None or t is None or list(w.columns) != WEIGHTS_COLUMNS or list(t.columns) != TRADES_COLUMNS:
            raise ValueError("Invalid weights/trades columns.")
        assets = tuple(sorted(w.asset_id.unique()))
        expected_keys = {(date, asset) for date in h.date for asset in assets}
        if (not assets or w.duplicated(["date", "asset_id"]).any()
                or set(zip(w.date, w.asset_id)) != expected_keys):
            raise ValueError("Weights must cover every valuation and asset exactly once.")
        for table, columns in [(w, WEIGHTS_COLUMNS), (t, TRADES_COLUMNS)]:
            if (not (table.strategy == self.strategy).all() or table.date.isna().any()
                    or table.duplicated(["date", "asset_id"]).any()
                    or not np.isfinite(table[columns[3:]].to_numpy(dtype=float)).all()):
                raise ValueError("Invalid finite, unique allocation/trade rows.")
        if (w[WEIGHTS_COLUMNS[3:]] < 0).any().any():
            raise ValueError("Weights must be long-only.")
        sums = w.groupby("date")[WEIGHTS_COLUMNS[3:]].sum()
        if not np.allclose(sums, 1.0, rtol=0, atol=WEIGHT_TOLERANCE):
            raise ValueError("Weights must sum to 1 at every valuation.")
        target = w.loc[w.date == h.date.iloc[0]].set_index("asset_id").target_weight.sort_index()
        trade_dates = set(t.date)
        if self.strategy == "country_weighting" and trade_dates != set(annual_rebalance_dates(h.date.tolist())):
            raise ValueError("Country-weighting trades must follow the annual valuation calendar.")
        wealth = h.set_index("date").portfolio_value
        for date, group in w.groupby("date", sort=True):
            group = group.set_index("asset_id").sort_index()
            if not np.array_equal(group.target_weight.to_numpy(), target.to_numpy()):
                if self.strategy != "country_weighting" or date not in trade_dates:
                    raise ValueError("Target weights may change only at actual country-weighting rebalancings.")
                target = group.target_weight.copy()
            expected_after = group.target_weight if date in trade_dates or date == h.date.iloc[0] else group.weight_before
            if not np.allclose(group.weight_after, expected_after, rtol=0, atol=WEIGHT_TOLERANCE):
                raise ValueError("Weight states disagree with rebalancing events.")
            if date == h.date.iloc[0] and not np.allclose(group.weight_before, target, rtol=0, atol=WEIGHT_TOLERANCE):
                raise ValueError("Initial weights must equal targets.")
        for date, group in t.groupby("date", sort=True):
            if date not in set(h.date.iloc[1:-1]) or tuple(sorted(group.asset_id)) != assets:
                raise ValueError("Trades require a complete asset set, no initial/final trades.")
            group = group.set_index("asset_id").sort_index()
            wg = w.loc[w.date == date].set_index("asset_id").sort_index()
            total = wealth.loc[date]
            if ((group[["value_before", "target_value"]] < 0).any().any()
                    or not np.allclose(group.transaction_value, group.target_value - group.value_before,
                                       rtol=CAPITAL_TOLERANCE, atol=CAPITAL_TOLERANCE * total)
                    or not np.allclose([group.value_before.sum(), group.target_value.sum()], total,
                                       rtol=CAPITAL_TOLERANCE, atol=0)
                    or abs(group.transaction_value.sum()) > CAPITAL_TOLERANCE * total
                    or not np.allclose(group.value_before / total, wg.weight_before, rtol=0, atol=WEIGHT_TOLERANCE)
                    or not np.allclose(group.target_value / total, wg.target_weight, rtol=0, atol=WEIGHT_TOLERANCE)):
                raise ValueError("Trade values, weights and capital conservation disagree.")


def validate_results(context, results):
    results = (results,) if isinstance(results, StrategyResult) else tuple(results)
    results = tuple(sorted(results, key=lambda r: r.strategy))
    if not results or len({r.strategy for r in results}) != len(results):
        raise ValueError("A run requires unique strategy results.")
    for result in results:
        result.validate(context.config.start_capital)
        if not pd.DatetimeIndex(result.portfolio_history.date).equals(context.performance.index):
            raise ValueError("Every strategy must use the complete shared valuation calendar.")
        if result.strategy == "country_weighting":
            events = annual_rebalance_dates(context.performance.index)
            if context.macro is None or set(result.trades.date) != set(events):
                raise ValueError("Country-weighting trades must match the annual shared calendar.")
            decisions = []
            for date in (context.performance.index[0], *events):
                kind = "initial" if date == context.performance.index[0] else "annual_rebalance"
                targets, decision = select_gdp_targets(context.macro, context.config.country_params(), date, kind)
                actual = result.weights_history.loc[result.weights_history.date == date].set_index("asset_id").target_weight.sort_index()
                if not actual.equals(targets):
                    raise ValueError("Country target weights differ from the historical GDP decision.")
                decisions.append(decision)
            if result.macro_decisions != tuple(decisions):
                raise ValueError("Macro provenance must match every applied historical GDP decision.")
        if result.strategy == "trend":
            signals = result.signals
            if not (signals.asset_id == context.config.trend_asset).all():
                raise ValueError("Trend signal asset differs from configuration.")
            expected = context.trend_signals
            if expected is None or not np.array_equal(
                    signals[["signal_value", "sma_short", "sma_long", "signal"]].to_numpy(), expected.to_numpy()):
                raise ValueError("Trend signals differ from the prepared source and SMA context.")
            prices = context.performance[context.config.trend_asset].to_numpy()
            returns = (prices[1:] / prices[:-1] - 1) * signals.position.iloc[1:].to_numpy()
            if not np.array_equal(result.portfolio_history.period_return.iloc[1:].to_numpy(), returns):
                raise ValueError("Trend returns must use lagged positions and performance values.")
    return results
