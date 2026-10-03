# Codex-Prompt: Engine v1 – Trendfolge

**Datum:** 2026-10-04
**Tool:** Codex
**Zweck:** Erweiterung der geprüften Backtesting-Engine um die SMA-basierte Long/Cash-Trendfolgestrategie

## Vollständiger Prompt

Erweitere die bereits geprüfte Backtesting-Engine um die SMA-basierte Long/Cash-Trendfolgestrategie.

Der akzeptierte Ausgangspunkt ist der Tag:

`engine-rebalancing-v0.2.0`

auf Commit:

`37edc79f4211c734423ca89ef3899d1cbc0b81b4`

Bestehender Core, Buy-and-Hold und Rebalancing sind fachlich abgenommen und sollen erweitert, nicht unnötig neu geschrieben werden.

LIES VOR DER IMPLEMENTIERUNG:

- `AGENTS.md`
- `documentation/engine/audit.md`
- `documentation/engine/open-decisions.md`
- `documentation/engine/decisions.md`
- `documentation/engine/implementation.md`
- `documentation/engine/testing.md`
- `notebooks/Analyse.ipynb`, insbesondere Kapitel 5.3 bis 5.9
- `notebooks/Theorie.ipynb`, insbesondere Kapitel 3.12 und 3.13 sowie die relevanten Rendite-/Backtesting-Abschnitte
- `src/funktionen.py`
- den gesamten bestehenden Engine-Code
- die gesamte bestehende Test-Suite

Für diesen Schritt sind insbesondere OD-01, OD-02, OD-03, OD-04, OD-05, OD-07, OD-08 und OD-10 verbindlich.

--------------------------------------------------
ZIEL
--------------------------------------------------

Implementiere:

- getrennte Verwendung von `performance_value` und `signal_value`,
- explizite Wahl der Signalquelle,
- SMA kurz und SMA lang,
- Long/Cash-Signal,
- Warm-up vor dem Untersuchungsbeginn,
- eine Periode Signalverzögerung,
- Cash-Rendite 0,
- standardisierten Trendfolge-Portfolioverlauf,
- `signals.csv`,
- Integration in Multi-Strategy-Runs,
- synthetische Tests und Demo.

Noch NICHT implementieren:

- BIP-/Country-Weighting,
- reale Yahoo-/FRED-Adapter,
- FX,
- verzinstes Cash,
- Long/Short,
- Transaktionskosten,
- Steuern,
- Inflation,
- Batch,
- Web/API,
- Parameteroptimierung,
- Hauptversuch.

--------------------------------------------------
DATENVERTRAG UND SIGNALQUELLE
--------------------------------------------------

Die bestehende Marktstruktur bleibt grundsätzlich:

date
asset_id
performance_value
optional: signal_value

`performance_value` und `signal_value` haben unterschiedliche Aufgaben:

- `performance_value` bestimmt ausschliesslich die tatsächlich erzielte Marktrendite.
- `signal_value` dient ausschliesslich der Berechnung der gleitenden Durchschnitte und Signale.

Die Trendstrategie darf diese Rollen nicht vermischen.

Erweitere die Konfiguration der Trendstrategie um eine explizite Signalquelle.

Bevorzugte Struktur:

"trend": {
  "enabled": true,
  "asset": "TREND_SYNTH",
  "short_window": 2,
  "long_window": 3,
  "signal_lag": 1,
  "signal_source": "signal_value"
}

Unterstützte Signalquellen in Engine v1:

- `"signal_value"`
- `"performance_value"`

`"performance_value"` bedeutet eine ausdrücklich konfigurierte Verwendung der Performance-Reihe als Signalbasis.

Es gibt KEINEN stillen Fallback.

Wenn `signal_source="signal_value"` konfiguriert ist und die Spalte fehlt, wird der Lauf abgelehnt.

Wenn `signal_value` vorhanden, aber für benötigte Beobachtungen leer, NaN oder nicht endlich ist, wird NICHT zeilenweise auf `performance_value` zurückgefallen.

