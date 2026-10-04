# Finaler Audit der allgemeinen Backtesting-Engine v1

**Datum:** 2026-10-04. **Ausführung:** Codex; ausschliesslich Prüfung und Dokumentation.

**Auftrag:** [Vollständiger finaler Audit-Prompt](../ai-usage/prompts/2026-10-04-engine-v1-final-audit.md). **Regeln:** `AGENTS.md` und [verbindliche Entscheidungen OD-01 bis OD-13](decisions.md).

**Akzeptierter Ausgangspunkt:** `engine-country-weighting-v0.4.0` auf `5a06432457c76de925258db16a5bcbb5dc48cdc2`. **Geprüfter Checkout:** `a298f69b12929f83da795bffa8c81833fef7f1d0`, Engine 0.4.0.

## 1. Urteil und Abgrenzung

**Der geprüfte Stand soll noch nicht als Engine v1.0 eingefroren werden.** Die vollständige bestehende Suite besteht im Checkout und im frisch installierten aktuellen Wheel jeweils mit **344 Tests**. Alle vier CLI-Demos sind auf beiden Installationen offline ausführbar, unabhängig nachgerechnet und fachlich bytegleich. Drei zusätzliche reproduzierte Vertragsfehler blockieren trotzdem den Freeze:

1. Positive Start-/Zielpositionen können numerisch zu null verschwinden; beide Portfolio-Strategien exportieren danach eine falsche erfolgreiche Performance (**EB-01**).
2. Die Result-/Exportgrenze lässt widersprüchliche Drawdowns, Summary-Werte/Status und feste Ziele gegenüber der Manifest-Konfiguration passieren (**EB-02**).
3. Überbreite CSV-Zeilen können durch pandas' automatische Indexinterpretation unter falschen Datumslabels erfolgreich verarbeitet werden (**EB-03**).

Das [vollständige Befundregister](final-open-issues.md) enthält **3 ENGINE-BLOCKING**, **7 STUDY-BLOCKING** und **3 NON-BLOCKING** Einträge mit Nachweis, Soll/Ist, Empfehlung und Entscheidungsbedarf. Die noch offenen endgültigen Versuchswerte sind keine Engine-Fehler. Die technische Klassifikation und Empfehlungen stammen von Codex und sind dem Autor zur Prüfung vorgelegt; sie wurden nicht als neue Methodik beschlossen.

Keine Engine-Funktion, kein Test, keine Config, keine Abhängigkeitsdatei und kein geschützter wissenschaftlicher Inhalt wurden geändert. Es wurden keine realen Daten beschafft oder untersucht und kein Commit erstellt. Dieser Bericht ist keine unabhängige Prüfung der gesamten zitierten Finanzliteratur und keine Freigabe eines realen Hauptversuchs.

## 2. Git-Ausgangspunkt und gelesene Quellen

Der Arbeitsbaum war am Auditbeginn sauber. `git rev-parse` bestätigt den vorgegebenen Tag-Commit. `git diff engine-country-weighting-v0.4.0 HEAD` enthält genau eine Datei: den finalen Audit-Prompt mit 693 eingefügten Zeilen. Engine, Tests, Demos, Entscheidungen und wissenschaftliche Dateien entsprechen damit dem akzeptierten Stand. Die 90 zu Beginn versionierten Dateien wurden zusätzlich mit SHA-256 als Vergleichsbasis erfasst.

Vollständig gelesen wurden die aktuellen nachstehenden Dateien beziehungsweise angegebenen Notebook-Kapitel. Notebook-Zellnummern sind nullbasiert; geprüft wurden Markdown- und Codequellen, keine Neu-Ausführung oder Korrektur der Notebooks.

| Bereich | Gelesene Dateien / Umfang |
|---|---|
| Auftrag und Regeln | Finaler Audit-Prompt vollständig einschliesslich „Vollständiger Prompt“; `AGENTS.md` vollständig |
| Vorherige Prüfung und Entscheidungen | `documentation/engine/audit.md`, `open-decisions.md`, `decisions.md`, `implementation.md`, `testing.md` vollständig |
| Wissenschaftlicher Kontext | `notebooks/Theorie.ipynb` 3.2–3.13 vollständig, zusätzlich 3.1; `notebooks/Analyse.ipynb` 5.1–5.9 vollständig; `methodik.qmd` vollständig |
| Mathematik und Einstieg | `src/funktionen.py`, `src/__init__.py`, `src/__main__.py` |
| Daten | `src/data/__init__.py`, `validate.py`, `normalize.py`, `macro.py` |
| Engine | `src/engine/__init__.py`, `config.py`, `context.py`, `portfolio.py`, `result.py`, `simulation.py` |
| Strategien | `src/strategies/__init__.py`, `buy_hold.py`, `rebalance.py`, `trend.py`, `country_weighting.py` |
| Kennzahlen / Export | `src/analysis/__init__.py`, `metrics.py`; `src/export/__init__.py`, `results.py` |
| Installation | `pyproject.toml`, `requirements.lock`, `.gitignore` |
| Vollständige Tests | `tests/conftest.py`, `test_functions.py`, `test_core.py`, `test_rebalance.py`, `test_trend.py`, `test_country_weighting.py` |
| Sämtliche Konfigurationen | `configs/demo_buy_hold.json`, `demo_rebalance.json`, `demo_trend.json`, `demo_country_weighting.json` |
| Sämtliche Demo-CSVs | Je `market.csv`, `assets.csv`, `risk_free.csv` unter `configs/demo/`, `rebalance_demo/`, `trend_demo/`, `country_weighting_demo/`; zusätzlich `country_weighting_demo/macro.csv` |
| KI-Nachweis | `documentation/ai-usage/README.md`, vollständiger bisheriger `ai-usage-log.md` |

