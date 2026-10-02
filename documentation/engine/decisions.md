# Verbindliche Entscheidungen für Backtesting-Engine v1

**Datum:** 2026-10-02  
**Grundlage:** `documentation/engine/audit.md` und `documentation/engine/open-decisions.md`

Dieses Dokument löst die BLOCKING-Entscheidungen OD-01 bis OD-13 vor der Implementierung der Engine auf.

Die Entscheidungen gelten für Engine v1. Änderungen daran dürfen während der Implementierung nicht still vorgenommen werden. Falls sich eine Regel als technisch oder fachlich problematisch erweist, muss dies dokumentiert und vor einer methodischen Änderung erneut entschieden werden.

## OD-01 – Datenkalender und gemeinsame Perioden

Mehrere für einen Lauf benötigte Performance-Reihen werden vor der Renditeberechnung auf gemeinsame tatsächlich vorhandene Bewertungszeitpunkte ausgerichtet.

Es erfolgt kein automatisches Forward-Fill und keine Interpolation von Marktwerten.

Nicht gemeinsame Zeitpunkte, die bei der Ausrichtung entfernt werden, müssen im Datenbericht dokumentiert werden.

Ein fehlender numerischer Wert (`NaN`) innerhalb einer vorhandenen Beobachtung gilt als Datenfehler und darf nicht still ersetzt werden.

Die Engine muss nicht selbst erraten, ob ein nicht vorhandener Handelstag auf einen Feiertag oder einen Datenfehler zurückzuführen ist.

## OD-02 – Startbewertung und erste Rendite

Jeder Portfolioverlauf beginnt mit einer expliziten Startbewertung:

- `portfolio_value = start_capital`
- `period_return = null / nicht beobachtet`
- `drawdown = 0`

Diese Startzeile ist kein zusätzlicher Nullrendite-Datenpunkt und wird nicht in Mittelwert, Volatilität oder Sharpe Ratio einbezogen.

Der effektive Start ist der erste gemeinsame gültige Bewertungszeitpunkt am oder nach dem gewünschten Startdatum.

Das effektive Ende ist der letzte gemeinsame gültige Bewertungszeitpunkt am oder vor dem gewünschten Enddatum.

Die tatsächlich verwendeten Grenzen werden im Run-Manifest gespeichert.

## OD-03 – Annualisierung

`periods_per_year` ist eine explizite Konfigurationseinstellung und wird im Run-Manifest gespeichert.

Die Engine wählt diesen Wert nicht still aufgrund einer Vermutung.

Annualisierte Rendite, Volatilität und Sharpe Ratio dürfen nur berechnet werden, wenn die verwendete Periodenlogik mit dem angegebenen Wert vereinbar ist.

Eine spätere kalenderzeitbasierte CAGR-Methode ist keine automatische Ersatzmethode.

## OD-04 – SMA-Anlaufphase

Für die Trendfolgestrategie werden historische Signalwerte vor dem eigentlichen Untersuchungsbeginn als Warm-up verwendet.

Die Warm-up-Daten dienen ausschliesslich zur Berechnung der SMA-Werte und Handelssignale. Sie gehören nicht zur ausgewerteten Portfolioperformance.

Am effektiven Startdatum muss ein gültiges SMA-Signal bestimmbar sein, damit dieses für die folgende Renditeperiode verwendet werden kann.

Sind nicht genügend historische Beobachtungen für das lange SMA-Fenster vorhanden, wird der Lauf abgelehnt.

Die Engine erzeugt aus einem nicht definierten SMA keine künstliche Cash-Position.

## OD-05 – Cash bei der Trendfolge

Cash wird in Engine v1 bei der Trendfolgestrategie unverzinst behandelt.

Die Cash-Rendite beträgt deshalb 0.

Die für die Sharpe Ratio verwendete risikofreie Rendite ist eine separate Vergleichsreihe und wird nicht automatisch als Rendite der Cash-Position verwendet.

Eine verzinste Cash-Variante wäre eine spätere methodische Erweiterung.

## OD-06 – Jährliches Rebalancing

