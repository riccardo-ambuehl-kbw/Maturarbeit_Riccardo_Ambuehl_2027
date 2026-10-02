# Offene Entscheidungen vor der Engine-Implementierung

Stand: 2026-10-02. Grundlage: der vollständige [Audit-Auftrag](../ai-usage/prompts/2026-10-02-engine-audit.md), `AGENTS.md` und die im [Audit](audit.md) ausgewerteten lokalen Quellen. Alle Empfehlungen stammen von Codex und sind **keine verabschiedeten methodischen Entscheidungen**.

Es bestehen **13 BLOCKING-Entscheidungen (OD-01 bis OD-13)** und **6 NON-BLOCKING-Entscheidungen (OD-14 bis OD-19)**. BLOCKING bezieht sich auf die vollständige, fachlich eindeutige Implementierung des beschriebenen Systems; einzelne Punkte betreffen nur ein bestimmtes Modul. Die endgültige Auswahl von Anlagen, Zeitraum, risikofreier Serie und SMA-Fenstern blockiert die allgemeine Engine ausdrücklich nicht. Ein Hauptversuch benötigt diese späteren Festlegungen trotzdem.

Technische Fehler wie fehlende Python-Abhängigkeiten, implizites Auffüllen durch pandas oder fehlende Eingabevalidierung sind im Audit gesondert aufgeführt. Ihre Behebung erfordert keine neue finanzwirtschaftliche Regel, ist in diesem reinen Dokumentationsschritt aber nicht erlaubt.

## OD-01 — Datenkalender, gemeinsame Perioden und echte Lücken

- **ID:** OD-01
- **Frage:** Welche Kalender- und Ausrichtungsregel gilt bei unterschiedlichen Handelstagen, fehlenden Beobachtungen und ungleicher Datenabdeckung mehrerer Anlagen und Strategien?
- **Warum notwendig:** Eine Rendite über Freitag bis Dienstag darf nicht ohne Prüfung mit einer Rendite über Montag bis Dienstag gewichtet werden. Ein gemeinsames Datum allein garantiert keine gemeinsame Renditeperiode. Die Auswahl oder Entfernung von Tagen verändert SMA-Fenster, Rebalancing und Kennzahlen.
- **Betroffene Kapitel/Funktionen:** Analyse 5.5.2–5.5.4; Theorie 3.2 und 3.13; `prozentuale_aenderung`, `trendfolge`, `korrelationsmatrix`, `portfolio_risiko`, `neue_gewichtung`.
- **Mögliche Optionen:** Ein gemeinsamer Beobachtungskalender mit gleichen Anfangs- und Endpunkten; Schnittmenge der Wertbeobachtungen und danach neue Renditeberechnung; gröbere gemeinsame, vollständig beobachtete Intervalle; ausdrücklich definierte Bewertung an geschlossenen Märkten. Echte Datenlücken können zum Abbruch oder zu einer explizit verkürzten gemeinsamen Stichprobe führen. Eine Schnittmenge darf keine tatsächliche Lücke verschleiern.
- **Auswirkungen:** Bestimmt Haltedauer, Vergleichsstichprobe, effektive Frequenz und zulässige Eingaben. Allgemeine Werktage sind kein ausreichender Börsenkalender. Automatisches Forward Fill oder Interpolieren bleibt durch AGENTS.md ausgeschlossen.
- **Empfehlung von Codex:** Echte Lücken zunächst als Fehler behandeln; unterschiedliche Marktfeiertage gesondert melden. Eine vom Autor freigegebene gemeinsame Periodenregel anwenden, Wertreihen vor der Renditeberechnung ausrichten und entfernte Beobachtungen im Datenbericht ausweisen. Keinen Kalender aus den Daten still erraten.
- **Klassifikation:** **BLOCKING** — Datenaufbereitung und Mehranlagen-Simulation.

## OD-02 — Startbewertung, erste Rendite und unvollständige Intervalle

