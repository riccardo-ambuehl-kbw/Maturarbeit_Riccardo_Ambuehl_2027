"""GDP decisions, independent hand controls, future isolation and shared-run invariants."""
from copy import deepcopy
from dataclasses import replace
from hashlib import sha256
from pathlib import Path
import json
import math
import pandas as pd
import pytest
from maturarbeit_engine.engine.config import ConfigError, load_config
from maturarbeit_engine.engine.context import prepare_context
from maturarbeit_engine.engine.result import validate_results, WEIGHTS_COLUMNS, TRADES_COLUMNS
from maturarbeit_engine.engine.simulation import run_simulation
from maturarbeit_engine.data.validate import validate_macro, DataValidationError
from maturarbeit_engine.data.macro import select_gdp_targets
from maturarbeit_engine.strategies.buy_hold import BuyAndHold
from maturarbeit_engine.strategies.rebalance import Rebalance
from maturarbeit_engine.strategies.trend import Trend
from maturarbeit_engine.strategies.country_weighting import CountryWeighting
from maturarbeit_engine.analysis.metrics import compute_metrics
from maturarbeit_engine.export.results import export_run

ROOT = Path(__file__).resolve().parents[1]
STRATEGIES = ["buy_hold", "country_weighting", "rebalance", "trend"]


@pytest.fixture
def country_case(tmp_path):
    c = {"root": tmp_path,
         "raw": json.loads((ROOT / "configs/demo_country_weighting.json").read_text(encoding="utf-8"))}
    for name in ["market", "assets", "risk_free", "macro"]:
        c[name] = pd.read_csv(ROOT / "configs/country_weighting_demo" / (name + ".csv"), dtype=str,
                              keep_default_na=False)
    c["raw"]["data"] = {"market": "market.csv", "assets": "assets.csv", "macro": "macro.csv",
                         "risk_free": {"path": "risk_free.csv", "series_id": "RF_SYNTHETIC"}}
    c["raw"]["output_dir"] = "runs"

    def save():
        for name in ["market", "assets", "risk_free", "macro"]:
            c[name].to_csv(tmp_path / (name + ".csv"), index=False)
        path = tmp_path / "config.json"
        path.write_text(json.dumps(c["raw"], allow_nan=False), encoding="utf-8")
        return path

    c["save"] = save
    return c


def run(c):
    return run_simulation(c["save"]())


def params(c):
    return {k: v for k, v in c["raw"]["strategies"]["country_weighting"].items() if k != "enabled"}


def decision(c, date="2020-12-30"):
    return select_gdp_targets(validate_macro(c["macro"]), params(c), pd.Timestamp(date), "annual_rebalance")


def macro_quality(out):
    return json.loads((out.output_path / "data_quality.json").read_text(encoding="utf-8"))["macro"]