Die vier aktiven Strategiepfade und der gemeinsame Portfoliohelper wurden gegen die verbindlichen Entscheidungen geprüft. Die übrigen Legacy-Analysehelpers wurden ebenfalls gelesen und mit Normal- und Fehlwertfällen untersucht. Geschützte Beispiele wurden mit aktuellen Funktionen verglichen; nötige spätere Synchronisierung ist SB-07.

## 3. Tatsächlich ausgeführte Prüfungen

Plattform: **Windows, CPython 3.14.0**, NumPy **2.3.5**, pandas **2.3.3**, pytest **8.4.2**. Die lokale editierbare Engine und die frische nicht editierbare Installation melden jeweils **0.4.0**. Weitere Interpreter/Plattformen wurden nicht getestet.

Alle temporären Prüfprogramme, Notebook-Quelltextauszüge, Eingabefixtures, Wheel-/Installations- und pytest-Ablagen liegen unter ignoriertem `.venv/final_audit/`; reguläre Demo-Runs unter ignoriertem `outputs/runs/`. Paketbau darf ausserdem die bereits ignorierten `build/`/`*.egg-info/`-Artefakte erzeugen. Diese Dateien sind keine versionierten Projektänderungen.

| Prüfung | Tatsächliches Ergebnis |
|---|---|
| Vollständige unveränderte Suite im Checkout | **344 passed in 50.33s**, Exit 0 |
| Aktueller Engine-0.4.0-Wheel-Build | Erfolgreich, `maturarbeit_engine-0.4.0-py3-none-any.whl` |
| Frische isolierte Wheel-Installation | Erfolgreich; kein Editable-Install, `include-system-site-packages=false` |
| `pip check`, Checkout und frische Installation | Je **No broken requirements found.** |
| Vollständige unveränderte Suite gegen installiertes Wheel | **344 passed in 39.33s**, Exit 0 |
| Vier CLI-Demos je Installation | Acht vollständige erfolgreiche Runs, Exit 0; unabhängige Kontrollen bestanden |
| Offline-Demos in tatsächlichen CLI-Unterprozessen | Socket-Verbindung und DNS über temporäres `sitecustomize` gesperrt; alle acht Runs bestanden |
| Manifest-/Hash-/Dateisatzprüfung | Alle acht Manifeste und Qualitätsberichte strikt gelesen; Eingabe-/Ergebnis-/Quell-/aggregierte Code-Hashes, UTC, Versionen, Git, Grenzen und Status geprüft |
| Unabhängige Mathematik-/Kalenderkontrollen | Alle geforderten Normalformeln und zwölf Frequenz-/Randfälle ausgeführt; Legacy-NaN-Verhalten gesondert reproduziert |
| Zusätzlicher Look-ahead-/Vergleichsversuch | Alle vier Strategien: frühere Zustände bei späteren Datenänderungen exakt identisch; umgekehrte Ausführung und gesamter Kontext unverändert |
| Zusätzliche Fehlerproben | EB-01/02/03 im Checkout und im installierten Wheel reproduziert; Zielpositionsunterlauf beim jährlichen Neuallokieren zusätzlich direkt im Helper |
| Historischer Testdateivergleich | Alle ursprünglichen 3/4/5 Testdateien der akzeptierten Core-/Rebalancing-/Trend-Tags bytegleich zum heutigen Stand |

Der erste pytest-Aufruf verwendete eine noch nicht vorhandene Elternablage für `--basetemp` und endete mit **65 passed, 279 setup errors in 7.77s**. Nach Erstellung des ignorierten Elternverzeichnisses wurde dieselbe vollständige Suite mit frischer Ablage erfolgreich ausgeführt. Das war ein Fehler des Audit-Aufrufs, keine fehlgeschlagene Engine-Assertion. Temporäre Kontrollprogramme benötigten zudem Korrekturen ihrer RF-/Trade-Spaltennamen und eines Helper-Imports; die vollständigen Kontrollen wurden danach erfolgreich erneut ausgeführt. Eine pandas-Dtypewarnung beim Ändern einer künstlichen GDP-Fixture wurde durch ausdrücklichen Float-Typ ausschliesslich im temporären Prüfprogramm beseitigt und der Versuch erneut ausgeführt. Keine Produktionsdatei oder Test-Erwartung wurde dafür angepasst.

### Befehle und Installationsnachweis

Aus dem Repository-Stamm, mit bereits vorhandener Projekt-`.venv`:

```powershell
New-Item -ItemType Directory -Force -Path .venv/final_audit | Out-Null
.venv\Scripts\python.exe -m pytest -q --basetemp=.venv/final_audit/pytest-source-rerun
.venv\Scripts\python.exe -m pip wheel --no-cache-dir --disable-pip-version-check --no-deps --wheel-dir .venv/final_audit/wheels .
.venv\Scripts\python.exe -m venv .venv/final_audit/installed
.venv\final_audit\installed\Scripts\python.exe -m pip install --no-cache-dir --disable-pip-version-check -c requirements.lock .venv/final_audit/wheels/maturarbeit_engine-0.4.0-py3-none-any.whl pytest==8.4.2
.venv\final_audit\installed\Scripts\python.exe -m pip check
```

Die Wheel-Suite wurde aus `.venv/final_audit/` mit absoluten Pfaden zu installiertem Interpreter, `tests/`, `pyproject.toml` und eigener `.venv/final_audit/pytest-wheel`-Ablage gestartet. So ist der Checkout nicht versehentlich die importierte Engine. Geprüfter Importpfad:

```text
C:/Users/modic/Documents/GitHub/Maturarbeit_Engine/.venv/final_audit/installed/Lib/site-packages/maturarbeit_engine/__init__.py
```

Der installierte Versionswert und Paketmetadaten sind 0.4.0; `sys.prefix` zeigt auf die frische Umgebung, `sys.base_prefix` auf `C:\Python314`. Python-Abhängigkeiten stammen aus der unveränderten Versionsbindung; Build-Werkzeuge aus `pyproject.toml`. Netzwerkgenehmigung wurde nur für Paketbau/-installation verwendet. Keine globale Installation oder Änderung der Lock-Datei.

