# Codex-Prompt: Finaler Audit der Backtesting-Engine v1

**Datum:** 2026-10-04
**Tool:** Codex
**Zweck:** Unabhängiger Gesamt-Audit der vollständig implementierten Backtesting-Engine vor dem Engine-v1.0-Freeze

## Vollständiger Prompt

Führe jetzt einen unabhängigen Gesamt-Audit der vollständig implementierten Backtesting-Engine durch.

Dies ist KEIN Implementierungsauftrag.

Der akzeptierte fachliche Ausgangspunkt ist:

`engine-country-weighting-v0.4.0`

auf Commit:

`5a06432457c76de925258db16a5bcbb5dc48cdc2`

Die vorherigen akzeptierten Zwischenstände sind:

- `engine-core-v0.1.0`
- `engine-rebalancing-v0.2.0`
- `engine-trend-v0.3.0`
- `engine-country-weighting-v0.4.0`

Der Zweck dieses Audits besteht ausdrücklich darin, Fehler, Inkonsistenzen, unzureichende Tests, versteckte Annahmen und Reproduzierbarkeitsprobleme zu finden, BEVOR die Engine als v1.0 eingefroren und mit realen Daten verwendet wird.

WICHTIG:

In diesem Arbeitsschritt darfst du KEINE Engine-Funktion korrigieren, KEINE Tests verändern und KEINE fachliche Entscheidung selbst neu treffen.

Wenn du ein Problem findest, dokumentiere es.

--------------------------------------------------
1. ZUERST VOLLSTÄNDIG LESEN
--------------------------------------------------

Lies mindestens:

- `AGENTS.md`
- `documentation/engine/audit.md`
- `documentation/engine/open-decisions.md`
- `documentation/engine/decisions.md`
- `documentation/engine/implementation.md`
- `documentation/engine/testing.md`

Lies ausserdem die vollständige aktuelle Engine:

- `src/funktionen.py`
- `src/data/`
- `src/engine/`
- `src/strategies/`
- `src/analysis/`
- `src/export/`
- `src/__main__.py`
- `src/__init__.py`

Lies:

- `pyproject.toml`
- `requirements.lock`
- alle Dateien unter `configs/`
- die vollständige Test-Suite unter `tests/`

Lies aus:

`notebooks/Theorie.ipynb`

mindestens die relevanten Kapitel 3.2 bis 3.13.

Lies aus:

`notebooks/Analyse.ipynb`

mindestens Kapitel 5.1 bis 5.9.

Lies:

`methodik.qmd`

als vorhandenen methodischen Kontext.

Geschützte wissenschaftliche Dateien dürfen in diesem Auftrag nicht verändert werden.

--------------------------------------------------
2. GIT-AUSGANGSPUNKT PRÜFEN
--------------------------------------------------

Prüfe zuerst den Repository-Zustand.

Der akzeptierte Engine-Stand ist der Tag:

`engine-country-weighting-v0.4.0`

Der aktuelle Branch darf gegenüber diesem Tag nur die Dokumentation des neuen Audit-Auftrags enthalten.

Prüfe insbesondere, ob seit dem akzeptierten Tag bereits unbeabsichtigte Änderungen an:

- `src/`
- `tests/`
- `configs/`
- `pyproject.toml`
- `requirements.lock`
- geschützten wissenschaftlichen Dateien

entstanden sind.

Falls ja, dokumentiere dies als Befund und beginne keine stillschweigende Korrektur.

--------------------------------------------------
3. AUDIT-ZIEL
--------------------------------------------------

Beantworte unabhängig:

Ist die aktuelle Engine technisch und methodisch eindeutig genug, um als allgemeine Backtesting-Engine v1.0 eingefroren zu werden?

Trenne Befunde in drei Klassen:

### ENGINE-BLOCKING

Muss vor `engine-v1.0` korrigiert oder entschieden werden.

Beispiele:

- falsche finanzmathematische Berechnung,
- Look-ahead,
- fehlerhafte Zustandsfolge,
- unzuverlässige Reproduzierbarkeit,
- Ergebnis kann von Reihenfolge oder verstecktem Default abhängen,
- Daten können still erfunden oder falsch ausgerichtet werden,
- getestetes Verhalten widerspricht `decisions.md`,
- Test-Suite bestätigt ein falsches Modell.