Eine explizite Verwendung von `performance_value` als Signalquelle ist zulässig und muss im Manifest nachvollziehbar bleiben.

--------------------------------------------------
KONFIGURATION UND PARAMETER
--------------------------------------------------

Trend benötigt mindestens:

- `enabled`
- `asset`
- `short_window`
- `long_window`
- `signal_lag`
- `signal_source`

Für Engine v1 gilt:

- Fenster müssen positive ganze Zahlen sein.
- `short_window < long_window`.
- `signal_lag` muss exakt 1 sein.
- Andere Lags werden nicht still interpretiert.
- Long/Short wird nicht unterstützt.
- Cash-Verzinsung wird nicht unterstützt.
- Cash-Rendite ist gemäss OD-05 exakt 0.

Keine fachlichen Defaults für SMA-Fenster.

Die konkreten SMA-Fenster des späteren Hauptversuchs bleiben weiterhin offen.

Die künstlichen Demo-Werte sind keine Versuchsauswahl.

--------------------------------------------------
GEMEINSAMER PERFORMANCE-KALENDER
--------------------------------------------------

Alle aktivierten Strategien desselben Runs müssen weiterhin denselben effektiven Performance-Kalender verwenden.

Die Vereinigung aller Performance-Assets der aktiven Strategien wird gemäss OD-01 vor Renditeberechnung auf gemeinsame Bewertungszeitpunkte ausgerichtet.

Trend darf den Performance-Zeitraum nicht eigenständig verkürzen.

Warm-up-Signaldaten vor dem effektiven Start gehören NICHT zum gemeinsamen Performance-Zeitraum.

Zusätzliche Warm-up-Beobachtungen der Signalreihe dürfen deshalb Buy-and-Hold oder Rebalancing nicht nach hinten verlängern oder den Vergleichsstart verändern.

Wenn für Trend am effektiven Start kein gültiges Signal berechnet werden kann, wird der gesamte Run abgelehnt. Der Trendlauf darf nicht still später beginnen.

--------------------------------------------------
SMA-WARM-UP – OD-04
--------------------------------------------------

Für den SMA dürfen historische Signalwerte VOR dem eigentlichen Untersuchungsbeginn verwendet werden.

Sie dienen ausschliesslich der Signalberechnung.

Sie dürfen:

- keine Portfoliorendite vor dem Untersuchungsbeginn erzeugen,
- das Startkapital nicht verändern,
- nicht als zusätzliche Performanceperioden gezählt werden,
- nicht in Volatilität, Sharpe oder andere Performancekennzahlen eingehen.

Am effektiven Startdatum muss bereits ein vollständig definierter kurzer und langer SMA vorhanden sein.

Für ein `long_window = N` werden somit genügend Signalbeobachtungen bis einschliesslich des effektiven Startdatums benötigt.

Sind nicht genügend gültige Beobachtungen vorhanden, wird der Lauf abgelehnt.

Ein undefinierter SMA wird NICHT als Signal 0 bzw. Cash interpretiert.

Keine fehlenden Signalwerte auffüllen oder interpolieren.

--------------------------------------------------
SIGNALDEFINITION
--------------------------------------------------

Die theoretische Definition ist verbindlich:

Wenn:

SMA_short(t) > SMA_long(t)

dann:

signal(t) = 1

sonst:

signal(t) = 0

Bei Gleichheit gilt also Cash / Signal 0.

Nur vollständig definierte SMA-Werte dürfen ein Signal erzeugen.

Keine Optimierung, keine Toleranzzone und kein zusätzlicher Filter.

--------------------------------------------------
ZEITLICHE LOGIK UND SIGNAL-LAG
--------------------------------------------------

Kein Look-ahead.

Die Marktrendite für die Periode:

t-1 → t

darf nur von einem Signal beeinflusst werden, das spätestens am Ende von t-1 bekannt war.

Die verbindliche Formel entspricht deshalb konzeptionell:

