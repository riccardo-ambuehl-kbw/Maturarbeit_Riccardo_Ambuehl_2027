"""Market-bound counterexamples for the remaining EB-02 portfolio-state gap."""
from copy import deepcopy
from dataclasses import replace
import json
import numpy as np
import pandas as pd
import pytest
from maturarbeit_engine.analysis.metrics import compute_run_metrics
from maturarbeit_engine.engine.config import load_config
from maturarbeit_engine.engine.context import prepare_context
from maturarbeit_engine.engine.result import validate_results
from maturarbeit_engine.export.results import export_run
from maturarbeit_engine.funktionen import drawdown
from maturarbeit_engine.strategies.country_weighting import CountryWeighting
from maturarbeit_engine.strategies.rebalance import Rebalance


@pytest.fixture
def portfolio_state_case(tmp_path):
    def prepare(strategy, *, annual=False, capital=100.):
        dates = ["2020-01-31", "2020-12-31", "2021-06-30", "2021-12-31", "2022-06-30"] if annual else ["2020-01-31", "2020-02-29"]
        values_a, values_b = ([100, 110, 99, 108.9, 119.79], [100, 100, 110, 110, 100]) if annual else ([100, 110], [100, 100])
        market = pd.DataFrame([(date, asset, value) for date, a, b in zip(dates, values_a, values_b)
                               for asset, value in [("A", a), ("B", b)]],
                              columns=["date", "asset_id", "performance_value"])
        market.to_csv(tmp_path / "market.csv", index=False)
        (tmp_path / "assets.csv").write_text(
            "asset_id,name,asset_class,country,currency,provider,provider_symbol\n"
            "A,Artificial A,synthetic,C_A,CHF,synthetic,A\n"
            "B,Artificial B,synthetic,C_B,CHF,synthetic,B\n", encoding="utf-8")
        (tmp_path / "macro.csv").write_text(
            "period,country,indicator,value,unit,available_from\n"
            "2019,C_A,GDP,60,UNITS,2020-01-01\n2019,C_B,GDP,40,UNITS,2020-01-01\n"
            "2020,C_A,GDP,50,UNITS,2020-12-31\n2020,C_B,GDP,50,UNITS,2020-12-31\n"
            "2021,C_A,GDP,80,UNITS,2021-12-31\n2021,C_B,GDP,20,UNITS,2021-12-31\n", encoding="utf-8")
        params = ({"target_weights": {"A": .6, "B": .4}, "rebalance_frequency": "annual"}
                  if strategy == "rebalance" else
                  {"country_assets": {"C_A": "A", "C_B": "B"}, "indicator": "GDP",
                   "unit": "UNITS", "rebalance_frequency": "annual"})
        raw = {"schema_version": "1.0", "run_name": "synthetic_state_check",
               "period": {"start": dates[0], "end": dates[-1]}, "start_capital": capital,
               "base_currency": "CHF", "periods_per_year": 12, "period_frequency": None,
               "data": {"market": "market.csv", "assets": "assets.csv", "macro": "macro.csv"},
               "strategies": {strategy: {"enabled": True, **params}}, "output_dir": "runs"}
        path = tmp_path / "config.json"
        path.write_text(json.dumps(raw), encoding="utf-8")
        context = prepare_context(load_config(path))
        runner = Rebalance() if strategy == "rebalance" else CountryWeighting()
        return context, runner.run(context, params)
    return prepare


def assert_market_state_rejected(context, result):
    # These forgeries satisfy the old local/context and recomputed-summary contracts.
    assert validate_results(context, result) == (result,)
    summary, status = compute_run_metrics([result], context)
    with pytest.raises(ValueError, match="market portfolio state"):
        validate_results(context, result, require_complete=True)
    with pytest.raises(ValueError, match="market portfolio state"):
        export_run(context, result, summary, status)
    assert not context.config.output_dir.exists()


@pytest.mark.parametrize("strategy", ["rebalance", "country_weighting"])
@pytest.mark.parametrize("capital", [100., 1e-200, 1e200])
def test_internally_consistent_120_instead_of_106_cannot_be_exported(portfolio_state_case, strategy, capital):
    context, correct = portfolio_state_case(strategy, capital=capital)
    assert correct.portfolio_history.portfolio_value.iloc[-1] == pytest.approx(capital * 1.06, rel=1e-14, abs=0)
    assert correct.trades.empty
    history = correct.portfolio_history.copy()
    history.loc[1, ["portfolio_value", "period_return"]] = [capital * 1.2, .2]
    weights = correct.weights_history.copy()
    weights.loc[weights.date == history.date.iloc[1], ["weight_before", "weight_after"]] = [[.6, .6], [.4, .4]]
    forged = replace(correct, portfolio_history=history, weights_history=weights)
    summary, _ = compute_run_metrics([forged], context)
    assert summary.end_value.iloc[0] == capital * 1.2
    assert summary.total_return.iloc[0] == pytest.approx(.2)
    assert_market_state_rejected(context, forged)


