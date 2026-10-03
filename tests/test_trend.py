"""Independent SMA, lag and portfolio controls; all values are artificial."""
from dataclasses import replace
from pathlib import Path
import hashlib
import json
import math
import subprocess
import sys
import numpy as np
import pandas as pd
import pytest
from maturarbeit_engine.funktionen import sma_signal, trendfolge
from maturarbeit_engine.engine.config import ConfigError, load_config
from maturarbeit_engine.engine.context import prepare_context
from maturarbeit_engine.engine.result import SIGNALS_COLUMNS, validate_results
from maturarbeit_engine.engine.simulation import run_simulation
from maturarbeit_engine.data.validate import DataValidationError
from maturarbeit_engine.strategies.buy_hold import BuyAndHold
from maturarbeit_engine.strategies.rebalance import Rebalance
from maturarbeit_engine.strategies.trend import Trend

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def trend_case(tmp_path):
    c = {"root": tmp_path, "raw": json.loads((ROOT / "configs/demo_trend.json").read_text(encoding="utf-8"))}
    for name in ["market", "assets", "risk_free"]:
        c[name] = pd.read_csv(ROOT / "configs/trend_demo" / (name + ".csv"), dtype=str, keep_default_na=False)
    c["raw"]["data"] = {"market": "market.csv", "assets": "assets.csv",
                        "risk_free": {"path": "risk_free.csv", "series_id": "RF_SYNTHETIC"}}
    c["raw"]["output_dir"] = "runs"
    def save():
        for name in ["market", "assets", "risk_free"]:
            c[name].to_csv(tmp_path / (name + ".csv"), index=False)
        path = tmp_path / "config.json"
        path.write_text(json.dumps(c["raw"], allow_nan=False), encoding="utf-8")
        return path
    c["save"] = save
    return c


def run(c):
    return run_simulation(c["save"]())


def change(c, date, column, value):
    c["market"].loc[(c["market"].asset_id == "TREND_SYNTH") & (c["market"].date == date), column] = value


def test_independent_sma_lag_returns_wealth_drawdown_and_metrics(trend_case):
    out = run(trend_case)
    h, s = out.results["trend"].portfolio_history, out.results["trend"].signals
    assert h.portfolio_value.tolist() == pytest.approx([100, 100, 110, 88, 88, 88, 96.8])
    assert pd.isna(h.period_return.iloc[0]) and h.drawdown.iloc[0] == 0
    returns = [0, .1, -.2, 0, 0, .1]
    assert h.period_return.iloc[1:].tolist() == pytest.approx(returns)
    assert h.drawdown.tolist() == pytest.approx([0, 0, 0, -.2, -.2, -.2, -.12])
    assert s.signal_value.tolist() == [10, 20, 30, 10, 10, 30, 30]
    assert s.sma_short.tolist() == pytest.approx([10, 15, 25, 20, 10, 20, 30])
    assert s.sma_long.tolist() == pytest.approx([10, 40/3, 20, 20, 50/3, 50/3, 70/3])
    assert s.signal.tolist() == [0, 1, 1, 0, 0, 1, 1]
    assert pd.isna(s.position.iloc[0])
    assert s.position.iloc[1:].tolist() == [0, 1, 1, 0, 0, 1]
    # Feb signal 1 does not earn Feb's -20%; Apr signal 0 does earn Apr's -20% with prior Long.
    assert h.period_return.iloc[1] == 0 and h.period_return.iloc[3] == pytest.approx(-.2)
    # Both +100% in May and -50% in June earn zero in Cash, despite nonzero RF.
    assert h.period_return.iloc[4] == h.period_return.iloc[5] == 0
    summary = pd.read_csv(out.output_path / "summary.csv").set_index("strategy")
    row = summary.loc["trend"]
    assert row.total_return == pytest.approx(-.032)
    assert row.annualized_return == pytest.approx(.968**2 - 1)
    assert row.annualized_volatility == pytest.approx(math.sqrt(.06/5) * math.sqrt(12))
    excess = [r - rf for r, rf in zip(returns, [.001, .002, .001, .002, .001, .002])]
    mean = sum(excess)/6
    std = math.sqrt(sum((x-mean)**2 for x in excess)/5)
    assert row.sharpe_ratio == pytest.approx(mean/std * math.sqrt(12))
    assert row.max_drawdown == pytest.approx(-.2)
    assert summary.loc["buy_hold", "end_value"] == pytest.approx(77.44)
    assert summary.loc["rebalance", "end_value"] == pytest.approx(86.464)