strategy_return(t)
=
position(t) * market_return(t)

mit:

position(t)
=
signal(t-1)

für die Renditeperiode, die bei t endet.

Das am effektiven Startdatum berechnete Signal entscheidet somit über die ERSTE Renditeperiode NACH dem Startdatum.

Ein Signal am Datum t darf niemals die bereits vergangene Rendite beeinflussen, die bei t endet.

`signal_lag = 1` ist verbindlich.

--------------------------------------------------
LONG/CASH
--------------------------------------------------

Positionen:

- 1 = vollständig Long in der konfigurierten Anlage
- 0 = vollständig Cash

Kein Short.

Wenn Position = 1:

strategy_return = market_return

Wenn Position = 0:

strategy_return = 0

Cash wird nicht verzinst.

Die Risk-Free-Reihe für Sharpe bleibt davon vollständig getrennt.

Sie darf nicht als Cash-Rendite verwendet werden.

--------------------------------------------------
PORTFOLIOVERLAUF
--------------------------------------------------

Die gemeinsame Struktur bleibt:

date
strategy
portfolio_value
period_return
drawdown

Die Trendstrategie beginnt mit derselben expliziten Startzeile wie die anderen Strategien:

- `portfolio_value = start_capital`
- `period_return = nicht beobachtet`
- `drawdown = 0`

Für jede folgende Performanceperiode:

1. Berechne die tatsächliche Marktrendite aus `performance_value`.
2. Verwende ausschliesslich das am vorherigen Bewertungstermin bekannte Signal als Position.
3. Bei Long wird die Marktrendite verdient.
4. Bei Cash beträgt die Strategierendite 0.
5. Aktualisiere den Portfoliowert.
6. Berechne Drawdown aus dem tatsächlichen Trendportfolio.

Keine Warm-up-Rendite darf in den Verlauf gelangen.

--------------------------------------------------
SIGNALS.CSV
--------------------------------------------------

Implementiere bei mindestens einer Trendstrategie:

`signals.csv`

mit exakt:

date
strategy
asset_id
signal
position
signal_value
sma_short
sma_long

Semantik:

`signal`
= am angegebenen Bewertungsdatum aus den zu diesem Zeitpunkt verfügbaren SMA-Werten berechnetes Signal.

`position`
= Position, welche die Renditeperiode verdient hat, die an diesem Datum endet.

Daraus folgt:

- In der Startzeile ist `position` nicht beobachtet / leer, weil im Untersuchungszeitraum noch keine Renditeperiode geendet hat.
- Ab der zweiten Bewertungszeile gilt `position(t) = signal(t-1)`.
- Das Signal der letzten Bewertungszeile darf berechnet und dokumentiert werden, auch wenn im Untersuchungszeitraum keine folgende Renditeperiode mehr existiert.

`signal_value`, `sma_short` und `sma_long` beziehen sich auf das angegebene Datum.

Für ALLE exportierten Untersuchungsdaten der Trendstrategie müssen beide SMAs vollständig definiert sein, weil der Warm-up dies sicherstellt.

Warm-up-Daten vor dem effektiven Start werden NICHT als zusätzliche Zeilen in `signals.csv` exportiert.

Die Tabellenreihenfolge muss deterministisch sein.

--------------------------------------------------
BESTEHENDE FUNKTION `trendfolge`
--------------------------------------------------

`src/funktionen.py` bleibt mathematischer Ausgangspunkt.

Der Audit hat bereits gezeigt, dass die bisherige Funktion:

- Signal- und Performance-Reihe nicht trennt,
- fehlende Werte per `dropna()` entfernt,
- bei noch nicht definiertem SMA implizit Signal 0 erzeugt,
- Fenster nicht vollständig validiert.

Diese Eigenschaften dürfen NICHT unverändert in die Engine übernommen werden.

Refaktoriere die bestehende Trendlogik transparent, soweit nötig.

Bevorzugt soll die mathematische SMA-/Signaldefinition an EINER Stelle liegen.

