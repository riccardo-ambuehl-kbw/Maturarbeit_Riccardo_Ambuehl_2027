# Codex-Prompt: Engine v1 – Multi-Asset und Rebalancing

**Datum:** 2026-10-04
**Tool:** Codex
**Zweck:** Erweiterung der geprüften Core-Engine um Multi-Asset-Portfolios und jährliches Rebalancing

## Vollständiger Prompt

Erweitere die bereits geprüfte und mit `engine-core-v0.1.0` markierte Core-Engine um Multi-Asset-Portfolios und die allgemeine Strategie mit festen Zielgewichten und jährlichem Rebalancing.

Der bestehende Core ist fachlich abgenommen und soll erweitert, nicht unnötig neu geschrieben werden.

LIES VOR DER IMPLEMENTIERUNG:

1. `AGENTS.md`
2. `documentation/engine/audit.md`
3. `documentation/engine/open-decisions.md`
4. `documentation/engine/decisions.md`
5. `documentation/engine/implementation.md`
6. `documentation/engine/testing.md`
7. `notebooks/Analyse.ipynb`, insbesondere Kapitel 5.3 bis 5.9
8. `notebooks/Theorie.ipynb`, insbesondere Kapitel 3.7 bis 3.10 und 3.13
9. `src/funktionen.py`
10. den bestehenden Engine-Code und die komplette Test-Suite

OD-01, OD-02, OD-03, OD-06, OD-10 und OD-13 sind für diesen Arbeitsschritt besonders wichtig.

Der Tag `engine-core-v0.1.0` ist der akzeptierte Ausgangspunkt. Bestehende Core-Funktionalität und bestehende Tests dürfen nicht ohne sachlichen Grund gebrochen werden.

--------------------------------------------------
ZIEL
--------------------------------------------------

Implementiere:

- Multi-Asset-Kontext für alle von aktivierten Strategien benötigten Anlagen,
- eine allgemeine Long-only-Rebalancing-Strategie mit festen Zielgewichten,
- jährliches Rebalancing gemäss OD-06,
- 60/40 als synthetischen Test- und Demonstrationsfall dieser allgemeinen Strategie,
- `weights_history`,
- `trades`,
- Unterstützung mehrerer aktivierter Strategien innerhalb desselben Runs, mindestens Buy-and-Hold und Rebalancing,
- gemeinsame Ergebnis- und Exportlogik für mehrere Strategien.

Noch NICHT implementieren:

- Trendfolge/SMA,
- BIP-/Country-Weighting,
- reale Datenadapter,
- Yahoo/FRED-Downloads,
- FX-Konvertierung,
- Transaktionskosten,
- Steuern,
- Inflation,
- Batch-System,
- Web/API,
- Parameteroptimierung,
- Hauptversuch.

--------------------------------------------------
1. GEMEINSAMER DATENKALENDER
--------------------------------------------------

OD-01 bleibt verbindlich.

Bestimme zunächst die Vereinigung aller `asset_id`, die von allen aktivierten Strategien eines Runs benötigt werden.

Alle diese benötigten Performance-Reihen werden VOR der Renditeberechnung auf gemeinsame tatsächlich vorhandene Bewertungszeitpunkte ausgerichtet.

Damit verwenden alle im selben Run verglichenen Strategien denselben effektiven Bewertungszeitraum.

Keine Interpolation.
Kein Forward-Fill.
Keine erfundenen Handelstage.
NaN/Inf bleiben Fehler.

Nicht gemeinsame Zeitpunkte müssen weiterhin im Datenqualitätsbericht dokumentiert werden.

Eine nicht benötigte zusätzliche Anlage in einer CSV darf den Vergleichskalender nicht beeinflussen.

--------------------------------------------------
2. KONFIGURATION
--------------------------------------------------

Erweitere das bestehende JSON-Schema so, dass mindestens folgende Strategien aktiviert werden können:

- `buy_hold`
- `rebalance`

Ein Run darf eine oder beide Strategien aktivieren.

Mindestens eine Strategie muss aktiviert sein.

Für `rebalance` müssen mindestens angegeben werden:

- `enabled`
- `target_weights`
- `rebalance_frequency`

Beispiel nur als Schema:

"rebalance": {
  "enabled": true,
  "target_weights": {
    "EQ_SYNTH": 0.60,
    "BD_SYNTH": 0.40
  },
  "rebalance_frequency": "annual"
}

Für Engine v1 in diesem Arbeitsschritt wird als Rebalancing-Frequenz ausschliesslich `"annual"` unterstützt.

