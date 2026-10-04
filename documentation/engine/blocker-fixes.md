# Engine – gezielte Korrekturen EB-01 bis EB-03

**Aktueller Stand:** Engine 0.4.2. Der erste Fix-Bericht unten betrifft 0.4.1; die nach dessen Review verbliebene EB-02-Restlücke und ihr gezielter Konsistenzfix sind im letzten Abschnitt dokumentiert.

**Datum:** 2026-10-04. **Auftrag:** [vollständiger Blocker-Prompt](../ai-usage/prompts/2026-10-04-engine-v1-blocker-fixes.md). **Fachliche Grundlage:** AGENTS.md und unveränderte [OD-01 bis OD-13](decisions.md).

Akzeptierter Engine-Ausgangspunkt ist `engine-country-weighting-v0.4.0`, Commit `5a06432457c76de925258db16a5bcbb5dc48cdc2`. Arbeitsbeginn war sauber auf `70a703c`; dieser Stand enthält zusätzlich die Audit-Dokumentation und den Fix-Auftrag. [final-audit.md](final-audit.md) und [final-open-issues.md](final-open-issues.md) bleiben als historische Nachweise unverändert. Dieser Bericht dokumentiert ausschliesslich die danach ausgeführten technischen Korrekturen.

## EB-01 – positive Zielpositionen

**Befund und Ursache:** Ein positives Zielgewicht konnte bei der Multiplikation mit positivem Vermögen zu `0.0` unterlaufen. Die bisherige Summenprüfung erkannte die verlorene Position nicht: bei Kapital `1e-200` und Gewichten A=`1e-200`, B=`1` bleibt die darstellbare Summe trotz Verlust der A-Position gleich dem Kapital. Eine spätere extreme Preissteigerung kann dann fälschlich wirkungslos bleiben.

**Korrektur:** Der gemeinsame Helper `allocate_target_values()` in `src/funktionen.py` prüft nach der unveränderten Multiplikation jede Zielposition auf Endlichkeit und bei Zielgewicht > 0 auf strikt positiven Wert. Unterlauf führt zu `Positive target allocation underflowed to zero.` Die bestehenden Gewichts- und Kapitalerhaltungstoleranzen bleiben erhalten. Exakte Nullgewichte dürfen weiterhin exakt null ergeben. Keine Präzisionserweiterung, Gewichtsänderung oder Normalisierung.

**Dateien:** `src/funktionen.py` verwendet den Helper auch in `rebalancing()`; `src/engine/portfolio.py` verwendet ihn für die initiale Allokation. Damit gelten dieselben Prüfungen am Start und an jährlichen Ereignissen von Fixed Rebalancing und Country-Weighting.

**Regressionen:** `tests/test_blocker_fixes.py` prüft das ursprüngliche Startbeispiel für beide Strategien einzeln und gemeinsam, den direkten Rebalancing-Helper, tatsächlich erreichte jährliche Unterläufe in beiden Strategien sowie erlaubte Nullgewichte bei sehr kleinem, normalem und sehr grossem Kapital. Die jährlichen Fälle besitzen zunächst darstellbare positive Positionen und erreichen den Fehler erst bei der späteren Zielallokation.

**Ursprüngliches Gegenbeispiel nach Fix:** Der ursprüngliche Zwei-Anlagen-Run und der direkte Helper werden im Checkout und im installierten Wheel abgelehnt; kein Run-Ordner wird veröffentlicht.

**Demos und Grenzen:** Normale 60/40- und GDP-Allokationen bleiben bytegleich. Die Engine verwendet weiterhin Float-Arithmetik und bricht nicht darstellbare Zustände ab. Die Summentoleranz wird durch die zusätzliche Einzelpositionsprüfung ergänzt; eine allgemeine Neugestaltung der Legacy-Analysehelpers gehört nicht zu diesem Auftrag.

## EB-02 – vollständiger Run- und Exportvertrag

**Befund und Ursache:** Lokale Strukturprüfungen, der minimale Drawdown und einzelne Summary-Prüfungen reichten nicht aus, um einen vollständigen Run an seine aufgelöste Konfiguration zu binden. Eine geänderte Drawdown-Zeile, `end_value=999`, `sharpe_ratio=Infinity`, ein falscher Status oder ein 20/80-Ergebnis unter einer 60/40-Konfiguration konnten die Exportgrenze passieren.

