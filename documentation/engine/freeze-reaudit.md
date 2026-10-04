# Finaler technischer Freeze-Re-Audit der Engine

**Datum:** 2026-10-04. **Ausführung:** Codex, ausschliesslich Prüfung und Dokumentation.
**Auftrag:** [Vollständiger Freeze-Re-Audit-Prompt](../ai-usage/prompts/2026-10-04-engine-v1-final-freeze-reaudit.md). Grundlage: `AGENTS.md`, unveränderte [OD-01 bis OD-13](decisions.md), [ursprünglicher Audit](final-audit.md), [Befundregister](final-open-issues.md), [Fixnachweis](blocker-fixes.md), [Blocker-Re-Audit](blocker-reaudit.md) sowie Implementierungs- und Testdokumentation.

**Geprüfter Code-Commit:** `270b7969a46bfbdb9f4614a4f6d88507540f6b92`. **Engine-Version:** **0.4.3**.
**Tatsächlicher HEAD:** `dd6face5345da37d6ab24b97aa885b490de2f67a`; Arbeitsbaum zu Beginn sauber. Der Diff zum Code-Commit enthält ausschliesslich den neuen Freeze-Re-Audit-Prompt. Engine, Tests, Configs und Abhängigkeitsdateien entsprechen exakt dem beauftragten Stand.

## Ergebnis und Umfang

| Befund | Status | Aktueller Nachweis |
|---|---|---|
| EB-01 | **CLOSED** | Nicht darstellbare positive Allokationen initial, im Helper und an späteren Jahresereignissen abgelehnt; echte Nullgewichte und sehr kleine darstellbare Positionen erhalten. |
| EB-02 | **CLOSED** | Drawdown, Summary/Status, Strategie-Set, Config-/GDP-Bindung und tatsächlich gehaltene Marktportfoliozustände werden vor Veröffentlichung geprüft. |
| EB-03 | **CLOSED** | Ursprünglicher Drei-/Vier-Felder-Fehler sowie weitere Breiten-/Header-/Quote-Fehler vor pandas abgelehnt; gültige CSV-Inhalte erhalten. |
| NEW-EB-01 | **CLOSED** | NUL-Inhalt in allen vier Dateiklassen einschliesslich Quotes/BOM, Header/Zusatzspalte und exaktem Minimalfall vor pandas und ohne Run-Ausgabe abgelehnt. |

**Neue ENGINE-BLOCKING-Befunde: 0** im gezielt geprüften Bereich. Keine Regression durch den letzten CSV-Fix gefunden. Die grüne Suite wurde durch unabhängige negative und positive Kontrollen ergänzt; das Urteil behauptet keine vollständige Widerlegung aller denkbaren Fehler.

Dieser Auftrag betrifft die technische Freeze-Grenze. SB-01 bis SB-07 bleiben für die reale Studie offen, NB-01 bis NB-03 bleiben dokumentiert. Keine erneute Auswahl von Anlagen, Zeitraum, RF-Serie, SMA-Parametern, GDP-Quelle oder Annualisierungsmethodik; keine neue Methodik und keine wissenschaftliche Textsynchronisierung.

## Plattform, Quellsuite und frisches Wheel

Geprüft: **Windows 11, Build 26300; CPython 3.14.0**, NumPy **2.3.5**, pandas **2.3.3**, pytest **8.4.2**. Alle zwölf für diese Plattform geltenden Pakete aus `requirements.lock` wurden auch in der Wheel-Umgebung gegen ihre Versionsbindung geprüft. Andere Plattformen/Interpreter wurden nicht ausgeführt.

| Prüfung | Tatsächlich ausgeführtes Ergebnis |
|---|---|
| Vollständige unveränderte Quellsuite | **441 passed in 113.49s**, Exit 0 |
| Vollständige unveränderte Wheel-Suite | **441 passed in 73.93s**, Exit 0 |
| `pip check`, Checkout und Wheel | Je **No broken requirements found.** |
| Temporäre Gegenkontrollen je Installation | **205: 180 erwartete Ablehnungen, 25 positive Kontrollen**, Exit 0 |
| Vier CLI-Demos je Installation | **8 Runs**, jeweils Exit 0, Netzwerk-Guard aktiv, unabhängige Kontrollen bestanden |
| Paket-/Quellvergleich | Alle enthaltenen Python-Dateien bytegleich zum aktuellen `src/` |

