from dataclasses import replace
import hashlib
import json
import math
from pathlib import Path
import socket
import subprocess
import sys
import numpy as np
import pandas as pd
import pytest
from maturarbeit_engine.engine.config import ConfigError, load_config
from maturarbeit_engine.engine.context import prepare_context
from maturarbeit_engine.engine.simulation import run_simulation
from maturarbeit_engine.data.normalize import align_performance
from maturarbeit_engine.data.validate import DataValidationError, validate_market, validate_assets


def run(case):
    return run_simulation(case["save"]())


def test_complete_slice_and_no_initial_return_in_statistics(case):
    outcome = run(case)
    h = outcome.result.portfolio_history
    assert h.portfolio_value.tolist() == pytest.approx([100, 110, 99])
    assert pd.isna(h.period_return.iloc[0])
    assert h.drawdown.tolist() == pytest.approx([0, 0, -.1])
    summary = pd.read_csv(outcome.output_path / "summary.csv").iloc[0]
    assert summary.start_value == 100
    assert summary.end_value == pytest.approx(99)
    assert summary.total_return == pytest.approx(-.01)
    assert summary.annualized_return == pytest.approx(.99 ** 6 - 1)
    assert summary.annualized_volatility == pytest.approx(math.sqrt(.02) * math.sqrt(12))
    excess = [.099, -.102]
    mean = sum(excess) / 2
    sigma = abs(excess[0] - excess[1]) / math.sqrt(2)
    assert summary.sharpe_ratio == pytest.approx(mean / sigma * math.sqrt(12))
    assert outcome.manifest["effective_period"] == {"start": "2020-01-31", "end": "2020-03-31"}
    assert outcome.manifest["requested_period"]["start"] == "2020-01-01"


def test_initial_loss_context(case):
    case["market"]["performance_value"] = [100, 90, 81]
    outcome = run(case)
    assert outcome.result.portfolio_history.drawdown.tolist() == pytest.approx([0, -.1, -.19])
    assert pd.read_csv(outcome.output_path / "summary.csv").max_drawdown.iloc[0] == pytest.approx(-.19)


@pytest.mark.parametrize("value", ["", "NaN", "inf", "-inf", "word", "0", "-1"])
def test_bad_market_values_reject_run(case, value):
    case["market"]["performance_value"] = ["100", value, "99"]
    with pytest.raises(DataValidationError):
        run(case)
    assert not (case["root"] / "runs").exists()


def test_duplicate_market_dates(case):
    case["market"].loc[1, "date"] = "2020-01-31"
    with pytest.raises(DataValidationError, match="Duplicate"):
        run(case)


@pytest.mark.parametrize("what", ["currency", "unknown_asset", "metadata_duplicate", "date", "missing_column"])
def test_invalid_data_contract(case, what):
    if what == "currency":
        case["assets"].loc[0, "currency"] = "USD"
    elif what == "unknown_asset":
        case["market"].loc[0, "asset_id"] = "UNKNOWN"
    elif what == "metadata_duplicate":
        case["assets"].loc[1] = case["assets"].iloc[0]
    elif what == "date":
        case["market"].loc[0, "date"] = "2020-02-31"
    else:
        case["market"].drop(columns="performance_value", inplace=True)
    with pytest.raises(DataValidationError):
        run(case)


@pytest.mark.parametrize("what", ["missing", "shifted_start", "nan", "inf", "duplicate", "wrong_series"])
def test_risk_free_must_match_whole_intervals(case, what):
    if what == "missing":
        case["rf"].drop(index=1, inplace=True)
    elif what == "shifted_start":
        case["rf"].loc[0, "period_start"] = "2020-01-30"
    elif what in {"nan", "inf"}:
        case["rf"]["period_return"] = ["NaN" if what == "nan" else "inf", ".002"]
    elif what == "duplicate":
        case["rf"].loc[2] = case["rf"].iloc[0]
    else:
        case["raw"]["data"]["risk_free"]["series_id"] = "NO_SERIES"
    with pytest.raises(DataValidationError):
        run(case)
    assert not (case["root"] / "runs").exists()


def test_no_risk_free_is_explicitly_unavailable(case):
    del case["raw"]["data"]["risk_free"]
    outcome = run(case)
    assert outcome.manifest["metric_status"]["sharpe_ratio"] == "risk_free_not_provided"
    assert pd.isna(pd.read_csv(outcome.output_path / "summary.csv").sharpe_ratio.iloc[0])