**Korrektur:**

- `StrategyResult.validate()` vergleicht den gesamten gespeicherten Drawdownpfad exakt mit der bestehenden gemeinsamen `drawdown()`-Funktion aus den tatsächlichen Periodenrenditen; die initiale Null wird vorangestellt.
- `validate_results(..., require_complete=True)` verlangt exakt die aktivierten Strategien. Der Runner und `export_run()` verwenden diese vollständige Prüfung; lokale Strategieprüfungen dürfen weiterhin Teilmengen validieren.
- Buy-and-Hold erhält ein additives internes `asset_id`-Feld und wird an das konfigurierte Asset samt dessen tatsächlicher Renditereihe gebunden. Damit sind auch verschiedene Assets mit zufällig identischen Renditen unterscheidbar. CSV-Schemas und normale Berechnung bleiben unverändert.
- Fixed Rebalancing wird gegen die exakte konfigurierte Assetmenge, alle konfigurierten Zielgewichte mit der bisherigen Toleranz `1e-12` und die exakten gemeinsamen jährlichen Trade-Termine geprüft. Konstante Ziele sowie die bisherigen Regeln gegen Start-/Abschlusstrades bleiben erhalten. Auch Ereignisse mit ausschliesslich Nulltransaktionen sind erforderlich.
- `compute_run_metrics()` bündelt ausschliesslich die bisherige Aufruf-/Zusammenführungslogik von `compute_metrics()`. `validate_run_metrics()` berechnet darüber die erwarteten Summary- und Statuswerte: exakte Spalten, geordnete Strategiezuordnung und Zeilenzahl, alle Zahlenwerte, endliche verfügbare Werte sowie passende fehlende Werte und Status. Verfügbare Zahlen werden exakt verglichen, weil dieselbe bestehende Berechnung verwendet wird. Die bisherige flache Statusform für einen Einzelrun und verschachtelte Form für mehrere Strategien bleiben erhalten.
- Der Export prüft zuerst die unveränderten Eingabe-Hashes, danach vollständige Resultate und Summary/Status, alles vor dem Anlegen des Ausgabe- oder Staging-Verzeichnisses. Die bestehenden strengen Trend- und Country-Weighting-Prüfungen werden weiterhin ausgeführt.

**Dateien:** `src/engine/result.py`, `src/strategies/buy_hold.py`, `src/analysis/metrics.py`, `src/engine/simulation.py`, `src/export/results.py`.

**Regressionen:** Die neue Testdatei prüft mittlere/letzte Drawdown-Korruption; jeden Summary-Zahlentyp einschliesslich NaN/Infinity und falsch gefüllter unverfügbarer Kennzahlen; fehlerhafte Spalten, Zeilen und Strategiezuordnung; Einzel-/Mehrstrategie-Status; fehlende/zusätzliche Strategien; falsches Buy-and-Hold-Asset und manipulierte Assetkennung; 20/80 statt 60/40, falsche Assetmenge, fehlende/zusätzliche jährliche Ereignisse sowie Start-/Endtrades. Ein korrektes Ziel innerhalb der bestehenden Toleranz bleibt exportierbar. Alle vier normalen Runner bleiben erfolgreich.

**Ursprüngliche Gegenbeispiele nach Fix:** Geänderte mittlere/letzte Drawdowns, Endwert 999, unendlicher Sharpe und falscher Status werden abgelehnt. Der ursprüngliche unvollständige 20/80-Export scheitert nun am aktivierten Strategie-Set; ein zusätzlich vervollständigter Run mit Buy-and-Hold und 20/80 scheitert gezielt an der 60/40-Konfiguration. Alle Fälle wurden gegen Checkout und Wheel ohne veröffentlichten Run reproduziert.

**Demos und Grenzen:** Bestehende korrekte Ergebnisse und Exportformate bleiben bytegleich. Die strengere Grenze bindet die im Prompt geforderten Result-/Summary-/Konfigurationsmerkmale; sie führt keine zweite Finanzformelsammlung ein. Lokale Teilresultate sind weiterhin zulässig, vollständige Exporte benötigen auch die interne Buy-and-Hold-Assetkennung. Bestehende Fachregeln und strenge Trend-/Makroprüfung bleiben erhalten.

## EB-03 – CSV-Struktur vor pandas

