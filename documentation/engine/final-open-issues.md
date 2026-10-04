# Offene Befunde des finalen Engine-Audits

**Datum:** 2026-10-04. **Geprüfte Engine:** 0.4.0, akzeptierter Tag `engine-country-weighting-v0.4.0`, Commit `5a06432457c76de925258db16a5bcbb5dc48cdc2`.

**Audit-Checkout:** `a298f69b12929f83da795bffa8c81833fef7f1d0`; gegenüber dem Tag ausschliesslich der neue Audit-Prompt. Grundlage: [Auditauftrag](../ai-usage/prompts/2026-10-04-engine-v1-final-audit.md), [verbindliche Entscheidungen](decisions.md), [Gesamtbericht](final-audit.md).

Das Register enthält **3 ENGINE-BLOCKING**, **7 STUDY-BLOCKING** und **3 NON-BLOCKING** Befunde. Unterbefunde mit derselben Vertragsursache sind gemeinsam gezählt. Empfehlungen sind nicht implementiert und keine neuen Autorenentscheidungen. Die 344 bestehenden Tests bestehen; die folgenden zusätzlichen Gegenbeispiele zeigen Grenzen ihrer Abdeckung.

## EB-01 – Positive Portfolioallokationen können unbemerkt zu null unterlaufen

- **Klassifikation:** ENGINE-BLOCKING.
- **Betroffen:** `src/engine/portfolio.py:run_annual_portfolio`, `src/funktionen.py:rebalancing`, beide Portfolio-Strategien; Tests zu kleinen Positionen/Allokationen.
- **Bezug:** Theorie 3.8/3.9, OD-06/11/13; positive konfigurierte Gewichte müssen tatsächlich gehalten werden oder bei numerischer Nichtdarstellbarkeit ausdrücklich scheitern.
- **Reproduktion:** Zwei positive, endliche Reihen A/B, zwei Bewertungen am 2020-01-31 und 2020-02-29. Startkapital `1e-200`, Ziele `{A:1e-200, B:1}`, Performance A `1 → 1e300`, B `1 → 1`, Jahresrebalancing, `period_frequency:null`, `periods_per_year:12`, keine RF-Datei. Metadaten A/B mit verschiedenen Ländern C_A/C_B, jeweils CHF. Für Country-Weighting GDP 2019: C_A `1e-200`, C_B `1`, jeweils GDP/UNITS und verfügbar ab 2020-01-01. Beide Strategien können gemeinsam aktiviert werden. Alle Eingaben erfüllen den derzeitigen Vertrag; die gerundete Gewichtssumme ist 1.
- **Erwartet:** Der nicht darstellbare positive Positionswert `1e-200 × 1e-200 = 1e-400` muss beim Allokieren erkannt und der Run abgelehnt werden. Falls eine ausdrücklich unterstützte Rechenrepräsentation diese Position erhalten könnte, ergäbe die unabhängige Decimal-Rechnung mit Präzision 450 am Ende `1e-100 + 1e-200`, also ungefähr `1e-100`, und eine Rendite ungefähr `1e100`. Endwert und Rendite sind selbst als Float darstellbar. Keine neue Arbiträrpräzisionspflicht wird daraus abgeleitet.
- **Tatsächlich:** Die Startposition A wird `0.0`. Beide Strategien exportieren einen erfolgreichen Run mit Endwert `1e-200` und Periodenrendite `0.0`. Die Startgewichtstabelle nennt trotzdem das positive Ziel. `neue_gewichtung` erkennt nur den Übergang einer bereits positiven Position zu null; das vorherige Verschwinden beim Allokieren bleibt unentdeckt. Die Gewichtstoleranz verdeckt diesen winzigen Anteil, dessen späterer Renditebeitrag jedoch gross sein kann.
- **Zusätzlicher Helper-Nachweis:** `rebalancing(pd.Series({'A':0.,'B':1e-200}), pd.Series({'A':1e-200,'B':1.}))[3]` liefert ebenfalls `{A:0.,B:1e-200}` ohne Fehler. Der gleiche Fehler ist damit auch beim jährlichen Neuallokieren möglich, nicht nur am Start.
- **Tatsächlich ausgeführt:** Temporäres `probe_underflow.py` über Checkout und installiertes 0.4.0-Wheel; beide zeigen den falschen erfolgreichen Endwert. `check_math_calendar.py` reproduziert den Helper-Fall. Prüfdateien liegen ausschliesslich unter ignoriertem `.venv/final_audit/`.
- **Empfehlung:** Positive Zielgewichte mit positiven Gesamtkapitalwerten an jeder Allokationsstelle gegen null unterlaufende Zielpositionen absichern; initiale und jährliche Pfade gleich behandeln. Eine weitere Implementierung muss beide Strategien mit diesem unabhängigen Gegenbeispiel prüfen. Toleranzen allein beheben den verlorenen wirtschaftlichen Beitrag nicht.
- **Neue fachliche Entscheidung erforderlich:** Nein. Ein ausdrücklicher numerischer Abbruch entspricht dem bestehenden Vertrag; keine Regeln oder Gewichte ändern.

