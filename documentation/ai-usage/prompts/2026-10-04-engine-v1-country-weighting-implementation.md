# Codex-Prompt: Engine v1 – BIP-/Ländergewichtung

**Datum:** 2026-10-04
**Tool:** Codex
**Zweck:** Erweiterung der geprüften Backtesting-Engine um eine zeitlich korrekte BIP-basierte Ländergewichtung

## Vollständiger Prompt

Erweitere die bereits geprüfte Backtesting-Engine um die BIP-basierte Ländergewichtungsstrategie.

Der akzeptierte Ausgangspunkt ist der Tag:

`engine-trend-v0.3.0`

auf Commit:

`c101ca558e60228d6e1807a0d192df11d3d5c49f`

Core, Buy-and-Hold, Multi-Asset-Rebalancing und SMA-Trendfolge sind fachlich abgenommen und sollen erweitert, nicht unnötig neu geschrieben werden.

LIES VOR DER IMPLEMENTIERUNG:

- `AGENTS.md`
- `documentation/engine/audit.md`
- `documentation/engine/open-decisions.md`
- `documentation/engine/decisions.md`
- `documentation/engine/implementation.md`
- `documentation/engine/testing.md`
- `notebooks/Analyse.ipynb`, insbesondere Kapitel 5.3 bis 5.9
- `notebooks/Theorie.ipynb`, insbesondere Kapitel 3.11 und 3.13 sowie Rebalancing/Portfolioabschnitte
- `src/funktionen.py`
- den gesamten bestehenden Engine-Code
- die gesamte bestehende Test-Suite

Für diesen Schritt sind insbesondere OD-01, OD-02, OD-06, OD-10, OD-11, OD-12 und OD-13 verbindlich.

--------------------------------------------------
ZIEL
--------------------------------------------------

Implementiere die in Theorie und `decisions.md` festgelegte reine BIP-Ländergewichtung.

Die Strategie soll:

- Länder anhand damals verfügbarer BIP-Daten gewichten,
- pro Land genau einen explizit konfigurierten investierbaren Proxy verwenden,
- historische Verfügbarkeit berücksichtigen,
- Revisionen zeitlich korrekt behandeln,
- die anfängliche Allokation am effektiven Start bestimmen,
- Zielgewichte bei tatsächlichen jährlichen Rebalancing-Ereignissen neu bestimmen,
- dieselbe Portfolio-/Drift-/Rebalancing-Logik wie die bereits geprüfte Rebalancing-Strategie verwenden,
- `weights_history` und `trades` in die bestehenden gemeinsamen Outputs integrieren,
- ihre verwendeten Makrodaten vollständig nachvollziehbar dokumentieren.

Noch NICHT implementieren:

- die gemischte Gerd-Kommer-ETF-Logik,
- Faktorgewichtung,
- eigene Marktkapitalisierungsgewichtung,
- reale BIP-Downloads,
- World-Bank-/FRED-/OECD-Liveadapter,
- reale Länder- oder ETF-Auswahl,
- FX-Konvertierung,
- Kosten,
- Steuern,
- Inflation,
- Batch,
- Web/API,
- Parameteroptimierung,
- Hauptversuch.

--------------------------------------------------
1. FACHLICHER UMFANG
--------------------------------------------------

OD-11 ist verbindlich.

Für konfigurierte Länder c gilt zu einem Entscheidungszeitpunkt:

weight_c
=
GDP_c / sum(GDP_all_configured_countries)

Die Engine berechnet ausschliesslich diese Ländergewichtung.

Für jedes Land wird genau ein explizit konfigurierter investierbarer Asset-Proxy verwendet.

Innerhalb des Länderproxies wird keine zusätzliche Unternehmensgewichtung durch die Engine vorgenommen.

Der vorhandene Inhalt des Länderproxies ist Teil der späteren realen Datenauswahl und nicht Aufgabe dieses Implementierungsschritts.

Keine Gleichsetzung mit einem bestehenden Gerd-Kommer-ETF.

--------------------------------------------------
2. MAKRODATENVERTRAG
--------------------------------------------------