Die 205 Kontrollen sind temporäre Audit-Assertions, keine neuen versionierten Tests, und werden nicht zur Suitezahl 441 addiert. Warnungen bleiben Testfehler, der bestehende pytest-Netzwerk-Guard bleibt aktiv. Keine Testdatei oder Erwartung wurde geändert.

Das Wheel wurde in diesem Audit neu aus dem unveränderten Stand gebaut: `maturarbeit_engine-0.4.3-py3-none-any.whl`, **29899 Bytes**, SHA-256:

```text
9d11763938c5e983ed643bee635d7a8a7f03985527c40871d6acec247f270c5e
```

Frische Umgebung `.venv/freeze_reaudit/installed`, `include-system-site-packages = false`, `sys.base_prefix = C:\Python314`. Import- und Distributionsversion jeweils **0.4.3**. Import aus `.venv/freeze_reaudit/installed/Lib/site-packages/maturarbeit_engine/__init__.py`; Distributionsmetadaten bestätigen die Installation des konkreten Wheel-Archivs, kein Editable-Install. Keine globale Installation oder Lockänderung. Unterschiedliche Hashes früherer Neubauten sind durch Build-Metadaten möglich; dieser Hash identifiziert das tatsächlich geprüfte Archiv.

Tatsächlich ausgeführte Kernbefehle aus dem Repository-Stamm, PowerShell:

```powershell
.venv/Scripts/python.exe -m pytest -q --basetemp .venv/freeze_reaudit/pytest-source
.venv/Scripts/python.exe -m pip wheel --no-cache-dir --disable-pip-version-check --no-deps --wheel-dir .venv/freeze_reaudit/wheels .
.venv/Scripts/python.exe -m venv .venv/freeze_reaudit/installed
.venv/freeze_reaudit/installed/Scripts/python.exe -m pip install --no-cache-dir --disable-pip-version-check -c requirements.lock .venv/freeze_reaudit/wheels/maturarbeit_engine-0.4.3-py3-none-any.whl pytest==8.4.2
.venv/Scripts/python.exe -m pip check
.venv/freeze_reaudit/installed/Scripts/python.exe -m pip check
.venv/Scripts/python.exe .venv/freeze_reaudit/probes.py source
.venv/freeze_reaudit/installed/Scripts/python.exe .venv/freeze_reaudit/probes.py wheel
.venv/Scripts/python.exe .venv/freeze_reaudit/check_demos.py
.venv/Scripts/python.exe .venv/freeze_reaudit/extra_demo_checks.py
```

Die vollständige Wheel-Suite lief nach bestätigtem Installationsabschluss und Importprüfung aus `.venv/freeze_reaudit`:

```powershell
installed/Scripts/python.exe -m pytest -q -c C:/Users/modic/Documents/GitHub/Maturarbeit_Engine/pyproject.toml C:/Users/modic/Documents/GitHub/Maturarbeit_Engine/tests --basetemp C:/Users/modic/Documents/GitHub/Maturarbeit_Engine/.venv/freeze_reaudit/pytest-wheel
```

## Eigene Gegenproben und Codeprüfung

Die relevanten aktuellen CSV-, Mathematik-, Portfolio-, Result-, Kennzahlen-, Export- und Runnerpfade sowie die drei Blocker-Testdateien wurden kritisch gegen die festgelegten Verträge gelesen. Die vorherigen unabhängigen temporären Auditprogramme dienten als kontrollierte Reproduktionsbasis; sie wurden neu ausgeführt und um direkte vollständige Marktportfolio-Prüfungen, die NUL-/BOM-Matrix und zusätzliche positive BOM-Kontrollen erweitert. Sämtliche CSV-/Config-Fixtures wurden in neuen ignorierten Ablagen erzeugt. Keine Fixtures aus `tests/` importiert, keine alten Dateien/Runs überschrieben und kein Produktionscode manipuliert.

Wirtschaftliche Sollwerte werden unabhängig skalar nachgerechnet. Die vorhandene Drawdown-/Kennzahlenberechnung wird zusätzlich bewusst benutzt, um intern konsistente Fälschungen herzustellen; ihre lokale Konsistenz ersetzt die anschliessende Marktbindung nicht. Erwartete Ablehnung zählt nur bei passendem Fehler und ohne Ausgabe-/Staging-Verzeichnis an der geprüften Runner-/Exportgrenze.

