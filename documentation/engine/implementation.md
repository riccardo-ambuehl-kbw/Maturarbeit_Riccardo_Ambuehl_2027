# Engine v1 – Core, Rebalancing und SMA-Trendfolge

**Stand:** 2026-10-04, Engine 0.3.0 / weiterhin Konfigurationsschema 1.0.
**Aufträge:** [Core](../ai-usage/prompts/2026-10-02-engine-v1-core-implementation.md), [Multi-Asset/Rebalancing](../ai-usage/prompts/2026-10-04-engine-v1-rebalancing-implementation.md) und [Trendfolge](../ai-usage/prompts/2026-10-04-engine-v1-trend-implementation.md).
**Fachliche Grundlage:** Analyse 5.3–5.9, Theorie und die vom Autor verbindlich festgelegten [OD-01 bis OD-13](decisions.md).

Der Autor hat den Core mit Tag `engine-core-v0.1.0` abgenommen (Commit `1a193094b312354c39a72bdf44ef2f6a20573011`) und Rebalancing mit Tag `engine-rebalancing-v0.2.0` (Commit `37edc79f4211c734423ca89ef3899d1cbc0b81b4`). Der saubere Arbeitsbeginn der Trend-Erweiterung auf `10d70e73826dc7e11dbe3eb5bf5770fa833e4ae6` enthält gegenüber dem letzten Tag ausschliesslich den neuen Prompt. Die technische Prüfung der Trend-Erweiterung ist getrennt von ihrer noch ausstehenden fachlichen Abnahme.

## Umfang und Struktur

Ein einzelner lokaler Run kann Buy-and-Hold, jährliches Rebalancing und SMA-Long/Cash-Trendfolge einzeln oder gemeinsam ausführen. CSV-Dateien und JSON-Konfiguration werden validiert, alle benötigten Performance-Anlagen auf einen gemeinsamen Kalender ausgerichtet und die Strategien über denselben Kontext ausgewertet. Der zusätzliche Signal-Kontext mit Warm-up verändert diesen Performance-Kalender nicht. Es gibt keine externen Cashflows; die Total-Return-Behandlung muss bereits in `performance_value` enthalten sein.

| Dateien | Aufgabe |
|---|---|
| `pyproject.toml`, `requirements.lock`, `.gitignore` | Installierbares Paket, festgeschriebene Abhängigkeiten, Ausschluss lokaler Umgebungen und Runs |
| `src/__init__.py`, `src/__main__.py` | Engine-Version und CLI |
| `src/funktionen.py` | Bestehende mathematische Funktionen mit den unten dokumentierten Korrekturen |
| `src/data/{__init__,validate,normalize}.py` | CSV-Snapshots, Datenprüfung, gemeinsame Bewertungen, Risk-Free-Ausrichtung |
| `src/engine/{__init__,config,context,result,simulation}.py` | JSON-Vertrag, SimulationContext, StrategyResult und gemeinsamer Ablauf |
| `src/strategies/{__init__,buy_hold,rebalance,trend}.py` | Einzelanlage, jährliches Portfolio und SMA-Long/Cash |
| `src/analysis/{__init__,metrics}.py` | Einheitliche Zusammenfassung und Verfügbarkeitsstatus |
| `src/export/{__init__,results}.py` | Vollständige Run-Verzeichnisse, Manifest und SHA-256 |
| `configs/demo_buy_hold.json`, `configs/demo/*.csv` | Ausschliesslich künstliche Demo |
| `configs/demo_rebalance.json`, `configs/rebalance_demo/*.csv` | Zweite künstliche Demo, Buy-and-Hold und 60/40 im selben Run |
| `configs/demo_trend.json`, `configs/trend_demo/*.csv` | Dritte künstliche Demo mit getrennten Signal-/Performance-Reihen und allen drei Strategien |
| `tests/{conftest,test_functions,test_core}.py` | Synthetische Funktions-, Integrations- und CLI-Prüfungen |
| `tests/test_rebalance.py` | Allgemeine Gewichte, Zustandsfolge, Jahresereignisse, Multi-Asset-/Exportregression |
| `tests/test_trend.py` | SMA-Handrechnung, Warm-up, Signalquelle, Lag, Cash, Vergleich und Regression |

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