Andere Frequenzen dürfen nicht still interpretiert werden.

Die Engine selbst ist allgemein für andere vollständig investierte positive Zielgewichte als 60/40 nutzbar. 60/40 ist nur der Demonstrationsfall der Maturarbeit.

OD-13:

- jedes Zielgewicht >= 0,
- kein Short,
- kein Hebel,
- Summe aller Zielgewichte = 1 innerhalb einer kleinen dokumentierten numerischen Toleranz,
- keine stille Normalisierung einer falschen Gewichtssumme,
- keine implizite Cash-Position,
- alle Assets müssen in Daten und Metadaten vorhanden sein,
- Währung muss zur Basiswährung passen.

Keine fachlichen Default-Zielgewichte.

--------------------------------------------------
3. MEHRERE STRATEGIEN IN EINEM RUN
--------------------------------------------------

Erweitere die Orchestrierung so, dass ein Run mehrere aktivierte Strategien ausführen kann.

Alle Strategien müssen denselben vorbereiteten `SimulationContext` und denselben effektiven Kalender verwenden.

Keine Strategie darf ihren eigenen Vergleichszeitraum still verkürzen.

Der bestehende Einzelstrategie-Buy-and-Hold-Fall muss weiterhin funktionieren.

Falls die interne `RunOutcome`-/Result-Struktur erweitert werden muss, bevorzuge eine rückwärtskompatible Lösung, soweit dies ohne unnötige Komplexität möglich ist.

Die Berechnungslogik darf nicht für CLI und Python doppelt implementiert werden.

--------------------------------------------------
4. PORTFOLIOZUSTAND DER REBALANCING-STRATEGIE
--------------------------------------------------

Zum effektiven Startzeitpunkt:

`position_value(asset) = start_capital * target_weight(asset)`

Das Portfolio ist vollständig investiert.

Die erste Zeile des Portfolioverlaufs bleibt:

- portfolio_value = start_capital
- period_return = nicht beobachtet
- drawdown = 0

Für jedes folgende Intervall:

1. Verwende die Positionswerte, die zu Beginn dieses Intervalls tatsächlich gehalten wurden.
2. Berechne je Asset die Rendite aus den gemeinsamen Performance-Werten.
3. Schreibe die einzelnen Positionswerte mit diesen Renditen fort.
4. Summiere die neuen Positionswerte zum neuen Portfoliowert.
5. Berechne daraus die tatsächliche Portfoliorendite.
6. Bestimme die Gewichte nach der Rendite und vor einem möglichen Rebalancing.
7. Prüfe, ob dieser Bewertungstermin ein gültiger jährlicher Rebalancing-Zeitpunkt ist.
8. Falls ja, berechne Zielwerte und Transaktionen.
9. Übernimm die Zielwerte tatsächlich als neuen Portfoliozustand für die folgende Renditeperiode.

Keine Berechnung mit in jeder Periode künstlich erneut gesetzten 60/40-Gewichten.

--------------------------------------------------
5. JÄHRLICHES REBALANCING – OD-06
--------------------------------------------------

Das jährliche Rebalancing findet am letzten gemeinsamen Bewertungszeitpunkt eines Kalenderjahres statt.

Reihenfolge ist verbindlich:

Rendite des gerade beendeten Intervalls
→ neue Positionswerte
→ Gewichtungsdrift
→ Rebalancing
→ Zielgewichte gelten für das nächste Intervall.

Die Rendite, die am Rebalancing-Datum endet, wurde also noch mit den vorher gehaltenen Gewichten verdient.

Kein Look-ahead.

Die Startbewertung gilt bereits als initiale Zielallokation und erzeugt keinen künstlichen Rebalancing-Trade.

Ein Rebalancing am letzten Datum des gesamten Untersuchungszeitraums wird nicht ausgeführt, wenn danach keine weitere Renditeperiode existiert.

Es soll kein wirtschaftlich wirkungsloser Abschlusstrade erzeugt werden.

--------------------------------------------------
6. WIEDERVERWENDUNG BESTEHENDER FUNKTIONEN
--------------------------------------------------

Verwende `neue_gewichtung()` und `rebalancing()` als Ausgangspunkt, soweit fachlich sinnvoll.

Der Audit hat gezeigt, dass fehlende Labels oder unvollständige Renditereihen dort zu problematischem Verhalten führen können.

Du darfst diese bestehenden Funktionen transparent härten, insbesondere für:

- identische Asset-Labels,
- eindeutige Labels,
- vollständige Werte,
- endliche Werte,
- gültige Renditen,
- positive bzw. zulässige Positionswerte,
- gültige Zielgewichte,
- Kapitalerhaltung.

