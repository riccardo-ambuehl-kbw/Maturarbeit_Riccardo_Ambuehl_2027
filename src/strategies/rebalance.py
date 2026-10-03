"""Annual target-weight portfolios: returns, drift, then trades for the next interval."""
import numpy as np
import pandas as pd
from ..funktionen import (prozentuale_aenderung, neue_gewichtung, rebalancing, drawdown,
                          validate_target_weights, CAPITAL_TOLERANCE)
from ..engine.result import StrategyResult, HISTORY_COLUMNS, WEIGHTS_COLUMNS, TRADES_COLUMNS


class Rebalance:
    def run(self, context, params):
        if set(params) != {"target_weights", "rebalance_frequency"} or params["rebalance_frequency"] != "annual":
            raise ValueError("Rebalancing requires explicit target weights and annual frequency.")
        target = validate_target_weights(pd.Series(params["target_weights"])).sort_index()
        if not set(target.index).issubset(context.performance.columns):
            raise ValueError("All rebalancing assets must be prepared in the shared context.")
        prices = context.performance.loc[:, target.index].copy()
        returns = prices.apply(prozentuale_aenderung).iloc[1:]
        dates = prices.index
        capital = context.config.start_capital
        positions = capital * target
        if not np.isclose(positions.sum(), capital, rtol=CAPITAL_TOLERANCE, atol=0):
            raise ValueError("Initial allocation must preserve capital.")
        history = [[dates[0], "rebalance", capital, np.nan, 0.0]]
        weights, trades = [], []
        for asset in target.index:
            weights.append([dates[0], "rebalance", asset, target[asset], target[asset], target[asset]])
        previous_total = capital
        for i, date in enumerate(dates[1:], start=1):
            positions, before = neue_gewichtung(positions, returns.loc[date])
            total = float(positions.sum())
            history.append([date, "rebalance", total, total / previous_total - 1, 0.0])
            after = before.copy()
            # Known valuation calendar, never future performance, determines the event.
            if i < len(dates) - 1 and date.year != dates[i + 1].year:
                current, before, _, positions, transactions = rebalancing(positions, target)
                after = positions / positions.sum()
                for asset in target.index:
                    trades.append([date, "rebalance", asset, current[asset], positions[asset], transactions[asset]])
            for asset in target.index:
                weights.append([date, "rebalance", asset, before[asset], target[asset], after[asset]])
            previous_total = total
        h = pd.DataFrame(history, columns=HISTORY_COLUMNS)
        observed = pd.Series(h.period_return.iloc[1:].to_numpy(), index=dates[1:])
        h.loc[1:, "drawdown"] = drawdown(observed).to_numpy()
        return StrategyResult("rebalance", h, pd.DataFrame(weights, columns=WEIGHTS_COLUMNS),
                              pd.DataFrame(trades, columns=TRADES_COLUMNS)).validate(capital)