def test_signals_export_contract_order_hash_and_provenance(trend_case):
    one, two = run(trend_case), run(trend_case)
    assert len(list(one.output_path.iterdir())) == 7
    s = pd.read_csv(one.output_path / "signals.csv")
    assert list(s.columns) == SIGNALS_COLUMNS
    assert s.date.tolist() == ["2020-01-31", "2020-02-29", "2020-03-31", "2020-04-30", "2020-05-31", "2020-06-30", "2020-07-31"]
    assert s.iloc[0].isna().sum() == 1 and pd.isna(s.position.iloc[0])
    assert not s[["signal_value", "sma_short", "sma_long", "signal"]].isna().any().any()
    assert s.position.iloc[1:].tolist() == s.signal.iloc[:-1].tolist()
    assert set(s.signal) == {0, 1}
    pd.testing.assert_frame_equal(s, s.sort_values(["strategy", "date", "asset_id"], kind="stable").reset_index(drop=True))
    for item in one.manifest["results"]:
        data = (one.output_path / item["path"]).read_bytes()
        assert hashlib.sha256(data).hexdigest() == item["sha256"]
        assert data == (two.output_path / item["path"]).read_bytes()
    assert one.manifest["executed_strategies"] == ["buy_hold", "rebalance", "trend"]
    config = one.manifest["config"]["strategies"]["trend"]
    assert config == trend_case["raw"]["strategies"]["trend"]
    quality = json.loads((one.output_path / "data_quality.json").read_text(encoding="utf-8"))["trend"]
    assert quality["available_warm_up_observations"] == quality["used_warm_up_observations"] == 2
    assert quality["long_window"] == 3 and quality["valid_start_signal"] is True
    assert quality["warm_up_period"] == {"start": "2019-11-30", "end": "2019-12-31"}
    assert quality["effective_start"] == "2020-01-31"
    assert "signal_value" not in json.loads((one.output_path / "data_quality.json").read_text(encoding="utf-8"))["unused_market_columns"]


@pytest.mark.parametrize("short,long", [(0,3), (-1,3), (1,0), (1,-1), (3,3), (4,3),
                                      (True,3), (1,True), (1.0,3), (1,3.0), ("2",3), (1,None)])
def test_invalid_windows_in_config_and_shared_helper(trend_case, short, long):
    p = trend_case["raw"]["strategies"]["trend"]
    p["short_window"], p["long_window"] = short, long
    with pytest.raises(ConfigError):
        run(trend_case)
    with pytest.raises(ValueError):
        sma_signal(pd.Series([10.,20.,30.]), short, long)
    assert not (trend_case["root"] / "runs").exists()


@pytest.mark.parametrize("key", ["enabled", "asset", "short_window", "long_window", "signal_lag", "signal_source"])
def test_no_missing_trend_parameters_or_defaults(trend_case, key):
    del trend_case["raw"]["strategies"]["trend"][key]
    with pytest.raises(ConfigError):
        run(trend_case)


@pytest.mark.parametrize("lag", [0, 2, -1, True, 1.0, "1", None])
def test_lag_must_be_exactly_integer_one(trend_case, lag):
    trend_case["raw"]["strategies"]["trend"]["signal_lag"] = lag
    with pytest.raises(ConfigError):
        run(trend_case)


