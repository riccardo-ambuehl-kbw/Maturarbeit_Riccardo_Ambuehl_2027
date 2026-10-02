# Codex-Prompt: Engine v1 – Kernimplementierung

**Datum:** 2026-10-02
**Tool:** Codex
**Zweck:** Implementierung des ersten vollständigen vertikalen Pfads der Backtesting-Engine

## Vollständiger Prompt

Implementiere jetzt die erste funktionsfähige Kernversion der allgemeinen Backtesting-Engine.

Dies ist der erste Implementierungsschritt nach dem abgeschlossenen Audit und den verbindlichen Entscheidungen.

LIES VOR DER IMPLEMENTIERUNG ZUERST VOLLSTÄNDIG:

1. `AGENTS.md`
2. `documentation/engine/audit.md`
3. `documentation/engine/open-decisions.md`
4. `documentation/engine/decisions.md`
5. `notebooks/Analyse.ipynb`, insbesondere Kapitel 5.3 bis 5.9
6. `notebooks/Theorie.ipynb`, insbesondere die für Datenverarbeitung, Renditen, Kennzahlen und Buy-and-Hold relevanten Teile aus Kapitel 3.2 bis 3.13
7. `src/funktionen.py`
8. `methodik.qmd`
9. `documentation/ai-usage/README.md`

`documentation/engine/decisions.md` ist für OD-01 bis OD-13 verbindlich.

Falls eine Implementierung diesen Entscheidungen widersprechen müsste, NICHT still abweichen. Dokumentiere das Problem und stoppe an dieser fachlichen Grenze.

--------------------------------------------------
ZIEL DIESES ARBEITSSCHRITTS
--------------------------------------------------

Implementiere einen vollständigen, reproduzierbaren vertikalen Pfad:

lokale standardisierte Daten
→ Datenvalidierung
→ Konfiguration
→ Vorbereitung eines SimulationContext
→ Buy-and-Hold
→ gemeinsame Kennzahlen
→ Ergebnisexport
→ Run-Manifest

Noch NICHT implementieren:

- 60/40-/Rebalancing-Strategie als vollständige Strategie,
- Trendfolgestrategie als vollständige Strategie,
- BIP-/Country-Weighting-Strategie,
- reale Yahoo-/FRED-Downloads,
- Batch-System,
- Web/API,
- Hauptversuch der Maturarbeit,
- endgültige Wertpapier-, Zeitraum-, Risk-Free-, SMA- oder BIP-Auswahl.

Diese Punkte folgen in späteren bestätigten Arbeitsschritten.

--------------------------------------------------
1. PYTHON-UMGEBUNG UND ABHÄNGIGKEITEN
--------------------------------------------------

Der Audit hat gezeigt, dass die aktuelle lokale Python-Umgebung inkonsistent ist und noch keine reproduzierbare Projektumgebung existiert.

Erstelle eine möglichst kleine, reproduzierbare Python-Projektkonfiguration.

Bevorzuge einen modernen, einfachen `pyproject.toml`.

Verwende nur Bibliotheken, die für diesen Kern tatsächlich benötigt werden.

Für Engine v1 Core werden voraussichtlich benötigt:

- numpy
- pandas
- pytest

QuantStats soll für die Kernkennzahlen nicht notwendig sein, wenn die in der Theorie definierten Berechnungen mit den bestehenden eigenen Funktionen umgesetzt werden können.

Entferne QuantStats nicht ohne Dokumentation aus historischem Code, aber die neue Kernengine soll nicht unnötig davon abhängig sein.

Dokumentiere unterstützte Python-Versionen.

Prüfe die Installation in einer sauberen lokalen virtuellen Umgebung, soweit dies im verfügbaren Workspace möglich ist.

Keine globalen Paketinstallationen, wenn eine lokale `.venv` verwendet werden kann.

--------------------------------------------------
2. PROJEKTSTRUKTUR
--------------------------------------------------

Implementiere die in Analyse 5.8 geplante Struktur nur soweit sie für diesen Kernpfad benötigt wird.

Mindestens:

src/
├── funktionen.py
├── data/
│   ├── __init__.py
│   ├── normalize.py
│   └── validate.py
├── engine/
│   ├── __init__.py
│   ├── config.py
│   ├── context.py
│   ├── result.py
│   └── simulation.py
├── strategies/
│   ├── __init__.py
│   └── buy_hold.py
├── analysis/
│   ├── __init__.py
│   └── metrics.py
└── export/
    ├── __init__.py
    └── results.py

