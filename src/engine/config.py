"""Strict JSON configuration; relative file paths are relative to the config."""
from dataclasses import dataclass
from datetime import date
from hashlib import sha256
from pathlib import Path
import json
import math
import re
import pandas as pd
from ..funktionen import validate_target_weights, validate_sma_windows


class ConfigError(ValueError):
    pass


def exact_keys(obj, required, optional=()):
    if not isinstance(obj, dict):
        raise ConfigError("Expected a JSON object.")
    missing, unknown = set(required) - obj.keys(), obj.keys() - set(required) - set(optional)
    if missing or unknown:
        raise ConfigError(f"Missing keys: {sorted(missing)}; unsupported keys: {sorted(unknown)}")


def iso_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ConfigError("Dates must use YYYY-MM-DD without time or timezone.")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ConfigError(f"Invalid date: {value}") from exc


def local_path(value, base):
    if not isinstance(value, str) or not value.strip() or "://" in value:
        raise ConfigError("A nonempty local file path is required; URLs are unsupported.")
    path = Path(value)
    return (path if path.is_absolute() else base / path).resolve()


@dataclass(frozen=True)
class RunConfig:
    schema_version: str
    run_name: str
    start: date
    end: date
    start_capital: float
    base_currency: str
    periods_per_year: float
    period_frequency: str | None
    market_path: Path
    assets_path: Path
    risk_free_path: Path | None
    risk_free_series: str | None
    asset: str | None
    output_dir: Path
    config_path: Path
    config_sha256: str
    buy_hold_enabled: bool = True
    rebalance_enabled: bool = False
    target_weights: tuple[tuple[str, float], ...] = ()
    rebalance_frequency: str | None = None
    trend_enabled: bool = False
    trend_asset: str | None = None
    short_window: int | None = None
    long_window: int | None = None
    signal_lag: int | None = None
    signal_source: str | None = None
    country_weighting_enabled: bool = False
    country_assets: tuple[tuple[str, str], ...] = ()
    gdp_indicator: str | None = None
    gdp_unit: str | None = None
    country_rebalance_frequency: str | None = None
    macro_path: Path | None = None

    @property
    def required_assets(self):
        assets = {self.asset} if self.buy_hold_enabled else set()
        if self.rebalance_enabled:
            assets.update(a for a, _ in self.target_weights)
        if self.trend_enabled:
            assets.add(self.trend_asset)
        if self.country_weighting_enabled:
            assets.update(asset for _, asset in self.country_assets)
        return tuple(sorted(assets))

    def country_params(self):
        return {"country_assets": dict(self.country_assets), "indicator": self.gdp_indicator,
                "unit": self.gdp_unit, "rebalance_frequency": self.country_rebalance_frequency}

    def trend_params(self):
        return {"asset": self.trend_asset, "short_window": self.short_window,
                "long_window": self.long_window, "signal_lag": self.signal_lag,
                "signal_source": self.signal_source}

    def strategies(self):
        strategies = {}
        if self.asset is not None:
            strategies["buy_hold"] = {"enabled": self.buy_hold_enabled, "asset": self.asset}
        if self.rebalance_frequency is not None:
            strategies["rebalance"] = {"enabled": self.rebalance_enabled,
                                       "target_weights": dict(self.target_weights),
                                       "rebalance_frequency": self.rebalance_frequency}
        if self.trend_asset is not None:
            strategies["trend"] = {"enabled": self.trend_enabled, **self.trend_params()}
        if self.country_rebalance_frequency is not None:
            strategies["country_weighting"] = {"enabled": self.country_weighting_enabled,
                                               **self.country_params()}
        return strategies

    def resolved(self):
        return {
            "schema_version": self.schema_version, "run_name": self.run_name,
            "period": {"start": self.start.isoformat(), "end": self.end.isoformat()},
            "start_capital": self.start_capital, "base_currency": self.base_currency,
            "periods_per_year": self.periods_per_year,
            "period_frequency": self.period_frequency,
            "data": {"market": str(self.market_path), "assets": str(self.assets_path),
                     "risk_free": None if self.risk_free_path is None else {
                         "path": str(self.risk_free_path), "series_id": self.risk_free_series},
                     **({"macro": str(self.macro_path)} if self.macro_path is not None else {})},
            "strategies": self.strategies(),
            "output_dir": str(self.output_dir),
        }