`performance_value` bestimmt ausschliesslich Marktrenditen. Optionales `signal_value` wird bei ausdrücklich so konfigurierter Trendfolge ausschliesslich für SMAs/Signale verwendet; ohne diese Verwendung bleibt es im Qualitätsbericht unbenutzt. Pflichtwerte, doppelte Spaltennamen, doppelte Markt-Schlüssel, doppelte Metadaten-IDs und doppelte Risk-Free-Perioden pro Reihe werden geprüft. Performance-Werte müssen endlich und positiv sein. Benötigte Signalwerte müssen reale numerische, vollständige und endliche Beobachtungen sein. Alle geladenen Markt-IDs benötigen Metadaten, verwendete Anlagen müssen zur Basiswährung passen. Es erfolgt keine Auffüllung, Interpolation, FX-Konvertierung oder erneute Total-Return-Bereinigung.

`align_performance()` unterstützt mehrere benötigte Anlagen: zuerst Schnittmenge tatsächlich vorhandener Bewertungen bilden, danach den gewünschten Zeitraum auswählen, erst anschliessend Renditen berechnen. Der Kontext verwendet jetzt die sortierte Vereinigung der Anlagen **aller aktivierten Strategien**; auch ein Buy-and-Hold-Asset ausserhalb der Rebalancing-Zielgewichte gehört dazu. Mindestens zwei Bewertungen müssen im gewünschten Zeitraum verbleiben. Entfernte nicht gemeinsame Termine und Beobachtungen ausserhalb des gewünschten Zeitraums werden separat berichtet. Zusätzliche unbenötigte Anlagen und Anlagen ausschliesslich deaktivierter Strategien bestimmen den Vergleichskalender nicht. Auch Anlagen mit explizitem Zielgewicht 0 benötigen Daten und Metadaten.

Die Demo-Konfigurationen zeigen den vollständigen JSON-Vertrag. Pflichtfelder sind `schema_version`, `run_name`, `period` mit `start/end`, `start_capital`, `base_currency`, `periods_per_year`, `data` mit `market/assets` und `strategies`. Unterstützt werden `buy_hold` mit `enabled/asset`, `rebalance` mit `enabled/target_weights/rebalance_frequency` und `trend` mit `enabled/asset/short_window/long_window/signal_lag/signal_source`. Mindestens eine Strategie muss aktiviert sein. Vorhandene Strategieblöcke werden vollständig geprüft, auch wenn sie deaktiviert sind; ihre Anlagen werden dann nicht für den Kontext angefordert. Es gibt keine fachlichen Defaults. Unbekannte Felder/Strategieoptionen, ungültige Typen und nicht endliche Zahlen werden abgelehnt. Relative Dateipfade beziehen sich auf die Konfigurationsdatei; ein fehlendes `output_dir` bedeutet technisch `outputs/runs` im aktuellen Arbeitsverzeichnis. URLs sind keine Datenreferenzen. Bestehende Core-/Rebalancing-Konfigurationen bleiben gültig.

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

Die Core-Prüfhilfen `_positive_periods()` und `_finite_returns()` dienen ausschliesslich der Eingabeprüfung. `buy_and_hold()`, `geometrisches_mittel()` und `annualisierte_volatilitaet()` werden mit validierten Eingaben wiederverwendet; ihre Formeln wurden nicht ersetzt. Die Rebalancing-Erweiterung härtete `neue_gewichtung()` und `rebalancing()`. Die Trend-Erweiterung refaktoriert ausschliesslich die bestehende `trendfolge()` auf einen gemeinsamen SMA-Helper; Einzelheiten stehen unten. Die übrigen vorhandenen Funktionen bleiben gegenüber dem akzeptierten Rebalancing-Tag unverändert.

## Exporte und Reproduzierbarkeit

Jeder erfolgreiche Lauf erzeugt unter `output_dir/<run_name>-<uuid>/` die Core-Dateien:

- `portfolio_history.csv`: Datum, Strategie, Vermögen, Periodenrendite und Drawdown; Start-Rendite leer.
- `summary.csv`: Start-/Endwert, Gesamtrendite, annualisierte Rendite/Volatilität, Sharpe und maximaler Drawdown. Nicht verfügbare Zahlen sind leer; ihr Grund steht im Manifest.
- `data_quality.json`: Status, geladene/benötigte Anlagen, ursprüngliche und effektive Grenzen, Beobachtungszahlen, entfernte Termine, Risk-Free- und Annualisierungsprüfung, Warnungen.
- `run_manifest.json`: Engine-/Schema-Version, Run-ID, UTC-Zeit, vollständig aufgelöste Konfiguration, gewünschte/effektive Grenzen, Währung, `m`, Eingabepfade und SHA-256, Git-Commit und Dirty-Status, Python-/Runtime-Paketversionen, Kennzahlstatus und Ergebnis-Hashes.