Zusätzlich:

tests/
configs/
documentation/engine/

Erstelle keine unnötige Plugin-Architektur, Datenbank oder Webschicht.

--------------------------------------------------
3. DATENVERTRAG
--------------------------------------------------

Unterstütze für den Kern zunächst lokale CSV-Daten gemäss Analyse.

Marktdaten mindestens:

date
asset_id
performance_value

Optional:

signal_value

Metadaten mindestens:

asset_id
name
asset_class
country
currency
provider
provider_symbol

Für Buy-and-Hold wird `signal_value` noch nicht benötigt.

Validierung gemäss `decisions.md`:

- Pflichtspalten prüfen.
- Datum sauber parsen.
- `(date, asset_id)` muss eindeutig sein.
- `performance_value` muss numerisch, endlich und für die verwendeten Preis-/Indexfunktionen positiv sein.
- NaN in einer vorhandenen Beobachtung ist ein Fehler.
- Keine automatische Interpolation.
- Kein automatisches Forward-Fill.
- Keine stillen Nullrenditen.
- `asset_id` muss in den Metadaten existieren.
- Währung muss zur konfigurierten Basiswährung passen.
- Mehrere benötigte Reihen werden vor Renditeberechnung auf gemeinsame tatsächlich vorhandene Bewertungszeitpunkte ausgerichtet.
- Entfernte Zeitpunkte werden im Datenqualitätsbericht dokumentiert.

Für den ersten Buy-and-Hold-Slice genügt ein Asset. Die Datenstruktur soll trotzdem nicht auf genau ein Asset hardcodiert sein.

--------------------------------------------------
4. KONFIGURATION
--------------------------------------------------

Implementiere eine validierte JSON-Konfiguration.

Sie muss für den Kern mindestens enthalten:

- schema_version
- run_name oder vergleichbare Run-Bezeichnung
- start
- end
- start_capital
- base_currency
- periods_per_year
- Datenreferenzen
- aktivierte Strategie
- Buy-and-Hold-Asset

Keine stillen fachlichen Defaults für fehlende Pflichtparameter.

Unbekannte oder nicht unterstützte Strategieoptionen sollen nicht kommentarlos ignoriert werden.

Erstelle unter `configs/` eine vollständig künstliche Demo-Konfiguration.

Die Demo-Werte sind ausdrücklich keine Parameter der späteren Maturarbeits-Untersuchung.

--------------------------------------------------
5. START UND PERIODENLOGIK
--------------------------------------------------

OD-02 ist verbindlich.

Der Portfolioverlauf beginnt mit einer expliziten Startzeile:

portfolio_value = start_capital
period_return = fehlend / nicht beobachtet
drawdown = 0

Diese Startzeile darf NICHT als beobachtete Nullrendite in statistische Kennzahlen eingehen.

Effektiver Start:

erster gültiger Bewertungszeitpunkt am oder nach dem konfigurierten Start.

Effektives Ende:

letzter gültiger Bewertungszeitpunkt am oder vor dem konfigurierten Ende.

Speichere gewünschte und effektive Grenzen im Manifest.

Bei Buy-and-Hold wird ab der Startbewertung Gewicht 1 in der konfigurierten Anlage gehalten.

--------------------------------------------------
6. BESTEHENDE FUNKTIONEN
--------------------------------------------------

`src/funktionen.py` bleibt fachlicher Ausgangspunkt.

Prüfe und verwende bestehende Funktionen soweit sinnvoll.

Die Entscheidungen aus `decisions.md` erlauben ausdrücklich Korrekturen an nachgewiesenen Fehlern.

Insbesondere:

### prozentuale_aenderung()

Es darf bei fehlenden Werten kein implizites Auffüllen stattfinden.

Passe die Funktion transparent so an, dass fehlende Werte nicht still zu Renditen gemacht werden.

Die Datenvalidierung soll fehlende Marktwerte bereits vorher ablehnen.

### Sharpe Ratio

Implementiere exakt die in OD-08 festgelegte Formel:

mean(r - rf) / std(r - rf, ddof=1) * sqrt(periods_per_year)

Keine QuantStats-Heuristik für die Interpretation der Eingabedaten.