Es ist zulässig:

- einen kleinen gemeinsamen SMA-/Signal-Helper in `src/funktionen.py` einzuführen,
- `trendfolge()` auf diesen Helper aufzubauen,
- die Engine-Strategie denselben Helper für die Signalerzeugung verwenden zu lassen.

Vermeide zwei voneinander unabhängige Implementierungen derselben SMA-Signalformel.

Die tatsächliche Kombination von Signal mit einer getrennten `performance_value`-Rendite gehört in die Trendstrategie.

Jede Änderung an `src/funktionen.py` dokumentieren und gezielt testen.

Keine Änderung am geschützten Theorie-Notebook.

--------------------------------------------------
MULTI-STRATEGY
--------------------------------------------------

Trend muss zusammen mit:

- Buy-and-Hold
- Rebalancing

im selben Run ausführbar sein.

Alle verwenden denselben Performance-Kontext und denselben effektiven Performance-Kalender.

Die Trend-Warm-up-Historie ist nur zusätzlicher Signal-Kontext.

Die Ausführung einer Strategie darf keine Daten einer anderen Strategie verändern.

`summary.csv` enthält eine Zeile pro ausgeführter Strategie.

`portfolio_history.csv` enthält alle Strategien in deterministischer Reihenfolge.

Risk-Free wird für Sharpe weiterhin identisch auf dieselben Performanceperioden ausgerichtet.

--------------------------------------------------
EXPORT
--------------------------------------------------

Bestehende Outputs bleiben:

- `portfolio_history.csv`
- `summary.csv`
- `data_quality.json`
- `run_manifest.json`

Rebalancing behält bei Bedarf:

- `weights_history.csv`
- `trades.csv`

Trend ergänzt bei Bedarf:

- `signals.csv`

`signals.csv` wird nur erzeugt, wenn mindestens eine Strategie tatsächlich Signaldaten besitzt.

Alle erzeugten Ergebnisdateien müssen weiterhin im Manifest mit SHA-256 erfasst sein.

Ein Buy-and-Hold-/Rebalancing-Run ohne Trend darf nicht künstlich eine leere `signals.csv` erhalten.

--------------------------------------------------
DATENQUALITÄT UND MANIFEST
--------------------------------------------------

Erweitere die Qualitäts-/Provenienzdokumentation für Trend mindestens um:

- Trend-Asset,
- verwendete Signalquelle,
- Anzahl verfügbarer Warm-up-Beobachtungen,
- benötigtes langes Fenster,
- tatsächlich verwendeten Warm-up-Bereich,
- effektives Startdatum,
- Bestätigung, dass am Start ein gültiges Signal vorlag.

Die vollständig aufgelöste Konfiguration im Manifest muss Signalquelle, Fenster und Lag enthalten.

Keine Demo-/Default-Parameter als Versuchswerte deklarieren.

--------------------------------------------------
SYNTHETISCHE TREND-DEMO
--------------------------------------------------

Erstelle einen kleinen künstlichen Demo-Fall:

`configs/demo_trend.json`

und passende künstliche Daten.

Der Datensatz soll:

- ausreichende Warm-up-Beobachtungen vor dem Untersuchungsbeginn enthalten,
- `performance_value` und `signal_value` bewusst unterschiedlich machen,
- mindestens einen Wechsel Cash → Long oder Long → Cash enthalten,
- mindestens eine Cash-Periode enthalten,
- mindestens eine Long-Periode enthalten,
- die Lag-Logik eindeutig von Hand überprüfbar machen,
- keine realen Wertpapiere verwenden.

Nutze kleine SMA-Fenster, beispielsweise 2 und 3, ausschliesslich für die technische Demo.

Diese Werte sind KEINE Parameterentscheidung für den Hauptversuch.

Die Demo soll möglichst auf einem regelmässigen kleinen Kalender liegen, damit auch die gemeinsamen Kennzahlen technisch geprüft werden können.

--------------------------------------------------
VERPFLICHTENDE TESTS
--------------------------------------------------