Bei aktiviertem Rebalancing kommen `weights_history.csv` und `trades.csv` hinzu, beide ebenfalls mit SHA-256 im Manifest. Ein ereignisfreier Rebalancing-Lauf hat eine korrekt benannte Trade-Tabelle mit Kopfzeile und ohne Datenzeilen. Ein reiner Buy-and-Hold-Lauf behält genau vier Dateien; ihm werden keine Gewichts-/Trade-Zeilen erfunden. Mehrere Strategien werden in Verlauf und Summary gemeinsam exportiert, ohne ihre Zahlen miteinander zu vermischen. Sortierung: `strategy,date`, bei Gewichten/Trades zusätzlich `asset_id`, jeweils stabil. Die Summary hat eine Zeile pro Strategie in Namensreihenfolge.

Eine tatsächlich ausgeführte Trendstrategie ergänzt `signals.csv`, ebenfalls atomisch und mit SHA-256. Ohne Signaldaten wird diese Datei nicht erzeugt. Die Startposition ist die einzige reguläre Zahlenlücke dieser Tabelle; Warm-up-Zeilen werden nicht exportiert.

JSON wird mit `allow_nan=False` geschrieben. Verfügbarkeitsfelder verwenden `null`, CSV-Zahlenlücken erhalten einen nachvollziehbaren Status. Der nicht beobachtete Startwert der Rendite ist die einzige reguläre Datenlücke im Verlauf. Numerischer Überlauf oder nicht endliche berechnete Ergebnisse führen zum Fehler.

Eingabe-Hashes beschreiben die gelesenen Bytes; vor dem Export wird eine zwischenzeitliche Dateiänderung abgefangen. Zusätzlich zu Git werden alle Python-Quellen und, im Checkout, `pyproject.toml` und `requirements.lock` gehasht, damit ein Dirty-Lauf unterscheidbar bleibt. Bei einer Wheel-Installation ausserhalb eines Git-Checkouts sind Git-Commit/Dirty ausdrücklich `null` mit Status `unavailable`; die installierten Python-Quellen werden weiterhin gehasht. Für archivierte wissenschaftliche Runs sind die Eingabedateien und der passende Checkout bzw. das installierte Paket zusätzlich aufzubewahren; der Core kopiert sie nicht in den Ergebnisordner.

Resultate werden erst vollständig in einem temporären Verzeichnis geschrieben und anschliessend innerhalb derselben Ausgabeablage umbenannt. Bestehende Runs werden nicht überschrieben. Run-ID und Zeitstempel variieren; fachliche CSV-Dateien und Datenqualitätsbericht sind bei identischen Inputs und Code bytegleich. Das Manifest hasht alle übrigen Ergebnisdateien: drei Basisdateien, gegebenenfalls zwei Rebalancing-Dateien und eine Signaldatei. Es enthält keinen eigenen Selbst-Hash.

## Ursprüngliche Core-Demo vom 2026-10-03

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

Noch nicht implementiert: BIP-Strategie und historische BIP-Verfügbarkeit, reale Datenadapter, FRED-Zinsumrechnung, FX, verzinstes Cash, Long/Short, Transaktionskosten, Steuern, Inflation, Batch, Web/API, Parameteroptimierung, reale Hauptversuche und Zusatzanalysen. Rebalancing unterstützt ausschliesslich `annual`; Trend ausschliesslich Lag 1 und unverzinstes Long/Cash. Die unveränderte Core-Prüfung der Annualisierung ist weiterhin auf die oben beschriebenen Kalendergitter beschränkt; es gibt keine Börsenkalender-Aufbereitung.