def test_hand_computed_start_drift_new_targets_trades_next_period_and_final(country_case):
    out = run(country_case)
    r = out.results["country_weighting"]
    h, w, t = r.portfolio_history, r.weights_history, r.trades
    assert h.portfolio_value.tolist() == pytest.approx([100, 106, 112.6, 112.6, 117.667])
    assert h.period_return.iloc[1:].tolist() == pytest.approx([.06, 6.6 / 106, 0, .045])
    assert h.drawdown.tolist() == pytest.approx([0] * 5)
    start = w.loc[w.date == pd.Timestamp("2020-01-31")].set_index("asset_id")
    assert start.target_weight.to_dict() == {"ASSET_A": .6, "ASSET_B": .4}
    assert (start.weight_after * 100).to_dict() == {"ASSET_A": 60, "ASSET_B": 40}
    assert start.weight_before.equals(start.target_weight) and start.weight_after.equals(start.target_weight)
    june = w.loc[w.date == pd.Timestamp("2020-06-30")].set_index("asset_id")
    assert june.loc["ASSET_A", "weight_before"] == pytest.approx(66 / 106)
    assert june.target_weight.to_dict() == {"ASSET_A": .6, "ASSET_B": .4}
    assert june.weight_after.equals(june.weight_before)
    event = w.loc[w.date == pd.Timestamp("2020-12-30")].set_index("asset_id")
    assert event.loc["ASSET_A", "weight_before"] == pytest.approx(72.6 / 112.6)
    assert event.target_weight.to_dict() == {"ASSET_A": .5, "ASSET_B": .5}
    assert event.weight_after.to_dict() == pytest.approx({"ASSET_A": .5, "ASSET_B": .5})
    assert set(t.date) == {pd.Timestamp("2020-12-30")}
    trades = t.set_index("asset_id")
    assert trades.value_before.to_dict() == pytest.approx({"ASSET_A": 72.6, "ASSET_B": 40})
    assert trades.target_value.to_dict() == pytest.approx({"ASSET_A": 56.3, "ASSET_B": 56.3})
    assert trades.transaction_value.to_dict() == pytest.approx({"ASSET_A": -16.3, "ASSET_B": 16.3})
    next_period = w.loc[w.date == pd.Timestamp("2021-06-30")].set_index("asset_id")
    assert next_period.weight_after.to_dict() == pytest.approx({"ASSET_A": .45, "ASSET_B": .55})
    assert next_period.target_weight.to_dict() == {"ASSET_A": .5, "ASSET_B": .5}
    final = w.loc[w.date == pd.Timestamp("2021-12-31")].set_index("asset_id")
    assert final.target_weight.to_dict() == {"ASSET_A": .5, "ASSET_B": .5}
    assert final.weight_before.equals(final.weight_after)
    # Available final GDP 2020 = 80/20 must not create a terminal decision or trade.
    assert [d["selected_period"] for d in r.macro_decisions] == ["2018", "2019"]
    assert [d["decision_date"] for d in r.macro_decisions] == ["2020-01-31", "2020-12-30"]
    summary = pd.read_csv(out.output_path / "summary.csv").set_index("strategy")
    assert summary.loc["country_weighting", "total_return"] == pytest.approx(.17667)
    assert summary.loc["country_weighting", "max_drawdown"] == pytest.approx(0)
    assert summary.loc["rebalance", "end_value"] == pytest.approx(116.4284)
    assert summary.loc["buy_hold", "end_value"] == pytest.approx(119.79)
    assert summary.loc["trend", "end_value"] == pytest.approx(99)


@pytest.mark.parametrize("column", ["period", "country", "indicator", "value", "unit", "available_from"])
def test_missing_macro_column_fails_without_output(country_case, column):
    country_case["macro"] = country_case["macro"].drop(columns=column)
    with pytest.raises(DataValidationError):
        run(country_case)
    assert not (country_case["root"] / "runs").exists()


@pytest.mark.parametrize("column,bad", [
    ("period", "20"), ("period", "20201"), ("period", "2020.0"), ("period", "202A"),
    ("period", "0000"), ("period", "２０２０"), ("period", ""),
    ("country", ""), ("country", " "), ("indicator", ""), ("indicator", " "),
    ("unit", ""), ("unit", " "), ("value", "0"), ("value", "-1"), ("value", "NaN"),
    ("value", "Inf"), ("value", "-Inf"), ("value", "text"), ("value", ""), ("value", "1e309"),
    ("available_from", ""), ("available_from", "2020-02-30"), ("available_from", "2020-1-01"),
    ("available_from", "2020-01-01T00:00:00"), ("available_from", "not-a-date")])
def test_bad_macro_value_rejected(country_case, column, bad):
    country_case["macro"].loc[0, column] = bad
    with pytest.raises(DataValidationError):
        run(country_case)
    assert not (country_case["root"] / "runs").exists()


def test_ambiguous_full_key_rejected_even_for_later_version(country_case):
    duplicate = country_case["macro"].iloc[[-1]].copy().assign(value="99")
    country_case["macro"] = pd.concat([country_case["macro"], duplicate], ignore_index=True)
    with pytest.raises(DataValidationError, match="Ambiguous"):
        run(country_case)


def test_identical_duplicates_are_order_independent_and_counted(country_case):
    first = run(country_case)
    country_case["macro"] = pd.concat([country_case["macro"], country_case["macro"].iloc[[0]]], ignore_index=True)
    second = run(country_case)
    for name in ["portfolio_history.csv", "weights_history.csv", "trades.csv", "summary.csv", "signals.csv"]:
        assert (first.output_path / name).read_bytes() == (second.output_path / name).read_bytes()
    assert macro_quality(second)["loaded_rows"] == 9
    assert macro_quality(second)["validated_version_rows"] == 8
    assert macro_quality(second)["identical_duplicate_rows"] == 1
    assert macro_quality(first)["decisions"] == macro_quality(second)["decisions"]