**Befund und Ursache:** Bei drei Headerfeldern und vier Datenfeldern konnte pandas das erste Feld als impliziten Index interpretieren. Dadurch verschob sich beispielsweise das Datum, ohne dass die fachliche Validierung das ursprüngliche CSV-Problem erkannte.

**Korrektur:** `src/data/normalize.py` prüft zentral mit `csv.reader(..., strict=True)` jede CSV-Datenzeile auf exakt die deklarierte Headerbreite, bevor pandas aufgerufen wird. Fehlende/zusätzliche Felder, unbenannte Header, doppelte Header, Leerzeilen und fehlerhafte Quotes werden abgelehnt. Der Fehler nennt Datei, Zeilennummer, erwartete und tatsächliche Feldzahl. Anschliessend liest pandas ausdrücklich mit `index_col=False`. Dies gilt gemeinsam für Markt-, Metadaten-, Risk-Free- und Makrodateien.

Die Strukturprüfung verwendet CSV-Datensätze: Ein korrekt gequotetes Feld mit eingebettetem Komma oder Zeilenumbruch zählt als ein Feld, auch wenn es mehrere physische Textzeilen belegt. Vollständig benannte Zusatzspalten bleiben erlaubt; keine pauschale Maximalspaltenzahl, kein Abschneiden, Verschieben oder Auffüllen.

**Regressionen:** Die neue Testdatei prüft drei Header-/vier Datenfelder, zu wenige und zu viele Felder in allen vier Eingabeklassen, gequotete Kommas und Zeilenumbrüche, erhaltene benannte Zusatzspalten, regulären DataFrame-Index sowie weiterhin abgelehnte doppelte/unbenannte Header, fehlerhafte Quotes und leere Datenzeilen. Ein vollständiger Run mit gequoteten Metadaten und benannter Zusatzspalte bleibt gültig.

**Ursprüngliches Gegenbeispiel nach Fix:** Die originale Datumsverschiebungs-CSV mit `DEMO` wird im Checkout und im Wheel vor pandas abgelehnt: `CSV field count mismatch in overwide-market.csv at line 2: expected 3, got 4.` Kein Run-Ordner entsteht.

**Demos und Grenzen:** Alle vorhandenen CSVs bleiben gültig und erzeugen dieselben fachlichen Ergebnisse. Die Prüfung sichert die Struktur; die vorhandenen fachlichen Datenprüfungen laufen weiterhin danach. Keine Datenreparatur und keine Änderung des akzeptierten CSV-Vertrags.

## Gemeinsame Prüfung und Paketierung

| Prüfung | Tatsächlich ausgeführtes Ergebnis |
|---|---|
| Vollständige Suite vor Änderungen | 344 passed in 61.05s |
| Erste neue Regressionsdatei | 60 bestanden, 2 Testaufbaufehler; beide korrigiert |
| Vollständige Suite nach den Fixes | 406 passed in 59.43s |
| Finaler Checkout, Version 0.4.1 | **406 passed in 64.74s** |
| Frisch installiertes Wheel 0.4.1 | **406 passed in 54.11s** |
| Lokale und frische Paketprüfung | Beide: **No broken requirements found.** |
| Exakte Audit-Reproduktionen | Alle drei Befundgruppen, insgesamt zehn Varianten, in beiden Installationen abgelehnt |
| Vier Demos | Je vier CLI-Runs in Checkout und Wheel, alle Exit 0, offline und unabhängig nachgerechnet |
| Demo-Regression | Alle CSV-Dateien und `data_quality.json` bytegleich zum tatsächlich ausgeführten Stand vor den Fixes |

Insgesamt **344 unveränderte bisherige Tests + 62 neue Fälle**. Die zwei anfänglichen Testaufbaufehler betrafen einen jährlichen Underflow-Fall, der versehentlich schon vor dem Zielereignis Drift-Unterlauf auslöste, sowie Windows-Zeilenumbruchkonvertierung in einer CSV-Fixture. Nur die neuen Fixtures wurden korrigiert; Engine-Anforderungen und bisherige Tests wurden nicht abgeschwächt. Warnungen bleiben Testfehler; der bestehende Netzwerk-Guard bleibt aktiv.