@pytest.mark.parametrize("source", ["auto", "close", "", None, [], True])
def test_unknown_signal_source_rejected(trend_case, source):
    trend_case["raw"]["strategies"]["trend"]["signal_source"] = source
    with pytest.raises(ConfigError):
        run(trend_case)


def test_insufficient_warm_up_rejects_entire_run(trend_case):
    trend_case["market"] = trend_case["market"].loc[trend_case["market"].date != "2019-12-31"]
    with pytest.raises(DataValidationError, match="warm-up"):
        run(trend_case)
    assert not (trend_case["root"] / "runs").exists()


def test_extra_older_signal_observation_is_not_used_as_performance(trend_case):
    baseline = run(trend_case)
    c = trend_case
    c["market"] = pd.concat([c["market"], pd.DataFrame([{"date": "2019-10-31", "asset_id": "TREND_SYNTH",
                          "performance_value": "1", "signal_value": "invalid_unused"}])], ignore_index=True)
    extra = run(c)
    for name in baseline.results:
        pd.testing.assert_frame_equal(baseline.results[name].portfolio_history, extra.results[name].portfolio_history)
    pd.testing.assert_frame_equal(baseline.results["trend"].signals, extra.results["trend"].signals)
    quality = json.loads((extra.output_path / "data_quality.json").read_text(encoding="utf-8"))["trend"]
    assert quality["available_warm_up_observations"] == 3 and quality["used_warm_up_observations"] == 2


@pytest.mark.parametrize("date", ["2019-12-31", "2020-03-31"])
@pytest.mark.parametrize("bad", ["", "NaN", "Inf", "-Inf", "word"])
def test_required_warm_up_and_study_signals_never_filled_or_dropped(trend_case, date, bad):
    change(trend_case, date, "signal_value", bad)
    with pytest.raises(DataValidationError):
        run(trend_case)
    assert not (trend_case["root"] / "runs").exists()


def test_missing_signal_column_has_no_fallback(trend_case):
    trend_case["market"] = trend_case["market"].drop(columns="signal_value")
    with pytest.raises(DataValidationError, match="signal source"):
        run(trend_case)


def test_performance_source_is_explicit_and_ignores_unused_signal_column(trend_case):
    c = trend_case
    c["raw"]["strategies"]["trend"]["signal_source"] = "performance_value"
    c["market"] = c["market"].drop(columns="signal_value")
    out = run(c)
    s = out.results["trend"].signals
    assert s.signal_value.tolist() == pytest.approx([100,80,88,70.4,140.8,70.4,77.44])
    assert s.sma_short.iloc[0] == 95 and s.sma_long.iloc[0] == 90 and s.signal.iloc[0] == 1
    assert out.results["trend"].portfolio_history.portfolio_value.iloc[1] == pytest.approx(80)
    c["market"]["signal_value"] = "not_used"
    second = run(c)
    pd.testing.assert_frame_equal(out.results["trend"].portfolio_history, second.results["trend"].portfolio_history)
    pd.testing.assert_frame_equal(s, second.results["trend"].signals)
    assert second.manifest["config"]["strategies"]["trend"]["signal_source"] == "performance_value"


def test_change_only_signal_changes_positions_not_market_returns(trend_case):
    first = run(trend_case)
    change(trend_case, "2020-02-29", "signal_value", "1")
    second = run(trend_case)
    assert first.results["trend"].signals.signal.iloc[1] != second.results["trend"].signals.signal.iloc[1]
    assert second.results["trend"].portfolio_history.portfolio_value.iloc[2] == 100
    for name in ["buy_hold", "rebalance"]:
        pd.testing.assert_frame_equal(first.results[name].portfolio_history, second.results[name].portfolio_history)