Vom Autor vorgegeben sind Datenvertrag, mathematische Definitionen, OD-01 bis OD-13 und die Arbeitsgrenze. Codex hat Paketname, strikten JSON-Vertrag, CSV-Lesetechnik, optionale Frequenzdeklaration als Prüfhilfe, Verfügbarkeitsstatus, Hashes, Exportablauf und synthetische Tests technisch umgesetzt. Neue finanzwirtschaftliche Regeln wurden nicht beschlossen; `decisions.md` wurde nicht geändert. Endgültige Versuchswerte bleiben beim Autor. Die bestandenen synthetischen Tests ersetzen keine fachliche Abnahme oder Prüfung realer Daten. Geschützte Notebooks, Methodik, Bibliographie und Buchkapitel bleiben unverändert.

## Multi-Asset- und Rebalancing-Erweiterung vom 2026-10-04

`RunConfig` ergänzt Aktivierung, immutable sortierte Zielgewichts-Paare und `rebalance_frequency`. `required_assets` ermittelt die Vereinigungsmenge für genau einen Kontext. Die vorhandenen CSV-/Kalender-/RF-Prüfungen werden weiterverwendet, ohne eine zweite Datenaufbereitung in der Strategie. `BuyAndHold` und gemeinsame Kennzahlenformeln sind unverändert. Beide Strategien lesen den Kontext, kopieren die benötigten Performance-Werte und verändern keine gemeinsam verwendeten Daten.

`RunOutcome.results` enthält alle Ergebnisse als Mapping nach Strategienamen. Für bestehende Python-Aufrufe bleibt `.result` verfügbar: das in Namensreihenfolge erste Ergebnis, damit bei aktiviertem Buy-and-Hold weiterhin dessen Ergebnis. Ohne Buy-and-Hold ist dies Rebalancing oder bei Trend allein das Trend-Ergebnis. Der bestehende Einzelstrategie-Status `metric_status` bleibt im Manifest erhalten; `metric_status_by_strategy` liefert für jeden Run einen einheitlichen Strategienamen-zu-Status-Nachweis. `executed_strategies` nennt die ausgeführten Strategien. Es gibt keine Plugin-Plattform und keine zweite CLI-Logik.

### Zielgewichte und Wiederverwendung

Zielgewichte sind ausdrücklich konfigurierte, nichtnegative reale Zahlen mit Summe 1. Die absolute Toleranz für Gewichtssummen und Gewichtszustände beträgt **1e-12**; Kapitalvergleiche haben relative Toleranz **1e-12**, und die tolerierte absolute Transaktionssumme beträgt `portfolio_value * 1e-12`. Diese technischen Rundungstoleranzen werden in `src/funktionen.py` zentral benannt. Es wird keine falsche Summe normalisiert, kein Cash ergänzt und kein Default 60/40 gewählt. Werte nahe 1 innerhalb der Toleranz bleiben unverändert; die Prüfungen erlauben nur entsprechend kleine Rundungsabweichungen der Kapitalbilanz.

Die Audit-Gegenbeispiele wurden vor der Änderung erneut ausgeführt: `neue_gewichtung({A:60,B:40},{A:0.1})` lieferte `A=66,B=NaN` und Gewicht `A=1`; `rebalancing({A:60,B:40},{A:0.5,B:0.4})` erzeugte Transaktionssumme −10. Beide Fälle werden jetzt abgelehnt, wie vom aktuellen Prompt und OD-13 erlaubt.

- `neue_gewichtung()`: eindeutige nicht leere Asset-Labels, exakt gleiche Labelmengen, vollständige endliche reale Renditen und nichtnegative Positionen mit positivem endlichem Gesamtwert prüfen. Anders angeordnete Labels werden ausdrücklich auf die Positionsreihenfolge ausgerichtet. Die vorhandene Formel `value * (1 + return)` und die Gewichtsermittlung bleiben erhalten. Renditen ≤ −100 % werden für die positiven Performance-Reihen abgelehnt; numerischer Über-/Unterlauf wird nicht als gültiger Zustand übernommen.
- `rebalancing()`: dieselben Positions-/Labelprüfungen, geprüfte Zielgewichte und Kapitalerhaltung. Die bestehenden Zielwert-, Transaktions- und Gewichtsformeln sowie die fünfteilige Rückgabe bleiben erhalten. Der Helper berechnet die Transaktionen; die neue Strategie übernimmt die Zielwerte als tatsächlichen Folgezustand.
- Neu: `validate_target_weights()`, `_asset_vector()`, `_position_values()` und `_same_assets()` bündeln diese Eingabeprüfungen. Extrem grosse, auch einzeln endliche Gewichte werden vor einer überlaufenden Summe abgelehnt. Es gibt keine zweite unabhängige Sammlung von Rebalancing-Formeln.