### STUDY-BLOCKING

Die allgemeine Engine kann trotzdem v1.0 werden, aber vor dem realen Hauptversuch muss dieser Punkt festgelegt oder geprüft werden.

Beispiele:

- konkrete Wertpapiere,
- realer Zeitraum,
- reale Signalreihe,
- SMA-Fenster,
- Risk-Free-Serie,
- reale BIP-Vintages,
- tatsächliche Datenfrequenz,
- geeignete Total-Return-Reihen,
- reale Datenkalender.

### NON-BLOCKING

Verbesserung, Dokumentationspunkt oder spätere Erweiterung, die Engine v1.0 nicht blockiert.

Klassifiziere jeden Befund eindeutig.

--------------------------------------------------
4. DATENVERTRÄGE PRÜFEN
--------------------------------------------------

Prüfe den vollständigen Datenweg:

lokale Dateien
→ Parsing
→ Validierung
→ gemeinsame Zeitachse
→ Strategie
→ Kennzahlen
→ Exporte

Prüfe Marktdaten:

- Pflichtfelder
- Datumslogik
- `asset_id`
- positive `performance_value`
- optionale `signal_value`
- NaN/Inf
- Duplikate
- Währung
- Metadaten
- zusätzliche unbenötigte Assets
- gemeinsamer Kalender
- Verhalten bei fehlenden gemeinsamen Bewertungen

Prüfe Risk-Free:

- exakte Periodengrenzen
- fehlende Perioden
- zusätzliche Intervalle
- Serienkennung
- keine Nullersetzung
- keine stillen Jahreszinskonvertierungen

Prüfe Makrodaten:

- `period`
- `country`
- `indicator`
- `value`
- `unit`
- `available_from`
- Versions-/Revisionslogik
- doppelte Versionen
- ungeeignete oder spätere Daten
- vollständige Provenienz

Suche insbesondere nach Fällen, in denen pandas-Standardverhalten unbemerkt:

- NaN überspringt,
- Daten auffüllt,
- Reihen ausrichtet,
- Labels verwirft,
- Summen trotz fehlender Werte bildet.

--------------------------------------------------
5. ZEITLICHE LOGIK / LOOK-AHEAD
--------------------------------------------------

Führe einen eigenen Look-ahead-Audit für jede Strategie durch.

### Buy-and-Hold

Prüfe:

- Startbewertung
- erste Rendite
- effektive Grenzen
- keine Zukunftsdaten

### Fixed Rebalancing

Prüfe:

- Rendite zuerst
- Drift danach
- Rebalancing danach
- neue Gewichte erst für die folgende Periode
- Jahresereignisse
- Startallokation
- kein Abschlusstrade

### Trend

Prüfe:

- Warm-up
- `signal_value` vs. `performance_value`
- SMA-Berechnung
- vollständige Fenster
- Signalgleichheit
- Lag exakt eine Periode
- Cash = 0
- kein Look-ahead
- Warm-up nicht Teil der Performance
- Signalzeitachse vs. Performancezeitachse

### Country Weighting

Prüfe:

- initiale As-of-Entscheidung
- `available_from <= decision_date`
- Revisionen
- jüngstes gemeinsames Referenzjahr
- kein Mischen von Länderperioden
- Rendite vor neuer BIP-Entscheidung
- Zielgewicht erst danach
- kein terminales Rebalancing
- spätere Revision verändert keine frühere Entscheidung

Versuche ausdrücklich Gegenbeispiele zu finden, die von bestehenden Tests nicht abgedeckt sind.

--------------------------------------------------
6. GEMEINSAME PORTFOLIOLOGIK
--------------------------------------------------

Prüfe:

- `run_annual_portfolio`
- `neue_gewichtung`
- `rebalancing`
- `validate_target_weights`
- Kapitalerhaltung
- Nullgewichte
- Assetreihenfolge
- mehrere Assets
- dynamische Zielgewichte
- konstante Zielgewichte
- sehr kleine/grosse Werte
- Rendite nahe -100 %
- numerischen Über-/Unterlauf

Prüfe, dass das Refactoring für Country-Weighting das zuvor akzeptierte feste Rebalancing nicht semantisch verändert hat.

