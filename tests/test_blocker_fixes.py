"""Independent counterexamples and export-boundary regressions for EB-01 through EB-03."""
from dataclasses import replace
import csv
from io import StringIO
import json
from pathlib import Path
import shutil
import numpy as np
import pandas as pd
import pytest
from maturarbeit_engine.funktionen import allocate_target_values, rebalancing
from maturarbeit_engine.data.normalize import read_csv_snapshot
from maturarbeit_engine.data.validate import DataValidationError
from maturarbeit_engine.engine.config import load_config
from maturarbeit_engine.engine.context import prepare_context
from maturarbeit_engine.engine.result import validate_results
from maturarbeit_engine.engine.simulation import run_simulation
from maturarbeit_engine.strategies.buy_hold import BuyAndHold
from maturarbeit_engine.strategies.rebalance import Rebalance
from maturarbeit_engine.strategies.trend import Trend
from maturarbeit_engine.strategies.country_weighting import CountryWeighting
from maturarbeit_engine.analysis.metrics import compute_run_metrics
from maturarbeit_engine.export.results import export_run


@pytest.fixture
def demo(tmp_path):
    """Copy the existing artificial CSV inputs; never write to repository demos."""
    def prepare(name, *, flat=False, frequency=None, declare_frequency=True):
        source = Path(__file__).resolve().parents[1] / "configs" / f"demo_{name}.json"
        raw = json.loads(source.read_text(encoding="utf-8"))
        folder = tmp_path / name
        folder.mkdir(exist_ok=True)
        for key in ["market", "assets", "macro"]:
            if key in raw["data"]:
                shutil.copyfile(source.parent / raw["data"][key], folder / f"{key}.csv")
                raw["data"][key] = f"{key}.csv"
        shutil.copyfile(source.parent / raw["data"]["risk_free"]["path"], folder / "rf.csv")
        raw["data"]["risk_free"]["path"] = "rf.csv"
        raw["output_dir"] = "runs"
        if flat:
            market = pd.read_csv(folder / "market.csv")
            market["performance_value"] = 100.
            market.to_csv(folder / "market.csv", index=False)
        if not declare_frequency:
            raw["period_frequency"] = frequency
        path = folder / "config.json"
        path.write_text(json.dumps(raw), encoding="utf-8")
        return prepare_context(load_config(path)), path
    return prepare


def strategy_results(context):
    cfg = context.config
    results = []
    if cfg.buy_hold_enabled:
        results.append(BuyAndHold().run(context, {"asset": cfg.asset}))
    if cfg.rebalance_enabled:
        results.append(Rebalance().run(context, {"target_weights": dict(cfg.target_weights),
                                                 "rebalance_frequency": "annual"}))
    if cfg.trend_enabled:
        results.append(Trend().run(context, cfg.trend_params()))
    if cfg.country_weighting_enabled:
        results.append(CountryWeighting().run(context, cfg.country_params()))
    return sorted(results, key=lambda result: result.strategy)


def rejected_export(context, results, *, summary=None, status=None, match=None):
    if summary is None or status is None:
        calculated, calculated_status = compute_run_metrics(results, context)
        summary = calculated if summary is None else summary
        status = calculated_status if status is None else status
    with pytest.raises(ValueError, match=match):
        export_run(context, results, summary, status)
    assert not context.config.output_dir.exists(), "Invalid runs must not be published or staged."


