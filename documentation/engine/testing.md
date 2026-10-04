# Engine v1 – ausgeführte Core-, Rebalancing-, Trend- und Länder-Prüfungen

**Core-Prüfung:** 2026-10-03. **Plattform:** Windows, CPython 3.14.0.
**Versionen:** Engine 0.1.0, NumPy 2.3.5, pandas 2.3.3, pytest 8.4.2; weitere Versionen siehe `requirements.lock`.

**Aktueller Abschluss:** 2026-10-04, Engine 0.4.1: **406 Tests bestanden**, im Checkout und gegen das frisch installierte Wheel. Die älteren Abschnitte dokumentieren die damaligen Prüfläufe; die gezielten Blocker-Fixes und ihre Grenzen stehen im letzten Abschnitt.

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

## Trendfolge – Prüfung vom 2026-10-04

Der Autor hat Core und Rebalancing mit `engine-rebalancing-v0.2.0` auf Commit `37edc79f4211c734423ca89ef3899d1cbc0b81b4` akzeptiert. Dieser Schritt begann sauber auf `10d70e73826dc7e11dbe3eb5bf5770fa833e4ae6`; einzig der neue Trend-Prompt unterschied den Beginn vom akzeptierten Tag. Die vorangehenden Abschnitte sind historische Prüfprotokolle ihrer jeweiligen Aufträge.

### Ausgangspunkt, Refactoring und Umgebung

Die gesamte bisherige Suite wurde vor Änderungen ausgeführt: **164 passed in 23.59s**. Vor dem Refactoring wurde die bestehende `trendfolge()` regulär importiert und geprüft:

- `[1,2,3]`, Fenster 2/3: Signale 0/0 vor definiertem langem SMA und eine frühe Strategierendite 0.
- `[1,NaN,3,4]`, Fenster 2/3: zweite Beobachtung verschwand; Marktrendite von 1 auf 3 wurde als +200 % überbrückt.

Die neuen Helper-/Legacy-Tests verlangen vollständige Beobachtungen, geprüfte Fenster und undefinierte Signale während des Anlaufs. Die Engine verlangt beide SMAs vollständig ab dem effektiven Start. Diese Korrekturen sind durch den dokumentierten Trend-Prompt autorisiert und beziehen sich auf Theorie 3.12 sowie OD-04. Keine andere vorhandene mathematische Funktion wurde für Trend geändert.

Weiterhin Windows, **CPython 3.14.0**, NumPy **2.3.5**, pandas **2.3.3**, pytest **8.4.2**. Keine neuen Runtime-Abhängigkeiten; `requirements.lock` unverändert. Lokale editierbare Neuinstallation und Prüfung tatsächlich ausgeführt:

```powershell
.\.venv\Scripts\python.exe -m pip install --no-cache-dir --disable-pip-version-check --no-deps -e .
.\.venv\Scripts\python.exe -m pip check
```

Ergebnis: Paket **0.3.0** erfolgreich installiert, **No broken requirements found.** pip verwendete ausschliesslich die bereits fixierten isolierten Build-Werkzeuge. Simulation und Testfälle laden keine Daten aus dem Internet. Für 0.3.0 wurde keine separate nicht editierbare Wheel-Installation behauptet; die historische Wheel-Prüfung oben gilt für den Core 0.1.0.

### Tatsächlich ausgeführte vollständige pytest-Läufe

Frische Testablagen wurden als absolute Pfade unter dem Workspace `.venv/` geprüft und verwendet:

| Befehl mit Python aus `.venv` | Ergebnis |
|---|---|
| `python -m pytest -q --basetemp=.venv/pytest-trend-baseline` | **164 passed in 23.59s** |
| `python -m pytest -q --basetemp=.venv/pytest-trend-001` | **236 passed in 45.90s** |
| `python -m pytest -q --basetemp=.venv/pytest-trend-002` | **242 passed in 37.36s** |

Final: **164 unveränderte bisherige Fälle + 78 neue Trend-Fälle**. Nach dem ersten Erweiterungslauf wurden sechs zusätzliche Randfälle ergänzt: effektiver gemeinsamer Start, eigenes Trend-Asset in der Vereinigungsmenge, ausschliesslich Cash, SMA-Vergleich ohne Toleranzzone, fehlende RF-Periode und unvollständige/fehlerhafte Signal-Startposition. Danach wurde die gesamte Suite erneut ausgeführt. Keine bisherigen Tests wurden geändert oder abgeschwächt. Der bestehende Netzwerk-Guard und Warnungen als Fehler gelten weiterhin. Nach dem finalen Lauf wurde kein Engine-Code mehr geändert.

### Pflichtgruppen A–M

