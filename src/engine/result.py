"""Common strategy result and invariants for every exported portfolio history."""
from dataclasses import dataclass
import numpy as np
import pandas as pd

HISTORY_COLUMNS = ["date", "strategy", "portfolio_value", "period_return", "drawdown"]


@dataclass(frozen=True)
class StrategyResult:
    strategy: str
    portfolio_history: pd.DataFrame
    weights_history: pd.DataFrame | None = None
    trades: pd.DataFrame | None = None
    signals: pd.DataFrame | None = None

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
        return self