Minimaler vollständiger Konfigurationskern für die beschriebenen temporären CSVs:

```json
{
  "schema_version": "1.0", "run_name": "audit_underflow",
  "period": {"start": "2020-01-31", "end": "2020-02-29"},
  "start_capital": 1e-200, "base_currency": "CHF",
  "periods_per_year": 12, "period_frequency": null,
  "data": {"market": "market.csv", "assets": "assets.csv", "macro": "macro.csv"},
  "strategies": {
    "rebalance": {"enabled": true, "target_weights": {"A": 1e-200, "B": 1}, "rebalance_frequency": "annual"},
    "country_weighting": {
      "enabled": true, "country_assets": {"C_A": "A", "C_B": "B"},
      "indicator": "GDP", "unit": "UNITS", "rebalance_frequency": "annual"
    }
  },
  "output_dir": "runs"
}
```

Die CSVs verwenden die vollständigen Pflichtspalten aus `implementation.md`; für Assets können `name`, `asset_class` und `provider` beliebige ausdrücklich künstliche Kennungen, `provider_symbol` jeweils A/B enthalten. Die nachstehende Marktdatei genügt:

```csv
date,asset_id,performance_value
2020-01-31,A,1
2020-01-31,B,1
2020-02-29,A,1e300
2020-02-29,B,1
```

## EB-02 – Result- und Exportprüfungen lassen widersprüchliche Ergebnisse passieren