def test_change_only_risk_free_changes_sharpe_not_any_portfolio(trend_case):
    first = run(trend_case)
    trend_case["risk_free"]["period_return"] = ".03"
    second = run(trend_case)
    for name in first.results:
        pd.testing.assert_frame_equal(first.results[name].portfolio_history, second.results[name].portfolio_history)
    pd.testing.assert_frame_equal(first.results["trend"].signals, second.results["trend"].signals)
    a, b = (pd.read_csv(out.output_path / "summary.csv").set_index("strategy") for out in [first, second])
    assert a.loc["trend", "sharpe_ratio"] != b.loc["trend", "sharpe_ratio"]
    pd.testing.assert_frame_equal(a.drop(columns="sharpe_ratio"), b.drop(columns="sharpe_ratio"))


@pytest.mark.parametrize("column", ["signal_value", "performance_value"])
def test_future_changes_do_not_change_earlier_signals_positions_or_wealth(trend_case, column):
    first = run(trend_case)
    change(trend_case, "2020-06-30", column, "200")
    second = run(trend_case)
    for name in first.results:
        pd.testing.assert_frame_equal(first.results[name].portfolio_history.iloc[:5], second.results[name].portfolio_history.iloc[:5])
    pd.testing.assert_frame_equal(first.results["trend"].signals.iloc[:5], second.results["trend"].signals.iloc[:5])
    if column == "performance_value":
        pd.testing.assert_frame_equal(first.results["trend"].signals, second.results["trend"].signals)
    else:
        assert first.results["trend"].portfolio_history.portfolio_value.iloc[5] == second.results["trend"].portfolio_history.portfolio_value.iloc[5]
        assert first.results["trend"].signals.position.iloc[5] == second.results["trend"].signals.position.iloc[5]


def test_all_three_share_calendar_and_strategy_execution_is_read_only(trend_case):
    c = trend_case
    context = prepare_context(load_config(c["save"]()))
    performance, signals, rf = context.performance.copy(deep=True), context.trend_signals.copy(deep=True), context.risk_free.copy(deep=True)
    strategies = [(BuyAndHold(), {"asset": "TREND_SYNTH"}),
                  (Rebalance(), {"target_weights": dict(context.config.target_weights), "rebalance_frequency": "annual"}),
                  (Trend(), context.config.trend_params())]
    first = [strategy.run(context, params) for strategy, params in strategies]
    second = [strategy.run(context, params) for strategy, params in reversed(strategies)]
    for a, b in zip(first, reversed(second)):
        pd.testing.assert_frame_equal(a.portfolio_history, b.portfolio_history)
        assert pd.DatetimeIndex(a.portfolio_history.date).equals(context.performance.index)
    pd.testing.assert_frame_equal(context.performance, performance)
    pd.testing.assert_frame_equal(context.trend_signals, signals)
    pd.testing.assert_series_equal(context.risk_free, rf)
    out = run(c)
    del c["raw"]["strategies"]["trend"]
    without = run(c)
    for name in without.results:
        pd.testing.assert_frame_equal(out.results[name].portfolio_history, without.results[name].portfolio_history)
    assert not (without.output_path / "signals.csv").exists()


def test_missing_common_performance_date_does_not_drop_own_signal_history(trend_case):
    c = trend_case
    c["market"] = c["market"].loc[~((c["market"].date == "2020-02-29") & (c["market"].asset_id == "BD_SYNTH"))]
    del c["raw"]["data"]["risk_free"]
    out = run(c)
    for result in out.results.values():
        assert len(result.portfolio_history) == 6 and pd.Timestamp("2020-02-29") not in set(result.portfolio_history.date)
    s = out.results["trend"].signals
    # SMA counts its asset's observed signal values, while lag counts shared performance valuations.
    assert s.sma_short.iloc[1] == 25 and s.sma_long.iloc[1] == 20
    assert s.position.iloc[1] == 0
    assert out.results["trend"].portfolio_history.portfolio_value.iloc[1] == 100
    quality = json.loads((out.output_path / "data_quality.json").read_text(encoding="utf-8"))
    assert quality["series"]["TREND_SYNTH"]["removed_non_common_dates"] == ["2019-11-30", "2019-12-31", "2020-02-29"]


