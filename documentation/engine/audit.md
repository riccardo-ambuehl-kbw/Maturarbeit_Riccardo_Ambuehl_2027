# Audit der geplanten Backtesting-Engine

**Datum:** 2026-10-02

**Auftrag:** [Vollständiger Audit-Prompt](../ai-usage/prompts/2026-10-02-engine-audit.md)

**Geprüfte Git-Version:** `cb8dfb817eb14edb8f8c0e22a468a519670aee0c`

**Ausführung:** Codex; ausschliesslich Prüfung und Dokumentation, keine Engine-Implementierung.

## 1. Ergebnis und Abgrenzung

Der aktuelle Stand beschreibt einen brauchbaren Daten-, Ergebnis- und Architekturrahmen, reicht aber **noch nicht für eine vollständig eindeutige, reproduzierbare Implementierung aller vorgesehenen Strategien**. Insbesondere fehlen verbindliche Regeln für Kalender/Perioden, SMA-Vorlauf, Cash, Rebalancing, risikofreie Periodenrenditen, Währungen und BIP-Verfügbarkeit. Zusätzlich bestehen Quellenwidersprüche und reproduzierbare Integrationsfehler im vorhandenen Code.

Das [Entscheidungsregister](open-decisions.md) enthält **13 BLOCKING-Entscheidungen** und **6 NON-BLOCKING-Entscheidungen**. Die bewusst vertagte endgültige Auswahl von Wertpapieren, Zeitraum, risikofreier Serie und SMA-Parametern ist kein Hindernis für Tests einer allgemeinen Engine mit künstlichen Daten. Eine ungeklärte Berechnungs- oder Zeitregel darf dagegen nicht durch einen stillen Standardwert ersetzt werden.

In diesem Audit wurden alle 18 bestehenden Funktionen statisch mit der Theorie verglichen, unveränderte Funktionsdefinitionen isoliert mit künstlichen Daten ausgeführt und die Python-Umgebung geprüft. Es wurden keine Marktdaten geladen, keine Pakete installiert, keine Konfigurationen oder Tests angelegt und keine mathematischen Funktionen geändert. Die nachstehenden Entwürfe sind Dokumentation für einen späteren bestätigten Implementierungsauftrag.

Die Quellen wurden auf interne Konsistenz geprüft. Dies ist keine unabhängige Validierung sämtlicher zitierter Finanzliteratur und keine Eignungsprüfung noch nicht ausgewählter realer Datensätze.

## 2. Gelesene Quellen und Belegstellen

Notebook-Zellnummern sind in diesem Dokument nullbasiert und beziehen sich auf den geprüften Stand. Sämtliche Quelltexte der bezeichneten Kapitel, einschliesslich Codebeispielen, wurden gelesen; die Notebooks wurden nicht als Ganzes ausgeführt.

| Datei | Vollständig gelesener relevanter Bereich | Bedeutung für den Audit |
|---|---|---|
| `AGENTS.md` | Gesamte Datei | Fachliche Grenzen, Wiederverwendung, Datenlücken, Tests, geschützte Inhalte, KI-Nachweis |
| `documentation/ai-usage/prompts/2026-10-02-engine-audit.md` | Gesamter Abschnitt „Vollständiger Prompt“ und Dokumentrahmen | Umfang, drei erlaubte Dokumentationsdateien, verpflichtender Stopp |
| `notebooks/Analyse.ipynb` | 5.1–5.9 vollständig; Zellen 1–110 | 5.3 Datenvertrag; 5.4 Adapter; 5.5 Validierung/Frequenz; 5.6 JSON; 5.7 Outputs; 5.8 Architektur/Ablauf; 5.9 bestehende Funktionen |
| `notebooks/Theorie.ipynb` | 3.2–3.13 vollständig; Beginn von 3.2 in Zelle 1, bis Zelle 81; zusätzlich 3.1 als Kontext | Rendite und Faktoren, Annualisierung, Volatilität, Drawdown, Sharpe, Korrelation, Drift, Buy-and-Hold, 60/40, BIP, SMA, Bias |
| `src/funktionen.py` | Gesamte Datei, alle 18 Funktionen, Zeilen 1–113 | Ausgangspunkt für mathematische Wiederverwendung und Gegenbeispiele |
| `methodik.qmd` | Gesamte Datei | Vergleichsbedingungen, jährliches 60/40-Rebalancing, Dividenden, Kosten-/Inflationsausschluss, noch unvollständige Versuchsparameter |
| `documentation/ai-usage/README.md` | Gesamte Datei | Pflichtinformationen für diesen KI-Nutzungseintrag |
| `documentation/ai-usage/ai-usage-log.md` | Gesamter bestehender Inhalt | Format und klare Trennung bisheriger Einträge vom neuen Audit |
| `README.md`, `.gitignore`, `_quarto.yml` | Gesamte Dateien | Projektstruktur, Python-Empfehlung, Bibliotheksideen, Notebook-/Book-Umgebung, ignorierte Artefakte |
| Installierte Paketmetadaten und relevante Quellfunktionen von QuantStats 0.0.81 | `stats.sharpe`, `utils._prepare_returns`, zugehörige Validierungs-/Cachefunktionen; `stats.to_drawdown_series` gelesen | Tatsächliche Vorverarbeitung und transitive Abhängigkeiten; kein Ersatz des bestehenden Codes |

Ein AST-Vergleich ergab: **Alle 18 Definitionen in `src/funktionen.py` entsprechen den Funktionsdefinitionen im Theorie-Notebook**, abgesehen von Kommentaren/Formatierung. Die gefundenen Fehler sind daher keine fehlerhafte Übertragung in `src`, sondern bestehen bereits in den Notebook-Beispielen bzw. ihrer Nutzung als allgemeine Schnittstelle.

SHA-256 der wichtigsten unveränderten Quellen:

| Datei | SHA-256 |
|---|---|
| `notebooks/Analyse.ipynb` | `efe4922988cc890fd46b0214441865d537a32874e228e57ab3f1699a3c977125` |
| `notebooks/Theorie.ipynb` | `fe0f5b212b442da04fd8debc6679e0b90be0f4e5e353f53785b4f51f9384e761` |
| `methodik.qmd` | `bb7b989134b0b471851e72f657daacb568d9767f45af4326baa2bf93bb0c39b0` |
| `src/funktionen.py` | `fb900b7f5444142b5302b59651965f7154e370c0ec5fc8a337321fa2b7db7c0b` |

## 3. Zuordnung A–D und bereits festgelegte Anforderungen

**A** bedeutet vom Autor bereits festgelegt; **B** eine technische Ausgestaltung, die Codex später innerhalb dieser Vorgaben wählen darf; **C** eine noch offene fachliche/methodische Entscheidung des Autors; **D** einen Quellenwiderspruch. Bei einer Mischlage bleibt der festgelegte Teil verbindlich, während die offenen Teile im Entscheidungsregister stehen.