- **Klassifikation:** ENGINE-BLOCKING.
- **Betroffen:** `src/engine/result.py:StrategyResult.validate/_validate_allocations/validate_results`, `src/analysis/metrics.py:compute_metrics`, `src/export/results.py:export_run`.
- **Bezug:** Analyse 5.7, Auditauftrag Abschnitt 10; OD-06/08/09/13 und nachvollziehbare tatsächliche Konfiguration im Manifest.
- **Reproduktion A, Drawdown:** Kontext aus unverändertem `configs/demo_buy_hold.json` vorbereiten und Buy-and-Hold ausführen. Eine Kopie der mittleren History-Zeile auf `drawdown=0.75` setzen, den Rest unverändert lassen. `validate_results`, `compute_metrics` und `export_run` akzeptieren das Ergebnis. Der Pfad lautet weiterhin 100/110/99 und sein Minimum weiterhin −0.1.
- **Reproduktion B, Summary/Status:** Für das unveränderte korrekte Resultat die berechnete Summary kopieren, `end_value=999`, `sharpe_ratio=float('inf')` setzen und einen beliebigen unzutreffenden Kennzahlstatus übergeben. `export_run` veröffentlicht eine CSV mit diesen Angaben und ein gültig gehashtes Manifest. Nur die geordnete Strategienamensliste wird an dieser Grenze kontrolliert.
- **Reproduktion C, Konfiguration:** Kontext aus `configs/demo_rebalance.json` mit 60/40 vorbereiten. `Rebalance().run(context, {'target_weights':{'EQ_SYNTH':0.2,'BD_SYNTH':0.8}, 'rebalance_frequency':'annual'})` ausführen und das Resultat durch `validate_results`, Kennzahlen und Export schicken. Tatsächliche Ziele 20/80 stehen dann neben der aufgelösten Manifest-Konfiguration 60/40. Der Kontext aktiviert auch Buy-and-Hold; das Exportieren allein des Rebalancing-Resultats wird ebenfalls nicht gegen die aktivierte Strategiemenge geprüft.
- **Erwartet:** Vollständiger Drawdown `V_t / max(V_0,...,V_t) - 1`; alle verfügbaren Summary-Zahlen endlich und mit geprüfter History/Kennzahlenformel konsistent, fehlende Werte mit zutreffendem Status. Portfolio-Assetmengen/Ziele, Ereigniskalender und ausgeführte Strategien müssen zur im Manifest ausgewiesenen Konfiguration passen oder ein explizit anderer unterstützter Aufrufvertrag muss diese Konfiguration korrekt ausweisen.
- **Tatsächlich:** Drawdownprüfung umfasst Endlichkeit und Startnull, die Kennzahlenprüfung vergleicht nur das Minimum. Feste Rebalancing-Ziele müssen zwar konstant sein, werden jedoch nicht mit `context.config.target_weights` abgeglichen. Der jährliche Ereigniskalender wird für Country-Weighting streng geprüft, für feste Rebalancing-Resultate fehlen entsprechende vollständige Kontextkontrollen. Summary-Spalten, Werte und Status werden an der Exportgrenze nicht validiert. Trend-Signale und historische GDP-Ziele werden hingegen ausdrücklich gegen ihren Kontext geprüft.
- **Reichweite des Nachweises:** Die Gegenbeispiele verwenden manipulierte bzw. abweichend parametrierte Resultate an den vorhandenen Python-Schnittstellen. Sie belegen eine Lücke der zugesagten Sicherungen. Sie behaupten nicht, dass der normale CLI-Runner mit unveränderten Demos diese Resultate erzeugt. Dessen Ergebnisse sind unabhängig korrekt nachgerechnet. EB-01 ist zusätzlich ein Fehler im normalen vollständigen Runner.
- **Tatsächlich ausgeführt:** Alle drei Reproduktionen über Checkout und Wheel mit `probe_contracts.py`, jeweils erfolgreiche widersprüchliche Exporte.
- **Empfehlung:** Den Kontext- und Ergebnisvertrag an der gemeinsamen Validierungs-/Exportgrenze vervollständigen: gesamter Drawdownpfad, konfigurierte Strategie-/Asset-/Zielmengen, jährliche Ereignisse, wirtschaftliche Zustandsfolge sowie Summary-/Statuskonsistenz. Bestehende finanzmathematische Funktionen wiederverwenden; keine zweite unverbundene Kennzahlenimplementierung einführen. Negative Grenzfälle müssen einen Export verhindern.
- **Neue fachliche Entscheidung erforderlich:** Nein. Die erforderlichen Regeln und Spalten sind festgelegt. Technisch zu klären ist die Reichweite der Python-Schnittstellen und ihre Abgleichstelle.

Kleiner ausführbarer Nachweis für A; er schreibt ausschliesslich einen zusätzlichen ignorierten Run:

```python
from dataclasses import replace
from maturarbeit_engine.engine.config import load_config
from maturarbeit_engine.engine.context import prepare_context
from maturarbeit_engine.engine.result import validate_results
from maturarbeit_engine.strategies.buy_hold import BuyAndHold
from maturarbeit_engine.analysis.metrics import compute_metrics
from maturarbeit_engine.export.results import export_run

ctx = prepare_context(load_config("configs/demo_buy_hold.json"))
r = BuyAndHold().run(ctx, {"asset": ctx.config.asset})
h = r.portfolio_history.copy()
h.loc[1, "drawdown"] = 0.75
bad = replace(r, portfolio_history=h)
validate_results(ctx, [bad])
summary, status = compute_metrics(bad, ctx)
export_run(ctx, [bad], summary, status)  # Wird in 0.4.0 akzeptiert.
```

## EB-03 – pandas interpretiert überbreite CSV-Zeilen still als Index

- **Klassifikation:** ENGINE-BLOCKING.
- **Betroffen:** `src/data/normalize.py:read_csv_snapshot`; gemeinsame Lesestelle für Markt-, Metadaten-, RF- und Makrodateien.
- **Bezug:** Analyse 5.3/5.5; Daten müssen unter ihren deklarierten Spalten korrekt und nachvollziehbar ausgerichtet werden. Ein erfolgreicher Hash der Originalbytes belegt nicht ihre richtige Interpretation.
- **Reproduktion:** Statt der Marktdatei der Buy-and-Hold-Demo eine temporäre CSV mit drei Kopfspalten und vier Feldern je Datenzeile verwenden:

```csv
date,asset_id,performance_value
2019-12-31,2020-01-31,DEMO_SYNTHETIC,100
2020-01-31,2020-02-29,DEMO_SYNTHETIC,110
2020-02-29,2020-03-31,DEMO_SYNTHETIC,99
```

- **Erwartet:** Zeilenbreitenfehler vor der Simulation. Unter dem deklarierten Header wäre das erste Feld das Datum; die nachfolgenden Felder passen nicht zu den Kopfspalten. Zusätzliche Daten dürfen nicht als unbenannter Index verschwinden.
- **Tatsächlich:** `pd.read_csv` nimmt das jeweils erste Feld als Index. Die Engine nutzt die zweite Spalte als Datum und ignoriert den ursprünglichen ersten Datumswert. Der vollständige Lauf endet erfolgreich mit Bewertungen 2020-01-31/02-29/03-31, Vermögen 100/110/99 und `validation_status=passed`. Keine Parsingwarnung im Qualitätsbericht. Sowohl Checkout als auch Wheel reproduziert.
- **Empfehlung:** CSV-Struktur unabhängig von pandas' impliziter Indexinterpretation prüfen, insbesondere Anzahl Felder gegen Header; danach eine ausdrückliche spaltenerhaltende Parsingregel. Ein blosses `index_col=False` genügt nicht, wenn es überschüssige Daten abschneidet. Benannte zusätzliche erlaubte Spalten bleiben von dieser strukturellen Fehlerprüfung unterscheidbar. Alle vier Eingabedateiarten an der gemeinsamen Lesestelle prüfen.
- **Neue fachliche Entscheidung erforderlich:** Nein. Es ist eine technische Verletzung des festgelegten Datenvertrags.

## SB-01 – Reale Performance-Reihen, Anlagen, Benchmark und Währungsbasis festlegen

- **Klassifikation:** STUDY-BLOCKING.
- **Betroffen:** Spätere reale Markt-/Metadatendateien und Versuchskonfiguration, OD-10/14; Theorie 3.9/3.13 und Methodik.
- **Begründung:** Alle vorhandenen Demos sind künstlich. `performance_value` und das Metadatenfeld `currency` können weder Dividendenreinvestition noch Netto-/Brutto-Total-Return, Fondsgebühren, Splitbehandlung, Investierbarkeit oder historische Proxyabdeckung aus Zahlen allein belegen.
- **Erwartet:** Vor Hauptlauf begründete Anlagen/Indizes/Benchmark und kompatible Währungsbasis; Quellspalten, Dividenden-/Splitbehandlung und gegebenenfalls bereits enthaltene Kosten explizit dokumentiert und stichprobenweise fachlich geprüft.
- **Tatsächlich:** Noch keine endgültigen Daten oder Proxies gewählt; keine realen Daten im Audit geprüft.
- **Empfehlung:** Autor legt Auswahl und Datenbedeutung vor Ergebnisvergleich fest; getrennte Datenaufbereitung und kontrollierte lokale Total-Return-Reihen archivieren. Keine Fondsreihen nachträglich um enthaltene Gebühren bereinigen, ohne entsprechende Entscheidung.
- **Neue fachliche Entscheidung erforderlich:** Ja, endgültige Versuchsauswahl und Datenbedeutung; keine Änderung der bereits festgelegten allgemeinen Engine-Regeln nötig.

## SB-02 – Zeitraum, Kapital, tatsächliche Frequenz und Annualisierungsbasis festlegen

