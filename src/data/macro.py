"""Historical GDP decisions using supplied version availability, without imputation."""
import math
import pandas as pd
from .validate import DataValidationError
from ..funktionen import validate_target_weights


def select_gdp_targets(macro, params, decision_date, decision_type):
    countries = sorted(params["country_assets"])
    available = macro.loc[(macro.indicator == params["indicator"])
                          & (macro.unit == params["unit"])
                          & macro.country.isin(countries)
                          & (macro.available_from <= decision_date)]
    years = [set(available.loc[available.country == country, "period"]) for country in countries]
    common = set.intersection(*years)
    if not common:
        raise DataValidationError(f"No common available GDP reference year at {decision_date.date()}.")
    period = max(common)
    selected = []
    for country in countries:
        versions = available.loc[(available.country == country) & (available.period == period)]
        selected.append(versions.sort_values("available_from", kind="stable").iloc[-1])
    try:
        total = math.fsum(float(row.value) for row in selected)
    except OverflowError as exc:
        raise DataValidationError("GDP sum exceeds finite numerical precision.") from exc
    weights = {params["country_assets"][row.country]: float(row.value) / total for row in selected}
    if any(weight <= 0 for weight in weights.values()):
        raise DataValidationError("Positive GDP weights exceed numerical precision.")
    targets = validate_target_weights(pd.Series(weights)).sort_index()
    decision = {"decision_date": decision_date.date().isoformat(), "decision_type": decision_type,
                "selected_period": period, "indicator": params["indicator"], "unit": params["unit"],
                "countries": [{"country": row.country, "asset_id": params["country_assets"][row.country],
                               "value": float(row.value), "available_from": row.available_from.date().isoformat(),
                               "target_weight": float(targets[params["country_assets"][row.country]])}
                              for row in selected]}
    return targets, decision
