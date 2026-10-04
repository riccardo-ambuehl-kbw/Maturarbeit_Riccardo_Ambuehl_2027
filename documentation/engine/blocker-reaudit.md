# Unabhängiger Re-Audit der Engine-Blocker

**Datum:** 2026-10-04. **Ausführung:** Codex, ausschliesslich Prüfung und Dokumentation.

**Auftrag:** [Vollständiger Re-Audit-Prompt](../ai-usage/prompts/2026-10-04-engine-v1-blocker-reaudit.md). Grundlage: `AGENTS.md`, unveränderte [OD-01 bis OD-13](decisions.md), [ursprünglicher Audit](final-audit.md), [Befundregister](final-open-issues.md) und [Fixnachweis](blocker-fixes.md).

**Geprüfter Code-Commit:** `2020d5377449e23b1a9e7c36bb0caa1c3a9ebf44`. **Engine-Version:** 0.4.2.

## Urteil

**Das technische Freeze-Kriterium ist nicht erreicht.** Die vollständige Suite und die vier Demos bestehen im Checkout sowie im frisch installierten Wheel. Die zusätzlichen Gegenproben bestätigen die Sicherungen von EB-01 und EB-02. Die ursprüngliche CSV-Zeilenbreiten-/Indexlücke wird ebenfalls zuverlässig abgelehnt. Die weitergehende, ausdrücklich verlangte CSV-Sicherung gegen stilles Abschneiden scheitert jedoch bei NUL-Zeichen innerhalb von Feldern.

| Befund | Re-Audit-Ergebnis | Begründung |
|---|---|---|
| EB-01 | **CLOSED** | Positive nicht darstellbare Zielpositionen scheitern initial, im Helper und bei tatsächlich späteren Jahresallokationen beider Portfoliostrategien. Darstellbare kleine Positionen und echte Nullgewichte bleiben zulässig. |
| EB-02 | **CLOSED** | Alle verlangten Result-/Summary-/Config-Korruptionen werden vor Veröffentlichung abgelehnt, einschliesslich intern konsistenter falscher Marktportfoliozustände und eines neuen Umschichtungs-Gegenbeispiels. |
| EB-03 | **STILL OPEN** | Der ursprüngliche Überbreitenfehler ist behoben. Für das im Re-Audit ausdrücklich geforderte Kriterium „keine Daten still abgeschnitten“ bleibt eine zusätzlich entdeckte Parserlücke offen: **NEW-EB-01**. |

**Ein neu entdeckter ENGINE-BLOCKING-Befund:** NEW-EB-01, stilles Kürzen von CSV-Feldinhalten am NUL-Zeichen. Seine acht Eingabevarianten sind ein gemeinsamer Befund, keine acht unterschiedlichen Fehler. Die Zuordnung zu EB-03 bezeichnet das nicht erfüllte CSV-Abnahmekriterium; sie behauptet nicht, der ursprüngliche Drei-/Vier-Felder-Fehler sei weiterhin reproduzierbar. Es gibt keinen zusätzlich gefundenen numerischen oder Portfoliozustands-Blocker.

SB-01 bis SB-07 und NB-01 bis NB-03 bleiben bewusst offen und werden hier nicht neu bewertet. Es wurde keine Korrektur implementiert, kein Commit und kein Tag erstellt.

## Git-Stand, Plattform und Lesekontrolle

Der tatsächliche HEAD ist `d0c3f75c01747b0cb079a6e19b65151e0f32580f`. Der Working Tree war vor den Prüfungen sauber. `git diff --name-status 2020d5377449e23b1a9e7c36bb0caa1c3a9ebf44 HEAD` enthält ausschliesslich den neu dokumentierten Re-Audit-Prompt. Engine, Tests, Configs und Abhängigkeitsdateien entsprechen deshalb exakt dem beauftragten Code-Commit. Import- und Distributionsversion wurden im Checkout und im Wheel als 0.4.2 geprüft.

Plattform: **Windows 11, Build 26300, CPython 3.14.0**, NumPy **2.3.5**, pandas **2.3.3**, pytest **8.4.2**. Die finale Wheel-Umgebung entspricht auch den transitiven Versionen aus der unveränderten `requirements.lock`, insbesondere pytz/tzdata 2026.4. Andere Plattformen und Interpreter wurden nicht ausgeführt.