Unterstütze lokale Makrodaten entsprechend Analyse 5.3.7:

period
country
indicator
value
unit
available_from

Für die BIP-Strategie von Engine v1 gilt:

- `period` ist ein vierstelliges Referenzjahr `YYYY`.
- `country` ist eine nicht leere stabile Länderkennung.
- `indicator` ist eine nicht leere Kennung des verwendeten BIP-Indikators.
- `value` muss numerisch, endlich und strikt positiv sein.
- `unit` muss eine nicht leere Einheit/Bedeutung besitzen.
- `available_from` ist ein tatsächliches Datum im Format `YYYY-MM-DD`, ab dem genau diese gespeicherte Datenversion historisch als verfügbar gilt.

Keine fehlenden Werte.
Kein Forward-Fill.
Keine Interpolation.
Keine automatische Renormierung wegen fehlender Länder.

Zusätzliche Länder, Indikatoren oder Perioden in der Datei dürfen die konfigurierte Strategie nicht beeinflussen.

--------------------------------------------------
3. HISTORISCHE VERSIONEN / REVISIONEN
--------------------------------------------------

OD-12 ist verbindlich.

Eine Makrodatei darf mehrere Versionen desselben:

country + indicator + period + unit

enthalten, sofern sie unterschiedliche `available_from`-Daten besitzen.

Für einen Entscheidungszeitpunkt D gilt:

Nur Zeilen mit

available_from <= D

dürfen verwendet werden.

Existieren für denselben:

country + indicator + period + unit

mehrere zu D verfügbare Versionen, wird diejenige mit dem spätesten `available_from` verwendet.

Damit kann eine damals bereits veröffentlichte Revision frühere Werte ersetzen.

Eine Revision mit:

available_from > D

darf die Entscheidung bei D niemals beeinflussen.

Zwei unterschiedliche Werte mit exakt demselben vollständigen Schlüssel einschliesslich `available_from` sind mehrdeutig und müssen abgelehnt werden.

Keine heute bekannte Revision darf mit einem künstlich zurückdatierten Veröffentlichungsdatum versehen oder von der Engine als historisch bekannt angenommen werden.

Die Engine kann die Richtigkeit der gelieferten `available_from`-Information nicht aus den Zahlen selbst beweisen. Sie muss diese Provenienz lediglich konsequent verwenden und dokumentieren.

--------------------------------------------------
4. AUSWAHL DES GEMEINSAMEN BIP-BEZUGSJAHRES
--------------------------------------------------

Zu jedem tatsächlichen Entscheidungszeitpunkt:

1. Betrachte nur den konfigurierten `indicator` und die konfigurierte `unit`.
2. Betrachte nur Versionen mit `available_from <= decision_date`.
3. Bestimme für jedes Land die zu diesem Zeitpunkt verfügbaren Referenzjahre.
4. Ermittle die Schnittmenge der Referenzjahre aller konfigurierten Länder.
5. Wähle das jüngste gemeinsame Referenzjahr.
6. Wähle je Land für genau dieses Referenzjahr die zuletzt bis zum Entscheidungszeitpunkt verfügbare Version.
7. Berechne daraus die BIP-Zielgewichte.

Beispiel:

Land A besitzt schon BIP 2020.
Land B besitzt nur BIP bis 2019.

Dann darf nicht A=2020 und B=2019 kombiniert werden.

Das jüngste gemeinsame Referenzjahr ist 2019.

Wenn kein gemeinsames gültiges Referenzjahr vorhanden ist, wird der gesamte Run abgelehnt.

Länder mit fehlenden Werten werden nicht aus dem Nenner entfernt.

--------------------------------------------------
5. ANFÄNGLICHE ALLOKATION
--------------------------------------------------

Die anfängliche Länderallokation ist ebenfalls eine historische Entscheidung.

Am effektiven Startdatum wird dieselbe As-of-Regel angewendet:

decision_date = effektives Startdatum

Es wird das jüngste gemeinsame BIP-Referenzjahr verwendet, das für alle konfigurierten Länder an diesem Datum bereits verfügbar war.