- **ID:** OD-02
- **Frage:** Welcher beobachtete Wert bildet die Bewertung des Startkapitals, welches Intervall ist die erste ausgewertete Rendite, und wie werden angebrochene Wochen, Monate oder Jahre am Rand behandelt?
- **Warum notwendig:** Ein Startdatum ohne Kurs und eine erste Rendite aus einem Wert vor dem Startdatum können unterschiedliche wirtschaftliche Startpunkte erzeugen. Analyse 5.5.4 verlangt abgeschlossene Intervalle, definiert aber deren Behandlung am Rand nicht. `buy_and_hold` liefert nur Werte nach Renditeperioden und keine eigene Startzeile.
- **Betroffene Kapitel/Funktionen:** Analyse 5.5.4, 5.6.1, 5.7 und 5.8.4; Theorie 3.2, 3.5 und 3.9; `resample_dataframe`, `buy_and_hold`, `wachstumsfaktor`, `drawdown`.
- **Mögliche Optionen:** Start an einem vorhandenen gemeinsamen Bewertungsdatum und Renditen erst danach; separate Vorstartbewertung mit ausdrücklich definiertem erstem Halteintervall; Abbruch bei nicht passenden Grenzen; dokumentierte Verschiebung auf gültige Grenzen. Angebrochene Intervalle ausschliessen oder ausdrücklich als solche auswerten.
- **Auswirkungen:** Verändert Zeitraum, Periodenzahl, Gesamtrendite und Start-High-Water-Mark. Eine technische Startzeile darf nicht als zusätzliche beobachtete Nullrendite in Mittelwerte und Standardabweichungen eingehen.
- **Empfehlung von Codex:** Eine explizite Startbewertung mit `portfolio_value = start_capital`, `period_return` ohne Beobachtung und Drawdown 0 vorsehen; nur danach gehaltene Intervalle auswerten. Die konkrete Datums- und Randintervallregel durch den Autor bestätigen lassen; effektive Grenzen im Manifest speichern.
- **Klassifikation:** **BLOCKING** — Zeitraumvorbereitung und gemeinsamer Ergebnisvertrag.

## OD-03 — Perioden pro Jahr und unregelmässige Abstände

- **ID:** OD-03
- **Frage:** Welche Zuordnung von Datenfrequenz zu `perioden_pro_jahr` gilt, und sind unregelmässige oder angebrochene Perioden für annualisierte Kennzahlen zulässig?
- **Warum notwendig:** Die Formeln für annualisierte Rendite, Volatilität und Sharpe Ratio benötigen ein gemeinsames `m`. Theorie 3.4 nennt 252 als häufigen Wert, legt damit aber keine universelle Konvention fest. Das JSON-Beispiel enthält weder Frequenz noch `m`.
- **Betroffene Kapitel/Funktionen:** Theorie 3.3.3, 3.4.3 und 3.6.2; Analyse 5.5.4 und 5.6; `annualisierte_rendite`, `annualisierte_volatilitaet`, `sharpe_ratio`.
- **Mögliche Optionen:** Explizites `m` pro Konfiguration; eine vom Autor festgelegte Frequenzzuordnung; Zulassung nur regelmässiger Perioden. Eine Annualisierung nach tatsächlicher verstrichener Zeit wäre eine zusätzliche, derzeit nicht festgelegte Methode.
- **Auswirkungen:** Unterschiedliche Werte verändern sämtliche annualisierten Kennzahlen. Nach Kalenderausrichtung oder Tagesentfernung sind verbleibende Beobachtungen nicht automatisch reguläre Handelstage.
- **Empfehlung von Codex:** Die bereits beschriebenen Formeln beibehalten; `m` ausdrücklich validieren und im Manifest speichern. Unregelmässige Intervalle bis zu einer methodischen Festlegung nicht mit einem still gewählten Standardwert annualisieren. Kein Wechsel zu einer CAGR-Methode nach Kalenderdauer ohne Auftrag.
- **Klassifikation:** **BLOCKING** — gemeinsame Kennzahlen und Frequenzverarbeitung.

## OD-04 — SMA-Anlaufphase und gemeinsamer Vergleichsbeginn

- **ID:** OD-04
- **Frage:** Soll die SMA-Strategie vor dem Untersuchungsbeginn historische Signalwerte erhalten, später starten oder die Anlaufphase als ausdrücklich definierte Cash-Phase durchlaufen?
- **Warum notwendig:** Bei fehlendem langen SMA erzeugt `np.where(NaN > NaN, 1, 0)` ein Signal 0. Ein nicht berechenbares Signal ist aber noch keine fachlich definierte Cash-Entscheidung. Das erste vollständige Signal wirkt erst in der folgenden Periode. Ein kürzerer Trend-Zeitraum wäre nicht direkt mit der vollständigen Benchmark vergleichbar.
- **Betroffene Kapitel/Funktionen:** Theorie 3.12 und 3.13.1; Analyse 5.3.6, 5.6.2 und 5.8.4; `trendfolge`, `buy_and_hold`.
- **Mögliche Optionen:** Vorlaufdaten nur für die Signalerzeugung, mit gültigem Signal an der Startbewertung; gemeinsamer späterer Auswertungsbeginn aller Strategien; vollständiger Untersuchungszeitraum mit expliziter Cash-Regel während des Vorlaufs; Abbruch bei unzureichenden Vorlaufdaten.
- **Auswirkungen:** Verändert frühe Positionen, Renditen und faire Vergleichbarkeit. Vorlaufwerte dürfen keine Portfoliorenditen vor dem eigentlichen Start in die Auswertung einschleusen. Fenster zählen Beobachtungen der festgelegten Frequenz, nicht automatisch Kalendertage.
- **Empfehlung von Codex:** Ausreichende historische Vorlaufdaten für das letzte Signal vor der ersten gehaltenen Renditeperiode verlangen; Untersuchungszeitraum für alle Strategien gleich halten. Falls das nicht möglich ist, abbrechen oder eine vom Autor ausdrücklich genehmigte gemeinsame Startverschiebung verwenden. Fehlende SMA-Werte sichtbar lassen.
- **Klassifikation:** **BLOCKING** — SMA-Strategie und Vergleichszeitraum.

