# Codex-Prompt: Engine v1 – finaler technischer Freeze-Re-Audit

**Datum:** 2026-10-04
**Tool:** Codex
**Zweck:** Letzte unabhängige technische Prüfung vor dem Engine-v1.0-Freeze

## Vollständiger Prompt

Führe den letzten gezielten technischen Re-Audit der Backtesting-Engine vor dem Engine-v1.0-Freeze durch.

Dies ist KEIN Implementierungsauftrag.

Geprüfter Code-Ausgangspunkt:

Commit:
`270b7969a46bfbdb9f4614a4f6d88507540f6b92`

Engine-Version:
`0.4.3`

Dieser Re-Audit ist bewusst kleiner als der frühere vollständige Audit.

Ziel ist ausschliesslich zu prüfen, ob:

- EB-01 weiterhin geschlossen ist,
- EB-02 weiterhin geschlossen ist,
- EB-03 einschliesslich NEW-EB-01 geschlossen ist,
- durch den letzten CSV-Fix keine Regression entstanden ist,
- keine neuen ENGINE-BLOCKING-Probleme im unmittelbar betroffenen Bereich sichtbar werden.

LIES ZUERST:

- `AGENTS.md`
- `documentation/engine/decisions.md`
- `documentation/engine/final-audit.md`
- `documentation/engine/final-open-issues.md`
- `documentation/engine/blocker-fixes.md`
- `documentation/engine/blocker-reaudit.md`
- `documentation/engine/implementation.md`
- `documentation/engine/testing.md`

Lies ausserdem den aktuellen Code der relevanten Bereiche:

- `src/data/normalize.py`
- `src/data/validate.py`
- `src/funktionen.py`
- `src/engine/portfolio.py`
- `src/engine/result.py`
- `src/analysis/metrics.py`
- `src/export/results.py`
- `src/engine/simulation.py`

und insbesondere:

- `tests/test_blocker_fixes.py`
- `tests/test_portfolio_state_validation.py`
- `tests/test_csv_nul.py`

Keine Dateien ausser der ausdrücklich erlaubten Audit-Dokumentation verändern.

--------------------------------------------------
1. CODESTAND
--------------------------------------------------

Prüfe:

- Commit
- Version
- Working Tree
- Diff gegen `270b7969a46bfbdb9f4614a4f6d88507540f6b92`

Der Engine-/Test-/Config-Code muss exakt diesem Commit entsprechen.

Gegenüber dem Commit darf vor Beginn ausschliesslich der neue Freeze-Re-Audit-Prompt versioniert sein.

Wenn Engine-Code bereits verändert wurde: dokumentieren und STOPP.

--------------------------------------------------
2. EB-01 REGRESSION
--------------------------------------------------

Prüfe unabhängig erneut mindestens:

- positiver initialer Allokationsunterlauf,
- direkter Rebalancing-Helper-Unterlauf,
- positiver Unterlauf bei jährlicher Neuallokation,
- Fixed Rebalancing,
- Country Weighting,
- echtes Nullgewicht weiterhin zulässig,
- sehr kleine, aber darstellbare positive Position weiterhin zulässig.

Erwartung:

Nicht darstellbare positive Zielposition → Fehler.

Kein Normalisieren, Entfernen oder stilles Nullsetzen.

Wenn dies weiterhin gilt:

EB-01 = CLOSED.

--------------------------------------------------
3. EB-02 REGRESSION
--------------------------------------------------

Prüfe gezielt erneut:

A. Drawdown
- manipulierte Drawdown-Zeile wird abgelehnt.

B. Summary
- manipulierter Endwert oder Sharpe wird abgelehnt.
- falscher Status wird abgelehnt.

C. Strategiemenge
- fehlende aktivierte Strategie wird abgelehnt.

D. Fixed Rebalancing
- 20/80 unter 60/40-Config wird abgelehnt.

E. Marktportfoliozustand

Minimalfall:

Kapital 100
A: 100 → 110
B: 100 → 100
Ziele 60/40

Korrektes Portfolio = 106.

Ein intern konsistentes gefälschtes Portfolio 120 muss für:

- Fixed Rebalancing
- Country Weighting

an der vollständigen Run-/Exportgrenze abgelehnt werden.

Prüfe zusätzlich mindestens eine Manipulation des gehaltenen Zustands zwischen zwei Perioden.

Wenn die Resultate weiterhin tatsächlich aus `context.performance` rekonstruiert werden:

EB-02 = CLOSED.

--------------------------------------------------
4. EB-03 UND NEW-EB-01
--------------------------------------------------

Prüfe zuerst den ursprünglichen EB-03-Fall:

Header:
3 Felder

Datenzeile:
4 Felder

→ muss vor pandas abgelehnt werden.

Prüfe danach NEW-EB-01.

Exakter Minimalfall:

`performance_value` enthält als tatsächliche Bytes:

`1\x00e2`

Der vollständige Run muss abgelehnt werden.

Prüfe NUL mindestens in:

- market
- assets
- risk_free
- macro

und mindestens einmal:

- unquoted
- quoted
- UTF-8-BOM

Prüfe ausdrücklich, dass pandas bei NUL-Inhalt NICHT aufgerufen wird.

Positive Kontrollen:

- gequotetes Komma
- gequoteter Zeilenumbruch
- benannte Zusatzspalte
- UTF-8-BOM ohne NUL

müssen weiterhin funktionieren.

Wenn kein NUL-Inhalt still gekürzt oder repariert wird und der ursprüngliche Breitenfehler ebenfalls geschlossen bleibt:

EB-03 = CLOSED
NEW-EB-01 = CLOSED