### EB-01: initiale und jährliche Allokation

- Originalfall für beide Portfoliostrategien: Kapital `1e-200`, A-Ziel `1e-200`, B-Ziel `1`; A-Performance `1 → 1e300`, B `1 → 1`, historisch gültige GDP-Ziele für Country Weighting. Initiale Allokation scheitert mit `Positive target allocation underflowed to zero.`
- Direkter Helper: `rebalancing({A:0,B:1e-200}, {A:1e-200,B:1})` scheitert ebenfalls.
- Fixed-Jahresfall: Kapital `1e-200`, A-Ziel `1e-120`/B=1, anfängliche A-Position etwa `1e-320` darstellbar. B-Preis fällt bis 2020-12-31 von 100 auf `1e-8`; erst die erneute Zielallokation aus dem kleineren Vermögen unterläuft. Bewertung 2021-01-31 folgt, das Ereignis ist wirtschaftlich erforderlich.
- Country-Jahresfall: zunächst gültige GDP-60/40-Allokation; erst am 2020-12-31 verfügbare GDP-Ziele A=`1e-200`/B≈1 führen bei der Neuallokation zum selben ausdrücklichen Fehler.
- Positive Kontrollen: echte Nullgewichte bei Kapital `1e-200`, 100 und `1e200`; Position etwa `1e-320`; kleinster positiver Float `5e-324` bei Kapital 1; grosse reguläre Allokation. Zwei vollständige Runs mit kleinen darstellbaren Positionen behalten beide Assets. Zulässige Gewichte innerhalb bestehender Toleranz werden nicht normalisiert.

Weitere Randkontrollen zu Allokations-/Driftüberlauf und Driftunterlauf bestehen. Codeprüfung bestätigt den gemeinsamen `allocate_target_values()`-Pfad am Start und über `rebalancing()` an Jahresereignissen. Keine Entfernung, Normalisierung oder stille Nullsetzung positiver nicht darstellbarer Ziele. **EB-01 CLOSED.**

### EB-02: Ergebnis- und Exportbindung

Manipulierte mittlere/letzte Drawdown-Zeilen werden abgelehnt. Alle sieben Summary-Zahlenfelder wurden einzeln mit falschem endlichem Wert, NaN und Infinity verändert; sämtliche Varianten scheitern, insbesondere Endwert und Sharpe. Falscher Status, Summary-Struktur/-Strategiezuordnung und fehlende aktivierte bzw. zusätzliche deaktivierte Strategie scheitern ebenfalls. Ein vollständiger 20/80-Run unter 60/40-Config wird ausdrücklich an den Zielgewichten abgelehnt. Buy-and-Hold-Assetidentität/-Renditen, jährliche Ereignisse und historische GDP-Ziele/Provenienz bleiben gebunden.

**Exakter Marktportfolio-Minimalfall**, je für Fixed Rebalancing und Country Weighting: Kapital 100, A `100 → 110`, B `100 → 100`, Ziele 60/40. Gehaltene Positionen sind unabhängig **60/40 → 66/40**, korrektes Vermögen **106**. Die Fälschung **100 → 120**, Rendite 20 %, konsistente Drawdowns, gültige Ziele und plausibel wirkende Gewichte passiert bewusst die lokale Prüfung und erhält eine dazu passende neu berechnete Summary. Danach scheitern sowohl `validate_results(..., require_complete=True)` als auch `export_run()` mit `history disagrees with the market portfolio state.` Keine Ausgabe entsteht.

**Manipulation des gehaltenen Zwischenzustands**, je für beide Strategien: drei Bewertungen, A **100/110/88**, B **100/100/110**, keine Jahresereignisse. Korrekt **100/106/96.8** aus Positionen **60/40 → 66/40 → 52.8/44**. Die Fälschung schichtet nach der mittleren Bewertung verborgen auf **40/66** um, behält Gesamtwert 106 und leere Trades, setzt dazu passende Gewichte und verdient danach fälschlich **104.6** aus **32/72.6**. Lokal konsistente History/Drawdowns/Summary werden an beiden vollständigen Grenzen abgelehnt. Zusätzliche falsche Vortradepositionen, Transaktionen und nicht übernommene Nachtradezustände scheitern ebenfalls.