## OD-05 — Verzinsung der Cash-Phasen

- **ID:** OD-05
- **Frage:** Bleibt Cash wie in Theorie 3.12.2 und im Code bei einer Rendite von 0, oder soll die konfigurierbare Cash-Behandlung aus Analyse 5.6.2 auch eine Verzinsung zulassen?
- **Warum notwendig:** Die vorhandene Formel `s_(t-1) * r_Markt,t` setzt Cash-Rendite 0 voraus. Eine risikofreie Verzinsung erfordert einen zusätzlichen Cash-Renditebeitrag und ist damit eine Erweiterung der beschriebenen Strategie.
- **Betroffene Kapitel/Funktionen:** Theorie 3.12.2; Analyse 5.6.2; Methodik, Trendfolge und Bedingungen; `trendfolge`, `sharpe_ratio`.
- **Mögliche Optionen:** Unverzinstes Cash gemäss vorhandener Formel; separate, explizit definierte Cash-Renditereihe; ausdrücklich zugelassene Auswahl zwischen beiden Varianten. Die Sharpe-Vergleichsreihe ist nicht automatisch eine investierbare Cash-Anlage.
- **Auswirkungen:** Verändert Rendite, Drawdown und Sharpe Ratio der Trendfolge. Die benötigte Zinsausrichtung hängt von OD-07 ab.
- **Empfehlung von Codex:** Für die erste Version unverzinstes Cash entsprechend der vorhandenen Formel bestätigen; weitere Cash-Modelle erst nach ausdrücklicher methodischer Erweiterung. Keine risikofreie Verzinsung automatisch hinzufügen.
- **Klassifikation:** **BLOCKING** — vollständiger Vertrag der SMA-Strategie.

## OD-06 — Zeitpunkt des Rebalancings und 60/40-Formel

- **ID:** OD-06
- **Frage:** Welcher genaue jährliche Stichtag und welche Reihenfolge von Renditeverbuchung und Rebalancing gelten, und ist die feste 60/40-Formel nur am Zeitpunkt gültiger Zielgewichte anzuwenden?
- **Warum notwendig:** Theorie 3.8.2 und Methodik verlangen jährliches Rebalancing mit Drift dazwischen. Die Formel in 3.10.1 zeigt dennoch feste Gewichte für `t`. Ihre Anwendung in jeder Periode entspräche laufendem Rebalancing. Eine jährlich wiederholte Regel definiert noch keinen konkreten Handelstag.
- **Betroffene Kapitel/Funktionen:** Theorie 3.8 und 3.10.1; Methodik, Bedingungen; Analyse 5.6.2 und 5.7.2; `neue_gewichtung`, `rebalancing`.
- **Mögliche Optionen:** Kalenderjahresende nach Verbuchung der abgelaufenen Periode; Kalenderjahresbeginn vor der nächsten Periode; Jahrestag der Startanlage; ein ausdrücklich festgelegter anderer jährlicher Stichtag. Jede Variante benötigt eine Regel für Feiertage und einen unvollständigen letzten Zeitraum.
- **Auswirkungen:** Bestimmt die Gewichte, die eine Rendite tatsächlich verdienen. Die bestehende `rebalancing`-Funktion berechnet Zielwerte und Transaktionen, führt diese jedoch nicht selbst aus. `weights_history` muss Vor- und Nachzustand konsistent ausweisen.
- **Empfehlung von Codex:** Gewichte zu Periodenbeginn für die bereits gehaltene Periode verwenden, danach Werte und Drift aktualisieren, dann am bestätigten Stichtag Zielwerte als neuen Zustand übernehmen. Die 60/40-Formel ausdrücklich auf Zielgewichtszustände beschränken. Einen Kalenderstichtag vom Autor festlegen lassen.
- **Klassifikation:** **BLOCKING** — Rebalancing-Strategie und Auflösung der Formelmehrdeutigkeit.

## OD-07 — Risikofreie Beobachtung zu Periodenrendite

