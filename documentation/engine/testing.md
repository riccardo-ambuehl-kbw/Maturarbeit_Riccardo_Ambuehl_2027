# Engine v1 – ausgeführte Core- und Rebalancing-Prüfungen

**Core-Prüfung:** 2026-10-03. **Plattform:** Windows, CPython 3.14.0.
**Versionen:** Engine 0.1.0, NumPy 2.3.5, pandas 2.3.3, pytest 8.4.2; weitere Versionen siehe `requirements.lock`.

## Saubere Projektumgebung

Tatsächlich ausgeführt:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --no-cache-dir --disable-pip-version-check -e '.[test]'
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m pytest -q
```

Die erste Paketinstallation war wegen des gesperrten Netzwerkzugriffs nicht erfolgreich (`WinError 10013`). Die anschliessende Installation mit genehmigtem Zugriff auf PyPI war erfolgreich. Es wurden nur die lokale Umgebung und temporäre Build-Verzeichnisse verwendet; keine globale Paketinstallation. `pip check`: **No broken requirements found.** QuantStats ist nicht installiert und kein Core-Import benötigt es.

Erster vollständiger pytest-Lauf: **85 passed in 6.69s**. Nach zusätzlichen Prüfungen und der unten beschriebenen Konfigurationshärtung: **93 passed in 6.59s**. Es wurden keine Tests abgeschwächt. Warnungen werden durch `filterwarnings = ["error"]` als Fehler behandelt.

## Prüfung des installierbaren Wheels

Nach Erstellung der transitiven Versionsbindung zusätzlich ausgeführt:

```powershell
.\.venv\Scripts\python.exe -m pip wheel --no-cache-dir --disable-pip-version-check -c requirements.lock --wheel-dir .venv/wheelhouse '.[test]'
.\.venv\Scripts\python.exe -m venv .venv/packaging-check
.\.venv\packaging-check\Scripts\python.exe -m pip install --no-cache-dir --disable-pip-version-check --no-index --find-links .venv/wheelhouse -c requirements.lock 'maturarbeit-engine[test]==0.1.0'
.\.venv\packaging-check\Scripts\python.exe -m pip check
.\.venv\packaging-check\Scripts\python.exe -m pytest -q
```

Wheel-Build und die Installation aus der lokalen Wheel-Ablage waren erfolgreich. Beide virtuellen Umgebungen haben `include-system-site-packages = false`. Das Projekt-Wheel ist `maturarbeit_engine-0.1.0-py3-none-any.whl`; SHA-256 der hier gebauten Datei: `c0f8b8220bb2e66396f0a49d63d6bd3dfc81af3d5b04afd2c678c4c484a5368a`.

`pip check`: **No broken requirements found.** Vollständige Suite gegen die Wheel-Installation: **93 passed in 4.05s**. Damit ist auch die technische Zuordnung der vorgesehenen `src/`-Struktur zum installierten Paket geprüft. Ein Integrationsfall ruft die CLI aus einem anderen Arbeitsverzeichnis auf.

## Kontrollfälle und Abdeckung des Auftrags

| Pflichtgruppe | Tatsächlich geprüfter Fall |
|---|---|
| A – Renditen | 100 → 110 = +10 %; `100, NaN, 110` erzeugt keine gefüllte Rendite |
| B – Buy-and-Hold | Kapital 100, +10 % / −10 % ergibt 100 → 110 → 99 |
| C – Startzeile | Startkapital, nicht beobachtete Start-Rendite, Drawdown 0; Stichproben-Volatilität/Sharpe unabhängig nur aus zwei echten Renditen berechnet |
| D – Drawdown | 100 → 90 → 81 ergibt 0 / −10 % / −19 %, Maximum −19 %; weitere Gewinn-, Erholungs- und konstante Verläufe |
| E – Sharpe | Unabhängige Handformel, konstante und variable RF-Reihen, fehlende/verschobene RF-Perioden, NaN/Inf, doppelte/ungleiche Indizes und Renditen von 110–130 % |
| F – Annualisierung | Explizite Faktoren inkl. Faktoren unter 1, unveränderte geometrische Formel; fehlendes Semantik-Keyword oder `returns` abgelehnt; invalides `m`/Faktoren abgelehnt |
| G – Validierung | Doppelte Markt-Schlüssel, NaN/Inf, leere/nicht numerische/nicht positive Werte, unbekannte Anlage, falsche Währung, fehlende Spalten/Dateien/Parameter, unbekannte Strategieoptionen, doppelte JSON-/CSV-Schlüssel und ungültige Typen |
| H – Reproduzierbarkeit | Zwei Läufe mit identischen Inputs: bytegleiche fachliche CSVs und `data_quality.json`, unterschiedliche Run-IDs; Eingabe-/Ergebnis-Hashes und striktes Manifest-JSON kontrolliert |
| I – Offline | Socket-Verbindungen, DNS und `urllib` in allen Tests des pytest-Prozesses gesperrt; Simulation läuft mit lokalen Daten erfolgreich. Die gesonderte CLI-Unterprozessprüfung nutzt dieselbe Engine, erbt aber nicht die Python-Monkeypatches. |
| J – Zukunftsdaten | Änderung der letzten Bewertung lässt alle früheren Portfoliozeilen unverändert |

Zusätzliche Fälle: Ausrichtung mehrerer Performance-Reihen vor Renditen samt entfernten Terminen; unbenötigte Anlage verändert den Lauf nicht; fehlende Frequenz, unregelmässiges Gitter und unpassendes `m` ergeben keine annualisierten Kennzahlen; fehlende gesamte RF-Dateireferenz ergibt ausdrücklich nicht verfügbare Sharpe; einzelne Rendite und konstante Überschussrendite liefern definierte Verfügbarkeitsstatus; zusätzliche überlappende RF-Intervalle werden abgelehnt; nach dem Lesen geänderte Eingabedatei verhindert den Export; ein manuell manipuliertes `RunConfig` kann die Dateivalidierung nicht umgehen.

Bei der technischen Durchsicht wurden Listen/Objekte als Frequenz sowie sehr grosse JSON-Ganzzahlen als zusätzliche Validierungsfälle ergänzt. Ohne die Härtung könnten diese einen `TypeError` bzw. `OverflowError` statt eines verständlichen `ConfigError` auslösen. Die Implementierung lehnt sie jetzt vor der Simulation ab. Die fachlichen Korrekturen an den bestehenden Funktionen waren bereits durch den Audit nachgewiesen und durch OD-08/09 bzw. den Implementierungsprompt autorisiert; siehe [Implementierungsdokumentation](implementation.md).

## Synthetischer CLI-Lauf und Exportkontrolle

Ausgeführt:

```powershell
.\.venv\Scripts\python.exe -m maturarbeit_engine run --config configs/demo_buy_hold.json
```

Exit-Code **0**, Run-Verzeichnis:
`outputs/runs/synthetic_buy_hold-e0252306f62f4409822e8ff617aa1614/`.

Ein separater Python-Prüfblock hat anschliessend kontrolliert:

- genau die vier geforderten Ergebnisdateien;
- Standard-JSON ohne `NaN`/`Infinity` in Manifest und Qualitätsbericht;
- sämtliche Eingabe-, Ergebnis- und Quellcode-Hashes sowie den aggregierten Code-Hash;
- Git-Commit gegen `git rev-parse HEAD`, `dirty=true` und UTC-Zeitangabe;
- Portfolio 100 / 110 / 99, Drawdowns 0 / 0 / −10 %, nur die Start-Rendite leer;
- alle sieben Kennzahlen gegen unabhängig ausgerechnete Kontrollwerte;
- gewünschte Grenzen 2020-01-01 bis 2020-03-31, effektive Grenzen 2020-01-31 bis 2020-03-31;
- Datenvalidierung bestanden, drei Bewertungen, zwei vollständig ausgerichtete RF-Perioden, keine Qualitätswarnungen.

Ergebnis: **alle Kontrollen bestanden**. Numerische Kontrollwerte und Output-Verträge stehen in [implementation.md](implementation.md).

## Abschlusskontrolle und Grenzen

`git diff` für bestehende Dateien und alle neuen Texte/Quellen wurde geprüft; `git diff --check` meldet keine Fehler. SHA-256 wurde für alle 38 zu Beginn versionierten Dateien mit dem Ausgangsstand verglichen. Nur die autorisierten bestehenden Dateien `.gitignore`, `src/funktionen.py` und das ergänzte KI-Nutzungslog sind verändert. Insbesondere Analyse-/Theorie-Notebooks, `methodik.qmd`, `references.bib`, alle vorhandenen Buchkapitel, AGENTS.md, Entscheidungen und ursprüngliche Audit-Dokumente bleiben bytegleich. Es wurde kein Commit erstellt.

Dies sind technische Tests mit künstlichen Daten. Nicht geprüft sind reale Markt-/Zinsdaten, weitere Strategien, reale Börsenkalender, andere Python-Versionen und Betriebssysteme. Die Versionsbindung fixiert Pakete, aber keine Distributions-Hashes. Tests und Kontrollrechnungen sind keine unabhängige fachliche Abnahme; diese bleibt beim Autor. Es wurde keine neue methodische Entscheidung getroffen und keine Stopp-Bedingung ausgelöst. Der Auftrag endet nach diesem Core.

## Multi-Asset und Rebalancing – Prüfung vom 2026-10-04

Ausgangspunkt: der vom Autor akzeptierte Tag `engine-core-v0.1.0` auf Commit `1a193094b312354c39a72bdf44ef2f6a20573011`. Arbeitsbeginn: sauberer Commit `045bfcb2580e09dc473a571216b5c40bcf2c8397`; der einzige Unterschied zum Tag war der neue Implementierungsprompt. Die bestehende vollständige Suite bestand mit **93 passed in 4.76s**. Beim anschliessenden pytest-Exit trat in der globalen Windows-Temp-Ablage ein Berechtigungsfehler beim Aufräumen von `pytest-current` auf. Die Tests selbst waren erfolgreich (Exit 0). Die weiteren Läufe verwenden frische, vorab auf ihren Workspace-Pfad geprüfte pytest-Ablagen unter `.venv/`; die fremde Temp-Ablage wurde nicht verändert. Diese Läufe endeten ohne die Aufräumstörung.

Die genehmigten Audit-Fehler wurden vor der Härtung regulär über das Core-Paket reproduziert:

- Fehlende B-Rendite bei Positionen A=60/B=40 ergab A=66/B=NaN und Gewicht A=1.
- Zielgewichte 0.5/0.4 bei Kapital 100 ergaben Transaktionssumme −10.

Die neuen Regressionen verlangen für beide Eingaben Fehler. Die zulässigen Drift-/Rebalancing-Formeln wurden erhalten; veränderte Labels, Fehlwerte oder falsche Gewichtssummen werden nicht mehr still weiterverarbeitet.

### Installation und tatsächlich ausgeführte Suite

Keine neuen Runtime-Abhängigkeiten. Weiterhin CPython **3.14.0**, NumPy **2.3.5**, pandas **2.3.3**, pytest **8.4.2**, Windows. Das Paket wurde nach der Versionsänderung lokal als **0.2.0** neu installiert:

```powershell
.\.venv\Scripts\python.exe -m pip install --no-cache-dir --disable-pip-version-check --no-deps -e .
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m pip show maturarbeit-engine
```

Installation erfolgreich; `pip check`: **No broken requirements found.** Netzwerk wurde nur für die bereits fixierten isolierten Build-Werkzeuge verwendet. Die neue Version wurde in der editierbaren lokalen Umgebung geprüft; die oben dokumentierte separate Wheel-Prüfung gilt für den akzeptierten Core 0.1.0 und wurde hier nicht als erneute 0.2.0-Wheel-Prüfung ausgegeben.

Vollständige pytest-Läufe nach Erweiterung:

| Befehl in `.venv`, mit frischer lokaler Testablage | Ergebnis |
|---|---|
| `python -m pytest -q --basetemp=.venv/pytest-rebalance-001` | **161 passed in 18.05s** |
| `python -m pytest -q --basetemp=.venv/pytest-rebalance-002` | **163 passed in 15.83s** |
| `python -m pytest -q --basetemp=.venv/pytest-rebalance-003` | **164 passed in 15.52s** |

Die jeweilige Ablage wurde als absoluter Workspace-Pfad an pytest übergeben. Zwischen den Läufen wurden zwei zusätzliche Fälle für Vereinigungsmenge und mehrere Jahre sowie ein Grenzfall für extrem grosse endliche Zielgewichte ergänzt. Für den letzten Fall wurde die Gewichtsprüfung vor einer möglichen überlaufenden Summe gehärtet. **93 unveränderte Core-Fälle und 71 neue Fälle** bestehen im finalen Lauf. Die ursprünglichen drei Testdateien wurden nicht geändert. Es wurden keine Tests abgeschwächt; Warnungen gelten weiterhin als Fehler.

### Abdeckung der Pflichtgruppen A–N

| Gruppe | Geprüfter Kontrollfall |
|---|---|
| A – Initialisierung | Kapital 100 → Positionen 60/40; Start-Rendite leer; keine initialen Trades; Start direkt am Jahresende ebenfalls ohne erneute Allokation |
| B/C – Drift | Zwei Aktienperioden +10 %, Anleihen 0: 100 → 106 → 112.6; Gewichte driften auf 66/106 und 72.6/112.6; falsches periodisches Zurücksetzen ergäbe 112.36 |
| D – Jahresereignis | Letzter gemeinsamer Termin 2020-12-30 wird verwendet, auch ohne 31.12.; erst Rendite, dann Zielwerte 67.56/45.04 und Trades −5.04/+5.04 |
| E – Folgezustand | Danach −10 %/+10 % auf den tatsächlich neuen Positionen ergibt 110.348, nicht den Verlauf ohne Ausführung |
| F – Kapital | Zielsumme 112.6 = Positionssumme; Transaktionssumme 0; relative Kapitaltoleranz 1e-12; Prüfung auch bei mehreren Jahresereignissen |
| G – Abschluss | Kein Trade am endgültigen 2021-12-31; Gewichte bleiben dort gedriftet |
| H – Zielgewichte | Summe unter/über 1, negative Werte, NaN/Inf, Bool/Text, leeres/falsches Mapping und extreme Zahlen abgelehnt; nah an 1 liegende erlaubte Rundungsabweichung unverändert statt normalisiert; Nullgewichte und drei Anlagen unterstützt |
| I – Kalender | Schnittmenge vor Renditen, fehlendes Datum berichtspflichtig; unbenötigte Anlage beeinflusst Vergleich nicht; Vereinigungsmenge enthält auch Buy-and-Hold-Anlage ausserhalb der Zielgewichte |
| J – Vergleich | Beide Strategien im selben Run, gleiche vollständige Bewertungsliste, eigene Summary-Zeilen, unveränderter Kontext bei vertauschter Strategieausführung; auch Rebalancing allein möglich |
| K – Tabellen/Hashes | Exakte Spalten, stabile Reihenfolge, Datum-/Asset-Raster, Vor-/Nachgewichtssummen, Tradegleichung und sämtliche optionalen Ergebnis-Hashes |
| L – Zukunft | Änderung nur der letzten Aktienbewertung lässt frühere Portfolio-, Gewichts- und Tradezustände unverändert |
| M – Reihenfolge | Umgekehrte CSV-/Metadaten-/Strategie- und Zielgewichtsreihenfolge ergibt bytegleiche fachliche Exporte |
| N – Core | Alle 93 bestehenden Tests und ursprüngliche Demo unverändert erfolgreich; fachliche CSVs und Datenqualität auch vor/nach Erweiterung bytegleich |

Weitere Tests: gleiche RF-Reihe und Handformel je Strategie auf regulärem Monatsgitter; fehlendes RF-Intervall lehnt den gesamten Lauf ab; keine Ereignisse innerhalb eines Jahres mit korrekt leerem Trade-Export; Transaktionswerte 0 an einem gültigen Ereignis dokumentiert; deaktivierte Strategie verlangt keine Anlage im Kontext; unbekannte/missing Assets und falsche Währung einschliesslich Nullgewicht abgelehnt; korrumpierte Gewicht-/Trade-Resultate scheitern an den gemeinsamen Invarianten. Der vorhandene Netzwerk-Guard gilt auch für die neuen pytest-Fälle.

### Beide CLI-Demos und separate Kontrollrechnung

Nach dem letzten Codewechsel ausgeführt, jeweils Exit **0**:

```powershell
.\.venv\Scripts\python.exe -m maturarbeit_engine run --config configs/demo_buy_hold.json
.\.venv\Scripts\python.exe -m maturarbeit_engine run --config configs/demo_rebalance.json
.\.venv\Scripts\python.exe .venv/check_rebalance_exports.py
```

Die letzte Datei ist ein lokaler, ignorierter Kontrollblock dieses Arbeitsauftrags; die dauerhaft versionierbaren Regressionen liegen in `tests/test_rebalance.py`.

- Buy-and-Hold: `outputs/runs/synthetic_buy_hold-81a32b30ed1442b185e762ed5b841f0d/`, weiterhin **100 → 110 → 99**, genau vier Dateien. `portfolio_history.csv`, `summary.csv` und `data_quality.json` sind bytegleich zum Kontrolllauf vor der Erweiterung (`synthetic_buy_hold-36e7c663f29f444bb1ffb17109a89ce7`).
- Neuer Vergleich: `outputs/runs/synthetic_rebalance-7535fb30fd80407f9fa5fe04522e0d26/`, genau sechs Dateien, Portfolioverlauf und Summary mit beiden Strategien, zehn Gewichtszeilen und zwei Trade-Zeilen.
- Kontrollrechnung: **100 → 106 → 112.6 → 110.348 → 116.4284**. Das Jahresereignis erhält **112.6** Kapital; Trades **−5.04/+5.04**, Summe **0** innerhalb der Toleranz. Alle zehn Vor-/Nachgewichte wurden gegen unabhängig ausgerechnete Werte geprüft. Schluss-Drawdown 0, Maximum −2 %; keine Abschlusstransaktion. Buy-and-Hold der neuen Aktienreihe endet bei 119.79 mit Maximum Drawdown −10 %.
- Beide Manifest-/Qualitäts-JSONs wurden strikt ohne NaN/Infinity gelesen; alle Eingabe-, Ergebnis-, einzelnen Quellcode- und aggregierten Code-Hashes wurden nachgerechnet. Git-Commit entspricht dem unveränderten Arbeitsbeginn, `dirty=true`, Engine-Version 0.2.0 und UTC-Zeitangabe sind korrekt. Beide Strategien verwenden identische gewünschte und effektive Grenzen.
- Die unregelmässige Rebalancing-Demo annualisiert ausdrücklich nicht: leere CSV-Zahlen und klarer Status für beide Strategien. Dies verändert die akzeptierte Core-Periodenregel nicht.

### Abschluss und Grenzen der Erweiterung

Die bestehenden Änderungen und neuen Dateien wurden vollständig geprüft; `git diff --check` und ergänzende Textprüfungen sind erfolgreich. SHA-256-Abgleich aller 66 anfänglich versionierten Dateien sichert die geschützten Notebooks, Methodik, Bibliographie, Buchkapitel, `decisions.md`, AGENTS.md, bisherigen Tests und ursprünglichen Demodaten. Ein AST-Abgleich sichert zusätzlich, dass von den bereits vorhandenen Funktionsdefinitionen nur `neue_gewichtung()` und `rebalancing()` geändert wurden; ihre Härtung ist ausdrücklich autorisiert und dokumentiert. Kein Commit und keine neue fachliche Entscheidung.

Die Core-Abnahme durch den Autor bleibt gültig; die fachliche Abnahme dieser neuen Erweiterung steht aus. Geprüft sind künstliche Daten auf Windows/CPython 3.14.0. Andere Plattformen, reale Daten und sämtliche noch ausgeschlossenen Strategien/Adapter sind weiterhin ungeprüft. Keine Trendfolge, BIP-, FX-, Kosten-, Steuer-, Inflations-, Batch- oder Hauptversuchslogik wurde ergänzt. Der Auftrag endet hier.
