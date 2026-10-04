# Engine v1.0 – technischer Release und Freeze

**Datum:** 2026-10-04. **Release-Version:** 1.0.0. **Konfigurationsschema:** unverändert 1.0.
**Auftrag:** [Vollständiger Release-/Freeze-Prompt](../ai-usage/prompts/2026-10-04-engine-v1-release-freeze.md). Regeln: `AGENTS.md` und die verbindlichen [Entscheidungen](decisions.md).

## Ausgangspunkt und Bedeutung

Der erfolgreiche [Freeze-Re-Audit](freeze-reaudit.md) ist in Commit **`27470204e3805a18a11f6630813b982b3174ea0d`** dokumentiert und enthält das Urteil `ENGINE-V1.0-FREEZE TECHNICALLY READY`. Er prüfte Engine 0.4.3, Code-Commit `270b7969a46bfbdb9f4614a4f6d88507540f6b92`. Der Release-Auftrag begann sauber auf Branch `engine-v1`, HEAD `04cab0673bfe48f733b3e50dd531ee282ff16a88`; gegenüber dem Re-Audit-Commit war ausschliesslich der Release-Prompt hinzugefügt.

Version 1.0.0 bezeichnet den technischen Freeze der geprüften allgemeinen Engine. Der Versionswechsel betrifft ausschliesslich `pyproject.toml` und `src/__init__.py`, jeweils 0.4.3 → 1.0.0. Keine Engine-Logik, Finanzformel, Validierung, Strategie, Testdatei, Config, Demodatei oder Abhängigkeitsbindung wird verändert. Die ergänzte Dokumentation führt bestehende Verträge zusammen; sie trifft keine neuen fachlichen Entscheidungen. Ein Release-Commit und der vorgesehene Tag `engine-v1.0` werden in diesem Auftrag ausdrücklich **nicht erstellt**.

**Engine v1.0 ist weder der Abschluss der Maturarbeit noch eine Freigabe realer Daten oder Hauptläufe.** Endgültige Versuchswerte und historische Quellenbelege bleiben beim Autor. Die technischen Prüfungen mit künstlichen Daten ersetzen dessen fachliche Kontrolle nicht.

## Eingefrorene fachliche Grenze

OD-01 bis OD-13 bleiben vollständig verbindlich. Nach diesem Release dürfen methodisch relevante Änderungen nur über eine neue Engine-Version erfolgen.

| Vertrag | Eingefrorene Regel |
|---|---|
| OD-01, gemeinsamer Kalender | Schnittmenge tatsächlich vorhandener Bewertungen aller aktiv benötigten Performance-Anlagen vor der Renditebildung; entfernte Termine berichten. Keine Interpolation, kein Forward-Fill, keine erfundenen Feiertags-/Marktwerte. |
| OD-02, Start | Erste gemeinsame gültige Bewertung am/nach gewünschtem Start: Startkapital, nicht beobachtete Rendite, Drawdown 0. Letzte Bewertung am/vor gewünschtem Ende; effektive Grenzen ausweisen. |
| OD-03, Annualisierung | Explizites `periods_per_year`; Jahreskennzahlen nur bei nachgewiesener kompatibler Periodik. Keine Frequenzvermutung oder Ersatz-CAGR. |
| OD-04/05, Trend | Vollständiger eigener beobachteter SMA-Warm-up vor effektivem Start, kein Warm-up-Ertrag. Gültiges Startsignal erforderlich; Long/Cash, Cash-Rendite 0. |
| OD-06, Portfoliozustandsfolge | Initiale Ziele → Rendite tatsächlich gehaltener Positionen → Drift → jährlicher Trade → neue gehaltene Positionen für die Folgeperiode. Letzter gemeinsamer Jahrestermin mit vergangener und folgender Periode; kein erneuter Start- oder wirkungsloser Abschlusstrade. |
| OD-07, Risk-Free | Vorgelagert normalisierte Dezimal-Periodenrenditen mit Serienidentität und exakt gleichen Anfangs-/Endgrenzen. Keine Jahreszinskonversion oder Nullersetzung innerhalb der Simulation. |
| OD-08, Sharpe | `mean(r-rf) / std(r-rf, ddof=1) * sqrt(periods_per_year)` aus vollständigen, endlichen, exakt ausgerichteten echten Renditeperioden; Startzeile ausschliessen. |
| OD-09, Drawdown | Startkapital ist anfänglicher High-Water-Mark; vollständiger Pfad und Maximum einschliesslich des ersten Verlusts. |
| OD-10, Währung | Bereits kompatible Basiswährung aller gemeinsam ausgewerteten Anlagen; keine FX-Konversion oder Absicherung. |
| OD-11, Ländergewichtung | Reines `GDP_country / sum(GDP_all_configured_countries)`, je Land ein expliziter Proxy; keine zusätzliche Binnenlandgewichtung oder gemischte Kommer-/Faktorlogik. |
| OD-12, historische Information | Nur Versionen mit `available_from <= Entscheidungsdatum`; jüngstes gemeinsames GDP-Jahr aller konfigurierten Länder, je Land letzte damals verfügbare Revision. Keine Länderentfernung, Jahresmischung oder rückwirkende heutige Revision. |
| OD-13, Kapital | Vollständig investiertes Long-only-Portfolio, nichtnegative Ziele, Summe 1 innerhalb bestehender Toleranz; keine Normalisierung, Short, Hebel oder beliebiges Rest-Cash. Positives nicht darstellbares Allokationsprodukt führt zum Abbruch. |