- **ID:** OD-07
- **Frage:** Wie werden Einheiten, Zinskonvention, Tageszählung, Veröffentlichungszeit und Gültigkeitsintervall einer Zinsbeobachtung in die risikofreie Rendite genau derselben Portfolio-Periode übersetzt?
- **Warum notwendig:** Der Vertrag `date, series_id, value, unit` unterscheidet noch nicht sicher zwischen beobachtetem jährlichem Zinssatz und realisierter Periodenrendite. Ein Datum kann Beobachtungsdatum, Veröffentlichungsdatum oder Gültigkeitsbeginn bedeuten. Ein jährlicher Prozentsatz ist keine tägliche Dezimalrendite.
- **Betroffene Kapitel/Funktionen:** Theorie 3.6; Analyse 5.3.7 und 5.4.3; `sharpe_ratio`, `resample_dataframe`.
- **Mögliche Optionen:** Bereits passende realisierte Periodenrenditen importieren; effektiven Jahreszins über die festgelegte Laufzeit umrechnen; eine ausdrücklich begründete einfache Geldmarktzinskonvention verwenden. Gültige Zinsbeobachtungen können über ihre dokumentierte Gültigkeit zugeordnet werden; fehlende Zinsdaten können zum Abbruch oder zu einer ausdrücklich genehmigten Auswertungsbeschränkung führen.
- **Auswirkungen:** Verändert Überschussrenditen, Cash-Renditen und Look-ahead-Eigenschaften. Eine beliebige Forward-Fill-Regel für fehlende Beobachtungen oder Nullersetzung ist nicht zulässig. Die Marktwertregel für fehlende Kurse und die Gültigkeit veröffentlichter Zinssätze sind unterschiedliche Sachverhalte.
- **Empfehlung von Codex:** Die Adapter müssen die Zinssemantik und gegebenenfalls zusätzliche Provenienz-/Verfügbarkeitsinformationen dokumentieren. Vor `sharpe_ratio` gleich lange, endliche Reihen mit identischen Periodengrenzen verlangen. Die Umrechnung pro unterstützt gehaltenem Datentyp vom Autor bestätigen lassen; keine FRED-Serie in diesem Audit auswählen.
- **Klassifikation:** **BLOCKING** — risikofreie Normalisierung, Sharpe-Auswertung und gegebenenfalls Cash-Modell.

## OD-08 — Widersprüchlicher Sharpe-Nenner

- **ID:** OD-08
- **Frage:** Soll die Engine die explizite Formel der Theorie mit der Standardabweichung der Überschussrenditen verwenden, und soll die abweichende Formulierung der Methodik später entsprechend geklärt werden?
- **Warum notwendig:** Theorie 3.6.2 und `sharpe_ratio` verwenden `sigma(r-r_f)`. Die Methodik beschreibt dagegen die Volatilität der Strategie als Nenner. Bei konstantem `r_f` stimmen beide Standardabweichungen überein; bei zeitlich variablem `r_f` im Allgemeinen nicht.
- **Betroffene Kapitel/Funktionen:** Theorie 3.6.2; Methodik, Sharpe Ratio; Analyse 5.7.3 und 5.9.1; `sharpe_ratio`.
- **Mögliche Optionen:** Explizite Theorieformel und Code bestätigen; die Methodikvariante als neue verbindliche Definition festlegen und deren Unterschied dokumentieren; beide getrennt benannte Kennzahlen nach zusätzlicher Entscheidung ausgeben.
- **Auswirkungen:** Ändert die wissenschaftliche Kennzahl. Die Vorverarbeitung durch QuantStats ist zusätzlich technisch abzusichern und löst diesen Definitionswiderspruch nicht.
- **Empfehlung von Codex:** Die präzise Formel der Theorie als verbindlich bestätigen und die Methodik später in einem gesonderten Auftrag konsistent beschreiben. Keine Umstellung des Nenners im Audit.
- **Klassifikation:** **BLOCKING** — Auflösung des fachlichen Quellenwiderspruchs vor Kennzahlenintegration.

## OD-09 — Drawdown und Start-High-Water-Mark

- **ID:** OD-09
- **Frage:** Darf die Integration den Anfangshöchststand gemäss der Formel mit `V_0` herstellen, obwohl die bestehende Funktion und das Theorie-Codebeispiel ihn derzeit auslassen?
- **Warum notwendig:** Für Renditen `[-0.10, -0.10]` liefert der bestehende Code Drawdowns `[0, -0.10]`; die Formel in Theorie 3.5.2 ergibt aus `V_0=1` die Werte `[-0.10, -0.19]`. Das Beispiel im Notebook beginnt positiv und zeigt den Fehler deshalb nicht.
- **Betroffene Kapitel/Funktionen:** Theorie 3.5.2, Codezelle 36; Analyse 5.7 und 5.9.1; `drawdown`, `maximum_drawdown`, `buy_and_hold`.
- **Mögliche Optionen:** Wrapper mit expliziter Startbewertung und Wiederverwendung der bestehenden Funktion; transparente Korrektur der bestehenden Funktion in einem späteren Auftrag; bewusst eine andere Drawdown-Definition festlegen und die Formel ändern. Letzteres wäre eine methodische Änderung.
- **Auswirkungen:** Betrifft sämtliche Strategien mit Verlusten ab Beginn und die Konsistenz zwischen Verlauf und Zusammenfassung. Eine synthetische Nullrendite darf nur dem Startzustand dienen und nicht die Renditestichprobe erweitern.
- **Empfehlung von Codex:** Die Formel mit `V_0` bestätigen; bevorzugt einen dokumentierten Wrapper verwenden, der den Startzustand berücksichtigt und die bestehende Funktion wiederverwendet. Danach beide Funktionen mit einem Verlust in der ersten Periode testen. Keine zweite unabhängige Drawdown-Implementierung einführen.
- **Klassifikation:** **BLOCKING** — ausdrückliche Auflösung des Formel-/Codewiderspruchs vor Wiederverwendung.