def test_latest_available_revision_and_inclusive_publication_date(country_case):
    c = country_case
    earlier, _ = decision(c, "2020-12-14")
    revised, used = decision(c, "2020-12-15")
    assert earlier.to_dict() == pytest.approx({"ASSET_A": 52 / 102, "ASSET_B": 50 / 102})
    assert revised.to_dict() == {"ASSET_A": .5, "ASSET_B": .5}
    assert used["countries"][0]["available_from"] == "2020-12-15"
    assert decision(c)[0].equals(revised)
    later, _ = decision(c, "2021-02-01")
    assert later.to_dict() == pytest.approx({"ASSET_A": 5000 / 5050, "ASSET_B": 50 / 5050})


def test_youngest_common_reference_year_never_mixes_years(country_case):
    c = country_case
    c["macro"].loc[(c["macro"].period == "2020") & (c["macro"].country == "COUNTRY_A"), "available_from"] = "2020-12-01"
    targets, used = decision(c)
    assert used["selected_period"] == "2019"
    assert [row["value"] for row in used["countries"]] == [50, 50]
    assert targets.to_dict() == {"ASSET_A": .5, "ASSET_B": .5}


@pytest.mark.parametrize("kind", ["missing_country", "disjoint_years", "later_initial", "wrong_indicator", "wrong_unit"])
def test_no_common_complete_initial_decision_rejects_entire_run(country_case, kind):
    c = country_case
    b = c["macro"].country == "COUNTRY_B"
    if kind == "missing_country":
        c["macro"] = c["macro"].loc[~b]
    elif kind == "disjoint_years":
        c["macro"].loc[b, "period"] = "2017"
    elif kind == "later_initial":
        c["macro"].loc[b & (c["macro"].period == "2018"), "available_from"] = "2020-02-01"
    else:
        c["macro"].loc[b, "indicator" if kind == "wrong_indicator" else "unit"] = "OTHER"
    with pytest.raises(DataValidationError, match="No common"):
        run(c)
    assert not (c["root"] / "runs").exists()


def test_later_revision_applies_only_at_the_next_actual_annual_decision(country_case):
    c = country_case
    c["raw"]["period"]["end"] = "2022-06-30"
    for asset in ["ASSET_A", "ASSET_B"]:
        c["market"].loc[len(c["market"])] = ["2022-06-30", asset, "239.58" if asset == "ASSET_A" else "110", "20"]
    del c["raw"]["data"]["risk_free"]
    c["macro"] = c["macro"].loc[c["macro"].period != "2020"]
    one = run(c).results["country_weighting"]
    c["macro"].loc[c["macro"].available_from == "2021-02-01", "value"] = "0.001"
    two = run(c).results["country_weighting"]
    # Even the value earned up to the later decision is unchanged: new targets act afterwards.
    pd.testing.assert_frame_equal(one.portfolio_history.iloc[:-1], two.portfolio_history.iloc[:-1], check_exact=True)
    prior = one.weights_history.date < pd.Timestamp("2021-12-31")
    pd.testing.assert_frame_equal(one.weights_history.loc[prior], two.weights_history.loc[prior], check_exact=True)
    pd.testing.assert_frame_equal(one.trades.iloc[:2], two.trades.iloc[:2], check_exact=True)
    assert one.macro_decisions[:2] == two.macro_decisions[:2]
    assert one.macro_decisions[2]["countries"][0]["value"] == 5000
    assert two.macro_decisions[2]["countries"][0]["value"] == .001
    assert one.portfolio_history.portfolio_value.iloc[-1] == pytest.approx(117.667 * (1 + 5000 / 5050))
    assert two.portfolio_history.portfolio_value.iloc[-1] == pytest.approx(117.667 * (1 + .001 / 50.001))