Die vier implementierten Strategien sind **Buy-and-Hold**, **jährliches Fixed Rebalancing**, **SMA Long/Cash mit Lag 1** und **reine GDP-Country-Weighting-Strategie**. Der SMA ist der arithmetische Mittelwert eigener Beobachtungen; strikt kurzer SMA > langer SMA ergibt Long, Gleichheit Cash. Das vorherige gemeinsame Signal steuert die nächste Renditeperiode. GDP-Ziele werden initial und an bestätigten Jahresereignissen historisch bestimmt; ihre Wirkung beginnt nach dem jeweiligen Trade.

## Lokale Daten- und Konfigurationsverträge

Import/Aufbereitung und Simulation bleiben getrennt. Ein Backtest liest nur lokale Dateien. Die strikten JSON-Configs deklarieren Parameter ausdrücklich; unbekannte Felder, doppelte Schlüssel, ungültige Typen und nicht endliche Werte werden abgelehnt. Es werden keine endgültigen Studienparameter aus den künstlichen Demos übernommen.

CSV-Vertrag: UTF-8, optional BOM; Kommatrennung; ISO-Daten `YYYY-MM-DD`. Benannte eindeutige Header und exakt gleiche Feldbreite jedes CSV-Datensatzes werden **vor pandas** geprüft. Korrekt gequotete Kommas/Zeilenumbrüche und vollständig benannte Zusatzspalten bleiben zulässig. Ein NUL-Byte irgendwo in den unveränderten Originalbytes verwirft die gesamte Datei vor Dekodierung/Parsing; keine Kürzung, Reparatur oder implizite Indexinterpretation.

| Eingabe | Pflichtspalten und Bedeutung |
|---|---|
| Markt | `date,asset_id,performance_value`; vollständig, endlich, strikt positiv, eindeutiges Datum/Asset. Optionales `signal_value` nur als ausdrücklich gewählte SMA-Quelle. Total-Return-Bedeutung muss die vorgelagerte Aufbereitung belegen. |
| Metadaten | `asset_id,name,asset_class,country,currency,provider,provider_symbol`; eindeutige Assetidentität, benötigte Anlage/Land/Währung konsistent. |
| Risk-Free | `period_start,period_end,series_id,period_return`; normalisierte, vollständig ausgerichtete Perioden. Fehlende ganze Dateireferenz ergibt nicht verfügbare Sharpe; eine referenzierte fehlerhafte/lückenhafte Serie scheitert. |
| Makro | `period,country,indicator,value,unit,available_from`; vierstelliges Referenzjahr, positive endliche GDP-Werte, nachvollziehbare Verfügbarkeit. Identische vollständige Versionen deduplizieren und zählen; widersprüchliche gleiche Versionsschlüssel ablehnen. |