Gelesen und gegen den Code abgeglichen: vollständiger Re-Audit-Prompt und AGENTS.md, Entscheidungen, beide historischen Auditdokumente, Blocker-Fixnachweis, Implementierungs- und Testdokumentation, sämtliche aktuellen Python-Engine-Dateien, die beiden neuen Testdateien sowie die für Mathematik, Kalender, RF, Lag, GDP, Resultatvertrag und Provenienz relevanten bisherigen Tests. Die beiden neuen Testdateien wurden vollständig kritisch gelesen. Die historischen fachlichen Quellen bleiben durch die unveränderten Entscheidungen und den ursprünglichen Audit eingeordnet; kein neuer vollständiger Methodik-Audit und keine wissenschaftliche Textänderung.

Die unabhängigen Gegenbeispiele verwenden neu erzeugte synthetische CSVs/Configs und importieren **keine** Fixtures aus den versionierten Tests. Wirtschaftliche Kontrollwerte werden skalar vorgegeben bzw. nachgerechnet. Die gemeinsame Engine-Kennzahlen-/Drawdownberechnung wird bewusst zusätzlich verwendet, um intern gültige Fälschungen für die Exportgrenze herzustellen. Das trennt lokale Tabellenkonsistenz von der Bindung an den Marktcontext.

## Tatsächlich ausgeführte Tests und Paketprüfung

| Prüfung | Ergebnis |
|---|---|
| Vollständige unveränderte Quellsuite, finale eigene Temp-Ablage | **428 passed in 124.92s**, Exit 0 |
| Vollständige unveränderte Suite gegen installiertes Wheel mit Lock-Versionen | **428 passed in 77.11s**, Exit 0 |
| `pip check`, Checkout und Wheel | Je **No broken requirements found.** |
| Unabhängiges temporäres Gegenprobenprogramm je Installation | **153 Kontrollen: 132 erwartete Ablehnungen und 21 positive Kontrollen**, Exit 0 |
| Zusätzliche NUL-Gegenbeispiele je Installation | **8 fehlerhaft akzeptierte vollständige Runs**, vier Eingabetypen jeweils unquoted/quoted |
| Zusätzlicher minimaler NUL-Nachweis je Installation | Ungültiger Rohwert wird verändert und als erfolgreicher Buy-and-Hold-Run veröffentlicht |
| Vier Original-CLI-Demos je Installation | Acht Runs, jeweils Exit 0, skalare Kontrollen und zusätzliche Metadaten-/Perioden-/Trade-/SMA-/GDP-Prüfung bestanden |
| Offline-Guard | Socket-Verbindungen und DNS in beiden tatsächlichen CLI-Installationen gesperrt; alle acht Demos erfolgreich |
| Wheel-/Checkout-Quellvergleich | Jede enthaltene Python-Datei bytegleich zur aktuellen Datei unter `src/` |

Die 153 Kontrollen sind temporäre Audit-Assertions ausserhalb von `tests/`; sie werden nicht zur Zahl 428 addiert. Eine erwartete Ablehnung ist nur erfolgreich, wenn ein `ValueError` auftritt und bei der Export-/Runnerprüfung kein Ausgabeordner entsteht. Die acht NUL-Akzeptanzen sind separat als Fehlernachweise gezählt, nicht als bestandene fachliche Prüfungen.

Frisch gebautes Wheel: `maturarbeit_engine-0.4.2-py3-none-any.whl`, **29873 Bytes**, SHA-256:

```text
ef2eb03cc6e6d35eaf88f3f502d646084da98a5a2ff065c7d005904b73a6974d
```

Frische Umgebung: `.venv/blocker_reaudit/installed`, `include-system-site-packages = false`, `sys.base_prefix = C:\Python314`. Tatsächlich importierte Engine:

```text
C:/Users/modic/Documents/GitHub/Maturarbeit_Engine/.venv/blocker_reaudit/installed/Lib/site-packages/maturarbeit_engine/__init__.py
```

Ausgeführte Kernbefehle im Repository, PowerShell:

```powershell
.venv\Scripts\python.exe -m pytest -q --basetemp .venv/blocker_reaudit/pytest-source
.venv\Scripts\python.exe -m pip wheel . --no-deps --wheel-dir .venv/blocker_reaudit/wheels
.venv\Scripts\python.exe -m venv .venv/blocker_reaudit/installed
.venv\blocker_reaudit\installed\Scripts\python.exe -m pip install .venv/blocker_reaudit/wheels/maturarbeit_engine-0.4.2-py3-none-any.whl pytest==8.4.2
.venv\blocker_reaudit\installed\Scripts\python.exe -m pip install -c requirements.lock -r requirements.lock
.venv\blocker_reaudit\installed\Scripts\python.exe -m pip check
.venv\Scripts\python.exe .venv/blocker_reaudit/probes.py source-confirmed
.venv\blocker_reaudit\installed\Scripts\python.exe .venv/blocker_reaudit/probes.py wheel
.venv\Scripts\python.exe .venv/blocker_reaudit/check_demos.py
.venv\Scripts\python.exe .venv/blocker_reaudit/extra_demo_checks.py
.venv\Scripts\python.exe .venv/blocker_reaudit/nul_repro.py source
.venv\blocker_reaudit\installed\Scripts\python.exe .venv/blocker_reaudit/nul_repro.py wheel
```

Die Wheel-Suite lief aus `.venv/blocker_reaudit` mit absoluten Pfaden zu installiertem Interpreter, `tests/`, `pyproject.toml` und eigener Ablage `pytest-wheel-locked`. Keine Editable-Installation in dieser Umgebung, keine globale Installation und keine Änderung der Versionsbindung. Paketbau/-installation verwendeten separat freigegebenen Netzwerkzugriff; die eigentlichen Backtests liefen mit gesperrtem Netzwerk.

Zusätzlich ausgeführte Vorläufe: erste Quellsuite **428 passed in 107.19s**, danach eine Windows-Aufräumausnahme für `pytest-current` in der fremden Standard-Temp-Ablage; die eigene finale Ablage behebt diese Aufrufstörung ohne Codeänderung. Erste Wheel-Suite vor der zusätzlichen transitiven Lock-Ausrichtung **428 passed in 68.26s**; anschliessend vollständige Wiederholung mit den finalen Lock-Versionen. Zwei erste Buildversuche scheiterten an fehlendem lokalen setuptools bei `--no-build-isolation` bzw. gesperrtem Paketnetzwerk; der reguläre isolierte Build mit genehmigtem Paketzugriff bestand. Ein temporäres Gegenprobenprogramm erwartete zuerst einen zu spezifischen Überlauf-Fehlertext; die tatsächlich korrekte Ablehnung lautete `Positions must be complete and finite.` Nur die Prüftext-Erwartung wurde korrigiert und das ganze Programm erneut erfolgreich ausgeführt. Keine Produktionsdatei oder versionierte Testerwartung wurde angepasst.

## EB-01: numerische Allokationsprüfung

Die ursprünglichen Startfälle wurden für Fixed Rebalancing und Country Weighting separat aus neuen CSVs reproduziert: Kapital `1e-200`, A-Ziel `1e-200`, B-Ziel `1`, A-Performance `1 → 1e300`, B `1 → 1`. GDP 2019 liefert für die Länderstrategie dieselben positiven Ziele und war vor dem Start verfügbar. Beide Runs brechen bereits bei der Anfangsallokation mit `Positive target allocation underflowed to zero.` ab. Kein Asset wird entfernt, kein erfolgreicher Nullpositions-Lauf veröffentlicht.

Der direkte Aufruf `rebalancing({A:0,B:1e-200}, {A:1e-200,B:1})` scheitert ebenfalls. Tatsächlich spätere Ereignisse wurden am 2020-12-31 mit noch folgender Bewertung 2021-01-31 geprüft:

- Fixed Rebalancing: Startkapital `1e-200`, Ziel A=`1e-120`/B=`1`, anfänglich positive darstellbare A-Position etwa `1e-320`. B verliert bis zum Jahresevent durch Preis `100 → 1e-8` einen Faktor etwa `1e-10`; A bleibt positiv. Erst die erneute A-Zielallokation aus dem nun etwa `1e-210` grossen Portfolio unterläuft und wird abgelehnt.
- Country Weighting: Start-GDP 60/40 und zunächst darstellbare Positionen. Erst am Jahresevent verfügbare GDP-2020-Ziele A=`1e-200`/B≈1 führen zum positiven, nicht darstellbaren Zielwert und zum selben Abbruch.