def load_config(path: str | Path) -> RunConfig:
    path = Path(path).resolve()
    content = path.read_bytes()
    def unique_object(pairs):
        obj = {}
        for key, value in pairs:
            if key in obj:
                raise ConfigError(f"Duplicate JSON key: {key}")
            obj[key] = value
        return obj
    def invalid_constant(value):
        raise ConfigError(f"Nonstandard JSON number: {value}")
    try:
        raw = json.loads(content.decode("utf-8-sig"), object_pairs_hook=unique_object,
                         parse_constant=invalid_constant)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ConfigError(f"Invalid JSON configuration: {exc}") from exc
    exact_keys(raw, ["schema_version", "run_name", "period", "start_capital",
                     "base_currency", "periods_per_year", "data", "strategies"],
               ["output_dir", "period_frequency"])
    if raw["schema_version"] != "1.0":
        raise ConfigError("Only schema_version 1.0 is supported.")
    if not isinstance(raw["run_name"], str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", raw["run_name"]):
        raise ConfigError("run_name must be a safe name of 1 to 64 characters.")
    exact_keys(raw["period"], ["start", "end"])
    start, end = (iso_date(raw["period"][k]) for k in ["start", "end"])
    if start > end:
        raise ConfigError("start must not be after end.")
    for key in ["start_capital", "periods_per_year"]:
        value = raw[key]
        try:
            valid = (not isinstance(value, bool) and isinstance(value, (int, float))
                     and math.isfinite(value) and value > 0)
        except OverflowError:
            valid = False
        if not valid:
            raise ConfigError(f"{key} must be a finite positive number.")
    currency = raw["base_currency"]
    if not isinstance(currency, str) or not re.fullmatch(r"[A-Z]{3}", currency):
        raise ConfigError("base_currency must be a three-letter uppercase code.")
    frequency = raw.get("period_frequency")
    if frequency is not None and (not isinstance(frequency, str)
                                  or frequency not in {"D", "W", "MS", "ME", "YS", "YE"}):
        raise ConfigError("Unsupported period_frequency. Use D, W, MS, ME, YS, YE or null.")
    exact_keys(raw["strategies"], [], ["buy_hold", "rebalance", "trend", "country_weighting"])
    buy_enabled = rebalance_enabled = False
    trend_enabled = False
    trend_asset = short_window = long_window = signal_lag = signal_source = None
    asset = rebalance_frequency = None
    target_weights = ()
    country_enabled = False
    country_assets = ()
    gdp_indicator = gdp_unit = country_frequency = None
    for name, params in raw["strategies"].items():
        required = {"buy_hold": ["enabled", "asset"],
                    "rebalance": ["enabled", "target_weights", "rebalance_frequency"],
                    "trend": ["enabled", "asset", "short_window", "long_window", "signal_lag", "signal_source"],
                    "country_weighting": ["enabled", "country_assets", "indicator", "unit", "rebalance_frequency"]}[name]
        exact_keys(params, required)
        if not isinstance(params["enabled"], bool):
            raise ConfigError("Strategy enabled must be a JSON boolean.")
        if name == "buy_hold":
            buy_enabled, asset = params["enabled"], params["asset"]
            if not isinstance(asset, str) or not asset.strip():
                raise ConfigError("Buy-and-Hold requires an explicit asset_id.")
        elif name == "rebalance":
            rebalance_enabled = params["enabled"]
            rebalance_frequency = params["rebalance_frequency"]
            if rebalance_frequency != "annual":
                raise ConfigError("Only annual rebalancing is supported.")
            weights = params["target_weights"]
            if (not isinstance(weights, dict) or not weights
                    or any(not isinstance(a, str) or not a.strip() for a in weights)
                    or any(isinstance(w, bool) or not isinstance(w, (int, float)) for w in weights.values())):
                raise ConfigError("target_weights must be a nonempty asset-to-number mapping.")
            try:
                validated = validate_target_weights(pd.Series(weights))
            except (ValueError, TypeError, OverflowError) as exc:
                raise ConfigError(f"Invalid target weights: {exc}") from exc
            target_weights = tuple(sorted(validated.items()))
        elif name == "trend":
            trend_enabled, trend_asset = params["enabled"], params["asset"]
            if not isinstance(trend_asset, str) or not trend_asset.strip():
                raise ConfigError("Trend requires an explicit asset_id.")
            short_window, long_window = params["short_window"], params["long_window"]
            try:
                validate_sma_windows(short_window, long_window)
            except ValueError as exc:
                raise ConfigError(str(exc)) from exc
            signal_lag, signal_source = params["signal_lag"], params["signal_source"]
            if type(signal_lag) is not int or signal_lag != 1:
                raise ConfigError("Trend signal_lag must be exactly integer 1.")
            if not isinstance(signal_source, str) or signal_source not in {"signal_value", "performance_value"}:
                raise ConfigError("Trend signal_source must explicitly select signal_value or performance_value.")
        else:
            country_enabled = params["enabled"]
            mapping = params["country_assets"]
            if (not isinstance(mapping, dict) or len(mapping) < 2
                    or any(not isinstance(c, str) or not c.strip() for c in mapping)
                    or any(not isinstance(a, str) or not a.strip() for a in mapping.values())):
                raise ConfigError("country_assets requires at least two explicit countries and asset proxies.")
            if len(set(mapping.values())) != len(mapping):
                raise ConfigError("Each country must have a unique asset proxy.")
            country_assets = tuple(sorted(mapping.items()))
            gdp_indicator, gdp_unit = params["indicator"], params["unit"]
            if any(not isinstance(v, str) or not v.strip() for v in [gdp_indicator, gdp_unit]):
                raise ConfigError("GDP indicator and unit must be explicit nonempty identifiers.")
            country_frequency = params["rebalance_frequency"]
            if country_frequency != "annual":
                raise ConfigError("Only annual country-weighting rebalancing is supported.")
    if not (buy_enabled or rebalance_enabled or trend_enabled or country_enabled):
        raise ConfigError("At least one supported strategy must be enabled.")
    data = raw["data"]
    exact_keys(data, ["market", "assets"], ["risk_free", "macro"])
    macro_path = local_path(data["macro"], path.parent) if "macro" in data else None
    if country_enabled and macro_path is None:
        raise ConfigError("Enabled country_weighting requires an explicit local data.macro path.")
    rf_path = rf_series = None
    if data.get("risk_free") is not None:
        exact_keys(data["risk_free"], ["path", "series_id"])
        rf_path = local_path(data["risk_free"]["path"], path.parent)
        rf_series = data["risk_free"]["series_id"]
        if not isinstance(rf_series, str) or not rf_series.strip():
            raise ConfigError("Risk-free series_id must be explicit.")
    output = local_path(raw["output_dir"], path.parent) if "output_dir" in raw else Path.cwd() / "outputs" / "runs"
    return RunConfig("1.0", raw["run_name"], start, end, float(raw["start_capital"]),
                     currency, float(raw["periods_per_year"]), frequency,
                     local_path(data["market"], path.parent), local_path(data["assets"], path.parent),
                     rf_path, rf_series, asset, output.resolve(), path, sha256(content).hexdigest(),
                     buy_enabled, rebalance_enabled, target_weights, rebalance_frequency,
                     trend_enabled, trend_asset, short_window, long_window, signal_lag, signal_source,
                     country_enabled, country_assets, gdp_indicator, gdp_unit, country_frequency, macro_path)
