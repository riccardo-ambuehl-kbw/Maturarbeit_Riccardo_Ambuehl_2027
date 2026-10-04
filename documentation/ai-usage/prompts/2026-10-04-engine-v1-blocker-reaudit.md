# Codex-Prompt: Engine v1 – unabhängiger Re-Audit der ehemaligen Blocker

**Datum:** 2026-10-04
**Tool:** Codex
**Zweck:** Unabhängige Nachprüfung von EB-01 bis EB-03 nach den technischen Korrekturen vor dem Engine-v1.0-Freeze

## Vollständiger Prompt

Führe einen unabhängigen Re-Audit der ehemaligen ENGINE-BLOCKING-Befunde EB-01, EB-02 und EB-03 durch.

Dies ist KEIN Implementierungsauftrag.

Geprüfter Code-Ausgangspunkt muss exakt sein:

Commit:
`2020d5377449e23b1a9e7c36bb0caa1c3a9ebf44`

Technische Engine-Version:
`0.4.2`

Der ursprüngliche Gesamt-Audit steht in:

- `documentation/engine/final-audit.md`
- `documentation/engine/final-open-issues.md`

Die anschliessenden Fixes stehen in:

- `documentation/engine/blocker-fixes.md`

Lies ausserdem:

- `AGENTS.md`
- `documentation/engine/decisions.md`
- `documentation/engine/implementation.md`
- `documentation/engine/testing.md`
- den vollständigen aktuellen Engine-Code
- `tests/test_blocker_fixes.py`
- `tests/test_portfolio_state_validation.py`
- alle bisherigen Tests, soweit zur unabhängigen Beurteilung erforderlich

ZIEL

Beantworte unabhängig:

Sind die ursprünglichen ENGINE-BLOCKING-Befunde EB-01, EB-02 und EB-03 im aktuellen Stand tatsächlich geschlossen?

Versuche ausdrücklich, die Korrekturen zu widerlegen.

Eine bestehende grüne Test-Suite allein genügt nicht.

--------------------------------------------------
1. GIT-/CODE-STAND
--------------------------------------------------

Prüfe zuerst:

- aktueller Commit,
- Engine-Version,
- Working Tree,
- Änderungen gegenüber Commit `2020d5377449e23b1a9e7c36bb0caa1c3a9ebf44`.

Der geprüfte Engine-Code muss exakt diesem Commit entsprechen.

Zulässig ist gegenüber diesem Commit ausschliesslich der neu dokumentierte Re-Audit-Prompt.

Falls Engine-/Test-/Config-Code bereits verändert wurde, dokumentiere dies und stoppe.

--------------------------------------------------
2. EB-01 ERNEUT UNABHÄNGIG PRÜFEN
--------------------------------------------------

Ursprünglicher Befund:

Positive Zielgewichte konnten bei

portfolio_value * target_weight

numerisch auf 0.0 unterlaufen und danach als erfolgreicher Run weiterlaufen.

Reproduziere unabhängig mindestens:

A)
start_capital = 1e-200
Gewichte A=1e-200, B=1
A erhält später eine extreme, aber als Float darstellbare Wertsteigerung.

B)
denselben Unterlauf direkt beim Rebalancing-Helper.

C)
Unterlauf bei einer tatsächlichen späteren jährlichen Neuallokation.

D)
für Fixed Rebalancing und Country Weighting.

Prüfe gleichzeitig:

- echtes Zielgewicht 0 bleibt erlaubt,
- positive darstellbare sehr kleine Position bleibt erlaubt,
- positive nicht darstellbare Position wird abgelehnt,
- normale 60/40- und GDP-Allokationen funktionieren weiterhin,
- kein stilles Normalisieren oder Entfernen eines Assets.

Versuche zusätzliche numerische Gegenbeispiele nahe Float-Unterlauf/Überlauf.

KLASSIFIKATION:

EB-01 ist nur CLOSED, wenn kein reproduzierbarer Fall des ursprünglichen Problems mehr gefunden wird.

--------------------------------------------------
3. EB-02 ERNEUT UNABHÄNGIG PRÜFEN
--------------------------------------------------

Der ursprüngliche Befund hatte mehrere Teile.

Prüfe sie getrennt.

### 3.1 Drawdown

Manipuliere:

- mittlere Drawdown-Zeile,
- letzte Drawdown-Zeile,
- mehrere Drawdown-Zeilen gleichzeitig.

History-Renditen und Vermögen bleiben dabei unverändert.

Jede Manipulation muss abgelehnt werden.

### 3.2 Summary

Manipuliere unabhängig:

- start_value
- end_value
- total_return
- annualized_return
- annualized_volatility
- sharpe_ratio
- max_drawdown
- Verfügbarkeitsstatus
- fehlende/zusätzliche Summary-Zeilen
- falsche Strategiezuordnung
- NaN/Infinity an nicht erlaubten Stellen

Export muss vor Veröffentlichung scheitern.

### 3.3 Aktivierte Strategiemenge

