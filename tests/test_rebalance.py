"""Independent scalar controls for stateful annual portfolios and shared runs."""
from dataclasses import replace
from pathlib import Path
import hashlib
import json
import math
import numpy as np
import pandas as pd
import pytest
from maturarbeit_engine.funktionen import neue_gewichtung, rebalancing, validate_target_weights
from maturarbeit_engine.engine.config import ConfigError, load_config
from maturarbeit_engine.engine.context import prepare_context
from maturarbeit_engine.engine.result import WEIGHTS_COLUMNS, TRADES_COLUMNS
from maturarbeit_engine.engine.simulation import run_simulation
from maturarbeit_engine.strategies.buy_hold import BuyAndHold
from maturarbeit_engine.strategies.rebalance import Rebalance
from maturarbeit_engine.data.validate import DataValidationError

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def portfolio_case(tmp_path):
    c = {"root": tmp_path,
         "raw": json.loads((ROOT / "configs/demo_rebalance.json").read_text(encoding="utf-8"))}
    for name in ["market", "assets", "risk_free"]:
        c[name] = pd.read_csv(ROOT / "configs/rebalance_demo" / (name + ".csv"))
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


def test_hand_computed_drift_event_next_period_and_final_value(portfolio_case):
    outcome = run(portfolio_case)
    result = outcome.results["rebalance"]
    h, w, t = result.portfolio_history, result.weights_history, result.trades
    assert h.portfolio_value.tolist() == pytest.approx([100, 106, 112.6, 110.348, 116.4284])
    assert pd.isna(h.period_return.iloc[0])
    assert h.period_return.iloc[1:].tolist() == pytest.approx([.06, 6.6 / 106, -.02, 6.0804 / 110.348])
    assert h.drawdown.tolist() == pytest.approx([0, 0, 0, -.02, 0])
    initial = w.loc[w.date == h.date.iloc[0]].set_index("asset_id")
    assert initial.weight_before.to_dict() == {"BD_SYNTH": .4, "EQ_SYNTH": .6}
    assert (initial.weight_before * 100).to_dict() == {"BD_SYNTH": 40, "EQ_SYNTH": 60}
    assert initial.weight_after.equals(initial.target_weight)
    june = w.loc[w.date == pd.Timestamp("2020-06-30")].set_index("asset_id")
    assert june.loc["EQ_SYNTH", "weight_before"] == pytest.approx(66 / 106)
    assert june.weight_after.equals(june.weight_before)
    event = w.loc[w.date == pd.Timestamp("2020-12-30")].set_index("asset_id")
    assert event.loc["EQ_SYNTH", "weight_before"] == pytest.approx(72.6 / 112.6)
    assert event.weight_after.to_dict() == pytest.approx({"BD_SYNTH": .4, "EQ_SYNTH": .6})
    assert set(t.date) == {pd.Timestamp("2020-12-30")}
    trade = t.set_index("asset_id")
    assert trade.value_before.to_dict() == pytest.approx({"BD_SYNTH": 40, "EQ_SYNTH": 72.6})
    assert trade.target_value.to_dict() == pytest.approx({"BD_SYNTH": 45.04, "EQ_SYNTH": 67.56})
    assert trade.transaction_value.to_dict() == pytest.approx({"BD_SYNTH": 5.04, "EQ_SYNTH": -5.04})
    assert trade.target_value.sum() == pytest.approx(112.6)
    assert trade.value_before.sum() == pytest.approx(112.6)
    assert trade.transaction_value.sum() == pytest.approx(0, abs=1e-12)
    assert not math.isclose(h.portfolio_value.iloc[2], 100 * 1.06 * 1.06)
    assert not math.isclose(h.portfolio_value.iloc[3], 72.6 * .9 + 40 * 1.1)
    final = w.loc[w.date == h.date.iloc[-1]].set_index("asset_id")
    assert final.weight_after.equals(final.weight_before)
    assert final.loc["EQ_SYNTH", "weight_after"] == pytest.approx(66.8844 / 116.4284)
    summary = pd.read_csv(outcome.output_path / "summary.csv").set_index("strategy")
    assert summary.loc["rebalance", "total_return"] == pytest.approx(.164284)
    assert summary.loc["rebalance", "max_drawdown"] == pytest.approx(-.02)
    assert summary.loc["buy_hold", "end_value"] == pytest.approx(119.79)
    assert outcome.result is outcome.results["buy_hold"]