| Thema | A: festgelegt | B: technische Ausgestaltung | C/D: offene Regel oder Widerspruch |
|---|---|---|---|
| Allgemeines System vs. Untersuchung | Wiederverwendbare Engine; Versuchswerte später festlegen, vor Hauptlauf fixieren | Konfiguration validieren, Versionen erfassen | C: OD-14–OD-18; keine Auswahl anhand bester Ergebnisse |
| Marktvertrag | CSV Long mit `date, asset_id, performance_value`; optional `signal_value`; intern pandas, bei Bedarf Wide | Datentypprüfung, Mapping, Pivot, deterministische Sortierung | C: Kalender und Perioden OD-01/OD-02 |
| Performance/Dividenden | Performance-Reihe muss Reinvestition der Dividenden abbilden; Quelle/Spalte/Adjustierung dokumentieren | Import-Provenienz und Eignungskennzeichnung | C: konkrete Reihen OD-14; Netto-ETF-/Brutto-Indexunterschiede prüfen |
| Signalreihe | Signal und Performance getrennt; Fallback nur ausdrücklich in Konfiguration | Zwei getrennte Datenansichten und geprüfte gemeinsame Indizes | C: Vorlauf/Cash OD-04/OD-05; konkrete Signalreihe OD-17 |
| Metadaten | `assets.csv`: `asset_id, name, asset_class, country, currency, provider, provider_symbol` | Eindeutiger Stammdatenschlüssel, referenzielle Prüfung | C: Währungen OD-10, Länderabbildung OD-11 |
| Risikofreie Daten | Eigene Tabelle mit `date, series_id, value, unit`; gleiche Periodenlogik wie Renditen | Serienauswahl aus expliziten Eingaben, Einheitenprüfung | C: OD-07; D: Sharpe-Nenner OD-08 |
| Makrodaten | Eigene Tabelle mit `period, country, indicator, value, unit, available_from` | Schlüsselkonsistenz, dokumentierte Versions-/Verfügbarkeitsprüfung | C: BIP-Regeln OD-11/OD-12; konkrete Daten OD-18 |
| Import | Anbieteradapter und eigener CSV-Import; `asset_id` unabhängig vom Ticker | Explizites Mapping von Anbietersymbol zu `asset_id`, getrennte Importbefehle | Die beispielhafte CSV-Zuordnung auf `provider_symbol` allein erfüllt noch nicht die Pflichtspalte `asset_id` |
| Datenstand | Rohdaten und verarbeitete Daten getrennt, Originale erhalten | Datei-Hashes, Adapterversion und Transformationsbericht | Keine nachträgliche unprotokollierte Rohdatenänderung |
| Validierung | Pflichtspalten, Datum, numerische Werte, Kennungen, Duplikate, NaN/Inf, Zeitraum je Anlage prüfen; Datenbericht | Präzise Fehlercodes, Prüfung der tatsächlich benötigten Reihen | C: Lücken-/Kalenderregel OD-01; D: implizite Auffüllung/Entfernung im Code |
| Resampling | Letzter verfügbarer Wert eines abgeschlossenen Intervalls; Renditen über Faktoren verknüpfen; keine Zukunftsinformation | Typabhängiger Wrapper, explizite Intervallbeschriftung | C: Grenzen/Frequenz OD-02/OD-03; beliebige Aggregation des Helpers ist keine freigegebene Regel |
| Konfiguration | JSON, allgemeine und strategieabhängige Einstellungen, aktivierbare Strategien | Vollständiges Schema mit Typ-/Bereichs-/Referenzprüfung | Beispiel unvollständig: Frequenz, Fehlwertregel, Signal-Fallback, Cash, RF, BIP und Datenreferenzen fehlen; keine Beispielwerte als Defaults |
| Buy-and-Hold | Einmal investiertes Kapital, reinvestierte Erträge, passive Benchmark | Wrapper auf `buy_and_hold`, gemeinsame Ausgabe | C: Startgewicht/Kapitalrest OD-13 |
| Rebalancing/60/40 | Drift und jährliches Rebalancing; Untersuchung 60 % Aktien/40 % Anleihen; allgemeines Modul kann andere Zielgewichte erhalten | Kalenderereignisse und Zustandsschritte, Wiederverwendung der Helpers | C/D: OD-06; nicht jede Periode mit festen Gewichten rechnen |
| Ländergewichtung | Theorie beschreibt BIP-Ländergewichte; Architektur plant `country_weighting.py` | Gemeinsame Portfoliohelpers; technische Konfigurations-/Outputstruktur ergänzen | C/D: OD-11/OD-12; Methodik beschreibt breiteren ETF-Ansatz |
| Trendfolge | SMA kurz/lang; Long/Cash; Gleichheit ergibt Cash; Signal wirkt eine Periode später | Signal aus `signal_value`, Rendite aus `performance_value`; keine Long/Short-Umstellung | C: OD-04/OD-05; vorhandener Helper verbindet beide Aufgaben in einer Reihe |
| Kennzahlen | Einfache Renditen, geometrische Faktoren, Stichproben-Std `ddof=1`, Skalierung über `m`, negative Drawdowns | Gemeinsame Auswertung und Eingabevertrag | C: `m` OD-03; D: Start-HWM OD-09, Sharpe OD-08 |
| Ergebnis | Vollständiger gemeinsamer Portfolioverlauf, optionale Gewichte/Trades/Signale, Zusammenfassung, Manifest | Einheitliche Struktur, geprüfte Exporttypen und Dateireihenfolge | C: Startzustand OD-02, zusätzliche wissenschaftliche Kennzahlen OD-19 |
| Architektur | `data`, `engine`, `strategies`, `analysis`, `export`; `strategy.run(context, params)` | Einfache Datenklassen/Module und lokale Orchestrierung | Keine neue methodische Logik im zentralen Runner |
| Reproduzierbarkeit | Konfiguration, Datenstand, Laufzeitpunkt und Codeversion zurückverfolgen; keine Downloads im Backtest | Hashes, Umgebungsversionsliste, Offline-Test, Schutz vor Überschreiben | „Später Git-Version“ aus 5.7.3 muss spätestens beim ersten reproduzierbaren Lauf erfüllt sein (AGENTS.md) |
| Methodische Vereinfachungen | Gleiches Startkapital, Dividendenreinvestition, gleiche Frequenz; keine Transaktionskosten, Steuern, Inflation oder weiteren Gebühren | Annahmen in Ergebnis/Manifest beschreiben | Keine stillen Kosten- oder Inflationsmodelle hinzufügen; bereits in Kursdaten enthaltene Fondsgebühren sind dadurch nicht rückgerechnet |

Die Diskussion realer Renditen in Theorie 3.3.4/3.13.4 und die Kostenwarnungen widersprechen dem bewusst vereinfachten nominalen Backtest nicht automatisch. Sie begrenzen seine Aussagekraft. Allgemein konfigurierbare Rebalancing-Rhythmen widersprechen ebenfalls nicht der festen jährlichen Untersuchung; beide Ebenen müssen getrennt bleiben.

## 4. Datenvertrag und nötige Integrationssicherungen

### 4.1 Markt- und Metadaten

Vor jedem Pivot muss `(date, asset_id)` eindeutig sein. Datumsnormalisierung darf Duplikate nicht verbergen. Kennungen sind Strings, Werte müssen numerisch und endlich sein; positive Wertreihen werden für die vorhandenen Preis-/Logarithmusfunktionen benötigt. Nullwerte, negative Werte oder ein Totalverlust dürfen nicht durch beliebiges Clipping repariert werden. Wenn diese Zustände unterstützt werden sollen, braucht ihr fachlicher Umgang eine explizite Erweiterung; andernfalls mit begründetem Validierungsfehler ablehnen.

`asset_id` muss zu einem eindeutigen Metadateneintrag und allen konfigurierten Strategiereferenzen passen. Die CSV-Umbenennung `Ticker -> provider_symbol` aus 5.4.4 benötigt zusätzlich ein explizites Stammdatenmapping auf `asset_id`. Der Code darf einen Ticker nicht still zur anbieterunabhängigen Modellkennung erklären.

Rohdaten, Performance-Wide-Tabelle und Signal-Wide-Tabelle bleiben nachvollziehbar getrennt. Eine vorhandene, aber teilweise fehlende Signalspalte ist kein automatischer Anlass für einen zeilenweisen Performance-Fallback. Ob dieser Fall überhaupt zulässig sein soll, muss ausdrücklich spezifiziert werden; sicher ist zunächst ein Fehler. Die fehlende Spalte insgesamt darf nur bei expliziter Erlaubnis auf Performance abgebildet werden.

Einheiten, Total-Return-Bedeutung und Dividenden-/Splitbehandlung müssen durch Herkunftsinformationen belegt sein. Die Engine kann eine Behauptung im Metadatensatz validieren, aber aus Zahlen allein keinen Total Return beweisen. Signale aus später adjustierten Reihen sind bei der konkreten Datenwahl auf zeitliche Eignung zu prüfen.

### 4.2 Kalender, Lücken und Frequenz

Die Validierung unterscheidet: tatsächliches NaN in einer gelieferten Zeile, vollständig fehlende Zeile an erwartetem Handelstag, legitimer Marktschliessungstag, fehlende Anlage, fehlende Vorlaufhistorie und fehlende Zins-/Makrobeobachtung. Aus einem lückenhaften Datensatz allein kann nicht entschieden werden, welche Kategorie vorliegt; ein Kalender oder explizite Datenbeschreibung wird benötigt (OD-01).

Wertreihen zuerst auf gemeinsame bestätigte Bewertungszeitpunkte ausrichten, **danach** periodische Renditen bilden. Die Schnittmenge bereits berechneter Rendite-Enddaten ist unzureichend, wenn ihre Startpunkte abweichen. Ein gemeinsamer Vergleich benötigt auch gleiche Anfangs-/Endgrenzen, Währung und Frequenz. Beobachtungszahlen, entfernte Zeitpunkte und die effektive Abdeckung je Anlage gehören in den Datenbericht.

Für Werte ist die letzte beobachtete Information eines abgeschlossenen Intervalls zulässig; ein Ergebnislabel darf nicht vor deren Verfügbarkeit liegen. Für Renditen ist die Verknüpfung `Produkt(1+r)-1` nötig. Ein aggregiertes Intervall benötigt trotzdem eine geprüfte vollständige Eingabestichprobe: das Standardverhalten von `prod`, `last` oder Statistikfunktionen darf fehlende erforderliche Beobachtungen nicht still verschlucken. Aus gröberen Reihen dürfen keine feineren Marktwerte erzeugt werden.