def test_trend_only_disabled_unavailable_other_strategies_and_ordering(trend_case):
    c = trend_case
    first = run(c)
    c["market"], c["assets"] = c["market"].iloc[::-1], c["assets"].iloc[::-1]
    c["raw"]["strategies"] = dict(reversed(list(c["raw"]["strategies"].items())))
    second = run(c)
    for item in first.manifest["results"]:
        assert (first.output_path / item["path"]).read_bytes() == (second.output_path / item["path"]).read_bytes()
    c["raw"]["strategies"] = {"trend": c["raw"]["strategies"]["trend"], "buy_hold": {"enabled": False, "asset": "ABSENT"}}
    out = run(c)
    assert list(out.results) == ["trend"] and out.result is out.results["trend"]
    assert not (out.output_path / "weights_history.csv").exists()
    assert not (out.output_path / "trades.csv").exists()


@pytest.mark.parametrize("kind", ["missing_asset", "currency", "disabled"])
def test_trend_asset_validation_and_disabled_trend_without_signal_data(trend_case, kind):
    c = trend_case
    if kind == "missing_asset":
        c["raw"]["strategies"]["trend"]["asset"] = "MISSING"
    elif kind == "currency":
        c["assets"].loc[c["assets"].asset_id == "TREND_SYNTH", "currency"] = "USD"
    else:
        c["raw"]["strategies"]["trend"]["enabled"] = False
        c["raw"]["strategies"]["trend"]["asset"] = "MISSING"
        c["market"] = c["market"].drop(columns="signal_value")
        assert not (run(c).output_path / "signals.csv").exists()
        return
    with pytest.raises(DataValidationError):
        run(c)


def test_shared_helper_undefined_sma_is_not_cash_and_legacy_uses_same_definition():
    prices = pd.Series([10.,10.,10.,20.,30.])
    original = prices.copy()
    s = sma_signal(prices,2,3)
    legacy = trendfolge(prices,2,3)
    assert len(legacy) == len(prices)
    assert s.signal.iloc[:2].isna().all() and legacy.Signal.iloc[:2].isna().all()
    assert legacy.Strategierendite.iloc[:3].isna().all()
    assert s.signal.iloc[2:].tolist() == [0,1,1]
    pd.testing.assert_series_equal(s.signal, legacy.Signal, check_names=False)
    pd.testing.assert_series_equal(prices, original)


@pytest.mark.parametrize("values", [pd.Series([1.,np.nan,3.]), pd.Series([1.,np.inf,3.]),
                                    pd.Series([True,False,True]), pd.Series(['1','2','3']),
                                    pd.Series([1+1j,2+0j,3+0j]), pd.Series([1.,2.,3.], index=[0,0,1]),
                                    pd.Series([1.,2.,3.], index=[2,1,0]), pd.Series(dtype=float)])
def test_shared_helper_and_legacy_reject_bad_observations(values):
    for function in [sma_signal, trendfolge]:
        with pytest.raises(ValueError):
            function(values,1,2)


@pytest.mark.parametrize("column", ["position", "signal", "sma_short", "signal_value", "asset_id"])
def test_result_rejects_corrupted_signal_tables(trend_case, column):
    context = prepare_context(load_config(trend_case["save"]()))
    result = Trend().run(context, context.config.trend_params())
    s = result.signals.copy()
    s.loc[1, column] = "OTHER" if column == "asset_id" else s.loc[1, column] + .5
    with pytest.raises(ValueError):
        validate_results(context, [replace(result, signals=s)])


def test_trend_cli_works_from_another_directory(trend_case):
    path = trend_case["save"]()
    result = subprocess.run([sys.executable, "-m", "maturarbeit_engine", "run", "--config", str(path)],
                            cwd=trend_case["root"], capture_output=True, text=True, timeout=30)
    assert result.returncode == 0, result.stderr
    assert (Path(result.stdout.strip()) / "signals.csv").is_file()


