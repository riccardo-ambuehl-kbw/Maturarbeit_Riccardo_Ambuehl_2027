# Codex-Prompt: Engine v1 – Fix der finalen Audit-Blocker

**Datum:** 2026-10-04
**Tool:** Codex
**Zweck:** Gezielte Korrektur der drei ENGINE-BLOCKING-Befunde EB-01 bis EB-03 vor dem Engine-v1.0-Freeze

## Vollständiger Prompt

Behebe ausschliesslich die drei ENGINE-BLOCKING-Befunde EB-01, EB-02 und EB-03 aus dem finalen Engine-Audit.

Dies ist ein gezielter technischer Bugfix-Auftrag.

LIES ZUERST VOLLSTÄNDIG:

- `AGENTS.md`
- `documentation/engine/decisions.md`
- `documentation/engine/final-audit.md`
- `documentation/engine/final-open-issues.md`
- `documentation/engine/implementation.md`
- `documentation/engine/testing.md`
- den gesamten aktuellen Engine-Code
- die gesamte aktuelle Test-Suite

Akzeptierter fachlicher Engine-Stand vor den Fixes:

`engine-country-weighting-v0.4.0`
Commit:
`5a06432457c76de925258db16a5bcbb5dc48cdc2`

Der aktuelle Branch enthält zusätzlich den finalen Audit und dessen Dokumentation.

WICHTIG:

- Keine neue finanzwirtschaftliche oder methodische Regel festlegen.
- Keine STUDY-BLOCKING- oder NON-BLOCKING-Punkte in diesem Auftrag beheben.
- Keine wissenschaftlichen Texte verändern.
- Keine neuen Strategien implementieren.
- Keine realen Daten verwenden.

Die Auditdokumente `final-audit.md` und `final-open-issues.md` bleiben als historischer Nachweis unverändert.

--------------------------------------------------
EB-01 – POSITIVE ALLOKATION DARF NICHT ZU NULL UNTERLAUFEN
--------------------------------------------------

Der Audit hat reproduziert, dass ein positives Zielgewicht bei:

portfolio_value * target_weight

numerisch zu `0.0` unterlaufen kann.

Beispiel:

start_capital = 1e-200
target_weight A = 1e-200
target_weight B = 1

Für A ergibt Float-Arithmetik:

1e-200 * 1e-200 = 0.0

obwohl das Zielgewicht positiv ist.

Dies darf nicht als erfolgreicher Portfoliozustand akzeptiert werden.

VERBINDLICHES VERHALTEN:

- Zielgewicht exakt 0 darf Zielpositionswert 0 ergeben.
- Zielgewicht > 0 bei positivem Gesamtvermögen muss einen strikt positiven, endlichen Zielpositionswert erzeugen.
- Wenn die verwendete Float-Repräsentation dies nicht darstellen kann, muss der Lauf mit einem klaren Fehler abbrechen.
- Keine Arbiträrpräzisionsarithmetik einführen.
- Keine Gewichte verändern.
- Keine Gewichte normalisieren.
- Keine Position still entfernen.

Diese Prüfung muss sowohl gelten für:

1. initiale Allokation,
2. jährliches Rebalancing,
3. feste Rebalancing-Strategie,
4. Country-Weighting.

Bevorzuge eine gemeinsame technische Prüfstelle, sodass Start- und Rebalancingpfad nicht zwei unterschiedliche Regeln erhalten.

Prüfe ausserdem weiterhin:

- endliche Zielpositionen,
- Kapitalerhaltung,
- exakt erlaubte Nullgewichte.

VERPFLICHTENDE REGRESSION:

Reproduziere das exakte Gegenbeispiel aus EB-01.

Der Run muss nach dem Fix fehlschlagen.

Zusätzlich:

- direkter Helper-Fall aus EB-01 muss fehlschlagen,
- echtes Zielgewicht 0 muss weiterhin funktionieren,
- normale 60/40- und GDP-Gewichte müssen unverändert funktionieren.

--------------------------------------------------
EB-02 – RESULT-/EXPORTVERTRAG VERVOLLSTÄNDIGEN
--------------------------------------------------