- **Klassifikation:** STUDY-BLOCKING.
- **Betroffen:** Spätere Konfiguration; `src/engine/context.py:check_period_logic`, OD-01/02/03/15.
- **Reproduktion/Begründung:** Monats-/Jahresanfangs- und -endgitter, Sonntag-Wochen und vollständige Kalendertage werden unterstützt. `D` mit Freitag/Montag ist unregelmässig; `m=252` wird nicht als Kalenderregel angenommen. Teilmonat mit tatsächlicher Bewertung am 15. und Monatsende scheitert ebenfalls an der Jahreskennzahlenfreigabe.
- **Erwartet:** Untersuchungszeitraum/Startkapital sowie Frequenz und Jahresfaktor vor Hauptlauf fixiert. Bei Börsentagesdaten muss entschieden und geprüft sein, welche tatsächlichen Kalender/Feiertage und Jahreskonventionen gelten. Gegebenenfalls eine gesondert beauftragte technische Erweiterung oder methodisch begründete Aufbereitung; keine automatische Ersatz-CAGR.
- **Tatsächlich:** Konservative Engine gibt bei ungeklärter Periodik leere annualisierte Zahlen mit Status aus; kein nachgewiesener falscher Jahreswert für die geprüften Fälle. Die Entscheidung zu 252, Schaltjahren, Wochenkonvention und eventuell echten Teilintervallen bleibt eine Versuchsfrage. Effektive Grenzen können von angeforderten Grenzen abweichen und werden ausgewiesen.
- **Empfehlung:** Reale gemeinsame Kalender und Frequenz je Rendite-/Signalreihe prüfen, entfernte Tage beurteilen, gewünschte/effektive Grenzen explizit abnehmen. Eine vollständig beobachtete Monatsperiode zwischen zwei Monatsendankern ist von einer innerhalb des Monats beginnenden tatsächlichen Teilperiode zu unterscheiden.
- **Neue fachliche Entscheidung erforderlich:** Ja, konkrete Versuchswerte und bei täglicher Studie die noch nicht definierte Handelskalender-/Annualisierungsregel. Diese fehlende Unterstützung blockiert den klar begrenzten allgemeinen Engine-Freeze nicht für sich allein.

## SB-03 – Reale risikofreie Serie und Normalisierung belegen

- **Klassifikation:** STUDY-BLOCKING.
- **Betroffen:** Späterer RF-Import/Adapter und lokale RF-Datei; OD-07/08/16.
- **Begründung:** Die Engine verlangt bereits normalisierte Dezimalrenditen mit exakten Anfangs-/Endgrenzen. Sie kann aus einer gelieferten Zahl nicht erkennen, ob versehentlich ein Jahresprozentzins als Periodenrendite bezeichnet wurde.
- **Erwartet:** Vom Autor gewählte kompatible Serie mit dokumentierter Notierung, Zins-/Tageskonvention, zeitlicher Verfügbarkeit und nachvollziehbarer Umrechnung auf jedes gemeinsame Renditeintervall; unabhängige Kontrollen.
- **Tatsächlich:** Nur künstliche RF-Perioden geprüft; kein reales Zinskonversionsmodul. Fehlende RF-Dateireferenz ergibt ausdrücklich nicht verfügbare Sharpe; eine angegebene lückenhafte oder falsch ausgerichtete Datei scheitert.
- **Empfehlung:** Serie und Umrechnung separat festlegen, testen und archivieren; fehlende Werte nicht durch null ersetzen. Sharpe nach der bereits verbindlichen Überschussrenditen-Standardabweichung berechnen.
- **Neue fachliche Entscheidung erforderlich:** Ja, konkrete Serie und Konversion; OD-08 bleibt verbindlich.

## SB-04 – Reale Signalreihe, SMA-Fenster und beobachtete Vorlaufhistorie festlegen

- **Klassifikation:** STUDY-BLOCKING.
- **Betroffen:** Späterer Trend-Datensatz und Konfiguration; OD-04/05/17, `prepare_trend_signals`.
- **Begründung:** SMA-Fenster zählen die tatsächlich beobachtete eigene Signalhistorie, Positions-Lag die gemeinsamen Performance-Bewertungen. Eine weitere aktive Anlage kann die gemeinsame Zeitachse ausdünnen; das ist die bestätigte Vergleichsregel. Nachträglich adjustierte Signalreihen benötigen zusätzlich eine Eignungsprüfung.
- **Erwartet:** Vor Hauptversuch begründete Quelle, Fenster und Signalfrequenz; vollständige benötigte Vorlaufbeobachtungen vor dem effektiven Start. Datenaufbereitung muss die beabsichtigte Beobachtungsfrequenz liefern, ohne fehlende Werte zu erfinden.
- **Tatsächlich:** Ausschliesslich künstliche Fenster 2/3 bzw. 1/2 geprüft; keine endgültige Auswahl. Engine lehnt unzureichenden Vorlauf ab, trennt Signal/Performance und verwendet Lag 1/Cash 0.
- **Empfehlung:** Parameter vor Ergebnissichtung einfrieren; eigene Signal- und gemeinsame Bewertungszeitachse mit realen Daten kontrollieren und im Untersuchungsbericht erklären.
- **Neue fachliche Entscheidung erforderlich:** Ja, konkrete Signal-/SMA-Versuchswerte und Datenaufbereitung; keine Änderung von Lag oder Cash-Regel.