Aus diesen Werten werden die anfänglichen Zielgewichte berechnet.

Das Startkapital wird entsprechend diesen Gewichten investiert.

Diese anfängliche Allokation ist KEIN Rebalancing-Trade.

Falls am effektiven Startdatum keine vollständige zulässige BIP-Entscheidung möglich ist, wird der Lauf abgelehnt.

Keine Nutzung später veröffentlichter Daten für die Startallokation.

--------------------------------------------------
6. JÄHRLICHE BIP-AKTUALISIERUNG
--------------------------------------------------

OD-06 und OD-12 gelten gemeinsam.

Das Portfolio driftet zwischen Rebalancing-Terminen.

Am letzten gemeinsamen Bewertungszeitpunkt eines Kalenderjahres wird nur dann eine neue BIP-Entscheidung ausgeführt, wenn danach noch mindestens eine weitere Renditeperiode existiert.

Reihenfolge:

gehaltene Positionen verdienen die Rendite bis zum Bewertungstermin
→ Gewichtungsdrift bestimmen
→ BIP-Daten auswählen, die an diesem Datum bereits verfügbar waren
→ jüngstes gemeinsames BIP-Referenzjahr bestimmen
→ neue BIP-Zielgewichte berechnen
→ Rebalancing durchführen
→ neue Zielpositionen gelten für die folgende Renditeperiode

Kein Look-ahead.

Das BIP-Zielgewicht am Jahresende darf die Rendite, die gerade bis zu diesem Jahresende verdient wurde, nicht rückwirkend verändern.

Am letzten Datum des gesamten Untersuchungszeitraums wird keine neue wirtschaftlich wirkungslose Allokation und kein Trade erzeugt.

--------------------------------------------------
7. KONFIGURATION
--------------------------------------------------

Erweitere das bestehende JSON-Schema um:

`country_weighting`

Bevorzugte Struktur:

"country_weighting": {
  "enabled": true,
  "country_assets": {
    "COUNTRY_A": "ASSET_A",
    "COUNTRY_B": "ASSET_B"
  },
  "indicator": "GDP_SYNTHETIC",
  "unit": "SYNTHETIC_UNITS",
  "rebalance_frequency": "annual"
}

Zusätzlich benötigt `data` bei aktivierter Länderstrategie:

"macro": "path/to/macro_data.csv"

Anforderungen:

- mindestens zwei Länder für die Strategie,
- jede Länderkennung eindeutig,
- jeder Asset-Proxy eindeutig,
- kein Asset darf zwei Ländern gleichzeitig zugeordnet werden,
- jedes Asset muss in Metadaten und Performance-Daten vorhanden sein,
- Metadatenwährung muss zur `base_currency` passen,
- `assets.csv.country` des Proxys muss der konfigurierten Länderkennung entsprechen,
- `indicator` explizit,
- `unit` explizit,
- `rebalance_frequency` exakt `"annual"`.

Keine fachlichen Defaults.

Andere Rebalancing-Frequenzen werden nicht still interpretiert.

Der konkrete reale Indikator und die tatsächlichen Länder bleiben weiterhin offen.

--------------------------------------------------
8. PERFORMANCE-KALENDER
--------------------------------------------------

Alle Länder-Assets einer aktivierten Länderstrategie gehören zur Vereinigungsmenge der benötigten Performance-Assets.

Damit verwenden Buy-and-Hold, Rebalancing, Trend und Country-Weighting in einem gemeinsamen Run denselben effektiven Performance-Kalender.

Makrodaten verändern oder erweitern den Performance-Kalender nicht.

Fehlende Marktbeobachtungen werden weiterhin gemäss OD-01 behandelt.

--------------------------------------------------
9. WIEDERVERWENDUNG DER PORTFOLIOLOGIK
--------------------------------------------------

Verwende die bereits geprüften Funktionen und Zustandsregeln für:

- `neue_gewichtung()`
- `rebalancing()`
- Drawdown
- Portfolioverlauf
- Kapitalerhaltung