`StrategyResult` prüft zusätzlich die vollständigen Datum-/Asset-Raster, feste Zielgewichte, Gewichts- und Kapitalbilanzen sowie die Tradegleichung. Die Orchestrierung und der Export prüfen, dass jede Strategie genau den gesamten Kontextkalender liefert. Optionale Dateien werden innerhalb des bestehenden atomischen Exportablaufs geschrieben und erst danach gemeinsam veröffentlicht.

### Zustandsfolge und Jahresereignisse

Am effektiven Start gilt `position_value = start_capital * target_weight`. Die Startzeile ist unverändert eine Bewertung ohne beobachtete Rendite; die anfängliche Allokation erzeugt keinen Trade.

Für jedes folgende Intervall: gehaltene Positionen mit Asset-Renditen fortschreiben → Portfoliowert und echte Portfoliorendite berechnen → Driftgewichte ausweisen → gegebenenfalls Rebalancing berechnen → Zielpositionen für das nächste Intervall übernehmen. Der Portfoliowert am Ereignisdatum ist der bereits verdiente Wert vor den kostenfreien Trades und bleibt innerhalb der dokumentierten Toleranz danach identisch.

Ein Ereignis liegt am letzten gemeinsamen Bewertungsdatum eines Kalenderjahres, wenn das nächste vorhandene Bewertungsdatum in einem anderen Jahr liegt. Dafür wird nur der vorbereitete Bewertungskalender betrachtet, kein späterer Performance-Wert. Die Startbewertung wird nicht erneut rebalanciert. Das letzte Datum des gesamten Laufs erzeugt unabhängig vom Jahresultimo keine Abschlusstransaktionen. Fehlende Kalenderdaten werden nicht ergänzt.

### Gewichtungs- und Trade-Semantik

`weights_history` enthält jede Bewertung und jedes Rebalancing-Asset genau einmal:

| Datum | `weight_before` | `target_weight` | `weight_after` |
|---|---|---|---|
| Start | Initiales Zielgewicht | Konfigurierte Referenz | Initiales Zielgewicht |
| Ohne Ereignis | Tatsächliches Gewicht nach Rendite | Konfigurierte Referenz | Unverändertes Driftgewicht |
| Jahresereignis | Tatsächliches Gewicht nach Rendite, vor Trade | Konfigurierte Referenz | Tatsächlich gehaltenes Gewicht nach Trade |

Eine Referenz-Zielspalte an jedem Datum bedeutet kein periodisches Zurücksetzen. Vor-/Nachgewichte summieren je Datum zu 1 innerhalb der Toleranz.

`trades` enthält nur tatsächliche geplante Jahresereignisse mit `transaction_value = target_value - value_before`, positiven Werten für Käufe und negativen für Verkäufe. Bei einem Ereignis werden alle Assets dokumentiert, auch bei Transaktionswert 0. Initiale Aufteilung und endgültiges Laufende erzeugen keine Trades. Je Ereignis stimmen Positions- und Zielsumme überein; die Transaktionssumme ist 0 innerhalb der Kapitaltoleranz.

### Zweite künstliche Demo und Regression

```powershell
.\.venv\Scripts\python.exe -m maturarbeit_engine run --config configs/demo_rebalance.json
```

Tatsächlich geprüfter neuer Run: `outputs/runs/synthetic_rebalance-7535fb30fd80407f9fa5fe04522e0d26/`. Anlagen sind ausschliesslich `EQ_SYNTH` und `BD_SYNTH`, Kapital 100 CHF, Demo-Zielgewichte 60/40. Diese Angaben wählen keine realen Versuchsanlagen oder Untersuchungsparameter aus.

| Datum | Aktien-/Anleihenwertreihe | Rebalancing-Portfolio | Zustand |
|---|---|---:|---|
| 2020-01-31 | 100 / 100 | 100 | Initiale Positionen 60 / 40 |
| 2020-06-30 | 110 / 100 | 106 | Positionen 66 / 40; Aktiengewicht 66/106 |
| 2020-12-30 | 121 / 100 | 112.6 | Erst Positionen 72.6 / 40, dann Zielpositionen 67.56 / 45.04 |
| 2021-06-30 | 108.9 / 110 | 110.348 | Neue Zielpositionen verdienen −10 % / +10 %: 60.804 / 49.544 |
| 2021-12-31 | 119.79 / 110 | 116.4284 | Positionen 66.8844 / 49.544; kein Abschlusstrade |