## OD-10 — Basiswährung und Wechselkurse

- **ID:** OD-10
- **Frage:** Darf die erste Engine nur bereits in derselben Basiswährung vorliegende Wertreihen akzeptieren, oder muss sie Reihen verschiedener Währungen umrechnen?
- **Warum notwendig:** `assets.csv` besitzt `currency`, die Konfiguration `base_currency`. Ein FX-Datenvertrag und die Bewertungs-/Ausrichtungsregeln fehlen. Unterschiedliche Währungen werden durch Umbenennung oder Normierung eines Index nicht vergleichbar.
- **Betroffene Kapitel/Funktionen:** Theorie 3.13.1; Analyse 5.3.7 und 5.6.1; `neue_gewichtung`, `rebalancing`, gemeinsame Renditefunktionen.
- **Mögliche Optionen:** Nur kompatible Basiswährungsreihen akzeptieren; bereits fachlich umgerechnete Performance-Reihen importieren und ihre Herkunft dokumentieren; eigenen FX-Vertrag sowie Kursrichtung, Kalender und Zeitpunkt definieren. Währungsabsicherung wäre eine weitere methodische Erweiterung.
- **Auswirkungen:** Eine Umrechnung verändert die Anlagerenditen. Der Währungsbedarf des Signals und die Währung der Sharpe-Vergleichsreihe müssen ebenfalls erklärt werden.
- **Empfehlung von Codex:** In Version 1 Währungskonsistenz streng prüfen und nicht passende Reihen ablehnen; keine automatische FX- oder Hedging-Methode erfinden. Eine spätere FX-Erweiterung mit eigenem Datenvertrag separat beauftragen.
- **Klassifikation:** **BLOCKING** — allgemeiner Eingabe- und Bewertungsvertrag.

## OD-11 — Umfang der Ländergewichtungsstrategie

- **ID:** OD-11
- **Frage:** Soll `country_weighting` eine reine BIP-Gewichtung von Länderanlagen nach Theorie 3.11 implementieren oder die gemischte Marktkapitalisierungs-/BIP-/Faktorstrategie, die in der Methodik beim Gerd-Kommer-ETF beschrieben ist? Wie werden Ländergewichte auf Anlagen abgebildet?
- **Warum notwendig:** Die Texte beschreiben unterschiedliche Umfänge. Die Analyse plant ein Modul, aber keine BIP-Konfiguration und keine vollständige Strategie. Für eigene Marktkapitalisierungs-/Faktorberechnungen fehlen entsprechende Datenverträge. Die feste `country`-Metadatenangabe definiert noch keine Aufteilung auf mehrere Anlagen je Land oder regionale Fonds.
- **Betroffene Kapitel/Funktionen:** Theorie 3.11; Methodik, BIP-Gewichtung; Analyse 5.3.7, 5.6 und 5.8.2; geplantes `country_weighting`; `neue_gewichtung`, `rebalancing`.
- **Mögliche Optionen:** Reine BIP-Gewichtung mit eindeutigem Länderproxy und dokumentierter Abbildung; Vergleich eines bestehenden gemischten ETF als eigene Buy-and-Hold-Anlage; eigene gemischte Gewichtungsstrategie mit zusätzlichem Datenvertrag. Marktkapitalisierungsgewichtete Länderindizes können die Binnenlandgewichtung liefern, müssen aber als solche geprüft werden.
- **Auswirkungen:** Bestimmt Strategie, benötigte Daten und Ergebnisinterpretation. Fehlende Länder dürfen nicht still aus dem BIP-Nenner verschwinden; mehrere Proxys pro Land dürfen kein BIP doppelt zählen. Konkrete Länder und Wertpapiere bleiben OD-14/OD-18.
- **Empfehlung von Codex:** Für die allgemeine Länderstrategie die einfache Theorieformel als klar abgegrenzten Umfang bestätigen lassen und eine explizite Länder-Anlagen-Zuordnung verlangen. Den beschriebenen ETF nicht ohne Entscheidung als gleichwertige Umsetzung dieser Formel behandeln.
- **Klassifikation:** **BLOCKING** — Ländergewichtungsmodul und fachlicher Strategieumfang.