Keine zweite unabhängige Rebalancing-Formelsammlung erstellen, wenn die bestehenden Funktionen sauber erweitert werden können.

Jede Änderung an `src/funktionen.py` dokumentieren und gezielt testen.

--------------------------------------------------
7. KAPITALERHALTUNG
--------------------------------------------------

Da Transaktionskosten in der Methodik ausgeschlossen sind, verändert das Rebalancing den Portfoliowert selbst nicht.

Für jeden Rebalancing-Zeitpunkt muss gelten:

sum(value_before) == sum(target_value)

innerhalb numerischer Toleranz.

Und:

sum(transaction_value) == 0

innerhalb numerischer Toleranz.

Nach dem Rebalancing:

weight_after == target_weight

innerhalb numerischer Toleranz.

Kein Kapital darf verschwinden oder entstehen.

--------------------------------------------------
8. `weights_history`
--------------------------------------------------

Implementiere:

`weights_history.csv`

mindestens mit den bereits in Analyse 5.7 vorgesehenen Feldern:

date
strategy
asset_id
weight_before
target_weight
weight_after

Für die Rebalancing-Strategie soll die Tabelle den Gewichtungszustand an jedem verwendeten Bewertungsdatum nachvollziehbar machen.

Definition:

- Startdatum:
  `weight_before = target_weight = weight_after`, da dies die initiale Allokation ist.
- Normales Datum ohne Rebalancing:
  `weight_before` = tatsächliches Gewicht nach der gerade verbuchten Rendite,
  `target_weight` = konfiguriertes Referenz-Zielgewicht,
  `weight_after = weight_before`.
- Rebalancing-Datum:
  `weight_before` = Gewicht nach Rendite und vor Rebalancing,
  `target_weight` = konfiguriertes Zielgewicht,
  `weight_after` = tatsächlich nach Rebalancing gehaltenes Gewicht.

Das Vorhandensein von `target_weight` an jedem Datum bedeutet NICHT, dass täglich rebalanciert wurde.

Dokumentiere diese Semantik klar.

Für jedes Datum müssen `weight_before` und `weight_after` jeweils über alle Assets zu 1 summieren.

--------------------------------------------------
9. `trades`
--------------------------------------------------

Implementiere:

`trades.csv`

mit:

date
strategy
asset_id
value_before
target_value
transaction_value

Dabei:

transaction_value = target_value - value_before

Trades werden nur für tatsächliche jährliche Rebalancing-Ereignisse ausgegeben.

Die initiale Kapitalaufteilung am Start ist kein Rebalancing-Trade.

Am endgültigen Untersuchungsende werden keine Trades erzeugt, wenn keine spätere Renditeperiode mehr existiert.

Bei einem gültigen geplanten Rebalancing-Ereignis dürfen auch Transaktionswerte nahe bzw. gleich 0 dokumentiert werden, wenn das Portfolio zufällig bereits den Zielgewichten entspricht.

--------------------------------------------------
10. PORTFOLIO_HISTORY
--------------------------------------------------

Die bestehende gemeinsame Struktur bleibt:

date
strategy
portfolio_value
period_return
drawdown

Für mehrere Strategien enthält die exportierte Datei mehrere Strategien.

Jede Strategie besitzt dieselben Bewertungsdaten.

Die Reihenfolge im Export muss deterministisch sein.

Der Portfoliowert am Rebalancing-Datum ist vor und nach den kostenfreien Trades identisch.

Drawdown und Kennzahlen werden aus dem tatsächlichen Portfolioverlauf jeder Strategie berechnet.

--------------------------------------------------
11. SUMMARY UND RISK-FREE
--------------------------------------------------

`summary.csv` enthält eine Zeile pro ausgeführter Strategie.

Alle Strategien werden über dieselben Perioden bewertet.

Risk-Free-Ausrichtung bleibt wie im akzeptierten Core.

Sharpe wird für jede Strategie aus deren tatsächlichen Portfoliorenditen gegen dieselbe vollständig ausgerichtete Risk-Free-Periodenreihe berechnet.

Keine Strategie darf fehlende Risk-Free-Daten selbst auffüllen.

--------------------------------------------------
12. EXPORT
--------------------------------------------------

Bei mindestens einer Rebalancing-Strategie soll ein erfolgreicher Run zusätzlich erzeugen:

- `weights_history.csv`
- `trades.csv`

Diese Dateien müssen ebenfalls im `run_manifest.json` mit SHA-256 erfasst werden.