Am 2020-12-30: Aktien verkaufen 5.04, Anleihen kaufen 5.04; Kapital vor/nach Trades 112.6. Rebalancing-Gesamtrendite **16.4284 %**, maximaler Drawdown **−2 %**. Buy-and-Hold derselben Aktienreihe endet bei **119.79**, Gesamtrendite **19.79 %**, maximaler Drawdown **−10 %**. Ein fälschliches Zurücksetzen nach jedem Intervall ergäbe schon vor dem Jahresereignis 112.36 statt 112.6.

Die fünf Demo-Bewertungen bilden absichtlich kein regelmässiges Periodengitter. `period_frequency=null` ist explizit; der konfigurierte Demo-Wert `periods_per_year=12` wird nicht zur stillen Kalenderannahme. Annualisierte Rendite/Volatilität/Sharpe bleiben für beide Strategien mit Status `period_frequency_not_declared` nicht verfügbar. Die vier RF-Intervalle sind vollständig und exakt ausgerichtet. Zusätzliche reguläre monatliche Tests prüfen Sharpe für beide Strategien mit jeweils eigenen Renditen gegen dieselbe RF-Reihe.

Der ursprüngliche Buy-and-Hold-Demo-Lauf wurde ebenfalls erneut ausgeführt: `outputs/runs/synthetic_buy_hold-81a32b30ed1442b185e762ed5b841f0d/`, weiterhin **100 → 110 → 99**. Beide fachlichen CSV-Dateien und `data_quality.json` sind bytegleich zum vor der Erweiterung erzeugten Kontrolllauf. Unterschiedliche Run-Metadaten und die neue Engine-/Codeversion sind ausdrücklich erlaubt. Alle neuen und bisherigen Exporte, Standard-JSON, Eingabe-/Code-/Ergebnis-Hashes und Kapitalbilanzen wurden kontrolliert; siehe [testing.md](testing.md).

Neue fachliche Entscheidungen waren für Rebalancing nicht erforderlich. Technische Entscheidungen von Codex in jenem Schritt: additive Konfigurationsfelder, sortierte Vereinigungsmenge, rückwärtskompatibles Result-Mapping, benannte Rundungstoleranzen, einheitliche Mehrstrategien-Sortierung, optionale Exporte und Versionsnummer 0.2.0. Der damalige Auftrag endete nach Rebalancing. Trendfolge wurde anschliessend separat bestätigt; BIP bleibt einem späteren Auftrag vorbehalten.

## Trend-Erweiterung vom 2026-10-04

### Konfiguration und Datenrollen

`Trend.run(context, params)` benötigt ausdrücklich `asset`, `short_window`, `long_window`, `signal_lag` und `signal_source`; der JSON-Block zusätzlich `enabled`. Fenster sind positive ganze Zahlen, keine Bool-Werte und keine gerundeten Dezimalzahlen; `short_window < long_window`. Lag ist exakt die ganze Zahl 1. Unterstützte Quellen sind ausschliesslich `signal_value` und `performance_value`. Unbekannte Optionen für Short, Cash-Verzinsung oder Filter werden abgelehnt.

Die Quelle bestimmt nur die SMA-Basis. Marktrenditen entstehen stets aus `performance_value` des gemeinsamen Kontextkalenders. Bei `signal_source="signal_value"` führen eine fehlende Spalte oder fehlende/nicht numerische/nicht endliche benötigte Beobachtungen zum Fehler für den gesamten Run. Es gibt keinen Fallback. `signal_source="performance_value"` ist eine ausdrücklich konfigurierte zweite Möglichkeit, die in der aufgelösten Manifest-Konfiguration erhalten bleibt; eine daneben liegende unbenutzte Signalspalte wird nicht als Ersatz verwendet.

### Warm-up, SMA und Zeitfolge

Die Performance-Vereinigungsmenge enthält jetzt auch das aktivierte Trend-Asset, selbst wenn es nicht in den anderen Portfolios liegt. Der vorhandene Core bereitet zuerst den gemeinsamen Performance-Kalender auf. `prepare_trend_signals()` bereitet danach eine zusätzliche Sicht der konfigurierten Signalquelle vor, ohne den Performance-Kalender zu verändern.