SHA-256 des tatsächlich gebauten Wheels:

```text
c4418fd446d21e6e1a1855ba3d8da066d498b48eb2e3fee186f90842852157ef
```

Dieser Hash identifiziert das konkrete Audit-Wheel, keine Zusage zeitunabhängig byteidentischer Neubauten.

## 4. Daten- und Konfigurationsaudit

### Lokale JSON-/CSV-Eingaben

Der Runner lädt explizite lokale Dateireferenzen, keine URLs. JSON-Parser und Schema kontrollieren doppelte Schlüssel, unbekannte Felder, notwendige Parameter, Typen/Bools, endliche Zahlen, positiven Startwert, explizites `periods_per_year`, gültige Strategieoptionen und mindestens eine aktive Strategie. Relative Datenpfade beziehen sich auf die Config. Ein übergebenes `RunConfig` wird gegen seine validierte Datei geprüft. Deaktivierte Strategieblöcke werden strukturell geprüft, verlangen jedoch keine Performance-Anlagen oder Makrodatei im Kontext.

CSV-Snapshots hashen die tatsächlich gelesenen Bytes vor dem Parsing; UTF-8/BOM, doppelte Header, Pflichtfelder und ISO-Datumswerte werden kontrolliert. **EB-03** zeigt jedoch eine strukturelle Parsinglücke vor diesen fachlichen Prüfungen: pandas kann ein zusätzliches führendes Feld als Index aufnehmen. Nachfolgende Prüfungen bestätigen dann die bereits verschobenen Spalten. Der Datenbericht muss deshalb derzeit als Beleg der implementierten Werteprüfungen, nicht als vollständiger CSV-Strukturnachweis verstanden werden.

### Markt, Metadaten und gemeinsamer Kalender

Performance-Werte sind vollständig, endlich und strikt positiv; doppelte `(date,asset_id)`, unbekannte Kennungen, fehlende Metadaten und nicht passende Währungen aktiver Anlagen scheitern. Auch ausdrücklich null gewichtete aktive Anlagen benötigen Bewertungen. Zusätzliche gültige unbenötigte Assets bestimmen den Vergleichskalender nicht. Alle gelieferten Performance-Zeilen werden validiert; ein ungültiges zusätzliches Asset wird deshalb nicht still ignoriert.

Die sortierte Vereinigung der Anlagen aller aktiven Strategien bestimmt die Schnittmenge tatsächlicher Bewertungen. Diese Schnittmenge entsteht **vor** der Renditebildung und wird erst danach auf den gewünschten Zeitraum begrenzt. Mindestens zwei gemeinsame Bewertungen sind erforderlich. Entfernte nicht gemeinsame Termine und tatsächliche Grenzen stehen im Bericht. Keine Interpolation, kein Forward-Fill und keine erfundenen Marktwerte. Die Engine errät gemäss OD-01 keinen Handelskalender.

### Risk-Free

Die Engine erwartet `period_start,period_end,series_id,period_return` mit normalisierten Dezimalrenditen. Serienkennung und beide Grenzen jeder gehaltenen Periode werden exakt ausgerichtet. Fehlende, verschobene oder zusätzliche überlappende Intervalle werden abgelehnt; Intervalle vollständig ausserhalb des Laufs werden gezählt. Keine Nullersetzung, implizite Jahreszinsumrechnung oder Cash-Verzinsung. Ohne RF-Referenz ist Sharpe begründet nicht verfügbar. Datenwerte allein können die behauptete Zinskonversion nicht belegen: SB-03.

### Makroversionen

`period` ist ein vierstelliges Referenzjahr; Kennungen/Einheiten vollständig, GDP endlich und positiv, `available_from` ISO-Datum. Unterschiedliche Versionen sind ausdrücklich erlaubt. Identische vollständige Versionen werden dedupliziert und gezählt; unterschiedliche Werte unter demselben vollständigen Versionsschlüssel werden abgelehnt, auch für erst spätere Zeilen. Die Tabelle wird vollständig geprüft, ihre unbenötigten gültigen Kombinationen beeinflussen keine Auswahl.

Für jedes Entscheidungsdatum werden zuerst exakt Länder/Indikator/Einheit und `available_from <= D` gefiltert, dann das jüngste für **alle** Länder gemeinsame Jahr und pro Land die letzte zulässige Revision gewählt. Vollständiger Nenner, kein Länderentfernen, Jahrmischen, Auffüllen oder Renormieren. Überlauf der GDP-Summe und zu null unterlaufende positive GDP-Gewichte werden abgelehnt. Der nachfolgende Positionswert-Unterlauf bleibt hingegen EB-01. Ausgewählte Versionen/Jahre/Werte/Gewichte und Entscheidungstypen sind im Qualitätsbericht, die Makrobytes im Manifest belegt. Historische Wahrheit und reale Einheitenvergleichbarkeit bleiben SB-05.

## 5. Zeitliche Logik und Strategieaudit

| Strategie | Geprüfte Zeit-/Zustandsregel | Urteil für geprüfte reguläre Fälle |
|---|---|---|
| Buy-and-Hold | Gewicht 1; erste gemeinsame Bewertung als Startkapital, Rendite leer; erste echte Rendite zwischen erster/zweiter Bewertung; spätere Kurse ohne Einfluss auf frühere Werte | Korrekt, kein gefundener Look-ahead |
| Fixed Rebalancing | Startziel; gehaltene Positionen verdienen zuerst die Intervallrendite, danach Drift, danach gegebenenfalls Jahrestrade; neue Ziele wirken erst folgendes Intervall | Korrekt; Start-/Zielpositionsunterlauf EB-01, unvollständige Resultkontextprüfung EB-02 |
| Trend | Eigene beobachtete Signalhistorie mit vollständigem Vorlauf; separate Performance-Reihe; beide SMAs am Start gültig; `short > long` Long, Gleichheit Cash; Position exakt vorheriges gemeinsames Signal | Korrekt; Warm-up verdient keine Rendite, Cash 0, kein gefundener Look-ahead |
| Country Weighting | Initiale As-of-Auswahl; jährlicher Entscheid erst nach Rendite/Drift; jüngstes gemeinsames Jahr und letzte bis D bekannte Revision; neue Allokation wirkt erst nächste Periode | Korrekt für historische Zeitfolge; Positionsunterlauf EB-01 |