Codeprüfung: Rekonstruktion mit `context.performance`, Startkapital und bereits gegen Config/GDP geprüften Zielen über die gemeinsame `run_annual_portfolio()`-Funktion. Gelieferte falsche Vermögenswerte oder gehaltene Gewichte steuern die Erwartungsberechnung nicht. Runner und Export verwenden die vollständige Grenze vor jeder Ablage. **EB-02 CLOSED.**

### EB-03 und NEW-EB-01: Struktur und Originalbytes

Das ursprüngliche CSV mit Header `date,asset_id,performance_value` und Datenzeile `2019-12-31,2020-01-31,A,100` wird am Leser und im vollständigen Run abgelehnt: `expected 3, got 4`. Der Leser wird mit einem pandas-Mock geprüft, der ausdrücklich nicht aufgerufen werden darf. Für jede der vier Dateiklassen bleiben zusätzliche/fehlende Felder, mehrere Zusatzfelder ohne Header, leere Datenzeilen, doppelte/unbenannte Header und ungeschlossene Quotes vor pandas sowie im Runner abgelehnt.

**NUL-Matrix:** market/performance_value, assets/currency, risk_free/period_return und macro/value, jeweils unquoted/quoted und UTF-8 ohne/mit BOM: **16 Eingabefälle**. Zusätzlich exakt `performance_value = 1\x00e2` als tatsächliche Bytes, danach 110; ferner NUL im BOM-Header und in der letzten ungenutzten Zusatzspalte. Insgesamt **19 NUL-Eingaben je Installation**, jeweils separat am Leser und vollständigen Runner geprüft.

Alle 19 Fälle scheitern mit **DataValidationError** und Dateiname; der pandas-Mock bleibt ohne Aufruf. Kein vollständiger Run oder Staging-Ordner entsteht, alle Eingabe-/Configbytes bleiben unverändert. Der Minimalfall veröffentlicht insbesondere kein Vermögen 100/11000. Der Guard durchsucht den vollständigen unveränderten Bytesnapshot vor Dekodierung und Parsing, ohne Kürzung oder Reparatur.

Positive Kontrollen für alle vier Dateiklassen: korrekt gequotete Kommas und Zeilenumbrüche, vollständig benannte Zusatzspalten sowie NUL-freie UTF-8-/BOM-Dateien bleiben vollständig lauffähig. Feldinhalte, normaler RangeIndex und Originalbyte-SHA stimmen; BOM-Portfolio unabhängig **100/106/103.4**. Bestehende CSV-Strukturprüfung und `index_col=False` erhalten. **EB-03 CLOSED; NEW-EB-01 CLOSED.**

## Vier Demos, Hashes und Offline-Prüfung

Alle vier Originalkonfigurationen liefen im tatsächlichen CLI-Unterprozess jeweils aus Checkout und Wheel, vor den Dokumentationsänderungen. Unabhängig geprüft wurden sämtliche mitausgeführten Strategiehistorien, Renditen, Drawdowns und Summary-Werte sowie die folgenden Kontrollwerte:

| Demo | Endwert und Stichproben |
|---|---|
| Buy-and-Hold | **99**, Pfad 100/110/99; Jahresrendite `0.99^6-1`, Volatilität `sqrt(0.24)`, Sharpe aus RF-Überschussrenditen mit ddof=1, MDD −10 %. |
| Fixed Rebalancing | **116.4284**, Vortrade 72.6/40 → Ziel 67.56/45.04, Transaktionen −5.04/+5.04; neue Positionen verdienen die Folgeperiode, MDD −2 %. |
| Trend | **96.8**, Signale 0/1/1/0/0/1/1; Position leer/0/1/1/0/0/1, Pfad 100/100/110/88/88/88/96.8; SMAs skalar nachgerechnet, Cash 0. |
| Country Weighting | **117.667**, GDP 2018 initial 60/40; GDP 2019 beim Trade 50/50, A-Version verfügbar seit 2020-12-15/B seit 2020-09-01; spätere A-Revision 5000 nicht verwendet. Trades −16.3/+16.3 zu je 56.3; kein terminaler GDP-2020-Entscheid. |