Der Audit hat gezeigt, dass widersprüchliche Resultate über die Python-Schnittstellen noch exportiert werden können.

Behebe die Lücken ohne zweite Finanzformelsammlung.

### A. Vollständiger Drawdownpfad

Nicht nur:

- Startdrawdown = 0,
- Endlichkeit,
- Minimum = Maximum Drawdown

prüfen.

Der vollständige gespeicherte Drawdownpfad muss exakt mit der bereits verbindlichen Drawdown-Definition aus den tatsächlichen Portfolio-Periodenrenditen übereinstimmen.

Verwende die bestehende gemeinsame Drawdown-Funktion.

Manipulation einer beliebigen Drawdown-Zeile muss vor Export erkannt werden.

### B. Summary

Vor einem erfolgreichen Export muss sichergestellt werden, dass:

- genau eine Summary-Zeile pro tatsächlich ausgeführter Strategie existiert,
- Strategiezuordnung korrekt ist,
- start_value korrekt ist,
- end_value korrekt ist,
- total_return korrekt ist,
- annualized_return korrekt bzw. korrekt nicht verfügbar ist,
- annualized_volatility korrekt bzw. korrekt nicht verfügbar ist,
- sharpe_ratio korrekt bzw. korrekt nicht verfügbar ist,
- max_drawdown korrekt ist,
- keine verfügbare Kennzahl NaN/Infinity enthält,
- nicht verfügbare Kennzahlen mit dem richtigen Status zusammenpassen.

Verwende für den Vergleich die bereits vorhandene gemeinsame Kennzahlenlogik.

Keine zweite unabhängige Berechnung derselben Kennzahlen erstellen.

Eine manipulierte Summary wie:

end_value = 999

oder:

sharpe_ratio = Infinity

muss den Export verhindern.

### C. Strategie-Set gegen Konfiguration

Ein vollständiger Run-Export muss genau die Strategien enthalten, die in der aufgelösten Konfiguration aktiviert sind.

Weder:

- fehlende aktivierte Strategie
- noch zusätzliche nicht aktivierte Strategie

darf still exportiert werden.

Falls strategieinterne Unit-Tests einzelne StrategyResults separat validieren müssen, kann zwischen lokaler StrategyResult-Validierung und strenger vollständiger Run-/Exportvalidierung technisch unterschieden werden.

Die wissenschaftliche Exportgrenze muss jedoch streng sein.

### D. Buy-and-Hold gegen Config

Prüfe beim vollständigen Runvertrag, dass Buy-and-Hold zur konfigurierten Buy-and-Hold-Anlage gehört.

### E. Fixed Rebalancing gegen Config

Prüfe:

- Assetmenge exakt gegen `config.target_weights`,
- Zielgewichte exakt gegen die konfigurierte Zielgewichtung innerhalb der bereits definierten numerischen Toleranz,
- keine 20/80-Ergebnisse unter einer 60/40-Manifestkonfiguration,
- Trade-Ereignisse exakt entsprechend dem bestätigten jährlichen Kalender,
- kein Starttrade,
- kein Abschlusstrade,
- konstante Zielgewichte zwischen allen Ereignissen.

### F. Trend gegen Config

Bestehende strenge Signal-/Asset-/Lag-Prüfungen erhalten.

Keine Lockerung.

### G. Country-Weighting gegen Config

Bestehende strenge Makro-/Proxy-/Entscheidungsprüfungen erhalten.

Keine Lockerung.

### H. Export

`export_run` darf widersprüchliche Resultate, Summary oder Status nicht veröffentlichen.

Wenn technisch sinnvoll, darf die Exportgrenze erwartete Summary-/Statuswerte intern über die gemeinsame bestehende Kennzahlenfunktion nachprüfen.

Keine inkonsistente Datei darf erst geschrieben und danach als erfolgreicher Run veröffentlicht werden.

--------------------------------------------------
VERPFLICHTENDE EB-02-TESTS
--------------------------------------------------

Mindestens:

1. Manipulierte mittlere Drawdown-Zeile → Fehler.
2. Manipulierte letzte Drawdown-Zeile → Fehler.
3. `end_value=999` in Summary → Fehler.
4. falsche `total_return` → Fehler.
5. falscher `max_drawdown` → Fehler.
6. `sharpe_ratio=Infinity` → Fehler.
7. falscher Verfügbarkeitsstatus → Fehler.
8. fehlende aktivierte Strategie beim vollständigen Export → Fehler.
9. zusätzliche nicht aktivierte Strategie → Fehler.
10. Rebalance-Resultat 20/80 bei Config 60/40 → Fehler.
11. falsche Rebalancing-Assetmenge → Fehler.
12. fehlender jährlicher Trade → Fehler.
13. zusätzlicher Trade an falschem Datum → Fehler.
14. korrekter normaler Runner aller vier Strategien bleibt erfolgreich.

Bestehende korrekte Resultate dürfen nicht verändert werden.

--------------------------------------------------
EB-03 – CSV-ZEILENBREITE VOR PANDAS PRÜFEN
--------------------------------------------------

Der Audit hat gezeigt, dass pandas bei einer CSV mit mehr Feldern als Header-Spalten das erste Feld still als Index interpretieren kann.

Dies verletzt den Datenvertrag.

Vor dem eigentlichen pandas-Parsing muss für jede physische CSV-Datenzeile strukturell geprüft werden:

- Anzahl Felder entspricht der Headerbreite,
- keine zusätzliche unbenannte Datenspalte,
- keine fehlenden Felder,
- kein stilles Abschneiden.

Verwende eine CSV-konforme Prüfung, die korrekt mit gequoteten Feldern und eingebetteten Trennzeichen umgehen kann.

Die bereits vorhandene `csv`-Standardbibliothek darf dafür verwendet werden.

Benannte zusätzliche Spalten im Header bleiben grundsätzlich technisch unterscheidbar und dürfen nicht durch eine pauschale Maximalspaltenzahl verboten werden. Entscheidend ist:

jede Datenzeile muss zur tatsächlich deklarierten Headerbreite passen.

Ein blosses:

index_col=False

ist NICHT als alleinige Lösung ausreichend, wenn dadurch überschüssige Felder verworfen werden könnten.

Nach erfolgreicher Strukturprüfung soll pandas die Spalten ausdrücklich ohne implizite Indexübernahme einlesen.

Die Prüfung gilt zentral für:

- market
- assets
- risk_free
- macro

--------------------------------------------------
VERPFLICHTENDE EB-03-TESTS
--------------------------------------------------

Mindestens:

1. Exaktes Audit-Gegenbeispiel mit drei Headerfeldern und vier Datenfeldern → Fehler.
2. Zu wenige Datenfelder → Fehler.
3. Überbreite market.csv → Fehler.
4. Überbreite assets.csv → Fehler.
5. Überbreite risk_free.csv → Fehler.
6. Überbreite macro.csv → Fehler.
7. korrekt gequotetes Feld mit Komma innerhalb eines Werts bleibt gültiges EIN Feld.
8. reguläre vorhandene Demo-CSVs bleiben unverändert erfolgreich.
9. doppelte Header bleiben weiterhin Fehler.

Kein stilles Abschneiden oder Verschieben.

--------------------------------------------------
TEST- UND REGRESSIONSANFORDERUNGEN
--------------------------------------------------

Die gesamte bisherige Suite muss weiterhin bestehen.

Vor Änderungen:

- aktuelle vollständige Suite ausführen und Ausgangswert dokumentieren.

Nach Fixes:

- vollständige Suite ausführen,
- alle drei Audit-Gegenbeispiele erneut ausführen,
- alle vier Demos erneut ausführen,
- Buy-and-Hold-Demo fachlich mit vorherigem Stand vergleichen,
- Rebalancing-Demo fachlich mit vorherigem Stand vergleichen,
- Trend-Demo fachlich mit vorherigem Stand vergleichen,
- Country-Weighting-Demo fachlich mit vorherigem Stand vergleichen.

Die normalen fachlichen Ergebnisse der vier Demos dürfen durch diese Bugfixes nicht verändert werden.

--------------------------------------------------
PAKETIERUNG
--------------------------------------------------

Wenn alle drei Blocker behoben sind:

- Paketversion technisch von 0.4.0 auf 0.4.1 erhöhen.
- Wheel bauen.
- In frische isolierte virtuelle Umgebung installieren.
- `pip check`.
- vollständige Suite gegen das installierte Wheel ausführen.
- mindestens die vier CLI-Demos gegen den installierten Paketstand prüfen.

Keine globale Installation.

--------------------------------------------------
DOKUMENTATION
--------------------------------------------------

Erstelle:

`documentation/engine/blocker-fixes.md`

Für EB-01, EB-02 und EB-03 jeweils:

- ursprünglicher Auditbefund,
- Ursache,
- technische Korrektur,
- geänderte Dateien,
- neue Regressionstests,
- Ergebnis des ursprünglichen Gegenbeispiels nach dem Fix,
- Auswirkungen auf normale Demos,
- verbleibende Grenzen.

Aktualisiere:

`documentation/engine/implementation.md`

nur soweit nötig, um die finalen technischen Sicherungen korrekt zu beschreiben.

Aktualisiere:

`documentation/engine/testing.md`

mit:

- Ausgangssuite,
- finaler Suite,
- den drei Audit-Reproduktionen,
- Wheel-Prüfung,
- vier Demo-Regressionen.

Aktualisiere:

`documentation/ai-usage/ai-usage-log.md`

gemäss bestehendem Schema.

`final-audit.md` und `final-open-issues.md` NICHT umschreiben. Sie sind der historische Nachweis, der die Bugs gefunden hat.

--------------------------------------------------
NICHT BEHEBEN IN DIESEM AUFTRAG
--------------------------------------------------

Nicht bearbeiten:

- SB-01 bis SB-07
- NB-01 bis NB-03

Insbesondere NICHT:

- reale Daten wählen,
- Daily-/252-Regel festlegen,
- Risk-Free-Serie auswählen,
- SMA-Fenster auswählen,
- BIP-Quelle auswählen,
- wissenschaftliche Notebook-Texte synchronisieren,
- Legacy-Analysehelpers allgemein redesignen,
- neue Plattformunterstützung versprechen.

--------------------------------------------------
GESCHÜTZTE DATEIEN
--------------------------------------------------

Nicht verändern:

- `notebooks/Analyse.ipynb`
- `notebooks/Theorie.ipynb`
- `methodik.qmd`
- `references.bib`
- fertige Buchkapitel
- `documentation/engine/decisions.md`
- `documentation/engine/final-audit.md`
- `documentation/engine/final-open-issues.md`

--------------------------------------------------
SELBSTSTÄNDIGES ARBEITEN
--------------------------------------------------

Innerhalb EB-01 bis EB-03 darfst du selbstständig:

implementieren
→ testen
→ Fehler korrigieren
→ erneut testen
→ dokumentieren.

Stoppe, wenn eine neue fachliche/methodische Entscheidung erforderlich wäre.

Keinen Commit erstellen.

--------------------------------------------------
ABSCHLUSSPRÜFUNG
--------------------------------------------------

Vor Abschluss:

1. vollständige Suite,
2. exakte EB-01-Reproduktion,
3. exakte EB-02-Reproduktionen,
4. exakte EB-03-Reproduktion,
5. vier CLI-Demos,
6. aktuelles Wheel,
7. frische Wheel-Installation,
8. `pip check`,
9. Suite gegen Wheel,
10. geschützte Dateien unverändert,
11. git diff prüfen,
12. Dokumentation aktualisieren.

--------------------------------------------------
ABSCHLUSSANTWORT
--------------------------------------------------

Berichte kompakt:

1. welche Dateien geändert/erstellt wurden,
2. wie EB-01 behoben wurde,
3. wie EB-02 behoben wurde,
4. wie EB-03 behoben wurde,
5. neue Gesamtzahl der Tests und Ergebnis,
6. Ergebnis der exakten drei Audit-Gegenbeispiele,
7. Ergebnis der vier Demo-Regressionen,
8. Ergebnis der Wheel-/Installationsprüfung,
9. ob neue fachliche Entscheidungen nötig wurden,
10. ob geschützte Dateien unverändert blieben.

Danach STOPPEN.

Noch keinen Engine-v1.0-Tag setzen.