def test_only_one_real_return_has_undefined_sample_statistics(case):
    case["raw"]["period"]["end"] = "2020-02-29"
    outcome = run(case)
    summary = pd.read_csv(outcome.output_path / "summary.csv").iloc[0]
    assert pd.isna(summary.annualized_volatility) and pd.isna(summary.sharpe_ratio)
    assert summary.annualized_return == pytest.approx(1.1 ** 12 - 1)


def test_constant_excess_returns_export_null_status(case):
    case["market"]["performance_value"] = [100., 100., 100.]
    case["rf"]["period_return"] = [0., 0.]
    outcome = run(case)
    assert outcome.manifest["metric_status"]["sharpe_ratio"] == "insufficient_sample_or_zero_excess_volatility"
    summary = pd.read_csv(outcome.output_path / "summary.csv").iloc[0]
    assert summary.annualized_volatility == 0 and pd.isna(summary.sharpe_ratio)


@pytest.mark.parametrize("what", ["missing_frequency", "incompatible_m", "irregular"])
def test_unverified_period_logic_never_silently_annualizes(case, what):
    if what == "missing_frequency":
        del case["raw"]["period_frequency"]
    elif what == "incompatible_m":
        case["raw"]["periods_per_year"] = 252
    else:
        case["market"].loc[1, "date"] = "2020-02-28"
        case["rf"].loc[0, "period_end"] = "2020-02-28"
        case["rf"].loc[1, "period_start"] = "2020-02-28"
    outcome = run(case)
    summary = pd.read_csv(outcome.output_path / "summary.csv").iloc[0]
    assert pd.isna(summary.annualized_return) and pd.isna(summary.annualized_volatility) and pd.isna(summary.sharpe_ratio)
    assert summary.total_return == pytest.approx(-.01)
    assert outcome.manifest["metric_status"]["annualized_return"] != "available"


def test_multi_asset_alignment_precedes_returns_and_reports_removed_dates(case):
    other = case["market"].copy()
    other["asset_id"] = "SYNTH_B"
    other.loc[1, "date"] = "2020-02-28"
    market = pd.concat([case["market"], other], ignore_index=True)
    metadata = pd.concat([case["assets"], case["assets"].assign(asset_id="SYNTH_B")], ignore_index=True)
    validated = validate_market(market, validate_assets(metadata), ("SYNTH_A", "SYNTH_B"), "CHF")
    wide, quality = align_performance(validated, ("SYNTH_A", "SYNTH_B"), "2020-01-01", "2020-03-31")
    assert len(wide) == 2 and not wide.isna().any().any()
    assert quality["series"]["SYNTH_A"]["removed_non_common_dates"] == ["2020-02-29"]
    assert quality["series"]["SYNTH_B"]["removed_non_common_dates"] == ["2020-02-28"]
    assert (wide.iloc[1] / wide.iloc[0] - 1).tolist() == pytest.approx([-.01, -.01])


def test_unneeded_asset_does_not_change_selected_strategy(case):
    other = case["market"].copy().assign(asset_id="SYNTH_B", performance_value=[200., 400., 600.])
    case["market"] = pd.concat([case["market"], other], ignore_index=True)
    case["assets"] = pd.concat([case["assets"], case["assets"].assign(asset_id="SYNTH_B")], ignore_index=True)
    assert run(case).result.portfolio_history.portfolio_value.tolist() == pytest.approx([100, 110, 99])


def test_reproducible_csv_files_and_hashes(case):
    one, two = run(case), run(case)
    assert one.output_path != two.output_path
    for name in ["portfolio_history.csv", "summary.csv", "data_quality.json"]:
        assert (one.output_path / name).read_bytes() == (two.output_path / name).read_bytes()
    def reject_constant(value):
        raise AssertionError(f"Nonstandard JSON value {value}")
    manifest = json.loads((one.output_path / "run_manifest.json").read_text(encoding="utf-8"), parse_constant=reject_constant)
    assert manifest["timestamp_utc"].endswith("+00:00")
    assert manifest["code"]["files"] and len(manifest["code"]["sha256"]) == 64
    for item in manifest["results"]:
        assert hashlib.sha256((one.output_path / item["path"]).read_bytes()).hexdigest() == item["sha256"]
    for item in manifest["input_files"]:
        assert hashlib.sha256(Path(item["path"]).read_bytes()).hexdigest() == item["sha256"]
    quality = json.loads((one.output_path / "data_quality.json").read_text(encoding="utf-8"), parse_constant=reject_constant)
    assert quality["validation_status"] == "passed" and quality["used_observations"] == 3
    assert one.manifest["code"]["sha256"] == two.manifest["code"]["sha256"]