Anlage und Risk-Free müssen exakt ausgerichtet, vollständig und endlich sein.

Wenn für diesen Kern noch keine reale Risk-Free-Datei verwendet wird, teste die Funktion mit einer synthetischen passende Reihe.

### Drawdown

OD-09 ist verbindlich.

Der Startwert ist High-Water-Mark.

Ein Verlust in der ersten Periode muss sofort als negativer Drawdown erscheinen.

Passe die vorhandenen Funktionen transparent an oder verwende einen minimalen Wrapper, aber vermeide zwei voneinander unabhängige Drawdown-Definitionen.

### Rendite vs. Wachstumsfaktor

Verhindere durch klare Schnittstellen und Tests, dass `annualisierte_rendite()` versehentlich einfache Renditen statt Wachstumsfaktoren erhält.

Keine stillen Typ-/Semantikkonvertierungen.

Dokumentiere jede Änderung an `src/funktionen.py` in der technischen Implementierungsdokumentation.

--------------------------------------------------
7. BUY-AND-HOLD
--------------------------------------------------

Implementiere Buy-and-Hold als erste Strategie.

Anforderungen:

- genau die konfigurierte Anlage verwenden,
- Startgewicht 1,
- keine externen Cashflows,
- Total-Return-Behandlung liegt bereits in `performance_value`,
- Startkapital sauber einfügen,
- Renditen aus den validierten Werten berechnen,
- Vermögensverlauf berechnen,
- Drawdown berechnen,
- standardisiertes StrategyResult zurückgeben.

Die Strategie darf keine Daten aus dem Internet laden.

Sie darf Daten nicht selbst nach eigenem Ermessen auffüllen oder bereinigen.

--------------------------------------------------
8. GEMEINSAME RESULT-STRUKTUR
--------------------------------------------------

Implementiere mindestens:

`portfolio_history`

mit:

date
strategy
portfolio_value
period_return
drawdown

Die Startzeile enthält:

period_return = leer
drawdown = 0

Implementiere eine gemeinsame Result-Struktur entsprechend Analyse 5.8.3.

Gewichte, Trades oder Signale können für diesen ersten Slice leer bzw. optional sein.

--------------------------------------------------
9. KENNZAHLEN
--------------------------------------------------

Implementiere den Kern der gemeinsamen Auswertung:

- start_value
- end_value
- total_return
- annualized_return
- annualized_volatility
- sharpe_ratio
- max_drawdown

Verwende soweit fachlich passend die bestehenden Funktionen aus `src/funktionen.py`.

`periods_per_year` stammt explizit aus der Konfiguration.

Keine automatische Frequenzannahme.

Falls für eine Kennzahl notwendige Daten fehlen, nicht still 0 ausgeben.

Verwende einen klaren `null`-/nicht-verfügbar-Zustand oder einen nachvollziehbaren Fehler entsprechend der Art des Problems.

--------------------------------------------------
10. RISK-FREE IM KERN
--------------------------------------------------

Die allgemeine Engine soll bereits einen normalisierten Risk-Free-Input für die Sharpe Ratio unterstützen.

Verwende dafür synthetische Testdaten.

Format der verarbeiteten Risk-Free-Daten so gestalten, dass pro Portfolio-Periode eine eindeutig zugeordnete Periodenrendite existiert.

Die Umrechnung eines FRED-Jahreszinses wird in diesem Arbeitsschritt NICHT implementiert.

Kein Forward-Fill und keine Nullersetzung fehlender Risk-Free-Perioden.

--------------------------------------------------
11. EXPORT UND REPRODUZIERBARKEIT
--------------------------------------------------

Erzeuge für einen erfolgreichen Run mindestens:

outputs/runs/<run_id>/
├── portfolio_history.csv
├── summary.csv
├── run_manifest.json
└── data_quality.json

oder eine funktional gleichwertige deterministische Struktur.

`run_manifest.json` soll mindestens enthalten:

- Engine-/Schema-Version
- Run-ID
- UTC-Zeitpunkt
- vollständig aufgelöste Konfiguration
- gewünschter und effektiver Zeitraum
- base_currency
- periods_per_year
- verwendete Eingabedateien
- SHA-256 der relevanten Eingabedateien
- Git-Commit
- Dirty-Status
- Python-Version
- relevante Paketversionen
- relevante Ergebnisdateien und deren SHA-256