Die Fenster zählen tatsächlich beobachtete Werte der Trend-Anlage, gemäss Theorie 3.12.1. Verwendet werden die letzten `long_window - 1` vorhandenen Beobachtungen vor dem **effektiven** gemeinsamen Start sowie die eigene beobachtete Signalhistorie vom effektiven Start bis zum effektiven Ende. Ältere nicht benötigte Signaldaten und spätere Daten liegen ausserhalb dieser Sicht. Benötigte Fehlwerte werden nicht entfernt, um stattdessen weiter zurückliegende gültige Werte einzusetzen. Zusätzliche Signalbeobachtungen zwischen gemeinsamen Bewertungsterminen bleiben für den SMA beobachtete Historie; Signale für Positionen werden ausschliesslich an den gemeinsamen Performance-Bewertungen entnommen. Der Lag zählt diese gemeinsamen Bewertungen, keine Zwischenbeobachtungen. Es wird weder resampelt noch interpoliert.

`SimulationContext.trend_signals` enthält die an den gemeinsamen Bewertungen vorbereiteten Signalwerte, SMAs und Signale. Alle exportierten SMAs müssen definiert sein, insbesondere beide am Start. Fehlt genügend Vorlauf, scheitert der gesamte Run ohne späteren Trendstart. Vorlaufwerte verdienen keine Rendite, verändern das Startkapital nicht und zählen nicht zur Kennzahlenstichprobe. Der Qualitätsbericht enthält Trend-Asset/Quelle, verfügbare historische Zeilenzahl, benötigtes langes Fenster, tatsächlich verwendete Vorlaufzahl/-grenzen, effektiven Start und `valid_start_signal=true`. Die verfügbare Zahl zählt gelieferte Beobachtungen; die tatsächlich verwendeten werden vollständig validiert.

SMA ist der arithmetische Mittelwert der letzten N Signalbeobachtungen. `signal(t)=1` gilt ausschliesslich bei `sma_short(t)>sma_long(t)`, sonst 0; Gleichheit ist Cash. Es gibt keine Toleranzzone, Optimierung oder zusätzliche Filter. Für eine bei t endende Renditeperiode gilt `position(t)=signal(t-1)` und `strategy_return(t)=position(t)*market_return(t)`. Das Startsignal steuert die erste folgende Periode. Das aktuelle Signal steuert niemals die gerade vergangene Rendite. Long verdient die Marktrendite; Cash verdient exakt 0, auch bei positiver oder negativer Marktrendite. Die RF-Reihe bleibt allein Vergleich für Sharpe.

### Gemeinsame Mathematik und Resultate

Vor dem Refactoring regulär reproduziert: `trendfolge([1,2,3],2,3)` setzte Signal 0 und Strategierendite 0 vor gültigem langen SMA. Bei `[1,NaN,3,4]` entfernte es die zweite Beobachtung und berechnete eine künstlich überbrückte Rendite. Dies ist der bereits dokumentierte und im Trend-Prompt zur Korrektur freigegebene Audit-Befund, kein neu entschiedener Strategiewechsel.

Neu in `src/funktionen.py`: `validate_sma_windows()` und **ein** `sma_signal()`-Helper mit vollständigen Fenstern, eindeutigen geordneten Indizes und vollständigen endlichen realen Werten. Während der noch undefinierten Anlaufphase bleiben Signale NaN. Die alte `trendfolge()` behält Namen und sechs Ausgabespalten als explizites Einreihen-Beispiel; sie verwendet denselben Helper und `prozentuale_aenderung()`, entfernt keine Zeilen und erzeugt kein künstliches Anlauf-Cash. Die Engine kombiniert die getrennte Performance-Rendite ausschliesslich in `Trend`, verwendet die bestehenden Vermögens-/Drawdown-Funktionen und verändert die anderen mathematischen Funktionen nicht.

`StrategyResult` prüft Signalspalten, vollständigen gemeinsamen Kalender, Asset, endliche SMAs, binäre Signalwerte, exakten SMA-Vergleich und verzögerte Positionen. Die gemeinsame Resultprüfung vergleicht zusätzlich mit vorbereitetem Signal-Kontext und Performance-Rendite. Buy-and-Hold, Rebalancing, RF-Ausrichtung und Kennzahlenformeln bleiben unverändert. Alle Strategien kopieren ihre benötigten Daten und verändern den geteilten Kontext nicht.