Die gesamte bisherige Suite muss unverändert grün bleiben.

Ergänze mindestens folgende Trend-Prüfungen.

A – SMA-Handrechnung

Mit kleinen künstlichen Signalwerten SMA kurz und SMA lang unabhängig von Hand nachrechnen.

Signal = 1 nur bei `short > long`.

Gleichheit ergibt 0.

B – Fensterprüfung

Ablehnen:

- short <= 0
- long <= 0
- short >= long
- Bool-Werte
- nicht-ganzzahlige Fenster
- fehlende Fenster

C – Warm-up

- genügend Vorlauf → am Start beide SMAs gültig
- zu wenig Vorlauf → kompletter Run Fehler
- Warm-up verändert Startkapital nicht
- Warm-up erzeugt keine zusätzliche Performance
- Warm-up erscheint nicht als zusätzliche Portfoliozeile

D – Getrennte Signal-/Performance-Reihen

Erstelle bewusst unterschiedliche Reihen.

Zeige:

- Signal wird aus `signal_value` berechnet.
- Rendite wird aus `performance_value` berechnet.
- Änderung nur von `signal_value` kann Signale ändern, ohne Marktrenditen selbst zu verändern.
- Änderung nur eines späteren Performance-Werts darf frühere Signale nicht ändern.

E – Explizite Signalquelle

- `signal_source="signal_value"` funktioniert bei vollständiger Spalte.
- fehlende `signal_value`-Spalte wird dabei abgelehnt.
- einzelne fehlende `signal_value` wird abgelehnt.
- kein zeilenweiser Fallback.
- `signal_source="performance_value"` funktioniert ausdrücklich.
- unbekannte Signalquelle wird abgelehnt.

F – Signal-Lag

Beweise mit einem handrechenbaren Beispiel:

- Signal an t wirkt NICHT auf Rendite bis t.
- Signal an t wirkt auf Rendite t → t+1.
- Kein Look-ahead.

G – Long/Cash

- Position 1 übernimmt exakt die Marktrendite.
- Position 0 erzeugt exakt Strategierendite 0.
- Negative Marktrendite während Cash verändert das Portfolio nicht.
- Positive Marktrendite während Cash verändert das Portfolio ebenfalls nicht.
- Kein Short.

H – Risk-Free-Trennung

Ändere nur die Risk-Free-Reihe.

Dadurch darf sich der Trend-Portfolioverlauf nicht verändern.

Nur Sharpe darf sich ändern.

I – signals.csv

Prüfe:

- exakte Spalten,
- deterministische Reihenfolge,
- Start-`position` leer,
- ab zweiter Zeile `position(t)=signal(t-1)`,
- signal nur 0 oder 1,
- SMA-Werte im Untersuchungszeitraum vollständig,
- keine Warm-up-Zeilen,
- Signalwerte/SMAs passen zum Datum,
- Datei-Hash im Manifest korrekt.

J – Multi-Strategy

Buy-and-Hold, Rebalancing und Trend können im selben Run laufen.

Alle Portfolioverläufe verwenden exakt denselben Performance-Kalender.

Trend-Warm-up verändert die anderen Strategien nicht.

`summary.csv` enthält alle Strategien genau einmal.

K – Zukunftsdaten / Look-ahead

Ändere einen Signalwert NACH einem früheren Bewertungsdatum.

Frühere:

- Signale,
- Positionen,
- Portfolioergebnisse

dürfen sich nicht verändern.

Ändere einen Performance-Wert in einer späteren Periode.

Frühere Portfolioergebnisse dürfen sich nicht verändern.

L – Fehlwerte

NaN/Inf bzw. nicht numerische Werte in benötigten Signalbeobachtungen werden abgelehnt.

Keine Interpolation.
Kein Forward-Fill.
Kein `dropna()` zur stillen Kalenderverkürzung.

M – Regression

Alle bisherigen Core- und Rebalancing-Tests bleiben grün.

