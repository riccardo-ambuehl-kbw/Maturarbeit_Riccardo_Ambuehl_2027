"""Fully invested single-asset Buy-and-Hold using the existing functions."""
import numpy as np
import pandas as pd
from ..funktionen import prozentuale_aenderung, buy_and_hold, drawdown
from ..engine.result import StrategyResult


class BuyAndHold:
    def run(self, context, params):
        if set(params) != {"asset"} or params["asset"] not in context.performance.columns:
            raise ValueError("Buy-and-Hold requires exactly one prepared asset.")
        prices = context.performance[params["asset"]].copy()
        returns = prozentuale_aenderung(prices).iloc[1:]
        if not np.isfinite(returns.to_numpy()).all() or (returns <= -1).any():
            raise ValueError("Observed returns are invalid or exceed numerical precision.")
        values = buy_and_hold(returns, context.config.start_capital)
        dd = drawdown(returns)
        h = pd.DataFrame({
            "date": prices.index, "strategy": "buy_hold",
            "portfolio_value": np.r_[context.config.start_capital, values.to_numpy()],
            "period_return": np.r_[np.nan, returns.to_numpy()],
            "drawdown": np.r_[0.0, dd.to_numpy()],
        })
        return StrategyResult("buy_hold", h).validate(context.config.start_capital)
