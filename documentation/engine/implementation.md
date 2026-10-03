# Engine v1 Core – technische Implementierung

**Stand:** 2026-10-03, Engine 0.1.0 / Konfigurationsschema 1.0.
**Auftrag:** [vollständiger Implementierungsprompt](../ai-usage/prompts/2026-10-02-engine-v1-core-implementation.md).
**Fachliche Grundlage:** Analyse 5.3–5.9, Theorie und die vom Autor verbindlich festgelegten [OD-01 bis OD-13](decisions.md).

## Umfang und Struktur

Implementiert ist ein einzelner lokaler Buy-and-Hold-Lauf: CSV-Dateien und JSON-Konfiguration validieren, gemeinsamen Kontext vorbereiten, die konfigurierte Anlage mit Gewicht 1 halten, gemeinsame Kennzahlen berechnen und vier Ergebnisdateien exportieren. Es gibt keine externen Cashflows; die Total-Return-Behandlung muss bereits in `performance_value` enthalten sein.

| Dateien | Aufgabe |
|---|---|
| `pyproject.toml`, `requirements.lock`, `.gitignore` | Installierbares Paket, festgeschriebene Abhängigkeiten, Ausschluss lokaler Umgebungen und Runs |
| `src/__init__.py`, `src/__main__.py` | Engine-Version und CLI |
| `src/funktionen.py` | Bestehende mathematische Funktionen mit den unten dokumentierten Korrekturen |
| `src/data/{__init__,validate,normalize}.py` | CSV-Snapshots, Datenprüfung, gemeinsame Bewertungen, Risk-Free-Ausrichtung |
| `src/engine/{__init__,config,context,result,simulation}.py` | JSON-Vertrag, SimulationContext, StrategyResult und gemeinsamer Ablauf |
| `src/strategies/{__init__,buy_hold}.py` | Einzelanlage mit Startbewertung und Gewicht 1 |
| `src/analysis/{__init__,metrics}.py` | Einheitliche Zusammenfassung und Verfügbarkeitsstatus |
| `src/export/{__init__,results}.py` | Vollständige Run-Verzeichnisse, Manifest und SHA-256 |
| `configs/demo_buy_hold.json`, `configs/demo/*.csv` | Ausschliesslich künstliche Demo |
| `tests/{conftest,test_functions,test_core}.py` | Synthetische Funktions-, Integrations- und CLI-Prüfungen |

Die geplante physische Struktur unter `src/` bleibt erhalten. Setuptools installiert sie unter dem eindeutigen Paketnamen `maturarbeit_engine`. Es gibt keine zweite CLI-Berechnungslogik: CLI und Python rufen `engine.simulation.run_simulation()` auf.

## Installation und Aufruf

Deklarierter Python-Bereich: **3.11 bis 3.14** (`>=3.11,<3.15`). Tatsächlich geprüft wurde **CPython 3.14.0 auf Windows**. Die anderen deklarierten Versionen und Betriebssysteme wurden hier nicht getestet.

Runtime: NumPy 2.3.5 und pandas 2.3.3. pytest 8.4.2 ist eine Testabhängigkeit. `requirements.lock` fixiert auch die aufgelösten transitiven Pakete; `pyproject.toml` fixiert die isolierten Build-Werkzeuge setuptools 80.9.0 und wheel 0.45.1. Die Lock-Datei ist eine Versionsbindung, kein Lock mit Distributions-Hashes; die lokal geprüften Wheels beziehen sich auf Windows / CPython 3.14.

Im Repository-Stamm, PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --no-cache-dir -c requirements.lock -e ".[test]"
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m maturarbeit_engine run --config configs/demo_buy_hold.json
```

Für eine bestehende `.venv` zuerst deren Python-Version und Isolation prüfen. Die in diesem Auftrag erstellte Umgebung und die separate Wheel-Prüfumgebung haben beide `include-system-site-packages = false`. Globale Pakete wurden nicht installiert oder repariert. Internetzugriff war nur für die Installation der Python-Pakete erforderlich; Simulationen lesen ausschliesslich lokale Dateien.

Direkter Python-Aufruf nach Installation:

```python
from maturarbeit_engine.engine.simulation import run_simulation