Die historische Wahrheit von `available_from`, Total-Return-Bedeutung, Einheitenvergleichbarkeit und realer Zinskonversion kann die Engine aus Zahlen allein nicht belegen. Die gemeinsame Performance-Zeitachse wird weder durch Signal-Warm-up noch durch Makrotermine verlängert.

## Resultate, Export und Reproduzierbarkeit

Alle aktivierten Strategien liefern denselben effektiven Kalender, Startwert, Währung und RF-Vergleich. Die vollständige Run-/Exportgrenze prüft Strategie-Set, konfigurierte Assets/Ziele, jährliche Ereignisse, tatsächliche Marktportfolio-Zustandsfolge, historische GDP-Entscheidungen, SMA/Lag, gesamten Drawdown und Summary samt kanonischen Verfügbarkeitsstatus. Vor Veröffentlichung werden Eingabe-Hashes erneut geprüft; bestehende mathematische und Portfoliofunktionen bleiben die gemeinsame Berechnungsbasis.

| Datei | Vertrag |
|---|---|
| `portfolio_history.csv` | Strategie/Datum, Vermögen, echte Periodenrendite und Drawdown; nur Start-Rendite leer. |
| `summary.csv` | Eine geordnete Zeile je Strategie, Start-/Endwert, Gesamt-/Jahresrendite, Jahresvolatilität, Sharpe und maximaler Drawdown. Fehlende Kennzahlen leer mit begründetem Manifeststatus. |
| `data_quality.json` | Validierung, Kalender, entfernte Beobachtungen, effektive Grenzen, RF/Annualisierung sowie gegebenenfalls Warm-up und angewandte GDP-Versionen. |
| `weights_history.csv`, `trades.csv` | Nur bei Portfolio-Strategien; Vor-/Ziel-/Nachgewichte und echte Jahresereignisse mit Vortrade-/Ziel-/Transaktionswerten. Ereignislose Trades behalten Header. |
| `signals.csv` | Nur bei Trend; gültige Untersuchungs-SMAs/Signale, verzögerte Position, keine Warm-up-Zeilen. Startposition leer. |
| `run_manifest.json` | Version/Schema, UUID/UTC, aufgelöste Config, gewünschte/effektive Grenzen, explizite Frequenz/Jahresbasis, Input-/Code-/Result-SHA-256, Umgebung, Git/Dirty und Kennzahlstatus. Kein Manifest-Selbsthash. |

Ausgabe erfolgt vollständig über Staging und Rename unter einem neuen Run-Namen; vorhandene Runs werden nicht überschrieben. JSON enthält kein NaN/Infinity. Alle nicht zum Manifest gehörenden Ergebnisdateien werden gehasht. Original-Inputbytes werden vor Parsing gehasht; Pythonquellen und im Checkout zusätzlich `pyproject.toml`/`requirements.lock` erhalten Einzel- und Gesamtfingerprints. Ein Wheel ohne Git-Zuordnung nennt Git ausdrücklich `unavailable`, Commit/Dirty null.

Hashes ersetzen kein wissenschaftliches Archiv. Für reale Läufe sind passende Raw-/Processed-Inputs, Config, Transformationen, Wheel/Codeversion und Abhängigkeitsdistributionen zu erhalten; der tatsächlich ausgeführte Code muss während des ganzen frischen Prozesses unverändert bleiben. Quellhashes werden beim Export gelesen. Zufällige Run-ID, Zeit und Installationsprovenienz dürfen abweichen; fachliche CSVs und Qualitätsbericht bleiben bei denselben Eingaben und Berechnungen gleich.

## Geschlossene technische Blocker