| Gruppe | Unabhängig geprüfter Fall |
|---|---|
| A – SMA | Werte 10/10/10/20/30/10/10/30/30, Handmittelwerte für Fenster 2/3; Gleichheit gibt 0, striktes Grössersignal auch ohne Toleranzzone |
| B – Fenster | Null/negative, gleiche/vertauschte Fenster, Bool, Float, Text, fehlende Angaben abgelehnt; gemeinsamer Helper und Konfiguration |
| C – Warm-up | Zwei Vorlaufwerte reichen für langes Fenster 3; fehlender Wert lehnt gesamten Run ab; Start bleibt 100; keine Vorlaufrendite/-Zeile/-Kennzahlen; effektiver Start Februar nutzt Dezember/Januar als Vorlauf |
| D – Rollen | Absichtlich getrennte Reihen; Änderung nur Signalwert verändert Position, lässt Buy-and-Hold-/Rebalancing-Performance identisch; spätere Performanceänderung verändert kein Signal |
| E – Quelle | Explizite Signalspalte und explizite Performance-Quelle funktionieren; fehlende Spalte/Beobachtung und unbekannte Quellen scheitern; kein zeilenweiser Fallback |
| F – Lag | Februar-Signal 1 gilt erst für März; April-Signal 0 gilt erst für Mai; Startsignal steuert erste folgende Periode; Position am Start leer |
| G – Long/Cash | Long verdient +10 %/−20 %; Cash verdient exakt 0 bei −20 %, +100 % und −50 %; kein Short; vollständig definierter reiner Cash-Lauf ebenfalls geprüft |
| H – RF | Änderung nur RF lässt alle Portfolio- und Signaldaten unverändert; nur Sharpe ändert sich; Cash wird nicht verzinst; fehlende RF-Periode ist Fehler |
| I – Export | Exakte Signalspalten, Datums-/Assetzuordnung, sieben Untersuchungszeilen ohne Vorlauf, binäre Signale, vollständig definierte SMAs, verzögerte Position und Hash |
| J – Vergleich | Alle drei Strategien, identische Kalender/Summary-Einträge; Kontext bei vertauschter Ausführung unverändert; Warm-up verlängert andere Portfolios nicht; eigenes Trend-Asset gehört zur Performance-Vereinigung |
| K – Zukunft | Spätere Signal-/Performanceänderungen lassen frühere Signale, Positionen und Vermögen unverändert; neues Signal verändert auch die an demselben Datum endende Rendite nicht |
| L – Fehlwerte | Leere/NaN/Inf/Text in benötigten Vorlauf-/Studienwerten scheitern; Helper lehnt auch Bool, komplexe Werte, doppelte/ungeordnete Indizes ab; kein Auffüllen oder `dropna()` |
| M – Regression | Alle 164 bisherigen Tests sowie beide bisherigen CLI-Demos unverändert; deren sämtliche fachlichen Exporte bytegleich zum Stand vor Trend |

Weitere Kontrollen: Trend allein, deaktivierte unbekannte Anlage ohne Signalspalte, Währung/Asset-Vertrag, vertauschte CSV-/Strategiereihenfolge mit bytegleichen Exports, gemeinsame Kalenderausdünnung vor Marktrenditen mit eigener beobachteter SMA-Historie, Result-Korruption sowie CLI aus anderem Arbeitsverzeichnis. Signale beziehen sich auf die beobachtete Historie der Trend-Anlage; der Positions-Lag bezieht sich auf gemeinsame Performance-Bewertungen. Diese getrennten Zeitsichten werden im Qualitätsbericht dokumentiert.

### Drei CLI-Demos und manuelle Skalarkontrolle

Nach dem letzten Codewechsel tatsächlich ausgeführt, alle Exit **0**:

```powershell
.\.venv\Scripts\python.exe -m maturarbeit_engine run --config configs/demo_buy_hold.json
.\.venv\Scripts\python.exe -m maturarbeit_engine run --config configs/demo_rebalance.json
.\.venv\Scripts\python.exe -m maturarbeit_engine run --config configs/demo_trend.json
.\.venv\Scripts\python.exe .venv/check_trend_exports.py
```

Die letzte Datei ist ein lokaler, ignorierter Kontrollblock dieses Auftrags mit unabhängigen skalaren Formeln und CSV-/JSON-/Hashprüfungen. Dauerhafte Regressionen liegen in `tests/test_trend.py`.

- Buy-and-Hold: `outputs/runs/synthetic_buy_hold-f2ccd5314fd34969bac07e63bab27e3c/`, weiterhin **100 → 110 → 99**, vier Dateien. Beide CSVs und Datenqualität bytegleich zum vor dieser Erweiterung erzeugten Kontrolllauf `synthetic_buy_hold-bfee55e0f2c84f26b5a9cca48538002b`.
- Rebalancing: `outputs/runs/synthetic_rebalance-8367ea25c0754a7681bc754961400b88/`, weiterhin **100 → 106 → 112.6 → 110.348 → 116.4284**, sechs Dateien. Alle CSVs und Datenqualität bytegleich zum Kontrolllauf `synthetic_rebalance-5ee833616a9f43bdbf62b5da1d79c07e`; kein künstliches `signals.csv`.
- Trend-Vergleich: `outputs/runs/synthetic_trend-d5d6bcd322664a9d9f2a6665ba67fe43/`, sieben Dateien. Drei Portfolioverläufe und Summary-Zeilen, sieben Signaldatenzeilen, 14 Rebalancing-Gewichtszeilen und korrekt leere Rebalancing-Trades mit Kopfzeile.

