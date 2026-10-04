# Codex-Prompt: Engine v1 – Restfix wirtschaftliche Portfoliozustandsfolge

**Datum:** 2026-10-04
**Tool:** Codex
**Zweck:** Vollständige Schliessung der verbleibenden EB-02-Lücke vor dem Re-Audit

## Vollständiger Prompt

Behebe ausschliesslich die verbleibende Restlücke von EB-02:

Die strenge vollständige Run-/Exportvalidierung bindet Fixed Rebalancing und Country Weighting derzeit zwar an Assetmengen, Zielgewichte, Trade-Termine und interne Kapitalbilanzen, prüft aber noch nicht vollständig, ob die gespeicherte wirtschaftliche Zustandsfolge tatsächlich aus den Performance-Werten des SimulationContext entstanden sein kann.

Dies ist ein technischer Konsistenzfix. Keine neue finanzwirtschaftliche Entscheidung treffen.

Lies zuerst:

- AGENTS.md
- documentation/engine/decisions.md
- documentation/engine/final-audit.md
- documentation/engine/final-open-issues.md
- documentation/engine/blocker-fixes.md
- src/engine/result.py
- src/engine/portfolio.py
- src/funktionen.py
- tests/test_blocker_fixes.py
- die bestehenden Rebalancing- und Country-Weighting-Tests

ZIEL

Bei `validate_results(..., require_complete=True)` muss für Fixed Rebalancing und Country Weighting zusätzlich geprüft werden, dass der vollständige Portfoliozustand mit

- dem vorher tatsächlich gehaltenen Zustand,
- den tatsächlichen Performance-Renditen aus `context.performance`,
- der festgelegten Reihenfolge Rendite → Drift → gegebenenfalls Rebalancing,
- den gespeicherten weights_history-Zuständen,
- den gespeicherten trades,
- dem gespeicherten portfolio_history

konsistent ist.

Ein Resultat darf nicht allein deshalb gültig sein, weil Portfolio-Werte, Renditen, Gewichte und Trades untereinander algebraisch konsistent aussehen.

Es muss zur tatsächlichen Marktwertentwicklung des Context passen.

WICHTIG

- Keine zweite unabhängige finanzielle Methodik erfinden.
- Verwende die bereits festgelegte Portfolio-Zustandsfolge und die bestehenden gemeinsamen Funktionen.
- Keine Änderung der akzeptierten Rebalancing-Regel.
- Keine Änderung von Toleranzen ohne technischen Grund.
- Normale Runner-Ergebnisse dürfen sich nicht verändern.

VERPFLICHTENDE REPRODUKTION

Erzeuge einen synthetischen Fixed-Rebalancing-Fall innerhalb eines Kalenderjahres ohne Rebalancing-Ereignis:

Startkapital = 100
Ziele = 60/40

Asset A:
100 → 110

Asset B:
100 → 100

Der korrekte Portfoliowert ist 106.

Konstruiere danach bewusst ein gefälschtes, intern konsistentes Resultat mit beispielsweise:

portfolio:
100 → 120

period_return:
leer → 20 %

drawdown:
0 → 0

weights_history:
Start 60/40
zweiter Zeitpunkt ebenfalls gültig aussehende Gewichte

trades:
leer

summary:
korrekt aus dem gefälschten Portfolio neu berechnet.

Dieses Resultat muss an der vollständigen Run-/Exportgrenze abgelehnt werden, weil es nicht aus den tatsächlichen Assetrenditen des Context entstehen kann.

COUNTRY-WEIGHTING

Erzeuge denselben Typ Gegenbeispiel auch für Country Weighting.

Die bereits geprüften historischen BIP-Ziele und Entscheidungen bleiben verbindlich; zusätzlich muss die tatsächliche Portfolioentwicklung aus den Assetrenditen nachvollziehbar sein.

PRÜFE INSBESONDERE

Für jede Periode:

1. Ausgangspositionen entsprechen dem tatsächlich nach der vorherigen Bewertung gehaltenen Zustand.
2. Die jeweilige Assetrendite stammt aus den gemeinsamen `performance_value`-Reihen.
3. Daraus resultieren die Positionen vor einem möglichen Trade.
4. Summe dieser Positionen entspricht dem gespeicherten Portfoliowert.
5. `weight_before` entspricht diesen Positionen.
6. Ohne Rebalancing gilt `weight_after = weight_before`.
7. Bei einem Rebalancing stimmen Trades und neue Zielpositionen.
8. Diese Zielpositionen bilden den Ausgangszustand der nächsten Periode.

Initiale Allokation und finales Datum bleiben nach den bestehenden Regeln behandelt.

TESTS

Ergänze mindestens:

- gefälschtes Fixed-Rebalancing-Portfolio trotz korrekter Targets → Fehler
- gefälschte Fixed-Rebalancing-Gewichte bei korrektem Portfolio → Fehler
- gefälschte Country-Weighting-Portfolioentwicklung → Fehler
- gefälschte Country-Weighting-Gewichte zwischen Entscheidungen → Fehler
- normale Fixed-Rebalancing-Demo unverändert
- normale Country-Weighting-Demo unverändert
- alle bisherigen 406 Tests weiterhin grün

Wenn möglich, verwende die vorhandenen gemeinsamen Portfoliofunktionen für die Validierung bzw. einen kleinen gemeinsamen technischen Helper. Keine parallele zweite Strategieimplementierung.

VERSION

Wenn Code geändert wird, erhöhe die technische Paketversion konsistent von 0.4.1 auf 0.4.2.

DOKUMENTATION

Aktualisiere:

- documentation/engine/blocker-fixes.md
- documentation/engine/implementation.md
- documentation/engine/testing.md
- documentation/ai-usage/ai-usage-log.md

Dokumentiere ausdrücklich, dass dies die nach dem ersten Fix-Review verbliebene EB-02-Restlücke schliesst.

Nicht verändern:

- final-audit.md
- final-open-issues.md
- decisions.md
- Theorie
- Analyse
- methodik.qmd
- references.bib
- fertige Buchkapitel

ABSCHLUSS

- vollständige Suite ausführen
- beide neuen Gegenbeispiele ausführen
- vier bestehenden Demos ausführen
- normale fachliche Demo-Outputs auf Regression prüfen
- Wheel bauen
- frische Wheel-Installation
- pip check
- komplette Suite gegen Wheel

Keinen Commit erstellen.

Abschlussantwort nur mit:
1. geänderten Dateien,
2. Ursache der Restlücke,
3. technischer Korrektur,
4. Ergebnis beider Gegenbeispiele,
5. Gesamtzahl Tests,
6. Demo-Regression,
7. Wheel-Prüfung,
8. ob neue fachliche Entscheidungen nötig waren,
9. ob geschützte Dateien unverändert blieben.

Danach stoppen.