## SB-05 – Historisch belegte GDP-Vintages, Länder und Einheiten beschaffen

- **Klassifikation:** STUDY-BLOCKING.
- **Betroffen:** Spätere Makrodaten, Länder-/Proxy-Mapping und Importprovenienz; OD-11/12/18.
- **Begründung:** Ein heutiger revidierter GDP-Wert mit erfundenem früherem `available_from` erfüllt syntaktisch den Vertrag, wäre jedoch historisch falsch. Die Engine kann die Wahrheit dieses Datums oder die reale Vergleichbarkeit einer als gleich bezeichneten Einheit nicht selbst beweisen.
- **Erwartet:** Vor Hauptversuch begründete Länder/Proxies, GDP-Indikator und gemeinsame Einheit, echte historische Versionen/Publikationsdaten und gegebenenfalls ausdrücklich begründeter Veröffentlichungslag. Jedes verwendete As-of-Resultat muss anhand archivierter Quellen belegbar sein.
- **Tatsächlich:** Historische Auswahlmechanik funktioniert mit künstlichen Versionen; reale Daten und Quellen sind noch ungeprüft.
- **Empfehlung:** Originalvintages und Veröffentlichungsbelege erhalten; Jahres-/Einheits-/Länderabdeckung und Revisionen unabhängig prüfen. Keine Länder aus dem Nenner entfernen, keine gemischte Kommer-/Faktorstrategie als äquivalent ausgeben.
- **Neue fachliche Entscheidung erforderlich:** Ja, endgültige GDP-/Länder-/Proxy-Versuchsauswahl und gegebenenfalls Veröffentlichungsregel; die As-of- und gemeinsame Jahreslogik ist bereits entschieden.

## SB-06 – Wissenschaftliches Archiv und unveränderliche Ausführungsumgebung herstellen

- **Klassifikation:** STUDY-BLOCKING.
- **Betroffen:** Run-Archivierung, Import-/Transformationsnachweise, Wheel/Checkout und Abhängigkeitsablage; `src/export/results.py:code_provenance/export_run`.
- **Begründung:** Manifeste hashen gelesene Eingaben und Ergebnisdateien, kopieren die Inputs oder installierbare Distribution jedoch nicht. Wheel-Runs besitzen bewusst keine Git-ID; die Quellfingerprints identifizieren ihren Inhalt. Ohne erhaltene passende Bytes kann aus einem Hash keine Datei rekonstruiert werden.
- **Erwartet:** Archiv mit originalen/verarbeiteten Inputs, konkreter Config, Aufbereitungsregeln und -version, angenommenem Code-/Paketstand und kontrollierter Laufzeitumgebung. Der tatsächlich ausgeführte Code muss während des ganzen Prozesses eingefroren bleiben.
- **Tatsächlich:** Technische Hash-/Inputänderungsprüfungen bestehen. Source-Hashes/Git werden beim Export vom Dateisystem gelesen; eine nach dem Import veränderte Quelle in einem langlebigen Python-Prozess könnte von bereits geladenem Code abweichen. Dieser Änderungsfall wurde wegen der Audit-Schreibgrenze nicht durch Source-Manipulation ausgeführt; er ist ein aus dem Code abgeleitetes Betriebsrisiko, kein behaupteter beobachteter Fehler der geprüften CLI-Läufe.
- **Empfehlung:** Für Hauptläufe unveränderlichen Checkout oder erhaltenes Wheel und frischen Prozess verwenden, alle Input-/Configbytes samt Konversionsnachweisen und passende Abhängigkeitsdistributionen archivieren. Wheel-Hash und akzeptierten Tag extern eindeutig zuordnen. Eine spätere Codeänderungsprüfung/Prozessabsicherung kann diese Betriebsanforderung ergänzen; in diesem Audit keine Implementierung.
- **Neue fachliche Entscheidung erforderlich:** Keine neue Finanzregel. Autor muss die konkrete wissenschaftliche Archivierung und Datenprovenienz abnehmen; technische Ausgestaltung ist frei innerhalb dieser Vorgaben.

## SB-07 – Wissenschaftliche Texte und Beispiele mit den akzeptierten Regeln synchronisieren