Vermeide eine unabhängige zweite Implementierung derselben Portfolio-/Trade-Formeln.

Da BIP-Zielgewichte über die Zeit variieren, darf die Result-/Validierungslogik technisch erweitert werden.

Dabei muss aber gelten:

- Für die bestehende feste Rebalancing-Strategie bleiben die Zielgewichte unverändert konstant.
- Für Country-Weighting können sich Zielgewichte ausschliesslich bei einer tatsächlichen initialen Allokation oder einem tatsächlichen BIP-Rebalancing ändern.
- Bestehende Rebalancing-Tests bleiben unverändert grün.

Technische Refactorings zur gemeinsamen Zustandslogik sind erlaubt, sofern alle bisherigen Regressionen bestehen.

--------------------------------------------------
10. WEIGHTS_HISTORY FÜR COUNTRY-WEIGHTING
--------------------------------------------------

Verwende dieselben Spalten:

date
strategy
asset_id
weight_before
target_weight
weight_after

Strategiename:

`country_weighting`

Semantik:

Startdatum:
- `weight_before = target_weight = weight_after`
- Zielgewichte stammen aus der zum Startdatum historisch zulässigen BIP-Entscheidung.

Normales Datum ohne Rebalancing:
- `weight_before` = tatsächliches Driftgewicht nach Rendite.
- `target_weight` = zuletzt tatsächlich angewandtes BIP-Zielgewicht.
- `weight_after = weight_before`.

Tatsächliches BIP-Rebalancing-Datum:
- `weight_before` = tatsächliches Gewicht nach Rendite und vor Trade.
- `target_weight` = neu aus damals verfügbaren BIP-Daten berechnetes Gewicht.
- `weight_after = target_weight`.

Nach dem Ereignis bleibt dieses Zielgewicht das Referenz-Zielgewicht, bis eine spätere tatsächliche BIP-Aktualisierung erfolgt.

Am endgültigen Untersuchungsende ohne folgende Renditeperiode wird kein neues Zielgewicht nur zu Dokumentationszwecken eingeführt. Das zuletzt tatsächlich angewandte Zielgewicht bleibt bestehen.

--------------------------------------------------
11. TRADES
--------------------------------------------------

Verwende die bestehenden Spalten:

date
strategy
asset_id
value_before
target_value
transaction_value

Nur tatsächliche BIP-Rebalancing-Ereignisse werden ausgegeben.

Keine initialen Trades.

Keine Abschlusstrades ohne folgende Renditeperiode.

Kapitalerhaltung bleibt verbindlich:

sum(value_before) == sum(target_value)

und:

sum(transaction_value) == 0

innerhalb der bereits dokumentierten Toleranzen.

--------------------------------------------------
12. MAKRO-PROVENIENZ
--------------------------------------------------

Es ist kein neuer fachlicher CSV-Output erforderlich.

Dokumentiere die tatsächlich verwendeten Makrodaten aber maschinenlesbar in `data_quality.json`.

Für jede tatsächlich angewandte BIP-Entscheidung mindestens:

- decision_date
- decision_type (`initial` oder `annual_rebalance`)
- selected_period
- indicator
- unit
- je Land:
  - country
  - asset_id
  - GDP value
  - available_from der verwendeten Version
  - berechnetes target_weight

Dokumentiere ausserdem:

- Zahl geladener Makrozeilen,
- konfigurierte Länder,
- verwendete Entscheidungen,
- gegebenenfalls ignorierte spätere Versionen müssen nicht einzeln gelistet werden, dürfen aber keine Entscheidung beeinflussen.

Die Makro-Eingabedatei muss in `run_manifest.json` als Input mit SHA-256 enthalten sein.

Die vollständig aufgelöste Konfiguration muss Länder-Mapping, Indikator, Einheit und Frequenz enthalten.

--------------------------------------------------
13. RESULTATE UND KENNZAHLEN
--------------------------------------------------

`portfolio_history.csv` und `summary.csv` integrieren `country_weighting` wie jede andere Strategie.

Die Strategie verwendet denselben:

- Startwert,
- effektiven Zeitraum,
- Performance-Kalender,
- Risk-Free-Vergleich,
- Kennzahlenvertrag

wie die anderen Strategien des Runs.

Keine spezielle Sharpe-, Drawdown- oder Annualisierungsformel für BIP.

--------------------------------------------------
14. SYNTHETISCHE BIP-DEMO
--------------------------------------------------

Erstelle:

`configs/demo_country_weighting.json`

und künstliche Daten, z. B. unter:

`configs/country_weighting_demo/`

Verwende keine realen Länder oder echten BIP-Werte.

Die Demo soll mindestens zwei künstliche Länder enthalten.

Empfohlene handrechenbare Struktur:

Startdatum 2020-01-31.

Zum Start ist das jüngste gemeinsame verfügbare BIP-Jahr 2018:

COUNTRY_A = 60
COUNTRY_B = 40

→ Startgewichte 60/40.

Für BIP-Jahr 2019:

COUNTRY_A:
- erste Version beispielsweise 52, früher verfügbar
- Revision 50, noch vor dem Jahresendentscheid 2020 verfügbar

COUNTRY_B:
- 50, vor Jahresendentscheid 2020 verfügbar

→ am Jahresendrebalancing 2020 Zielgewicht 50/50.

Zusätzlich eine spätere Revision von BIP 2019 mit:
available_from nach dem Jahresendentscheid 2020.

Diese darf die Entscheidung von 2020 nicht verändern.

Für BIP 2020 können weitere Werte vorhanden sein, die erst 2021 verfügbar werden.

Nutze künstliche Performance-Reihen so, dass:

- Start 60/40 sichtbar ist,
- Gewichte 2020 driften,
- am Jahresende 2020 auf ein anderes BIP-Gewicht, z. B. 50/50, gewechselt wird,
- mindestens eine folgende Periode beweist, dass die neuen Zielgewichte verwendet wurden,
- am endgültigen Jahresende kein nutzloser Abschlusstrade erfolgt.

Alle Zahlen müssen von Hand nachvollziehbar bleiben.

--------------------------------------------------
15. VERPFLICHTENDE TESTS
--------------------------------------------------

Die gesamte bestehende Suite muss unverändert grün bleiben.

Ergänze mindestens folgende Tests.

A – Makrovertrag
Ablehnen:

- fehlende Pflichtspalten,
- ungültiges Referenzjahr,
- leeres Land,
- leeren Indikator,
- nichtpositive GDP-Werte,
- NaN/Inf/Textwerte,
- leere Einheit,
- ungültiges `available_from`,
- mehrdeutige doppelte Versionen.

B – As-of-Verfügbarkeit

Eine Zeile mit:

available_from > decision_date

darf die Entscheidung nicht beeinflussen.

Beweise mit einem synthetischen Gegenbeispiel, dass eine spätere Revision einen früheren historischen Portfoliozustand nicht verändert.

C – Revisionen

Für dasselbe Land/Referenzjahr:

Version 1 verfügbar vor Entscheidung.
Version 2 ebenfalls vor Entscheidung, aber später veröffentlicht.

Die jüngste bis zur Entscheidung verfügbare Version wird verwendet.

Eine erst danach verfügbare Version wird ignoriert.

D – Gemeinsames Referenzjahr

Land A besitzt bereits Jahr 2020.
Land B nur Jahr 2019.

Es muss 2019 für BEIDE Länder verwendet werden.

Keine Mischung unterschiedlicher Referenzjahre.

E – Fehlende Länder

Fehlt für mindestens ein konfiguriertes Land ein gemeinsamer gültiger Datenstand:

Run ablehnen.

Keine Renormierung der übrigen Länder.

F – Startallokation

Am effektiven Start:

- nur damals verfügbare Daten verwenden,
- jüngstes gemeinsames Jahr wählen,
- GDP 60/40 → Positionen 60/40 bei Kapital 100,
- kein Start-Trade.

Eine erst nach dem Start verfügbare neuere Periode darf die Startgewichte nicht beeinflussen.

G – Jährliches BIP-Rebalancing