Handkontrolle der sieben SMA-/Signalzeilen:

| Datum | SMA kurz | SMA lang | Signal | Verdiente Position | Trendwert |
|---|---:|---:|---:|---:|---:|
| 2020-01-31 | 10 | 10 | 0 | leer | 100 |
| 2020-02-29 | 15 | 40/3 | 1 | 0 | 100 |
| 2020-03-31 | 25 | 20 | 1 | 1 | 110 |
| 2020-04-30 | 20 | 20 | 0 | 1 | 88 |
| 2020-05-31 | 10 | 50/3 | 0 | 0 | 88 |
| 2020-06-30 | 20 | 50/3 | 1 | 0 | 88 |
| 2020-07-31 | 30 | 70/3 | 1 | 1 | 96.8 |

Nur sechs echte Trendrenditen: **0, 0.1, −0.2, 0, 0, 0.1**. Vorlauf nicht einbezogen. Gesamtrendite **−3.2 %**, Jahresrendite `0.968^2−1 = −6.2976 %`, Jahresvolatilität `sqrt(0.06/5)*sqrt(12) = 37.9473319220 %`, Sharpe mit RF 0.001/0.002 im Wechsel **−0.0475924749**, maximaler Drawdown **−20 %**, Schlussdrawdown **−12 %**. Das unabhängige Kontrollprogramm rechnete auch Kennzahlen/Drawdowns von Buy-and-Hold und Rebalancing vollständig nach; ihre Endwerte sind 77.44 und 86.464.

Alle Manifeste und Qualitätsberichte strikt ohne NaN/Infinity gelesen. Jede Eingabe, jede Ergebnisdatei, alle einzelnen Quellcode-Hashes und der aggregierte Code-Hash wurden nachgerechnet. Engine 0.3.0, UTC-Zeit, unveränderter Git-Commit mit `dirty=true`, aufgelöste Signalquelle/Fenster/Lag, effektiver Zeitraum, Warm-up und identische RF-Perioden sind geprüft. Unterschiedliche Version-/Run-Metadaten sind erwartbar; die bisherigen fachlichen Exporte bleiben bytegleich.

### Abschluss und verbleibende Grenzen

`git diff` einschliesslich neuer Quellen/Tests/Daten geprüft; `git diff --check` und Text-/Link-/JSON-Prüfungen erfolgreich. SHA-256-Abgleich aller **73** zu Beginn versionierten Dateien bestätigt unveränderte geschützte Notebooks, Methodik, Bibliographie, Buchkapitel, `decisions.md`, AGENTS.md, bestehende Tests und beide bisherigen Demo-Datensätze. AST-Vergleich gegenüber dem akzeptierten Tag bestätigt, dass von den vorhandenen Definitionen in `src/funktionen.py` ausschliesslich `trendfolge()` refaktoriert wurde. Neue Helper sind gesondert dokumentiert. Kein Commit erstellt.

Keine neue fachliche Entscheidung nötig. Core-/Rebalancing-Abnahme laut Autor akzeptiert; fachliche Trend-Abnahme offen. Geprüft sind künstliche Daten auf Windows/CPython 3.14.0, keine realen Daten und keine anderen Plattformen. Endgültige SMA-Fenster/Signalreihe bleiben beim Autor. Keine BIP-, Liveadapter-, FX-, verzinste Cash-, Short-, Kosten-, Steuer-, Inflations-, Batch-, Optimierungs- oder Hauptversuchslogik ergänzt. Dieser Auftrag endet nach Trend.

## Länder-Erweiterung vom 2026-10-04 (Engine 0.4.0)

Akzeptierter Ausgangspunkt: `engine-trend-v0.3.0` auf `c101ca558e60228d6e1807a0d192df11d3d5c49f`. Arbeitsbeginn sauber auf `b364109325ad227ad9b519b312374202405453a4`; gegenüber dem Tag ausschliesslich der neue Länder-Prompt. Alle bisherigen Quellen, Tests und Demos entsprachen dem akzeptierten Tag. Vor Implementierung wurden 80 versionierte Datei-Hashes gesichert.

### Tatsächlich ausgeführte Befehle und Ergebnisse

```powershell
.\.venv\Scripts\python.exe -m pytest -q --basetemp=.venv/pytest-country-baseline
.\.venv\Scripts\python.exe -m pytest -q --basetemp=.venv/pytest-country-refactor
.\.venv\Scripts\python.exe -m pytest -q tests/test_country_weighting.py --basetemp=.venv/pytest-country-new
.\.venv\Scripts\python.exe -m pip install --no-cache-dir --disable-pip-version-check --no-deps -e .
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m pytest -q --basetemp=.venv/pytest-country-final
```