def test_effective_start_uses_latest_warm_up_without_moving_other_calendars(trend_case):
    c = trend_case
    c["market"] = c["market"].loc[~((c["market"].asset_id == "BD_SYNTH") & (c["market"].date == "2020-01-31"))]
    out = run(c)
    for result in out.results.values():
        assert result.portfolio_history.date.iloc[0] == pd.Timestamp("2020-02-29")
        assert result.portfolio_history.portfolio_value.iloc[0] == 100
    s = out.results["trend"].signals
    assert s.sma_short.iloc[0] == 15 and s.sma_long.iloc[0] == pytest.approx(40/3)
    assert s.signal.iloc[0] == 1 and pd.isna(s.position.iloc[0])
    assert out.results["trend"].portfolio_history.portfolio_value.iloc[1] == pytest.approx(110)
    q = json.loads((out.output_path / "data_quality.json").read_text(encoding="utf-8"))["trend"]
    assert q["warm_up_period"] == {"start": "2019-12-31", "end": "2020-01-31"}
    assert q["available_warm_up_observations"] == 3 and q["used_warm_up_observations"] == 2


def test_union_includes_trend_asset_outside_other_portfolios(trend_case):
    c = trend_case
    c["raw"]["strategies"]["buy_hold"]["asset"] = "BD_SYNTH"
    c["raw"]["strategies"]["rebalance"]["target_weights"] = {"BD_SYNTH": 1.0}
    c["market"] = c["market"].loc[~((c["market"].asset_id == "TREND_SYNTH") & (c["market"].date == "2020-03-31"))]
    del c["raw"]["data"]["risk_free"]
    out = run(c)
    for result in out.results.values():
        assert len(result.portfolio_history) == 6 and pd.Timestamp("2020-03-31") not in set(result.portfolio_history.date)
    q = json.loads((out.output_path / "data_quality.json").read_text(encoding="utf-8"))
    assert q["required_assets"] == ["BD_SYNTH", "TREND_SYNTH"]
    assert "2020-03-31" in q["series"]["BD_SYNTH"]["removed_non_common_dates"]


def test_valid_all_cash_run_keeps_capital_but_uses_risk_free_for_sharpe(trend_case):
    c = trend_case
    c["market"].loc[c["market"].asset_id == "TREND_SYNTH", "signal_value"] = "10"
    out = run(c)
    result = out.results["trend"]
    assert result.portfolio_history.portfolio_value.tolist() == [100] * 7
    assert result.signals.signal.tolist() == [0] * 7
    assert result.signals.position.iloc[1:].tolist() == [0] * 6
    row = pd.read_csv(out.output_path / "summary.csv").set_index("strategy").loc["trend"]
    assert row.total_return == row.annualized_return == row.annualized_volatility == row.max_drawdown == 0
    assert row.sharpe_ratio == pytest.approx(-.0015 / math.sqrt(6 * .0005**2 / 5) * math.sqrt(12))


def test_no_tolerance_zone_or_filter_in_sma_comparison():
    s = sma_signal(pd.Series([1., 1., 1. + 1e-12]), 2, 3)
    assert s.sma_short.iloc[-1] > s.sma_long.iloc[-1]
    assert s.signal.iloc[-1] == 1


def test_missing_rf_interval_cannot_be_filled_by_trend(trend_case):
    trend_case["risk_free"] = trend_case["risk_free"].iloc[:-1]
    with pytest.raises(DataValidationError):
        run(trend_case)
    assert not (trend_case["root"] / "runs").exists()


def test_signal_table_requires_complete_dates_and_initial_position(trend_case):
    context = prepare_context(load_config(trend_case["save"]()))
    result = Trend().run(context, context.config.trend_params())
    missing = result.signals.iloc[1:]
    with pytest.raises(ValueError):
        replace(result, signals=missing).validate(100)
    initial = result.signals.copy()
    initial.loc[0, "position"] = 0
    with pytest.raises(ValueError):
        replace(result, signals=initial).validate(100)