Keine Secrets speichern.

JSON muss standardkonform sein.
Kein NaN oder Infinity in JSON.

Wenn eine Kennzahl nicht definiert ist, verwende `null` plus bei Bedarf einen Status oder Hinweis.

Unterschiedliche Run-ID und Zeitstempel dürfen bei identischen fachlichen Inputs variieren.
Die fachlichen Resultate müssen bei identischen Daten, Config und Code reproduzierbar sein.

--------------------------------------------------
12. DATENQUALITÄTSBERICHT
--------------------------------------------------

Erzeuge einen maschinenlesbaren `data_quality.json`.

Mindestens dokumentieren:

- geladene Assets,
- ursprünglicher Zeitraum je benötigter Reihe,
- effektiver Zeitraum,
- Beobachtungszahlen,
- entfernte nicht gemeinsame Bewertungszeitpunkte,
- erkannte Warnungen,
- Validierungsstatus.

Ein erfolgreicher Run darf keine unbemerkten NaN-/Inf-Werte enthalten.

--------------------------------------------------
13. TESTS
--------------------------------------------------

Richte eine echte pytest-Test-Suite ein.

Mindestens folgende Tests müssen vorhanden und tatsächlich ausgeführt werden:

A. Renditen
- 100 -> 110 ergibt +10 %.
- Ein NaN darf nicht zu einer impliziten Nullrendite werden.

B. Buy-and-Hold
- Startkapital 100 und Renditen +10 %, -10 %:
  erwarteter Verlauf 100 -> 110 -> 99.

C. Startzeile
- Startwert vorhanden.
- `period_return` der Startzeile ist nicht 0, sondern nicht beobachtet.
- Startzeile fliesst nicht in Volatilität/Sharpe ein.

D. Drawdown
- Start 100 -> 90 -> 81:
  Drawdowns -10 % und -19 %.
- Maximum Drawdown = -19 %.

E. Sharpe
- Handrechenbares Beispiel gegen die definierte Formel.
- Variable Risk-Free-Reihe.
- Fehlende Risk-Free-Periode muss Fehler bzw. nicht zulässigen Lauf erzeugen.
- Renditen >100 % dürfen nicht als Preisreihe uminterpretiert werden.

F. Annualisierung
- Wachstumsfaktoren verwenden.
- Versehentliche Übergabe falscher Semantik muss verhindert bzw. klar abgelehnt werden.

G. Datenvalidierung
- doppelte `(date, asset_id)` ablehnen.
- NaN ablehnen.
- Inf ablehnen.
- falsche Währung ablehnen.
- unbekannte asset_id ablehnen.
- ungültige oder fehlende Konfigurationsparameter ablehnen.

H. Reproduzierbarkeit
- derselbe synthetische Datenstand + dieselbe Config erzeugt dieselben fachlichen CSV-Ergebnisse.
- Manifest-Zeitstempel und Run-ID dürfen abweichen.

I. Kein Netzwerk im Backtest
- Kernsimulation muss vollständig mit lokalen Daten ausführbar sein.
- Tests dürfen keinen Marktdownload benötigen.

J. Zukunftsdaten
- Eine Änderung eines Datenpunkts nach einer bereits berechneten früheren Periode darf keine früheren Buy-and-Hold-Ergebnisse verändern.

Weitere sinnvolle Randtests darfst du selbst ergänzen.

Tests dürfen nicht abgeschwächt werden, nur damit der Code grün wird.

--------------------------------------------------
14. SYNTHETISCHE DEMODATEN
--------------------------------------------------

Erstelle einen kleinen vollständig künstlichen Datensatz für den End-to-End-Test.

Keine realen Marktwerte verwenden.

Er muss klein genug sein, dass zentrale Ergebnisse manuell nachvollzogen werden können.

Er soll über die normale Engine-Schnittstelle laufen und dieselben Exporte erzeugen wie später reale Daten.

--------------------------------------------------
15. CLI / AUFRUF
--------------------------------------------------

Stelle einen einfachen lokalen Aufruf bereit.

Bevorzugtes Ziel:

python -m <paketname> run --config <config>

oder eine ähnlich einfache, dokumentierte Variante.

Der konkrete Paketname ist eine technische Entscheidung.