Zusätzliche Kontrollen: echte Nullgewichte bei Kapital `1e-200`, 100 und `1e200`; positive Zielposition etwa `1e-320`; kleinster positiver Float `5e-324` als darstellbare Einzelposition bei Kapital 1; gewöhnliche 60/40-Allokation bei Kapital `1e308`; nicht darstellbare Aufteilung des kleinsten positiven Kapitals; Allokationsüberlauf nahe dem maximalen Float; Drift-Unterlauf und Drift-Überlauf. Nicht darstellbare Zustände werden abgelehnt. Zwei vollständige Runs mit sehr kleinen darstellbaren Positionen behalten beide Assets und das korrekte Vermögen. Zulässige Zielabweichungen innerhalb der bestehenden Toleranz werden ausdrücklich nicht normalisiert.

Codeprüfung bestätigt dieselbe Allokationsstelle für initiale und jährliche Ziele; kein neuer Finanzalgorithmus. Reguläre 60/40-/GDP-Ziele funktionieren in den Demos und der vollständigen Suite. **EB-01: CLOSED.**

## EB-02: vollständige Exportbindung und wirtschaftliche Zustände

| Teilbereich | Unabhängige Manipulation und Ergebnis |
|---|---|
| Drawdown | Mittlere, letzte und mehrere Zeilen gleichzeitig bei unverändertem Vermögen/Renditen geändert; jede Variante abgelehnt. |
| Summary | Alle sieben Zahlenfelder einzeln mit falschem endlichem Wert, NaN und Infinity manipuliert; jeweils abgelehnt. Fehlende/zusätzliche Zeilen, falsche Strategie, zusätzliche Spalte und falscher Status ebenfalls abgelehnt. |
| Strategiemenge | Fehlende aktive bzw. zusätzliche nicht aktive Strategie: Export scheitert am vollständigen aktivierten Set. |
| Buy-and-Hold | Falsches Asset bei verschiedenen und bei identischen Reihen abgelehnt; korrekte Assetkennung mit falschen Renditen ebenfalls abgelehnt. |
| Fixed-Konfiguration | Vollständiger Run mit 20/80 unter 60/40, falsche Assetmenge und zwischen Bewertungen geändertes Ziel abgelehnt. |
| Jahresereignisse | Fehlende, zusätzliche, initiale und finale Trades bei beiden Portfoliostrategien abgelehnt; flat-price Nulltransaktionen verdecken kein fehlendes Ereignis. |
| Country Weighting | Falsche historische GDP-Ziele, falsche Proxyzuordnung und manipulierte Versionsprovenienz abgelehnt. Die bisherigen Prüfungen von Ländern, Metadaten, Einheiten, As-of-Auswahl, Zielpersistenz und Kalender bleiben aktiv. |
| Marktportfolio | Falsches Vermögen, einzelne Vor-/Nachgewichte, Drift, finaler Zustand, kapitalerhaltende falsche Vortradepositionen, Ziel-/Transaktionswerte und nicht übernommene Nachtradepositionen abgelehnt. |

Die bestehenden Tests ergänzen insbesondere nicht verfügbare Kennzahlen, Einzel-/Mehrstrategie-Status, Ziel-/Gewichtstoleranzen, mehrere Jahresereignisse und die separate direkte vollständige Validierung. Im Export liegen Result-/Summary-Prüfungen weiterhin vor dem Anlegen von Ausgabe-/Staging-Verzeichnissen; die Eingabe-Hashkontrolle bleibt zuerst.

### Exakter Restlücken-Nachweis

Für jede Portfoliostrategie: A `100 → 110`, B `100 → 100`, Kapital 100 und Ziele 60/40. Unabhängig ergeben gehaltene Positionen 66/40 und Vermögen **106**. Ersetzt werden History durch **100 → 120**, Rendite 0.2, Drawdown 0 und formal passende Gewichte bei leeren Trades. Country-GDP-Entscheidung/Provenienz bleiben gültig. Die Summary wird aus der falschen History neu berechnet. Das Resultat passiert die lokale Prüfung, scheitert aber am vollständigen Export mit `rebalance history disagrees with the market portfolio state.` bzw. entsprechender Country-Meldung. Checkout und Wheel verhalten sich identisch; kein Ausgabeordner.

### Zusätzliches neues wirtschaftliches Gegenbeispiel