def test_output_contract_order_reproducibility_and_all_hashes(portfolio_case):
    one, two = run(portfolio_case), run(portfolio_case)
    names = {"portfolio_history.csv", "summary.csv", "data_quality.json", "weights_history.csv", "trades.csv"}
    assert {p.name for p in one.output_path.iterdir()} == names | {"run_manifest.json"}
    assert {i["path"] for i in one.manifest["results"]} == names
    for name in names:
        assert (one.output_path / name).read_bytes() == (two.output_path / name).read_bytes()
    for item in one.manifest["results"]:
        assert hashlib.sha256((one.output_path / item["path"]).read_bytes()).hexdigest() == item["sha256"]
    for name, columns in [("weights_history", WEIGHTS_COLUMNS), ("trades", TRADES_COLUMNS)]:
        frame = pd.read_csv(one.output_path / (name + ".csv"))
        assert list(frame.columns) == columns
        pd.testing.assert_frame_equal(frame, frame.sort_values(["strategy", "date", "asset_id"], kind="stable").reset_index(drop=True))
    weights = pd.read_csv(one.output_path / "weights_history.csv")
    np.testing.assert_allclose(weights.groupby(["date", "strategy"])[["weight_before", "weight_after"]].sum(), 1)
    trades = pd.read_csv(one.output_path / "trades.csv")
    np.testing.assert_allclose(trades.transaction_value, trades.target_value - trades.value_before, atol=1e-12)
    history = pd.read_csv(one.output_path / "portfolio_history.csv")
    pd.testing.assert_frame_equal(history, history.sort_values(["strategy", "date"], kind="stable").reset_index(drop=True))
    assert history.groupby("strategy").date.apply(list).iloc[0] == history.groupby("strategy").date.apply(list).iloc[1]
    assert one.manifest["executed_strategies"] == ["buy_hold", "rebalance"]


def test_shared_context_is_unchanged_by_strategy_order(portfolio_case):
    context = prepare_context(load_config(portfolio_case["save"]()))
    before = context.performance.copy(deep=True)
    rf_before = context.risk_free.copy(deep=True)
    params = {"target_weights": dict(context.config.target_weights), "rebalance_frequency": "annual"}
    bh_one = BuyAndHold().run(context, {"asset": "EQ_SYNTH"})
    rb_one = Rebalance().run(context, params)
    rb_two = Rebalance().run(context, params)
    bh_two = BuyAndHold().run(context, {"asset": "EQ_SYNTH"})
    pd.testing.assert_frame_equal(bh_one.portfolio_history, bh_two.portfolio_history)
    pd.testing.assert_frame_equal(rb_one.portfolio_history, rb_two.portfolio_history)
    pd.testing.assert_frame_equal(context.performance, before)
    pd.testing.assert_series_equal(context.risk_free, rf_before)


def test_csv_and_json_asset_order_is_irrelevant(portfolio_case):
    first = run(portfolio_case)
    portfolio_case["market"] = portfolio_case["market"].iloc[::-1]
    portfolio_case["assets"] = portfolio_case["assets"].iloc[::-1]
    portfolio_case["raw"]["strategies"] = dict(reversed(list(portfolio_case["raw"]["strategies"].items())))
    portfolio_case["raw"]["strategies"]["rebalance"]["target_weights"] = {"BD_SYNTH": .4, "EQ_SYNTH": .6}
    second = run(portfolio_case)
    for name in ["portfolio_history.csv", "summary.csv", "weights_history.csv", "trades.csv", "data_quality.json"]:
        assert (first.output_path / name).read_bytes() == (second.output_path / name).read_bytes()


