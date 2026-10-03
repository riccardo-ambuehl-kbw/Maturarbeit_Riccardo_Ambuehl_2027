"""Read immutable local CSV snapshots and align values before computing returns."""
from hashlib import sha256
from io import StringIO
from pathlib import Path
import csv
import pandas as pd
from .validate import DataValidationError


def read_csv_snapshot(path: Path, kind: str):
    content = path.read_bytes()
    text = content.decode("utf-8-sig")
    try:
        header = next(csv.reader(StringIO(text)))
        if len(header) != len(set(header)):
            raise DataValidationError(f"Duplicate CSV column in {path.name}.")
        frame = pd.read_csv(StringIO(text), dtype=str, keep_default_na=False)
    except (StopIteration, pd.errors.ParserError, pd.errors.EmptyDataError) as exc:
        raise DataValidationError(f"Invalid CSV: {path.name}") from exc
    return frame, {"kind": kind, "path": str(path), "sha256": sha256(content).hexdigest()}


def align_performance(market, required_assets, start, end):
    if not required_assets or len(set(required_assets)) != len(required_assets):
        raise DataValidationError("Required assets must be nonempty and unique.")
    series = {asset: market.loc[market.asset_id == asset].set_index("date")["performance_value"]
              for asset in required_assets}
    if any(s.empty for s in series.values()):
        raise DataValidationError("Required performance series is absent.")
    common = series[required_assets[0]].index
    for values in list(series.values())[1:]:
        common = common.intersection(values.index)
    common = common.sort_values()
    selected = common[(common >= pd.Timestamp(start)) & (common <= pd.Timestamp(end))]
    if len(selected) < 2:
        raise DataValidationError("At least two common valuations are needed in the requested period.")
    report = {
        "validation_status": "passed", "loaded_assets": sorted(market.asset_id.unique().tolist()),
        "required_assets": list(required_assets), "series": {}, "warnings": [],
        "effective_period": {"start": selected[0].date().isoformat(), "end": selected[-1].date().isoformat()},
        "common_observations": len(common), "used_observations": len(selected),
    }
    for asset, values in series.items():
        removed = values.index.difference(common)
        report["series"][asset] = {
            "original_start": values.index.min().date().isoformat(),
            "original_end": values.index.max().date().isoformat(), "loaded_observations": len(values),
            "used_observations": len(selected), "removed_non_common_dates": [d.date().isoformat() for d in removed],
            "outside_requested_period": int(((values.index < pd.Timestamp(start)) | (values.index > pd.Timestamp(end))).sum()),
        }
        if len(removed):
            report["warnings"].append(f"{asset}: {len(removed)} non-common valuations removed before returns.")
    return pd.DataFrame({asset: values.loc[selected] for asset, values in series.items()}, index=selected), report


def align_risk_free(frame, series_id, valuation_dates):
    rows = frame.loc[frame.series_id == series_id].set_index(["period_start", "period_end"])
    expected = pd.MultiIndex.from_arrays([valuation_dates[:-1], valuation_dates[1:]],
                                         names=["period_start", "period_end"])
    missing = expected.difference(rows.index)
    if len(missing):
        raise DataValidationError(f"Missing or misaligned risk-free periods for {series_id}: {list(missing)}")
    overlapping = rows.loc[(rows.index.get_level_values(0) < valuation_dates[-1])
                           & (rows.index.get_level_values(1) > valuation_dates[0])]
    if len(overlapping.index.difference(expected)):
        raise DataValidationError("Risk-free intervals overlap the run with incompatible boundaries.")
    values = rows.loc[expected, "period_return"]
    return pd.Series(values.to_numpy(), index=valuation_dates[1:], name="risk_free_return"), {
        "series_id": series_id, "loaded_periods": len(rows), "used_periods": len(expected),
        "unused_periods": len(rows) - len(expected),
    }