- Rendite zuerst.
- Drift danach sichtbar.
- Makroentscheidung auf Jahresenddatum.
- neue BIP-Gewichte danach anwenden.
- Trades korrekt.
- folgende Renditeperiode verdient mit den neuen Positionen.

H – Dynamische Zielgewichte

`weights_history`:

- Startziel korrekt,
- Ziel bleibt zwischen Entscheidungen unverändert,
- Ziel ändert sich nur beim tatsächlichen BIP-Rebalancing,
- nach Rebalancing bleibt neues Ziel aktiv.

I – Kein Abschlusstrade

Letzter Bewertungstermin:
keine neue BIP-Allokation/kein Trade, wenn danach keine Renditeperiode folgt.

J – Kapitalerhaltung

Bei jedem Country-Weighting-Rebalancing:

- Vorwertsumme = Zielwertsumme = Portfoliovermögen
- Transaktionssumme = 0
- Gewicht nach Trade = Zielgewicht

K – Länder-/Asset-Mapping

Ablehnen:

- unbekanntes Asset,
- dasselbe Asset für zwei Länder,
- falsches `assets.csv.country`,
- falsche Währung,
- leeres Mapping,
- nur ein Land, falls Engine v1 mindestens zwei Länder verlangt.

L – Indicator / Unit

Nur exakt konfigurierte Kombination verwenden.

Andere Indikatoren/Einheiten in derselben Datei dürfen Ergebnisse nicht verändern.

Fehlt die konfigurierte Kombination für ein benötigtes Land, Run ablehnen.

M – Zukunftsdaten

Ändere:

- eine spätere Makroversion,
- einen späteren BIP-Referenzwert,
- einen späteren Marktwert.

Frühere Portfolio-, Gewichts- und Tradezustände dürfen unverändert bleiben.

N – Multi-Strategy

Buy-and-Hold, feste Rebalancing-Strategie, Trend und Country-Weighting können im selben Run ausgeführt werden.

Alle verwenden denselben Performance-Kalender.

Makrodaten verändern andere Strategien nicht.

Summary enthält jede Strategie genau einmal.

O – Reihenfolge

Andere Reihenfolge von:

- Makrozeilen,
- Ländern im JSON,
- Assetzeilen,
- Marktzeilen

darf fachliche Ergebnisse nicht verändern.

P – Provenienz

Prüfe:

- Makrodatei-Hash im Manifest,
- tatsächlich verwendetes BIP-Jahr je Entscheidung,
- verwendete Version / `available_from`,
- GDP-Wert,
- berechnetes Gewicht,
- initial vs annual_rebalance.

Q – Regression

Alle bisherigen Core-, Rebalancing- und Trendtests bleiben grün.

Alle drei bisherigen Demo-Läufe bleiben fachlich unverändert.

Weitere sinnvolle Randfälle darfst du ergänzen.

Tests nicht abschwächen, damit die Implementierung grün erscheint.

--------------------------------------------------
16. WICHTIGE LOOK-AHEAD-PRÜFUNG
--------------------------------------------------

Erzeuge ausdrücklich mindestens einen Test, bei dem:

- eine Revision eines historischen BIP-Werts erst NACH einem Rebalancing-Datum veröffentlicht wird,
- ihr numerischer Wert stark vom vorher bekannten Wert abweicht.

Der historische Rebalancing-Trade und alle davor liegenden Ergebnisse müssen trotzdem exakt unverändert bleiben.

Dieser Test ist für die wissenschaftliche Glaubwürdigkeit der BIP-Strategie besonders wichtig.

--------------------------------------------------
17. DOKUMENTATION
--------------------------------------------------

Aktualisiere:

`documentation/engine/implementation.md`

Dokumentiere mindestens:

- Makro-Datenvertrag,
- Bedeutung von `period` und `available_from`,
- Versions-/Revisionsauswahl,
- jüngstes gemeinsames Referenzjahr,
- initiale BIP-Allokation,
- jährliche Aktualisierung,
- Länder-Asset-Mapping,
- dynamische `target_weight`-Semantik,
- Wiederverwendung der Rebalancing-Logik,
- Provenienz,
- künstliche Demo,
- verbleibende Grenzen.