`MS` mit `last` beschriftet einen Monatsendwert am Monatsanfang und ist daher unzulässig. `ME` und ähnliche Labels müssen mit tatsächlich abgeschlossenen Intervallen und dem Betrachtungsende übereinstimmen. Die in Theorie 3.2 abgedruckten älteren Aliasnamen sind kein versionsunabhängiger API-Vertrag; technische Aliasnormalisierung ist erlaubt, die Periodenbedeutung muss erhalten bleiben. Beschriftung und Entscheidungszeitpunkt sind getrennt von der letzten realen Marktbeobachtung zu prüfen.

### 4.3 Zinsen und BIP

Zinswerte werden erst nach bestätigter Einheit/Zinskonvention in Dezimalrenditen der gehaltenen Perioden umgerechnet (OD-07). Prozent und Dezimalanteil, Jahreszins und Periodenrendite sowie Beobachtungs- und Verfügbarkeitsdatum sind unterscheidbare Größen. Die risikofreie Reihe muss vor `sharpe_ratio` mit den ausgewerteten Renditeintervallen exakt übereinstimmen. Unbekannte RF-Werte sind weder 0 noch automatisch der letzte bekannte Wert.

Für BIP müssen Einheit, Indikator, Länderabbildung, Bezugszeitraum, Veröffentlichung und Revision zusammenpassen (OD-11/OD-12). Mehrere Vintages derselben Länderperiode dürfen gespeichert werden, wenn ihre Verfügbarkeitsversionen eindeutig identifiziert werden; echte doppelte Versionen sind Fehler. Eine datierte Zeile mit `available_from` kann nur dann historisch korrekt sein, wenn der gespeicherte Wert dieser damals verfügbaren Version entspricht. Die Versions-/Quellenprovenienz ist technisch speicherbar, ersetzt aber keine methodische Vintage-Regel.

Der Context darf die ganze Makrotabelle enthalten; die Strategie darf an einem Zeitpunkt dennoch nur die zulässige historische Sicht verwenden. Dasselbe gilt für künftige Marktdaten in einem vorbereiteten DataFrame: vollständiges Laden allein ist kein Bias, ihre Verwendung in einer früheren Entscheidung wäre einer.

## 5. Anforderungen, bestehende Funktionen und geplante Tests

Die Testbezeichnungen beschreiben **spätere** automatisierte Tests; diese Dateien wurden nicht angelegt. Die tatsächlich ausgeführten Audit-Prüfungen stehen in Abschnitt 7. Eingabevalidierung und Wrapper sind gegenüber parallelen mathematischen Neuentwicklungen zu bevorzugen.

| Anforderung / Quelle | Bestehende Funktion; Eingabe -> Ausgabe | Nötige Integration/Erweiterung | Geplanter Test |
|---|---|---|---|
| Frequenz, Theorie 3.2 / Analyse 5.5.4 | `resample_dataframe`: DataFrame mit Zeitindex, Frequenz, Aggregationsdict -> DataFrame | Datenart, Intervalllabel, Grenzen und Vollständigkeit prüfen; Wert-/Renditeaggregation getrennt | T-D01: Monats-/Wochenende, Feiertag, NaN-Endwert, leeres/angebrochenes Intervall, `MS+last` ablehnen, zwei Renditen +10 %/-10 % ergeben -1 % |
| Absolute Änderung, 3.3.1 | `absolute_aenderung`: Series -> Differenz-Series, erster Wert NaN | Nur ergänzende Diagnose; Zeitreihenreihenfolge vorher prüfen | T-M01: `[100,110,126.5] -> [NaN,10,16.5]`; doppelte/unsortierte Daten vorgelagert prüfen |
| Einfache Rendite, 3.3.1 | `prozentuale_aenderung`: Werte-Series -> relative Änderung, erster Wert NaN | Vorab Kalender/Lücken prüfen; implizites Fill deaktivieren bzw. NaN-Eingaben strikt ausschliessen | T-M02: +10 %/+15 %; `[100,NaN,110]` darf keine erfundene Nullrendite ergeben; Nullnenner/Inf ablehnen |
| Kumulierte Logrendite, 3.3.2 | `kumulierte_rendite`: positive Werte-Series -> kumulierte Logrendite, erster Wert NaN | Funktionsname nicht mit einfacher Gesamtrendite verwechseln; keine Lücken überspringen | T-M03: Endwert `log(1.265)`; NaN/0/negative Werte werden vorher zurückgewiesen |
| Wachstum, 3.3.2 | `wachstumsfaktor`: positive Werte-Series -> Faktor-Series, erster Wert NaN | Explizite Startbewertung; einfache Gesamtrendite = Endfaktor - 1 | T-M04: Endfaktor 1.265; Skalierung der Preisreihe verändert Ergebnis nicht |
| Geometrisches Mittel, 3.3.3 | `geometrisches_mittel`: positive Faktoren-array -> Skalar | Eingabe immer `1+r`; array/Series normalisieren, NaN/leer/nichtpositive Faktoren prüfen | T-M05: `[1.1,.9] -> sqrt(.99)`; keine simple-rendite-Eingabe, kein typeabhängiges NaN-Überspringen |
| Annualisierte Rendite, 3.3.3 | `annualisierte_rendite`: Faktoren-array, positives `m` -> Skalar | OD-03; Startzeile nicht mitzählen; Periodenanzahl dokumentieren | T-M06: zwei Faktoren und `m=12` ergeben `.99**6-1`; ungültiges `m`/unregelmässige Intervalle ablehnen |
| Stichprobenstreuung, 3.4.2 | `standardabweichung`: 1-D Renditen -> Skalar, `ddof=1` | Endliche echte Renditestichprobe prüfen; weniger als zwei Beobachtungen sind nicht definiert | T-M07: `[.1,-.1] -> sqrt(.02)`; konstant, leer, ein Wert und NaN behandeln |
| Annualisierte Volatilität, 3.4.3 | `annualisierte_volatilitaet`: Renditen, `m` -> Skalar | Gemeinsames `m`; keine andere Autokorrelationsmethode still hinzufügen | T-M08: `[.1,-.1], m=12 -> sqrt(.24)`; Faktor-/Renditevertrag prüfen |
| Drawdown, 3.5.2 | `drawdown`: Renditen-Series -> negative Drawdown-Series | OD-09; Start-HWM 1/Startkapital fehlt derzeit; Wrapper nach Bestätigung; NaN-Prüfung | T-M09: erster Verlust -10 %, zweite -10 % -> -10 %/-19 %; neue Hochs, vollständige Erholung, Konstanz |
| Maximum Drawdown, 3.5.2 | `maximum_drawdown`: Renditen-Series -> Minimum | Dieselbe korrigierte Ausgangsbewertung wie Verlauf, keine getrennte Formel | T-M10: -19 % im Anfangsverlustbeispiel; identisch zu Minimum des exportierten Drawdowns |
| Sharpe, 3.6 | `sharpe_ratio`: Anlagen- und RF-Renditen-Series, `m` -> Skalar über QuantStats | OD-07/OD-08; gemeinsame Intervalle/Indizes und Endlichkeit; QuantStats-Nullersetzung und Preisheuristik absichern | T-M11: Handformel mit konstantem und variablem RF; verschobener Index/Lücke muss Fehler sein; Renditen über 100 % nicht als Preise behandeln |
| Korrelation, 3.7.2 | `korrelationsmatrix`: Renditen-DataFrame -> Matrix | Vollständig gemeinsame Stichprobe statt still paarweiser Auswahl; konstante Reihen und geringe Stichprobe kenntlich machen | T-M12: ±1, Symmetrie, identische Spalten; unterschiedliche Lücken dürfen keine uneinheitlichen Paarstichproben erzeugen |
| Portfolio-Risiko, 3.7.2 | `portfolio_risiko`: Renditen-DataFrame, Gewichte-Series/array -> `(Varianz, Volatilität)` pro Periode | Labels explizit ausrichten, Gewichte validieren (OD-13), vollständige Stichprobe; nur feste Gewichtungsanalyse | T-M13: zwei gegenläufige Reihen mit .5/.5 ergeben 0; vertauschte Labels identisch; array-Reihenfolge kontrollieren; nicht als Risikokennzahl eines driftenden Verlaufs ausgeben |
| Drift, 3.8.2 | `neue_gewichtung`: Positionswerte-Series, Renditen-Series -> `(neue Werte, neue Gewichte)` | Gleiche Asset-Labels, finite Werte, zulässiger Gesamtwert; keine fehlenden Anlagen durch `sum(skipna)` verlieren | T-S01: 60/40 und +10 %/0 % -> 66/40, Summe 106; fehlende Anlage/Rendite Fehler; Gewichte summieren sich auf 1 |
| Rebalancing, 3.8.2 | `rebalancing`: Positionswerte, Zielgewichte -> fünf Series für vor/ziel/Trades | OD-06/OD-13; nach Ausführung Zustand auf Zielwerte setzen; kein Ausführungsmodell im Helper vorhanden | T-S02: 66/40 -> 63.6/42.4, Trades -2.4/+2.4, Gesamtwert erhalten; kein jährliches Ereignis doppelt |
| Buy-and-Hold, 3.9 | `buy_and_hold`: Renditen-Series, Kapital -> Vermögens-Series nach Perioden | Startzeile und gemeinsames Ergebnis ergänzen; NaN darf nicht kumulativ übersprungen werden | T-S03: Kapital 100, +10 %/-10 % -> 110/99; Datumsstart gemäss OD-02, keine laufenden Trades |
| SMA/Long-Cash, 3.12 | `trendfolge`: eine Werte-Series, Fenster -> DataFrame `Kurs, SMA kurz, SMA lang, Signal, Marktrendite, Strategierendite` | OD-04/OD-05; positive ganze Fenster; Signal auf Signalreihe, Rendite separat auf Performance; vor Aufruf keine stillen Datumsverluste zulassen | T-S04: strikte Kreuzung/Gleichheit, erstes vollständiges Signal erst nächste Periode, fehlender Vorlauf, separate Reihen, expliziter/fehlender Fallback |
| BIP-Strategie, 3.11 / Analyse 5.8 | Kein bestehender vollständiger Helper; `neue_gewichtung`/`rebalancing` als Portfolio-Bausteine | Erst OD-11/OD-12 klären; neue kleine Gewichtsermittlung erforderlich, keine fremde Framework-Engine | T-S05: synthetische BIP-Werte 2/1 -> 2/3 und 1/3; Publikationsgrenze, Revision, fehlendes Land, gleichwertige Einheit, Drift und bestätigtes Rebalancing |
| Import, JSON, Datenbericht, Context, Outputs, Manifest, 5.3–5.8 | Keine vorhandenen Implementierungen | Technische Module innerhalb des vorgegebenen Rahmens; Schnittstellen validieren | T-I01: Schema-/Mapping-/Duplikatfehler; unbekannte Parameter/Assets; deterministische Exporte, Hashänderungen, Offline-End-to-End-Lauf |