Die Paket-/Quellversionen in `pyproject.toml` und `src/__init__.py` sind 0.4.1. Wheel: `maturarbeit_engine-0.4.1-py3-none-any.whl`, 29363 Bytes, SHA-256 `7041c747a1b455f024980098d35486818409b71cd3c212119c5f5655fed862ef`. Eine frisch erzeugte Umgebung unter `.venv/blocker_fixes/installed` hat `include-system-site-packages = false` und importiert ausschliesslich das installierte Paket aus ihrem `site-packages`. Tests gegen das Wheel wurden aus der temporären Prüfablage aufgerufen. Keine globale Installation; Abhängigkeiten und Lock unverändert. Geprüfte Plattform: Windows / CPython 3.14.0, NumPy 2.3.5, pandas 2.3.3, pytest 8.4.2.

Vier Demo-Endwerte unverändert: Buy-and-Hold **99**, Fixed Rebalancing **116.4284**, Monats-Trend **96.8**, Country-Weighting **117.667**. Sämtliche Strategie-Verläufe, Renditen, Drawdowns und Summary-Werte wurden zusätzlich mit unabhängigen skalaren Kontrollrechnungen geprüft; Signale, GDP-Entscheidungen, Trades und Eingabe-/Ergebnis-/Codehashes ebenfalls. Run-ID, Zeitstempel, Version und Code-Provenienz im Manifest unterscheiden sich erwartungsgemäss. Details und Run-IDs stehen in [testing.md](testing.md).

## Umfang, Dateiliste und Abschluss

Geändert: `pyproject.toml`, `src/__init__.py`, `src/funktionen.py`, `src/data/normalize.py`, `src/engine/portfolio.py`, `src/engine/result.py`, `src/engine/simulation.py`, `src/strategies/buy_hold.py`, `src/analysis/metrics.py`, `src/export/results.py`, `documentation/engine/implementation.md`, `documentation/engine/testing.md` und append-only `documentation/ai-usage/ai-usage-log.md`. Neu: `tests/test_blocker_fixes.py` und dieses Dokument.

93 zu Beginn versionierte Dateien wurden per SHA-256 gesichert. Der Abschlussvergleich und Diff prüfen ausschliesslich diese 13 geänderten vorhandenen Dateien und zwei erlaubten neuen Dateien; alle übrigen Ausgangsdateien bleiben bytegleich. Geschützte wissenschaftliche Inhalte, AGENTS.md, Entscheidungen, beide historischen Auditdateien, sämtliche bisherige Tests, Configs/Demodaten und Abhängigkeitsbindung bleiben unverändert; der bisherige KI-Loginhalt bleibt bytegleich als Präfix erhalten.

Keine neue fachliche oder methodische Entscheidung war erforderlich. Autorvorgaben bleiben OD-01 bis OD-13 und der begrenzte Blocker-Auftrag; Codex ergänzt ausschliesslich technische Prüfstellen, Regressionen, Paketversion und Nachweise. Keine SB-01 bis SB-07 oder NB-01 bis NB-03 bearbeitet, keine realen Daten oder endgültigen Versuchsparameter gewählt. Synthetische Prüfungen auf einer Plattform ersetzen keine fachliche Abnahme durch den Autor. Kein Commit und kein Tag erstellt, kein v1.0-Freeze erklärt. Der Auftrag endet nach diesen drei Fixes.

## EB-02-Restfix nach dem ersten Fix-Review (Engine 0.4.2)

**Auftrag:** [Portfoliozustands-Konsistenzfix](../ai-usage/prompts/2026-10-04-engine-v1-portfolio-state-validation-fix.md), 2026-10-04. Arbeitsbeginn sauber auf `78b7d34`; der vorherige Commit `f05f0bd` enthält die überprüften 0.4.1-Fixes. Die akzeptierten OD-01 bis OD-13 bleiben verbindlich. Dies schliesst ausschliesslich die nach dem ersten Fix-Review verbliebene EB-02-Restlücke; EB-01/03, SB-/NB-Punkte und historische Auditdokumente werden nicht geändert.

### Ursache und unabhängiger Nachweis

Die vollständige 0.4.1-Prüfung band bereits Assetmengen, Ziele, Ereignisse, historische GDP-Entscheidungen, Drawdowns, Summary und Kapitalbilanzen. Zwischen zwei Bewertungen war aber noch nicht nachgewiesen, dass gespeicherte Positionen/Gewichte und Vermögen tatsächlich aus den Performance-Renditen des Kontextes entstanden waren. Algebraisch stimmige Fälschungen konnten deshalb die strenge Run-/Exportgrenze passieren.