| Lauf | Tatsächliches Ergebnis |
|---|---|
| Ausgangspunkt, gesamte bisherige Suite | 242 passed in 30.09s |
| Gemeinsame Portfolio-Zustandsfolge, bisherige Suite | 242 passed in 28.32s |
| Erste vollständige Länder-Testdatei | 99 passed in 27.19s |
| Finale gesamte Suite nach zusätzlichen Kontrollen | **344 passed in 50.68s** |
| Lokale Paketprüfung | **No broken requirements found.** |

Final: **242 unveränderte bisherige Fälle + 102 neue Länderfälle**. Nach dem ersten Länderlauf wurde die Revisionsprüfung um einen tatsächlichen Folgeentscheid ergänzt und zusätzlich ein während des Laufs geänderter Makrosnapshot, voneinander abweichende Länder-/Proxy-Sortierung und doppelte Länder-JSON-Schlüssel geprüft. Die finale Suite wurde danach tatsächlich ausgeführt. Keine bisherigen Tests verändert oder abgeschwächt; bestehender Netzwerk-Guard und Warnungen als Fehler bleiben aktiv. Seit dem finalen Lauf wurden nur Dokumentation und lokale Kontrollhilfen ergänzt, kein Engine-Code oder Test mehr geändert.

Die editierbare lokale Installation wurde von 0.3.0 auf 0.4.0 aktualisiert, Quell-/Paketversion konsistent geprüft. Der erste Versuch scheiterte am gesperrten Netzwerkzugriff für die festgeschriebenen isolierten Build-Werkzeuge (`WinError 10013`); der anschliessende genehmigte Versuch war erfolgreich. Runtime-Abhängigkeiten/Lock unverändert; keine globale Installation. Geprüfte Plattform weiterhin Windows/CPython 3.14.0 mit NumPy 2.3.5, pandas 2.3.3 und pytest 8.4.2. Die Testablagen liegen frisch unter der lokalen `.venv`.

### Pflichtgruppen A–Q

| Gruppe | Unabhängig geprüfter Nachweis |
|---|---|
| A – Makrovertrag | Alle sechs Pflichtspalten; vierstelliges Referenzjahr; vollständige Kennungen; positive endliche Werte; korrekte Datumswerte; ambige vollständige Versionsschlüssel abgelehnt. Identische Dubletten reproduzierbar dedupliziert und gezählt. |
| B – As-of | GDP-2019-Revision 5000 veröffentlicht 2021-02-01, nach Trade 2020-12-30; Änderung auf 0.001 lässt frühere Portfolio-/Gewichts-/Tradezustände exakt identisch. |
| C – Revisionen | Bis 2020-12-14 A=52, ab Veröffentlichungsdatum 2020-12-15 A=50, B=50; später A=5000 erst ab 2021-02-01 zulässig. Gleichheit `available_from == D` eingeschlossen. |
| D – Gemeinsames Jahr | A besitzt bereits GDP 2020 am Jahresentscheid, B nur 2019: beide verwenden 2019; kein Mischen. |
| E – Fehlende Länder | Fehlendes Land, disjunkte Jahre, zu späte Startverfügbarkeit und fehlende konfigurierte Indikator-/Einheitskombination lehnen gesamten Run vor Output ab. Keine Renormierung. |
| F – Start | Effektiver Start, GDP 2018 60/40, Kapital 100 → Positionen 60/40; später verfügbare 2019-Daten ignoriert; Start am Jahresende bleibt initial und tradefrei. |
| G – Jahresfolge | Verdiente Rendite ergibt 72.6/40 vor Trade; Ziel 50/50 ergibt 56.3/56.3; Folgeperiode 50.67/61.93 ergibt unveränderte Summe 112.6. |
| H – Ziele | 60/40 bleibt bis zum Ereignis, dann 50/50 bis einschliesslich Ende. Mehrjährige Variante wechselt am nächsten wirklichen Jahresereignis auf GDP 2020 80/20. Korruption zwischen Ereignissen abgelehnt. Feste Rebalancing-Ziele weiterhin streng konstant. |
| I – Ende | Terminale GDP-2020-Verfügbarkeit erzeugt weder neues Ziel noch Trade/Entscheidung. Zwei Bewertungen liefern nur initiale Entscheidung und korrekt leere Trade-Tabelle mit Kopfzeile. |
| J – Kapital | Vor-/Zielsumme = Vermögen und Transaktionssumme 0 bei jedem der mehrjährigen Ereignisse. Nulltransaktionen werden als echtes jährliches Ereignis dokumentiert. |
| K – Mapping | Unbekannte/fehlende Proxies, fehlende Metadaten, doppelte Proxys, falsches Land/Währung, leeres/einländriges/typfalsches Mapping abgelehnt. Verschiedene Länder-/Asset-Sortierung korrekt. |
| L – Indikator/Einheit | Zusätzliche gültige Kombinationen und unbenötigte Länder verändern keine CSV-Ergebnisse oder Entscheidungen. Fehlende exakte Kombination abgelehnt. |
| M – Zukunft | Spätere Revision, späterer GDP-Referenzwert und späterer Marktwert verändern keine früheren Portfolio-/Gewichts-/Tradezustände (`check_exact=True`). Zusätzlicher tatsächlicher Folgeentscheid zeigt Wirkung erst in dessen folgender Renditeperiode. |
| N – Vergleich | Alle vier Strategien im selben Run, Summary je einmal und identische Kalender; Makro beeinflusst andere Strategien nicht. Eigenes Länderasset bestimmt die Performance-Vereinigung. Länder allein und deaktiviert geprüft; regulärer Monatsfall nutzt dieselbe RF-/Stichproben-Sharpe-/Annualisierungsformel. |
| O – Reihenfolge | Makro-, Markt-, Metadaten-/RF-Zeilen und JSON-Länder-/Strategiereihenfolge vertauscht: alle fachlichen CSVs und Qualitätsberichte bytegleich. Umgekehrte Strategieausführung verändert weder Resultate noch gemeinsamen Kontext. |
| P – Provenienz | Geladene Zeilen, Länder, jede angewandte Entscheidung samt Jahr/Wert/Version/Gewicht, Makro-SHA, aufgelöste Parameter, gemeinsame Output-Hashes und striktes JSON geprüft. Geänderter Makrosnapshot wird vor Export abgelehnt. |
| Q – Regression | Alle 242 bisherigen Tests unverändert grün; alle drei bisherigen CLI-Demos erneut erfolgreich und deren sämtliche fachlichen Exporte bytegleich vor/nach Erweiterung. |