outcome = run_simulation("configs/demo_buy_hold.json")
print(outcome.output_path)
history = outcome.result.portfolio_history
```

Ein über `load_config()` erzeugtes `RunConfig` ist ebenfalls zulässig; es wird mit seiner weiterhin vorhandenen Konfigurationsdatei abgeglichen. Manuelle Abänderungen des Objekts können die Validierung nicht umgehen. Die CLI gibt bei ungültigen lokalen Daten oder Konfigurationen eine Fehlermeldung und Exit-Code 2 aus.

## Daten- und Konfigurationsvertrag

CSV-Dateien verwenden UTF-8, optional mit BOM, Kommatrennung und ISO-Datumswerte `YYYY-MM-DD` ohne Uhrzeit. Pflichtspalten:

- Markt: `date,asset_id,performance_value`.
- Metadaten: `asset_id,name,asset_class,country,currency,provider,provider_symbol`.
- Normalisierte risikofreie Renditen: `period_start,period_end,series_id,period_return`.

`signal_value` und weitere Marktspalten werden in diesem Slice nicht verwendet und im Qualitätsbericht aufgeführt. Pflichtwerte, doppelte Spaltennamen, doppelte Markt-Schlüssel, doppelte Metadaten-IDs und doppelte Risk-Free-Perioden pro Reihe werden geprüft. Marktwerte müssen endlich und positiv sein; fehlende numerische Beobachtungen werden abgelehnt. Alle geladenen Markt-IDs benötigen Metadaten, die verwendete Anlage muss zur Basiswährung passen. Es erfolgt keine Auffüllung, Interpolation, FX-Konvertierung oder erneute Total-Return-Bereinigung.

`align_performance()` unterstützt mehrere benötigte Anlagen: zuerst Schnittmenge tatsächlich vorhandener Bewertungen bilden, danach den gewünschten Zeitraum auswählen, erst anschliessend Renditen berechnen. Der Core benötigt für Buy-and-Hold nur eine Anlage. Mindestens zwei Bewertungen müssen im gewünschten Zeitraum verbleiben. Entfernte nicht gemeinsame Termine und Beobachtungen ausserhalb des gewünschten Zeitraums werden separat berichtet. Zusätzliche geladene Anlagen bestimmen den Kalender der verwendeten Anlage nicht.

Die Demo-Konfiguration zeigt den vollständigen JSON-Vertrag. Pflichtfelder sind `schema_version`, `run_name`, `period` mit `start/end`, `start_capital`, `base_currency`, `periods_per_year`, `data` mit `market/assets` und `strategies.buy_hold` mit `enabled/asset`. Unbekannte Felder oder Strategieoptionen, deaktiviertes Buy-and-Hold, ungültige Typen und nicht endliche Zahlen werden abgelehnt. Es gibt keine fachlichen Defaults. Relative Dateipfade beziehen sich auf die Konfigurationsdatei; ein fehlendes `output_dir` bedeutet technisch `outputs/runs` im aktuellen Arbeitsverzeichnis. URLs sind keine Datenreferenzen.

`data.risk_free` ist optional. Bei vollständigem Fehlen bleibt Sharpe nicht verfügbar. Bei einer angegebenen Datei sind Serien-ID und beide Grenzen **jeder** tatsächlichen Renditeperiode verbindlich: fehlende, verschobene oder zusätzlich überlappende Intervalle führen zum Fehler. Ausserhalb des Laufs liegende Intervalle werden gezählt und nicht verwendet. FRED-Jahreszinsumrechnung und Beschaffung gehören nicht zum Core.

## Start und Annualisierung

Die erste Zeile ist die Bewertung am ersten gemeinsamen Datum am oder nach `start`: Startkapital, leere Rendite, Drawdown 0. Das Ende ist das letzte gemeinsame Datum am oder vor `end`. Ausschliesslich die nachfolgenden beobachteten Renditen gehen in Kennzahlen ein.

Zur technischen Prüfung von OD-03 kann die Konfiguration zusätzlich `period_frequency` deklarieren. Es wird weder aus Datumsabständen noch aus `periods_per_year` eine Frequenz gewählt. Der Core erkennt ausschliesslich vollständig regelmässige, tatsächlich vorhandene Kalendergitter:

| Deklaration | Erkanntes Gitter | Zulässiges explizites `periods_per_year` |
|---|---|---|
| `MS`, `ME` | Monatsanfang / Monatsende | 12 |
| `YS`, `YE` | Jahresanfang / Jahresende | 1 |
| `W` | Wöchentlich am Sonntag | 52 |
| `D` | Jeder Kalendertag | 365 oder 366 |

Diese Prüfung erzeugt oder resampelt keine Beobachtung und legt keinen Versuchsparameter fest. Fehlt die Deklaration, ist das Gitter unregelmässig oder passt der konfigurierte Jahresfaktor nicht, bleiben annualisierte Rendite, Volatilität und Sharpe nicht verfügbar. Gesamtperformance und Drawdown bleiben auswertbar. Insbesondere werden tägliche Börsendaten mit Handelspausen hier nicht als 252 regelmässige Perioden erraten; Börsenkalender und weitergehende Periodenaufbereitung sind noch nicht implementiert. Es gibt keinen automatischen kalenderzeitbasierten CAGR-Ersatz.

Die annualisierte Rendite verwendet ausdrücklich `1 + r` als Wachstumsfaktoren. Volatilität verwendet die Stichproben-Standardabweichung der Anlagerenditen; Sharpe verwendet exakt die Stichproben-Standardabweichung der Überschussrenditen gemäss OD-08. Bei weniger als zwei Renditen sind Stichproben-Volatilität und Sharpe nicht definiert. Bei konstanter Überschussrendite bleibt Sharpe ebenfalls nicht verfügbar, statt unendlich oder 0 auszugeben. Tatsächliche Nullvolatilität bleibt hingegen 0.

## Änderungen an bestehenden Funktionen

Der [Audit](audit.md) enthält die ursprünglichen Gegenbeispiele; die Tests reproduzieren die verbindlich korrigierten Fälle unabhängig von der Engine.

| Funktion / Änderung | Nachweis und Bezug |
|---|---|
| `prozentuale_aenderung()` | `pct_change(fill_method=None)`: aus `100, NaN, 110` wird keine künstliche Nullrendite. OD-01 und Prompt Abschnitt 6. |
| `annualisierte_rendite()` | Die Formel über das geometrische Mittel bleibt erhalten. Neuer zwingender Keyword-Parameter `input_kind="growth_factors"` sowie Prüfung auf positive, endliche, nicht leere Faktoren und positives `m`. Ein alter Aufruf ohne Semantikangabe oder mit `input_kind="returns"` wird abgelehnt. Faktoren unter 1 bleiben zulässig: der Zahlenwert allein kann die Semantik nicht beweisen. Der Engine-Aufruf bildet `1 + r` sichtbar. OD-03 und Prompt Abschnitt 6. |
| `drawdown()` | Das anfängliche Vermögensniveau 1 wird in die High-Water-Mark einbezogen; bei `100 → 90 → 81` entstehen `−10 %` und `−19 %`. Eingaberenditen müssen vollständig und endlich sein; Werte unter −100 % werden abgelehnt. OD-09. |
| `maximum_drawdown()` | Keine eigene zweite Formel hinzugefügt; die unveränderte Funktion profitiert von der Korrektur ihrer aufgerufenen `drawdown()`-Funktion. |
| `sharpe_ratio()` | QuantStats-Aufruf durch `mean(r-rf) / std(r-rf, ddof=1) * sqrt(m)` ersetzt. Beide Reihen müssen eindeutige, identische Periodenindizes und endliche Werte besitzen. Test mit Renditen über 100 % verhindert Preis-Heuristik. Weniger als zwei Werte oder konstante Überschussrendite liefern intern einen undefinierten Wert, der im Engine-Output als nicht verfügbar mit Status erscheint. OD-07/08. |
| QuantStats-Import | Aus `src/funktionen.py` entfernt, weil nach der autorisierten Sharpe-Korrektur keine Funktion dieses Imports mehr bedarf. Keine QuantStats-Abhängigkeit im Core; historische Definitionen im geschützten Theorie-Notebook bleiben unverändert. |

Die zusätzlichen privaten Prüfhilfen `_positive_periods()` und `_finite_returns()` dienen ausschliesslich der Eingabeprüfung. `buy_and_hold()`, `geometrisches_mittel()` und `annualisierte_volatilitaet()` werden mit validierten Eingaben wiederverwendet; ihre Formeln wurden nicht ersetzt. Das neue Strategieobjekt ergänzt Startzeile, Vertrag und Exportfähigkeit um das bestehende `buy_and_hold()`. Die übrigen historischen Funktionen wurden nicht verändert. Insbesondere gelten alte `rebalancing()`-/`trendfolge()`-Funktionen dadurch nicht als geprüfte vollständige Engine-Strategien.

## Exporte und Reproduzierbarkeit

Ein erfolgreicher Lauf erzeugt unter `output_dir/<run_name>-<uuid>/` genau:

- `portfolio_history.csv`: Datum, Strategie, Vermögen, Periodenrendite und Drawdown; Start-Rendite leer.
- `summary.csv`: Start-/Endwert, Gesamtrendite, annualisierte Rendite/Volatilität, Sharpe und maximaler Drawdown. Nicht verfügbare Zahlen sind leer; ihr Grund steht im Manifest.
- `data_quality.json`: Status, geladene/benötigte Anlagen, ursprüngliche und effektive Grenzen, Beobachtungszahlen, entfernte Termine, Risk-Free- und Annualisierungsprüfung, Warnungen.
- `run_manifest.json`: Engine-/Schema-Version, Run-ID, UTC-Zeit, vollständig aufgelöste Konfiguration, gewünschte/effektive Grenzen, Währung, `m`, Eingabepfade und SHA-256, Git-Commit und Dirty-Status, Python-/Runtime-Paketversionen, Kennzahlstatus und Ergebnis-Hashes.

JSON wird mit `allow_nan=False` geschrieben. Verfügbarkeitsfelder verwenden `null`, CSV-Zahlenlücken erhalten einen nachvollziehbaren Status. Der nicht beobachtete Startwert der Rendite ist die einzige reguläre Datenlücke im Verlauf. Numerischer Überlauf oder nicht endliche berechnete Ergebnisse führen zum Fehler.

Eingabe-Hashes beschreiben die gelesenen Bytes; vor dem Export wird eine zwischenzeitliche Dateiänderung abgefangen. Zusätzlich zu Git werden alle Python-Quellen und, im Checkout, `pyproject.toml` und `requirements.lock` gehasht, damit ein Dirty-Lauf unterscheidbar bleibt. Bei einer Wheel-Installation ausserhalb eines Git-Checkouts sind Git-Commit/Dirty ausdrücklich `null` mit Status `unavailable`; die installierten Python-Quellen werden weiterhin gehasht. Für archivierte wissenschaftliche Runs sind die Eingabedateien und der passende Checkout bzw. das installierte Paket zusätzlich aufzubewahren; der Core kopiert sie nicht in den Ergebnisordner.

Resultate werden erst vollständig in einem temporären Verzeichnis geschrieben und anschliessend innerhalb derselben Ausgabeablage umbenannt. Bestehende Runs werden nicht überschrieben. Run-ID und Zeitstempel variieren; fachliche CSV-Dateien und Datenqualitätsbericht sind bei identischen Inputs und Code bytegleich. Das Manifest hasht die drei übrigen Ergebnisdateien; es enthält keinen unmöglichen eigenen Selbst-Hash.

## Tatsächlich ausgeführte Demo

Aufruf: `python -m maturarbeit_engine run --config configs/demo_buy_hold.json` in der lokalen `.venv`.

Run: `outputs/runs/synthetic_buy_hold-e0252306f62f4409822e8ff617aa1614/`.

Künstliche Performance-Werte: 100 am 2020-01-31, 110 am 2020-02-29, 99 am 2020-03-31. Startkapital 100 CHF, Monatsendgitter, `m=12`; passende künstliche risikofreie Periodenrenditen 0.001 und 0.002. Diese Angaben legen keine Parameter der Maturarbeit fest.

| Kontrollgrösse | Ergebnis, gerundet |
|---|---:|
| Vermögensverlauf | 100 → 110 → 99 |
| Gesamtrendite | −1 % |
| Annualisierte Rendite, `0.99^6 − 1` | −5.8519850599 % |
| Annualisierte Stichproben-Volatilität | 48.9897948557 % |
| Sharpe | −0.0365595484 |
| Maximaler Drawdown | −10 % |

Die vier Dateien, Standard-JSON, alle Eingabe-/Ergebnis-/Code-Hashes und der Git-Stand wurden zusätzlich zur Test-Suite kontrolliert. Das Manifest nennt Commit `61ff5700ca455e9a0a71f158da3611d641937f6e` und `dirty=true`, weil die Implementierung ausdrücklich nicht committed wurde.

## Grenzen und Verantwortlichkeiten

Noch nicht implementiert: vollständige 60/40-/Rebalancing-, Trendfolge-/SMA- und BIP-Strategien, Warm-up, historische BIP-Verfügbarkeit, reale Marktdatenadapter, FRED-Zinsumrechnung, Batch, Web/API, Parameteroptimierung und Zusatzanalysen. Gewichte, Trades und Signale sind in `StrategyResult` optional und im Einzelanlage-Slice nicht exportiert. Es gibt noch keine Benchmark- oder Vergleichsauswertung mehrerer Strategien und keine Börsenkalender-Aufbereitung.

Vom Autor vorgegeben sind Datenvertrag, mathematische Definitionen, OD-01 bis OD-13 und die Arbeitsgrenze. Codex hat Paketname, strikten JSON-Vertrag, CSV-Lesetechnik, optionale Frequenzdeklaration als Prüfhilfe, Verfügbarkeitsstatus, Hashes, Exportablauf und synthetische Tests technisch umgesetzt. Neue finanzwirtschaftliche Regeln wurden nicht beschlossen; `decisions.md` wurde nicht geändert. Endgültige Versuchswerte bleiben beim Autor. Die bestandenen synthetischen Tests ersetzen keine fachliche Abnahme oder Prüfung realer Daten. Geschützte Notebooks, Methodik, Bibliographie und Buchkapitel bleiben unverändert.