Statisch wichtige Randfälle: Viele Helpers prüfen weder leer/NaN/Inf noch Datumsreihenfolge, Periodenlänge oder fachliche Einheiten. pandas-Statistikfunktionen können fehlende Werte ignorieren; `corr`/`cov` können paarweise unterschiedliche Stichproben verwenden. numpy-array-Gewichte sind positionsabhängig, Series-Gewichte labelabhängig. `rebalancing` verändert das Eingabeportfolio nicht. `portfolio_risiko` annualisiert nicht und beschreibt keinen tatsächlich simulierten Verlauf mit wechselnden Gewichten. Keine dieser Eigenschaften darf bei Integration verborgen bleiben.

Undefined Kennzahlen bei leerer/zu kurzer Stichprobe oder Nullvolatilität dürfen technisch als fehlend mit Begründung exportiert werden, statt als 0. Eine minimale Implementierung kann solche Runs alternativ mit einem klaren Fehler ablehnen. Die technische Darstellung muss eindeutig sein; sobald solche Fälle wissenschaftlich gerankt oder durch eine andere Kennzahl ersetzt werden sollen, ist eine zusätzliche Autorenentscheidung erforderlich.

## 6. Widersprüche und Risiken mit Gegenbeispielen

### 6.1 Quellenwidersprüche und unvollständige Spezifikation

| Befund | Beleg und Bedeutung | Vorgehen im späteren Auftrag |
|---|---|---|
| **D-01: Drawdown-Formel vs. Code** | Theorie 3.5.2 verlangt `max(V_0,...,V_t)`. `src/funktionen.py:48–55` und Notebook-Zelle 36 bilden den Höchststand erst ab dem ersten Renditewert. R2 zeigt unterschätzte Anfangsverluste. | OD-09 vom Autor bestätigen lassen; Startzustand/Wrapper mit Test ergänzen, Definition nicht still ändern |
| **D-02: Sharpe-Theorie vs. Methodik** | Theorie 3.6.2 und Code verwenden Std der Überschussrenditen; die Methodik nennt Strategievolatilität. Ein variables RF verändert den Nenner. | OD-08 klären; Text und Implementierung erst in einem dafür freigegebenen Arbeitsschritt konsistent machen |
| **D-03: BIP-Strategieumfang** | Theorie 3.11 beschreibt reine BIP-Ländergewichtung; Methodik beschreibt einen ETF mit gemischter Marktkapitalisierung/BIP und Faktoren. Analyse plant ein Ländergewichtungsmodul, aber keine eindeutige Gesamtregel. | Als Umfangskonflikt melden, nicht behaupten, dass die Methoden gleich sind; OD-11/OD-12 |
| **D-04: feste 60/40-Formel vs. jährliche Drift** | Formel 3.10.1 mit konstant .60/.40 steht neben Drift 3.8.2 und jährlichem Rebalancing. Sie kann als Momentaufnahme gemeint sein; eine Anwendung für jede Periode wäre widersprüchlich. R14 unterscheidet beide Ergebnisse. | Mehrdeutigkeit ausdrücklich klären (OD-06), keine still gewählte Auslegung |
| **D-05: unvollständige Gewichte im Theoriebeispiel** | Zelle 52 verwendet .20/.40/.20, Summe .80, ohne Erklärung der verbleibenden .20. Die Kovarianzrechnung ist algebraisch möglich, der Gesamtportfoliozustand nicht vollständig beschrieben. | OD-13; weder Gewichte normalisieren noch Cash erfinden |
| **D-06: Fehlwertregeln vs. Codeverhalten** | AGENTS.md/Analyse 5.5 verlangen sichtbare Lücken ohne still erzeugte Werte. pandas 2.3.3 füllt bei `pct_change()` standardmässig; `trendfolge` entfernt NaN-Zeilen; QuantStats füllt fehlende Überschussrenditen mit 0. | Technische Sicherungen nach bestätigter Kalenderregel; R1/R3/R5; keine Änderungen in diesem Audit |

Weitere Risiken sind **keine automatisch neuen fachlichen Definitionen**: der nicht lauffähige Paketimport; fehlende JSON-Pflichtfelder; fehlende Datenprovenienz; die Vermischung von Renditen und Faktoren; ungeprüfte Einheiten/Asset-Labels; die Wiederaufnahme kumulativer Reihen nach NaN; nicht validierte SMA-Fenster und die Preisheuristik des Sharpe-Pakets. Sie verlangen sichtbare technische Integrationsarbeit und Tests.

### 6.2 Tatsächlich ausgeführte kleine Beispiele

Alle Zahlen sind künstliche Audit-Daten, keine Versuchsauswahl. Dezimalrenditen sind verwendet; numerische Ergebnisse sind gerundet. Bei R5/R6 wurde der unveränderte Sharpe-Code mit isoliert geladenen Definitionen aus der **installierten** QuantStats-Version ausgeführt, nicht über einen erfolgreichen Paketimport.