--------------------------------------------------
5. VOLLSTÄNDIGE SUITE
--------------------------------------------------

Führe die gesamte unveränderte Test-Suite aus.

Erwarteter Umfang:

441 Tests.

Keine Tests verändern.

--------------------------------------------------
6. VIER DEMOS
--------------------------------------------------

Führe erneut aus:

- `configs/demo_buy_hold.json`
- `configs/demo_rebalance.json`
- `configs/demo_trend.json`
- `configs/demo_country_weighting.json`

Unabhängig kontrollierte Endwerte:

- Buy-and-Hold: 99
- Fixed Rebalancing: 116.4284
- Trend: 96.8
- Country Weighting: 117.667

Prüfe ausserdem stichprobenweise:

- Rebalancing-Trades
- Trend-Signale/Lag
- GDP-Auswahl/Revision
- Datenqualität
- Manifest/Input-/Resultathashes

--------------------------------------------------
7. WHEEL
--------------------------------------------------

Baue aus exakt diesem Stand ein Wheel 0.4.3.

Frische isolierte virtuelle Umgebung:

- kein Editable-Install
- Import aus `site-packages`
- Version 0.4.3
- `pip check`
- komplette 441-Test-Suite gegen Wheel
- EB-01-Gegenprobe
- EB-02-Marktportfolio-Gegenprobe
- EB-03-NUL-Gegenprobe
- vier CLI-Demos

Keine globale Installation.

--------------------------------------------------
8. OFFLINE
--------------------------------------------------

Prüfe erneut, dass die eigentlichen vier Backtests ohne Netzwerkzugriff laufen.

Paketbau/-installation ist davon getrennt.

--------------------------------------------------
9. KEIN NEUER GROSSER METHODIK-AUDIT
--------------------------------------------------

SB-01 bis SB-07 bleiben bewusst offen für die reale Studie.

NB-01 bis NB-03 bleiben bewusst dokumentiert.

Diese Punkte verhindern den technischen Freeze der klar abgegrenzten Engine nicht.

Nicht erneut reale Wertpapiere, SMA-Parameter, RF-Serie, GDP-Quelle oder Annualisierungsmethodik auswählen.

--------------------------------------------------
10. BEWERTUNG
--------------------------------------------------

Berichte separat:

- EB-01 = CLOSED oder STILL OPEN
- EB-02 = CLOSED oder STILL OPEN
- EB-03 = CLOSED oder STILL OPEN
- NEW-EB-01 = CLOSED oder STILL OPEN

Falls irgendein Befund STILL OPEN ist:

`ENGINE-V1.0-FREEZE TECHNICALLY READY`

darf NICHT ausgegeben werden.

Falls ein neuer ENGINE-BLOCKING-Befund gefunden wird:

als `NEW-EB-XX` mit reproduzierbarem Beispiel dokumentieren.

Keine Korrektur implementieren.

--------------------------------------------------
11. FREEZE-KRITERIUM
--------------------------------------------------

Nur wenn gleichzeitig:

- EB-01 CLOSED
- EB-02 CLOSED
- EB-03 CLOSED
- NEW-EB-01 CLOSED
- 0 neue ENGINE-BLOCKING-Befunde
- 441 Quelltests erfolgreich
- 441 Wheeltests erfolgreich
- vier Demos erfolgreich
- Offline-Backtests erfolgreich
- Engine-/Test-/Config-Code unverändert

darf das Urteil exakt lauten:

`ENGINE-V1.0-FREEZE TECHNICALLY READY`

Dies bedeutet ausdrücklich NICHT:

- reale Daten freigegeben,
- Hauptuntersuchung durchgeführt,
- SB-01 bis SB-07 gelöst,
- wissenschaftliche Texte synchronisiert.

--------------------------------------------------
12. DOKUMENTATION
--------------------------------------------------

Erstelle ausschliesslich:

`documentation/engine/freeze-reaudit.md`

mit:

- geprüftem Commit
- Version
- Plattform
- Quelltests
- Wheeltests
- EB-01 Ergebnis
- EB-02 Ergebnis
- EB-03 Ergebnis
- NEW-EB-01 Ergebnis
- eigene Gegenproben
- vier Demos
- Offline-Prüfung
- neue ENGINE-BLOCKING-Befunde
- finales Freeze-Urteil

Ergänze ausschliesslich append-only:

`documentation/ai-usage/ai-usage-log.md`

Keine andere versionierte Datei verändern.

--------------------------------------------------
13. NICHT ERLAUBT
--------------------------------------------------

Keine Änderungen an:

- src/
- tests/
- configs/
- pyproject.toml
- requirements.lock
- AGENTS.md
- decisions.md
- final-audit.md
- final-open-issues.md
- blocker-fixes.md
- blocker-reaudit.md
- implementation.md
- testing.md
- Notebooks
- methodik.qmd
- references.bib
- fertigen Buchkapiteln

Keine Bugfixes.
Keine neuen Tests.
Keine realen Daten.
Keine neue Methodik.
Kein v1.0-Tag.

--------------------------------------------------
14. ABSCHLUSSANTWORT
--------------------------------------------------

Berichte nur:

1. geprüfter Commit und Version,
2. Quellsuite,
3. Wheel-Suite,
4. EB-01,
5. EB-02,
6. EB-03,
7. NEW-EB-01,
8. Anzahl neuer ENGINE-BLOCKING-Befunde,
9. vier Demo-Ergebnisse,
10. ob Engine-/Test-/Config-Code unverändert blieb,
11. finales Freeze-Urteil.

Danach STOPPEN.