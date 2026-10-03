# Engine v1 – ausgeführte Core-, Rebalancing- und Trend-Prüfungen

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