--------------------------------------------------
7. MATHEMATISCHE FUNKTIONEN
--------------------------------------------------

Prüfe erneut unabhängig:

- `prozentuale_aenderung`
- `kumulierte_rendite`
- `wachstumsfaktor`
- `geometrisches_mittel`
- `annualisierte_rendite`
- `standardabweichung`
- `annualisierte_volatilitaet`
- `drawdown`
- `maximum_drawdown`
- `sharpe_ratio`
- `korrelationsmatrix`
- `portfolio_risiko`
- `buy_and_hold`
- SMA-Helper
- Legacy-`trendfolge`

Unterscheide:

- mathematisch korrekt,
- korrekt nur unter einem dokumentierten Eingabevertrag,
- noch nicht ausreichend abgesichert.

Vergleiche mit der im Projekt festgelegten Theorie und den autorisierten Entscheidungen.

Wenn geschützter Theorie-Code und korrigierte Engine inzwischen auseinanderliegen, dokumentiere die notwendige spätere Text-/Code-Synchronisierung, ändere das Notebook aber NICHT.

--------------------------------------------------
8. ANNUALISIERUNG UND FREQUENZ
--------------------------------------------------

Prüfe besonders kritisch die aktuelle Logik aus:

- `period_frequency`
- `periods_per_year`
- `check_period_logic`

Beurteile:

- Monatsdaten
- Jahresdaten
- Wochendaten
- Kalendertage
- reale Börsentagesdaten mit Wochenenden/Feiertagen
- unregelmässige Daten
- teilweise Perioden am Rand

Prüfe, ob die aktuelle Engine falsche annualisierte Werte erzeugen kann.

Falls die Engine bei nicht sicher bestimmbarer Periodik Kennzahlen bewusst als nicht verfügbar ausgibt, bewerte dies separat von fehlender Unterstützung realer täglicher Börsendaten.

Klassifiziere eine eventuell noch notwendige Handelskalender-/252-Tage-Regel korrekt als ENGINE-BLOCKING oder STUDY-BLOCKING und begründe dies.

Keine neue Annualisierungsmethode selbst festlegen.

--------------------------------------------------
9. STRATEGIEVERGLEICH
--------------------------------------------------

Prüfe Runs mit mehreren Strategien.

Es muss gelten:

- identischer effektiver Performance-Kalender,
- identisches Startkapital,
- identische Währungsbasis,
- identische Risk-Free-Perioden,
- gleiche Periodengrenzen,
- keine gegenseitige Mutation des Context,
- stabile Ergebnisreihenfolge,
- Strategie A darf Daten von Strategie B nicht beeinflussen, ausser dass alle aktiv benötigten Performance-Assets bewusst den gemeinsamen Vergleichskalender bestimmen.

Prüfe insbesondere, ob das Hinzufügen einer Strategie die Resultate bestehender Strategien aus einem fachlich nicht beabsichtigten Grund verändern kann.

Unterscheide dabei die bewusst vorgesehene gemeinsame Kalender-Schnittmenge von einem Fehler.

--------------------------------------------------
10. KENNZAHLEN UND RESULT CONTRACT
--------------------------------------------------

Prüfe:

`portfolio_history.csv`

- Startzeile
- Renditen
- Drawdown
- Datum
- Strategie

`summary.csv`

- Gesamtrendite
- annualisierte Rendite
- Volatilität
- Sharpe
- Maximum Drawdown
- Status nicht verfügbarer Werte

`weights_history.csv`

- Semantik vor/target/nach
- konstante vs. dynamische Ziele

`trades.csv`

- tatsächliche Ereignisse
- Kapitalerhaltung
- kein Start-/Ende-Fake-Trade

`signals.csv`

- Signal
- Position
- Lag
- SMA
- keine Warm-up-Zeilen

Prüfe, dass alle Result-Invarianten tatsächlich verhindern, dass widersprüchliche Resultate exportiert werden.

--------------------------------------------------
11. REPRODUZIERBARKEIT UND MANIFEST
--------------------------------------------------

Prüfe:

- Config-Hash
- Input-Datei-Hashes
- Makro-Hash
- Code-Hashes
- Git-Commit
- Dirty-State
- Engine-Version
- Python-Version
- Paketversionen
- Ergebnis-Hashes
- UTC-Zeit
- effektive Grenzen
- aufgelöste Konfiguration
- Datenqualitätsbericht