- **Klassifikation:** STUDY-BLOCKING.
- **Betroffen:** Geschützte `notebooks/Theorie.ipynb`, `notebooks/Analyse.ipynb`, `methodik.qmd`; spätere wissenschaftliche Beschreibung.
- **Belege:** Theorie-Zellen 9/15/36/45/58/59/76 enthalten frühere Funktionsaufrufe bzw. Implementierungen; besonders der Start-High-Water-Mark, QuantStats-Sharpe und `trendfolge.dropna()` unterscheiden sich inzwischen vom korrigierten Code. Theorie-Zelle 52 hat Beispielgewichte mit Summe 0.8. Analyse-Zelle 30 beschreibt den RF-Rohvertrag statt des normalisierten Engine-Vertrags; Zelle 71 ist kein vollständiges gültiges 1.0-Configbeispiel. Die Methodik nennt RSI/Short, Strategievolatilität als Sharpe-Nenner und einen gemischten Kommer-ETF.
- **Erwartet:** Wissenschaftlicher Hauptversuch und seine Beschreibung müssen auf denselben akzeptierten Regeln beruhen: SMA Long/Cash, Lag 1, unverzinstes Cash, Überschussrenditen-Std mit `ddof=1`, Start-HWM, jährliche Drift-/Tradefolge, reine BIP-Länderstrategie, historischer As-of und lokaler normalisierter Eingabevertrag.
- **Tatsächlich:** `decisions.md` löst die fachlichen Konflikte eindeutig; die geschützten älteren Texte und Codebeispiele sind noch nicht entsprechend nachgeführt. Kein Anlass, sie still als aktuelle Engine-Schnittstelle auszuführen.
- **Empfehlung:** Separater ausdrücklicher Text-/Notebookauftrag mit fachlicher Kontrolle des Autors. Roh- und Engine-Verträge sowie geplante und implementierte Funktionen klar unterscheiden. Fixe 60/40-Renditeformel als Momentaufnahme erklären; jährliche Drift nicht durch konstante periodische Gewichte beschreiben.
- **Neue fachliche Entscheidung erforderlich:** Nein für die Übertragung bestehender Entscheidungen. Jede gewünschte Abweichung davon oder tatsächliche RSI-/Short-/Kommer-Erweiterung braucht dagegen einen neuen Auftrag und eine methodische Entscheidung.

## NB-01 – Legacy-Analysehelpers benötigen vollständige eigene Eingabeverträge

- **Klassifikation:** NON-BLOCKING.
- **Betroffen:** `src/funktionen.py:resample_dataframe/kumulierte_rendite/wachstumsfaktor/geometrisches_mittel/standardabweichung/annualisierte_volatilitaet/korrelationsmatrix/portfolio_risiko/buy_and_hold` bei direkter Verwendung.
- **Reproduktion:** `kumulierte_rendite([100,NaN,110,121])` setzt nach der Lücke bei `log(1.1)` fort; `buy_and_hold([.1,NaN,-.1],100)` liefert 110/NaN/99. `geometrisches_mittel(pd.Series([1.1,NaN,.9]))` gibt ca. 0.994987 aus, die entsprechende ndarray-Eingabe NaN. Standardabweichung ignoriert NaN; `corr/cov` verwenden paarweise vollständige Stichproben. Der generische Resamplinghelper erlaubt weiterhin beispielsweise `MS+last` ohne Verfügbarkeitskontrolle.
- **Erwartet:** Diese Hilfen nur auf vollständigen, gleich ausgerichteten und semantisch passenden Daten verwenden; bei zusätzlicher öffentlicher Integration vorher Validierung und zeitlich geeignete Aggregationsregeln definieren. `portfolio_risiko` ist eine feste Gewichts-/Kovarianzanalyse, kein Ersatz der Volatilität eines tatsächlich driftenden Portfolios.
- **Tatsächlich:** Mathematisch korrekte Normalfälle unabhängig geprüft. Engine-Preisvalidierung und Rendite-/Kennzahlenwrapper verhindern die gezeigten NaN-Fälle auf den aktiven Pfaden; Resampling, Logwachstum und Kovarianzanalyse sind kein aktiver Simulationspfad. Series-Gewichte werden bei Kovarianz labelbezogen ausgerichtet, ndarray-Gewichte hängen von Spaltenreihenfolge ab.
- **Empfehlung:** Eingabeverträge bei späterer Zusatzanalyse dokumentieren und gezielt prüfen; keine zweite Formelsammlung erstellen. Die Beispiele wurden als temporäre Prüfungen ausgeführt, keine neuen versionierten Tests geschrieben.
- **Neue fachliche Entscheidung erforderlich:** Nein für technische Validierung; eine neue Analyse-/Resamplingmethodik wäre separat zu entscheiden.