Jahresereignisse liegen am letzten gemeinsamen Bewertungstermin vor einem Jahreswechsel, mit bereits vergangener und noch folgender Renditeperiode. Keine erneute Startallokation und kein terminaler wirkungsloser Trade. Das Wissen um den vorhandenen gemeinsamen Bewertungskalender ist eine bestätigte Ablaufregel, kein Zugriff auf spätere Preis-/GDP-Werte. Zielspalten bleiben als Referenz zwischen Ereignissen bestehen; Driftgewichte dürfen sich ändern.

Die Trendfenster zählen die eigenen tatsächlich beobachteten Asset-Werte, auch solche zwischen gemeinsamen Performance-Terminen. Die Signale werden an gemeinsamen Bewertungen entnommen, der Lag zählt diese Bewertungen. Hinzufügen einer aktiven Anlage darf deshalb bewusst den gemeinsamen Vergleichskalender und die gehaltenen Intervalle ändern; das ist von einer unerlaubten gegenseitigen Datenmutation zu unterscheiden. Unbenötigte Anlagen und eine blosse Reihenfolgenänderung haben diesen Effekt nicht.

Zusätzlich zur ausgeführten Suite wurde ein unabhängiger temporärer Versuch auf der Vier-Strategien-Demo durchgeführt: letzter A-Performance-/Signalwert auf 500/999, erst später veröffentlichte GDP-Revision von 5000 auf 0.001 geändert. Alle früheren Portfolio-, Gewicht-, Trade- und Signalzeilen aller vier Strategien wurden **exakt** gegen den unveränderten Lauf verglichen. Sie bleiben gleich; die im kurzen Lauf tatsächlich angewandten GDP-Entscheidungen ebenfalls. Vorwärts-/Rückwärtsausführung der vier Strategien liefert exakt dieselben Resultate. Performance, RF, Signal- und Makrotabellen sowie Qualitätsbericht und Inputinformationen des gesamten Kontextes bleiben unverändert.

Bestehende Tests ergänzen dies insbesondere um eine verlängerte GDP-Revision mit tatsächlichem späterem Folgeentscheid, Signaländerung am selben Datum, gültigen Start am Jahresende, mehrere Jahresereignisse und fehlende Vorlaufhistorie. Kein Look-ahead wurde in diesen geprüften Fällen festgestellt; reale Vintage-/Signalbedeutung ist dadurch noch nicht geprüft.

## 6. Gemeinsame Portfoliologik und Mathematik

`run_annual_portfolio` verwendet denselben Drift-/Tradepfad für konstante und dynamische Ziele. Feste Rebalancing-Ziele kommen aus der Konfiguration; Country-Ziele aus einer Entscheidung am zulässigen Datum. Asset-Labels werden ausdrücklich ausgerichtet, nicht positionsweise verwechselt. `validate_target_weights` akzeptiert nichtnegative Gewichte mit Summe 1 innerhalb der dokumentierten absoluten Toleranz 1e-12, ohne Normalisierung, Short, Hebel oder Rest-Cash. Helper prüfen vollständige Assetmengen, endliche echte Zahlen und positive Gesamtsummen.

Kapital- und Transaktionssummen werden mit relativer Toleranz 1e-12 verglichen. Nullgewichte, umgekehrte Labels, drei Assets, wechselnde GDP-Ziele, Nulltransaktionen und mehrere Jahresereignisse sind getestet. Grosse nicht endliche Folgezustände werden zurückgewiesen; Renditen nahe −100 % mit noch darstellbarem positivem Faktor wurden zusätzlich kontrolliert. **Diese Prüfungen decken positive Allokationsprodukte, die schon am Start oder beim Zielsetzen zu null werden, nicht ab: EB-01.** Ein Totalverlustzustand wird von den positiven Performance-/Portfoliowertverträgen nicht als normaler unterstützter Lauf behandelt.

Das Länder-Refactoring hat die Formeln nicht ersetzt. `src/funktionen.py`, Buy-and-Hold, Trend, Kennzahlen und Kalender sind gegenüber dem akzeptierten Trend-Stand erhalten; die feste Portfolio-Zustandsfolge wurde in einen gemeinsamen Helper verschoben. Die unveränderten historischen Tests und die unabhängig bestätigte 60/40-Demo sprechen gegen eine normale semantische Regression. Der jetzt gefundene Allokationsgrenzfall widerspricht trotzdem der allgemeinen Numeriksicherung.

Unabhängig ausgeführte skalare Kontrollen verwenden keine zweite Produktionsimplementierung:

| Funktion | Unabhängiger Nachweis / Eingabevertrag |
|---|---|
| `prozentuale_aenderung` | 100/110/99 → +0.1/−0.1, `fill_method=None`; geordnete vollständige positive Werte werden vorgelagert geprüft |
| `kumulierte_rendite`, `wachstumsfaktor` | Endwert `log(0.99)` bzw. 0.99; korrekt für vollständige positive Preisreihe, direkte NaN-Eingaben ungesichert (NB-01) |
| `geometrisches_mittel` | Faktoren 1.1/0.9 → `sqrt(0.99)`; direkte Series-/array-NaN-Semantik unterschiedlich, Engine normalisiert und validiert vorher |
| `annualisierte_rendite` | `0.99^6−1`, nur ausdrückliche positive Faktoren und `input_kind='growth_factors'`; kein Erraten einfacher Renditen |
| `standardabweichung`, `annualisierte_volatilitaet` | +0.1/−0.1 → `sqrt(0.02)` und bei m=12 `sqrt(0.24)`; `ddof=1`, vollständige echte Renditestichprobe nötig |
| `drawdown`, `maximum_drawdown` | Zwei Anfangsverluste −0.1 → −0.1/−0.19, Minimum −0.19; Start-HWM korrekt, finite Renditen nötig |
| `sharpe_ratio` | Überschüsse 0.099/−0.102; skalare Stichproben-Std und Mittelwert, multipliziert mit `sqrt(12)`; exakt gleiche RF-Indizes, kurze/konstante Stichprobe ausdrücklich undefiniert |
| `korrelationsmatrix` | Zwei gegenläufige Reihen → −1; algebraisch korrekt, vollständige gemeinsame Stichprobe nötig, kein aktiver Engine-Kennzahlenpfad |
| `portfolio_risiko` | Gegenläufige Reihen mit labelvertauschten 0.5/0.5-Gewichten → Varianz 0; feste Kovarianzanalyse, ndarray-Reihenfolge und Gewichtsbedeutung benötigen Vertrag |
| `buy_and_hold` | 100 mit +0.1/−0.1 → 110/99; nur vollständige Renditen, explizite Startbewertung vom Strategie-Wrapper |
| `neue_gewichtung`, `rebalancing` | 60/40 mit +0.1/0 → 66/40, danach 63.6/42.4 und −2.4/+2.4; kapitalerhaltend, einschliesslich vertauschter Asset-Labels; EB-01 bleibt |
| `sma_signal`, Legacy-`trendfolge` | Sämtliche 2/3-Fenstermittelwerte der künstlichen Signalreihe skalar nachgerechnet; Anlauf-Signale NaN, strikter Vergleich und lagged Legacy-Renditen stimmen |

Die direkten Log-/Statistik-/Kovarianz-/Resamplinghelpers sind unter einem vollständigen Eingabevertrag korrekt, aber als allgemeine ungeprüfte Schnittstelle nicht ausreichend abgesichert. NaN-Überspringen in pandas wurde ausdrücklich reproduziert (NB-01). Es befindet sich in diesen Beispielen ausserhalb der validierten aktiven Engine-Pfade. Ein späterer Datenadapter darf den generischen `resample_dataframe` insbesondere nicht ohne eigene Intervall-/Verfügbarkeitsregel einsetzen.

## 7. Annualisierung, Frequenz und Randperioden

Die Engine leitet aus `m` keine Frequenz ab. `check_period_logic` vergleicht die komplette vorhandene Bewertungsachse mit einem ausdrücklich deklarierten `pd.date_range`-Gitter; erst danach wird die Kompatibilität von `m` geprüft.

| Tatsächlich zusätzlich geprüfte Achse | Ergebnis |
|---|---|
| Drei Monatsendbewertungen Jan/Feb/März 2020, ME/12 | Verfügbar, einschliesslich Schalt-Februar |
| Drei Monatsanfänge, MS/12 | Verfügbar |
| Drei Jahresanfänge bzw. -enden, YS/YE und m=1 | Verfügbar |
| Drei Sonntag-Wochenbewertungen, W/52 | Verfügbar |
| Drei aufeinanderfolgende Kalendertage, D/365 bzw. D/366 | Verfügbar für die ausdrücklich unterstützten Jahreskonventionen |
| Freitag/Montag, D/252 oder D/365 | Nicht verfügbar, Gitter unregelmässig |
| Tatsächliche Bewertung 15. Januar bis Februarende, ME/12 | Nicht verfügbar, kein ME-Gitter |
| Fehlender Februar zwischen Januar-/Märzende, ME/12 | Nicht verfügbar |
| Vollständiges Monatsgitter ohne Frequenzdeklaration | Nicht verfügbar, keine Frequenzvermutung |

Unpassendes `m`, kurze Stichprobe und weitere unregelmässige Fälle werden zusätzlich in der Suite geprüft. Die Startbewertung geht nicht in die Statistik ein. Für n echte Renditen wird die geometrische Rendite mit m skaliert, Volatilität als Stichproben-Std der Strategierenditen und Sharpe als Stichproben-Std der Überschussrenditen. Bei weniger als zwei echten Renditen fehlen Volatilität/Sharpe mit Status; tatsächliche Nullvolatilität bleibt 0. Es gibt keine kalenderzeitbasierte Ersatz-CAGR.

Ein angeforderter Start mitten im Monat führt bei gelieferten Monatsendbewertungen zum ausgewiesenen ersten Monatsendanker. Die folgenden tatsächlichen Monatsendintervalle sind volle beobachtete Perioden; der nicht bewertete Teil davor verdient keine Rendite. Liegt eine wirkliche Bewertung mitten im Monat in der verwendeten Achse, scheitert die Monatsgitterfreigabe. Das entsprechende Prinzip gilt für den Endanker. Der Audit hat für diese Fälle keinen falschen freigegebenen Jahreswert gefunden.

`D/365` und `D/366` sind ausdrücklich zulässige Konventionen, keine automatisch gemessene Jahreslänge; ebenso bedeutet `W/52` keine tagesgenaue CAGR. Reale Börsentage mit Wochenenden/Feiertagen fallen aus der derzeitigen Kalendergitter-Unterstützung. Eine konkrete Handelskalender-/252-Tage-Regel bleibt deshalb **STUDY-BLOCKING (SB-02)**, sofern die Studie tägliche annualisierte Werte benötigt. Ihre Abwesenheit erzeugt gegenwärtig begründete Nichtverfügbarkeit und ist für sich kein falsches Engine-Ergebnis. Hier wurde keine neue Kalenderregel festgelegt.

## 8. Resultatvertrag, Kennzahlen und Export