Dieses Beispiel steht so nicht in `test_portfolio_state_validation.py`: drei Monatsbewertungen, A **100 → 110 → 88**, B **100 → 100 → 110**, Ziele 60/40, keine Jahresereignisse. Korrekt sind Positionen **60/40 → 66/40 → 52.8/44** und Vermögen **100 → 106 → 96.8**.

Die Fälschung rotiert nach der mittleren Bewertung heimlich von 66/40 auf **40/66**. Das mittlere Vermögen bleibt 106, die Tabellen nennen passende Vor-/Nachgewichte 40/106 und 66/106, Referenzziele bleiben 60/40 und die Trade-Tabelle bleibt leer. Aus diesen falschen gehaltenen Positionen entstehen zuletzt **32/72.6**, Vermögen **104.6**, passende Driftgewichte, neu berechnete Renditen/Drawdowns und konsistente Summary. Alle lokalen Bilanzen sind stimmig.

Sowohl Fixed Rebalancing als auch Country Weighting passieren damit die lokale Prüfung, werden aber an der vollständigen Exportgrenze aufgrund der tatsächlichen Markt-Zustandsfolge abgelehnt. Dies prüft eine verschwiegene kapitalerhaltende Umschichtung und deren wirtschaftliche Folgewirkung, zusätzlich zu den vorhandenen reinen Endwert-/Gewichtsfehlern.

Die Codeprüfung zeigt: Rekonstruktion mit `context.performance`, Startkapital und zuvor gegen Config/GDP geprüften Zielen; gespeicherte Vor-/Nachgewichte oder Vermögenswerte steuern die Erwartungsberechnung nicht. Erhaltene Toleranzen und Reihenfolgeunabhängigkeit sind durch die unveränderte Suite geprüft. **EB-02: CLOSED.**

## EB-03: Breite, Header, Quotes und Feldinhalt

Das ursprüngliche Beispiel mit Header `date,asset_id,performance_value` und einer Datenzeile `2019-12-31,2020-01-31,DEMO,100` scheitert an `expected 3, got 4`. Im unabhängigen Versuch ist pandas zusätzlich durch einen fehlschlagenden Platzhalter ersetzt: Der Breitenfehler tritt tatsächlich **vor** jedem pandas-Aufruf auf.

Für **market, assets, risk_free und macro** wurden jeweils zusätzliche, fehlende und mehrere zusätzliche Felder, leere Datenzeilen, doppelte/unbenannte Header und nicht geschlossene Quotes geprüft. Alle 28 Varianten werden vor pandas sowie im vollständigen Runner ohne Ausgabe abgelehnt. Korrekt gequotete Kommas, gequotete Zeilenumbrüche und vollständig benannte Zusatzspalten bleiben bei allen vier Eingabetypen erhalten und vollständig lauffähig. Alle gelesenen Felder wurden gegen `csv.reader` verglichen; der DataFrame hat einen normalen `RangeIndex`, keine impliziten Datumsspalten im Index.

Damit ist der konkrete ursprüngliche Zeilenbreiten-/Indexfehler geschlossen. Das zusätzliche NUL-Gegenbeispiel verletzt jedoch das ebenfalls verlangte Verbot stillen Abschneidens. **EB-03 im gesamten geforderten CSV-Abnahmeumfang: STILL OPEN.** Der nachstehende neue Befund ist die einzige verbleibende CSV-Sperre dieses Re-Audits.

## NEW-EB-01: stille CSV-Feldkürzung am NUL-Zeichen

**Klassifikation:** ENGINE-BLOCKING. **Status:** offen, nicht korrigiert.

**Betroffene Funktion:** `src/data/normalize.py:read_csv_snapshot`, gemeinsam für Markt, Metadaten, RF und Makro. Nachgelagerte fachliche Validatoren erhalten bereits veränderten Feldinhalt.

**Ursache:** `csv.reader(..., strict=True)` erhält NUL-Zeichen innerhalb eines korrekt breiten Feldes. Die Vorprüfung kontrolliert nur Header und Feldzahl. Der anschliessende pandas-C-Parser kürzt das Feld am NUL-Zeichen, obwohl `dtype=str`, `keep_default_na=False` und `index_col=False` gesetzt sind. Die Engine prüft und verarbeitet danach den gültig aussehenden Präfix. Dies ist ein zusätzlicher neu entdeckter Parserfehler; eine durch die Fixes neu eingeführte Regression wurde damit nicht nachgewiesen.