## OD-12 — BIP-Verfügbarkeit, Revisionen und Aktualisierungsregel

- **ID:** OD-12
- **Frage:** Welche historische BIP-Version darf zu welchem Entscheidungszeitpunkt verwendet werden, müssen alle Länder denselben Bezugszeitraum besitzen, und wann werden daraus tatsächlich neue Portfolioanteile?
- **Warum notwendig:** `period` ist kein Veröffentlichungsdatum. `available_from` ist vorgesehen, seine genaue Regel jedoch ausdrücklich offen. Ein heute revidierter Jahreswert mit dem historischen Datum der Erstveröffentlichung bleibt ein Look-ahead-Fehler. Die BIP-Rebalancingfrequenz und der Umgang mit nicht verfügbaren Ländern fehlen.
- **Betroffene Kapitel/Funktionen:** Theorie 3.11 und 3.13.2; Analyse 5.3.7, 5.4.3 und 5.8.2; geplantes `country_weighting`; `rebalancing`.
- **Mögliche Optionen:** Historische Vintages mit tatsächlich damaligen Veröffentlichungsdaten; ausdrücklich dokumentierte, konservative Verfügbarkeitsannahmen bei fehlenden Vintages; revidierte Ex-post-Daten nur als gesondert bezeichnete, eingeschränkte Analyse. Gemeinsamer abgeschlossener BIP-Zeitraum oder jüngster verfügbarer Wert je Land; fester Gewichtsaktualisierungstermin oder Aktualisierung nach Veröffentlichungen.
- **Auswirkungen:** Bestimmt Look-ahead-Freiheit und Vergleichbarkeit. Nominales/reales/PPP-BIP, Einheit und gemeinsamer Bezugszeitraum müssen konsistent sein. Verfügbarkeitszeitpunkte, alte gültige Werte und echte Lücken sind voneinander zu unterscheiden; automatische Renormierung bei fehlenden Ländern wäre eine zusätzliche Regel.
- **Empfehlung von Codex:** Zum festgelegten Entscheidungszeitpunkt nur zu diesem Zeitpunkt verfügbare Versionen zulassen; gemeinsame Einheit und einen ausdrücklich bestätigten Bezugszeitraum verwenden. Gewichtsermittlung und Ausführung zeitlich trennen. Ohne geeignete historische Verfügbarkeitsinformationen den Lauf stoppen oder die Einschränkung ausdrücklich vom Autor genehmigen lassen. Konkrete Quelle und numerischer Veröffentlichungslag bleiben spätere Versuchswerte.
- **Klassifikation:** **BLOCKING** — zeitliche und methodische Regeln der Länderstrategie.

## OD-13 — Zulässige Gewichte und nicht investiertes Kapital

- **ID:** OD-13
- **Frage:** Welche allgemeinen Einschränkungen gelten für Start-/Zielgewichte: vollständige Long-Anlage mit Summe 1, ausdrücklich bilanziertes Rest-Cash oder auch Hebel/Short-Positionen?
- **Warum notwendig:** Analyse 5.6.2 nennt für Buy-and-Hold ein Startgewicht, zeigt aber nur eine einzelne Anlage ohne Cash-Vertrag. Die Theorie-Beispielgewichte von `portfolio_risiko` summieren sich auf 0.8. `rebalancing` mit Zielsumme 0.9 erzeugt bei Vermögen 100 Transaktionen mit Summe -10, ohne den Rest als Cash auszuweisen.
- **Betroffene Kapitel/Funktionen:** Theorie 3.7.2, Codezelle 52, 3.8 und 3.9; Analyse 5.6.2 und 5.7.2; `portfolio_risiko`, `neue_gewichtung`, `rebalancing`, `buy_and_hold`.
- **Mögliche Optionen:** Vollständig investierte, nichtnegative Gewichte mit Summe 1; zusätzliche explizite Cash-Position mit bestätigter Verzinsung; gesonderte Unterstützung von Hebel/Short mit zusätzlicher Methodik. Die Trendfolge ist bereits ausdrücklich Long/Cash und darf nicht automatisch um Short erweitert werden.
- **Auswirkungen:** Bestimmt Kapitalerhaltung, erlaubte Konfigurationen und Kennzahlen. Eine Kovarianzrechnung mit Summe 0.8 ist mathematisch möglich, beschreibt ohne Cash-Erklärung jedoch kein vollständig spezifiziertes Gesamtportfolio.
- **Empfehlung von Codex:** Für die erste allgemeine Portfolioimplementierung vollständige Long-Gewichte mit Summe 1 und Einzelanlagen-Buy-and-Hold mit Gewicht 1 bestätigen lassen; weitere Kapitalanteile explizit modellieren. Das 0.8-Beispiel als unvollständiges Portfolio kennzeichnen, nicht still normalisieren.
- **Klassifikation:** **BLOCKING** — Konfigurationsvalidierung und Kapitalmodell.