Aktuelle Abnahme ist der erfolgreiche 0.4.3-[Freeze-Re-Audit](freeze-reaudit.md). Ältere [Auditbefunde](final-open-issues.md) und der [Blocker-Re-Audit](blocker-reaudit.md) bleiben unveränderte historische Nachweise ihrer damaligen Stände; ihre damaligen offenen Urteile werden durch die spätere technische Prüfung eingeordnet.

| Befund | Finaler Status / Sicherung |
|---|---|
| EB-01 | **CLOSED** – positive Zielpositionen gegen Null-Unterlauf am Start und bei jährlichen Allokationen beider Portfolios abgesichert. |
| EB-02 | **CLOSED** – vollständige Drawdown-/Summary-/Status-/Strategie-/Config-/GDP-Bindung und wirtschaftliche Zustandsrekonstruktion vor Export. |
| EB-03 | **CLOSED** – exakte CSV-Feldbreite, Header/Quotes und erhaltende Spalteninterpretation vor pandas. |
| NEW-EB-01 | **CLOSED** – vollständige NUL-Byte-Ablehnung, alle vier Dateiklassen, Quotes/BOM, Header/Zusatzfelder und Minimalfall geprüft. |

Der Freeze-Re-Audit fand **0 neue ENGINE-BLOCKING-Befunde im gezielt geprüften Bereich** und bestätigte je Installation zusätzlich 205 temporäre Gegenkontrollen. Der Release führt keine neuen Fixes aus und erklärt keine allgemeine Fehlerfreiheitsgarantie.

## Offene Studienvoraussetzungen und technische Grenzen

Alle sieben **STUDY-BLOCKING**-Punkte bleiben vor realen Hauptläufen offen. Sie blockieren den technischen Release nicht und werden hier nicht gelöst.

| Punkt | Vor der realen Studie durch den Autor festzulegen / zu belegen |
|---|---|
| SB-01 | Reale Performance-/Total-Return-Reihen, Anlagen/Indizes, Proxies/Benchmark, Investierbarkeit, Dividenden-/Split-/bereits enthaltene Gebührenbehandlung und kompatible Währungsbasis. |
| SB-02 | Untersuchungszeitraum, Startkapital, tatsächlich gemeinsame Frequenz/Kalender, effektive Grenzen und begründete Annualisierungsbasis; bei Börsentagen gegebenenfalls gesonderte Handelskalender-/252-Regel. |
| SB-03 | Konkrete Risk-Free-Serie, Notierung/Einheit/Verfügbarkeit und dokumentierte vorgelagerte Umrechnung auf exakt dieselben Perioden. |
| SB-04 | Konkrete Signalreihe/SMA-Fenster, eigene beobachtete Signalfrequenz, vollständiger Warm-up und Eignung historischer Adjustierung. |
| SB-05 | Länder-/Proxy-Auswahl, GDP-Indikator/-Einheit, echte historische Vintages/Veröffentlichungsdaten und gegebenenfalls ausdrücklich begründeter Veröffentlichungslag. |
| SB-06 | Wissenschaftliches Daten-/Run-Archiv mit originalen/verarbeiteten Bytes, Config, Aufbereitung, unveränderlicher Ausführungsumgebung und zugeordnetem Code-/Paketstand. |
| SB-07 | Wissenschaftliche Texte und Beispiele mit akzeptiertem Sharpe, Start-HWM, SMA Long/Cash/Lag, Jahreszustandsfolge, reiner BIP-Logik und normalisierten Eingabeverträgen synchronisieren. |

OD-14 bis OD-18 bleiben deshalb bewusst endgültigen Versuchswerten vorbehalten. Zusatzanalysen nach OD-19 werden separat vor ihrer wissenschaftlichen Verwendung definiert, nicht nach günstigen Ergebnissen gewählt.