Prüfe, ob ein wissenschaftlicher Run später aus den archivierten Inputs, der Config und dem Engine-Stand ausreichend eindeutig reproduziert werden kann.

Prüfe auch mögliche Änderungen zwischen Einlesen und Export.

Kein eigener Manifest-Selbsthash ist erforderlich.

--------------------------------------------------
12. PAKETIERUNG / SAUBERE INSTALLATION
--------------------------------------------------

Die bisherige separate Wheel-Prüfung stammt aus Engine 0.1.0.

Prüfe deshalb die aktuelle Engine 0.4.0 erneut als installierbares Paket.

Ohne Quellcode zu verändern:

- Wheel bauen.
- In eine frische isolierte virtuelle Umgebung installieren.
- `pip check`.
- gesamte Test-Suite soweit technisch sinnvoll gegen die installierte Engine ausführen.
- mindestens alle vier CLI-Demos gegen diesen Paketstand ausführen oder nachvollziehbar prüfen.

Verwende nur temporäre/ignorierte Arbeitsverzeichnisse.

Keine globalen Paketinstallationen.

Falls lokale Umgebung oder Plattform dies verhindert, dokumentiere exakt was nicht geprüft werden konnte.

Behaupte keine Kompatibilität mit Python-Versionen oder Betriebssystemen, die nicht tatsächlich getestet wurden.

--------------------------------------------------
13. OFFLINE-EIGENSCHAFT
--------------------------------------------------

Prüfe, dass ein eigentlicher Backtest:

- keine Marktdaten herunterlädt,
- keine Makrodaten herunterlädt,
- kein Netzwerk benötigt.

Paketinstallation ist von dieser Regel getrennt.

Suche nach Netzwerkimports oder Codepfaden, die während Simulation unerwartet auf externe Quellen zugreifen könnten.

--------------------------------------------------
14. TEST-SUITE AUDITIEREN
--------------------------------------------------

Nicht nur Tests ausführen.

Lies alle Tests kritisch.

Prüfe:

- testen sie wirklich die fachlichen Regeln?
- vergleichen manche Tests nur zwei Implementierungen derselben möglicherweise falschen Formel?
- gibt es unabhängige Handrechnungen?
- gibt es Tests, die nur den aktuellen Code reproduzieren?
- fehlen wichtige Grenzfälle?
- wurden frühere Tests tatsächlich unverändert erhalten?
- gibt es zu enge Tests, die unbeabsichtigt eine technische Implementierungsform statt des fachlichen Vertrags festschreiben?

Führe bei Bedarf kleine unabhängige temporäre Gegenbeispiele aus.

Keine bestehenden Tests verändern.

--------------------------------------------------
15. VIER DEMOS ERNEUT PRÜFEN
--------------------------------------------------

Führe bzw. prüfe erneut:

- `configs/demo_buy_hold.json`
- `configs/demo_rebalance.json`
- `configs/demo_trend.json`
- `configs/demo_country_weighting.json`

Berechne die zentralen Ergebnisse unabhängig nach.

Prüfe insbesondere die bereits dokumentierten Kontrollwerte.

Ein bestandener Demo-Lauf allein ist kein Beweis der Korrektheit; verwende ihn als zusätzliche End-to-End-Prüfung.

--------------------------------------------------
16. REAL-DATA-READINESS
--------------------------------------------------

Bewerte separat, welche Punkte noch VOR dem realen Hauptversuch geklärt werden müssen.

Mindestens prüfen:

- konkrete Total-Return-Performance-Reihen
- Dividendenbehandlung
- Base Currency
- Datenfrequenz
- Handelstage / Kalender
- `periods_per_year`
- Untersuchungszeitraum
- Startkapital
- Benchmark
- Risk-Free-Serie und deren Konvertierung
- konkrete SMA-Fenster
- konkrete Signalreihe
- Signal-Warm-up
- konkrete Länderproxies
- BIP-Indikator
- BIP-Einheit
- historische BIP-Vintages / echte Veröffentlichungsdaten
- Datenprovenienz und Archivierung