Prüfe:

- fehlende aktivierte Strategie,
- zusätzliche nicht aktivierte Strategie.

Der vollständige Export muss exakt der aufgelösten Konfiguration entsprechen.

### 3.4 Buy-and-Hold

Prüfe:

- falsches Asset,
- anderes Asset mit zufällig identischer Preis-/Renditereihe,
- manipulierte Rendite trotz korrekter Asset-ID.

### 3.5 Fixed Rebalancing – Konfiguration

Prüfe:

- 20/80-Ergebnis unter 60/40-Config,
- falsche Assetmenge,
- veränderte Zielgewichte zwischen Bewertungen,
- fehlender Jahrestrade,
- zusätzlicher falscher Trade,
- Starttrade,
- Abschlusstrade.

### 3.6 Country Weighting

Prüfe weiterhin:

- GDP-Ziele gegen historische Entscheidung,
- Asset-/Proxybindung,
- Trade-Termine,
- Provenienz.

Keine bestehende strenge Prüfung darf durch die Fixes geschwächt worden sein.

### 3.7 Wirtschaftliche Portfoliozustandsfolge

Dies ist die zuletzt gefundene Restlücke.

Prüfe sie besonders unabhängig.

Minimalfall:

Startkapital 100
Ziel 60/40

A:
100 → 110

B:
100 → 100

Korrektes Portfolio:
100 → 106

Konstruiere ein vollständig intern konsistentes falsches Resultat:

100 → 120
period_return = 20 %
passender Drawdown
passende daraus neu berechnete Summary
formal gültige Gewichts-/Trade-Tabellen

Es muss aufgrund der tatsächlichen Marktperformance abgelehnt werden.

Prüfe dies für:

- Fixed Rebalancing
- Country Weighting

Prüfe ausserdem Manipulationen von:

- `weight_before`
- `weight_after`
- Drift zwischen Rebalancings
- Vor-Trade-Positionen
- Trade-Werten
- nach dem Trade gehaltenen Positionen für die Folgeperiode
- Zuständen am finalen Datum

Die Validierung muss die Zustandsfolge tatsächlich aus den Performance-Reihen des Context rekonstruieren.

Sie darf nicht lediglich die Tabellen gegeneinander vergleichen.

Versuche mindestens ein neues Gegenbeispiel, das NICHT bereits exakt als Testfall in `test_portfolio_state_validation.py` vorhanden ist.

--------------------------------------------------
4. EB-03 ERNEUT UNABHÄNGIG PRÜFEN
--------------------------------------------------

Reproduziere das ursprüngliche Beispiel:

Header mit drei Feldern,
Datenzeile mit vier Feldern.

Muss vor pandas scheitern.

Prüfe zusätzlich für alle vier Eingabetypen:

- market
- assets
- risk_free
- macro

Gegenbeispiele:

- ein Feld zu viel,
- ein Feld zu wenig,
- mehrere zusätzliche Felder,
- leere Datenzeile,
- doppelter Header,
- unbenannter Header,
- fehlerhafte Quotes,
- korrekt gequotetes Komma,
- korrekt gequoteter Zeilenumbruch,
- benannte zusätzliche Spalte mit überall korrekter Zeilenbreite.

Prüfe, dass keine Daten still abgeschnitten oder zu einem impliziten DataFrame-Index gemacht werden.

--------------------------------------------------
5. CROSS-CHECK DER FIXES
--------------------------------------------------

Prüfe, dass die drei Fixbereiche keine neue Regression verursacht haben.

Mindestens:

- Buy-and-Hold
- Fixed Rebalancing
- Trend
- Country Weighting

Prüfe insbesondere:

- gemeinsamer Kalender,
- Annualisierung,
- RF-Ausrichtung,
- Trend-Lag,
- GDP-As-of,
- Zielgewichte,
- Trades,
- Manifest,
- Datenqualität.

Keinen vollständigen neuen Methodik-Audit erfinden; Fokus bleibt EB-01 bis EB-03 und mögliche Regressionen daraus.

--------------------------------------------------
6. TEST-SUITE
--------------------------------------------------

Führe die vollständige bestehende Suite unverändert aus.

Erwarteter aktueller Ausgangsumfang:

428 Tests.

Die Zahl allein ist kein Beweis.

Lies insbesondere die neuen Tests kritisch und prüfe, ob sie tatsächlich die ursprünglichen Fehler reproduzieren.

Keine Tests verändern.

--------------------------------------------------
7. VIER DEMOS
--------------------------------------------------

Führe erneut aus:

- `configs/demo_buy_hold.json`
- `configs/demo_rebalance.json`
- `configs/demo_trend.json`
- `configs/demo_country_weighting.json`

Kontrolliere die zentralen bekannten Ergebnisse unabhängig.

Insbesondere unveränderte Endwerte:

- Buy-and-Hold-Demo: 99
- Rebalancing-Demo: 116.4284
- Trend-Demo: 96.8
- Country-Weighting-Demo: 117.667