Beide Strategien wurden separat mit demselben künstlichen Zwei-Bewertungs-Fall geprüft: Kapital 100, Ziele A/B 60/40, A 100 → 110, B 100 → 100, beide Termine im Jahr 2020 ohne Rebalancing. Country-Weighting besitzt hierfür eine gültige historische GDP-2019-Entscheidung mit Werten 60/40, verfügbar vor dem Start. Unabhängig ergeben gehaltene Positionen 60 → 66 und 40 → 40, somit Vermögen **106** und Driftgewichte **66/106, 40/106**.

Danach wurden bewusst Vermögen **100 → 120**, Rendite **20 %**, Drawdowns **0/0**, unveränderte gültige Ziele, plausibel aussehende Vor-/Nachgewichte **60/40** und leere Trades konstruiert. Die Summary wurde aus dieser falschen History mit der bestehenden Kennzahlenfunktion neu berechnet; GDP-Entscheidung und Provenienz blieben unverändert. Vor dem Fix akzeptierte Version 0.4.1 beide Resultate einschliesslich Export mit Endwert 120. Die temporäre Kontrolle `.venv/portfolio_state_fix/reproduce.py before` dokumentiert beide tatsächlich veröffentlichten künstlichen Gegenbeispiele ausschliesslich in der ignorierten Prüfablage.

### Technische Korrektur und Toleranzen

`validate_results(..., require_complete=True)` ruft nach den bestehenden Struktur-/Config-/GDP-Prüfungen für beide Portfoliostrategien den gemeinsamen `validate_market_portfolio_state()` auf. Dieser verwendet unverändert `run_annual_portfolio()` zur Rekonstruktion des erwarteten gesamten Zustands aus `context.performance`, Startkapital und den bereits geprüften Zielgewichten.

Damit gibt es weiterhin nur eine Portfolio-Zustandsfolge und dieselben Funktionen `allocate_target_values()`, `prozentuale_aenderung()`, `neue_gewichtung()` und `rebalancing()`. Initial gehaltene Positionen verdienen die tatsächlichen Renditen, daraus entstehen Vortradepositionen und Drift, und ausschliesslich an den bestätigten jährlichen Ereignissen werden Zielpositionen gebildet. Diese gehaltenen Positionen werden in die nächste Periode übernommen. Weder gespeicherte falsche Gewichte noch gespeicherte falsche Vermögenswerte bestimmen die Rekonstruktion.

Verglichen werden der vollständige Vermögens-/Renditepfad, alle Vor-/Ziel-/Nachgewichte sowie alle Vortrade-, Ziel- und Transaktionswerte. Gewicht-/Tradezeilen werden nach Datum und Asset ausgerichtet; ihre Reihenfolge bleibt irrelevant. Leere Trade-Tabellen bleiben zulässig, sofern nach bestehendem Kalender kein Ereignis erforderlich ist. Alle Abweichungen führen zu einem klaren Fehler mit Strategie und betroffenem Tabellentyp, bevor der bestehende Export eine Ablage anlegt.

Bestehende Toleranzen bleiben erhalten: Vermögen relativ `CAPITAL_TOLERANCE=1e-12`, ohne kapitalunabhängige absolute Toleranz; Renditen relativ `1e-12` / absolut `1e-14`; Gewichte absolut `WEIGHT_TOLERANCE=1e-12`; Tradebeträge relativ `1e-12` plus die bereits verwendete kapitalabhängige absolute Toleranz `1e-12 × Portfoliowert`. Bereits gegen Config/GDP geprüfte gespeicherte Ziele werden zur Rekonstruktion benutzt, damit die akzeptierte Fixed-Rebalancing-Zieltoleranz nicht durch aufsummierte Unterschiede zu nochmals eingesetzten Config-Gewichten verschärft wird. Country-Ziele bleiben zuvor exakt an die historische GDP-Auswahl gebunden. Keine Gewichtsnormalisierung oder Reparatur eines Resultats.

Der Helper wird erst innerhalb der vollständigen Prüfung importiert, weil das bestehende Portfoliomodul selbst die Resulttypen verwendet. Die Rekonstruktion ruft nur lokale `StrategyResult.validate()` auf; es gibt keine rekursive vollständige Run-Prüfung. Lokale Teilresultvalidierung bleibt erhalten, die wissenschaftliche Exportgrenze ist streng. Initiale Bewertung, Start-/Endtrade-Regeln, gesamte ursprüngliche Portfoliofunktion und mathematische Funktionen bleiben unverändert.