Normalfälle: Alle Strategien liefern denselben effektiven Kalender und dasselbe Startkapital/Währung/RF-Intervallset. Historien beginnen mit Kapital, leerer Rendite und Drawdown 0. Nachfolgende Renditen stimmen mit Vermögensquotienten überein. Summaries enthalten jeweils genau eine geordnete Strategiezeile und verwenden nur echte Renditen. Optionale Gewicht-/Trade-/Signaldateien erscheinen nur für tatsächlich vorliegende Resultate; ereignislose Trade-Tabellen behalten korrekte Header.

Gewichte decken jedes Datum/Asset genau einmal ab. `weight_before` beschreibt Drift vor Trade, `target_weight` den bis zur nächsten Entscheidung geltenden Referenzwert, `weight_after` den gehaltenen Zustand. Konstante feste Ziele und dynamische GDP-Ziele sind unterscheidbar. Trades haben `transaction_value = target_value - value_before`, je Ereignis vollständige Assetmengen und erhaltenes Kapital; keine Start-/End-Fake-Trades. Signale enthalten vollständig definierte SMAs, binäre Entscheidungen und exakt einen Lag; Startposition leer, kein Warm-up im Export.

**Die Behauptung, alle Invarianten verhinderten widersprüchliche Exporte, ist dennoch widerlegt (EB-02).** Ein positiver Drawdown 0.75 an einem Zwischenhoch überlebt die Kontrolle, solange das Minimum −0.1 bleibt. Export akzeptiert veränderte Summary-Endwerte/Infinity und unzutreffende Status. Feste Ziele 20/80 können an der Python-Grenze neben konfigurierten 60/40 erscheinen; die aktive Strategiemenge wird dort nicht vollständig abgeglichen. Reguläre Demo-/CLI-Berechnungen erzeugen diese manipulierten Ergebnisse nicht, aber die verpflichtende Vertragsprüfung ist unvollständig. Hashes oder atomische Veröffentlichung machen einen widersprüchlichen Zahleninhalt nicht richtig.

## 9. Vier Demos und unabhängige Gegenrechnungen

Die Demos wurden mit Original-Configs im tatsächlichen CLI-Unterprozess aus einer anderen Arbeitsablage je einmal vollständig aus Checkout und Wheel ausgeführt. Temporärer Netzwerkguard galt in jedem Kindprozess. Alle fachlichen CSVs und `data_quality.json` sind zwischen beiden Installationen bytegleich; Manifest-Run-IDs/Zeitstempel und Installationsprovenienz unterscheiden sich erwartungsgemäss.

| Demo | Zentrale unabhängige Kontrollwerte |
|---|---|
| Buy-and-Hold | 100 → 110 → 99; Gesamtrendite −1 %, Jahresrendite `0.99^6−1` ≈ −5.8519850599 %, Jahresvolatilität `sqrt(0.24)` ≈ 48.9897948557 %, Sharpe ≈ −0.0365595484, MDD −10 % |
| Rebalancing | 100 → 106 → 112.6 → 110.348 → 116.4284; am 2020-12-30 zuerst 72.6/40, dann 67.56/45.04, Trades −5.04/+5.04; nächste Periode 60.804/49.544; Gesamtrendite 16.4284 %, MDD −2 %; Benchmarkende 119.79 |
| Trend | Signal 0/1/1/0/0/1/1, Position leer/0/1/1/0/0/1; Renditen 0/+0.1/−0.2/0/0/+0.1, Vermögen 100/100/110/88/88/88/96.8; Jahresrendite `0.968^2−1` = −6.2976 %, Jahresvolatilität `sqrt(0.06/5)*sqrt(12)` ≈ 37.9473319220 %, Sharpe ≈ −0.0475924749; MDD −20 %, Schlussdrawdown −12 %; BH-Ende 77.44, RB-Ende 86.464 |
| Country Weighting | GDP 2018 initial 60/40; GDP 2019 am Trade 50/50 aus historisch verfügbaren Versionen; 100 → 106 → 112.6 → 112.6 → 117.667, Gesamtrendite 17.667 %, MDD 0; Trade −16.3/+16.3 zu je 56.3; Folgewerte 50.67/61.93, Schluss 55.737/61.93; BH 119.79, feste RB 116.4284, Trend 99 |

Die Sharpe-Kontrollen berechnen Mittelwert und `ddof=1`-Streuung **der Überschussrenditen** skalar. Die zusätzliche BIP-Revision 5000 ab 2021-02-01 darf den Trade 2020-12-30 nicht beeinflussen; GDP 2020 80/20 wird am endgültigen 2021-12-31 nicht neu angewandt. Unregelmässige Rebalancing-/Country-Demos haben korrekte leere Jahreskennzahlen/Sharpe samt Status `period_frequency_not_declared`; reguläre BH-/Trend-Demos erlauben Jahreskennzahlen. Kontrolliert wurden alle Strategiehistorien und Kennzahlen, nicht nur die genannten Endwerte.

Tatsächliche Audit-Runs unter `outputs/runs/`:

| Demo | Checkout-Run | Wheel-Run |
|---|---|---|
| Buy-and-Hold | `synthetic_buy_hold-6478c9bc43194209bcbd0b4b53455230` | `synthetic_buy_hold-a466e1ff27e84152810b92d67fe0a508` |
| Rebalancing | `synthetic_rebalance-f7084b48617a402388b20590ccc42ea8` | `synthetic_rebalance-e8933a1ebe9744ba9bdb26d3cc8e9df7` |
| Trend | `synthetic_trend-a5fc8334682e4e7db98fd120d5d78dae` | `synthetic_trend-804bab59a0a54564b318962ded598ad8` |
| Country Weighting | `synthetic_country_weighting-9c0d5b23bc964a1e809501e43bd1176e` | `synthetic_country_weighting-dc2539031e7443f98dcc198529dd6cb4` |

Die erwarteten Dateisätze umfassen vier/sechs/sieben/sieben Dateien einschliesslich Manifest. Sämtliche jeweiligen Ergebnis- und Input-Hashes wurden nachgerechnet. Weitere beim Entwickeln der temporären Kontrollprogramme erzeugte ignorierte Runs werden nicht als zusätzliche erfolgreiche unabhängige Kontrollabschlüsse gezählt.