| NON-BLOCKING | Verbleibender Hinweis |
|---|---|
| NB-01 | Direkte Legacy-Analyse-/Resampling-/Kovarianzhelpers benötigen vollständige eigene Eingabeverträge. Die dokumentierten NaN-Fälle liegen ausserhalb der validierten aktiven Engine-Pfade. |
| NB-02 | Python 3.11–3.14 ist deklariert; tatsächlich geprüft nur Windows/CPython 3.14.0. Lock bindet Versionen, keine Distributions-Hashes. Andere Plattformen und dauerhaft reproduzierbare Paketarchive benötigen gesonderten Nachweis. |
| NB-03 | Veralteter Strategie-Docstring und historische Stand-/Abnahmeangaben bleiben erhalten. Die erlaubte aktuelle Implementierungsnotiz und dieser Release-/Testnachweis ordnen den heutigen Stand ein; keine weitere Pythondatei wird zur Textkorrektur verändert. |

Weitere feste Grenzen: Float-Arithmetik mit ausdrücklichem Abbruch nicht darstellbarer Zustände; Jahreskennzahlen nur bei kompatiblen deklarierten Kalendergittern MS/ME, YS/YE, W oder D. Keine automatische Börsenkalender-/252-Aufbereitung, Liveadapter, FX, verzinstes Cash, Short, Kosten-/Steuer-/Inflationsmodelle, gemischte Kommerstrategie, Optimierung, Batch oder Web/API im bestätigten Umfang. Unregelmässige Demos behalten begründet nicht verfügbare Jahreskennzahlen.

## Release-Prüfnachweis

Geprüft am 2026-10-04 auf **Windows 11 / CPython 3.14.0**, NumPy **2.3.5**, pandas **2.3.3**, pytest **8.4.2**. Andere Plattformen/Interpreter wurden nicht ausgeführt. Die vollständige unveränderte Suite umfasst weiterhin **441 Tests**, ohne neue oder gelockerte Erwartungen.

| Release-Prüfung | Tatsächlich ausgeführtes Ergebnis |
|---|---|
| Quellsuite 1.0.0 | **441 passed in 149.56s**, Exit 0 |
| Frische nicht editierbare Wheel-Suite 1.0.0 | **441 passed in 84.08s**, Exit 0 |
| `pip check`, Checkout und Wheel | Beide **No broken requirements found.** |
| Wheel-Bau | `maturarbeit_engine-1.0.0-py3-none-any.whl`, **29899 Bytes** |
| Isolierte Installation | Erfolgreich, `include-system-site-packages = false`, Import aus `site-packages`; Import- und Distributionsversion jeweils **1.0.0** |
| Abhängigkeiten | Alle zwölf für Windows geltenden Lock-Versionen bestätigt, keine Änderung an `requirements.lock` |
| Paketinhalt | Jede Wheel-Pythondatei bytegleich zur entsprechenden aktuellen `src/`-Datei |
| Original-CLI-Demos | Vier Checkout- und vier Wheel-Runs, alle Exit 0 |
| Offline | Socket-Verbindungen und DNS in allen acht tatsächlichen CLI-Unterprozessen gesperrt; Guard je Interpreter vorab bestätigt |
| Demo-Regression | Alle CSVs und `data_quality.json` bytegleich zwischen Checkout/Wheel und zu den akzeptierten 0.4.3-Freeze-Re-Audit-Runs |

SHA-256 des tatsächlich gebauten und installierten 1.0.0-Wheels:

```text
045f0dda4fa4bdb4774390fd166140290ae061d1478e99c1a356c8fc91ed46d2
```

Die frische Umgebung liegt unter `.venv/release_v1/installed`; der geprüfte Importpfad ist `.venv/release_v1/installed/Lib/site-packages/maturarbeit_engine/__init__.py`, `sys.base_prefix = C:\Python314`. Distributionsmetadaten nennen exakt das geprüfte Wheel samt Archivhash, keinen Editable-Install. Nur die bestehende Checkout-Umgebung ist editierbar aktualisiert. Keine globale Installation. Paketbau/-installation mit separat genehmigtem Paketzugriff ist von Offline-Simulationen getrennt. Der Hash identifiziert dieses konkrete Archiv; kein Versprechen bytegleicher späterer Neubauten.