Ein Rebalancing-Portfolio beginnt am Startzeitpunkt mit den konfigurierten Zielgewichten.

Zwischen den Rebalancing-Zeitpunkten verändern sich die Gewichte durch die unterschiedlichen Renditen der Anlagen.

Das jährliche Rebalancing findet am letzten gemeinsamen Bewertungszeitpunkt eines Kalenderjahres statt.

Zuerst wird die Rendite der bis zu diesem Zeitpunkt gehaltenen Positionen verbucht und die daraus entstandene Gewichtungsdrift bestimmt.

Anschliessend werden die Positionen auf die Zielgewichte zurückgesetzt. Diese neuen Gewichte gelten für die folgende Renditeperiode.

Die festen Zielgewichte von 60/40 dürfen deshalb nicht in jeder einzelnen Periode neu angewendet werden.

Wenn nach dem letzten möglichen Rebalancing-Zeitpunkt keine weitere Renditeperiode im Untersuchungszeitraum liegt, muss kein wirtschaftlich wirkungsloser Abschlusstrade erzwungen werden.

## OD-07 – Risikofreie Rendite

Die eigentliche Engine arbeitet mit bereits normalisierten risikofreien Periodenrenditen.

Diese müssen dieselben Periodengrenzen besitzen wie die Portfoliorenditen.

Der verarbeitete Risk-Free-Datensatz muss mindestens die Identität der Reihe und die zugehörige Periodenrendite eindeutig enthalten.

Die Umrechnung eines veröffentlichten Jahreszinses oder einer anderen Zinsnotierung in eine Periodenrendite erfolgt vor der eigentlichen Strategieauswertung und muss durch den jeweiligen Datenadapter bzw. die Datenaufbereitung dokumentiert werden.

Es darf keine fehlende risikofreie Rendite automatisch durch 0 ersetzt werden.

## OD-08 – Sharpe Ratio

Für Engine v1 gilt die im Theoriekapitel explizit angegebene Definition:

`Sharpe = mean(r - rf) / std(r - rf) * sqrt(periods_per_year)`

Dabei wird die Stichproben-Standardabweichung der periodischen Überschussrenditen mit `ddof=1` verwendet.

Anlage- und risikofreie Rendite müssen vollständig, endlich und exakt auf dieselben Perioden ausgerichtet sein.

Der Audit hat gezeigt, dass das bisher verwendete QuantStats-Verhalten bei bestimmten Eingaben nicht zuverlässig der definierten Eingabesemantik entspricht.

Die bestehende Funktion `sharpe_ratio()` darf deshalb transparent korrigiert werden, damit sie exakt die theoretisch festgelegte Formel implementiert.

Die Änderung muss dokumentiert und mit unabhängigen synthetischen Tests geprüft werden.

## OD-09 – Drawdown

Der Startwert des Portfolios ist der anfängliche High-Water-Mark.

Ein Verlust unmittelbar in der ersten Renditeperiode muss deshalb bereits als negativer Drawdown erscheinen.

Die bestehenden Funktionen `drawdown()` und `maximum_drawdown()` dürfen transparent korrigiert oder über einen klar dokumentierten Wrapper so integriert werden, dass diese Definition erfüllt wird.

Die Startbewertung darf dabei nicht als zusätzliche beobachtete Nullrendite in die statistische Stichprobe eingehen.

## OD-10 – Währung

Engine v1 führt keine automatische Wechselkursumrechnung und keine Währungsabsicherung durch.

Alle gemeinsam verglichenen Performance-Reihen müssen bereits in einer zur konfigurierten Basiswährung kompatiblen Darstellung vorliegen.

Die Währung wird über die Metadaten geprüft.

Bei nicht kompatiblen Reihen wird der Lauf abgelehnt.

Eine spätere FX-Unterstützung benötigt einen eigenen Datenvertrag und eine separate methodische Entscheidung.

## OD-11 – Ländergewichtungsstrategie

Das Modul `country_weighting` implementiert in Engine v1 die im Theoriekapitel beschriebene reine BIP-Ländergewichtung.