def test_future_price_changes_no_earlier_portfolio_weights_or_trades(portfolio_case):
    first = run(portfolio_case)
    portfolio_case["market"].loc[(portfolio_case["market"].date == "2021-12-31")
                                 & (portfolio_case["market"].asset_id == "EQ_SYNTH"), "performance_value"] = 200
    second = run(portfolio_case)
    for name in first.results:
        pd.testing.assert_frame_equal(first.results[name].portfolio_history.iloc[:-1], second.results[name].portfolio_history.iloc[:-1])
    pd.testing.assert_frame_equal(first.results["rebalance"].weights_history.iloc[:-2], second.results["rebalance"].weights_history.iloc[:-2])
    pd.testing.assert_frame_equal(first.results["rebalance"].trades, second.results["rebalance"].trades)


def test_all_active_assets_share_calendar_before_returns(portfolio_case):
    c = portfolio_case
    c["market"] = c["market"].loc[~((c["market"].date == "2020-12-30") & (c["market"].asset_id == "BD_SYNTH"))]
    del c["raw"]["data"]["risk_free"]
    out = run(c)
    for result in out.results.values():
        assert result.portfolio_history.date.dt.strftime("%Y-%m-%d").tolist() == ["2020-01-31", "2020-06-30", "2021-06-30", "2021-12-31"]
    quality = json.loads((out.output_path / "data_quality.json").read_text(encoding="utf-8"))
    assert quality["series"]["EQ_SYNTH"]["removed_non_common_dates"] == ["2020-12-30"]
    assert out.results["rebalance"].trades.date.unique().tolist() == [pd.Timestamp("2020-06-30")]
    assert out.results["buy_hold"].portfolio_history.period_return.iloc[2] == pytest.approx(108.9 / 110 - 1)


def test_unused_asset_does_not_change_comparison_calendar(portfolio_case):
    one = run(portfolio_case)
    c = portfolio_case
    extra = c["market"].iloc[[0]].copy().assign(asset_id="UNUSED", date="2018-01-01")
    c["market"] = pd.concat([c["market"], extra], ignore_index=True)
    c["assets"] = pd.concat([c["assets"], c["assets"].iloc[[0]].assign(asset_id="UNUSED")], ignore_index=True)
    two = run(c)
    for name in one.results:
        pd.testing.assert_frame_equal(one.results[name].portfolio_history, two.results[name].portfolio_history)
    quality = json.loads((two.output_path / "data_quality.json").read_text(encoding="utf-8"))
    assert "UNUSED" in quality["loaded_assets"] and "UNUSED" not in quality["required_assets"]


def test_rebalance_only_and_disabled_unavailable_buy_hold(portfolio_case):
    c = portfolio_case
    c["raw"]["strategies"]["buy_hold"] = {"enabled": False, "asset": "NOT_LOADED"}
    one = run(c)
    del c["raw"]["strategies"]["buy_hold"]
    two = run(c)
    assert list(one.results) == list(two.results) == ["rebalance"]
    assert two.result is two.results["rebalance"]
    pd.testing.assert_frame_equal(one.result.portfolio_history, two.result.portfolio_history)


def test_start_year_end_is_initial_allocation_not_trade(portfolio_case):
    portfolio_case["raw"]["period"]["start"] = "2020-12-30"
    result = run(portfolio_case).results["rebalance"]
    assert result.trades.empty
    assert result.portfolio_history.portfolio_value.tolist() == pytest.approx([100, 98, 103.4])


def test_scheduled_event_with_zero_transactions_is_recorded(portfolio_case):
    c = portfolio_case
    equity = c["market"].loc[c["market"].asset_id == "EQ_SYNTH", "performance_value"].to_numpy()
    c["market"].loc[c["market"].asset_id == "BD_SYNTH", "performance_value"] = equity
    result = run(c).results["rebalance"]
    assert len(result.trades) == 2
    assert result.trades.transaction_value.tolist() == pytest.approx([0, 0], abs=1e-12)


