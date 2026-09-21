import numpy as np
import pandas as pd
import quantstats as qs


def resample_dataframe(df: pd.DataFrame, frequenz: str, aggregation: dict):
    return df.resample(frequenz).agg(aggregation)


def absolute_aenderung(df: pd.Series):
    return df.diff()


def prozentuale_aenderung(df: pd.Series):
    return df.pct_change()


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


def annualisierte_rendite(werte: np.ndarray, perioden_pro_jahr: int):
    return geometrisches_mittel(werte) ** perioden_pro_jahr - 1


def standardabweichung(werte: np.ndarray):
    werte = pd.Series(werte, dtype="float64")
    return werte.std(ddof=1)


def annualisierte_volatilitaet(werte: np.ndarray, perioden_pro_jahr: int):
    annualisierte_volatilitaet = standardabweichung(werte) * perioden_pro_jahr ** (1/2)
    return annualisierte_volatilitaet


def drawdown(renditen: pd.Series):
    vermoegen = (1 + renditen).cumprod()
    bisheriger_hoechststand = vermoegen.cummax()
    return vermoegen / bisheriger_hoechststand - 1


def maximum_drawdown(renditen: pd.Series):
    return drawdown(renditen).min()


def sharpe_ratio(
    renditen: pd.Series,
    risikofreie_renditen: pd.Series,
    perioden_pro_jahr: int,
):
    daten = pd.concat([renditen, risikofreie_renditen], axis=1)
    daten.columns = ["Anlage", "Risikofrei"]
    ueberschussrenditen = daten["Anlage"] - daten["Risikofrei"]
    return qs.stats.sharpe(
        ueberschussrenditen,
        rf=0,
        periods=perioden_pro_jahr,
    )


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
