"""Shared annual portfolio state sequence for fixed and historical GDP targets."""
import numpy as np
import pandas as pd
from ..funktionen import (prozentuale_aenderung, neue_gewichtung, rebalancing, drawdown,
                          validate_target_weights, CAPITAL_TOLERANCE)
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
    positions = capital * target
    if not np.isclose(positions.sum(), capital, rtol=CAPITAL_TOLERANCE, atol=0):
        raise ValueError("Initial allocation must preserve capital.")
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