def test_future_prices_do_not_change_earlier_results(case):
    first = run(case).result.portfolio_history
    case["market"].loc[2, "performance_value"] = 200
    second = run(case).result.portfolio_history
    pd.testing.assert_frame_equal(first.iloc[:2], second.iloc[:2])


def test_backtest_completes_under_network_guard(case):
    with pytest.raises(AssertionError, match="Network"):
        socket.create_connection(("example.invalid", 443))
    assert run(case).output_path.is_dir()


def test_cli_uses_installed_package_from_other_directory(case):
    path = case["save"]()
    command = [sys.executable, "-m", "maturarbeit_engine", "run", "--config", str(path)]
    result = subprocess.run(command, cwd=case["root"], capture_output=True, text=True, timeout=30)
    assert result.returncode == 0, result.stderr
    output = Path(result.stdout.strip())
    assert output.is_dir() and (output / "run_manifest.json").is_file()


@pytest.mark.parametrize("key", ["schema_version", "run_name", "period", "start_capital", "base_currency", "periods_per_year", "data", "strategies"])
def test_missing_required_config(case, key):
    del case["raw"][key]
    with pytest.raises(ConfigError):
        load_config(case["save"]())


@pytest.mark.parametrize("what", ["unknown", "bad_version", "negative_capital", "bool_capital", "zero_periods", "inverted", "unknown_strategy", "unsupported_option", "url", "bad_frequency"])
def test_invalid_config(case, what):
    r = case["raw"]
    if what == "unknown": r["secret"] = "not_allowed"
    elif what == "bad_version": r["schema_version"] = "2.0"
    elif what == "negative_capital": r["start_capital"] = -1
    elif what == "bool_capital": r["start_capital"] = True
    elif what == "zero_periods": r["periods_per_year"] = 0
    elif what == "inverted": r["period"]["end"] = "2019-01-01"
    elif what == "unknown_strategy": r["strategies"]["trend"] = {"enabled": False}
    elif what == "unsupported_option": r["strategies"]["buy_hold"]["weight"] = .8
    elif what == "url": r["data"]["market"] = "https://example.invalid/market.csv"
    else: r["period_frequency"] = "intraday"
    with pytest.raises(ConfigError):
        load_config(case["save"]())


def test_duplicate_or_nonstandard_json_rejected(case):
    path = case["root"] / "config.json"
    for text in ['{"x": 1, "x": 2}', '{"x": NaN}', '{"x": Infinity}']:
        path.write_text(text, encoding="utf-8")
        with pytest.raises(ConfigError):
            load_config(path)


def test_missing_file_and_no_observed_period(case):
    case["raw"]["data"]["market"] = "absent.csv"
    with pytest.raises(OSError):
        run(case)
    case["raw"]["data"]["market"] = "market.csv"
    case["raw"]["period"]["start"] = "2020-03-01"
    with pytest.raises(DataValidationError):
        run(case)


@pytest.mark.parametrize("key,value", [("period_frequency", []), ("period_frequency", {}),
                                      ("start_capital", 10 ** 400), ("periods_per_year", "12")])
def test_malformed_parameter_types_fail_as_config_errors(case, key, value):
    case["raw"][key] = value
    with pytest.raises(ConfigError):
        load_config(case["save"]())


def test_python_config_object_cannot_bypass_validation(case):
    config = load_config(case["save"]())
    assert run_simulation(config).result.portfolio_history.portfolio_value.iloc[-1] == pytest.approx(99)
    with pytest.raises(ConfigError):
        run_simulation(replace(config, start_capital=-1))


def test_extra_overlapping_risk_free_interval_rejected(case):
    case["rf"].loc[2] = ["2020-01-31", "2020-03-31", "SYNTH_RF", .003]
    with pytest.raises(DataValidationError, match="overlap"):
        run(case)


def test_duplicate_csv_header_rejected(case):
    path = case["save"]()
    (case["root"] / "market.csv").write_text(
        "date,asset_id,performance_value,performance_value\n2020-01-31,SYNTH_A,100,200\n",
        encoding="utf-8")
    with pytest.raises(DataValidationError, match="Duplicate CSV"):
        run_simulation(path)


def test_input_edit_after_reading_prevents_export(case, monkeypatch):
    from maturarbeit_engine.engine import simulation
    original = simulation.export_run
    def edit_then_export(context, *args):
        context.config.market_path.write_text("changed", encoding="utf-8")
        return original(context, *args)
    monkeypatch.setattr(simulation, "export_run", edit_then_export)
    with pytest.raises(ValueError, match="Input changed"):
        run(case)
    assert not (case["root"] / "runs").exists()