## 10. Reproduzierbarkeit und Offline-Eigenschaft

Für alle acht Demos geprüft: Config-SHA, Markt-/Metadaten-/RF- und gegebenenfalls Makro-SHA, alle Python-Datei-Hashes, im Checkout zusätzlich `pyproject.toml`/`requirements.lock`, aggregierter Code-Hash, Engine-/Schema-/Python-/Runtime-Paketversionen, UTC-Zeit, effektive/angeforderte Grenzen, aufgelöste Konfiguration, Datenqualität, Strategie-/Kennzahlstatus und sämtliche Ergebnis-Hashes. Alle JSONs wurden strikt ohne nicht standardkonformes NaN/Infinity eingelesen. Ein Manifest-Selbsthash ist gemäss Auftrag nicht nötig.

Checkout-Demos nennen korrekt `a298f69b12929f83da795bffa8c81833fef7f1d0` und **dirty=false**: sie wurden vor den drei Dokumentationsänderungen ausgeführt, die Prüfartefakte sind ignoriert. Wheel-Demos nennen **Git unavailable**, Commit/Dirty null, und hashen die tatsächlich installierten Python-Quellen. Ihre Quellhashes entsprechen den Checkout-Python-Dateien. Die zwei zusätzlichen Projektdatei-Hashes existieren im Wheel ausserhalb des Checkouts erwartungsgemäss nicht.

Snapshots und erneute Eingabe-Hashprüfung vor Export fangen Änderungen seit dem Lesen ab; ausgeführte Suite enthält hierzu Markt-/Config- und Makroänderungsfälle. Der Bericht behauptet keine dauerhafte Dateisperre: nach der letzten Vergleichsprüfung könnten Dateien erneut verändert werden. Der gespeicherte Hash beschreibt weiterhin die konsumierten Bytes, die deshalb separat zu archivieren sind. Sources/Git werden erst beim Export gehasht; bereits importierter Code und später geänderte Quellen in einem langlebigen Prozess sind nicht durch einen Code-Snapshot am Importzeitpunkt abgesichert. Für wissenschaftliche Läufe gilt daher die konkrete unveränderliche Ausführungs-/Archivbedingung SB-06. Source-Manipulation wurde in diesem dokumentationsbegrenzten Audit nicht durchgeführt.

Ausgabe läuft in ein geprüftes temporäres Verzeichnis unter dem Zielroot und wird erst vollständig per Rename veröffentlicht. UUID-Namen und Existenzprüfung schützen vorhandene Ergebnisse. Fachliche Dateien sind bei identischen Inputs/Code deterministisch; zufällige Run-ID/Zeit dürfen variieren. Fehlerhafte Exporte durch EB-01/02/03 sind trotz korrekter technischer Veröffentlichung fachlich ungültig.

Statische Suche findet keine Runtime-Netzwerkimports, Markt-/Makrodownloads, Anbieteradapter oder externe Quellpfade. Die lokale Git-Provenienz benötigt keine Netzwerkverbindung. Der bestehende pytest-Guard sperrt Socket/DNS und urllib im Testprozess; seine Monkeypatches gehen nicht automatisch in CLI-Unterprozesse über. Diese Lücke des früheren Offline-Nachweises wurde hier durch den temporären Guard in allen acht tatsächlichen CLI-Prozessen separat geprüft. Paketinstallation bleibt davon getrennt.

## 11. Kritischer Audit der Test-Suite

Alle sechs Testdateien wurden vollständig gelesen. Parametrisierung ergibt 344 Fälle: 93 Core/Funktionen, 71 Rebalancing, 78 Trend, 102 Country. Warnungen gelten weiterhin als Fehler. Git-Bytevergleich bestätigt 3/4/5 historische Testdateien gegenüber den akzeptierten Zwischenständen unverändert; es wurden weder Erwartungen gelockert noch Tests ersetzt.

Stärken: echte CSV-/JSON-End-to-End-Fälle, unabhängige skalare Sharpe-, Drawdown-, SMA-, Drift-/Trade-/GDP-Rechnungen, exakte Revisions-/Zukunftsvergleiche, Kapitalerhaltung, Reihenfolge-/Kontextkontrollen, Fehlerinputs und Provenienz. Die 60/40-Kontrolle unterscheidet bewusst Jahresdrift von fälschlichen konstanten periodischen Gewichten. Die spätere GDP-Revision wird auch in einem verlängerten Lauf mit tatsächlichem Folgeentscheid geprüft.

Grenzen: Einige Wiederverwendungs-/Wrapperprüfungen vergleichen Ergebnisse mit demselben Helper oder reproduzieren Teile der Implementierung. Das belegt Integration, aber allein keine Formelrichtigkeit; die vorhandenen Handfälle und die zusätzlichen skalaren Auditkontrollen sind deshalb wesentlich. Exakte Tabellen-/Spalten-/Sortierprüfungen testen den zugesagten Vertrag. Exakte Floating-Point-Vergleiche innerhalb der festgeschriebenen Umgebung belegen Zukunftsunverändertheit, keine unbegrenzte plattformübergreifende Bytegleichheit.

Die Suite deckt initialen/erneuten Zielpositionsunterlauf nicht ab; GDP-Gewichtsunterlauf ist eine andere Stelle. Die bisherigen Result-Korruptionsfälle erfassen nicht den gesamten Drawdownpfad, die Summary-Exportgrenze oder konstante Ziele gegenüber der Config. Headerfehler werden geprüft, automatische Indexinterpretation überbreiter Datenzeilen bisher nicht. Deshalb widerlegen EB-01/02/03 den Schluss, 344 grüne Tests seien ein vollständiger Vertragsbeweis. Für einen späteren Korrekturauftrag braucht es negative Regressionen genau zu diesen Befunden; in diesem Audit wurden keine Testdateien ergänzt oder geändert.