@pytest.mark.parametrize("change", ["later_revision", "later_reference", "later_market"])
def test_future_changes_leave_earlier_portfolios_weights_trades_exact(country_case, change):
    c = country_case
    first = run(c)
    if change == "later_revision":
        c["macro"].loc[c["macro"].available_from == "2021-02-01", "value"] = "0.001"
    elif change == "later_reference":
        c["macro"].loc[c["macro"].period == "2020", "value"] = "1000000"
    else:
        c["market"].loc[(c["market"].date == "2021-12-31") & (c["market"].asset_id == "ASSET_A"), "performance_value"] = "999"
    second = run(c)
    for name in first.results:
        one, two = first.results[name], second.results[name]
        pd.testing.assert_frame_equal(one.portfolio_history.iloc[:-1], two.portfolio_history.iloc[:-1], check_exact=True)
        if one.weights_history is not None:
            pd.testing.assert_frame_equal(one.weights_history.iloc[:-2], two.weights_history.iloc[:-2], check_exact=True)
            pd.testing.assert_frame_equal(one.trades, two.trades, check_exact=True)
    assert first.results["country_weighting"].macro_decisions == second.results["country_weighting"].macro_decisions
    if change != "later_market":
        for name in ["portfolio_history.csv", "weights_history.csv", "trades.csv", "signals.csv", "summary.csv", "data_quality.json"]:
            assert (first.output_path / name).read_bytes() == (second.output_path / name).read_bytes()


def test_exact_indicator_unit_and_country_filter_ignores_valid_extra_rows(country_case):
    c = country_case
    first = run(c)
    extra = pd.concat([c["macro"].assign(indicator="OTHER", value="999999"),
                       c["macro"].assign(unit="OTHER", value="999999"),
                       c["macro"].assign(country="UNUSED_COUNTRY", value="999999")], ignore_index=True)
    c["macro"] = pd.concat([c["macro"], extra], ignore_index=True)
    second = run(c)
    for name in ["portfolio_history.csv", "weights_history.csv", "trades.csv", "signals.csv", "summary.csv"]:
        assert (first.output_path / name).read_bytes() == (second.output_path / name).read_bytes()
    assert macro_quality(first)["decisions"] == macro_quality(second)["decisions"]


@pytest.mark.parametrize("mapping", [{}, {"COUNTRY_A": "ASSET_A"},
    {"COUNTRY_A": "ASSET_A", "COUNTRY_B": "ASSET_A"}, {"": "ASSET_A", "COUNTRY_B": "ASSET_B"},
    {"COUNTRY_A": "", "COUNTRY_B": "ASSET_B"}, {"COUNTRY_A": [], "COUNTRY_B": "ASSET_B"}, [], None])
def test_invalid_country_mapping_is_rejected(country_case, mapping):
    country_case["raw"]["strategies"]["country_weighting"]["country_assets"] = mapping
    with pytest.raises(ConfigError):
        run(country_case)


@pytest.mark.parametrize("key", ["enabled", "country_assets", "indicator", "unit", "rebalance_frequency"])
def test_no_country_parameter_defaults(country_case, key):
    del country_case["raw"]["strategies"]["country_weighting"][key]
    with pytest.raises(ConfigError):
        run(country_case)


@pytest.mark.parametrize("key,value", [("enabled", "true"), ("enabled", 1), ("enabled", None),
    ("indicator", ""), ("indicator", []), ("unit", " "), ("unit", None),
    ("rebalance_frequency", "monthly"), ("rebalance_frequency", []), ("rebalance_frequency", None)])
def test_invalid_explicit_parameters_rejected(country_case, key, value):
    country_case["raw"]["strategies"]["country_weighting"][key] = value
    with pytest.raises(ConfigError):
        run(country_case)


@pytest.mark.parametrize("kind", ["absent", "null", "url", "missing_file"])
def test_required_local_macro_path(country_case, kind):
    c = country_case
    if kind == "absent":
        del c["raw"]["data"]["macro"]
    else:
        c["raw"]["data"]["macro"] = {"null": None, "url": "https://example.test/gdp.csv", "missing_file": "absent.csv"}[kind]
    with pytest.raises((ConfigError, OSError)):
        run(c)
    assert not (c["root"] / "runs").exists()


@pytest.mark.parametrize("kind", ["unknown", "missing_market", "missing_metadata", "wrong_country", "wrong_currency"])
def test_proxies_require_data_metadata_country_and_base_currency(country_case, kind):
    c = country_case
    if kind == "unknown":
        c["raw"]["strategies"]["country_weighting"]["country_assets"]["COUNTRY_B"] = "UNKNOWN"
    elif kind == "missing_market":
        c["market"] = c["market"].loc[c["market"].asset_id != "ASSET_B"]
    elif kind == "missing_metadata":
        c["assets"] = c["assets"].loc[c["assets"].asset_id != "ASSET_B"]
    else:
        c["assets"].loc[c["assets"].asset_id == "ASSET_B", "country" if kind == "wrong_country" else "currency"] = "OTHER" if kind == "wrong_country" else "USD"
    with pytest.raises(DataValidationError):
        run(c)
    assert not (c["root"] / "runs").exists()