Weitere Kontrollen: mindestens drei Länder mit vollständigem Nenner (60/40/100 → 30/20/50), Pflichtparameter ohne Defaults, lokale Makropfade, doppelte Länder-JSON-Schlüssel, abgelehnte numerisch nicht darstellbare GDP-Gewichte/Summen und Result-Provenienzkorruption. Die GDP-Datei wird vollständig validiert; zusätzliche gültige Zeilen ändern die konfigurierte Auswahl nicht.

### Besonders wichtige historische Revisionskontrolle

`test_future_changes_leave_earlier_portfolios_weights_trades_exact[later_revision]` ändert die am 2021-02-01 veröffentlichte GDP-2019-Revision von A **5000 → 0.001**. Beide Werte unterscheiden sich stark von der vor dem Trade bekannten Revision **50** vom 2020-12-15. Der Trade 2020-12-30 bleibt exakt **−16.3/+16.3**; alle früheren Zustände werden exakt verglichen. Da der kurze Demolauf keine spätere wirkliche GDP-Entscheidung hat, sind sogar sämtliche CSVs und `data_quality.json` bytegleich.

`test_later_revision_applies_only_at_the_next_actual_annual_decision` verlängert bis 2022-06-30 und entfernt nur die synthetischen GDP-2020-Zeilen. Nun darf die Revision erst am wirklichen Folgeentscheid 2021-12-31 angewandt werden. Vermögen bis einschliesslich dieses Entscheiddatums ist exakt identisch; frühere Gewichte/Trades bleiben identisch. Erst die folgende Periode unterscheidet sich: `117.667 × (1 + 5000/5050)` bzw. `117.667 × (1 + 0.001/50.001)`. Damit wird sowohl historische Unverändertheit als auch die spätere zulässige Wirkung der Revision unabhängig kontrolliert.

### Vier CLI-Demos und manuelle Kontrollen

Nach dem finalen Code-/Teststand ausgeführt, jeweils Exit **0**:

```powershell
.\.venv\Scripts\python.exe -m maturarbeit_engine run --config configs/demo_buy_hold.json
.\.venv\Scripts\python.exe -m maturarbeit_engine run --config configs/demo_rebalance.json
.\.venv\Scripts\python.exe -m maturarbeit_engine run --config configs/demo_trend.json
.\.venv\Scripts\python.exe -m maturarbeit_engine run --config configs/demo_country_weighting.json
.\.venv\Scripts\python.exe .venv/check_country_exports.py
```

Die letzte Datei ist eine lokale ignorierte Kontrolle mit unabhängigen skalaren Handformeln, Bytevergleichen und CSV-/JSON-/Hashprüfungen. Dauerhafte Tests liegen in `tests/test_country_weighting.py`. Vor Implementierung wurden die drei bestehenden CLI-Demos als Vergleich tatsächlich ausgeführt.

| Demo | Finaler Run unter `outputs/runs/` | Nachweis |
|---|---|---|
| Buy-and-Hold | `synthetic_buy_hold-3a715bd033a641459520a32b914c825d` | 100 → 110 → 99, vier Dateien, fachliche Exporte bytegleich zu `synthetic_buy_hold-190856cffd2c42f5836093dd68199465` |
| Rebalancing | `synthetic_rebalance-ab87083f6af44d0797b3ab60e5d9f2c4` | 100 → 106 → 112.6 → 110.348 → 116.4284, sechs Dateien, fachliche Exporte bytegleich zu `synthetic_rebalance-43275012cb964712bf89ddafb2da1546` |
| Trend | `synthetic_trend-f7f356f13dfe4d5a8b663548bd199c68` | Trendende 96.8, sieben Dateien, fachliche Exporte bytegleich zu `synthetic_trend-305222cac5c34450997ad8710d9aec11` |
| Länder/Vier-Strategien-Vergleich | `synthetic_country_weighting-5757988362414d40afd5067a9bf4b6dd` | Sieben Dateien, 20 Portfoliozeilen, vier Summary-Zeilen, 20 Gewichtszeilen, vier Tradezeilen, fünf Signalzeilen, zwei GDP-Entscheidungen |