| Demo | Unabhängig bestätigter Endwert | Checkout-Run unter `outputs/runs/` | Wheel-Run unter `outputs/runs/` |
|---|---:|---|---|
| Buy-and-Hold | **99** | `synthetic_buy_hold-d3ac996076df4fea83f4be9f24224f8e` | `synthetic_buy_hold-4a63bcc09af14edc80857b902ac3d715` |
| Fixed Rebalancing | **116.4284** | `synthetic_rebalance-a5285be5d9c74256ba5cbdebef1f56bd` | `synthetic_rebalance-4ad2d31c818c4230b956ac0a1bf9696c` |
| Trend | **96.8** | `synthetic_trend-82a18d5c602043ccb92c5cd3019f36a7` | `synthetic_trend-5372ca951be246dba94f8f844ff8dd08` |
| Country Weighting | **117.667** | `synthetic_country_weighting-bd1103a1dce9421ba95ca8c36d1d9207` | `synthetic_country_weighting-4a06fbaab6e7410db635ffba566405d4` |

Sämtliche mitausgeführten Strategie-Verläufe, Periodenrenditen, Drawdowns und Summary-Kennzahlen wurden skalar nachgerechnet. Stichproben: Fixed-Rebalancing-Trades −5.04/+5.04 zu 67.56/45.04; Trend-Signale 0/1/1/0/0/1/1, Lag 1 und Cash 0; GDP 2018 initial 60/40, GDP 2019 am Trade 50/50 mit damals verfügbaren Revisionen, Trades −16.3/+16.3 zu je 56.3. Spätere GDP-Revision und terminale neue GDP-Ziele bleiben ungenutzt. Gemeinsame RF-Intervalle, SMA-Warm-up, Jahreskennzahlstatus und vier/sechs/sieben/sieben Ergebnisdateien bestätigt.

Input-/Result-/Einzelquell-/aggregierte Codehashes, striktes JSON, UTC, Grenzen und Strategie-Set sind geprüft. Im Checkout nennen die Manifeste korrekt HEAD `04cab0673bfe48f733b3e50dd531ee282ff16a88`, **dirty=true**; im Wheel Git **unavailable**, Commit/Dirty null. Gegenüber den jeweiligen 0.4.3-Manifesten ändern sich ausschliesslich Version, `__init__.py`-Hash, aggregierter Codehash, Run-ID/Zeit sowie im Checkout `pyproject.toml`-Hash und Git-/Dirty-Angaben. Alle übrigen Manifestinhalte bleiben gleich.

Die Abschlusskontrolle vergleicht **104** Ausgangsdateien per SHA-256: ausschliesslich die fünf erlaubten bestehenden Dateien geändert, die übrigen **99 bytegleich**; neu ausschliesslich `release-v1.0.md`. In den zwei Versionsdateien verändert sich exakt 0.4.3 → 1.0.0. Alle anderen Pythondateien, sämtliche Tests, Configs/Demos, Lock, AGENTS, Entscheidungen, Audit-/Fixberichte, Notebooks, Methodik, Bibliographie und Buchkapitel bleiben bytegleich. Historische Implementierungs-/Testabschnitte bleiben erhalten, der vollständige bisherige KI-Log als Bytepräfix ebenfalls. Diff, neue Datei, Whitespace und Links sind geprüft; HEAD und vorhandene Tags bleiben unverändert.

**Der Stand ist technisch bereit für den Release-Commit und den Tag `engine-v1.0`. Beide wurden nicht erstellt.** Keine neue Methodik, keine Engine-Logikänderung, keine realen Daten, keine Studienparameterwahl und keine wissenschaftliche Textänderung. SB-01 bis SB-07 und NB-01 bis NB-03 bleiben wie oben dokumentiert offen. Details der Befehle und Vergleichsruns stehen im [Release-Testnachweis](testing.md#release-freeze-v100-vom-2026-10-04).