| ID | Minimale Eingabe / Aufruf | Beobachtet | Erwartung bzw. offener Punkt und Quellenbezug |
|---|---|---|---|
| R1 | `prozentuale_aenderung(Series([100, NaN, 110]))` | `[NaN, 0, .10]` plus pandas-FutureWarning | Eine nicht beobachtete Marktperiode wird zur Nullrendite. Analyse 5.5.3/AGENTS.md widersprechen diesem impliziten Fill. Explizites `fill_method=None` und vorgelagerte Validierung später vorschlagen. [pandas 2.3.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.pct_change.html) dokumentiert dieses versionsabhängige Verhalten. |
| R2 | `drawdown(Series([-.10, -.10]))`, `maximum_drawdown(...)` | `[0, -.10]`, MDD -.10 | Theorie 3.5.2 mit Startwert 1: Vermögen .90/.81, Drawdown -.10/-.19, MDD -.19. OD-09. |
| R3 | `trendfolge(Series([100, NaN, 110, 120], täglicher Index), 1, 2)` | Vier Termine werden zu drei: 01.01., 03.01., 04.01.; am 03.01. erscheint .10 als Marktrendite | Die Rendite überspannt die entfernte Beobachtung; Beobachtungsfenster und Lag laufen nun auf anderem Kalender. Analyse 5.5/5.7: Datum nicht unbemerkt entfernen. OD-01. |
| R4 | `trendfolge(Series([100,110,120]), 1, 3)` | Langer SMA `[NaN,NaN,110]`, Signal `[0,0,1]`, Strategie `[NaN,0,0]` | Cash während nicht definiertem SMA ist durch die Formel nicht entschieden. Erst gültiges Signal wirkt nächste Periode. OD-04. |
| R5 | Anlage `[.02,.03,.04]` an drei Tagen; RF `[.01,.01]` nur an den ersten zwei Tagen; `m=12` | Überschüsse `[.01,.02,NaN]` werden intern `[.01,.02,0]`; Sharpe 3.464102 | Kein zulässiger vollständiger Vergleich. Nur zwei passende Paare ergäben 7.348469, aber auch diese Stichprobenverkürzung wäre zu genehmigen. Theorie 3.6/Analyse 5.3.7; vorab fehlende RF-Periode erkennen, OD-07. |
| R6 | Anlagenrenditen `[1.1,1.2,1.3]`, RF 0, `m=12` | QuantStats deutet durchweg nichtnegative Überschüsse mit Maximum >1 als Preise; Sharpe 3.988706 | Explizite Theorieformel für diese Renditen ergibt 41.569219. Renditen von mehr als 100 % sind keine Preisreihe. Fachlich korrekte Eingabesemantik muss technisch abgesichert werden; nicht durch Ablehnung aller >100%-Renditen umgehen. |
| R7 | `neue_gewichtung({'A':60,'B':40}, {'A':.10})` | Werte A=66, B=NaN; Summe 66; Gewicht A=1 | Fehlende Rendite lässt Vermögen B bei `sum()` verschwinden. Theorie 3.8/Analyse 5.5: gleiche, vollständige Labels verlangen. |
| R8 | `rebalancing({'A':60,'B':40}, {'A':.5,'B':.4})` | Transaktionen summieren sich auf -10 | Restvermögen fehlt ohne Cash-Zustand. Gewichtssumme und erlaubtes Kapitalmodell sind OD-13; innerhalb des bestätigten Modells streng validieren. |
| R9 | Januarwerte 100 am 01.01., 110 am 31.01.; `resample_dataframe(...,'MS',{'v':'last'})` | Wert 110 wird mit 01.01. beschriftet | Monatsendinformation liegt scheinbar am Anfang vor. Theorie 3.13.2/Analyse 5.5.4; Intervalllabel kontrollieren. [pandas-Resampling](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.resample.html) stellt die technischen Label-/Intervallparameter bereit. |
| R10 | `annualisierte_rendite(array([.1,.2]),12)` statt Faktoren `[1.1,1.2]` | Nahe -1 statt 4.289852801 | Die Funktion erwartet Faktoren, keine einfachen Renditen. Kein Formelfehler bei gültigen Eingaben; Integrationsvertrag aus Theorie 3.3.3 deutlich machen. |
| R11 | `geometrisches_mittel([1.1,NaN,1.2])` als ndarray bzw. Series | ndarray: NaN; Series: 1.148912529 | Typabhängig wird NaN durch numpy/pandas-Mittelwert anders behandelt. Theorie 3.3.3/Analyse 5.5: vorab Vollständigkeit und einheitlichen Eingabetyp erzwingen. |
| R12 | `buy_and_hold(Series([.1,NaN,.1]),100)` | `[110,NaN,121]` | `cumprod` setzt nach fehlender Rendite fort. Ein unbekannter Vermögensschritt darf nicht so zu einem scheinbar vollständigen Endwert führen. Analyse 5.5/5.7; ebenfalls für kumulierte Helpers prüfen. |
| R13 | `trendfolge(Series([100,110,120]),0,2)` | Kein Fenster-Validierungsfehler; Signal `[0,0,0]` | Ein SMA mit 0 Beobachtungen ist fachlich nicht definiert (3.12.1). Positive ganze Fenster und `kurz < lang` validieren. |
| R14 | 60/40, zwei Perioden Aktien +10 %, Anleihen 0, ohne Rebalancingtermin zwischen ihnen | Nach erster Periode 66/40, Gesamt 106; zweite Rendite .06226415, Ende 112.60 | Feste .60/.40 in beiden Perioden ergäbe Ende 112.36, also laufendes Zurücksetzen. Mehrdeutige Formel nicht als jährliche Strategie implementieren (OD-06). |
| R15 | Beispielgewichte aus Theorie-Zelle 52: .20/.40/.20 | Summe .80 | Keine ausgewiesene restliche Position. OD-13; mathematische Rechnung allein beweist keinen vollständigen Portfoliovertrag. |

Ein zusätzliches leicht reproduzierbares Beispiel zu D-02: Anlagenrenditen `[.02,.04]`, RF `[0,.02]` ergeben konstante Überschüsse `[.02,.02]`. Deren Standardabweichung ist 0, die Strategievolatilität dagegen `sqrt(.0002)`. Die beiden beschriebenen Sharpe-Nenner führen damit zu unterschiedlichen bzw. nicht definierten Ergebnissen. Dieses Beispiel begründet OD-08 und darf nicht als neue Sharpe-Definition interpretiert werden.

### 6.3 Reproduktionsweg ohne Änderung von Quelldateien

Der normale Import scheitert in der aktuellen Umgebung (Abschnitt 9). Deshalb wurden **unveränderte AST-Funktionsdefinitionen** mit vorhandenen numpy-/pandas-Modulen im Arbeitsspeicher ausgeführt. Es wurde keine Importzeile in `src` geändert und keine Testdatei geschrieben. Der folgende Auszug reproduziert R1–R4/R7/R8/R12/R13 nach Laden derselben Definitionen; `python -B` verhindert Projekt-Bytecode-Dateien:

```python
import ast
from pathlib import Path
import numpy as np
import pandas as pd

tree = ast.parse(Path('src/funktionen.py').read_text(encoding='utf-8'))
nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
scope = {'np': np, 'pd': pd}
exec(compile(ast.Module(body=nodes, type_ignores=[]),
             'src/funktionen.py', 'exec'), scope)

print(scope['prozentuale_aenderung'](pd.Series([100., np.nan, 110.])))
print(scope['drawdown'](pd.Series([-.10, -.10])))
print(scope['maximum_drawdown'](pd.Series([-.10, -.10])))
idx = pd.date_range('2020-01-01', periods=4, freq='D')
print(scope['trendfolge'](pd.Series([100., np.nan, 110., 120.], index=idx), 1, 2))
print(scope['trendfolge'](pd.Series([100., 110., 120.]), 1, 3))
print(scope['neue_gewichtung'](pd.Series({'A':60., 'B':40.}),
                              pd.Series({'A':.10})))
print(scope['rebalancing'](pd.Series({'A':60., 'B':40.}),
                          pd.Series({'A':.5, 'B':.4}))[-1])
print(scope['buy_and_hold'](pd.Series([.1, np.nan, .1]), 100.))
print(scope['trendfolge'](pd.Series([100.,110.,120.]), 0, 2))
```

R5/R6 können in einer später reparierten, versiongleichen Umgebung direkt mit `sharpe_ratio` und den Eingaben der Tabelle wiederholt werden. Im Audit wurden aus den lokalen Paketdateien die Originaldefinitionen `QuantStatsError`, `DataValidationError`, `validate_input`, `_generate_cache_key`, `_clear_cache_if_full`, `_prepare_returns` und `sharpe` per AST geladen. Ihre Original-Globals wurden mit numpy, pandas, inspect, threading und dem leeren Original-Cache bereitgestellt; `rf=0` und `smart=False` entsprechen dem bestehenden Aufruf. Ein einfacher Namensraum verband `qs.stats.sharpe` mit dieser Originaldefinition. Weder Formel noch Vorverarbeitung wurden nachgebaut oder korrigiert. Dieser Befund gilt für den untersuchten isolierten Aufrufpfad und ersetzt keinen Paketintegrationstest.

## 7. Ausgeführte Prüfungen und Grenzen

| Prüfung | Tatsächliches Ergebnis |
|---|---|
| Vollständige Quellenlektüre und Vergleich aller 18 Definitionen mit Theorie-Code | Durchgeführt; alle Funktions-ASTs identisch |
| 21 numerische Vergleichsprüfungen mit unabhängigen erwarteten Werten | Erfolgreich; decken Standardfälle aller 18 Funktionen ab, Sharpe über isolierten Originalquellpfad |
| R1–R15 als künstliche Gegen-/Randbeispiele | Ausgeführt und beobachtete Ergebnisse dokumentiert; zusätzlich vier Assertions für R1/R2/R3/R5 erfolgreich, die das **fehlerhafte bestehende Verhalten** nachweisen, keine Engine-Fertigmeldung |
| Normaler Import von `src/funktionen.py` | Fehlgeschlagen: `ModuleNotFoundError: No module named 'platformdirs'` durch QuantStats → yfinance |
| `python -B -m pip check` | Exit 1: `rich 14.3.3` benötigt fehlendes `pygments`; `yfinance 1.5.2` benötigt fehlendes `platformdirs` |
| Projekt-/Interpreterinventar | Durchgeführt; keine Test-Suite, Paket-/Lockdatei oder `.venv` vorhanden; zweiter registrierter Interpreter nicht startbar |
| Engine-, Adapter-, Manifest- und reale Datenintegration | Nicht prüfbar: diese Komponenten und Datensätze existieren noch nicht |
| Änderungen und Git-Diff | Abschliessende Kontrolle siehe Abschnitt 12 |