Manuelle GDP-Kontrolle: Start 2020-01-31 aus gemeinsamem GDP-Jahr 2018 mit 60/40. Entscheid 2020-12-30 aus Jahr 2019, A-Revision 50 vom 2020-12-15 und B=50 vom 2020-09-01; 2021-Revision 5000 ausgeschlossen. GDP 2020 80/20 wird am terminalen 2021-12-31 nicht neu angewandt. Drift A 66/106 im Juni und 72.6/112.6 am Jahresende; danach je 56.3 investiert, Transaktionen −16.3/+16.3, Summe 0. Folgeperiode A=50.67/B=61.93, Summe 112.6, tatsächliche Gewichte 45/55 bei weiter geltendem Referenzziel 50/50. Ende A=55.737/B=61.93, Summe **117.667**, Gesamtrendite **17.667 %**, maximaler Drawdown **0**. Kein Start-/Abschluss-Trade. Buy-and-Hold **119.79**, festes Rebalancing **116.4284**, Trend **99**.

Unregelmässiges Gitter mit `period_frequency=null`: Jahresrendite, Volatilität und Sharpe bleiben für alle vier Strategien korrekt leer mit bestehendem Status; vier RF-Intervalle und fünf gemeinsame Performance-Bewertungen geprüft. Der separate reguläre Monats-Test kontrolliert die unveränderte Sharpe-Definition über RF-Überschussrenditen mit `ddof=1` und Jahresfaktor 12.

Alle Manifeste und Qualitätsberichte strikt ohne NaN/Infinity gelesen. Jede Eingabe-/Ergebnisdatei, alle einzelnen Quellcode-Hashes und der aggregierte Code-Hash nachgerechnet. UTC-Zeit, Engine 0.4.0, Schema 1.0, unveränderter Commit `b364109325ad227ad9b519b312374202405453a4` mit `dirty=true`, explizite Länderparameter und Makro-SHA bestätigt. Bisherige fachliche Exporte sind bytegleich, veränderte Versions-/Run-Metadaten erwartbar.

### Abschluss und Grenzen

Gesamten Diff einschliesslich neuer Quellen/Tests/Daten geprüft; `git diff --check`, JSON-/Text-/Linkprüfungen sowie SHA-256-Abgleich der 80 zu Beginn versionierten Dateien durchgeführt. Geschützte Notebooks, Methodik, Bibliographie, Buchkapitel, `decisions.md`, AGENTS.md, alle bisherigen Tests/Demos und `src/funktionen.py` unverändert. Dessen sämtliche 26 Funktionsdefinitionen bleiben erhalten. Buy-and-Hold, Trend, Kennzahlen und Kalenderaufbereitung sind bytegleich; nur feste Rebalancing-Zustandsfolge wurde technisch in den gemeinsamen Helper verschoben. Kein Commit erstellt.

Keine neue fachliche Entscheidung nötig. Core, Rebalancing und Trend laut Autor akzeptiert; fachliche Länder-Abnahme offen. Synthetische Daten auf Windows/CPython 3.14.0 geprüft, andere Plattformen und reale Daten nicht geprüft. Die Engine setzt gelieferte Verfügbarkeitsdaten konsequent um, kann deren historische Richtigkeit aber nicht beweisen. Keine realen Quellen/Länder/Proxies oder Hauptversuchsparameter gewählt. Keine gemischte Kommer-/Faktor-/Marktkapitalisierungsstrategie, Downloads, FX, Kosten, Steuern, Inflation, Batch, Web/API oder Optimierung ergänzt. Der Auftrag endet hier nach der Länder-Erweiterung.

## Gezielte Blocker-Fixes vom 2026-10-04 (Engine 0.4.1)

Arbeitsbeginn sauber auf `70a703c`, akzeptierte fachliche Grundlage `engine-country-weighting-v0.4.0` (`5a06432457c76de925258db16a5bcbb5dc48cdc2`). Vor Änderungen wurden die vollständige Suite und alle vier vorhandenen Demos ausgeführt sowie 93 versionierte Dateien per SHA-256 gesichert. Ursachen, technische Korrekturen und Umfang stehen in [blocker-fixes.md](blocker-fixes.md).

### Vollständige Suite und neue Regressionen