def test_zero_weight_and_three_assets_are_supported(portfolio_case):
    c = portfolio_case
    extra = c["market"].loc[c["market"].asset_id == "EQ_SYNTH"].copy().assign(asset_id="C_SYNTH", performance_value=[100, 80, 120, 90, 180])
    c["market"] = pd.concat([c["market"], extra], ignore_index=True)
    c["assets"] = pd.concat([c["assets"], c["assets"].iloc[[0]].assign(asset_id="C_SYNTH")], ignore_index=True)
    c["raw"]["strategies"]["rebalance"]["target_weights"] = {"EQ_SYNTH": .2, "BD_SYNTH": .3, "C_SYNTH": .5}
    out = run(c).results["rebalance"]
    # Independent units-times-prices calculation, followed by one explicit target allocation.
    end_2020 = .2 * 121 + .3 * 100 + .5 * 120
    after_2021 = end_2020 * (.2 * .9 + .3 * 1.1 + .5 * .75)
    final = end_2020 * (.2 * .9 * 1.1 + .3 * 1.1 + .5 * 1.5)
    assert out.portfolio_history.portfolio_value.tolist() == pytest.approx([100, 92, end_2020, after_2021, final])
    c["raw"]["strategies"]["rebalance"]["target_weights"] = {"EQ_SYNTH": 1., "BD_SYNTH": 0., "C_SYNTH": 0.}
    result = run(c).results["rebalance"]
    assert result.portfolio_history.portfolio_value.tolist() == pytest.approx([100, 110, 121, 108.9, 119.79])
    assert (result.weights_history.loc[result.weights_history.asset_id != "EQ_SYNTH", "weight_after"] == 0).all()


def test_both_strategies_use_same_risk_free_and_own_observed_returns(case):
    case["market"].loc[3] = ["2020-01-31", "SYNTH_B", 100.]
    case["market"].loc[4] = ["2020-02-29", "SYNTH_B", 100.]
    case["market"].loc[5] = ["2020-03-31", "SYNTH_B", 100.]
    case["assets"].loc[1] = case["assets"].iloc[0]
    case["assets"].loc[1, "asset_id"] = "SYNTH_B"
    case["raw"]["strategies"]["rebalance"] = {"enabled": True, "target_weights": {"SYNTH_A": .6, "SYNTH_B": .4}, "rebalance_frequency": "annual"}
    out = run_simulation(case["save"]())
    summary = pd.read_csv(out.output_path / "summary.csv").set_index("strategy")
    for name, returns in [("buy_hold", [.1, -.1]), ("rebalance", [.06, -6.6 / 106])]:
        excess = [returns[0] - .001, returns[1] - .002]
        mean = sum(excess) / 2
        sigma = abs(excess[0] - excess[1]) / math.sqrt(2)
        assert summary.loc[name, "sharpe_ratio"] == pytest.approx(mean / sigma * math.sqrt(12))
    result = out.results["rebalance"]
    assert result.trades.empty
    assert list(pd.read_csv(out.output_path / "trades.csv").columns) == TRADES_COLUMNS


@pytest.mark.parametrize("weights", [{"EQ_SYNTH": .5, "BD_SYNTH": .4}, {"EQ_SYNTH": .7, "BD_SYNTH": .4},
                                    {"EQ_SYNTH": -.1, "BD_SYNTH": 1.1}, {}, {"EQ_SYNTH": "one"},
                                    {"EQ_SYNTH": True}, {"EQ_SYNTH": 10 ** 400}, [1],
                                    {"EQ_SYNTH": 1e308, "BD_SYNTH": 1e308}])
def test_invalid_config_weights_rejected(portfolio_case, weights):
    portfolio_case["raw"]["strategies"]["rebalance"]["target_weights"] = weights
    with pytest.raises(ConfigError):
        run(portfolio_case)
    assert not (portfolio_case["root"] / "runs").exists()


@pytest.mark.parametrize("bad", ["NaN", "Infinity", "-Infinity"])
def test_nonfinite_json_weights_rejected(portfolio_case, bad):
    path = portfolio_case["save"]()
    path.write_text(path.read_text(encoding="utf-8").replace('"EQ_SYNTH": 0.6', '"EQ_SYNTH": ' + bad), encoding="utf-8")
    with pytest.raises(ConfigError):
        run_simulation(path)