@pytest.mark.parametrize("enabled", ["rebalance", "country_weighting", "both"])
def test_exact_audit_initial_allocation_underflow_aborts_run(tmp_path, enabled):
    (tmp_path / "market.csv").write_text(
        "date,asset_id,performance_value\n2020-01-31,A,1\n2020-01-31,B,1\n"
        "2020-02-29,A,1e300\n2020-02-29,B,1\n", encoding="utf-8")
    (tmp_path / "assets.csv").write_text(
        "asset_id,name,asset_class,country,currency,provider,provider_symbol\n"
        "A,Artificial A,synthetic,C_A,CHF,synthetic,A\n"
        "B,Artificial B,synthetic,C_B,CHF,synthetic,B\n", encoding="utf-8")
    (tmp_path / "macro.csv").write_text(
        "period,country,indicator,value,unit,available_from\n"
        "2019,C_A,GDP,1e-200,UNITS,2020-01-01\n"
        "2019,C_B,GDP,1,UNITS,2020-01-01\n", encoding="utf-8")
    raw = {"schema_version": "1.0", "run_name": "audit_underflow",
           "period": {"start": "2020-01-31", "end": "2020-02-29"},
           "start_capital": 1e-200, "base_currency": "CHF", "periods_per_year": 12,
           "period_frequency": None, "data": {"market": "market.csv", "assets": "assets.csv", "macro": "macro.csv"},
           "strategies": {
               "rebalance": {"enabled": enabled in {"rebalance", "both"}, "target_weights": {"A": 1e-200, "B": 1}, "rebalance_frequency": "annual"},
               "country_weighting": {"enabled": enabled in {"country_weighting", "both"},
                                     "country_assets": {"C_A": "A", "C_B": "B"}, "indicator": "GDP", "unit": "UNITS", "rebalance_frequency": "annual"}},
           "output_dir": "runs"}
    path = tmp_path / "config.json"
    path.write_text(json.dumps(raw), encoding="utf-8")
    with pytest.raises(ValueError, match="Positive target allocation underflowed"):
        run_simulation(path)
    assert not (tmp_path / "runs").exists()


def test_exact_audit_rebalancing_helper_underflow():
    with pytest.raises(ValueError, match="underflowed"):
        rebalancing(pd.Series({"A": 0., "B": 1e-200}), pd.Series({"A": 1e-200, "B": 1.}))


@pytest.mark.parametrize("capital", [1e-200, 100., 1e200])
def test_exact_zero_target_is_allowed_and_preserves_capital(capital):
    targets = pd.Series({"A": 0., "B": 1.})
    initial = allocate_target_values(capital, targets)
    assert initial.A == 0. and initial.B == capital
    after = rebalancing(pd.Series({"A": capital * .5, "B": capital * .5}), targets)
    assert after[3].A == 0. and after[3].B == capital
    assert abs(after[4].sum()) <= capital * 1e-12


@pytest.mark.parametrize("strategy", ["rebalance", "country_weighting"])
def test_annual_allocation_underflow_aborts_for_both_portfolios(demo, strategy):
    context, path = demo("country_weighting")
    # Start positions are representable; only the later target allocation must underflow.
    raw = json.loads(path.read_text(encoding="utf-8"))
    raw["start_capital"] = 1e-200
    raw["strategies"] = {strategy: raw["strategies"][strategy]}
    if strategy == "rebalance":
        # Shrink the dominant B position; held A remains positive until it is reallocated.
        raw["strategies"][strategy]["target_weights"] = {"ASSET_A": 1e-120, "ASSET_B": 1.}
        market = pd.read_csv(path.parent / "market.csv")
        market["performance_value"] = market.performance_value.astype(float)
        market.loc[(market.date >= "2020-06-30") & (market.asset_id == "ASSET_B"), "performance_value"] = 1e-10
        market.to_csv(path.parent / "market.csv", index=False)
    else:
        macro = pd.read_csv(path.parent / "macro.csv")
        macro["value"] = macro.value.astype(float)
        macro.loc[(macro.period == 2019) & (macro.country == "COUNTRY_A") & (macro.available_from <= "2020-12-30"), "value"] = 1e-200
        macro.to_csv(path.parent / "macro.csv", index=False)
    path.write_text(json.dumps(raw), encoding="utf-8")
    with pytest.raises(ValueError, match="Positive target allocation underflowed"):
        run_simulation(path)
    assert not context.config.output_dir.exists()


@pytest.mark.parametrize("index", [1, -1])
def test_drawdown_manipulation_at_middle_or_end_prevents_export(demo, index):
    context, _ = demo("buy_hold")
    result = strategy_results(context)[0]
    summary, status = compute_run_metrics([result], context)
    history = result.portfolio_history.copy()
    history.iloc[index, history.columns.get_loc("drawdown")] = .75
    rejected_export(context, [replace(result, portfolio_history=history)], summary=summary, status=status, match="drawdown")