Optional nicht benötigte Tabellen sollen bei einem reinen Buy-and-Hold-Run nicht künstlich mit leeren/fiktiven Daten gefüllt werden.

Bestehende Core-Exporte bleiben erhalten:

- portfolio_history.csv
- summary.csv
- data_quality.json
- run_manifest.json

Reproduzierbarkeit und atomischer Export bleiben erhalten.

--------------------------------------------------
13. SYNTHETISCHE DEMODATEN
--------------------------------------------------

Erstelle einen zweiten künstlichen Demo-Fall für Rebalancing.

Er muss mindestens enthalten:

- zwei Assets,
- unterschiedliche Renditeverläufe,
- mehrere Bewertungen innerhalb mindestens eines Kalenderjahres,
- sichtbare Gewichtungsdrift,
- mindestens ein tatsächliches Jahresendrebalancing,
- mindestens eine Renditeperiode nach diesem Rebalancing, damit nachgewiesen werden kann, dass die neuen Zielgewichte wirklich verwendet werden,
- einen endgültigen Jahresultimo ohne nachfolgende Periode, an dem kein nutzloser Abschlusstrade erzeugt wird, wenn dies durch den Datensatz darstellbar ist.

Die Werte sollen klein und künstlich sein und zentrale Zwischenschritte von Hand nachvollziehbar machen.

Keine realen Wertpapiere verwenden.

Erstelle eine entsprechende Demo-Konfiguration, z. B.:

`configs/demo_rebalance.json`

Die 60/40-Gewichte der Demo sind Testwerte und noch keine Festlegung der späteren realen Wertpapiere oder des Untersuchungszeitraums.

--------------------------------------------------
14. VERPFLICHTENDE TESTS
--------------------------------------------------

Die bisherigen Core-Tests müssen weiterhin bestehen.

Ergänze mindestens folgende Prüfungen:

A. Initiale Allokation
- Startkapital 100 und Zielgewichte 60/40 ergeben Positionswerte 60/40.
- Kein initialer Rebalancing-Trade.

B. Gewichtungsdrift
Beispiel:
- Aktienposition steigt stärker als Anleihenposition.
- Gewicht der Aktie liegt danach über 60 %.
- Vor dem Jahresende wird nicht auf 60/40 zurückgesetzt.

C. Kein periodisches Schein-Rebalancing
- Innerhalb eines Kalenderjahres müssen Gewichte weiterdriften.
- Ergebnis muss sich von einer fälschlich in jeder Periode auf 60/40 zurückgesetzten Berechnung unterscheiden, wenn der Testdatensatz dies sichtbar macht.

D. Jahresendrebalancing
- Letzter gemeinsamer Bewertungszeitpunkt des Jahres wird korrekt erkannt.
- Erst Rendite, dann Rebalancing.
- `weight_before` zeigt Drift.
- `weight_after` entspricht 60/40.
- Trades ergeben die richtige Richtung und Grösse.

E. Folgende Periode
- Die Rendite nach dem Jahresendrebalancing wird mit den nach dem Rebalancing gehaltenen Positionen verdient.

F. Kapitalerhaltung
- Summe der Zielwerte = Portfoliowert.
- Summe der Transaktionen = 0.
- Rebalancing verändert den Portfoliowert nicht.

G. Kein Abschlusstrade
- Ist das letzte Bewertungsdatum zugleich Jahresultimo und es folgt keine weitere Renditeperiode, wird dort kein Rebalancing-Trade erzeugt.

H. Gewichtsvalidierung
Ablehnen:
- Summe < 1,
- Summe > 1,
- negative Gewichte,
- NaN/Inf,
- unbekanntes Asset,
- leeres Mapping,
- nicht numerische Gewichte.

Gewichte niemals automatisch normalisieren.

I. Multi-Asset-Daten
- Alle benötigten Assets verwenden denselben gemeinsamen Kalender.
- Fehlt ein gemeinsamer Bewertungszeitpunkt bei einem Asset, wird dieser vor Renditeberechnung aus allen benötigten Reihen entfernt und dokumentiert.
- Nicht benötigte Assets verändern den Kalender nicht.

J. Mehrere Strategien
- Buy-and-Hold und Rebalancing können im selben Run ausgeführt werden.
- Beide besitzen denselben effektiven Kalender.
- `summary.csv` enthält beide Strategien.
- Ergebnisse werden nicht gegenseitig verändert.

K. Trades-/Gewichtsexport
- Spalten exakt prüfen.
- deterministic ordering.
- Gewichte summieren je Datum zu 1.
- Tradegleichung prüfen.
- Output-Hashes im Manifest prüfen.