### Regressionen und Ergebnis

Neu ist `tests/test_portfolio_state_validation.py` mit **22 Fällen**, davon 16 negative Gegenbeispiele und sechs positive Kontrollen: gefälschter Endwert 120 statt 106 für beide Strategien und Kapital 100 / `1e-200` / `1e200`; falsche Gewichte bei richtigem Vermögen; falsche Drift zwischen Entscheidungen und am finalen Datum; intern kapitalerhaltende falsche Vortradepositionen samt passenden Trades/Gewichten; verlorene Übernahme der Nachtradepositionen; unabhängige Handrechnung über zwei Jahresereignisse; unveränderter Kontext, beliebige Zeilenreihenfolge und erhaltene Gewichtstoleranz.

Vor Produktionsänderungen wurden **406 Tests bestanden**. Nach Korrektur einer neuen Fixture, die bei Fixed Rebalancing fälschlich eine Makrotabelle voraussetzte, zeigten die neuen Tests auf 0.4.1 genau **16 erwartete Fehlschläge / 6 bestandene Normalfälle**. Nach dem ersten Codefix wurden **20 bestanden / 2 Fehler** gefunden: die zulässige leere Trade-Tabelle besitzt pandas-Objektdtype und benötigte für den Vergleich eine ausdrückliche Float-Sicht. Dieser technische Fehler wurde behoben, ohne Tests oder Toleranzen zu lockern. Die vollständige finale Quellsuite besteht mit **428 Tests**; die bisherigen 406 bleiben unverändert.

Die beiden exakten 100 → 120-Gegenbeispiele werden nach dem Fix an vollständiger Validierung und Export abgelehnt: `rebalance history disagrees with the market portfolio state.` beziehungsweise `country_weighting history disagrees with the market portfolio state.` Kein Ausgabe- oder Staging-Verzeichnis wird dabei angelegt. Beide Reproduktionen wurden auch mit dem frisch installierten 0.4.2-Wheel ausgeführt und werden dort genauso abgelehnt.

Alle vier bestehenden CLI-Demos wurden vor dem Fix mit 0.4.1 und nachher jeweils aus Checkout und Wheel mit 0.4.2 ausgeführt. Alle fachlichen CSV-Dateien und `data_quality.json` bleiben **bytegleich**; unabhängige skalare Rechnungen und Offline-/Hashkontrollen bestehen. Die normalen Endwerte bleiben 99 / 116.4284 / 96.8 / 117.667. Manifest-Version, Codehash, Run-ID und Zeitpunkt unterscheiden sich erwartungsgemäss. Paket-/Suite-Ergebnisse und Run-IDs stehen im aktuellen Abschnitt von [testing.md](testing.md).

### Dateien, Verantwortung und verbleibende Grenzen

Geändert für diesen Restfix: `src/engine/portfolio.py`, `src/engine/result.py`, `src/__init__.py`, `pyproject.toml` sowie die vier beauftragten Dokumentationen `blocker-fixes.md`, `implementation.md`, `testing.md`, `../ai-usage/ai-usage-log.md`. Neu: `tests/test_portfolio_state_validation.py`. Paket-/Quellversion konsistent **0.4.2**, Konfigurationsschema, Exportschemas und Abhängigkeiten unverändert.

Autorvorgaben sind der begrenzte Restfix-Auftrag und die bestehende fachliche Zustandsfolge. Codex wählt ausschliesslich die gemeinsame Rekonstruktion als technische Prüfmethode, ergänzt Regressionen und dokumentiert die ausgeführten Kontrollen. Keine neue fachliche Entscheidung nötig. Die zusätzliche Validierung kostet Rechenzeit, führt aber keine zweite Strategieimplementierung oder neue Finanzformeln ein. Sie prüft Konsistenz mit dem gelieferten Kontext innerhalb der vorhandenen Toleranzen; die historische Wahrheit realer Daten bleibt eine gesonderte Studienvoraussetzung.

Geschützte Dateien und historische Auditnachweise bleiben unverändert. Kein Commit oder Tag erstellt, kein v1.0-Freeze oder realer Hauptversuch. Dieser Auftrag endet nach dem verbleibenden EB-02-Konsistenzfix.