Die 21 Standardprüfungen überprüften Differenzen, einfache/logarithmische Renditen, Faktoren, geometrische/annualisierte Rendite, Stichproben-Std/Volatilität, Standard-Drawdown/MDD, Korrelation, Kovarianzrisiko, Driftwerte/-gewichte, Rebalancingzielwerte/-transaktionen, Buy-and-Hold, SMA-Signal/Lag, Monats-Resampling und die Sharpe-Handformel. Der Prüfprozess lief über `python -B -` und endete mit Exit 0. Kein `pytest`-Lauf wird behauptet: pytest und eine Repository-Test-Suite fehlen. Die Fehler wurden als Audit-Befunde belassen; ihre Korrektur wäre im aktuellen Auftrag unzulässig.

## 8. Technischer Architekturvorschlag innerhalb von Analyse 5.8

Alle folgenden technischen Vorschläge sind Kategorie **B**, solange sie keine Entscheidung aus OD-01–OD-13 vorwegnehmen. Der vorhandene Code bleibt die mathematische Grundlage.

| Bereich / geplante Datei | Verantwortung und Grenze |
|---|---|
| `src/data/adapters/` | Eigene CSV- und später Anbieteradapter; explizite Quelldatenmappings, Rohdaten-/Provenienzspeicherung. Netzwerkzugriff nur in separat ausgelöstem Import, keine Markt-Downloads aus Strategie/Analyse |
| `src/data/normalize.py` | Standardspalten, Kennungen und Zeittypen; getrennte Performance-/Signalansichten; typgebundenes Downsampling nach bestätigten Periodenregeln |
| `src/data/validate.py` | Datenschema, Schlüssel, Metadaten, Lücken/Abdeckung, Einheiten, Kalender, RF/Makro-Versionen; maschinenlesbarer Datenbericht mit klaren Fehlern/Warnungen |
| `src/engine/config.py` | JSON laden, vollständige Struktur prüfen, unbekannte Schlüssel/ungültige Werte ablehnen, Datenreferenzen und aktive Strategien auflösen; keine Datenwahl/Optimierung |
| `src/engine/context.py` | Vorbereitete lokale Daten, Metadaten, Perioden, Startbewertung, Signalvorlauf, RF und Makrodaten plus Provenienz; keine Download-Methode. Strategien dürfen Context-Daten nicht gegenseitig verändern |
| `src/engine/result.py` | Gemeinsame Portfoliohistorie und optionale Strategieausgaben als einfache strukturierte Datentypen; Pflichtfelder und gemeinsame Kalenderkonsistenz prüfen |
| `src/engine/simulation.py` | Nur Orchestrierung des Ablaufs aus 5.8.4; aktive Strategien über `run(context, params)` ausführen; keine zweite Finanzformelsammlung |
| `src/strategies/buy_hold.py` | `buy_and_hold` nutzen, Startzustand und gemeinsamen Result-Vertrag ergänzen |
| `src/strategies/rebalance.py` | Zustandsfolge aus Drift, bestätigtem Kalenderereignis und `rebalancing`; Trades tatsächlich in Zielpositionswerte übernehmen |
| `src/strategies/trend.py` | Vorhandene SMA-/Lag-Logik wiederverwenden; Signal- und Performance-Reihe technisch trennen; Vorlauf, Position und bestätigte Cash-Regel sichtbar abbilden |
| `src/strategies/country_weighting.py` | Nach Entscheidung neue kleine BIP-Zielgewichtsermittlung aus damals zulässigen Daten; Portfoliozustand/Drift/Rebalancinghelpers gemeinsam wiederverwenden |
| `src/analysis/metrics.py` | Bestehende mathematische Helpers über validierte Wrapper aufrufen; gemeinsame tatsächliche Renditestichprobe, `m` und RF-Ausrichtung; kein eigenständiges Backtesting-Framework |
| `src/export/results.py` | Einheitliche CSV-/JSON-Exporte, stabile Spalten-/Zeilenreihenfolge, Manifest und Hashes; erst vollständige, validierte Resultate als erfolgreichen Run speichern |

Einfache Standardbibliotheks-Datenklassen genügen für Context/Result. Eine Plugin-Plattform, Datenbank, API oder Weboberfläche ist für Version 1 nicht erforderlich. Die technische JSON-Struktur darf um fehlende, fachlich bestätigte Einstellungen ergänzt werden; die vorhandenen Beispielschlüssel nicht ohne Grund inkompatibel umbenennen. Erforderliche Einstellungen nicht mit stillen Versuchsdefaults versehen. Für BIP ist nach OD-11/OD-12 ein eigener Strategieparameterblock erforderlich.

Der Simulationsablauf bleibt: **Konfiguration laden → lokale Daten laden/prüfen → Zeitraum und Vorlauf vorbereiten → aktive Strategien bestimmen → Strategien ausführen → gemeinsame Kennzahlen berechnen → Resultate und Manifest speichern**. Netzwerkadapter werden dafür nicht aufgerufen. In einem späteren Offline-Test müssen versehentliche Download-/HTTP-Aufrufe fehlschlagen.

Für die Zustandsverarbeitung wird empfohlen: bestätigter Anfangszustand → Positionswerte mit Renditen des gehaltenen Intervalls fortschreiben → neue Werte und Drift ausweisen → nur zu diesem Zeitpunkt verfügbare Signale/Zielgewichte bestimmen → bestätigtes Rebalancing für das nächste Intervall anwenden. Die genaue Ausführungs-/Zeitpunktkonvention bleibt OD-02/OD-06/OD-12. Ein Signal am Ende von `t` darf niemals die bereits vergangene Rendite von `t` verdienen. Das vorhandene Modell arbeitet mit diskreten Perioden; eine Ausführung zum nächsten Börsen-Open wäre ein zusätzliches Modell mit weiteren Daten und darf nicht still eingeführt werden.

### 8.1 Gemeinsamer Ergebnisvertrag

| Ausgabe | Vorgegebene Felder und technische Prüfung |
|---|---|
| `portfolio_history.csv` | `date, strategy, portfolio_value, period_return, drawdown`; eindeutiges Datum/Strategie, gemeinsamer Vergleichszeitraum, endliche beobachtete Werte; Startzeile nach OD-02; Renditen mit Wertverhältnissen konsistent |
| `weights_history.csv` | `date, strategy, asset_id, weight_before, target_weight, weight_after`; Vor-/Nachzeitpunkt nach OD-06; Zielgewicht kann nur an den tatsächlich definierten Ereignissen wirksam sein |
| `trades.csv` | `date, strategy, asset_id, value_before, target_value, transaction_value`; `transaction_value = target_value - value_before`; Kapitalerhaltung im bestätigten Kapitalmodell |
| `signals.csv` | `date, strategy, asset_id, signal, position, signal_value, sma_short, sma_long`; Signal und verzögerte Position getrennt, echte Vorlauf-NaN sichtbar, keine Tradeentscheidung aus undefiniertem SMA |
| Zusammenfassung | `strategy, start_value, end_value, total_return, annualized_return, annualized_volatility, sharpe_ratio, max_drawdown`; Dateiname `summary.csv` als technische Empfehlung, im Text noch nicht festgelegt |
| `run_manifest.json` | Tatsächlich aufgelöste Konfiguration, konkrete Datenstände, Zeitpunkt, Codeversion; weitere technische Nachweise wie unten |

Optionale Ausgaben werden nur für Strategien erzeugt, die sie tatsächlich benötigen; fehlende optionale Tabellen nicht mit fiktiven Trades/Signalen füllen. Für Ländergewichtung können die vorhandenen Gewichts-/Tradefelder wiederverwendet und die verwendeten Makroversionen zusätzlich in einem Provenienznachweis gespeichert werden. Ein eigener fachlicher BIP-Output ist noch nicht festgelegt. Erholungs-/Krisenanalysen und zusätzliche Marktkapitalisierungsvergleiche sind OD-19.