## NB-02 – Kompatibilitätsbereich und Paketarchivierung nur teilweise verifiziert

- **Klassifikation:** NON-BLOCKING.
- **Betroffen:** `pyproject.toml`, `requirements.lock`, Installations-/Kompatibilitätsnachweis.
- **Begründung:** Deklariert ist Python `>=3.11,<3.15`; tatsächlich geprüft wurde ausschliesslich Windows/CPython 3.14.0. Der Lock bindet Versionen, enthält aber keine Distributions-Hashes. Der aktuelle 0.4.0-Wheel-Build, frische Installation, `pip check`, 344 Tests und vier CLI-Demos bestehen.
- **Erwartet:** Aussagen zur Portabilität nur für tatsächlich geprüfte Plattformen; bei späterer Nutzung weiterer Versionen neue Kompatibilitätsläufe und für dauerhaft offline herstellbare Umgebungen archivierte Distributionen.
- **Tatsächlich:** Keine bestätigte Inkompatibilität gefunden; andere Plattformen/Interpreter nicht ausgeführt, Installation benötigte Paketquellenzugriff. Backtests selbst brauchen diesen Zugriff nicht.
- **Empfehlung:** Bei Bedarf passende Testmatrix und Wheelhouse/Hashbindung ergänzen. Für die jetzt geprüfte Umgebung kein zusätzlicher Engine-Freeze-Blocker; wissenschaftliches Archiv siehe SB-06.
- **Neue fachliche Entscheidung erforderlich:** Nein.

## NB-03 – Technische Bestandsdokumentation enthält veraltete Standangaben

- **Klassifikation:** NON-BLOCKING.
- **Betroffen:** `src/strategies/__init__.py`, `documentation/engine/implementation.md`, `documentation/engine/testing.md`.
- **Belege:** Strategien-Docstring behauptet nur implementiertes Buy-and-Hold; aktuelle Engine führt vier Strategien aus. Historische Abschlussabschnitte nennen die Länder-Abnahme noch offen. Im aktuellen Audit gilt laut Autor der Länder-Tag ausdrücklich als akzeptiert. Die frühere isolierte Wheel-Prüfung dokumentiert zutreffend nur Core 0.1.0; dieser Audit ergänzt den aktuellen 0.4.0-Nachweis.
- **Erwartet:** Aktuelle Standzusammenfassung kennt vier Strategien, akzeptierten Tag und aktualisierten Paketnachweis; historische Protokolle bleiben als solche erkennbar.
- **Tatsächlich:** Funktionaler Code und historische Testzahlen sind davon nicht betroffen. Die Behauptung vollständiger Result-Sicherungen ist durch EB-02 eingeschränkt, kein separat gezählter Dokumentfehler.
- **Empfehlung:** Bei einem später erlaubten Dokumentations-/Implementierungsschritt aktuelle Standangaben und Docstring nachführen, historische Ausführungsberichte erhalten. Die neuen Audit-Dokumente halten bereits die heutige Abnahme und Wheel-Prüfung fest.
- **Neue fachliche Entscheidung erforderlich:** Nein.

## Weiteres Vorgehen und Stopp

Vor einem allgemeinen v1.0-Freeze sind EB-01 bis EB-03 in einem neuen ausdrücklichen Auftrag zu bearbeiten und unabhängig erneut zu prüfen. SB-01 bis SB-07 blockieren die reale Hauptuntersuchung, nicht die bereits klar abgegrenzte allgemeine Methodik. NB-01 bis NB-03 sind dokumentierte Grenzen/Verbesserungen. Zusätzliche wissenschaftliche Kennzahlen nach OD-19 bleiben separat und dürfen nicht anhand günstiger Ergebnisse gewählt werden.

Dieser Audit korrigiert keine Funktion, keinen Test, keine Config und keine wissenschaftliche Datei; er endet mit den drei erlaubten Dokumentationsänderungen.