## OD-14 — Endgültige Anlagen, Indizes und Benchmark

- **ID:** OD-14
- **Frage:** Welche endgültigen Wertpapiere/Indizes, Länderproxies und welcher Benchmark werden in der Maturarbeit eingesetzt?
- **Warum notwendig:** Wissenschaftliche Vergleichbarkeit benötigt eine begründete Auswahl, einschliesslich Total Return, Dividendenbehandlung, Historie und möglichem Survivorship Bias. `EQ_DEMO`, `BD_DEMO` und Beispieljahre sind keine Auswahl.
- **Betroffene Kapitel/Funktionen:** Theorie 3.1, 3.9–3.13; Analyse 5.1, 5.4 und 5.9.3; sämtliche Strategien und Importadapter.
- **Mögliche Optionen:** Geeignete Total-Return-Indizes; geeignete bereinigte ETF-Reihen; dokumentierte andere Proxys. Der Autor bestimmt konkrete Titel und Anlageuniversum.
- **Auswirkungen:** Bestimmt Datenabdeckung, Währung und Aussagebereich; eine Datenreihe muss ihre Bedeutung belegen. Ein Performance-Import ist kein Nachweis einer realen historischen Ausführbarkeit zu diesen Werten.
- **Empfehlung von Codex:** Nach Prüfung der allgemeinen Engine auswählen und begründen, vor dem Hauptversuch fixieren. Bis dahin ausschliesslich künstliche Testanlagen verwenden.
- **Klassifikation:** **NON-BLOCKING** — allgemeine Engine; vor Hauptversuch erforderlich.

## OD-15 — Endgültiger Untersuchungszeitraum und allgemeine Versuchswerte

- **ID:** OD-15
- **Frage:** Welcher Zeitraum, welches Startkapital, welche Basiswährung und welche Datenfrequenz gelten für den Hauptversuch?
- **Warum notwendig:** Die Methodik listet Rahmenbedingungen, aber noch keine Werte. Alle verglichenen Strategien benötigen gleiche Auswertungsbedingungen.
- **Betroffene Kapitel/Funktionen:** Methodik, Bedingungen; Theorie 3.13.1; Analyse 5.6.1 und 5.9.3; Konfiguration, Zeitraumvorbereitung, Kennzahlen.
- **Mögliche Optionen:** Unterschiedliche fachlich begründete Zeiträume und Frequenzen innerhalb der freigegebenen allgemeinen Regeln; separate vorher definierte Teilperiodenanalysen.
- **Auswirkungen:** Bestimmt Datenumfang und Aussagekraft. Die technische Regel für Start und Perioden ist OD-02/OD-03 und muss früher entschieden werden.
- **Empfehlung von Codex:** Erst nach allgemeiner Integration und Dateneignungsprüfung durch den Autor festlegen. Keine Werte aus dem JSON-Beispiel übernehmen und den Zeitraum nicht nach dem besten Resultat auswählen.
- **Klassifikation:** **NON-BLOCKING** — allgemeine Engine; vor Hauptversuch erforderlich.

## OD-16 — Endgültige risikofreie Serie

- **ID:** OD-16
- **Frage:** Welche konkrete risikofreie Serie mit welcher Währung, Laufzeit und Datenquelle gilt für die Untersuchung?
- **Warum notwendig:** Die allgemeinen Einheiten-/Ausrichtungsregeln wählen noch keine passende Serie aus. Eine Serie ohne ausreichende Abdeckung ist kein vollständiger Vergleichsmassstab.
- **Betroffene Kapitel/Funktionen:** Theorie 3.6; Analyse 5.3.7, 5.4.3 und 5.9.3; `sharpe_ratio`.
- **Mögliche Optionen:** Unterschiedliche fachlich begründete Zins- oder Renditereihen; passende bereits berechnete Periodenrenditen. Eine Raw Sharpe Ratio ist keine still zulässige Ersatzserie.
- **Auswirkungen:** Verändert Überschussrenditen und Sharpe Ratio. Falls Cash verzinst wird, ist dessen Anlage gesondert zu begründen.
- **Empfehlung von Codex:** Autor entscheidet nach Prüfung von Basiswährung, Laufzeit, Historie und Zinssemantik; die allgemeine Engine zunächst mit synthetischen passenden Reihen testen.
- **Klassifikation:** **NON-BLOCKING** — allgemeine Engine; vor Hauptversuch erforderlich.

## OD-17 — Endgültige SMA-Fenster und Signalreihe