@pytest.mark.parametrize("column,value", [
    ("start_value", 101.), ("end_value", 999.), ("total_return", .5),
    ("annualized_return", .5), ("annualized_volatility", .5),
    ("sharpe_ratio", np.inf), ("sharpe_ratio", np.nan),
    ("sharpe_ratio", .5), ("max_drawdown", -.5), ("annualized_return", np.nan)])
def test_each_summary_metric_is_checked_before_export(demo, column, value):
    context, _ = demo("buy_hold")
    results = strategy_results(context)
    summary, status = compute_run_metrics(results, context)
    summary.loc[0, column] = value
    rejected_export(context, results, summary=summary, status=status, match="Summary metric")


@pytest.mark.parametrize("kind", ["columns", "extra_column", "strategy", "duplicate_row", "missing_row"])
def test_summary_structure_and_strategy_assignment(demo, kind):
    context, _ = demo("buy_hold")
    results = strategy_results(context)
    summary, status = compute_run_metrics(results, context)
    if kind == "columns": summary = summary.drop(columns="max_drawdown")
    elif kind == "extra_column": summary["extra"] = 1.
    elif kind == "strategy": summary.loc[0, "strategy"] = "other"
    elif kind == "duplicate_row": summary = pd.concat([summary, summary])
    else: summary = summary.iloc[:0]
    rejected_export(context, results, summary=summary, status=status, match="Summary")


@pytest.mark.parametrize("column", ["annualized_return", "annualized_volatility", "sharpe_ratio"])
def test_unavailable_metric_cannot_be_exported_as_zero(demo, column):
    context, _ = demo("buy_hold", declare_frequency=False)
    results = strategy_results(context)
    summary, status = compute_run_metrics(results, context)
    assert pd.isna(summary.loc[0, column])
    summary.loc[0, column] = 0.
    rejected_export(context, results, summary=summary, status=status, match="Unavailable summary metric")


@pytest.mark.parametrize("name", ["buy_hold", "country_weighting"])
def test_wrong_availability_status_rejected_for_single_and_multiple_strategies(demo, name):
    context, _ = demo(name)
    results = strategy_results(context)
    summary, status = compute_run_metrics(results, context)
    status["invented"] = "not_available"
    rejected_export(context, results, summary=summary, status=status, match="availability status")


def test_missing_enabled_strategy_is_rejected_only_at_complete_run_boundary(demo):
    context, _ = demo("country_weighting")
    results = strategy_results(context)
    subset = [result for result in results if result.strategy != "rebalance"]
    assert len(validate_results(context, subset)) == 3
    rejected_export(context, subset, match="enabled strategies")


def test_additional_disabled_strategy_rejected(demo):
    context, _ = demo("buy_hold")
    result = strategy_results(context)[0]
    history = result.portfolio_history.assign(strategy="unexpected")
    results = [result, replace(result, strategy="unexpected", portfolio_history=history)]
    rejected_export(context, results, match="enabled strategies")


@pytest.mark.parametrize("identical_prices", [False, True])
def test_buy_hold_asset_identity_is_bound_even_if_prices_are_identical(demo, identical_prices):
    context, _ = demo("rebalance", flat=identical_prices)
    results = strategy_results(context)
    results[0] = BuyAndHold().run(context, {"asset": "BD_SYNTH"})
    rejected_export(context, results, match="result asset differs")


def test_forged_buy_hold_asset_marker_does_not_hide_wrong_returns(demo):
    context, _ = demo("rebalance")
    results = strategy_results(context)
    wrong = BuyAndHold().run(context, {"asset": "BD_SYNTH"})
    results[0] = replace(wrong, asset_id="EQ_SYNTH")
    rejected_export(context, results, match="returns differ")


@pytest.mark.parametrize("weights", [{"EQ_SYNTH": .2, "BD_SYNTH": .8}, {"EQ_SYNTH": 1.}])
def test_fixed_targets_and_asset_set_match_manifest_config(demo, weights):
    context, _ = demo("rebalance")
    results = strategy_results(context)
    results[1] = Rebalance().run(context, {"target_weights": weights, "rebalance_frequency": "annual"})
    rejected_export(context, results, match="differ from configuration")