**Erwartet:** Ungültige Pflichtwerte mit NUL-Zeichen ausdrücklich ablehnen oder ihren vollständigen Inhalt unverändert an die vorhandene fachliche Validierung weiterreichen. Keine stillschweigende Datenreparatur und keine Veröffentlichung eines daraus erzeugten Runs.

**Tatsächlich:** `performance_value` mit Rohinhalt `1\x00e2` wird zu String `1`. Die unveränderte numerische Validierung würde den vollständigen Rohwert ablehnen; nach dem CSV-Parser akzeptiert der vollständige Runner ihn jedoch. A-Preise erscheinen als 1/110, Kapital 100 wird als **100/11000** und Periodenrendite **109 = 10900 %** exportiert. `data_quality.json.validation_status` lautet `passed`. Der korrekte Input-SHA enthält weiterhin die NUL-Bytes; Hashkonsistenz verhindert die falsche Interpretation nicht.

### Selbständig reproduzierbarer Minimalfall

Der folgende Python-Block erzeugt nur neue synthetische Dateien unter dem ignorierten `.venv/blocker_reaudit` und ruft die bestehende Engine auf. In der Bytezeichenfolge bezeichnet `\x00` ein wirkliches NUL-Byte, nicht die vier Zeichen eines Text-Escapes.

```python
from pathlib import Path
from tempfile import mkdtemp
import json
from maturarbeit_engine.engine.simulation import run_simulation

p = Path(mkdtemp(prefix="nul-counterexample-", dir=".venv/blocker_reaudit"))
(p / "market.csv").write_bytes(
    b"date,asset_id,performance_value\n"
    b"2020-01-31,A,1\x00e2\n2020-02-29,A,110\n"
)
(p / "assets.csv").write_bytes(
    b"asset_id,name,asset_class,country,currency,provider,provider_symbol\n"
    b"A,Artificial,synthetic,C_A,CHF,audit,A\n"
)
cfg = {
    "schema_version": "1.0", "run_name": "nul_minimal",
    "period": {"start": "2020-01-31", "end": "2020-02-29"},
    "start_capital": 100, "base_currency": "CHF",
    "periods_per_year": 12, "period_frequency": None,
    "data": {"market": "market.csv", "assets": "assets.csv"},
    "strategies": {"buy_hold": {"enabled": True, "asset": "A"}},
    "output_dir": "runs",
}
(p / "config.json").write_text(json.dumps(cfg), encoding="utf-8")
out = run_simulation(p / "config.json")  # Erwartet: Eingabefehler.
print(out.result.portfolio_history.portfolio_value.tolist())
# Tatsaechlich unter 0.4.2: [100.0, 11000.0]
```

Tatsächlich ausgeführt im Checkout und im frisch installierten Wheel über `.venv/blocker_reaudit/nul_repro.py`. Belege: `nul-source.txt`/`nul-wheel.txt`; veröffentlichte fehlerhafte Prüf-Runs:

- `.venv/blocker_reaudit/nul-minimal-source/runs/nul_minimal-73c524f749b6499f95403d24380ac03d`
- `.venv/blocker_reaudit/nul-minimal-wheel/runs/nul_minimal-430a4c75f7764c02986f575cfea754ec`

### Reichweite in allen vier Eingabetypen

| Eingabetyp / Pflichtspalte | Vollständiger Rohfeldinhalt | Tatsächlich übergebener Präfix | Vollständiger Run |
|---|---|---|---|
| Markt / `performance_value` | `100.0\x00INVALID` | `100.0` | Erfolgreich, Qualitätsstatus `passed` |
| Assets / `currency` | `CHF\x00INVALID` | `CHF` | Erfolgreich; die eigentlich abweichende Währung wird verdeckt |
| RF / `period_return` | `0.001\x00INVALID` | `0.001` | Erfolgreich; ungültiger Zahleninhalt wird verdeckt |
| Makro / `value` | `60\x00INVALID` | `60` | Erfolgreich; ungültiger GDP-Inhalt wird verdeckt |