def test_macro_and_json_row_order_do_not_change_any_result(country_case):
    first = run(country_case)
    for name in ["market", "assets", "macro", "risk_free"]:
        country_case[name] = country_case[name].iloc[::-1]
    strategies = country_case["raw"]["strategies"]
    country_case["raw"]["strategies"] = dict(reversed(list(strategies.items())))
    strategies["country_weighting"]["country_assets"] = dict(reversed(list(strategies["country_weighting"]["country_assets"].items())))
    second = run(country_case)
    for name in ["portfolio_history.csv", "summary.csv", "weights_history.csv", "trades.csv", "signals.csv", "data_quality.json"]:
        assert (first.output_path / name).read_bytes() == (second.output_path / name).read_bytes()


def test_all_four_strategies_shared_calendar_and_macro_do_not_change_others(country_case):
    c = country_case
    one = run(c)
    assert list(one.results) == STRATEGIES
    assert one.manifest["executed_strategies"] == STRATEGIES
    summary = pd.read_csv(one.output_path / "summary.csv")
    assert summary.strategy.tolist() == STRATEGIES
    assert summary.strategy.is_unique
    dates = one.results["country_weighting"].portfolio_history.date
    for r in one.results.values():
        assert r.portfolio_history.date.equals(dates)
    del c["raw"]["strategies"]["country_weighting"]
    del c["raw"]["data"]["macro"]
    two = run(c)
    for name in two.results:
        pd.testing.assert_frame_equal(one.results[name].portfolio_history, two.results[name].portfolio_history, check_exact=True)
    c["raw"]["strategies"] = {"country_weighting": one.manifest["config"]["strategies"]["country_weighting"]}
    c["raw"]["data"]["macro"] = "macro.csv"
    only = run(c)
    assert list(only.results) == ["country_weighting"]
    pd.testing.assert_frame_equal(one.results["country_weighting"].portfolio_history, only.result.portfolio_history, check_exact=True)


def test_country_only_asset_in_union_controls_all_strategies_calendar(country_case):
    c = country_case
    c["raw"]["strategies"]["rebalance"]["target_weights"] = {"ASSET_A": 1}
    c["market"] = c["market"].loc[~((c["market"].date == "2020-12-30") & (c["market"].asset_id == "ASSET_B"))]
    del c["raw"]["data"]["risk_free"]
    out = run(c)
    for r in out.results.values():
        assert r.portfolio_history.date.dt.strftime("%Y-%m-%d").tolist() == ["2020-01-31", "2020-06-30", "2021-06-30", "2021-12-31"]
    cw = out.results["country_weighting"]
    assert set(cw.trades.date) == {pd.Timestamp("2020-06-30")}
    assert cw.macro_decisions[1]["selected_period"] == "2018"
    quality = json.loads((out.output_path / "data_quality.json").read_text(encoding="utf-8"))
    assert quality["required_assets"] == ["ASSET_A", "ASSET_B"]


def test_effective_start_and_year_end_initial_allocation_without_trade(country_case):
    c = country_case
    c["raw"]["period"]["start"] = "2020-12-01"
    c["risk_free"] = c["risk_free"].iloc[2:]
    out = run(c)
    r = out.results["country_weighting"]
    assert r.macro_decisions[0]["decision_date"] == "2020-12-30"
    assert r.macro_decisions[0]["selected_period"] == "2019"
    assert r.trades.empty
    assert r.portfolio_history.portfolio_value.tolist() == pytest.approx([100, 100, 104.5])
    assert r.weights_history.target_weight.tolist() == [.5] * 6


def test_two_valuations_have_only_initial_decision_and_empty_trade_headers(country_case):
    c = country_case
    c["raw"]["period"]["end"] = "2020-06-30"
    c["risk_free"] = c["risk_free"].iloc[:1]
    out = run(c)
    assert len(out.results["country_weighting"].macro_decisions) == 1
    assert out.results["country_weighting"].trades.empty
    assert pd.read_csv(out.output_path / "trades.csv").empty
    assert list(pd.read_csv(out.output_path / "trades.csv").columns) == TRADES_COLUMNS