## 12. Real-Data-Readiness und Dokumentationskonsistenz

Die allgemeine Engine besitzt einen lokalen, klar abgegrenzten Vier-Strategien-Pfad. Sie ist derzeit wegen EB-01 bis EB-03 noch nicht freeze-bereit. Ein realer Hauptversuch ist zusätzlich erst nach folgenden Studienarbeiten bereit:

| Studienvoraussetzung | Register |
|---|---|
| Konkrete Total-Return-Anlagen/Indizes, Dividenden-/Splitbehandlung, kompatible Basiswährung, Benchmark und Investierbarkeit | SB-01 |
| Zeitraum, Startkapital, reale Frequenz/Kalender, effektive Grenzen und begründetes `periods_per_year`; gegebenenfalls Handelskalender-/252-Regel | SB-02 |
| Reale RF-Serie, Einheit/Notierung, nachvollziehbare Konversion und exakt gemeinsame Intervalle | SB-03 |
| SMA-Fenster, reale Signalreihe, beobachtete Frequenz, vollständiger Warm-up und Eignung historischer Adjustierung | SB-04 |
| Länderproxies, GDP-Indikator/-Einheit, historische Vintages, echte Publikationsdaten und Quellenbelege | SB-05 |
| Erhaltene Raw-/Processed-Inputs, Config und Aufbereitung, unveränderlicher Code-/Paketstand, Umgebung und konkrete Archivzuordnung | SB-06 |
| Wissenschaftliche Beschreibung und Beispiele entsprechen den akzeptierten Regeln und tatsächlichen Schnittstellen | SB-07 |

Theorie, Analyse und Methodik wurden mit Entscheidungen und Engine verglichen. Besonders relevant sind alte Drawdown-/QuantStats-/Trendbeispiele, die RF-Rohdatenstruktur, ein unvollständiges Configbeispiel, RSI-/Short-Text, die gemischte Kommerbeschreibung und der abweichend formulierte Sharpe-Nenner. `decisions.md` entscheidet diese Konflikte bereits für die Engine; ein Textauftrag muss sie später sichtbar übertragen. Die aktuelle reine BIP-Strategie ist kein Nachbau des beschriebenen gemischten ETFs. Das Theorie-Risikobeispiel mit 0.8 Gesamtgewicht muss fachlich erläutert werden; die Engine erfindet kein Restkapital. Keiner dieser geschützten Texte wurde geändert.

Keine Liveadapter, FX, verzinstes Cash, Short, Kosten-/Steuer-/Inflationsmodelle, Optimierung, Batch oder Web/API gehören zum jetzigen akzeptierten Umfang. Ihr Fehlen ist hier kein weiterer Freeze-Fehler. OD-19-Zusatzanalysen sind separat vor ihrer Verwendung festzulegen. Ungeprüfte direkte Legacy-Helpers, nicht ausgeführte Plattformen und veraltete technische Standangaben sind NB-01 bis NB-03.

## 13. Kriterien für einen späteren v1.0-Freeze

1. EB-01 bis EB-03 in einem neuen ausdrücklich bestätigten Auftrag beheben oder den konkret zulässigen Vertrag ausdrücklich und fachlich konsistent abgrenzen; keine stillen Regeln/Toleranzänderungen.
2. Beide Portfolio-Allokationspfade, CSV-Zeilenstruktur und sämtliche Result-/Summary-/Configinvarianten mit unabhängigen negativen Gegenbeispielen prüfen. Kein scheinbar erfolgreicher falscher Run für diese Fälle.
3. Bestehende unveränderte fachliche Erwartungen beibehalten; vollständige relevante Suite, aktuelle isolierte Wheel-Installation, Paketprüfung und alle vier Offline-CLI-Demos erneut bestehen lassen. Fachliche Kontrollwerte, As-of/Lag und Kontextunverändertheit erhalten.
4. Manifest-/Archiv- und unveränderliche Code-Ausführungsbedingungen klar dokumentieren. Freeze-Tag muss genau dem fachlich abgenommenen, geprüften Code entsprechen; unterstützte Plattformen nur gemäss tatsächlichen Prüfungen nennen.
5. Autor prüft Befunde, repräsentative Handbeispiele und korrigierte Ergebnisse fachlich. SB-01 bis SB-07 bleiben als gesonderte verbindliche Checkliste vor dem realen Hauptversuch offen, solange ihre konkreten Werte/Belege fehlen.

Der Audit selbst erteilt keine v1.0-Freigabe und startet keinen Korrekturauftrag.

## 14. Abschlusskontrolle und Änderungsgrenze

Erlaubte Änderungen sind ausschliesslich die neuen `documentation/engine/final-audit.md`, `documentation/engine/final-open-issues.md` und ein angehängter Eintrag in `documentation/ai-usage/ai-usage-log.md`. Finale Git-Diff-/Status-/Hashkontrolle bestätigt diese Grenze: Von 90 anfänglich versionierten Dateien ist nur der erlaubte KI-Log geändert; die anderen 89 bleiben bytegleich. Sämtliche bisherigen Logbytes bleiben erhalten. Die beiden neuen Dokumente werden zusätzlich zum normalen Git-Diff als neue Dateidiffs geprüft, weil `git diff` allein unversionierte Texte nicht zeigt.

`git diff --check`, neue Text-/Struktur-/Linkkontrolle und finale Statusprüfung sind ausgeführt. `src/`, `tests/`, `configs/`, `pyproject.toml`, `requirements.lock`, AGENTS, Entscheidungen, Notebooks, Methodik, Bibliographie und fertige Buchkapitel sind unverändert. Prüfartefakte sind ignoriert; keine nicht erlaubten neuen Repository-Dateien verbleiben. Kein Commit, keine Implementierung, keine fachliche Auswahl und keine Quarto-/Notebook-Neuausführung.

**Stopp nach dem dokumentierten Audit.**
