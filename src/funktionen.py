import numpy as np
import pandas as pd

WEIGHT_TOLERANCE = 1e-12
CAPITAL_TOLERANCE = 1e-12


def resample_dataframe(df: pd.DataFrame, frequenz: str, aggregation: dict):
    return df.resample(frequenz).agg(aggregation)


def absolute_aenderung(df: pd.Series):
    return df.diff()


def prozentuale_aenderung(df: pd.Series):
    """Relative changes without fabricating values at missing observations."""
    return df.pct_change(fill_method=None)


def kumulierte_rendite(preise: pd.Series):
    log_rendite = np.log(preise / preise.shift(1))
    kumulierte_log_rendite = log_rendite.cumsum()
    return kumulierte_log_rendite


def wachstumsfaktor(preise: pd.Series):
    kumulierte_log_rendite = kumulierte_rendite(preise)
    wachstumsfaktoren = np.exp(kumulierte_log_rendite)
    return wachstumsfaktoren


def geometrisches_mittel(werte: np.ndarray):
    return np.exp(np.mean(np.log(werte)))


def annualisierte_rendite(
    werte: np.ndarray, perioden_pro_jahr: int, *, input_kind: str
):
    """Annualize explicitly declared growth factors, never guess return semantics."""
    if input_kind != "growth_factors":
        raise ValueError("annualisierte_rendite requires growth_factors (1 + r).")
    _positive_periods(perioden_pro_jahr)
    werte = np.asarray(werte, dtype=float)
    if werte.ndim != 1 or len(werte) == 0 or not np.isfinite(werte).all() or (werte <= 0).any():
        raise ValueError("Growth factors must be a nonempty finite positive vector.")
    return geometrisches_mittel(werte) ** perioden_pro_jahr - 1


def standardabweichung(werte: np.ndarray):
    werte = pd.Series(werte, dtype="float64")
    return werte.std(ddof=1)


def annualisierte_volatilitaet(werte: np.ndarray, perioden_pro_jahr: int):
    annualisierte_volatilitaet = standardabweichung(werte) * perioden_pro_jahr ** (1/2)
    return annualisierte_volatilitaet


def drawdown(renditen: pd.Series):
    """OD-09: the initial wealth factor 1 is included in every high-water mark."""
    _finite_returns(renditen)
    if (renditen < -1).any():
        raise ValueError("Returns below -100% are invalid for this wealth model.")
    vermoegen = (1 + renditen).cumprod()
    bisheriger_hoechststand = vermoegen.cummax().clip(lower=1.0)
    return vermoegen / bisheriger_hoechststand - 1


def maximum_drawdown(renditen: pd.Series):
    return drawdown(renditen).min()


def sharpe_ratio(
    renditen: pd.Series,
    risikofreie_renditen: pd.Series,
    perioden_pro_jahr: int,
):
    """OD-08: exact sample Sharpe on explicitly aligned period returns."""
    _positive_periods(perioden_pro_jahr)
    _finite_returns(renditen)
    _finite_returns(risikofreie_renditen)
    if not renditen.index.equals(risikofreie_renditen.index):
        raise ValueError("Investment and risk-free period indices must match exactly.")
    ueberschussrenditen = renditen - risikofreie_renditen
    if len(ueberschussrenditen) < 2 or ueberschussrenditen.nunique() == 1:
        return float("nan")
    return float(ueberschussrenditen.mean() / ueberschussrenditen.std(ddof=1)
                 * np.sqrt(perioden_pro_jahr))


def _positive_periods(value):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, float, np.number)):
        raise ValueError("periods_per_year must be a finite positive number.")
    if not np.isfinite(value) or value <= 0:
        raise ValueError("periods_per_year must be a finite positive number.")


def _finite_returns(value):
    if not isinstance(value, pd.Series) or not value.index.is_unique:
        raise ValueError("Returns must be a Series with unique period indices.")
    if not pd.api.types.is_numeric_dtype(value) or not np.isfinite(value.to_numpy()).all():
        raise ValueError("Returns must be numeric, complete and finite.")


def korrelationsmatrix(renditen: pd.DataFrame):
    return renditen.corr()


def portfolio_risiko(renditen, gewichte):
    cov = renditen.cov()
    varianz = gewichte @ cov @ gewichte
    volatilitaet = np.sqrt(varianz)
    return varianz, volatilitaet


def neue_gewichtung(startwerte: pd.Series, renditen: pd.Series):
    """Advance complete, identically labelled long-only positions (OD-06/13)."""
    startwerte = _position_values(startwerte)
    renditen = _asset_vector(renditen, "Returns")
    _same_assets(startwerte, renditen)
    renditen = renditen.reindex(startwerte.index)
    if (renditen <= -1).any():
        raise ValueError("Positive performance values require returns above -100%.")
    try:
        with np.errstate(over="raise", invalid="raise"):
            neue_werte = startwerte * (1 + renditen)
    except FloatingPointError as exc:
        raise ValueError("Position update exceeded finite numerical precision.") from exc
    neue_werte = _position_values(neue_werte)
    if ((startwerte > 0) & (neue_werte == 0)).any():
        raise ValueError("Position update underflowed to zero.")
    gesamtwert = neue_werte.sum()
    neue_gewichte = neue_werte / gesamtwert
    return neue_werte, neue_gewichte