def test_shared_context_unchanged_by_strategy_execution_order(country_case):
    context = prepare_context(load_config(country_case["save"]()))
    performance, macro = context.performance.copy(deep=True), context.macro.copy(deep=True)
    rf, signals, quality = context.risk_free.copy(deep=True), context.trend_signals.copy(deep=True), deepcopy(context.data_quality)
    cfg = context.config
    jobs = [(BuyAndHold(), {"asset": cfg.asset}), (Rebalance(), {"target_weights": dict(cfg.target_weights), "rebalance_frequency": "annual"}),
            (Trend(), cfg.trend_params()), (CountryWeighting(), cfg.country_params())]
    first = {r.strategy: r for strategy, p in jobs for r in [strategy.run(context, p)]}
    second = {r.strategy: r for strategy, p in jobs[::-1] for r in [strategy.run(context, p)]}
    for name in first:
        for attr in ["portfolio_history", "weights_history", "trades", "signals"]:
            if getattr(first[name], attr) is not None:
                pd.testing.assert_frame_equal(getattr(first[name], attr), getattr(second[name], attr), check_exact=True)
        assert first[name].macro_decisions == second[name].macro_decisions
    pd.testing.assert_frame_equal(context.performance, performance)
    pd.testing.assert_frame_equal(context.macro, macro)
    pd.testing.assert_frame_equal(context.trend_signals, signals)
    pd.testing.assert_series_equal(context.risk_free, rf)
    assert context.data_quality == quality


def test_disabled_country_strategy_needs_neither_proxies_nor_macro(country_case):
    c = country_case
    c["raw"]["strategies"]["country_weighting"]["enabled"] = False
    c["raw"]["strategies"]["country_weighting"]["country_assets"] = {"MISSING_A": "MISSING_A", "MISSING_B": "MISSING_B"}
    del c["raw"]["data"]["macro"]
    out = run(c)
    assert list(out.results) == ["buy_hold", "rebalance", "trend"]
    assert "macro" not in json.loads((out.output_path / "data_quality.json").read_text(encoding="utf-8"))


def test_multiple_annual_decisions_persist_and_preserve_capital(country_case):
    c = country_case
    c["raw"]["period"]["end"] = "2022-12-31"
    c["market"] = pd.concat([c["market"], pd.DataFrame([
        ["2022-06-30", "ASSET_A", "239.58", "20"], ["2022-06-30", "ASSET_B", "110", ""],
        ["2022-12-31", "ASSET_A", "239.58", "20"], ["2022-12-31", "ASSET_B", "110", ""]], columns=c["market"].columns)], ignore_index=True)
    del c["raw"]["data"]["risk_free"]
    out = run(c)
    r = out.results["country_weighting"]
    assert [d["selected_period"] for d in r.macro_decisions] == ["2018", "2019", "2020"]
    assert [d["decision_type"] for d in r.macro_decisions] == ["initial", "annual_rebalance", "annual_rebalance"]
    assert set(r.trades.date) == {pd.Timestamp("2020-12-30"), pd.Timestamp("2021-12-31")}
    assert r.portfolio_history.portfolio_value.iloc[-1] == pytest.approx(117.667 * 1.8)
    for date, trades in r.trades.groupby("date"):
        total = r.portfolio_history.set_index("date").loc[date, "portfolio_value"]
        assert trades.value_before.sum() == pytest.approx(total)
        assert trades.target_value.sum() == pytest.approx(total)
        assert trades.transaction_value.sum() == pytest.approx(0, abs=1e-12)
        weights = r.weights_history.loc[r.weights_history.date == date]
        assert weights.weight_after.tolist() == pytest.approx(weights.target_weight.tolist())
    assert r.weights_history.loc[r.weights_history.date >= pd.Timestamp("2021-12-31"), "target_weight"].tolist() == [.8, .2] * 3


def test_three_countries_share_full_gdp_denominator(country_case):
    c = country_case
    c["raw"]["strategies"]["country_weighting"]["country_assets"]["COUNTRY_C"] = "ASSET_C"
    c["assets"] = pd.concat([c["assets"], c["assets"].iloc[[1]].assign(asset_id="ASSET_C", country="COUNTRY_C")], ignore_index=True)
    c["market"] = pd.concat([c["market"], c["market"].loc[c["market"].asset_id == "ASSET_B"].assign(asset_id="ASSET_C")], ignore_index=True)
    c["macro"] = pd.concat([c["macro"], c["macro"].loc[c["macro"].country == "COUNTRY_B"].assign(country="COUNTRY_C", value="100")], ignore_index=True)
    r = run(c).results["country_weighting"]
    assert r.weights_history.target_weight.iloc[:3].tolist() == [.3, .2, .5]
    assert r.weights_history.target_weight.iloc[6:9].tolist() == [.25, .25, .5]
    assert r.portfolio_history.portfolio_value.iloc[2] == pytest.approx(106.3)