@pytest.mark.parametrize("key", ["enabled", "target_weights", "rebalance_frequency"])
def test_missing_rebalance_parameters_rejected(portfolio_case, key):
    del portfolio_case["raw"]["strategies"]["rebalance"][key]
    with pytest.raises(ConfigError):
        run(portfolio_case)


@pytest.mark.parametrize("frequency", ["monthly", None, [], True])
def test_only_annual_rebalancing_is_supported(portfolio_case, frequency):
    portfolio_case["raw"]["strategies"]["rebalance"]["rebalance_frequency"] = frequency
    with pytest.raises(ConfigError):
        run(portfolio_case)


@pytest.mark.parametrize("enabled", [1, "true", None, [], {}])
def test_enabled_must_be_boolean(portfolio_case, enabled):
    portfolio_case["raw"]["strategies"]["rebalance"]["enabled"] = enabled
    with pytest.raises(ConfigError):
        run(portfolio_case)


@pytest.mark.parametrize("mode", ["empty", "disabled"])
def test_at_least_one_strategy_enabled(portfolio_case, mode):
    if mode == "empty":
        portfolio_case["raw"]["strategies"] = {}
    else:
        for params in portfolio_case["raw"]["strategies"].values():
            params["enabled"] = False
    with pytest.raises(ConfigError):
        run(portfolio_case)


@pytest.mark.parametrize("kind", ["unknown", "missing_market", "missing_metadata", "wrong_currency", "zero_weight_unknown"])
def test_all_rebalance_assets_require_data_metadata_and_currency(portfolio_case, kind):
    c = portfolio_case
    if kind == "unknown":
        c["raw"]["strategies"]["rebalance"]["target_weights"] = {"UNKNOWN": 1}
    elif kind == "zero_weight_unknown":
        c["raw"]["strategies"]["rebalance"]["target_weights"] = {"EQ_SYNTH": 1, "UNKNOWN": 0}
    elif kind == "missing_market":
        c["market"] = c["market"].loc[c["market"].asset_id != "BD_SYNTH"]
    elif kind == "missing_metadata":
        c["assets"] = c["assets"].loc[c["assets"].asset_id != "BD_SYNTH"]
    else:
        c["assets"].loc[c["assets"].asset_id == "BD_SYNTH", "currency"] = "USD"
    with pytest.raises(DataValidationError):
        run(c)


@pytest.mark.parametrize("bad", [np.nan, np.inf, -np.inf, -.1, 0., "text", True])
def test_invalid_position_values_rejected(bad):
    values = pd.Series({"A": bad, "B": 0.})
    with pytest.raises(ValueError):
        neue_gewichtung(values, pd.Series({"A": .1, "B": .0}))


@pytest.mark.parametrize("returns", [pd.Series({"A": .1}), pd.Series({"A": .1, "B": 0., "C": 0.}),
                                     pd.Series([.1, 0.], index=["A", "A"]), pd.Series({"A": np.nan, "B": 0.}),
                                     pd.Series({"A": np.inf, "B": 0.}), pd.Series({"A": -1., "B": 0.}),
                                     pd.Series({"A": -1.1, "B": 0.})])
def test_drift_rejects_incomplete_invalid_or_mismatched_returns(returns):
    with pytest.raises(ValueError):
        neue_gewichtung(pd.Series({"A": 60., "B": 40.}), returns)


@pytest.mark.parametrize("weights", [pd.Series({"A": .5, "B": .4}), pd.Series({"A": -.1, "B": 1.1}),
                                     pd.Series({"A": np.nan, "B": .4}), pd.Series({"A": np.inf, "B": .4}),
                                     pd.Series({"A": 1.}), pd.Series([.6, .4], index=["A", "A"]),
                                     pd.Series(dtype=float), pd.Series({"A": "0.6", "B": "0.4"})])
def test_rebalancing_rejects_invalid_weights_or_asset_labels(weights):
    with pytest.raises(ValueError):
        rebalancing(pd.Series({"A": 60., "B": 40.}), weights)