`signals.csv` hat exakt `date,strategy,asset_id,signal,position,signal_value,sma_short,sma_long`. `signal` beschreibt die Entscheidung an diesem Datum; `position` beschreibt die Position der dort endenden Renditeperiode. Am Start ist Position leer, danach das Signal der vorherigen Bewertung. Signalwert und beide SMAs gehören zum angegebenen Datum. Die letzte Entscheidung darf dokumentiert sein, auch ohne nächste Periode. Exportiert werden nur Untersuchungsbewertungen, keine Vorlaufzeilen. Sortierung und Hash-/Exportablauf entsprechen den bestehenden optionalen Tabellen.

### Dritte künstliche Demo

```powershell
.\.venv\Scripts\python.exe -m maturarbeit_engine run --config configs/demo_trend.json
```

Tatsächlich geprüfter Run: `outputs/runs/synthetic_trend-d5d6bcd322664a9d9f2a6665ba67fe43/`. Alle drei Strategien verwenden sieben Monatsendbewertungen, Kapital 100 CHF und explizites `m=12`. Demo-Fenster 2/3, Lag 1 und künstliche Anlagen legen keine Werte des Hauptversuchs fest. Vorlauf: 2019-11-30 und 2019-12-31 mit Signalwert jeweils 10; nur die Trend-Anlage besitzt diese Vorlaufzeilen.

| Bewertung | Performance-Wert | Signalwert | SMA kurz | SMA lang | Signal | Position | Trendvermögen |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2020-01-31 | 100 | 10 | 10 | 10 | 0 | leer | 100 |
| 2020-02-29 | 80 | 20 | 15 | 40/3 | 1 | 0 | 100 |
| 2020-03-31 | 88 | 30 | 25 | 20 | 1 | 1 | 110 |
| 2020-04-30 | 70.4 | 10 | 20 | 20 | 0 | 1 | 88 |
| 2020-05-31 | 140.8 | 10 | 10 | 50/3 | 0 | 0 | 88 |
| 2020-06-30 | 70.4 | 30 | 20 | 50/3 | 1 | 0 | 88 |
| 2020-07-31 | 77.44 | 30 | 30 | 70/3 | 1 | 1 | 96.8 |

Trendrenditen: **0, +10 %, −20 %, 0, 0, +10 %**. Das Februar-Signal Long beeinflusst nicht den bereits vergangenen Marktverlust −20 %. Das April-Signal Cash vermeidet nicht rückwirkend den im Long verdienten Verlust. Mai +100 % und Juni −50 % bleiben bei gehaltenem Cash ohne Vermögensänderung.

Trend: Gesamtrendite **−3.2 %**, annualisierte Rendite **−6.2976 %**, annualisierte Volatilität **37.9473319220 %**, Sharpe **−0.0475924749**, maximaler Drawdown **−20 %**. Buy-and-Hold endet bei **77.44**, Rebalancing bei **86.464**. Das regelmässige Monatsendgitter erlaubt die bestehenden annualisierten Kennzahlen; die sechs synthetischen RF-Intervalle werden für alle Strategien identisch verwendet. Die Trend-Demo erzeugt sieben Dateien, darunter sieben Signalzeilen und eine Rebalancing-Trade-Tabelle ohne Ereigniszeilen.

Die ursprünglichen Buy-and-Hold-/Rebalancing-Demos wurden erneut ausgeführt; ihre fachlichen CSVs und Qualitätsberichte sind bytegleich zu den vor der Trend-Erweiterung erzeugten Kontrollläufen. Details und sämtliche Test-/Hashnachweise stehen in [testing.md](testing.md).

Technische Entscheidungen durch Codex: additive Konfigurations-/Kontextfelder, einmal vorbereitete SMA-Sicht, vollständige Resultprüfung, Wiederverwendung des optionalen Exports und Version 0.3.0. Keine neue finanzwirtschaftliche Entscheidung war nötig. Die akzeptierte Core-/Rebalancing-Abnahme bleibt erhalten; fachliche Trend-Abnahme steht aus. Keine endgültige Versuchsauswahl, kein BIP und keine weiteren ausgeschlossenen Funktionen. Dieser Auftrag endet nach Trend.