def test_zero_transaction_annual_event_still_has_applied_decision(country_case):
    c = country_case
    c["macro"].loc[c["macro"].period == "2019", "value"] = "60"
    c["macro"].loc[(c["macro"].period == "2019") & (c["macro"].country == "COUNTRY_B"), "value"] = "40"
    by_date = c["market"].loc[c["market"].asset_id == "ASSET_A"].set_index("date").performance_value
    mask = c["market"].asset_id == "ASSET_B"
    c["market"].loc[mask, "performance_value"] = c["market"].loc[mask, "date"].map(by_date)
    r = run(c).results["country_weighting"]
    assert r.trades.transaction_value.tolist() == pytest.approx([0, 0], abs=1e-12)
    assert len(r.macro_decisions) == 2


def test_output_hashes_provenance_resolved_mapping_and_determinism(country_case):
    one, two = run(country_case), run(country_case)
    names = {"portfolio_history.csv", "summary.csv", "weights_history.csv", "trades.csv", "signals.csv", "data_quality.json"}
    assert {p.name for p in one.output_path.iterdir()} == names | {"run_manifest.json"}
    assert {r["path"] for r in one.manifest["results"]} == names
    for name in names:
        assert (one.output_path / name).read_bytes() == (two.output_path / name).read_bytes()
    for item in one.manifest["results"]:
        assert sha256((one.output_path / item["path"]).read_bytes()).hexdigest() == item["sha256"]
    macro = [i for i in one.manifest["input_files"] if i["kind"] == "macro"]
    assert len(macro) == 1
    assert macro[0]["sha256"] == sha256((country_case["root"] / "macro.csv").read_bytes()).hexdigest()
    cfg = one.manifest["config"]
    assert cfg["strategies"]["country_weighting"] == country_case["raw"]["strategies"]["country_weighting"]
    assert Path(cfg["data"]["macro"]) == (country_case["root"] / "macro.csv").resolve()
    q = macro_quality(one)
    assert q["loaded_rows"] == q["validated_version_rows"] == 8
    assert q["configured_countries"] == ["COUNTRY_A", "COUNTRY_B"]
    assert q["decisions"] == list(one.results["country_weighting"].macro_decisions)
    assert q["decisions"][0]["decision_type"] == "initial"
    assert q["decisions"][0]["selected_period"] == "2018"
    assert q["decisions"][1]["countries"] == [
        {"country": "COUNTRY_A", "asset_id": "ASSET_A", "value": 50, "available_from": "2020-12-15", "target_weight": .5},
        {"country": "COUNTRY_B", "asset_id": "ASSET_B", "value": 50, "available_from": "2020-09-01", "target_weight": .5}]
    for name, columns in [("weights_history", WEIGHTS_COLUMNS), ("trades", TRADES_COLUMNS)]:
        table = pd.read_csv(one.output_path / (name + ".csv"))
        assert list(table.columns) == columns
        pd.testing.assert_frame_equal(table, table.sort_values(["strategy", "date", "asset_id"], kind="stable").reset_index(drop=True))
    for name in ["data_quality.json", "run_manifest.json"]:
        json.loads((one.output_path / name).read_text(encoding="utf-8"), parse_constant=lambda x: pytest.fail(x))


@pytest.mark.parametrize("kind", ["target_between_events", "terminal_target", "missing_event", "missing_allocations", "bad_provenance"])
def test_country_result_rejects_corrupt_states_or_provenance(country_case, kind):
    context = prepare_context(load_config(country_case["save"]()))
    r = CountryWeighting().run(context, context.config.country_params())
    if kind in {"target_between_events", "terminal_target"}:
        w = r.weights_history.copy()
        mask = w.date == pd.Timestamp("2020-06-30" if kind == "target_between_events" else "2021-12-31")
        w.loc[mask, "target_weight"] = [.8, .2]
        bad = replace(r, weights_history=w)
    elif kind == "missing_event":
        bad = replace(r, trades=r.trades.iloc[:0])
    elif kind == "missing_allocations":
        bad = replace(r, weights_history=None, trades=None)
    else:
        bad = replace(r, macro_decisions=())
    with pytest.raises(ValueError):
        validate_results(context, bad)