Diese offenen Versuchswerte dürfen NICHT einfach als Engine-Fehler klassifiziert werden.

--------------------------------------------------
17. DOKUMENTATIONS-KONSISTENZ
--------------------------------------------------

Vergleiche:

- Theory
- Analyse
- Methodik
- decisions
- tatsächliche Engine

Suche nach:

- veralteten Codebeispielen,
- widersprüchlichen Formulierungen,
- inzwischen korrigierten Funktionen, die in der Theorie noch anders abgedruckt sind,
- Methodik, die noch RSI oder andere inzwischen nicht implementierte Regeln nennt,
- fehlender Beschreibung wichtiger finaler Engine-Regeln.

Diese Dateien in diesem Audit NICHT verändern.

Klassifiziere die nötigen späteren Textanpassungen separat.

--------------------------------------------------
18. ERSTELLE NUR DOKUMENTATION
--------------------------------------------------

Erstelle:

`documentation/engine/final-audit.md`

Diese Datei soll enthalten:

- geprüfter Tag / Commit,
- gelesene Dateien,
- tatsächlich ausgeführte Prüfungen,
- Test-/Paketierungsresultate,
- Audit je Engine-Komponente,
- unabhängige Gegenrechnungen,
- erkannte Risiken,
- ENGINE-BLOCKING-Befunde,
- STUDY-BLOCKING-Befunde,
- NON-BLOCKING-Befunde,
- Real-Data-Readiness,
- Kriterien für einen späteren Engine-v1.0-Freeze.

Erstelle:

`documentation/engine/final-open-issues.md`

Jeder Befund:

- ID
- Titel
- Klassifikation:
  - ENGINE-BLOCKING
  - STUDY-BLOCKING
  - NON-BLOCKING
- betroffene Dateien/Funktionen
- reproduzierbares Beispiel oder Begründung
- erwartetes Verhalten
- tatsächliches Verhalten
- Empfehlung
- ob eine neue fachliche Entscheidung erforderlich ist

Wenn keine ENGINE-BLOCKING-Probleme gefunden werden, schreibe dies ausdrücklich.

Ergänze:

`documentation/ai-usage/ai-usage-log.md`

für diesen Audit.

--------------------------------------------------
19. NICHT ERLAUBT
--------------------------------------------------

Keine Änderungen an:

- `src/`
- `tests/`
- `configs/`
- `pyproject.toml`
- `requirements.lock`
- `AGENTS.md`
- `documentation/engine/decisions.md`
- `notebooks/Analyse.ipynb`
- `notebooks/Theorie.ipynb`
- `methodik.qmd`
- `references.bib`
- fertigen Buchkapiteln

Keine Fehlerkorrekturen.

Keine neuen Tests committen.

Keine neuen Strategien.

Keine realen Daten.

Keine neuen finanzwirtschaftlichen Definitionen.

Temporäre Prüfdateien müssen in ignorierten/temporären Bereichen liegen und dürfen am Ende nicht als Repository-Änderungen verbleiben.

--------------------------------------------------
20. ABSCHLUSSPRÜFUNG
--------------------------------------------------

Am Ende:

- vollständige relevante Tests tatsächlich ausgeführt,
- Wheel-/Installationsprüfung soweit möglich,
- vier Demos geprüft,
- `git diff` ausgeführt,
- `git status` geprüft,
- geschützte Dateien unverändert,
- ausser den drei erlaubten Dokumentationsdateien keine versionierten Dateien verändert.

--------------------------------------------------
21. ABSCHLUSSANTWORT
--------------------------------------------------

Antworte am Ende nur mit:

1. welche Dokumentationsdateien erstellt/geändert wurden,
2. Ergebnis der vollständigen Tests,
3. Ergebnis der aktuellen Paket-/Wheel-Prüfung,
4. Anzahl ENGINE-BLOCKING-Befunde,
5. Anzahl STUDY-BLOCKING-Befunde,
6. Anzahl NON-BLOCKING-Befunde,
7. die wichtigsten ENGINE-BLOCKING-Befunde,
8. ob alle vier Strategien grundsätzlich auditierbar/reproduzierbar liefen,
9. ob geschützte bzw. Engine-Dateien verändert wurden.

Danach STOPPEN.

Keine Korrekturen implementieren.