Unregelmässige Rebalancing-/Country-Demos behalten korrekt fehlende Jahreskennzahlen samt Status. Qualitätsstatus, gemeinsame Bewertungen/RF-Perioden, erwartete vier/sechs/sieben/sieben Dateien, Standard-JSON, UTC, Version, Grenzen und Strategie-Set kontrolliert. Alle Input-, Resultat-, Einzelquell- und aggregierten Codehashes nachgerechnet. Checkout-Manifeste nennen HEAD `dd6face...`, `dirty=false`; Wheel-Manifeste Git `unavailable`. Fachliche CSVs und `data_quality.json` zwischen Installationen sowie gegenüber den vorherigen geprüften 0.4.3-Runs bytegleich.

| Demo | Checkout-Run unter `outputs/runs/` | Wheel-Run unter `outputs/runs/` |
|---|---|---|
| Buy-and-Hold | `synthetic_buy_hold-31e8c571989d4c3490e570928ed62b8f` | `synthetic_buy_hold-6b858aef85c74733b8a5c7bce5697ab1` |
| Rebalancing | `synthetic_rebalance-1224dc9dd86b41c3910fb5211bfd6338` | `synthetic_rebalance-c995af14002b4344a02a90245b8b8ac2` |
| Trend | `synthetic_trend-43a72abfbf7d43948965db9876b70966` | `synthetic_trend-d229a6e6e37f4e83864d57b36b10bef3` |
| Country Weighting | `synthetic_country_weighting-39da6ed39de0434490254202dcce7681` | `synthetic_country_weighting-e0d63754ace2489f994a2887fbe2807c` |

Für beide CLI-Interpreter wurde die Aktivierung des temporären `sitecustomize`-Guards separat bestätigt. Er sperrt Socket-Verbindungen (`connect`, `connect_ex`, `create_connection`) und DNS (`getaddrinfo`) in den tatsächlichen CLI-Prozessen; alle acht Backtests bestehen damit. Die Gegenproben sperren dieselben Funktionen. Statische Suche findet keine Runtime-Netzwerkimports oder Downloadpfade in `src/`. Paketbau/-installation mit separat genehmigtem Paketzugriff bleibt davon getrennt.

## Abschlusskontrolle und finales Freeze-Urteil

102 Ausgangsdateien per SHA-256 erfasst; vor Erstellung der Auditdokumentation alle 102 bytegleich. Nach Abschluss davon ausschliesslich das erlaubte KI-Log geändert, alle anderen **101 bytegleich**. Neu ausschliesslich dieses Dokument. Vollständiger bisheriger Loginhaltsblock bleibt als Bytepräfix erhalten; ein Eintrag wird an die bestehende Tabelle angehängt. Diff, neue Datei, Whitespace, Links und Codegleichheit zum vorgegebenen Commit geprüft.

Keine Änderung an Engine, Tests, Configs, Abhängigkeiten, AGENTS, Entscheidungen, historischen Audits/Fixnachweisen oder wissenschaftlichen Dateien. Temporäre Kontrollen, Fixtures, Logs, Wheel und frische Installation ausschliesslich unter ignoriertem `.venv/freeze_reaudit/`, Demo-Runs unter ignoriertem `outputs/runs/`; übliche ignorierte Build-Artefakte erlaubt. HEAD unverändert, kein Commit oder v1.0-Tag erstellt.

Autorvorgaben sind der genaue Code-Stand, die bestehenden Fachentscheidungen, Prüfkriterien und Schreibgrenze. Codex verantwortet die technischen Gegenkontrollen, die neue Audit-Dokumentation und das eng abgegrenzte technische Urteil. Fachliche Autorenkontrolle, reale Daten und deren historische Wahrheit werden hierdurch nicht bestätigt; SB-01 bis SB-07 bleiben vor der Hauptuntersuchung offen. Keine Hauptuntersuchung oder Synchronisierung wissenschaftlicher Texte erfolgt.

Alle vorgegebenen technischen Freeze-Kriterien sind erfüllt: vier Befunde CLOSED, 0 neue Engine-Blocker, 441 Quelltests und 441 Wheeltests erfolgreich, vier Demos in beiden Installationen offline erfolgreich, Engine-/Test-/Config-Code unverändert.

**ENGINE-V1.0-FREEZE TECHNICALLY READY**

Stopp nach diesem dokumentierten Audit.