def test_fixed_rebalance_targets_remain_strictly_constant(country_case):
    r = run(country_case).results["rebalance"]
    w = r.weights_history.copy()
    w.loc[w.date == pd.Timestamp("2020-12-30"), "target_weight"] = [.5, .5]
    with pytest.raises(ValueError):
        replace(r, weights_history=w).validate(100)


def test_country_regular_metrics_use_common_risk_free_and_sample_sharpe(country_case):
    c = country_case
    # Keep GDP targets 60/40 on a regular three-month sample, no annual event.
    dates = {"2020-06-30": "2020-02-29", "2020-12-30": "2020-03-31"}
    c["market"] = c["market"].loc[c["market"].date < "2021-01-01"].copy()
    c["market"]["date"] = c["market"].date.replace(dates)
    c["raw"]["period"]["end"] = "2020-03-31"
    c["raw"]["period_frequency"] = "ME"
    c["risk_free"] = c["risk_free"].iloc[:2].copy()
    c["risk_free"]["period_start"] = ["2020-01-31", "2020-02-29"]
    c["risk_free"]["period_end"] = ["2020-02-29", "2020-03-31"]
    out = run(c)
    summary = pd.read_csv(out.output_path / "summary.csv").set_index("strategy")
    excess = [.06 - .001, 6.6 / 106 - .002]
    mean = sum(excess) / 2
    sigma = abs(excess[0] - excess[1]) / math.sqrt(2)
    assert summary.loc["country_weighting", "sharpe_ratio"] == pytest.approx(mean / sigma * math.sqrt(12))
    assert summary.loc["country_weighting", "sharpe_ratio"] == summary.loc["rebalance", "sharpe_ratio"]
    assert summary.loc["country_weighting", "annualized_return"] == pytest.approx(1.126 ** 6 - 1)


@pytest.mark.parametrize("values", [["1e308", "1e308"], ["5e-324", "1e308"]])
def test_unrepresentable_gdp_weights_fail_explicitly(country_case, values):
    country_case["macro"].loc[country_case["macro"].period == "2018", "value"] = values
    with pytest.raises(DataValidationError, match="precision"):
        run(country_case)


def test_changed_macro_snapshot_is_rejected_before_export(country_case):
    context = prepare_context(load_config(country_case["save"]()))
    result = CountryWeighting().run(context, context.config.country_params())
    summary, status = compute_metrics(result, context)
    path = country_case["root"] / "macro.csv"
    path.write_text(path.read_text(encoding="utf-8").replace(
        "5000,SYNTHETIC_UNITS", "999999,SYNTHETIC_UNITS"), encoding="utf-8")
    with pytest.raises(ValueError, match="Input changed during run: macro"):
        export_run(context, result, summary, status)
    assert not (country_case["root"] / "runs").exists()


def test_country_order_and_proxy_order_need_not_correspond(country_case):
    c = country_case
    c["raw"]["strategies"] = {"country_weighting": c["raw"]["strategies"]["country_weighting"]}
    c["raw"]["strategies"]["country_weighting"]["country_assets"] = {"COUNTRY_A": "Z_PROXY", "COUNTRY_B": "A_PROXY"}
    for name in ["market", "assets"]:
        c[name]["asset_id"] = c[name].asset_id.replace({"ASSET_A": "Z_PROXY", "ASSET_B": "A_PROXY"})
    r = run(c).result
    assert r.weights_history.target_weight.iloc[:2].tolist() == [.4, .6]
    assert r.macro_decisions[0]["countries"][0]["asset_id"] == "Z_PROXY"
    assert r.macro_decisions[0]["countries"][0]["target_weight"] == .6
    assert r.portfolio_history.portfolio_value.tolist() == pytest.approx([100, 106, 112.6, 112.6, 117.667])


def test_duplicate_country_json_key_is_not_silently_overwritten(country_case):
    path = country_case["save"]()
    content = path.read_text(encoding="utf-8")
    path.write_text(content.replace('"COUNTRY_A": "ASSET_A"', '"COUNTRY_A": "ASSET_A", "COUNTRY_A": "ASSET_B"'), encoding="utf-8")
    with pytest.raises(ConfigError, match="Duplicate JSON key: COUNTRY_A"):
        run_simulation(path)