Prüfe auch relevante Trades, Signale und GDP-Entscheidungen.

--------------------------------------------------
8. WHEEL / INSTALLATION
--------------------------------------------------

Baue aus dem exakt geprüften Stand ein aktuelles Wheel 0.4.2.

Installiere es in eine frische isolierte virtuelle Umgebung.

Prüfe:

- Import tatsächlich aus `site-packages`,
- Version 0.4.2,
- `pip check`,
- vollständige 428-Test-Suite gegen das Wheel,
- die drei ehemaligen Blocker-Gegenbeispiele gegen das Wheel,
- vier CLI-Demos gegen das Wheel.

Keine globale Installation.

--------------------------------------------------
9. OFFLINE
--------------------------------------------------

Prüfe erneut, dass die vier eigentlichen Backtests kein Netzwerk benötigen.

Paketbau/-installation ist davon getrennt.

--------------------------------------------------
10. BEWERTUNG
--------------------------------------------------

Bewerte jeden ursprünglichen Blocker separat:

- EB-01: CLOSED oder STILL OPEN
- EB-02: CLOSED oder STILL OPEN
- EB-03: CLOSED oder STILL OPEN

Falls STILL OPEN:

- reproduzierbarer Fall,
- betroffene Funktion,
- erwartetes Verhalten,
- tatsächliches Verhalten,
- Schweregrad.

Falls bei diesem Re-Audit ein NEUER ENGINE-BLOCKING-Fehler entdeckt wird, dokumentiere ihn ausdrücklich als:

NEW-EB-XX

mit reproduzierbarem Nachweis.

Keine Korrektur implementieren.

STUDY-BLOCKING SB-01 bis SB-07 und NON-BLOCKING NB-01 bis NB-03 bleiben bewusst offen und werden in diesem Auftrag nicht als Fehler neu bewertet, ausser eine Fix-Regression betrifft sie direkt.

--------------------------------------------------
11. DOKUMENTATION
--------------------------------------------------

Erstelle:

`documentation/engine/blocker-reaudit.md`

Inhalt mindestens:

- geprüfter Commit
- Engine-Version
- Plattform
- tatsächlich ausgeführte Tests
- Wheel-/Installationsprüfung
- EB-01-Nachprüfung
- EB-02-Nachprüfung
- EB-03-Nachprüfung
- zusätzliche neue Gegenbeispiele
- Demo-Regression
- Ergebnis pro Blocker CLOSED/STILL OPEN
- neu entdeckte ENGINE-BLOCKING-Befunde
- abschliessendes Freeze-Urteil

Ergänze:

`documentation/ai-usage/ai-usage-log.md`

gemäss bestehendem Schema.

Keine anderen versionierten Dateien verändern.

--------------------------------------------------
12. FREEZE-KRITERIUM
--------------------------------------------------

Schreibe nur dann:

`ENGINE-V1.0-FREEZE TECHNICALLY READY`

wenn gleichzeitig:

- EB-01 = CLOSED
- EB-02 = CLOSED
- EB-03 = CLOSED
- keine neuen ENGINE-BLOCKING-Befunde gefunden wurden
- vollständige Suite erfolgreich
- Wheel-Prüfung erfolgreich
- vier Demos erfolgreich
- Engine-/Test-/Config-Code während des Re-Audits unverändert

Dies bedeutet ausdrücklich NICHT:

- reale Studie fertig,
- SB-01 bis SB-07 gelöst,
- wissenschaftliche Texte synchronisiert,
- reale Daten validiert.

--------------------------------------------------
13. NICHT ERLAUBT
--------------------------------------------------

Keine Änderung an:

- `src/`
- `tests/`
- `configs/`
- `pyproject.toml`
- `requirements.lock`
- `documentation/engine/decisions.md`
- `documentation/engine/final-audit.md`
- `documentation/engine/final-open-issues.md`
- `documentation/engine/blocker-fixes.md`
- Notebooks
- methodik.qmd
- references.bib
- fertigen Buchkapiteln

Keine Bugfixes.

Keine neuen Tests committen.

Keine neue Methodik.

Keine realen Daten.

Temporäre Prüfdateien nur in ignorierten Bereichen.

--------------------------------------------------
14. ABSCHLUSSANTWORT
--------------------------------------------------

Berichte am Ende nur:

1. geprüfter Commit und Version,
2. Ergebnis vollständige Suite,
3. Ergebnis Wheel-Suite,
4. EB-01 CLOSED/STILL OPEN,
5. EB-02 CLOSED/STILL OPEN,
6. EB-03 CLOSED/STILL OPEN,
7. Anzahl neuer ENGINE-BLOCKING-Befunde,
8. Ergebnis der vier Demos,
9. ob Engine-/Test-/Config-Code verändert wurde,
10. ob `ENGINE-V1.0-FREEZE TECHNICALLY READY` erreicht wurde.

Danach STOPPEN.

Keine Korrekturen implementieren und noch keinen v1.0-Tag setzen.