@pytest.mark.parametrize("kind", ["missing", "extra", "initial", "terminal"])
def test_fixed_annual_events_are_required_even_for_zero_transactions(demo, kind):
    context, _ = demo("rebalance", flat=True)
    results = strategy_results(context)
    result = results[1]
    trades = result.trades.copy()
    assert (trades.transaction_value == 0).all()
    if kind == "missing":
        trades = trades.iloc[:0]
    else:
        extra = trades.copy()
        extra["date"] = context.performance.index[{"extra": 1, "initial": 0, "terminal": -1}[kind]]
        trades = pd.concat([trades, extra], ignore_index=True)
    results[1] = replace(result, trades=trades)
    rejected_export(context, results)


def test_existing_config_target_tolerance_is_not_tightened(demo):
    context, _ = demo("rebalance")
    results = strategy_results(context)
    weights = {"EQ_SYNTH": .6 + 5e-13, "BD_SYNTH": .4 - 5e-13}
    results[1] = Rebalance().run(context, {"target_weights": weights, "rebalance_frequency": "annual"})
    summary, status = compute_run_metrics(results, context)
    assert export_run(context, results, summary, status)[0].is_dir()


@pytest.mark.parametrize("name", ["buy_hold", "rebalance", "trend", "country_weighting"])
def test_correct_demo_runner_succeeds_with_complete_contract(demo, name):
    _, path = demo(name)
    assert run_simulation(path).output_path.is_dir()


def test_exact_audit_overwide_csv_rejected(case):
    path = case["save"]()
    (case["root"] / "market.csv").write_text(
        "date,asset_id,performance_value\n"
        "2019-12-31,2020-01-31,SYNTH_A,100\n"
        "2020-01-31,2020-02-29,SYNTH_A,110\n"
        "2020-02-29,2020-03-31,SYNTH_A,99\n", encoding="utf-8")
    with pytest.raises(DataValidationError, match="expected 3, got 4"):
        run_simulation(path)
    assert not (case["root"] / "runs").exists()


@pytest.mark.parametrize("kind,filename", [("market", "market.csv"), ("assets", "assets.csv"),
                                          ("risk_free", "rf.csv"), ("macro", "macro.csv")])
@pytest.mark.parametrize("width_change", [-1, 1])
def test_every_input_file_rejects_missing_and_extra_fields(demo, kind, filename, width_change):
    context, path = demo("country_weighting")
    target = path.parent / filename
    rows = list(csv.reader(StringIO(target.read_text(encoding="utf-8"))))
    if width_change == 1: rows[1].append("unlabelled")
    else: rows[1].pop()
    buffer = StringIO()
    csv.writer(buffer, lineterminator="\n").writerows(rows)
    target.write_text(buffer.getvalue(), encoding="utf-8")
    with pytest.raises(DataValidationError, match="CSV field count mismatch"):
        run_simulation(path)
    assert not context.config.output_dir.exists()


def test_quoted_comma_and_multiline_fields_and_named_additional_columns_are_preserved(tmp_path):
    path = tmp_path / "quoted.csv"
    path.write_bytes(b'asset_id,name,extra\nA,"Artificial, quoted name","line one\nline two"\n')
    frame, _ = read_csv_snapshot(path, "assets")
    assert frame.index.equals(pd.RangeIndex(1))
    assert frame.iloc[0].tolist() == ["A", "Artificial, quoted name", "line one\nline two"]


def test_quoted_asset_name_with_comma_remains_valid_in_full_runner(case):
    case["assets"].loc[0, "name"] = "Artificial, quoted name"
    case["market"]["additional_named_column"] = ["x,y", "z", "w"]
    assert run_simulation(case["save"]()).output_path.is_dir()


@pytest.mark.parametrize("content", ["a,a\n1,2\n", "a,\n1,2\n", 'a,b\n1,"unclosed\n', "a,b\n\n"])
def test_duplicate_unnamed_malformed_or_empty_csv_rows_are_rejected(tmp_path, content):
    path = tmp_path / "invalid.csv"
    path.write_text(content, encoding="utf-8")
    with pytest.raises(DataValidationError):
        read_csv_snapshot(path, "market")
