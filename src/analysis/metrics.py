"""Shared metrics. The initial valuation is excluded from the return sample."""
import math
import numpy as np
import pandas as pd
from ..funktionen import annualisierte_rendite, annualisierte_volatilitaet, sharpe_ratio, maximum_drawdown

SUMMARY_COLUMNS = ["strategy", "start_value", "end_value", "total_return", "annualized_return",
                   "annualized_volatility", "sharpe_ratio", "max_drawdown"]


def annual_return_from_factors(factors, periods_per_year, *, input_kind):
    """Explicit input semantics are mandatory even when all numbers are positive."""
    return annualisierte_rendite(np.asarray(factors), periods_per_year, input_kind=input_kind)


def compute_metrics(result, context):
    h = result.portfolio_history
    returns = pd.Series(h.period_return.iloc[1:].to_numpy(),
                        index=pd.DatetimeIndex(h.date.iloc[1:]), name="period_return")
    first, last = float(h.portfolio_value.iloc[0]), float(h.portfolio_value.iloc[-1])
    row = {"strategy": result.strategy, "start_value": first, "end_value": last,
           "total_return": last / first - 1, "annualized_return": None,
           "annualized_volatility": None, "sharpe_ratio": None,
           "max_drawdown": float(maximum_drawdown(returns))}
    status = {}
    if context.annualization_available:
        # Converting returns to factors is explicit at this single call site.
        row["annualized_return"] = float(annual_return_from_factors(
            1.0 + returns.to_numpy(), context.config.periods_per_year, input_kind="growth_factors"))
        if len(returns) >= 2:
            row["annualized_volatility"] = float(annualisierte_volatilitaet(returns.to_numpy(),
                                                                         context.config.periods_per_year))
        else:
            status["annualized_volatility"] = "fewer_than_two_observed_returns"
        if context.risk_free is None:
            status["sharpe_ratio"] = "risk_free_not_provided"
        else:
            value = sharpe_ratio(returns, context.risk_free, context.config.periods_per_year)
            row["sharpe_ratio"] = float(value) if math.isfinite(value) else None
            if row["sharpe_ratio"] is None:
                status["sharpe_ratio"] = "insufficient_sample_or_zero_excess_volatility"
    else:
        for key in ["annualized_return", "annualized_volatility", "sharpe_ratio"]:
            status[key] = context.annualization_status
    for key, value in row.items():
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError(f"Metric {key} exceeded finite numerical precision.")
    if not np.isclose(row["max_drawdown"], h.drawdown.min(), atol=1e-14, rtol=1e-12):
        raise ValueError("Maximum drawdown and history disagree.")
    return pd.DataFrame([row], columns=SUMMARY_COLUMNS), status


def compute_run_metrics(results, context):
    """One canonical summary/status shape for runner and export validation."""
    summaries, statuses = [], {}
    for result in results:
        summary, status = compute_metrics(result, context)
        summaries.append(summary)
        statuses[result.strategy] = status
    metric_status = statuses[results[0].strategy] if len(results) == 1 else statuses
    return pd.concat(summaries, ignore_index=True), metric_status


def validate_run_metrics(results, context, summary, metric_status):
    """Reject inconsistent numbers and availability using the existing metric calculation."""
    expected, expected_status = compute_run_metrics(results, context)
    if (not isinstance(summary, pd.DataFrame) or list(summary.columns) != SUMMARY_COLUMNS
            or len(summary) != len(expected)
            or summary.strategy.tolist() != expected.strategy.tolist()):
        raise ValueError("Summary must contain the exact columns and one ordered row per strategy.")
    for column in SUMMARY_COLUMNS[1:]:
        for actual, wanted in zip(summary[column], expected[column]):
            if pd.isna(wanted):
                if not pd.api.types.is_scalar(actual) or not pd.isna(actual):
                    raise ValueError(f"Unavailable summary metric {column} must be missing.")
            elif (isinstance(actual, (bool, np.bool_))
                  or not isinstance(actual, (int, float, np.number))
                  or not np.isrealobj(actual) or not np.isfinite(actual)
                  or actual != wanted):
                raise ValueError(f"Summary metric {column} disagrees with the computed value.")
    if not isinstance(metric_status, dict) or metric_status != expected_status:
        raise ValueError("Metric availability status disagrees with the computed summary.")