@pytest.mark.parametrize("strategy", ["rebalance", "country_weighting"])
def test_false_weights_with_correct_106_portfolio_are_rejected(portfolio_state_case, strategy):
    context, correct = portfolio_state_case(strategy)
    weights = correct.weights_history.copy()
    weights.loc[weights.date == context.performance.index[1], ["weight_before", "weight_after"]] = .5
    assert_market_state_rejected(context, replace(correct, weights_history=weights))


@pytest.mark.parametrize("strategy", ["rebalance", "country_weighting"])
@pytest.mark.parametrize("index", [2, 4])
def test_false_drift_between_decisions_and_at_final_date_is_rejected(portfolio_state_case, strategy, index):
    context, correct = portfolio_state_case(strategy, annual=True)
    weights = correct.weights_history.copy()
    date = context.performance.index[index]
    assert date not in set(correct.trades.date)
    weights.loc[weights.date == date, ["weight_before", "weight_after"]] = .5
    assert_market_state_rejected(context, replace(correct, weights_history=weights))


@pytest.mark.parametrize("strategy", ["rebalance", "country_weighting"])
def test_balanced_trades_and_weights_cannot_hide_false_pretrade_positions(portfolio_state_case, strategy):
    context, correct = portfolio_state_case(strategy, annual=True)
    trades, weights = correct.trades.copy(), correct.weights_history.copy()
    date = context.performance.index[1]
    selected = trades.date == date
    trades.loc[selected, "value_before"] = [76., 30.]  # Sum 106, but the actual positions are 66/40.
    trades.loc[selected, "transaction_value"] = trades.loc[selected, "target_value"] - trades.loc[selected, "value_before"]
    weights.loc[weights.date == date, "weight_before"] = [76 / 106, 30 / 106]
    assert_market_state_rejected(context, replace(correct, weights_history=weights, trades=trades))


@pytest.mark.parametrize("strategy", ["rebalance", "country_weighting"])
def test_posttrade_positions_must_supply_the_next_period(portfolio_state_case, strategy):
    context, correct = portfolio_state_case(strategy, annual=True)
    # Pretend the first trade's actual target positions did not carry forward.
    history = correct.portfolio_history.copy()
    history.loc[2, "portfolio_value"] = 66 * .9 + 40 * 1.1
    history.loc[1:, "period_return"] = history.portfolio_value.iloc[1:].to_numpy() / history.portfolio_value.iloc[:-1].to_numpy() - 1
    history.loc[1:, "drawdown"] = drawdown(pd.Series(history.period_return.iloc[1:].to_numpy())).to_numpy()
    assert_market_state_rejected(context, replace(correct, portfolio_history=history))


@pytest.mark.parametrize("strategy,values", [
    ("rebalance", [100, 106, 103.88, 109.604, 112.19464]),
    ("country_weighting", [100, 106, 106, 110.77, 117.6176])])
def test_multiple_events_follow_hand_computed_positions_and_leave_context_unchanged(portfolio_state_case, strategy, values):
    context, correct = portfolio_state_case(strategy, annual=True)
    performance = context.performance.copy(deep=True)
    macro = context.macro.copy(deep=True) if context.macro is not None else None
    quality = deepcopy(context.data_quality)
    assert correct.portfolio_history.portfolio_value.tolist() == pytest.approx(values)
    assert set(correct.trades.date) == {pd.Timestamp("2020-12-31"), pd.Timestamp("2021-12-31")}
    assert validate_results(context, correct, require_complete=True) == (correct,)
    summary, status = compute_run_metrics([correct], context)
    assert export_run(context, correct, summary, status)[0].is_dir()
    pd.testing.assert_frame_equal(context.performance, performance, check_exact=True)
    if macro is None:
        assert context.macro is None
    else:
        pd.testing.assert_frame_equal(context.macro, macro, check_exact=True)
    assert context.data_quality == quality


@pytest.mark.parametrize("strategy", ["rebalance", "country_weighting"])
def test_allocation_and_trade_row_order_remains_irrelevant(portfolio_state_case, strategy):
    context, correct = portfolio_state_case(strategy, annual=True)
    reordered = replace(correct, weights_history=correct.weights_history.iloc[::-1], trades=correct.trades.iloc[::-1])
    assert validate_results(context, reordered, require_complete=True) == (reordered,)


@pytest.mark.parametrize("strategy", ["rebalance", "country_weighting"])
def test_existing_weight_tolerance_is_preserved(portfolio_state_case, strategy):
    context, correct = portfolio_state_case(strategy)
    weights = correct.weights_history.copy()
    mask = weights.date == context.performance.index[1]
    weights.loc[mask, ["weight_before", "weight_after"]] += np.array([[5e-13], [-5e-13]])
    assert validate_results(context, replace(correct, weights_history=weights), require_complete=True)