Aktualisiere:

`documentation/engine/testing.md`

Dokumentiere:

- tatsächlich ausgeführte Testbefehle,
- Gesamtzahl Tests,
- As-of-/Revisionstest,
- handrechenbare Start- und Jahresendgewichte,
- BIP-Demo,
- Regression aller bisherigen Strategien,
- verbleibende Grenzen.

Aktualisiere:

`documentation/ai-usage/ai-usage-log.md`

gemäss bestehendem Schema.

--------------------------------------------------
18. VERSION
--------------------------------------------------

Wenn die Erweiterung technisch vollständig umgesetzt wird, darf die technische Paketversion konsistent auf `0.4.0` erhöht werden.

Dies ist eine technische Versionsnummer und keine Freigabe der späteren realen Untersuchung.

--------------------------------------------------
19. SELBSTSTÄNDIGES ARBEITEN
--------------------------------------------------

Innerhalb dieses bestätigten Auftrags darfst du:

implementieren
→ testen
→ technische Fehler korrigieren
→ erneut testen
→ dokumentieren.

Stoppe, wenn eine neue finanzwirtschaftliche oder methodische Entscheidung notwendig wäre.

Nicht still:

- fehlende Länder entfernen,
- BIP-Werte interpolieren,
- Veröffentlichungsdaten schätzen,
- BIP-Perioden mischen,
- aktuelle revidierte Werte rückwirkend verwenden,
- einen realen Indikator auswählen.

--------------------------------------------------
20. NICHT ERLAUBT
--------------------------------------------------

Nicht verändern:

- `notebooks/Analyse.ipynb`
- `notebooks/Theorie.ipynb`
- `methodik.qmd`
- `references.bib`
- `documentation/engine/decisions.md`
- fertige Buchkapitel

Nicht implementieren:

- reale Makro-/Marktdatenadapter,
- Live-Downloads,
- gemischte Kommer-Strategie,
- Faktorlogik,
- FX,
- Kosten,
- Steuern,
- Inflation,
- Batch,
- Web/API,
- Optimierung,
- reale Hauptuntersuchung.

--------------------------------------------------
21. ABSCHLUSSPRÜFUNG
--------------------------------------------------

Vor Abschluss:

- vollständige pytest-Suite ausführen,
- Buy-and-Hold-Demo erneut ausführen,
- Rebalancing-Demo erneut ausführen,
- Trend-Demo erneut ausführen,
- Country-Weighting-Demo ausführen,
- Startgewichte manuell kontrollieren,
- Jahresend-GDP-Auswahl manuell kontrollieren,
- Revision-/As-of-Test kontrollieren,
- Trades und Kapitalerhaltung prüfen,
- weights_history prüfen,
- Makro-Provenienz prüfen,
- alle Output-Hashes prüfen,
- Manifest prüfen,
- git diff prüfen,
- geschützte Dateien auf Unverändertheit prüfen,
- Dokumentation aktualisieren,
- KI-Log aktualisieren.

Keinen Commit erstellen.

--------------------------------------------------
22. ABSCHLUSSANTWORT
--------------------------------------------------

Berichte am Ende kompakt:

1. welche Dateien erstellt/geändert wurden,
2. welche bestehenden Komponenten refaktoriert wurden,
3. wie historische BIP-Versionen ausgewählt werden,
4. wie das anfängliche BIP-Portfolio bestimmt wird,
5. wie jährliche BIP-Rebalancings bestimmt werden,
6. wie der Demo-Lauf gestartet wird,
7. wichtigste handrechenbare Demo-Ergebnisse,
8. Anzahl und Ergebnis der tatsächlich ausgeführten Tests,
9. ob Core, Rebalancing und Trend unverändert funktionieren,
10. ob neue fachliche Entscheidungen nötig wurden,
11. ob geschützte Dateien unverändert blieben.

Danach STOPPEN.

Noch keine realen Daten importieren und noch keinen Hauptversuch starten.