```powershell
.\.venv\Scripts\python.exe -m pytest -q --basetemp=.venv/blocker_fixes/pytest-baseline
.\.venv\Scripts\python.exe -m pytest -q tests/test_blocker_fixes.py --basetemp=.venv/blocker_fixes/pytest-new-first
.\.venv\Scripts\python.exe -m pytest -q --basetemp=.venv/blocker_fixes/pytest-fixes-first
.\.venv\Scripts\python.exe -m pytest -q --basetemp=.venv/blocker_fixes/pytest-final-source
```

| Lauf | Ergebnis |
|---|---|
| Vor Änderungen | **344 passed in 61.05s** |
| Erste neue Datei | 60 passed, 2 failed in 10.83s; neue Fixtures korrigiert |
| Vollständige Suite nach Fixture-Korrektur | **406 passed in 59.43s** |
| Finaler Stand 0.4.1, Checkout | **406 passed in 64.74s** |
| Frisch installiertes Wheel 0.4.1 | **406 passed in 54.11s** |

Die Zwischenfehler waren reproduzierbare Testaufbaufehler: Die Fixed-Rebalancing-Fixture verlor ursprünglich schon bei der Drift die kleine Position, statt erst beim jährlichen Ziel zu unterlaufen; die Quote-Fixture wurde durch Windows-Textschreiben von LF auf CRLF konvertiert. Nur diese neuen Fixtures wurden korrigiert. Alle **344 bisherigen Fälle und Dateien unverändert**, **62 neue Fälle** in `tests/test_blocker_fixes.py`. Warnungen bleiben Fehler und der bestehende Netzwerk-Guard bleibt erhalten. Seit dem finalen Quell-/Wheel-Lauf wurden ausschliesslich Dokumentation und lokale Kontrollhilfen ergänzt.

Neue Pflichtabdeckung: initialer/jährlicher positiver Allokationsunterlauf in beiden Portfoliostrategien, direkter Helper und erlaubte Nullgewichte; beliebige mittlere/letzte Drawdown-Korruption; alle Summary-Zahlen, Spalten, Zeilen, Zuordnungen und Verfügbarkeitsstatus; fehlende/zusätzliche Strategien; falsches Buy-and-Hold-Asset auch bei identischer Rendite; Fixed-Rebalancing-Assets/Ziele und fehlende/zusätzliche/initiale/terminale Trade-Ereignisse auch bei Nulltransaktionen; bestehende Gewichtstoleranz; alle vier normalen Runner. CSV: zu wenige/zu viele Felder in allen vier Eingabeklassen, gequotete Kommas/Zeilenumbrüche und erhaltene benannte Zusatzspalten, RangeIndex, doppelte/unbenannte Header, fehlerhafte Quotes und Leerzeilen.

### Exakte ursprüngliche Audit-Reproduktionen

Die lokale ignorierte Kontrolle `.venv/blocker_fixes/reproduce_audit.py` verwendet die ursprünglichen Audit-Fixtures zusätzlich zur dauerhaften Testdatei. Sie wurde im Checkout und erneut mit dem frisch installierten Wheel ausgeführt, beide Exit 0; jeder erwartete Fehler wurde abgefangen und das Fehlen des Ausgabeordners geprüft.

| Gegenbeispiel | Ergebnis nach Fix in beiden Installationen |
|---|---|
| EB-01: Kapital `1e-200`, A-Gewicht `1e-200`, B-Gewicht `1`, beide Portfolio-Strategien | `Positive target allocation underflowed to zero.` |
| EB-01: ursprünglicher direkter Rebalancing-Helper | Derselbe Fehler |
| EB-02: mittlere/letzte Drawdown-Zeile | Vollständiger returnbasierter Pfad widerspricht dem gespeicherten Verlauf |
| EB-02: Endwert 999 / Sharpe Infinity | Summary widerspricht der gemeinsamen Kennzahlenberechnung |
| EB-02: falscher Verfügbarkeitsstatus | Status widerspricht der erwarteten Summary |
| EB-02: ursprünglicher unvollständiger 20/80-Export | Aktiviertes Strategie-Set unvollständig |
| EB-02: vollständiger Run mit 20/80 unter 60/40-Config | Zielgewichte widersprechen der Konfiguration |
| EB-03: originale `DEMO`-CSV mit Datumsverschiebung, Header 3 / Daten 4 | Feldzahlfehler vor pandas, Zeile 2, erwartet 3 / erhalten 4 |

Insgesamt zehn Varianten der drei ursprünglichen Befundgruppen wurden in jeder Installation abgelehnt. Es wurden keine inkonsistenten Exportdateien veröffentlicht.

### Wheel und frische Installation

```powershell
.\.venv\Scripts\python.exe -m pip install --no-cache-dir --disable-pip-version-check --no-deps -e .
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m pip wheel --no-cache-dir --disable-pip-version-check --no-deps --wheel-dir .venv/blocker_fixes/wheels .
.\.venv\Scripts\python.exe -m venv .venv/blocker_fixes/installed
.\.venv\blocker_fixes\installed\Scripts\python.exe -m pip install --no-cache-dir --disable-pip-version-check -c requirements.lock .venv/blocker_fixes/wheels/maturarbeit_engine-0.4.1-py3-none-any.whl pytest==8.4.2
.\.venv\blocker_fixes\installed\Scripts\python.exe -m pip check
```

