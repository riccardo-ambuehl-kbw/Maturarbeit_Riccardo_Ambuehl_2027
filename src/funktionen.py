import numpy as np
import pandas as pd


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
    neue_werte = startwerte * (1 + renditen)
    gesamtwert = neue_werte.sum()
    neue_gewichte = neue_werte / gesamtwert
    return neue_werte, neue_gewichte


def rebalancing(aktuelle_werte: pd.Series, zielgewichte: pd.Series):
    gesamtwert = aktuelle_werte.sum()
    zielwerte = gesamtwert * zielgewichte
    transaktionen = zielwerte - aktuelle_werte
    aktuelle_gewichte = aktuelle_werte / gesamtwert
    return aktuelle_werte, aktuelle_gewichte, zielgewichte, zielwerte, transaktionen


def buy_and_hold(renditen: pd.Series, startkapital: float):
    return startkapital * (1 + renditen).cumprod()


def trendfolge(preise: pd.Series, kurzes_fenster: int, langes_fenster: int):
    if kurzes_fenster >= langes_fenster:
        raise ValueError("Das kurze Fenster muss kleiner als das lange Fenster sein.")

    daten = pd.DataFrame({"Kurs": preise}).dropna().sort_index()
    daten["SMA kurz"] = daten["Kurs"].rolling(kurzes_fenster).mean()
    daten["SMA lang"] = daten["Kurs"].rolling(langes_fenster).mean()
    daten["Signal"] = np.where(daten["SMA kurz"] > daten["SMA lang"], 1, 0)
    daten["Marktrendite"] = daten["Kurs"].pct_change()
    daten["Strategierendite"] = daten["Signal"].shift(1) * daten["Marktrendite"]
    return daten