def rebalancing(aktuelle_werte: pd.Series, zielgewichte: pd.Series):
    """Calculate capital-preserving trades; the caller applies the target state."""
    aktuelle_werte = _position_values(aktuelle_werte)
    zielgewichte = validate_target_weights(zielgewichte)
    _same_assets(aktuelle_werte, zielgewichte)
    zielgewichte = zielgewichte.reindex(aktuelle_werte.index)
    gesamtwert = aktuelle_werte.sum()
    zielwerte = gesamtwert * zielgewichte
    transaktionen = zielwerte - aktuelle_werte
    aktuelle_gewichte = aktuelle_werte / gesamtwert
    if not np.isfinite(zielwerte.to_numpy()).all() or not np.isfinite(transaktionen.to_numpy()).all():
        raise ValueError("Rebalancing exceeded finite numerical precision.")
    if (not np.isclose(zielwerte.sum(), gesamtwert, rtol=CAPITAL_TOLERANCE, atol=0)
            or abs(transaktionen.sum()) > CAPITAL_TOLERANCE * gesamtwert):
        raise ValueError("Rebalancing must preserve capital.")
    return aktuelle_werte, aktuelle_gewichte, zielgewichte, zielwerte, transaktionen


def _asset_vector(values, name):
    if (not isinstance(values, pd.Series) or values.empty or not values.index.is_unique
            or not all(isinstance(a, str) and a.strip() for a in values.index)):
        raise ValueError(f"{name} require nonempty, unique asset labels.")
    if (not pd.api.types.is_numeric_dtype(values) or pd.api.types.is_bool_dtype(values)
            or not np.isrealobj(values.to_numpy())):
        raise ValueError(f"{name} must be real numeric values.")
    values = values.astype(float).copy()
    if not np.isfinite(values.to_numpy()).all():
        raise ValueError(f"{name} must be complete and finite.")
    return values


def _position_values(values):
    values = _asset_vector(values, "Positions")
    if (values < 0).any():
        raise ValueError("Positions must be nonnegative.")
    with np.errstate(over="ignore"):
        total = values.sum()
    if not np.isfinite(total) or total <= 0:
        raise ValueError("Total portfolio value must be finite and positive.")
    return values


def _same_assets(one, two):
    if set(one.index) != set(two.index):
        raise ValueError("Asset labels must match exactly; no missing or extra assets.")


def validate_target_weights(weights):
    """OD-13: validate, never normalize; absolute sum tolerance is 1e-12."""
    weights = _asset_vector(weights, "Target weights")
    if ((weights < 0).any() or (weights > 1.0 + WEIGHT_TOLERANCE).any()
            or not np.isclose(weights.sum(), 1.0, atol=WEIGHT_TOLERANCE, rtol=0)):
        raise ValueError("Target weights must be nonnegative and sum to 1 (tolerance 1e-12).")
    return weights


def buy_and_hold(renditen: pd.Series, startkapital: float):
    return startkapital * (1 + renditen).cumprod()


def validate_sma_windows(short_window, long_window):
    """Windows count observations; no defaults, rounding or boolean integers."""
    for window in [short_window, long_window]:
        if isinstance(window, (bool, np.bool_)) or not isinstance(window, (int, np.integer)) or window <= 0:
            raise ValueError("SMA windows must be positive integers.")
    if short_window >= long_window:
        raise ValueError("The short SMA window must be smaller than the long window.")


def sma_signal(values: pd.Series, short_window: int, long_window: int):
    """One SMA/Long-Cash definition; undefined warm-up signals remain NaN."""
    validate_sma_windows(short_window, long_window)
    if (not isinstance(values, pd.Series) or values.empty or not values.index.is_unique
            or not values.index.is_monotonic_increasing or values.index.hasnans
            or not pd.api.types.is_numeric_dtype(values) or pd.api.types.is_bool_dtype(values)
            or not np.isrealobj(values.to_numpy())):
        raise ValueError("Signals require an ordered, unique, real numeric Series.")
    values = values.astype(float).copy()
    if not np.isfinite(values.to_numpy()).all():
        raise ValueError("Signal observations must be complete and finite; no filling or dropping.")
    short = values.rolling(short_window, min_periods=short_window).mean()
    long = values.rolling(long_window, min_periods=long_window).mean()
    signal = pd.Series(np.nan, index=values.index, dtype=float)
    valid = short.notna() & long.notna()
    if not np.isfinite(short.loc[valid]).all() or not np.isfinite(long.loc[valid]).all():
        raise ValueError("SMA calculation exceeded finite numerical precision.")
    signal.loc[valid] = (short.loc[valid] > long.loc[valid]).astype(float)
    return pd.DataFrame({"signal_value": values, "sma_short": short, "sma_long": long, "signal": signal})


def trendfolge(preise: pd.Series, kurzes_fenster: int, langes_fenster: int):
    """Legacy single-series example using the same validated SMA definition."""
    daten = sma_signal(preise, kurzes_fenster, langes_fenster).rename(columns={
        "signal_value": "Kurs", "sma_short": "SMA kurz", "sma_long": "SMA lang", "signal": "Signal"})
    daten["Marktrendite"] = prozentuale_aenderung(daten["Kurs"])
    daten["Strategierendite"] = daten["Signal"].shift(1) * daten["Marktrendite"]
    return daten