L. Zukunftsdaten
- Änderung eines späteren Performance-Werts darf keinen früheren Portfolio-, Gewichts- oder Tradezustand verändern.

M. Asset-Reihenfolge
- Eine andere Reihenfolge der Assets in CSV oder JSON darf fachliche Ergebnisse nicht verändern.

N. Regression
- Bestehender künstlicher Buy-and-Hold-Demo-Lauf 100 → 110 → 99 funktioniert unverändert weiter.
- Alle bisherigen Core-Tests bleiben grün.

Weitere sinnvolle Randtests darfst du ergänzen.

Tests nicht abschwächen, um die Implementierung passend erscheinen zu lassen.

--------------------------------------------------
15. DOKUMENTATION
--------------------------------------------------

Aktualisiere:

`documentation/engine/implementation.md`

mit:

- Multi-Asset-Erweiterung,
- Strategiearchitektur,
- genaue Rebalancing-Reihenfolge,
- Semantik von weights_history,
- Semantik von trades,
- Änderungen an `src/funktionen.py`,
- Demo-Rebalancing-Fall,
- weiterhin bestehende Grenzen.

Aktualisiere:

`documentation/engine/testing.md`

mit:

- neu ausgeführten Testbefehlen,
- Gesamtanzahl Tests,
- handrechenbaren Rebalancing-Kontrollfällen,
- tatsächlich ausgeführtem Demo-Lauf,
- geprüfter Kapitalerhaltung,
- Regression des Buy-and-Hold-Core.

Aktualisiere:

`documentation/ai-usage/ai-usage-log.md`

gemäss bestehendem Schema.

--------------------------------------------------
16. SELBSTSTÄNDIGES ARBEITEN
--------------------------------------------------

Innerhalb dieses Auftrags darfst du:

implementieren
→ testen
→ technische Fehler korrigieren
→ erneut testen
→ Dokumentation aktualisieren.

Stoppe nur, wenn eine neue finanzwirtschaftliche oder methodische Entscheidung nötig wird.

Technische Refactorings sind erlaubt, wenn:

- bestehende fachliche Definitionen unverändert bleiben,
- Core-Verhalten erhalten bleibt,
- Tests die Regression absichern,
- Refactoring dokumentiert wird.

--------------------------------------------------
17. NICHT ERLAUBT
--------------------------------------------------

Nicht verändern:

- `notebooks/Analyse.ipynb`
- `notebooks/Theorie.ipynb`
- `methodik.qmd`
- `references.bib`
- `documentation/engine/decisions.md`
- fertige Buchkapitel

Nicht implementieren:

- Trendfolge,
- BIP-Gewichtung,
- reale Datenadapter,
- Live-Downloads,
- FX,
- Transaktionskosten,
- Steuern,
- Inflation,
- Batch,
- Web/API,
- Optimierung,
- reale Hauptversuche.

--------------------------------------------------
18. ABSCHLUSSPRÜFUNG
--------------------------------------------------

Vor Abschluss:

1. vollständige pytest-Suite ausführen,
2. bestehenden Buy-and-Hold-Demo-Lauf ausführen,
3. neuen Rebalancing-Demo-Lauf ausführen,
4. Portfolioverlauf manuell gegen Kontrollrechnung prüfen,
5. weights_history prüfen,
6. trades prüfen,
7. Kapitalerhaltung prüfen,
8. Manifest-/Output-Hashes prüfen,
9. git diff prüfen,
10. geschützte Dateien auf Unverändertheit prüfen,
11. Dokumentation aktualisieren,
12. KI-Log aktualisieren.

Keinen Commit erstellen.

--------------------------------------------------
19. ABSCHLUSSANTWORT
--------------------------------------------------

Berichte am Ende kompakt:

1. welche Dateien erstellt/geändert wurden,
2. welche Core-Komponenten erweitert/refaktoriert wurden,
3. ob `src/funktionen.py` geändert wurde und warum,
4. wie der Rebalancing-Demo-Lauf gestartet wird,
5. die handrechenbaren wichtigsten Demo-Ergebnisse,
6. Anzahl und Ergebnis der tatsächlich ausgeführten Tests,
7. welche zusätzlichen Outputs erzeugt wurden,
8. ob Buy-and-Hold unverändert funktioniert,
9. ob neue fachliche Entscheidungen nötig wurden,
10. ob geschützte Dateien unverändert blieben.

Danach STOPPEN.

Noch nicht mit Trendfolge oder BIP fortfahren.