Alle Befehle erfolgreich; beide `pip check` melden **No broken requirements found.** Netzwerkzugriff nur für lokale Paket-/Buildwerkzeuginstallation genehmigt, keine globalen Änderungen. Wheel **29363 Bytes**, SHA-256 **`7041c747a1b455f024980098d35486818409b71cd3c212119c5f5655fed862ef`**. Runtime-/Build-Versionen und `requirements.lock` bleiben unverändert.

Die frische Umgebung hat `include-system-site-packages = false`; Version 0.4.1 und Importpfad `.venv/blocker_fixes/installed/Lib/site-packages/maturarbeit_engine/__init__.py` wurden tatsächlich geprüft. Aus dem Arbeitsverzeichnis `.venv/blocker_fixes` wurde die vollständige Suite mit dem frischen Interpreter, absoluten Pfaden zu `tests`/`pyproject.toml` und frischer Ablage `pytest-wheel-final` aufgerufen. Somit wurde das installierte Wheel geprüft. Plattform weiterhin ausschliesslich Windows / CPython 3.14.0, NumPy 2.3.5, pandas 2.3.3, pytest 8.4.2.

### Vier unveränderte Demo-Regressionen

Alle vier ursprünglichen Konfigurationen wurden mit `python -m maturarbeit_engine run --config ...` vor Änderungen und nach den Fixes erneut aufgerufen. Nachher je vier CLI-Runs im Checkout und im Wheel, alle Exit 0. `.venv/blocker_fixes/check_demos.py` kontrolliert jede Ausführung mit einem Socket-/DNS-Guard; die Simulationen benötigen keinen Netzwerkzugriff. Es rechnet die Verläufe, Renditen, Drawdowns, Summary-Kennzahlen, Signale und Länder-Trades unabhängig nach und prüft striktes JSON sowie Eingabe-, Ergebnis- und Quellcodehashes.

| Demo | Vor Fix, Run unter `outputs/runs/` | Nach Fix, Checkout | Nach Fix, Wheel |
|---|---|---|---|
| Buy-and-Hold | `synthetic_buy_hold-1cfc8210e2e9491db548bb8ad02b8756` | `synthetic_buy_hold-99df6c81403b4fcb9a743bc56933803b` | `synthetic_buy_hold-526ce4999bbd4866afcd0f3e8de1a1d9` |
| Rebalancing | `synthetic_rebalance-3989cc1b7b1d454c9029569978531aab` | `synthetic_rebalance-353393fd2c874908a18b79701ac9f61b` | `synthetic_rebalance-cc8f1b43adf542f6a48e7ac7d702b86e` |
| Trend | `synthetic_trend-709c0ef40406487299b956d0830979f0` | `synthetic_trend-3b1a667e6c224bc490e34dd68a28bb84` | `synthetic_trend-f5de877812864a4a821344492643e512` |
| Country-Weighting | `synthetic_country_weighting-a2503582d2324c7a83e71d6eb7a804b0` | `synthetic_country_weighting-758d9d7d0971483eb3206bb1d9c2d81b` | `synthetic_country_weighting-2130128e67b4459ab39495204ae1d36c` |

Alle vorhandenen Ergebnisdateien ausser dem Manifest sind **bytegleich vor/nach Fix und zwischen Checkout/Wheel**, insbesondere jede CSV und `data_quality.json`. Endwerte unverändert **99**, **116.4284**, **96.8**, **117.667**. Die bereits dokumentierten Kontrollrechnungen aller mitausgeführten Strategien stimmen weiterhin. Nur erwartete Manifestangaben wie Version, Codehash, Run-ID, Zeit und Git-Verfügbarkeit unterscheiden sich; die installierten Quellcodehashes stimmen mit dem Checkout überein.

### Abschlusskontrolle und Grenzen

Diff einschliesslich neuer Dateien sowie `git diff --check` geprüft. SHA-256-Vergleich der 93 Ausgangsdateien bestätigt Änderungen ausschliesslich in den 13 freigegebenen bestehenden Dateien; neu sind nur die Regressionsdatei und `blocker-fixes.md`. Geschützte wissenschaftliche Inhalte, AGENTS.md, Entscheidungen, historische Auditdokumente, alte Tests, sämtliche Configs/Demodaten und Lock bleiben bytegleich. Das KI-Log wurde ausschliesslich angehängt; sein bisheriger Inhalt bleibt bytegleich erhalten.

Keine neue fachliche Entscheidung nötig, kein Commit und kein Tag erstellt, kein v1.0-Freeze erklärt. SB-01 bis SB-07 und NB-01 bis NB-03 bleiben ausserhalb dieses Auftrags. Reale Daten, andere Plattformen, historische Wahrheit gelieferter Daten und fachliche Abnahme durch den Autor sind durch diese synthetischen technischen Prüfungen nicht bestätigt. Der Auftrag endet nach EB-01 bis EB-03.