Das Manifest sollte als technische Konkretisierung mindestens enthalten: Schema-/Engineversion, Run-ID, UTC-Laufzeit, tatsächlich angewandte Konfiguration einschliesslich expliziter Fallbacks, effektive Bewertungs-/Auswertungsgrenzen, Frequenz und `m`, Roh-/Processed-Dateinamen mit SHA-256, Metadaten-/RF-/Makrostände, Adapter-/Transformationsversionen, Datenberichtreferenz, Git-Commit und Dirty-Zustand, Fingerprint der tatsächlich verwendeten Code-Dateien, Python- und Paketversionen sowie Ergebnisdatei-Hashes. Bei lokaler nicht committeter Änderung reicht der Commit allein nicht; ein Codefingerprint bzw. archivierter Codezustand muss die konkrete Version zusätzlich identifizieren. Ohne Git kann eine explizite Quellversion mit Inhaltsfingerprint die Rückverfolgbarkeit sichern; sie darf nicht als Git-Commit ausgegeben werden.

Gleiche Daten-, Konfigurations- und Codeinhalte sollen dieselben fachlichen Ergebnisse erzeugen. Unterschiedliche Run-ID/Zeitstempel sind zulässige Laufmetadaten; sie dürfen nicht versehentlich als Ergebnisabweichung gelten. Das Manifest muss vollständige reproduzierbare Werte erfassen, aber keine Anbieterzugangsschlüssel oder anderen Geheimnisse enthalten. JSON muss standardkonform bleiben: nicht definierte Kennzahlen als `null`/mit Status, nicht als unzulässiges `NaN` oder `Infinity` schreiben. Exportencoding, Rundung, Floatpräzision und Datumsdarstellung sind technisch dokumentierbar; Rundung erfolgt erst beim Export, nicht bei der Simulation.

## 9. Python-/Projektumgebung und notwendige Abhängigkeiten

### 9.1 Tatsächlicher Stand

| Komponente | Beobachtung am 2026-10-02 |
|---|---|
| Aktiver Interpreter | `C:\Python314\python.exe`, Python 3.14.0, 64-bit; `prefix == base_prefix`, keine aktive virtuelle Umgebung |
| Weiterer registrierter Interpreter | Python 3.11 wird von `py -0p` gelistet, ist jedoch über `py -3.11 -B -` nicht startbar: registrierter WindowsApps-Pfad nicht gefunden |
| Lokale `.venv` | Nicht vorhanden |
| Kernpakete | numpy 2.3.5; pandas 2.3.3; quantstats 0.0.81 |
| Weitere vorhandene Pakete | yfinance 1.5.2; matplotlib 3.10.7 |
| Nicht installierte geprüfte Pakete | pytest, fredapi, jupyter-Metapaket, plotly, empyrical, vectorbt, backtesting, pandas-ta, bt |
| Abhängigkeitsdateien / Tests | Keine gefundenen requirements-/pyproject-/Lock-/Umgebungsdateien; keine Repository-Test-Suite |
| Engine-Gerüst | Nur `src/funktionen.py`; `tests`, `configs`, `scripts`, `data`, `outputs` fehlen; `documentation/engine` war leer |
| README-Vorgaben | Empfiehlt Python 3.11+ und jupyter/pandas/matplotlib; benennt weitere Bibliotheken als zu prüfende Auswahl, keine verbindliche vollständige Engine-Umgebung |
| Paketprüfung | Zwei Inkonsistenzen: `platformdirs` für yfinance und `pygments` für rich fehlen; normaler Funktionsimport scheitert an der ersten |

Die Metadaten von QuantStats 0.0.81 verlangen Python >=3.10 und unter anderem numpy, pandas, matplotlib, scipy, python-dateutil, seaborn, tabulate und yfinance. Somit benötigt der bestehende **reguläre Import** auch für einfache Funktionen transitive Report-/Download-Abhängigkeiten. Das bedeutet nicht, dass im Backtest Daten heruntergeladen werden müssen. Der Importfehler beweist auch keine generelle Inkompatibilität mit Python 3.14; zuerst fehlt eine konkret benannte deklarierte Abhängigkeit. Keine dieser Umgebungsstörungen wurde in diesem Audit repariert.

### 9.2 Kleiner begründeter Abhängigkeitssatz

| Abhängigkeit | Nutzen / Vorschlag |
|---|---|
| **pandas** | Erforderlich für bestehende Zeitreihenhelpers, CSV, Pivot, Resampling, Labels und Tabellen; Version reproduzierbar festhalten |
| **numpy** | Erforderlich für bestehende logarithmische/geometrische Berechnungen, lineare Algebra und numerische Prüfungen |
| **quantstats** | Derzeit erforderlich, weil `sharpe_ratio` und der Modulimport es benutzen; Theorie erwähnt zusätzlich Drawdown-Erholungsfunktionen. Beibehalten und den exakt genutzten Quellpfad testen; nicht aus Bequemlichkeit durch andere Finanzbibliothek ersetzen |
| **QuantStats-Transitivabhängigkeiten** | Im späteren getrennten Projektvenv vollständig auflösen; insbesondere aktuell fehlendes platformdirs über den deklarierten yfinance-Abhängigkeitsbaum. pygments betrifft zusätzlich die geprüfte globale Umgebung, ist keine neue fachliche Engine-Kernanforderung |
| **Python-Standardbibliothek** | `json`, `csv` bei Bedarf, `pathlib`, `dataclasses`, `hashlib`, `datetime`, `importlib.metadata`, gegebenenfalls `subprocess` für Git genügen für Konfiguration, Manifest und einfache Strukturen |
| **pytest** — vorgeschlagen, nur Entwicklung | Klarer Nutzen für Parametrisierung, Fixtures, temporäre Exportverzeichnisse, numerische Assertions und Offline-Tests. `unittest` wäre ohne neues Paket möglich; nicht beide Testframeworks einführen |
| **yfinance** — nur eigener Importadapter | Bereits indirekt vorhanden; als direkter Importbedarf nur nach Auswahl eines Yahoo-Adapters, nicht als Strategieabhängigkeit. Quellspalten/Adjustierung vor Nutzung an offizieller API-Dokumentation prüfen |
| **fredapi** — optionaler Importadapter | Erst begründen, wenn ein FRED-Adapter tatsächlich gebraucht wird. CSV-Import kann den allgemeinen RF-/Makrovertrag ohne dieses Paket erfüllen |
| **Börsenkalenderbibliothek** — bedingt optional | Erst nach OD-01 bewerten; klarer möglicher Nutzen bei mehreren Börsen. Ein mitgelieferter expliziter Kalender kann zunächst genügen. Keine Kalenderbibliothek vorsorglich hinzufügen |

Nicht erforderlich für den Kern sind empyrical, vectorbt, backtesting.py, bt und pandas-ta: die beschriebenen Formeln/SMA und Portfoliohelpers liegen bereits vor; zusätzliche Frameworks würden ein zweites Berechnungssystem und neue implizite Annahmen einführen. Matplotlib wird bereits transitiv benötigt, separate Diagramm-/Webpakete sind für CSV-/JSON-Ergebnisse nicht notwendig. Jupyter/Quarto gehören zur Notebook-/Bucharbeit, nicht zur Ausführung eines lokalen CSV-Backtests.

Technische Empfehlung für später: separates Projektvenv mit einer tatsächlich verfügbaren, gemeinsam getesteten Python-Version; zunächst vorhandene Versionen prüfen, dann kompatible direkte und transitive Versionen festhalten. Kein blindes Upgrade und keine Umstellung auf eine neue Python-/pandas-Version ohne Regressionstests. Der Audit installiert oder pinnt nichts.

## 10. Vorgeschlagene Implementierungsreihenfolge

