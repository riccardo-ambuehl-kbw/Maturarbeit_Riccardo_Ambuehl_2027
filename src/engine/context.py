"""Prepare a validated local context; no strategy-specific data cleaning."""
from dataclasses import dataclass
import pandas as pd
from .config import RunConfig
from ..data.normalize import read_csv_snapshot, align_performance, align_risk_free, prepare_trend_signals
from ..data.validate import validate_assets, validate_market, validate_risk_free, validate_macro, DataValidationError


@dataclass(frozen=True)
class SimulationContext:
    config: RunConfig
    performance: pd.DataFrame
    risk_free: pd.Series | None
    data_quality: dict
    input_files: tuple[dict, ...]
    annualization_available: bool
    annualization_status: str
    trend_signals: pd.DataFrame | None = None
    macro: pd.DataFrame | None = None


def check_period_logic(index, frequency, periods_per_year):
    """Conservative check: unknown/irregular grids yield unavailable annual metrics."""
    if frequency is None:
        return False, "period_frequency_not_declared"
    expected = pd.date_range(index[0], index[-1], freq=frequency)
    if not index.equals(expected):
        return False, "valuation_grid_not_regular_for_declared_frequency"
    compatible = {"MS": {12}, "ME": {12}, "YS": {1}, "YE": {1},
                  "D": {365, 366}, "W": {52}}
    if periods_per_year not in compatible[frequency]:
        return False, "periods_per_year_not_compatible_with_declared_frequency"
    return True, "available"


def prepare_context(config: RunConfig) -> SimulationContext:
    assets, asset_info = read_csv_snapshot(config.assets_path, "assets")
    assets = validate_assets(assets)
    market, market_info = read_csv_snapshot(config.market_path, "market")
    required = config.required_assets
    market = validate_market(market, assets, required, config.base_currency)
    if config.country_weighting_enabled:
        metadata = assets.set_index("asset_id")
        for country, asset in config.country_assets:
            if metadata.loc[asset, "country"] != country:
                raise DataValidationError(f"Country mismatch for proxy {asset}: expected {country}.")
    performance, quality = align_performance(market, required, config.start, config.end)
    used_columns = {"date", "asset_id", "performance_value"}
    trend_signals = None
    if config.trend_enabled:
        trend_signals, quality["trend"] = prepare_trend_signals(
            market, config.trend_asset, config.signal_source, config.short_window, config.long_window,
            performance.index)
        used_columns.add(config.signal_source)
    quality["unused_market_columns"] = sorted(set(market.columns) - used_columns)
    quality["requested_period"] = {"start": config.start.isoformat(), "end": config.end.isoformat()}
    quality["periods_per_year"] = config.periods_per_year
    rf = None
    inputs = [market_info, asset_info, {"kind": "config", "path": str(config.config_path),
                                      "sha256": config.config_sha256}]
    macro = None
    if config.country_weighting_enabled:
        macro_rows, macro_info = read_csv_snapshot(config.macro_path, "macro")
        macro = validate_macro(macro_rows)
        inputs.append(macro_info)
        quality["macro"] = {"loaded_rows": len(macro_rows), "validated_version_rows": len(macro),
                            "identical_duplicate_rows": len(macro_rows) - len(macro),
                            "configured_countries": sorted(dict(config.country_assets))}
    if config.risk_free_path is not None:
        frame, rf_info = read_csv_snapshot(config.risk_free_path, "risk_free")
        rf, quality["risk_free"] = align_risk_free(validate_risk_free(frame), config.risk_free_series,
                                                  performance.index)
        inputs.append(rf_info)
    else:
        quality["risk_free"] = {"status": "not_provided"}
        quality["warnings"].append("Risk-free input absent: Sharpe is unavailable, not a raw Sharpe.")
    available, status = check_period_logic(performance.index, config.period_frequency,
                                           config.periods_per_year)
    quality["annualization"] = {"available": available, "status": status,
                                "period_frequency": config.period_frequency}
    if not available:
        quality["warnings"].append(f"Annual metrics unavailable: {status}. No frequency is inferred.")
    return SimulationContext(config, performance, rf, quality, tuple(inputs), available, status,
                             trend_signals, macro)
