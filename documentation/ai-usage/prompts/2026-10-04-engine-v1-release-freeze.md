# Codex-Prompt: Engine v1.0 – Release und technischer Freeze

**Datum:** 2026-10-04
**Tool:** Codex
**Zweck:** Technischer Release der vollständig auditierten Backtesting-Engine als Version 1.0.0

## Vollständiger Prompt

Bereite den finalen technischen Release der auditierten Backtesting-Engine als Version 1.0.0 vor.

Dies ist KEIN neuer Implementierungsauftrag.

Ausgangspunkt:

Branch:
`engine-v1`

Aktueller Freeze-Re-Audit-Commit:
`27470204e3805a18a11f6630813b982b3174ea0d`

Aktuell geprüfte Engine-Version:
`0.4.3`

Der finale Re-Audit in:

`documentation/engine/freeze-reaudit.md`

enthält das Urteil:

`ENGINE-V1.0-FREEZE TECHNICALLY READY`

Die technische Engine darf deshalb nun als v1.0.0 eingefroren werden.

--------------------------------------------------
1. VORHER LESEN
--------------------------------------------------

Lies vollständig:

- `AGENTS.md`
- `documentation/engine/decisions.md`
- `documentation/engine/final-audit.md`
- `documentation/engine/final-open-issues.md`
- `documentation/engine/blocker-fixes.md`
- `documentation/engine/blocker-reaudit.md`
- `documentation/engine/freeze-reaudit.md`
- `documentation/engine/implementation.md`
- `documentation/engine/testing.md`
- `pyproject.toml`
- `src/__init__.py`

Prüfe zusätzlich den aktuellen Git-Stand.

--------------------------------------------------
2. WICHTIGSTE REGEL
--------------------------------------------------

Keine Engine-Logik mehr verändern.

Insbesondere KEINE Änderungen an:

- Finanzformeln
- Datenvalidierung
- Kalenderlogik
- Portfoliozustandsfolge
- Buy-and-Hold
- Rebalancing
- Trend
- Country Weighting
- Kennzahlen
- Export
- CSV-Parser
- Tests
- Configs
- Demodaten

Der Release besteht ausschliesslich aus:

- Versionswechsel 0.4.3 → 1.0.0
- finaler Release-/Freeze-Dokumentation
- nötiger Aktualisierung technischer Standangaben
- vollständiger erneuter Regression/Paketprüfung

Wenn eine Engine-Codeänderung nötig erscheint:
STOPPEN und berichten.

--------------------------------------------------
3. VERSION
--------------------------------------------------

Ändere konsistent:

`pyproject.toml`

von:

`version = "0.4.3"`

auf:

`version = "1.0.0"`

und:

`src/__init__.py`

von:

`__version__ = "0.4.3"`

auf:

`__version__ = "1.0.0"`

Keine weitere Python-Datei verändern.

--------------------------------------------------
4. RELEASE-DOKUMENT
--------------------------------------------------

Erstelle:

`documentation/engine/release-v1.0.md`

Dokumentiere mindestens:

- Datum
- Release-Version 1.0.0
- Ausgangscommit des erfolgreichen Freeze-Re-Audits
- Bedeutung des technischen Freeze
- implementierte Strategien
- zentrale fachliche Verträge
- Datenverträge
- Resultate/Outputs
- Reproduzierbarkeit
- final geschlossene Engine-Blocker
- aktuelle Testzahl
- Paket-/Wheel-Prüfung
- vier Demo-Kontrollwerte
- bekannte technische Grenzen
- STUDY-BLOCKING-Punkte, die vor realen Hauptläufen weiterhin offen bleiben
- NON-BLOCKING-Punkte
- Hinweis, dass Engine v1.0 kein Abschluss der Maturarbeit und keine Freigabe realer Daten bedeutet

Erfinde keine neuen fachlichen Entscheidungen.

--------------------------------------------------
5. FREEZE-GRENZE
--------------------------------------------------

Dokumentiere klar:

Engine v1.0 friert insbesondere ein:

- OD-01 bis OD-13
- gemeinsamen Markt-/Performance-Datenvertrag
- expliziten Risk-Free-Periodenvertrag
- historischen Makro-/available_from-Vertrag
- Buy-and-Hold
- jährliches Fixed Rebalancing
- SMA Long/Cash mit Lag 1
- reine GDP-Country-Weighting-Strategie
- gemeinsame Performance-Zeitachse
- Startzeilen-/Drawdown-Semantik
- Sharpe-Definition
- Portfoliozustandsfolge
- Result-/Exportvertrag
- Input-/Code-/Result-Provenienz
- strikte CSV-Struktur-/NUL-Prüfung

Nach diesem Release dürfen methodisch relevante Änderungen nur über eine neue Engine-Version erfolgen.

--------------------------------------------------
6. NOCH OFFEN VOR DER REALEN STUDIE
--------------------------------------------------

Übernimm die bereits dokumentierten STUDY-BLOCKING-Punkte sinngemäss, ohne sie neu zu lösen:

- reale Performance-/Total-Return-Reihen und Proxies
- Währungsbasis
- Untersuchungszeitraum
- Startkapital
- tatsächliche Frequenz und Annualisierungsbasis
- Risk-Free-Serie und deren vorgelagerte Konvertierung
- konkrete SMA-Fenster und Signalreihe
- Warm-up
- Länder-/Proxy-Auswahl
- GDP-Indikator/-Einheit
- historische GDP-Vintages / Veröffentlichungsdaten
- wissenschaftliches Daten-/Run-Archiv
- Synchronisierung der wissenschaftlichen Texte mit den akzeptierten Regeln

Diese Punkte blockieren reale Hauptläufe, aber nicht den technischen Engine-v1.0-Release.

--------------------------------------------------
7. IMPLEMENTATION / TESTING DOKUMENTATION
--------------------------------------------------

Aktualisiere `documentation/engine/implementation.md` nur mit einer kurzen aktuellen Standnotiz:

- Engine v1.0 technisch eingefroren
- Release-Dokument verlinken
- keine neue Methodik
- vorherige historische Abschnitte nicht umschreiben

Aktualisiere `documentation/engine/testing.md` nur mit dem finalen Release-Testnachweis.

Historische Testprotokolle erhalten.

--------------------------------------------------
8. KI-LOG
--------------------------------------------------

Ergänze:

`documentation/ai-usage/ai-usage-log.md`

append-only gemäss bestehendem Schema.

--------------------------------------------------
9. VOLLSTÄNDIGE TESTS
--------------------------------------------------

Nach dem reinen Versions-/Dokumentationswechsel:

Führe die vollständige unveränderte Suite aus.

Erwartet:

441 Tests.

Keine Tests verändern.

--------------------------------------------------
10. VIER DEMOS
--------------------------------------------------

Führe erneut aus:

- `configs/demo_buy_hold.json`
- `configs/demo_rebalance.json`
- `configs/demo_trend.json`
- `configs/demo_country_weighting.json`

Bekannte Endwerte:

- Buy-and-Hold: 99
- Fixed Rebalancing: 116.4284
- Trend: 96.8
- Country Weighting: 117.667

Fachliche CSVs und `data_quality.json` müssen gegenüber dem akzeptierten 0.4.3-Stand unverändert bleiben.

Manifest darf sich erwartungsgemäss ändern wegen:

- engine_version = 1.0.0
- Codehash
- Run-ID
- Timestamp
- Git-/Dirty-Provenienz

--------------------------------------------------
11. WHEEL 1.0.0
--------------------------------------------------

Baue:

`maturarbeit_engine-1.0.0-py3-none-any.whl`

Dann frische isolierte virtuelle Umgebung:

- kein Editable-Install
- Wheel installieren
- Import aus `site-packages`
- `__version__ == "1.0.0"`
- Distributionsversion 1.0.0
- `pip check`
- vollständige 441-Test-Suite gegen Wheel
- vier CLI-Demos gegen Wheel

Keine globale Installation.

--------------------------------------------------
12. OFFLINE
--------------------------------------------------

Prüfe erneut, dass die vier Backtests selbst keinen Netzwerkzugriff benötigen.

Paketbau/-installation ist davon getrennt.

--------------------------------------------------
13. SCHREIBGRENZE
--------------------------------------------------

Erlaubte bestehende Änderungen:

- `pyproject.toml`
- `src/__init__.py`
- `documentation/engine/implementation.md`
- `documentation/engine/testing.md`
- `documentation/ai-usage/ai-usage-log.md`

Erlaubte neue Datei:

- `documentation/engine/release-v1.0.md`

NICHT verändern:

- alle anderen Dateien unter `src/`
- `tests/`
- `configs/`
- `requirements.lock`
- `AGENTS.md`
- `documentation/engine/decisions.md`
- alle Audit-/Fixdokumente
- Notebooks
- `methodik.qmd`
- `references.bib`
- fertige Buchkapitel

--------------------------------------------------
14. ABSCHLUSSPRÜFUNG
--------------------------------------------------

Vor Abschluss:

1. Git-Diff prüfen
2. nur erlaubte Dateien verändert
3. Engine-Code ausser Versionsdatei unverändert
4. Tests unverändert
5. Configs/Demos unverändert
6. 441 Quelltests erfolgreich
7. Wheel 1.0.0 gebaut
8. frische Installation erfolgreich
9. pip check erfolgreich
10. 441 Wheeltests erfolgreich
11. vier Demos Checkout erfolgreich
12. vier Demos Wheel erfolgreich
13. bekannte Endwerte bestätigt
14. Offline-Backtests bestätigt
15. geschützte wissenschaftliche Dateien unverändert

Keinen Commit erstellen.
Keinen Git-Tag erstellen.

--------------------------------------------------
15. ABSCHLUSSANTWORT
--------------------------------------------------

Berichte nur:

1. geänderte/erstellte Dateien,
2. Version,
3. Quellsuite,
4. Wheel-Suite,
5. Wheel-/Installationsstatus,
6. vier Demo-Endwerte,
7. ob fachliche Outputs gegenüber 0.4.3 unverändert sind,
8. ob Engine-Logik verändert wurde,
9. ob Tests/Configs verändert wurden,
10. ob geschützte Dateien unverändert sind,
11. ob der Stand bereit für Release-Commit und Tag `engine-v1.0` ist.

Danach STOPPEN.

Keinen Commit und keinen Tag erstellen.