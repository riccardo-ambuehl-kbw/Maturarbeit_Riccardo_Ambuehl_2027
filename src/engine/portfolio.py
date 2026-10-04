"""Shared annual portfolio state sequence for fixed and historical GDP targets."""
import numpy as np
import pandas as pd
from ..funktionen import (prozentuale_aenderung, neue_gewichtung, rebalancing, drawdown,
                          validate_target_weights, allocate_target_values, CAPITAL_TOLERANCE, WEIGHT_TOLERANCE)
from .result import StrategyResult, HISTORY_COLUMNS, WEIGHTS_COLUMNS, TRADES_COLUMNS, annual_rebalance_dates


def run_annual_portfolio(context, strategy, target_at):
    dates = context.performance.index
    target = validate_target_weights(target_at(dates[0], "initial")).sort_index()
    assets = target.index
    if not set(assets).issubset(context.performance.columns):
        raise ValueError("All portfolio assets must be prepared in the shared context.")
    prices = context.performance.loc[:, assets].copy()
    returns = prices.apply(prozentuale_aenderung).iloc[1:]
    capital = context.config.start_capital
    positions = allocate_target_values(capital, target)
    history = [[dates[0], strategy, capital, np.nan, 0.0]]
    weights, trades = [], []
    for asset in assets:
        weights.append([dates[0], strategy, asset, target[asset], target[asset], target[asset]])
    previous_total = capital
    events = set(annual_rebalance_dates(dates))
    for date in dates[1:]:
        positions, before = neue_gewichtung(positions, returns.loc[date])
        total = float(positions.sum())
        history.append([date, strategy, total, total / previous_total - 1, 0.0])
        after = before.copy()
        if date in events:
            target = validate_target_weights(target_at(date, "annual_rebalance")).sort_index()
            if not target.index.equals(assets):
                raise ValueError("Annual decisions must preserve the configured asset set.")
            current, before, _, positions, transactions = rebalancing(positions, target)
            after = positions / positions.sum()
            for asset in assets:
                trades.append([date, strategy, asset, current[asset], positions[asset], transactions[asset]])
        for asset in assets:
            weights.append([date, strategy, asset, before[asset], target[asset], after[asset]])
        previous_total = total
    h = pd.DataFrame(history, columns=HISTORY_COLUMNS)
    observed = pd.Series(h.period_return.iloc[1:].to_numpy(), index=dates[1:])
    h.loc[1:, "drawdown"] = drawdown(observed).to_numpy()
    return StrategyResult(strategy, h, pd.DataFrame(weights, columns=WEIGHTS_COLUMNS),
                          pd.DataFrame(trades, columns=TRADES_COLUMNS)).validate(capital)


def validate_market_portfolio_state(context, result):
    """Replay the shared state sequence after targets/calendar have been validated."""
    weights = result.weights_history.set_index(["date", "asset_id"]).sort_index()

    def target_at(date, kind):
        # Config/GDP binding was checked first; preserve the accepted target tolerance.
        return weights.xs(date, level="date").target_weight

    expected = run_annual_portfolio(context, result.strategy, target_at)
    history, wanted = result.portfolio_history, expected.portfolio_history
    if (not np.allclose(history.portfolio_value, wanted.portfolio_value,
                        rtol=CAPITAL_TOLERANCE, atol=0)
            or not np.allclose(history.period_return.iloc[1:], wanted.period_return.iloc[1:],
                               rtol=CAPITAL_TOLERANCE, atol=1e-14)):
        raise ValueError(f"{result.strategy} history disagrees with the market portfolio state.")
    wanted_weights = expected.weights_history.set_index(["date", "asset_id"]).sort_index()
    if (not weights.index.equals(wanted_weights.index)
            or not np.allclose(weights[WEIGHTS_COLUMNS[3:]], wanted_weights[WEIGHTS_COLUMNS[3:]],
                               rtol=0, atol=WEIGHT_TOLERANCE)):
        raise ValueError(f"{result.strategy} weights disagree with the market portfolio state.")
    trades = result.trades.set_index(["date", "asset_id"]).sort_index()
    wanted_trades = expected.trades.set_index(["date", "asset_id"]).sort_index()
    if not trades.index.equals(wanted_trades.index):
        raise ValueError(f"{result.strategy} trades disagree with the market portfolio state.")
    totals = wanted.set_index("date").portfolio_value.reindex(wanted_trades.index.get_level_values("date"))
    if not np.allclose(trades[TRADES_COLUMNS[3:]].to_numpy(dtype=float),
                       wanted_trades[TRADES_COLUMNS[3:]].to_numpy(dtype=float),
                       rtol=CAPITAL_TOLERANCE, atol=CAPITAL_TOLERANCE * totals.to_numpy()[:, None]):
        raise ValueError(f"{result.strategy} trades disagree with the market portfolio state.")