1. **Autorenentscheidungen klären:** OD-01–OD-13, mit Fokus auf Perioden/Start, Währung/Kapitalmodell, SMA/Cash/Rebalancing sowie Sharpe-/Drawdown-Konflikte; OD-11/OD-12 vor BIP-Modul. Antworten und ausdrücklich erlaubte mathematische Korrekturen dokumentieren. Keine finalen Versuchsdaten auswählen.
2. **Reproduzierbare Entwicklungsumgebung:** Verfügbaren Interpreter und isolierte Abhängigkeiten herstellen, regulären Import und Paketprüfung erfolgreich ausführen, Tests einrichten. Dies ist ein späterer technischer Auftrag.
3. **Daten-/Konfigurations-/Result-Verträge:** Typen, Pflichtfelder, Referenzen und validierte explizite Einstellungen; CSV-/JSON-Fixtures mit künstlichen Kennungen; Datenbericht und Provenienzstruktur.
4. **Lokale Datenverarbeitung:** CSV-Mapping, Metadaten, Validierung, Kalender/Perioden, sichere Resamplingwrapper, getrennte Performance-/Signalreihen, Vorlauf sowie RF-/Makrovalidierung. Noch kein Anbieter-Download für End-to-End-Tests nötig.
5. **Mathematische Integration:** Bestehende Funktionen über dünne geprüfte Wrapper wiederverwenden; bestätigter Start-HWM, keine implizite Fehlwertbehandlung, korrekte Faktoren-/Renditeübergabe, QuantStats-Verhalten absichern. Jede erlaubte Korrektur mit Gegenbeispiel und Test dokumentieren.
6. **Buy-and-Hold und gemeinsame Auswertung:** Einfache Benchmark mit Startzustand; alle Kernkennzahlen und gemeinsames Result-Schema; erste handrechenbare Gesamtsimulation.
7. **Rebalancing:** Werte/Drift, jährliche Ereignisse, Zielzustandsübernahme, Gewichte/Trades, Kapitalerhaltung und Zeitreihenkonsistenz.
8. **SMA:** Getrennte Signal-/Performance-Daten, Vorlauf, eine Periode Signalverzögerung, bestätigte Cash-Regel und Signalexport; Beginn und Kreuzungen explizit prüfen.
9. **BIP-/Länderstrategie:** Bestätigte Gewichtungsregel, Einheiten/Länderabbildung, point-in-time Versionen, Gewichtsaktualisierung und bestehende Portfoliohelpers; keine historische Informationsvorwegnahme.
10. **Exports/Manifest und Abschlussprüfung:** Volle Konfiguration, Daten-/Codehashes, effektiver Kalender, deterministische Ergebnisse, Offline-Lauf, veränderte Inputs und Fehlerfälle. Anbieteradapter erst getrennt auf ihre fachlich belegte Quellenabbildung prüfen.
11. **Danach erst Hauptversuch vorbereiten:** OD-14–OD-18 durch Autor fixieren, zusätzliche Auswertungen OD-19 entscheiden, Dateneignung/manuelle Kontrolle und Parameterfreeze vor wissenschaftlichem Hauptlauf.

## 11. Spätere technische Fertigkriterien

Die Engine darf nach einem späteren Implementierungsauftrag erst als technisch fertig bezeichnet werden, wenn die folgenden Kriterien tatsächlich geprüft sind:

- Alle für den freigegebenen Umfang nötigen BLOCKING-Entscheidungen sind dokumentiert; es gibt keine still gewählten fachlichen Defaults oder ungelösten Formel-/Codekonflikte.
- Der reguläre Import und die erforderlichen Abhängigkeiten funktionieren in der dokumentierten Projektumgebung; eine frische Umgebung ist aus gespeicherten Versionsangaben herstellbar.
- Vollständige, echte CSV-/JSON-Schnittstellen erfüllen Analyse 5.3/5.6/5.7. Fehlerhafte Schlüssel, NaN/Inf, fehlende Assets, unzulässige Gewichte, Einheiten oder unzureichender Vorlauf erzeugen nachvollziehbare Fehler statt scheinbar gültiger Ergebnisse.
- Alle vorgesehenen freigegebenen Strategien besitzen `run(context, params)` und den gleichen Grundoutput; optionale Ausgaben stimmen mit dem tatsächlichen Zustand überein. Eine abgeschaltete oder noch fehlende BIP-Strategie darf nicht als vollständig fertig implementiert gelten, wenn sie zum bestätigten Umfang gehört.
- Tests T-D/T-M/T-S/T-I wurden ausgeführt und bestanden; R1–R15 bleiben als Regressionen/Vertragsnachweise erhalten. Tests dürfen Fehler nicht durch gelockerte Erwartungen verbergen.
- Ein handrechenbarer Anfangsverlust belegt den korrekten Start-HWM; MDD entspricht dem Minimum des Verlaufs. Summaries enthalten das tatsächliche Startkapital, nicht versehentlich den ersten nach Rendite veränderten Portfoliowert.
- Gemeinsame tatsächliche Perioden und Stichproben sind für Strategie- und RF-Renditen identisch. Resamplinglabels, erstes Halteintervall, jährliche Rebalancingtermine und letzte Teilintervalle folgen den bestätigten Regeln.
- Ein Test verändert ausschliesslich zukünftige Markt-/Signal-/BIP-Beobachtungen: frühere Entscheidungen, Trades und Vermögenswerte bleiben gleich. Eine spätere BIP-Revision kann frühere Gewichte nicht verändern. Ein Signal von `t` verdient keine Rendite von `t`.
- Rebalancing erhält Kapital ohne Kostenmodell; ohne Ereignis driften Gewichte. Tatsächliche Wertentwicklung, Periodenrenditen, Gewichte, Trades und Signale sind algebraisch konsistent und Labels korrekt ausgerichtet.
- Alle Strategien nutzen dasselbe Startkapital, dieselbe bestätigte Währungs-/Dividenden-/Frequenzbehandlung und den gleichen Vergleichszeitraum. Signal-Fallbacks erfolgen ausschliesslich bei ausdrücklicher Erlaubnis.
- Ein kompletter Lauf funktioniert mit gesperrtem Netzwerk aus eingefrorenen lokalen Dateien. Derselbe Daten-/Konfigurations-/Codezustand erzeugt dieselben fachlichen Outputs; keine Konfiguration, Rohdatei oder Context-Daten werden währenddessen verändert.
- Das Manifest identifiziert tatsächlich verwendete Daten, Konfiguration, Code und Paketversionen. Änderungen an Daten/Konfiguration/Code sind im Nachweis erkennbar; vorhandene Resultate werden nicht unbemerkt überschrieben. Fehlgeschlagene Läufe erscheinen nicht als erfolgreiche vollständige Ergebnisse.
- Der Autor hat Datenbedeutung, bestätigte Regeln, repräsentative Handbeispiele und Ausgaben manuell geprüft; die KI-Dokumentation unterscheidet diese Kontrolle von automatisierten Tests. Technische Fertigstellung ist kein Nachweis einer künftig erfolgreichen Anlagestrategie und keine endgültige Versuchsauswahl.

## 12. Änderungsgrenze und Abschlusskontrolle

Erlaubt sind ausschliesslich dieses Audit, `documentation/engine/open-decisions.md` und ein neuer Eintrag am Ende von `documentation/ai-usage/ai-usage-log.md`. Der Arbeitsbaum war vor dem Audit ohne vorgemerkte oder nicht vorgemerkte Änderungen und ohne nicht ignorierte neue Dateien. Vor Dokumentationsänderungen wurden SHA-256-Werte aller 34 versionierten Dateien als Vergleichsbasis erfasst.

Abschlusskontrolle durchgeführt: `git diff` für den bestehenden KI-Logeintrag sowie vollständige `git diff --no-index -- NUL <Datei>` für beide neuen, noch nicht versionierten Dokumente. Ein gewöhnlicher `git diff` allein würde diese neuen Dateien nicht anzeigen. Die neuen Dateidiffs wurden gegen ihre gesamten Dateiinhalte geprüft. `git diff --check` für die versionierte Änderung war erfolgreich; Markdown-Hardbreak-Leerzeichen in der neuen Audit-Datei wurden vor dem Abschluss entfernt.

`git status --short --untracked-files=all` zeigt genau:

```text
 M documentation/ai-usage/ai-usage-log.md
?? documentation/engine/audit.md
?? documentation/engine/open-decisions.md
```

Die SHA-256-Kontrolle bestätigt: Von 34 zuvor versionierten Dateien ist nur das erlaubte KI-Log geändert; alle anderen 33 Dateien sind bytegleich zur Ausgangsbasis. Der Log-Diff enthält genau einen angehängten Tabellen-Eintrag; alle bisherigen Zeilen bleiben erhalten. Die Dokumentstrukturprüfung bestätigt 13 BLOCKING-/6 NON-BLOCKING-Einträge mit allen verlangten Feldern, alle 18 Funktionen in der Integrationsmatrix, gültige lokale Links und geschlossene Codeblöcke.

**Bestätigung:** Ausser der erlaubten Dokumentation wurden keine Projektdateien verändert. `src/`, Theorie, Analyse, Methodik, Bibliographie und Buchkapitel bleiben unverändert. Keine Engine, keine neuen Tests, keine Abhängigkeitsinstallation, kein Git-Commit und keine endgültige fachliche Auswahl wurden vorgenommen. Die anfängliche Git-Ownership-Warnung wurde nur mittels auf einzelne Befehle begrenztem `git -c safe.directory=...` behandelt; keine globale Git-Konfiguration wurde geändert.

**Stopp nach dem Audit:** Implementierung und fachliche Entscheidungen bleiben einem weiteren ausdrücklichen Auftrag vorbehalten.