def test_existing_helpers_preserve_formulas_labels_inputs_and_near_unit_weights():
    positions = pd.Series({"A": 60., "B": 40.})
    original = positions.copy()
    values, weights = neue_gewichtung(positions, pd.Series({"B": 0., "A": .1}))
    assert values.to_dict() == pytest.approx({"A": 66, "B": 40})
    assert weights.to_dict() == pytest.approx({"A": 66 / 106, "B": 40 / 106})
    _, _, target, desired, transactions = rebalancing(values, pd.Series({"B": .4, "A": .6}))
    assert desired.to_dict() == pytest.approx({"A": 63.6, "B": 42.4})
    assert transactions.to_dict() == pytest.approx({"A": -2.4, "B": 2.4})
    assert target.index.equals(positions.index)
    pd.testing.assert_series_equal(positions, original)
    close = pd.Series({"A": .6, "B": .4000000000005})
    pd.testing.assert_series_equal(validate_target_weights(close), close)


@pytest.mark.parametrize("table, column", [("weights_history", "weight_after"), ("trades", "transaction_value")])
def test_result_invariants_reject_corrupted_weights_and_trades(portfolio_case, table, column):
    result = run(portfolio_case).results["rebalance"]
    changed = getattr(result, table).copy()
    changed.loc[0, column] += .1
    with pytest.raises(ValueError):
        replace(result, **{table: changed}).validate(100)


def test_multi_strategy_missing_risk_free_interval_fails(portfolio_case):
    portfolio_case["risk_free"] = portfolio_case["risk_free"].iloc[:-1]
    with pytest.raises(DataValidationError):
        run(portfolio_case)


def test_union_includes_buy_hold_asset_outside_rebalance_targets(portfolio_case):
    c = portfolio_case
    extra = c["market"].loc[(c["market"].asset_id == "EQ_SYNTH")
                             & c["market"].date.isin(["2020-06-30", "2020-12-30", "2021-06-30"])].copy().assign(asset_id="BENCHMARK")
    c["market"] = pd.concat([c["market"], extra], ignore_index=True)
    c["assets"] = pd.concat([c["assets"], c["assets"].iloc[[0]].assign(asset_id="BENCHMARK")], ignore_index=True)
    c["raw"]["strategies"]["buy_hold"]["asset"] = "BENCHMARK"
    del c["raw"]["data"]["risk_free"]
    outcome = run(c)
    quality = json.loads((outcome.output_path / "data_quality.json").read_text(encoding="utf-8"))
    assert quality["required_assets"] == ["BD_SYNTH", "BENCHMARK", "EQ_SYNTH"]
    for result in outcome.results.values():
        assert result.portfolio_history.date.dt.strftime("%Y-%m-%d").tolist() == ["2020-06-30", "2020-12-30", "2021-06-30"]


def test_rebalancing_repeats_annually_and_conserves_capital_each_time(portfolio_case):
    c = portfolio_case
    extra = pd.DataFrame({"date": ["2022-06-30", "2022-06-30", "2022-12-31", "2022-12-31"],
                          "asset_id": ["BD_SYNTH", "EQ_SYNTH", "BD_SYNTH", "EQ_SYNTH"],
                          "performance_value": [110, 239.58, 110, 239.58]})
    c["market"] = pd.concat([c["market"], extra], ignore_index=True)
    c["risk_free"].loc[4] = ["2021-12-31", "2022-06-30", "RF_SYNTHETIC", .001]
    c["risk_free"].loc[5] = ["2022-06-30", "2022-12-31", "RF_SYNTHETIC", .002]
    c["raw"]["period"]["end"] = "2022-12-31"
    result = run(c).results["rebalance"]
    assert set(result.trades.date) == {pd.Timestamp("2020-12-30"), pd.Timestamp("2021-12-31")}
    for _, trades in result.trades.groupby("date"):
        assert trades.value_before.sum() == pytest.approx(trades.target_value.sum())
        assert trades.transaction_value.sum() == pytest.approx(0, abs=1e-12)
    assert result.portfolio_history.portfolio_value.iloc[-1] == pytest.approx(116.4284 * 1.6)
