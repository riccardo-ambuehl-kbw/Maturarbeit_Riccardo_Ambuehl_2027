"""Fail on missing observations; never fill, interpolate or invent a calendar."""
import numpy as np
import pandas as pd
from ..engine.config import iso_date


class DataValidationError(ValueError):
    pass


def require_columns(frame, names):
    missing = set(names) - set(frame.columns)
    if missing or frame.empty:
        raise DataValidationError(f"Empty data or missing columns: {sorted(missing)}")


def dates(values):
    try:
        return pd.to_datetime([iso_date(v) for v in values])
    except ValueError as exc:
        raise DataValidationError(str(exc)) from exc


def numeric(values, positive=False):
    try:
        result = pd.to_numeric(values, errors="raise").astype(float)
    except (TypeError, ValueError) as exc:
        raise DataValidationError("Values must be numeric, complete and finite.") from exc
    if not np.isfinite(result.to_numpy()).all() or (positive and (result <= 0).any()):
        raise DataValidationError("Values must be finite and, for prices, positive; NaN/Inf are errors.")
    return result


def identifiers(frame, columns):
    for col in columns:
        if not frame[col].map(lambda x: isinstance(x, str) and bool(x.strip())).all():
            raise DataValidationError(f"Missing/invalid identifier in {col}.")


def validate_assets(frame):
    fields = ["asset_id", "name", "asset_class", "country", "currency", "provider", "provider_symbol"]
    require_columns(frame, fields)
    identifiers(frame, fields)
    if frame["asset_id"].duplicated().any():
        raise DataValidationError("Duplicate asset_id in metadata.")
    return frame.copy()


def validate_market(frame, assets, required_assets, base_currency):
    require_columns(frame, ["date", "asset_id", "performance_value"])
    identifiers(frame, ["asset_id"])
    frame = frame.copy()
    frame["date"] = dates(frame["date"])
    frame["performance_value"] = numeric(frame["performance_value"], positive=True)
    if frame.duplicated(["date", "asset_id"]).any():
        raise DataValidationError("Duplicate (date, asset_id).")
    unknown = set(frame["asset_id"]) - set(assets["asset_id"])
    if unknown:
        raise DataValidationError(f"Unknown asset_id in market data: {sorted(unknown)}")
    for asset in required_assets:
        metadata = assets.loc[assets["asset_id"] == asset]
        if metadata.empty or asset not in set(frame["asset_id"]):
            raise DataValidationError(f"Missing required asset_id: {asset}")
        if metadata.iloc[0]["currency"] != base_currency:
            raise DataValidationError(f"Wrong currency for {asset}; FX conversion is unsupported.")
    return frame.sort_values(["date", "asset_id"], kind="stable").reset_index(drop=True)


def validate_risk_free(frame):
    require_columns(frame, ["period_start", "period_end", "series_id", "period_return"])
    frame = frame.copy()
    identifiers(frame, ["series_id"])
    for col in ["period_start", "period_end"]:
        frame[col] = dates(frame[col])
    frame["period_return"] = numeric(frame["period_return"])
    if (frame["period_start"] >= frame["period_end"]).any():
        raise DataValidationError("Risk-free period_start must precede period_end.")
    if frame.duplicated(["period_start", "period_end", "series_id"]).any():
        raise DataValidationError("Duplicate risk-free period/series.")
    return frame.sort_values(["series_id", "period_start", "period_end"], kind="stable").reset_index(drop=True)