Jede Variante wurde ungequotet und mit vollständig gequoteten Feldern gegen **beide** Installationen erfolgreich als Fehlakzeptanz reproduziert. Insgesamt 16 vollständige problematische Runs plus zwei Minimalruns. Vor jeder Simulation wurden Rohfeld/Präfix, korrekte Breite und nachher Qualitätsstatus und Inputhash kontrolliert. Detaillierte Pfade stehen in den ignorierten `probe-results-source-confirmed.json` und `probe-results-wheel.json`.

**Empfehlung, nicht implementiert:** Gemeinsamen CSV-Lesepfad so absichern, dass NUL-haltiger Inhalt nicht gekürzt werden kann; eine ausdrückliche technische Ablehnung vor pandas wäre mit dem bestehenden Datenvertrag vereinbar. Danach unabhängige Negativkontrollen für alle vier Eingabetypen und Quotes sowie erneute unveränderte Suite/Wheel-/Demo-Prüfung. Keine neue finanzwirtschaftliche Entscheidung erforderlich. Dieser Audit autorisiert oder implementiert diesen Fix nicht.

## Demo- und Cross-Check-Ergebnisse

Alle vier Originalkonfigurationen liefen aus einem anderen Arbeitsverzeichnis jeweils mit `python -m maturarbeit_engine run --config <absoluter Configpfad>`. Der temporäre `sitecustomize`-Guard sperrt `connect`, `connect_ex`, `create_connection` und `getaddrinfo` auch in den tatsächlichen CLI-Unterprozessen; seine Aktivierung wurde für beide Interpreter separat bestätigt. Die temporären Gegenproben sperren ebenfalls Socket/DNS. Paketnetzwerk und Simulation sind getrennt.

| Demo | Unabhängig geprüfter zentraler Verlauf / Ergebnis |
|---|---|
| Buy-and-Hold | 100 → 110 → **99**; Jahresrendite `0.99^6-1`, Volatilität `sqrt(0.24)`, Sharpe über RF-Überschussrenditen und `ddof=1`, MDD −10 %. |
| Rebalancing | 100 → 106 → 112.6 → 110.348 → **116.4284**; Vortrade 72.6/40, Ziel 67.56/45.04, Trades −5.04/+5.04, MDD −2 %. |
| Trend | 100 → 100 → 110 → 88 → 88 → 88 → **96.8**; Signale 0/1/1/0/0/1/1, Position leer/0/1/1/0/0/1, Cash 0, Jahresrendite `0.968^2-1`, MDD −20 %. |
| Country Weighting | 100 → 106 → 112.6 → 112.6 → **117.667**; initial GDP 2018 60/40, dann GDP 2019 50/50, je 56.3 Zielwert und Trades −16.3/+16.3; MDD 0. |

Geprüft wurden auch sämtliche mitausgeführten Strategien, echte Periodenrenditen, komplette Drawdowns und Summary-Zahlen. Unregelmässige Rebalancing-/Country-Demos behalten korrekt nicht verfügbare Jahreskennzahlen samt Status. Gemeinsame Bewertungsdaten und RF-Intervallgrenzen stimmen exakt; Warm-up zählt nicht zur Performance. SMAs wurden zusätzlich aus den Original-Signalwerten skalar berechnet. GDP-Auswahl verwendet A=50 verfügbar seit 2020-12-15 und B=50 seit 2020-09-01, nicht die Revision 5000 ab 2021-02-01; terminales GDP 2020 erzeugt keine Schlussentscheidung. Ziele und Trades stimmen mit den unabhängigen Positionsrechnungen überein.

Alle acht Manifeste und Qualitätsberichte wurden strikt gelesen. Geprüft: vier/sechs/sieben/sieben Dateien, UTC, Versionen, effektiv/angefordert, Input-/Output-/Einzelquell-/aggregierte Codehashes, Strategiemenge, Datenqualität und RF-Zeilenanzahl. Checkout-Manifeste nennen HEAD `d0c3f75...`, `dirty=false` vor den Dokumentationsänderungen; Wheel-Manifeste nennen Git `unavailable`. Sämtliche fachlichen CSVs und `data_quality.json` sind zwischen beiden Installationen bytegleich. Damit wurde für reguläre Eingaben keine Fix-Regression gefunden; dies widerlegt den separaten NUL-Fehler nicht.