Die Ländergewichte ergeben sich aus:

`GDP_country / sum(GDP_all_included_countries)`

Für jedes berücksichtigte Land muss ein eindeutiger investierbarer Länderproxy konfiguriert sein.

Innerhalb dieses Länderproxys wird keine eigene zusätzliche Unternehmensgewichtung durch die Engine durchgeführt; der Proxy muss fachlich zur gewünschten Binnenlandabbildung passen.

Der in der Methodik erwähnte Gerd-Kommer-ETF mit kombinierter Marktkapitalisierungs-, BIP- und Faktorlogik wird nicht still mit dieser reinen BIP-Strategie gleichgesetzt.

Eine eigene gemischte Kommer-Strategie wäre eine separate Erweiterung.

## OD-12 – BIP-Verfügbarkeit und Aktualisierung

Für eine historische BIP-Entscheidung dürfen nur Informationen verwendet werden, die am jeweiligen Entscheidungszeitpunkt verfügbar waren.

Die Makrodaten müssen deshalb eine nachvollziehbare Verfügbarkeitsinformation besitzen.

Am jeweiligen jährlichen Entscheidungszeitpunkt wird der jüngste gemeinsame BIP-Bezugszeitraum verwendet, für den für alle konfigurierten Länder zulässige Daten verfügbar sind.

Länder mit fehlenden Werten werden nicht still aus dem Nenner entfernt.

Falls für mindestens ein benötigtes Land kein gültiger gemeinsamer Datenstand verfügbar ist, wird der Lauf abgelehnt.

Gewichtsermittlung und Portfolioausführung sind zeitlich getrennt. Die am jährlichen Rebalancing-Zeitpunkt mit damals verfügbaren BIP-Daten bestimmten Zielgewichte gelten für die folgende Renditeperiode.

Heute bekannte revidierte Werte dürfen nicht rückwirkend als historisch bekannte Werte behandelt werden, sofern ihre damalige Verfügbarkeit nicht nachvollziehbar belegt werden kann.

Die konkrete BIP-Quelle und gegebenenfalls ein später begründeter Veröffentlichungslag werden erst vor dem Hauptversuch festgelegt.

## OD-13 – Gewichte und Kapitalmodell

Die allgemeine Portfolio-Engine v1 unterstützt vollständig investierte Long-only-Portfolios.

Für allgemeine Zielgewichte gilt:

- jedes Gewicht ist grösser oder gleich 0,
- kein Short,
- kein Hebel,
- die Summe der Gewichte beträgt innerhalb einer kleinen numerischen Toleranz 1.

Buy-and-Hold einer einzelnen Anlage verwendet Gewicht 1.

Nicht investiertes Restkapital darf nicht still entstehen.

Die Long/Cash-Logik der Trendfolgestrategie ist ein ausdrücklich definierter eigener Strategiezustand und erweitert das allgemeine Portfolio-Gewichtsmodell nicht automatisch um frei konfigurierbares Rest-Cash.

## Noch nicht festgelegte Versuchswerte

OD-14 bis OD-18 bleiben bewusst offen, weil sie die allgemeine Engine nicht blockieren:

- konkrete Anlagen, Indizes und Länderproxies,
- endgültiger Untersuchungszeitraum und Startkapital,
- konkrete risikofreie Serie,
- konkrete SMA-Fenster und Signalreihe,
- konkrete BIP-Datenquelle und Länderabdeckung.

Diese Werte werden nach Implementierung und Prüfung der allgemeinen Engine festgelegt und vor dem Hauptversuch eingefroren.

## Wissenschaftliche Zusatzanalysen

OD-19 wird für Engine v1 so behandelt, dass zunächst der in Analyse 5.7 definierte Kernoutput implementiert wird.

Zusätzliche Analysen wie Erholungsdauer, Krisenphasen, positive/negative Phasen oder weitere Robustheitsuntersuchungen werden später separat definiert und dürfen nicht nachträglich anhand besonders günstiger Ergebnisse ausgewählt werden.