- **ID:** OD-17
- **Frage:** Welche konkreten kurzen und langen SMA-Fenster und welche geeignete Signalreihe werden vor dem Hauptversuch festgelegt? Soll dabei ein expliziter Performance-Fallback zugelassen werden?
- **Warum notwendig:** Beispielwerte sind unverbindlich. Die erlaubte Trennung von Signal und Performance entscheidet noch nicht, welche konkrete Reihe fachlich geeignet ist; nachträglich adjustierte Signaldaten benötigen eine Eignungsprüfung.
- **Betroffene Kapitel/Funktionen:** Theorie 3.12 und 3.13.3; Analyse 5.3.6, 5.6.2 und 5.9.3; `trendfolge`.
- **Mögliche Optionen:** Vorab begründete Fenster und separate Signalreihe; ausdrücklich erlaubte Verwendung der Performance-Reihe; vorab definierte Robustheitsanalysen. Kein automatischer Optimierungslauf als Hauptparameterwahl.
- **Auswirkungen:** Bestimmt Vorlaufbedarf und Signale. Ein Fallback darf nur auf ausdrückliche Konfiguration hin erfolgen. Die vorgegebene Verzögerung beträgt eine Periode; andere Verzögerungen erfordern eine begründete Erweiterung.
- **Empfehlung von Codex:** Auswahl durch den Autor vor dem Hauptvergleich dokumentieren. Anlauf- und Cash-Regel zuvor über OD-04/OD-05 klären; verschiedene synthetische Fenster nur zur technischen Prüfung verwenden.
- **Klassifikation:** **NON-BLOCKING** — allgemeine Engine; vor Hauptversuch erforderlich.

## OD-18 — Endgültige BIP-Daten und Länderabdeckung

- **ID:** OD-18
- **Frage:** Welche konkrete BIP-Quelle, welcher Indikator, welche Länder und gegebenenfalls welcher begründete Veröffentlichungslag gelten im Hauptversuch?
- **Warum notwendig:** Das Makroformat ersetzt keine Dateneignungsprüfung. Verfügbarkeitsangaben müssen zur tatsächlich gespeicherten Version passen.
- **Betroffene Kapitel/Funktionen:** Theorie 3.11; Analyse 5.3.7 und 5.4.3; geplantes `country_weighting`.
- **Mögliche Optionen:** Geeignete historische Vintages; geeignete amtliche Veröffentlichungsdaten; ausdrücklich genehmigte Daten mit dokumentierten Einschränkungen. Die Wahl eines nominalen/PPP-/realen Indikators muss zur in OD-12 bestätigten Bedeutung passen.
- **Auswirkungen:** Bestimmt Gewichte, Reproduzierbarkeit und Geltungsbereich. Eine angenommene Verzögerung beseitigt die Rückschau durch revidierte Werte nicht automatisch.
- **Empfehlung von Codex:** Erst nach Festlegung von OD-11/OD-12 durch den Autor auswählen; tatsächliche Versionen und Veröffentlichungsinformationen zusammen mit den Rohdaten archivieren.
- **Klassifikation:** **NON-BLOCKING** — allgemeine Engine; vor BIP-Hauptversuch erforderlich.

## OD-19 — Zusätzliche wissenschaftliche Auswertungen

- **ID:** OD-19
- **Frage:** Gehören Erholungsdauer, positive/negative Phasen, Krisenfestigkeit, zusätzliche Marktkapitalisierungsvergleiche und Out-of-Sample-Untersuchungen zum verbindlichen ersten Engine-Output oder zur späteren Auswertung?
- **Warum notwendig:** Methodik und Theorie erwähnen diese Analysen, Analyse 5.7 definiert jedoch nur einen Kernoutput und beispielhafte Kennzahlen. Für Krisen und Phasen fehlen exakte Grenzen und Messregeln.
- **Betroffene Kapitel/Funktionen:** Methodik, Kennzahlen; Theorie 3.5.3, 3.11 und 3.13.3; Analyse 5.7; QuantStats `drawdown_details`, geplante `analysis/metrics.py`.
- **Mögliche Optionen:** Kernkennzahlen der Analyse 5.7 zuerst; zusätzliche separat spezifizierte Auswertungen; klar benannte optionale Ergebnisse mit vorab festgelegten Perioden und Definitionen.
- **Auswirkungen:** Verändert Umfang und Fertigkriterien. Nicht abgeschlossene Erholungsphasen benötigen eine Regel; fehlende Kennzahlen dürfen nicht als 0 interpretiert werden. Zusätzliche wissenschaftliche Kennzahlen brauchen eigene Definitionen und Tests.
- **Empfehlung von Codex:** Den dokumentierten Kernoutput als erste technische Stufe bestätigen; wissenschaftliche Zusatzanalysen separat spezifizieren, ohne Datenphasen nach günstigen Ergebnissen auszuwählen. Bereits erwähnte Erholungsfunktionen auf Kompatibilität mit derselben Drawdown-Definition prüfen.
- **Klassifikation:** **NON-BLOCKING** — allgemeiner Kern; Entscheidung vor Erweiterung bzw. wissenschaftlicher Auswertung.
