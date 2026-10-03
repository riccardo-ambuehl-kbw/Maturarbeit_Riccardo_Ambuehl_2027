# Engine v1 Core – ausgeführte Prüfungen

**Datum:** 2026-10-03. **Plattform:** Windows, CPython 3.14.0.
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