Buy-and-Hold-Demo bleibt unverändert.

Rebalancing-Demo bleibt unverändert.

Weitere sinnvolle Randtests darfst du ergänzen.

Tests dürfen nicht abgeschwächt werden, damit die Implementierung grün erscheint.

--------------------------------------------------
DOKUMENTATION
--------------------------------------------------

Aktualisiere:

`documentation/engine/implementation.md`

Dokumentiere mindestens:

- Trendstrategie,
- Trennung performance_value / signal_value,
- Warm-up,
- Signalquelle,
- SMA-Definition,
- Lag-Semantik,
- Long/Cash,
- Cash-Rendite 0,
- Semantik von signals.csv,
- Änderungen an `src/funktionen.py`,
- künstlichen Demo-Fall,
- weiterhin bestehende Grenzen.

Aktualisiere:

`documentation/engine/testing.md`

Dokumentiere:

- tatsächlich ausgeführte Testbefehle,
- Gesamtzahl Tests,
- handrechenbare SMA-/Lag-Kontrollfälle,
- Demo-Lauf,
- Regression von Core und Rebalancing,
- verbleibende Grenzen.

Aktualisiere:

`documentation/ai-usage/ai-usage-log.md`

gemäss bestehendem Schema.

--------------------------------------------------
SELBSTSTÄNDIGES ARBEITEN
--------------------------------------------------

Innerhalb dieses bestätigten Auftrags darfst du:

implementieren
→ testen
→ technische Fehler korrigieren
→ erneut testen
→ dokumentieren.

Stoppe jedoch, wenn eine NEUE finanzwirtschaftliche oder methodische Entscheidung erforderlich wird.

Technische Refactorings sind erlaubt, wenn fachliche Definitionen unverändert bleiben und Regressionstests bestehen.

--------------------------------------------------
NICHT ERLAUBT
--------------------------------------------------

Nicht verändern:

- `notebooks/Analyse.ipynb`
- `notebooks/Theorie.ipynb`
- `methodik.qmd`
- `references.bib`
- `documentation/engine/decisions.md`
- fertige Buchkapitel

Nicht implementieren:

- BIP-/Country-Weighting,
- reale Datenadapter,
- Live-Downloads,
- FX,
- verzinstes Cash,
- Long/Short,
- Kosten,
- Steuern,
- Inflation,
- Batch,
- Web/API,
- Optimierung,
- reale Hauptuntersuchung.

--------------------------------------------------
ABSCHLUSSPRÜFUNG
--------------------------------------------------

Vor Abschluss:

- vollständige pytest-Suite ausführen,
- Buy-and-Hold-Demo erneut ausführen,
- Rebalancing-Demo erneut ausführen,
- neue Trend-Demo ausführen,
- SMA-Werte manuell kontrollieren,
- Signal-Lag manuell kontrollieren,
- Long-/Cash-Renditen kontrollieren,
- `signals.csv` prüfen,
- alle Output-Hashes prüfen,
- Manifest prüfen,
- git diff prüfen,
- geschützte Dateien auf Unverändertheit prüfen,
- Dokumentation aktualisieren,
- KI-Log aktualisieren.

Keinen Commit erstellen.

--------------------------------------------------
ABSCHLUSSANTWORT
--------------------------------------------------

Berichte am Ende kompakt:

1. welche Dateien erstellt/geändert wurden,
2. welche bestehenden Komponenten refaktoriert wurden,
3. ob und warum `src/funktionen.py` geändert wurde,
4. genaue Semantik von Signal und Position,
5. wie der Trend-Demo-Lauf gestartet wird,
6. die wichtigsten handrechenbaren Demo-Ergebnisse,
7. Anzahl und Ergebnis der tatsächlich ausgeführten Tests,
8. ob Core und Rebalancing unverändert funktionieren,
9. ob neue fachliche Entscheidungen nötig wurden,
10. ob geschützte Dateien unverändert blieben.

Danach STOPPEN.

Noch nicht mit BIP fortfahren.