Der CLI-Aufruf muss denselben Engine-Code verwenden wie direkte Python-Aufrufe.
Keine zweite Berechnungslogik.

Für diesen Arbeitsschritt genügt ein einzelner Run.
Noch kein Batch-System implementieren.

--------------------------------------------------
16. DOKUMENTATION
--------------------------------------------------

Erstelle bzw. aktualisiere:

`documentation/engine/implementation.md`

Dokumentiere dort:

- tatsächlich implementierte Struktur,
- technische Entscheidungen,
- Änderungen an bestehenden Funktionen,
- Unterschiede zwischen ursprünglichem Code und Engine-Integration,
- Installationsweg,
- Startbefehl,
- Demo-Lauf,
- bekannte Grenzen,
- noch NICHT implementierte Strategien und Funktionen.

Erstelle:

`documentation/engine/testing.md`

Dokumentiere:

- tatsächlich ausgeführte Testbefehle,
- Python-Version,
- Testergebnis,
- Anzahl Tests,
- wichtige synthetische Kontrollfälle,
- gegebenenfalls behobene Fehler,
- verbleibende Einschränkungen.

Aktualisiere am Ende:

`documentation/ai-usage/ai-usage-log.md`

Dokumentiere diesen Codex-Arbeitsschritt sachlich gemäss bestehendem Schema.

Keine Aussagen wie „vollständig korrekt“, wenn nur Tests bestanden wurden.
Unterscheide technische Tests von fachlicher Abnahme durch den Autor.

--------------------------------------------------
17. SELBSTSTÄNDIGES ARBEITEN
--------------------------------------------------

Innerhalb dieses bestätigten Auftrags darfst du selbstständig iterieren:

implementieren
→ Tests ausführen
→ Fehler analysieren
→ korrigieren
→ Tests erneut ausführen

Du musst nicht nach jedem technischen Fehler stoppen.

STOPPE aber sofort, wenn:

- eine neue finanzwirtschaftliche/methodische Entscheidung nötig wäre,
- `decisions.md` geändert werden müsste,
- eine geschützte Inhaltsdatei verändert werden müsste,
- die vorhandene Theorie nur durch eine neue fachliche Definition erfüllt werden könnte,
- eine bislang nicht genehmigte Datenauffüllung oder Annahme nötig wäre.

In diesem Fall dokumentiere das Problem präzise und ändere die Methodik nicht selbst.

--------------------------------------------------
18. VERBOTENE ÄNDERUNGEN
--------------------------------------------------

In diesem Arbeitsschritt NICHT inhaltlich verändern:

- `notebooks/Analyse.ipynb`
- `notebooks/Theorie.ipynb`
- `methodik.qmd`
- `references.bib`
- andere fertige Kapitel

NICHT implementieren:

- reale Marktdatenbeschaffung,
- Yahoo-/FRED-Liveadapter,
- 60/40-Strategie,
- Trendfolge,
- BIP-Strategie,
- Batch-Runner,
- Webserver/API,
- Parameteroptimierung,
- Hauptuntersuchung.

--------------------------------------------------
19. ABSCHLUSSPRÜFUNG
--------------------------------------------------

Vor Abschluss:

1. komplette relevante Test-Suite ausführen,
2. synthetischen End-to-End-Demo-Lauf ausführen,
3. Exporte prüfen,
4. Manifest und Hashes prüfen,
5. `git diff` prüfen,
6. sicherstellen, dass geschützte Inhalte unverändert sind,
7. technische Dokumentation aktualisieren,
8. KI-Nutzungslog aktualisieren.

Keine Commits erstellen, ausser dies wurde ausdrücklich separat angefordert.

--------------------------------------------------
20. ABSCHLUSSANTWORT
--------------------------------------------------

Berichte am Ende kompakt:

1. welche Dateien erstellt/geändert wurden,
2. welche bestehenden Funktionen geändert wurden und warum,
3. wie die Engine gestartet wird,
4. welche Tests tatsächlich ausgeführt wurden und deren Ergebnis,
5. ob der synthetische End-to-End-Lauf erfolgreich war,
6. welche Outputs erzeugt wurden,
7. welche Einschränkungen bestehen,
8. ob neue fachliche Entscheidungen nötig wurden,
9. ob geschützte Dateien unverändert blieben.

Danach STOPPEN.

Noch nicht mit 60/40, Trendfolge oder BIP fortfahren.