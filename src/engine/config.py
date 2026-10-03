"""Strict JSON configuration; relative file paths are relative to the config."""
from dataclasses import dataclass
from datetime import date
from hashlib import sha256
from pathlib import Path
import json
import math
import re


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
    asset: str
    output_dir: Path
    config_path: Path
    config_sha256: str

    def resolved(self):
        return {
            "schema_version": self.schema_version, "run_name": self.run_name,
            "period": {"start": self.start.isoformat(), "end": self.end.isoformat()},
            "start_capital": self.start_capital, "base_currency": self.base_currency,
            "periods_per_year": self.periods_per_year,
            "period_frequency": self.period_frequency,
            "data": {"market": str(self.market_path), "assets": str(self.assets_path),
                     "risk_free": None if self.risk_free_path is None else {
                         "path": str(self.risk_free_path), "series_id": self.risk_free_series}},
            "strategies": {"buy_hold": {"enabled": True, "asset": self.asset}},
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
    exact_keys(raw["strategies"], ["buy_hold"])
    params = raw["strategies"]["buy_hold"]
    exact_keys(params, ["enabled", "asset"])
    if params["enabled"] is not True:
        raise ConfigError("This core requires an enabled Buy-and-Hold strategy.")
    if not isinstance(params["asset"], str) or not params["asset"].strip():
        raise ConfigError("Buy-and-Hold requires an explicit asset_id.")
    data = raw["data"]
    exact_keys(data, ["market", "assets"], ["risk_free"])
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
                     rf_path, rf_series, params["asset"], output.resolve(), path, sha256(content).hexdigest())
