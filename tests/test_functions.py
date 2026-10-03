import math
import numpy as np
import pandas as pd
import pytest
from maturarbeit_engine import funktionen as f
from maturarbeit_engine.analysis.metrics import annual_return_from_factors


def test_relative_return():
    r = f.prozentuale_aenderung(pd.Series([100., 110.]))
    assert pd.isna(r.iloc[0])
    assert r.iloc[1] == pytest.approx(.1)


def test_missing_price_never_filled():
    assert f.prozentuale_aenderung(pd.Series([100., np.nan, 110.])).isna().all()


def test_buy_hold_uses_existing_function():
    assert f.buy_and_hold(pd.Series([.1, -.1]), 100).tolist() == pytest.approx([110, 99])


@pytest.mark.parametrize("returns,expected", [([-.1, -.1], [-.1, -.19]),
                                             ([.1, -.1, .2], [0, -.1, 0]), ([0, 0], [0, 0])])
def test_drawdown_includes_start(returns, expected):
    r = pd.Series(returns, dtype=float)
    assert f.drawdown(r).tolist() == pytest.approx(expected)
    assert f.maximum_drawdown(r) == pytest.approx(min(expected))


@pytest.mark.parametrize("bad", [np.nan, np.inf, -np.inf])
def test_drawdown_rejects_unobserved_returns(bad):
    with pytest.raises(ValueError):
        f.drawdown(pd.Series([.1, bad]))


@pytest.mark.parametrize("rf", [[.002, .002, .002], [0, .01, -.002]])
def test_sharpe_hand_formula_and_variable_rf(rf):
    r = pd.Series([.02, -.01, .04])
    free = pd.Series(rf)
    x = [a - b for a, b in zip(r, free)]
    mean = sum(x) / len(x)
    sample_std = math.sqrt(sum((v - mean) ** 2 for v in x) / (len(x) - 1))
    assert f.sharpe_ratio(r, free, 12) == pytest.approx(mean / sample_std * math.sqrt(12))


def test_sharpe_large_returns_are_returns():
    assert f.sharpe_ratio(pd.Series([1.1, 1.2, 1.3]), pd.Series([0., 0., 0.]), 12) == pytest.approx(12 * math.sqrt(12))


@pytest.mark.parametrize("kind", ["missing", "shifted", "nan", "inf", "duplicate"])
def test_sharpe_invalid_alignment_or_missing(kind):
    r = pd.Series([.02, .01, .03])
    rf = pd.Series([.001] * 3)
    if kind == "missing":
        rf = rf.iloc[:2]
    elif kind == "shifted":
        rf.index = [1, 2, 3]
    elif kind in {"nan", "inf"}:
        rf.iloc[1] = np.nan if kind == "nan" else np.inf
    else:
        rf.index = [0, 0, 2]
    with pytest.raises(ValueError):
        f.sharpe_ratio(r, rf, 12)


def test_zero_volatility_sharpe_is_undefined():
    assert math.isnan(f.sharpe_ratio(pd.Series([.02, .02]), pd.Series([0., 0.]), 12))


def test_annualization_growth_factors():
    expected = .99 ** 6 - 1
    assert f.annualisierte_rendite(np.array([1.1, .9]), 12, input_kind="growth_factors") == pytest.approx(expected)
    # Legitimate loss factors below 1 remain accepted; numeric values are not guessed.
    assert f.annualisierte_rendite(np.array([.1, .2]), 1, input_kind="growth_factors") == pytest.approx(math.sqrt(.02) - 1)


def test_annualization_requires_explicit_semantics():
    with pytest.raises(TypeError):
        f.annualisierte_rendite(np.array([.1, .2]), 12)
    with pytest.raises(ValueError, match="growth_factors"):
        annual_return_from_factors([.1, .2], 12, input_kind="period_returns")


@pytest.mark.parametrize("factors", [[], [1, np.nan], [1, np.inf], [0, 1], [-1, 1]])
def test_invalid_growth_factors(factors):
    with pytest.raises(ValueError):
        f.annualisierte_rendite(np.array(factors), 12, input_kind="growth_factors")


@pytest.mark.parametrize("periods", [0, -1, np.nan, np.inf, True, "12"])
def test_invalid_annualization_parameter(periods):
    with pytest.raises(ValueError):
        f.annualisierte_rendite(np.array([1.1]), periods, input_kind="growth_factors")


def test_other_reused_math_regression():
    prices = pd.Series([100., 110., 126.5])
    assert f.absolute_aenderung(prices).iloc[1:].tolist() == pytest.approx([10, 16.5])
    assert f.kumulierte_rendite(prices).iloc[-1] == pytest.approx(math.log(1.265))
    assert f.wachstumsfaktor(prices).iloc[-1] == pytest.approx(1.265)
    assert f.standardabweichung(np.array([.1, -.1])) == pytest.approx(math.sqrt(.02))
    assert f.annualisierte_volatilitaet(np.array([.1, -.1]), 12) == pytest.approx(math.sqrt(.24))