| Demo | Checkout-Run unter `outputs/runs/` | Wheel-Run unter `outputs/runs/` |
|---|---|---|
| Buy-and-Hold | `synthetic_buy_hold-31c1249cb4114ebc9b6089f0e267abb0` | `synthetic_buy_hold-5b91ceef68b4401aad486c7b5ee7a92c` |
| Rebalancing | `synthetic_rebalance-e24cea47706b4a46a63004228f9dd398` | `synthetic_rebalance-ddef3ffa9c744beaae56a3cf51ee3a21` |
| Trend | `synthetic_trend-db01c3de1e3d4d4b8cf64e6549be4164` | `synthetic_trend-176367b59a14486ebd4816d25ddc246d` |
| Country Weighting | `synthetic_country_weighting-ede4fa44f31e450e84113c24cb84de1a` | `synthetic_country_weighting-7b1e3e15b3e944c2ac993785fc0c63e4` |

## Kritische Testbewertung

Die 62 Fälle in `test_blocker_fixes.py` erfassen tatsächlich positive Zielpositionsunterläufe, vollständige Drawdown-/Summary-/Configbindungen und CSV-Breitenfehler. Jährliche Unterlauf-Fixtures starten mit darstellbaren Positionen, sodass sie die Zielallokation am späteren Ereignis prüfen. Die 22 Fälle in `test_portfolio_state_validation.py` lassen die 16 Fälschungsvarianten bewusst erst die lokale Prüfung und die aus der falschen History neu berechnete Summary passieren; anschliessend prüfen sie direkte vollständige Validierung und Export. Sechs positive Kontrollen decken unter anderem Handrechnung, Kontextunverändertheit, Zeilenreihenfolge und bestehende Toleranz ab.

Wiederverwendung von Drawdown/Kennzahlen für intern gültige Fälschungen ist sinnvoll, beweist deren finanzmathematische Richtigkeit jedoch nicht allein. Die unabhängigen Positions- und skalaren Demo-Rechnungen ergänzen dies. Die neue verschwiegene Umschichtung erweitert die Widerlegungsversuche über die vorhandenen exakten Fälle hinaus. Die CSV-Tests enthalten bislang kein NUL-Zeichen und prüfen keine solche Inhaltsabweichung zwischen Standardbibliothek und pandas; genau deshalb kann die gesamte unveränderte Suite trotz NEW-EB-01 grün sein. Keine Tests wurden verändert, hinzugefügt oder abgeschwächt.

## Abschlusskontrolle, Verantwortung und Freeze

98 zu Beginn versionierte Dateien wurden per SHA-256 gesichert. Nach Abschluss ist ausschliesslich `documentation/ai-usage/ai-usage-log.md` davon verändert; dessen vollständiger bisheriger Byteinhalt bleibt als Präfix erhalten. Alle übrigen 97 Dateien sind bytegleich. Neu ist ausschliesslich dieses Dokument. Git-Diff-/Status-/Whitespace-/Linkkontrolle und expliziter Codevergleich gegen `2020d537...` bestätigen die erlaubte Grenze.

Keine Änderung an Engine, Tests, Configs, pyproject.toml, requirements.lock, Entscheidungen, historischen Audit-/Fixnachweisen oder geschützten wissenschaftlichen Dateien. Temporäre Prüfprogramme, Fixtures, Logs und Installationsartefakte liegen in ignorierten Bereichen. HEAD bleibt unverändert; kein Commit oder v1.0-Tag.

Autorvorgaben sind Code-Stand, OD-01 bis OD-13, Re-Auditumfang und Schreibgrenze. Codex verantwortet technische Reproduktionen, Kontrollrechnungen, Klassifikation und Dokumentation. Empfehlungen sind nicht als Entscheidungen übernommen oder umgesetzt. Fachliche Kontrolle des Autors, reale Daten und historische Quellenwahrheit werden durch die synthetischen Prüfungen nicht bestätigt.

**Freeze-Urteil: nicht technisch bereit.** EB-01 und EB-02 sind geschlossen; EB-03 erfüllt wegen NEW-EB-01 das geforderte CSV-Abnahmekriterium noch nicht. Der positive Freeze-Satz wird daher nicht erteilt. SB-01 bis SB-07 bleiben zusätzlich vor einem realen Hauptversuch zu lösen; wissenschaftliche Texte und reale Daten sind mit diesem Audit nicht freigegeben. **Stopp nach dieser Dokumentation.**
