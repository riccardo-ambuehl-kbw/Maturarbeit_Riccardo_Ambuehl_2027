# Codex-Prompt: Engine v1 – CSV-NUL-Fix

**Datum:** 2026-10-04
**Tool:** Codex
**Zweck:** Behebung des letzten offenen ENGINE-BLOCKING-Befunds NEW-EB-01 vor dem Engine-v1.0-Freeze

## Vollständiger Prompt

Behebe ausschliesslich NEW-EB-01 aus:

`documentation/engine/blocker-reaudit.md`

Dies ist der letzte aktuell bekannte technische ENGINE-BLOCKING-Befund.

LIES ZUERST:

- `AGENTS.md`
- `documentation/engine/decisions.md`
- `documentation/engine/final-audit.md`
- `documentation/engine/final-open-issues.md`
- `documentation/engine/blocker-fixes.md`
- `documentation/engine/blocker-reaudit.md`
- `src/data/normalize.py`
- `src/data/validate.py`
- `tests/test_blocker_fixes.py`
- `tests/test_portfolio_state_validation.py`

Aktueller akzeptierter technischer Code-Stand:

Commit:
`2020d5377449e23b1a9e7c36bb0caa1c3a9ebf44`

mit den danach ausschliesslich dokumentierten Audit-Commits.

Aktuelle technische Engine-Version:
`0.4.2`

--------------------------------------------------
PROBLEM
--------------------------------------------------

Der gemeinsame CSV-Lesepfad prüft bereits Header und Feldbreite mit `csv.reader`, bevor pandas aufgerufen wird.

Der Re-Audit hat jedoch gezeigt:

Ein Feld mit einem eingebetteten NUL-Zeichen kann durch den anschliessenden pandas-C-Parser still am NUL-Zeichen gekürzt werden.

Beispiel Rohinhalt:

`1\x00e2`

kann nach pandas zu:

`1`

werden.

Damit validiert die Engine nicht mehr die tatsächlich gelieferten Eingabebytes.

Reproduziert wurde dies für:

- market / performance_value
- assets / currency
- risk_free / period_return
- macro / value

sowohl in gequoteten als auch ungequoteten Feldern.

--------------------------------------------------
VERBINDLICHES VERHALTEN
--------------------------------------------------

CSV-Eingaben mit eingebetteten NUL-Zeichen müssen vor dem pandas-Parsing ausdrücklich abgelehnt werden.

Keine Reparatur.

Kein Abschneiden.

Kein Entfernen des NUL-Zeichens.

Kein Ersetzen.

Keine Interpretation nur des Präfixes.

Die vollständige Eingabedatei wird verworfen.

Der Fehler soll als `DataValidationError` aus dem gemeinsamen CSV-Lesepfad auftreten.

Die Prüfung muss zentral für alle über `read_csv_snapshot()` gelesenen Dateien gelten:

- market
- assets
- risk_free
- macro

Eine neue finanzwirtschaftliche oder methodische Entscheidung ist dafür nicht erforderlich.

--------------------------------------------------
TECHNISCHE UMSETZUNG
--------------------------------------------------

Bevor pandas die Datei erhält:

- prüfe die tatsächlichen gelesenen CSV-Bytes bzw. den vollständig dekodierten Text auf NUL-Inhalt,
- bei vorhandenem NUL-Zeichen: klarer Abbruch.

Bevorzuge die einfachste robuste gemeinsame Lösung.

Beispielsweise ist eine Prüfung des unveränderten Dateiinhalts auf ein NUL-Byte zulässig, sofern dadurch reguläre UTF-8-/UTF-8-BOM-Dateien nicht verändert werden.

Die bisherige CSV-Strukturprüfung muss erhalten bleiben:

- exakte Feldbreite
- doppelte/unbenannte Header abgelehnt
- fehlerhafte Quotes abgelehnt
- korrekt gequotete Kommas erlaubt
- korrekt gequotete Zeilenumbrüche erlaubt
- vollständig benannte Zusatzspalten erlaubt
- kein impliziter pandas-Index

Keine allgemeine Neuentwicklung des CSV-Parsers.

--------------------------------------------------
VERPFLICHTENDE TESTS
--------------------------------------------------

Ergänze dauerhafte Regressionstests für mindestens:

1. market: ungequotetes NUL im Pflichtfeld → Fehler
2. market: gequotetes NUL im Pflichtfeld → Fehler
3. assets: ungequotetes NUL → Fehler
4. assets: gequotetes NUL → Fehler
5. risk_free: ungequotetes NUL → Fehler
6. risk_free: gequotetes NUL → Fehler
7. macro: ungequotetes NUL → Fehler
8. macro: gequotetes NUL → Fehler

Reproduziere zusätzlich exakt den Minimalfall aus `blocker-reaudit.md`:

`performance_value = 1\x00e2`

Dieser vollständige Run muss vor Veröffentlichung scheitern.

Es darf kein erfolgreicher Output-Run entstehen.

Positive Regressionen:

- alle bisherigen korrekten CSV-Fixtures weiterhin gültig
- gequotetes Komma weiterhin gültig
- gequoteter Zeilenumbruch weiterhin gültig
- benannte Zusatzspalte weiterhin gültig
- alle bisherigen 428 Tests weiterhin grün

--------------------------------------------------
REGRESSION EB-01 UND EB-02
--------------------------------------------------

Die Korrektur darf EB-01 und EB-02 nicht berühren oder abschwächen.

Führe die vollständige Suite aus.

Prüfe insbesondere, dass weiterhin bestehen:

- positiver Allokationsunterlauf wird abgelehnt
- vollständiger Drawdownpfad wird geprüft
- Summary/Status werden geprüft
- Strategie-Set wird geprüft
- Buy-and-Hold ist an Config-Asset gebunden
- Fixed Rebalancing ist an Config und Marktportfolio gebunden
- Country Weighting ist an GDP-Entscheidungen und Marktportfolio gebunden

Keine Änderung dieser Logik, sofern nicht technisch zwingend zur Behebung von NEW-EB-01.

--------------------------------------------------
VERSION
--------------------------------------------------

Wenn der Fix umgesetzt ist:

- Paketversion von 0.4.2 auf 0.4.3 erhöhen
- `pyproject.toml`
- `src/__init__.py`

konsistent aktualisieren.

--------------------------------------------------
PAKETIERUNG
--------------------------------------------------

Nach erfolgreichem Fix:

- aktuelles Wheel 0.4.3 bauen
- frische isolierte virtuelle Umgebung
- Wheel installieren
- Importpfad auf `site-packages` prüfen
- Version 0.4.3 prüfen
- `pip check`
- vollständige Suite gegen Wheel ausführen
- NUL-Gegenbeispiele gegen Wheel ausführen

Keine globale Installation.

--------------------------------------------------
VIER DEMOS
--------------------------------------------------

Führe erneut aus:

- configs/demo_buy_hold.json
- configs/demo_rebalance.json
- configs/demo_trend.json
- configs/demo_country_weighting.json

Bekannte Endwerte müssen unverändert bleiben:

- Buy-and-Hold: 99
- Fixed Rebalancing: 116.4284
- Trend: 96.8
- Country Weighting: 117.667

Prüfe, dass fachliche CSVs und `data_quality.json` gegenüber dem korrekten Vor-Fix-Stand unverändert bleiben, abgesehen von erwarteten Manifest-/Versionsinformationen.

--------------------------------------------------
DOKUMENTATION
--------------------------------------------------

Aktualisiere:

- `documentation/engine/blocker-fixes.md`
- `documentation/engine/implementation.md`
- `documentation/engine/testing.md`
- `documentation/ai-usage/ai-usage-log.md`

Dokumentiere:

- NEW-EB-01
- Ursache
- Fix
- acht NUL-Regressionen
- exakten Minimalfall
- vollständige Suite
- Wheel
- vier Demo-Regressionen

NICHT verändern:

- `documentation/engine/final-audit.md`
- `documentation/engine/final-open-issues.md`
- `documentation/engine/blocker-reaudit.md`

Diese bleiben historische Auditnachweise.

--------------------------------------------------
NICHT ERLAUBT
--------------------------------------------------

Nicht bearbeiten:

- SB-01 bis SB-07
- NB-01 bis NB-03
- reale Daten
- Annualisierungsmethodik
- Risk-Free-Auswahl
- SMA-Auswahl
- BIP-Auswahl
- Legacy-Analysehelper
- wissenschaftliche Texte

Geschützt:

- `notebooks/Analyse.ipynb`
- `notebooks/Theorie.ipynb`
- `methodik.qmd`
- `references.bib`
- fertige Buchkapitel
- `documentation/engine/decisions.md`
- alle historischen Auditdokumente

--------------------------------------------------
ABSCHLUSSPRÜFUNG
--------------------------------------------------

Vor Abschluss:

1. vollständige Suite
2. acht NUL-Fälle
3. exakter `1\x00e2`-Minimalfall
4. EB-01-/EB-02-Regressionen
5. vier Demos
6. Wheel 0.4.3
7. frische Installation
8. pip check
9. vollständige Wheel-Suite
10. NUL-Fälle gegen Wheel
11. git diff
12. geschützte Dateien unverändert

Keinen Commit erstellen.

--------------------------------------------------
ABSCHLUSSANTWORT
--------------------------------------------------

Berichte nur:

1. geänderte Dateien,
2. technische Ursache von NEW-EB-01,
3. technische Korrektur,
4. Ergebnis aller NUL-Gegenbeispiele,
5. Gesamtzahl und Ergebnis der Tests,
6. Wheel-Suite,
7. vier Demo-Ergebnisse,
8. ob EB-01/EB-02 unverändert geschützt bleiben,
9. ob neue fachliche Entscheidungen erforderlich waren,
10. ob geschützte Dateien unverändert blieben.

Danach STOPPEN.

Noch keinen Engine-v1.0-Tag setzen.