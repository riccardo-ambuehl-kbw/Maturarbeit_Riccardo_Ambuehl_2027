"""SMA Long/Cash: yesterday's valuation signal earns today's performance return."""
import numpy as np
import pandas as pd
from ..funktionen import prozentuale_aenderung, buy_and_hold, drawdown
from ..engine.result import StrategyResult, SIGNALS_COLUMNS


class Trend:
    def run(self, context, params):
        if (params != context.config.trend_params() or not context.config.trend_enabled
                or context.trend_signals is None):
            raise ValueError("Trend requires its explicitly configured, prepared signal context.")
        dates = context.performance.index
        signals = context.trend_signals.copy(deep=True)
        if not signals.index.equals(dates):
            raise ValueError("Trend signals must cover the complete shared valuation calendar.")
        prices = context.performance[params["asset"]].copy()
        market_returns = prozentuale_aenderung(prices).iloc[1:]
        if not np.isfinite(market_returns).all() or (market_returns <= -1).any():
            raise ValueError("Observed market returns exceed finite numerical precision.")
        position = signals.signal.shift(1)
        returns = market_returns * position.iloc[1:]
        capital = context.config.start_capital
        h = pd.DataFrame({"date": dates, "strategy": "trend",
                          "portfolio_value": np.r_[capital, buy_and_hold(returns, capital).to_numpy()],
                          "period_return": np.r_[np.nan, returns.to_numpy()],
                          "drawdown": np.r_[0., drawdown(returns).to_numpy()]})
        signals["position"] = position
        signals["date"], signals["strategy"], signals["asset_id"] = dates, "trend", params["asset"]
        return StrategyResult("trend", h, signals=signals[SIGNALS_COLUMNS].reset_index(drop=True)).validate(capital)
