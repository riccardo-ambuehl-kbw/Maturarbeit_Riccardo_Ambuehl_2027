# Wissenschaftliches und technisches Gegenlesen – Phase 2

Datum: 12. Oktober 2026. Verfasser dieses Prüfberichts: Codex. Autorenkontrolle und Freigabe stehen aus. **Die vorgeschlagenen Fachkorrekturen wurden nicht ausgeführt.**

Prüfstand: Branch `dev`, HEAD `c2cb80eb8bb512d562cdd43ed1a168f20cece5f6`, zu Beginn sauberer Arbeitsbaum. Repository: `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027`. Keine `AGENTS.md` im Schreib-Repository oder seinen übergeordneten Verzeichnissen gefunden. Der unverändert konservierte Auftrag steht unter `documentation/ai-usage/prompts/2026-10-12-gesamtgegenlesen-phase2.txt`.

## A. Zusammenfassung

### Gesamturteil und Beweisgrenzen

Die Arbeit hat einen nachvollziehbaren roten Faden und eine überwiegend vorsichtige Interpretation der historischen Ergebnisse. Forschungsfrage, Untersuchungsblöcke und Fazit passen zusammen. Die unabhängigen Rechnungen aus den vorhandenen Exporten bestätigen die Portfoliopfade und daraus ableitbaren Hauptkennzahlen. Es wurde **kein P0-Fehler in den realen Studienergebnissen nachgewiesen**. Daraus folgt keine vollständige fachliche Freigabe: Die ursprünglichen eingefrorenen Eingangsdateien sind an ihren dokumentierten Pfaden nicht zugänglich. Insbesondere die realen Sharpe-Werte und die Herkunft sämtlicher historischer Markt-, Zins- und BIP-Beobachtungen konnten hier nicht unabhängig vollständig geprüft werden.

Vor einer Abgabe sollten einzelne Theorieerklärungen, zwei Quellenverweise, die historische KI-Dokumentation und die formalen Abgabeteile korrigiert beziehungsweise ergänzt werden. Der Haupttext überschreitet den vorliegenden Schulrahmen deutlich. Eine begründete Auswahl und Kürzung muss der Autor entscheiden; sie ist keine Aufgabe dieses Gegenleselaufs.

| Priorität | Bedeutung im Auftrag | Anzahl |
|:---|:---|---:|
| P0 | Kritischer nachgewiesener Fehler in wesentlichen Ergebnissen/Aussagen | 0 |
| P1 | Vor der Abgabe wichtig: fachlich, mathematisch, quellenbezogen oder abgaberelevant | 11 |
| P2 | Relevante sprachliche, didaktische oder strukturelle Verbesserung | 6 |
| P3 | Kleiner optionaler Hinweis | 0 |
| **Gesamt** | Eindeutige Befunde R-001 bis R-017 | **17** |

**Status:** 16 BESTÄTIGT, 0 VERDACHT, 1 NICHT VERIFIZIERBAR. Der ungeklärte Befund R-017 ist eine Zugangs- und Nachweisgrenze, kein nachgewiesener Rechenfehler. BESTÄTIGT bezeichnet jeweils das genau beschriebene Problem, nicht eine pauschale Fehlerhaftigkeit des gesamten Abschnitts. Bereits bekannte offene Abgabeteile werden gemeinsam als R-016 geführt, nicht mehrfach gezählt.

### Wichtigste Risiken und Korrekturreihenfolge

1. **R-002/R-016:** Umfang, vollständige Titelseite, Abstract, Verzeichnisse und Eigenständigkeitserklärung mit Betreuungsperson klären. Der notwendige Kürzungsumfang beeinflusst die spätere Textkorrektur.
2. **R-001/R-003/R-004/R-006/R-007/R-015:** Gespeicherte Beispielausgabe, Quellenzuordnung und missverständliche Finanzdefinitionen gezielt berichtigen.
3. **R-005/R-017:** Veraltete Referenzfunktion abgrenzen und vorhandenes eingefrorenes Datenarchiv wieder zugänglich machen; keine neue Studie starten.
4. **R-008/R-012:** Tatsächliche historische Programmierhilfe vollständig nachtragen und den Stand der Autorenkontrolle eindeutig datieren.
5. **R-009 bis R-014:** Seitenlocator, Versionshinweise, Präzisierungen und überholte beziehungsweise doppelte Textstellen bereinigen.

### Bereiche ohne relevante Auffälligkeiten

- Forschungsfrage in Einleitung und Fazit ist identisch; die Analyse beantwortet sie anhand konkreter Ergebnisse und Grenzen.
- H1 und Z1 werden als unterschiedliche Markt- **und** Zeitraumkonstellationen behandelt. K1 vergleicht BIP- und Gleichgewichtung derselben sieben Länder-ETFs; Gleichgewichtung wird nicht als Marktkapitalisierungsgewichtung ausgegeben.
- SMA 3/12 bleibt die vorab festgelegte Hauptvariante. SMA 2/12 und 6/12 bleiben ergänzende Sensitivitätsvarianten. Die bessere historische 6/12-Rendite wird nicht zur nachträglich ausgewählten Hauptstrategie gemacht.
- Niedrige Volatilität und geringer MDD werden ausdrücklich unterschieden. Das schwächere H1-MDD der Trendstrategie wird nicht versteckt.
- USD-Auswertung, nominale Renditen, Fonds-Proxys, fehlende zusätzliche Handelskosten/Steuern und unverzinste Cash-Phasen sind als Grenzen erkennbar. Die risikofreie Vergleichsreihe der Sharpe Ratio ist von diesem Cash unterschieden.
- Aktuelle MDD-Definition und aktueller Theorie-Code berücksichtigen den Ausgangswert. Die geometrische Annualisierung und die Stichprobenstandardabweichung mit `ddof=1` sind konsistent. Frühere Befunde zu einer Gewichtssumme von 0,8 und zur fehlenden Ausgangswertbegrenzung im Theorie-Notebook sind im jetzigen Stand erledigt.
- Die Ergebnisinterpretation bleibt historisch und beansprucht weder sichere zukünftige Renditen noch einen statistisch oder kausal bewiesenen allgemeinen Strategiesieg.

### Tatsächlich ausgeführte Prüfung

Alle sechs Notebooks und `ki-nutzung.qmd` vollständig gelesen: 467 Zellen, davon 28 Codezellen und 28 gespeicherte Output-Objekte. Die acht gespeicherten PNG-Diagramme wurden aus den Outputs nur zum Betrachten in ein externes temporäres Verzeichnis dekodiert und visuell geprüft. Keine Notebook-Zelle ausgeführt. Alle 28 Codezellen statisch auf Python-Syntax geprüft. Funktionen, Aufrufreihenfolge, Variablen, Formeln, Zeitbezug und Erklärungen wurden miteinander verglichen. Kleine Gegenrechnungen liefen separat mit Standardbibliotheksfunktionen, nicht durch Ausführen der originalen Notebook-/Engine-Funktionen.

Zusätzlich gelesen beziehungsweise geprüft: `_quarto.yml`, `references.bib`, CSL-Datei, `README.md`, `src/funktionen.py`, KI-Log und zugehörige Arbeitsanweisungen, Formatierungsbericht vom 12.10.2026, Lehrerfeedback-Bericht sowie die relevanten Schulvorgaben. Die zweiseitige Vereinbarung hat keine extrahierbare Textebene; beide Seiten wurden aus ihrer PDF-Darstellung visuell gelesen. Die markierte wissenschaftliche schriftliche Arbeit macht den Umfangsrahmen für diesen Entwurf relevant. Es wurde keine dokumentierte Ausnahme vom Umfang gefunden.

Das separate Verzeichnis `C:\Users\modic\Documents\GitHub\Maturarbeit_Engine` fehlt. Der in allen fünf Manifesten genannte Commit `1954bfbcb257b51e7f9174aa824cb35e437de752` ist jedoch im lokalen Git verfügbar. Verträge, finale Konfigurationen, relevante Engine-Funktionen und historische Freigabe-/Freeze-Nachweise wurden mittels `git show` gelesen. Das ist keine Wiederholung des vollständigen früheren Engine-Audits. Frühere Testberichte wurden als historische Nachweise behandelt; deren Tests, Wheels und Demos wurden hier nicht erneut ausgeführt.

Die Quellenprüfung verwendete vorhandene Originalbücher/-publikationen in Zotero und offizielle Dokumentationen beziehungsweise Anbieter-Webseiten. Es wurden keine neuen Finanzdaten heruntergeladen. Die genaue Abdeckung und ihre Grenzen stehen in B und D. Kein kostenpflichtiger Plagiatscheck; keine Aussage über die vollständige Originalität sämtlicher Formulierungen.

## B. Kapitelweise Prüfung

### 1. Überblick – `index.ipynb`

Geprüft: vollständiger Text, Projektanleitung, Strukturübersicht, Quellenbeispiel und Einordnung im Buch. Befund: **R-014**, überholte Dateipfade und Zukunftsformulierungen. Der Text ist als technische Projektübersicht verständlich, entspricht aber teilweise dem früheren QMD-Gerüst. Das wörtliche Beispiel `@markowitz1952` steht in einem Markdown-Codeblock und ist keine aktive, fehlerhafte Zitation. Ob diese technische Anleitung im wissenschaftlichen Haupttext bleiben oder in README/Anhang wechseln soll, ist eine Autorenentscheidung, kein nachgewiesener inhaltlicher Widerspruch.

### 2. Einleitung – `notebooks/Einleitung.ipynb`

Geprüft: Motivation, Fragestellung, Ziele, Abgrenzung und Zusammenhang mit Methodik/Analyse/Fazit. Die Forschungsfrage in Zelle `ef01feb0` stimmt mit Fazit-Zelle `ed6169f5` überein. Die Entwicklung eines eigenen Werkzeugs und dessen Anwendung auf vier Strategietypen werden tatsächlich behandelt. Literarische Einordnung, persönliche Motivation und wissenschaftliche Aussagen bleiben unterscheidbar. Keine eigenständige relevante Auffälligkeit ausser dem kapitelübergreifenden Umfang R-002.

Die ursprünglich vereinbarte Frage ist allgemeiner formuliert als die aktuelle Werkzeug-/Vergleichsfrage. Das ist nicht automatisch ein Widerspruch oder ein nicht genehmigter Themenwechsel; der aktuelle Text bleibt thematisch im vereinbarten Rahmen. Eine ausdrückliche Bestätigung der endgültigen Fragestellung durch den Autor/die Betreuungsperson liegt für diesen Audit nicht vor (D).

### 3. Theorie – `notebooks/Theorie.ipynb`

Geprüft: alle 86 Zellen, 17 Codezellen, gespeicherte Ausgaben, Formeln und Quellen. Betroffen sind **R-001, R-003, R-004, R-006, R-007, R-009, R-010, R-011 und R-015**; die Funktionsabweichung ausserhalb des Notebooks steht unter R-005. R-002/R-016 gelten zusätzlich für Umfang und formale Einbindung.

Tragfähig: Diversifikation und Kovarianzformel; Markt-/BIP-Gewichtung als unterschiedliche Regeln; praktische Indexnachbildung durch vollständige Replikation, Sampling oder Tauschverträge; ETF-Abkürzung; Buy-and-Hold/Rebalancing; Zusammenhang zwischen Logrenditen und Wachstumsfaktoren; einfache/logarithmische Renditen; geometrisches Mittel als Mittel der **Wachstumsfaktoren**, nicht der blossen Nettorenditen; Stichprobenvolatilität; aktueller MDD-Zeitbereich; Sharpe Ratio aus zeitlich abgestimmten Überschussrenditen mit Stichprobenstandardabweichung. Die Erklärung der acht Sharpe-Variablen ist jetzt vollständig.

Beispielkontrollen ohne Notebook-Ausführung: Rebalancing-Werte 84 / 20,4 / 10,5, Gesamtwert 114,9 und Trades −3,57 / +2,58 / +0,99 stimmen; Buy-and-Hold-Endwert 107,066444 stimmt; geometrisches Mittel der Faktoren 1,1 / 1,2 / 0,9 / 1,05 = 1,056821 und annualisierte Rendite = 94,0963 % stimmen; Beispielstandardabweichung 0,125 und annualisierte Volatilität 0,4330127 stimmen; aktuelles MDD-Beispiel = −24 %; Sharpe-Beispiel = 1,234888 und Ausgabe 1,23 stimmen. Die kumulierten Logrenditen sind bei ihrer anschliessenden Exponentialumwandlung richtig verwendet. Der Name `kumulierte_rendite` allein ist kein Nachweis eines Rechenfehlers.

Die SMA-Spielzeugreihe weist während des undefinierten langen Durchschnitts Cash zu; die echte Engine nutzt vorgelagerte Warm-up-Daten und beginnt den Messzeitraum erst danach. Diese Vereinfachung erklärt einen Unterschied, beweist aber keine falsche Studie. Ein kurzer ausdrücklicher Hinweis wäre didaktisch hilfreich, ist hier kein zusätzlicher Fehlerbefund. QuantStats ist in der lokalen Projektumgebung nicht installiert; keine Installation und keine Ausführung nachgeholt. Die konkrete Bedeutungsabweichung der gespeicherten Erholungs-Tabelle ist dennoch rechnerisch nachweisbar (R-006).

### 4. Methodik – `notebooks/Methodik.ipynb`

Geprüft: Daten-/Assetauswahl, globale Hauptperiode, US-Ergänzung, Monatswerte, adjusted close, BIP-Veröffentlichungsstände, risikofreier Proxy, Cash-Regel, Strategieparameter und Grenzen. Keine zusätzliche gesicherte methodische Fehlbehauptung gefunden. Nominales BIP in USD-Milliarden und nicht kaufkraftbereinigtes BIP ist eindeutig; dies ist die gewählte Definition. Die Aktien-/Anleiheninstrumente sind ETFs und werden nicht als direkt investierbare kostenlose Indizes beschrieben. IEF ist ein Fonds für US-Treasuries mit 7–10 Jahren Laufzeit und nicht der risikofreie Sharpe-Proxy.

Die FRED-DGS3MO-Reihe ist als annualisierte Zinsquote in Prozent veröffentlicht. Die Verwendung eines verzögerten Satzes und einer ACT/365-Näherung ist als Modellannahme kenntlich gemacht; sie ist nicht identisch mit einem handelbaren Total-Return-Index. Die Konzeptbeschreibung ist stimmig. Die tatsächlichen täglichen Originalwerte und ihre Überführung in alle Monatswerte sind ohne das Archiv nicht nachprüfbar (**R-017**). Gleiches gilt für alle konkreten WEO-Vintage-Zellen. R-002 betrifft den Gesamtumfang, nicht einen isoliert fehlerhaften Methodikabschnitt.

### 5. Analyse – `notebooks/Analyse.ipynb`

Geprüft: alle 269 Zellen, 11 Codezellen, Exporte/Manifeste, Tabellen, sieben gespeicherte Diagramme, Beschreibungen und Interpretation. **R-013** betrifft eine identische Absatzdoppelung. **R-008/R-017** betreffen die historische KI-Dokumentation beziehungsweise die Beweisgrenze zu den Eingangsdaten. Kein nachgewiesener Fehler in den aus verfügbaren Portfoliopfaden berechenbaren realen Hauptkennzahlen.

| Block | Tatsächliche Konstellation | Vergleichsaussage |
|:---|:---|:---|
| H1 | VT / IEF / VT-SMA 3/12 / sieben G7-Länder-ETFs mit BIP-Gewichten; Renditen 2010–2025 | Globaler Hauptvergleich; VT und G7-Portfolio haben verschiedene Universen |
| K1 | Dieselben sieben ETFs, BIP versus je 1/7, jährliches Rebalancing, 2010–2025 | Geeignet zur Trennung dieser beiden Gewichtungsregeln im festgelegten Universum; keine MK-Kontrolle |
| Z1 | VTI / IEF / VTI-SMA 3/12; Renditen 2003–2025 | US-Markt und längerer Zeitraum gleichzeitig verändert |
| S1/S2 | VT-SMA 2/12 beziehungsweise 6/12; Renditen 2010–2025 | Vordefinierte ergänzende Sensitivität, kein Ersatz für die Hauptvariante |

**Integrität und Provenienz:** Alle fünf Manifest-Dateihashes stimmen mit den Erwartungen in Plot-/Ladezelle `99cad7ec` überein. Alle **25** von diesen Manifesten aufgeführten Ergebnisdateien stimmen bytegenau mit ihren SHA-256-Werten überein. Die fünf finalen Config-Dateien wurden als Git-Blobs des eingefrorenen Commits geprüft; ihre Bytes passen zu den Eingangs-Hashes. Jedes Manifest enthält 24 Code-/Paketdatei-Hashes. Die Git-Blobs passen; bei `src/funktionen.py` reproduziert die LF→CRLF-Zeilenendenumwandlung den Manifest-Hash exakt. Dies ist eine nachvollziehbare Zeilenendenabweichung, kein nachgewiesener Codewechsel. Die Originaleingaben wurden dadurch nicht ersetzt oder nachträglich als verifiziert ausgegeben.

**Unabhängige Exportkontrolle:** Für alle elf Strategie-Reihen über fünf Läufe wurde jede verfügbare Vermögens-/Rendite-/Drawdown-Zeile durch einfache Rekursion beziehungsweise Hochwasserstandkontrolle geprüft. Rendite = `V_t/V_(t-1)-1`; Jahresrendite = `(V_N/V_0)^(12/N)-1`; Jahresvolatilität = Stichprobenstandardabweichung der Monatsrenditen × √12; MDD = Minimum der Drawdowns einschliesslich Ausgangswert. Übereinstimmung der abgeleiteten Hauptkennzahlen bis auf gewöhnliche Gleitkommatoleranz ≤ 10^−12; keine Ersetzung vorhandener Ergebnisse. H1/K1/S1/S2 enthalten 193 Bewertungszeitpunkte und 192 Renditen; Z1 277 beziehungsweise 276. Der Startwert ist der Bewertungszeitpunkt vor der ersten ausgewerteten Monatsrendite.

| Lauf/Strategie | Endvermögen USD | Geometrische Jahresrendite | Jahresvolatilität | MDD |
|:---|---:|---:|---:|---:|
| H1 Buy-and-Hold | 466’061,26 | 10,10 % | 14,77 % | −25,51 % |
| H1 BIP | 469’842,35 | 10,15 % | 14,98 % | −26,39 % |
| H1 60/40 | 311’991,42 | 7,37 % | 8,93 % | −21,57 % |
| H1 Trend 3/12 | 262’910,87 | 6,23 % | 11,85 % | −29,69 % |
| K1 BIP | 469’842,35 | 10,15 % | 14,98 % | −26,39 % |
| K1 Gleichgewichtung | 323’348,36 | 7,61 % | 16,31 % | −27,09 % |
| S1 Trend 2/12 | 261’863,42 | 6,20 % | 11,28 % | −22,15 % |
| S2 Trend 6/12 | 338’010,82 | 7,91 % | 12,79 % | −22,15 % |
| Z1 Buy-and-Hold | 1’224’167,13 | 11,51 % | 14,93 % | −50,84 % |
| Z1 60/40 | 689’366,99 | 8,76 % | 8,98 % | −26,79 % |
| Z1 Trend 3/12 | 733’369,66 | 9,05 % | 11,12 % | −22,14 % |

72 gedruckte Kennzahlenfelder in den vier Tabellen 5.12.1–5.12.4 wurden gegen die Summary-Exporte kontrolliert, einschliesslich richtiger Rundung/Vorzeichen. **Für Sharpe ist dies nur ein Übertragungsabgleich**, weil die echten risikofreien Monatsreihen fehlen. Die obige Tabelle enthält deshalb keine unabhängig behaupteten Sharpe-Werte. Alle acht gespeicherten Diagramme zeigen die dazu passenden Reihen, Achsen und Rangfolgen; die Plotzelle lädt vorhandene Exporte statt neue Hauptläufe auszuführen. Die sieben Analysegrafiken und die Theorieillustration wurden visuell angesehen, nicht neu berechnet.

Weitere Prüfungen: H1- und K1-BIP-Pfade sind identisch. Die Jahresrenditen der beiden H1-Halbperioden stimmen (Buy-and-Hold 9,52 % / 10,68 %, 60/40 7,74 % / 7,00 %, Trend 4,57 % / 7,91 %, BIP 9,45 % / 10,86 %). 60/40-Halbperiodenvolatilitäten 7,27 % / 10,37 % stimmen. Halbperioden-Sharpe bleibt mangels Rf-Reihe offen. Die Jahresbetrachtung 2020/2022 und der H1-Trend-MDD zwischen April 2011 und Mai 2012 passen zu den Exporten. Der Rebalancing-Trade Ende 2010 verschiebt 893,49 USD von VT nach IEF ohne Vermögensänderung. Alle sieben Monatszeilen Februar–August 2020 mit VT-Rendite, Position, neuem Signal und Trendrendite stimmen; das Cash-Signal im März wirkt erst im April.

Bei allen drei VT-SMA-Reihen entspricht die gehaltene Position dem Signal der Vorperiode: S1 153 Long-/39 Cash-Monate und 18 Wechsel; H1 156/36 und 12; S2 153/39 und 12. Die US-Cashphase Februar 2008 bis Juni 2009 ist in Z1 nachvollziehbar. Dies stützt die Signalverzögerung; ohne ursprüngliche Marktpreise ist die Neuberechnung aller SMA-Werte trotzdem offen.

Die 16 BIP-Entscheidungsstände/112 Länderzeilen der Qualitätsnachweise erfüllen `available_from <= Entscheidungsdatum`; die Zielgewichte entsprechen jeweils BIP/Summe(BIP). Der dokumentierte gemeinsame Datenjahrgang 2020 im Entscheidungsstand Ende 2022 und der GBR-Wert 2’758,87 USD-Milliarden passen zum früheren Autorenfreigabenachweis. Die USA-Zielgewichtsentwicklung 44,59 % → 58,55 % und die sieben gedruckten Ländergewichte passen zu den Exporten. **Damit ist die innere Konsistenz geprüft, nicht die Echtheit aller zugrunde liegenden WEO-Zellen.**

### 6. Fazit – `notebooks/Fazit.ipynb`

Geprüft: vollständiger Text, identische Forschungsfrage, Zahlen/Rangfolgen, Grenzen, eigene Bewertung und Ausblick. Die Antwort unterscheidet Ertrag, Volatilität und MDD sinnvoll. Der kleine H1-Renditevorsprung der BIP-Variante wird nicht als allgemeine Überlegenheit interpretiert. Der US-Anteil ist als mögliche Erklärung, nicht als vollständig durchgeführte Kausalanalyse dargestellt. Die Resultate von K1/Z1/S1/S2 werden richtig zugeordnet. Keine eigenständige gesicherte neue Auffälligkeit. R-002 und die Nachweisgrenze R-017 bleiben kapitelübergreifend relevant; die Autorenverantwortung ist erkennbar.

### Anhang: KI-Nutzung – `ki-nutzung.qmd`

Geprüft: vollständiger Anhang, aktueller ausführlicher Log, Nachträge zu Lehrerfeedback/Formatierung, historische Engine-Einträge im verfügbaren Referenzcommit und Aussagen zur manuellen Kontrolle. **R-008:** Nachweisbare Programmier-/Adaptereinsätze fehlen im aktuellen Gesamtlog und sind im Buchanhang nicht ausreichend abgebildet. **R-012:** Eine undatierte allgemeine Aussage über abgeschlossene Autorenkontrolle ist neben ausdrücklich ausstehenden Kontrollen missverständlich. Die ChatGPT-Erklärungsarbeit zum Lehrerfeedback ist jetzt ausdrücklich erwähnt; sie wurde nicht pauschal als reine Formatierung ausgegeben. Der vorliegende Review wird nur als Prüfung/Bericht dokumentiert, nicht als ausgeführte Korrektur oder Autorenfreigabe.

### Literaturprüfung: Reichweite und konkrete Nachweise

Die gesamte BibLaTeX-Datei wurde durch Pandoc eingelesen: **52 eindeutige Einträge; 29 aktive Citation Keys; 157 aktive Vorkommen; keine unaufgelösten Keys**. Codeblock-Beispiele wurden ausgeschlossen. Die CSL-Datei ist Chicago 17, shortened notes and bibliography. 23 nicht aktiv zitierte Datenbankeinträge sind kein Fehler im ausgegebenen Literaturverzeichnis. Der Phase-1-Nachweis zur Ausgabe nur zitierter Werke wurde gelesen. Jeder aktive Key wurde auf Auflösung, Titel/Quelle und Verwendung geprüft; dies ist **keine lückenlose Bestätigung aller 157 Seitenbelege**.

| Quelle/aktive Keys | Was im Original geprüft wurde | Grenze/Ergebnis |
|:---|:---|:---|
| `hilpischPythonFinanceMastering2019` | Vorhandenes Original-PDF, Zotero `44965DIG`; relevante Stellen zu Frequenzen, Finanzzeitreihen, Änderungen/Logrenditen, Resampling, SMA und vectorized backtesting (angegebene Bereiche 191–192, 304, 315–328, 689–697) | Themenabdeckung plausibel; historische Alias-Tabelle benötigt Versionskennzeichnung R-011. Keine vollständige Einzelprüfung jedes Vorkommens. |
| `kommerSouveraenInvestierenMit2025` | Original-PDF, Zotero `A8Q9SBUT`; relevante Stellen zu nominal/real, Diversifikation, Risiken, Drawdown/Erholung, Sharpe, Allokation, Buy-and-Hold, Index-/ETF-Regeln, BIP und Rebalancing | Inhaltliche Grundlagen überwiegend gestützt. Abschnitt 9.2/PDF-Seiten 464–465 belegt die fälschlich dem Starterbuch zugeschriebenen Indexerklärungen R-003. |
| `kommerLeichteEinstiegWelt2025` | Original-EPUB, Zotero `MZ4YACD4`; OPF mit 192 Seiten, 2. Auflage; Kapitel 1 und Index-/ETF-Kontext | 464–465 unmöglich, R-003. Bei EPUB sind die übrigen Druckseiten 58–60 nicht zuverlässig als exakte Seitenanker verifizierbar; Kapitelbelege inhaltlich, Seitenlocator offen. |
| `mckinneyPythonDataAnalysis2022` | Original-PDF, Zotero `PJA9S9HY`; Zeitreihenkapitel, Datumskonvertierung und Kontext | PDF-Seite 511 ist Kapitelbeginn, `to_datetime` erscheint auf 516: R-009. Druck-/E-Book-Seitenzuordnung vor Ersetzen des Locators klären. |
| `markowitzPortfolioSelection1952` | Originalaufsatz, Zotero `FFDVRR6Q`, gedruckte Seiten 80–81 | Kovarianz-/Korrelationszusammenhang und Portfolio-Varianz sind gestützt. |
| `phamPerformance60402025` | Original-CFA-Publikation, Zotero `7XAAKIL6`, Seiten 1–7 und 50–51 | 60/40-Kontext, wechselnde Korrelationen, 2022 und Formeln gestützt. Gewichtete Periodenrendite benötigt tatsächliche Periodenanfangsgewichte R-004. Die Quelle ist keine Garantie für diesen ETF-Backtest. |
| `sharpeSharpeRatioFall2021` | Autorentext der ursprünglichen Veröffentlichung 1994 auf Stanford, Formeln und Zeitaggregation | Ex-post-Überschussrenditen/Standardabweichung und Bedingungen der √T-Annualisierung gestützt. Bib-Eintrag 2021 bezeichnet die verlinkte Wiederveröffentlichung, kein automatisch falsches Ursprungsjahr. |
| `PandasSeriespct_changePandas305`, `PandasSeriesstdPandas305` | Offizielle pandas-Dokumentation, auch vorhandene gespeicherte Originalseiten | Relative Änderung versus Prozentdarstellung, `ddof=1`/N−1 verifiziert. Live-Dokumentation inzwischen 3.0.6; keine automatische Änderung des historischen Zugriffstitels. |
| `aroussiRanaroussiQuantstats2026` | Öffentliches Originalrepository erreichbar; konkrete vorhandene Ausgabe mit Beispielvermögen verglichen | Keine festgehaltene lokale Paketversion und keine neue Ausführung. R-006 stützt sich auf gespeicherte Zahlen, nicht auf angenommene aktuelle Bibliothekssemantik. |
| `VanguardTotalWorld`, `VanguardMorningstarTotal`, `IShares710Year` | Gespeicherte Originalanbieter-Seiten und offizielle IEF-Seite; Anlageuniversum und Auflagezeitpunkte | VT ab 24.06.2008, VTI ab 24.05.2001, IEF ab 22.07.2002 passen zur gewählten Historie. Der aktuelle VTI-Name mit Morningstar-Benchmark ist belegt; keine falsche Korrektur auf einen älteren Benchmark. Vollständige historische Indexwechsel bleiben offen. |
| `ISharesMSCICanada`, `ISharesMSCIJapan`, `ISharesMSCIUnited`, `ISharesMSCIGermany`, `ISharesMSCIFrance`, `ISharesMSCIItaly` | Offizielle iShares-Produktseiten für alle sechs Nicht-USA-Länder | Länder-/Instrumentzuordnung bestätigt; aktuelle Produktseite ersetzt keinen historischen Kurs-/Ausschüttungsnachweis. |
| `WhatAdjustedClose`, `yahooYahooFinanzenDeutschlandBoerse2026` | Yahoo-Hilfeseite als gespeicherte Original-HTML-Datei `AKRA9QQ6`, insbesondere deren Artikeltext; Marktportal nur als Quellenidentifikation | Definition der Anpassung um Splits/Dividenden bestätigt; konkrete Kurswerte nicht bestätigt. Der Live-Hilfezugriff war zeitweise blockiert. |
| `MarketYieldUS2026`, `federalreservebankofst.louisFederalReserveEconomic2026`, `FederalReserveBoard` | Offizielle FRED-DGS3MO-Reihe und Federal-Reserve-H.15-Seite; vorhandene Quellenmetadaten | Quote/Einheit/Anbieter bestätigt, keine Wiederbeschaffung der historischen Zinsdaten. H.15 ist eine fortlaufend wechselnde Seite. |
| `WorldEconomicOutlooka`, `DownloadEntireWorld`, `WorldEconomicOutlook` | Offizielle IMF-FAQ zu tatsächlichen/geschätzten Daten und Revisionen; vorhandene bibliografische Original-Downloadverweise und gespeicherte 2009-Downloadseite | Direkte Live-Zugriffe auf die konkret verlinkten 2009-/2024-Downloadseiten scheiterten. Die tatsächlichen eingefrorenen Vintage-Dateien fehlen; einzelne Werte/Veröffentlichungstage nicht als originalverifiziert ausgegeben. |
| `PriceHistoryClassYfinance` | Offizielle yfinance-API-Dokumentation | Automatische Anpassung als Default, explizite Adapterwahl und Rolle von `repair` nachvollziehbar; tatsächlicher Raw-Download nicht erneut geprüft. |
| `Preise` | Gespeicherte Original-BFS-HTML-Seite `8NRJRVVL`, Tabelle 2016–2025 | Historisches Mittel korrekt gerundet; daraus abgeleiteter Zukunftsschwellenwert falsch R-015. |

PDF-Seitenzahlen in dieser Prüfung beziehen sich bei konvertierten E-Book-PDFs auf die tatsächlichen Datei-Seiten, sofern nicht ausdrücklich „gedruckte Seite“ genannt ist. Bei abweichender Druckpaginierung sind Kapitel-/Abschnittsangaben sicherer. Quelleninhalte wurden nicht erfunden, unzugängliche historische Daten nicht mit aktuellen Webwerten ersetzt.

Original-Webnachweise für die fachlichen Kontrollen: [Sharpe, The Sharpe Ratio](https://web.stanford.edu/~wfsharpe/art/sr/sr.htm), [pandas pct_change](https://pandas.pydata.org/docs/reference/api/pandas.Series.pct_change.html), [pandas std](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html), [FRED DGS3MO](https://fred.stlouisfed.org/series/DGS3MO), [Federal Reserve H.15](https://www.federalreserve.gov/releases/h15/), [IMF WEO FAQ](https://www.imf.org/en/Publications/WEO/frequently-asked-questions), [yfinance PriceHistory](https://ranaroussi.github.io/yfinance/reference/yfinance.price_history.html), [IEF](https://www.ishares.com/us/products/239456/ishares-710-year-treasury-bond-etf). Die besonderen Fehlerbelege stehen direkt bei R-007/R-011; die lokalen Originalpublikationen und Schulunterlagen sind die Belege der übrigen quellenbezogenen Befunde.

## C. Vollständige Befundliste

### R-001 – Gespeicherte Portfolio-Volatilität passt nicht zu den aktuellen Beispielgewichten

**Priorität/Status:** P1 · BESTÄTIGT.

**Datei/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\notebooks\Theorie.ipynb`; 3.1.2.2 Python-Beispiel Portfoliorisiko; Codezelle `5b4e89ac`, gespeicherte Stream-Ausgabe.

**Originalauszug:** `gewichte = pd.Series({"Aktien": 0.20, "Anleihen": 0.40, "ETF": 0.40})`; Ausgabe `Volatilität: 1.15%`.

**Problem:** Der Code ist für die angegebenen Daten mathematisch richtig; die gespeicherte Ausgabe ist veraltet/falsch. Die Gewichte ergeben jetzt 1,00. Die richtige Periodenvolatilität ist 1,57 %, nicht 1,15 %.

**Prüfnachweis:** Gewichtete sechs Renditen: `[0.024, −0.014, 0.004, 0.030, 0.006, 0.014]`. Mittelwert = 0,0106666667. Stichprobenvarianz `Σ(r−Mittel)²/(6−1)` = 0,0002474666666666667; Quadratwurzel = 0,0157310732840028. Dies ist identisch zur Kovarianzrechnung `wᵀΣw` bei vollständigen Zeilen und festen Gewichten. Mit der vorhandenen Formatierung folgt `1.57%`. Keine Annualisierung in diesem Beispiel.

**Kleinste Korrektur:** In einem späteren Lauf nur das konkrete Beispiel mit den aktuellen Gewichten kontrolliert neu ausführen und seine Output-/Execution-Metadaten ehrlich aktualisieren. Keine reale Studie neu ausführen.

**Auswirkung:** Beispielausgabe und Darstellung des Theoriekapitels; keine Abweichung der realen Exportkennzahlen nachgewiesen.

**Autorenentscheidung:** Keine neue Gewichtungsmethode nötig. Freigabe des späteren gezielten Notebook-Korrekturlaufs erforderlich; hier unverändert belassen.

### R-002 – Haupttext überschreitet den dokumentierten Umfang deutlich

**Priorität/Status:** P1 · BESTÄTIGT, vorbehaltlich einer vom Autor nachgewiesenen individuellen Ausnahme.

**Dateien/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\notebooks\Einleitung.ipynb`, `Theorie.ipynb`, `Methodik.ipynb`, `Analyse.ipynb`, `Fazit.ipynb` im selben Notebook-Verzeichnis; gesamter Haupttext. Schulbeleg: `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\documents\Maturarbeit_Vorgaben_2027.pdf`, Datei-Seite 1; Arbeitsvereinbarung Datei-Seite 1.

**Originalauszug:** Schulvorgabe: „6000–8000 Wörter“ reiner Text für die einschlägige schriftliche Arbeitsform.

**Problem:** Schon die konservativere Zählung ergibt **14’838** Wort-/Zahlentoken; damit ungefähr 6’838 beziehungsweise 85 % über 8’000. Die Vereinbarung markiert eine wissenschaftliche schriftliche Arbeit; keine Ausnahme wurde gefunden.

**Prüfnachweis/Zählmethode:** Gezählt wurden ausschliesslich Markdown-Inhalte der Kapitel 2–6. Ausgeschlossen: Überblick, KI-Anhang, Bibliografie, Raw-/YAML-Zellen, Codezellen, Outputs/Bilder, Markdown-Codeblöcke, Formeln in `$$` und `$`, Zitationsklammern, Überschriften und Markdown-Tabellenzeilen. HTML-Tags wurden entfernt; Absätze, Listen, Inline-Fachbegriffe, Zahlen und kurze Quellen-/Tabellenlabel im verbleibenden Lauftext wurden mitgezählt. Token-Regel: `\b\w+(?:[’'-]\w+)*\b`. Keine Behauptung einer identischen Microsoft-Word-Zählung. Variante einschliesslich Überschriften und Tabellen, weiterhin ohne Code/Outputs/Mathematik/Zitationsklammern: **16’281**. Die Grössenordnung ist nicht durch einzelne Labels oder Zählkonventionen erklärbar.

| Kapitel | Lauftext-Token ohne Überschriften/Tabellen | Mit Überschriften/Tabellen |
|:---|---:|---:|
| Einleitung | 785 | 805 |
| Theorie | 3’670 | 3’954 |
| Methodik | 1’068 | 1’162 |
| Analyse | 8’363 | 9’383 |
| Fazit | 952 | 977 |
| **Summe** | **14’838** | **16’281** |

**Kleinste ausreichende Korrektur:** Zuerst verbindlichen Zielumfang/Anhangsregeln mit Betreuungsperson bestätigen; danach einen vom Autor ausgewählten Kürzungs-/Auslagerungsplan ausführen. Eine bloss kleine Stilkorrektur genügt nicht.

**Auswirkung:** Schwerpunktsetzung und Kapitelstruktur, besonders Theorie/Analyse; Zählung, interne Verweise und Verzeichnisse danach erneut prüfen. Studiendaten nicht kürzen oder verändern.

**Autorenentscheidung:** Unbedingt nötig: Ausnahme vorhanden? Welche Erklärungen bleiben im Haupttext, welche technischen Details gehen in den Anhang? Kein Text wurde automatisch gekürzt.

### R-003 – Zwei Indexquellen verweisen auf unmögliche Seiten im falschen Kommer-Buch

**Priorität/Status:** P1 · BESTÄTIGT.

**Datei/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\notebooks\Theorie.ipynb`; 3.1.1.1 Indexfonds und ETFs; Markdown-Zelle `1941d2df`, erste zwei Absätze.

**Originalauszug:** `[@kommerLeichteEinstiegWelt2025, S. 464-465]` und `[@kommerLeichteEinstiegWelt2025, S. 465]`.

**Problem:** Der referenzierte Titel „Der leichte Einstieg in die Welt der ETFs“ hat in der vorliegenden 2. Auflage 192 Seiten; die genannten Seiten existieren dort nicht. Die Aussagen passen dagegen zu „Souverän investieren mit Indexfonds und ETFs“, Abschnitt 9.2.

**Prüfnachweis:** Original-EPUB `MZ4YACD4`: OPF nennt `192 pages`. Original-PDF `A8Q9SBUT`: Datei-Seiten 464–465 vollständig gelesen; Abschnitt 9.2 erklärt Indexfunktion, Referenzindex, Gewichtung und regelmässige Auswahlprüfung. Es handelt sich um eine falsche Werkzuordnung, nicht nur einen ungenauen Seitenanker.

**Kleinste Korrektur:** Nur diese zwei Verweise auf den bereits vorhandenen Key `kommerSouveraenInvestierenMit2025`, vorzugsweise Abschnitt 9.2, umstellen. Druckseiten erst nach Abgleich der tatsächlich verwendeten Ausgabe nennen. Die korrekten Starterbuch-Verweise auf Kapitel 1 nicht pauschal ersetzen.

**Auswirkung:** Quellen im Theoriekapitel; keine Rechnung. Das Starterbuch bleibt wegen anderer Zitationen im Literaturverzeichnis.

**Autorenentscheidung:** Tatsächlich verwendete Ausgabe/Paginierung bestätigen; die falsche Zuordnung ist unabhängig davon belegt.

### R-004 – 60/40-Periodenformel nennt Zielgewichte statt ihrer notwendigen Anfangsbedingung

**Priorität/Status:** P1 · BESTÄTIGT als fehlende Bedingung; kein nachgewiesener Engine-Fehler.

**Datei/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\notebooks\Theorie.ipynb`; 3.1.5.1; Zelle `990d4cd6`.

**Originalauszug:** `r_(60/40,t)=0,60 r_(Aktien,t)+0,40 r_(Anleihen,t)`; „0,60 und 0,40 sind ihre Zielgewichte.“

**Problem:** Die Formel gilt für eine einzelne Periode nur bei tatsächlichen Periodenanfangsgewichten 60/40. Bei jährlichem Rebalancing driften die Gewichte in den dazwischenliegenden Monaten. Der folgende Driftabsatz ist richtig, verbindet diese Drift aber nicht ausdrücklich mit der Gültigkeitsbedingung der Formel.

**Prüfnachweis:** Start 60/40; erste Periode Aktien +100 %, Anleihen 0 %: Werte 120/40, Gesamtwert 160, neue Gewichte 75/25. Zweite Periode Aktien −50 %, Anleihen 0 %: tatsächliche Portfoliorendite = −37,5 %, starre Formel = −30 %. Allgemein `r_(P,t)=Σ_i w_(i,t−1) r_(i,t)` für die gehaltenen Anfangsgewichte. Die Engine-/Exportlogik lässt diese Gewichte korrekt driften und rebalanciert jährlich.

**Kleinste Korrektur:** Einen Bedingungssatz direkt vor/nach der bestehenden Formel ergänzen und tatsächliche Anfangsgewichte für die allgemeine Formel definieren. Rebalancing-Regel nicht verändern.

**Auswirkung:** Verbindung Theorie–Methodik–Analyse wird eindeutiger; reale Ergebnisse bleiben gültig innerhalb der geprüften Exportgrenzen.

**Autorenentscheidung:** Keine neue Strategieentscheidung nötig; nur Präzisierung der Erklärung in einem späteren Korrekturlauf.

### R-005 – Lokale Referenzfunktion Drawdown verliert einen anfänglichen Verlust

**Priorität/Status:** P1 · BESTÄTIGT für diese Hilfsdatei; eingefrorene Engine und aktuelles Theorie-Notebook sind davon abzugrenzen.

**Datei/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\src\funktionen.py`; Funktionen `drawdown()` und `maximum_drawdown()`.

**Originalauszug:** `bisheriger_hoechststand = vermoegen.cummax()` nach `vermoegen = (1 + renditen).cumprod()`.

**Problem:** Der Ausgangswert 1 fehlt als untere Grenze des bisherigen Höchststands. Ist bereits die erste Rendite negativ, wird dieser Verlust nicht vollständig gegenüber dem Startvermögen gemessen.

**Prüfnachweis:** Renditen `[-0.10, 0.0]`: Vermögensfaktoren `[0.9, 0.9]`; aktuelles `cummax` = `[0.9, 0.9]`; Funktion liefert `[0, 0]` und MDD 0 %. Mit Ausgangswert 1 muss beides −10 % sein. Theorie-Notebook und eingefrorener Engine-Commit verwenden bereits `.clip(lower=1.0)`; die tatsächlichen Export-MDDs wurden einschliesslich Ausgangswert unabhängig bestätigt.

**Kleinste Korrektur:** In einem späteren autorisierten Lauf diese veraltete Referenzfunktion mit der bereits erklärten Ausgangswertkonvention abgleichen oder die Datei ausdrücklich als historisch markieren. Mindestens anfänglichen Verlust und späteren neuen Höchststand gezielt prüfen.

**Auswirkung:** Zukünftige Verwendung dieser Hilfsdatei könnte falsche MDDs erzeugen. Kein Beleg, dass die fünf Studienläufe diese alte Fassung nutzten; ihre Manifest-/Codebelege weisen auf die richtige Engine-Fassung.

**Autorenentscheidung:** Soll `src/funktionen.py` eine aktuelle wiederverwendbare Referenz bleiben oder als historische Sammlung gelten? Keine Änderung an der eingefrorenen Engine nötig.

### R-006 – QuantStats-Tabellenzeiten werden als vollständige Erholungsdauer erklärt

**Priorität/Status:** P1 · BESTÄTIGT für die Interpretation der vorhandenen Ausgabe.

**Datei/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\notebooks\Theorie.ipynb`; 3.2.4.2 Erholungsdauer; Zellen `d501a004`, `83fd3049`, `d606f0f5` und gespeicherte Tabelle.

**Originalauszug:** „Zeit vom früheren Höchststand, bis dieser Wert vollständig wieder erreicht wird“; Ausgabeüberschrift `Erholungsphasen`; erste Zeile `start 2024-02-29`, `end 2024-03-31`, `days 32`.

**Problem:** Die eigene Definition ist richtig. Die ausgegebenen `start/end/days` messen in diesem Beispiel jedoch den beobachteten Unterwasserabschnitt, nicht die gesamte Zeit vom vorherigen Peak zur tatsächlichen Wiedererreichung. Die letzte Tabellenepisode ist am Datenende noch offen.

**Prüfnachweis:** Vermögen erreicht den Peak am 31.01.2024, liegt im Februar/März darunter und erreicht/überschreitet ihn am 30.04.2024. Peak→Erholung dauert **90 Kalendertage**. Die 32 Tage entsprechen 29.02.→31.03. inklusive beider Beobachtungstage. Der Dezember-Drawdown ist noch −2,4054 %; `end 2024-12-31` ist deshalb kein Erholungstag. Ohne lokal gepinnte QuantStats-Version wird keine Aussage gemacht, dass alle heutigen Versionen genau diese Tabellenkonvention hätten.

**Kleinste Korrektur:** Output als Drawdown-Episoden bezeichnen, Spaltenkonvention und offenen Endfall erklären. Falls die eigene Peak→Recovery-Kennzahl benötigt wird, diese getrennt definieren und gezielt berechnen; gespeicherte 32 nicht einfach in 90 umetikettieren.

**Auswirkung:** Theorieverständnis von Verlustdauer; reale Studie berichtet MDD, keine falsch übertragene Recovery-Zahl nachgewiesen.

**Autorenentscheidung:** Reicht die verständlich erklärte Episodentabelle oder soll zusätzlich eine explizite Recovery-Kennzahl dargestellt werden? Kein Paketwechsel oder Blind-Neurendern dieser Phase.

### R-007 – S&P 500 ist nicht automatisch die Rangliste der 500 grössten US-Unternehmen

**Priorität/Status:** P1 · BESTÄTIGT.

**Datei/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\notebooks\Theorie.ipynb`; 3.1.1.1; Zelle `1941d2df`.

**Originalauszug:** „Der S&P 500 umfasst beispielsweise die 500 grössten Unternehmen der USA.“

**Problem/Beleg:** Das ist eine falsche Vereinfachung der Indexauswahl. Der Anbieter beschreibt 500 führende grosse US-Unternehmen mit weiteren Auswahlkriterien, etwa Gewinnfähigkeit, Liquidität und Streubesitz. Eine blosse Sortierung aller Unternehmen nach Grösse ist nicht die Regel. Originalquelle: [S&P Dow Jones Indices, The 500](https://www.spglobal.com/spdji/en/landing/investment-themes/the-500/).

**Kleinste Korrektur:** „500 führende grosse US-Unternehmen, die die Auswahlkriterien des Index erfüllen“; passenden Anbieterbeleg hinzufügen. Keine unnötige Liste sämtlicher Indexregeln im Haupttext.

**Auswirkung:** Verdeutlicht die nachfolgende richtige Erklärung des Regelwerks; keine Änderung der untersuchten ETF-Reihen.

**Autorenentscheidung:** Keine neue Finanzannahme; Wortlaut/Beleg im späteren Korrekturlauf bestätigen.

### R-008 – Historische KI-Programmierung und Datenaufbereitung fehlen im aktuellen Gesamtlog

**Priorität/Status:** P1 · BESTÄTIGT für die Dokumentationslücke; keine Behauptung absichtlicher Verheimlichung.

**Dateien/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\documentation\ai-usage\ai-usage-log.md` und `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\ki-nutzung.qmd`; aktuelle Gesamtdokumentation. Historischer Beleg: Git-Commit `1954bfbcb257b51e7f9174aa824cb35e437de752`, Pfad `documentation/ai-usage/ai-usage-log.md`.

**Originalauszug:** Anhang: „vor allem für technische Einrichtung, Strukturierung, Übertragung bereits vorhandener Inhalte und sprachliche Unterstützung“. Analyse 5.9 nennt dagegen die KI-gestützte technische Zusammenstellung der Engine.

**Problem:** Der aktuelle Log enthält nicht die 14 konkreten Oktober-Einträge aus dem verfügbaren Engine-/Studienreferenzstand. Die allgemeine Zusammenfassung reicht für den tatsächlichen Anteil an Implementierung, Tests, Adapter und Freeze nicht aus. Hinweise in Analyse/Methodik ersetzen diesen strukturierten Nachweis nicht vollständig.

**Prüfnachweis:** Historisch dokumentiert, im aktuellen Log fehlend: 02.10. Engine-Audit; 03.10. Core-Implementierung; 04.10. Multi-Asset/Rebalancing, SMA-Trend, BIP-Gewichtung, finaler Audit, EB-01–03-Fixes, Portfoliozustands-Fix, Blocker-Re-Audit, CSV-NUL-Fix, finaler Freeze-Re-Audit und Release/Freeze; 10.10. Datenadapter sowie finale Autorenfreigabe/Config-/Studien-Freeze-Vorbereitung. Die Originaleinträge enthalten Zweck, Umfang, Übernahme und Prüfgrenzen; die referenzierten Promptdateien sind in diesem Git-Stand vorhanden. Historische Prüfungen dürfen nicht als hier erneut ausgeführt bezeichnet werden.

**Kleinste Korrektur:** Später belegte historische Einträge samt Originalprompt-Verweisen datentreu in den Gesamtnachweis übernehmen und im Buchanhang verständlich bündeln. Autorenentscheidungen über Strategien/Freeze von der KI-Implementierung trennen; tatsächliche manuelle Freigaben nur so weit behaupten, wie belegt. Keine Gesprächsverläufe oder fehlenden Backtest-Aufträge erfinden.

**Auswirkung:** KI-Anhang, Log und Erklärung der Werkzeugentwicklung. Keine Änderung der Fachresultate; die bisherige Anerkennung der ChatGPT-Formulierungen bleibt erhalten.

**Autorenentscheidung:** Historische Übernahmen/Kontrollen prüfen und ergänzen; weitere nicht in diesen 14 Einträgen belegte Einsätze gegebenenfalls anhand vorhandener Originalnachweise rekonstruieren. In dieser Phase wurde nur die Lücke berichtet, kein historischer Log umgeschrieben.

### R-009 – `to_datetime`-Beleg zeigt auf den Kapitelanfang statt die Funktion

**Priorität/Status:** P2 · BESTÄTIGT für den vorliegenden PDF-Locator; Druckseitenzuordnung offen.

**Datei/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\notebooks\Theorie.ipynb`; Datumskonvertierungsbeispiel 3.2.1; Zelle `7e670f16`.

**Originalauszug:** „Quelle zur Nutzung von to_datetime() [@mckinneyPythonDataAnalysis2022, S. 511].“

**Problem/Beleg:** Im vorhandenen Original-PDF `PJA9S9HY` beginnt auf Datei-Seite 511 lediglich Kapitel 11 „Time Series“. Die konkrete `pandas.to_datetime`-Erklärung mit Beispielen steht auf Datei-Seite 516. Beide Seiten vollständig gelesen. Kein Fehler in der Funktion selbst.

**Kleinste Korrektur:** Verweis auf Kapitel 11, Unterabschnitt „Converting Between String and Datetime“ präzisieren oder die in der tatsächlich verwendeten Ausgabe kontrollierte Druckseite nennen. Nicht ungeprüft „516“ als gedruckte Buchseite einsetzen.

**Auswirkung:** Nur Nachvollziehbarkeit des Quellenlocators.

**Autorenentscheidung:** Benutzte Ausgabe und Seitenzählung bestätigen.

### R-010 – Gleiches arithmetisches Monatsmittel wird als „gleiche Rendite“ bezeichnet

**Priorität/Status:** P2 · BESTÄTIGT als Mehrdeutigkeit.

**Datei/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\notebooks\Theorie.ipynb`; 3.2.3.6; Plotzelle `c09ff8c4`, Erläuterung `5a028097`.

**Originalauszug:** „wie ein Kurs bei gleicher Rendite eine ganz unterschiedliche Volatilität aufweisen kann“.

**Problem/Beleg:** Beide Beispiele haben 1 % arithmetisches Monatsmittel, aber unterschiedliche aufmultiplizierte Jahresrenditen. Separate Multiplikation der vorliegenden zwölf Faktoren ergibt A **12,6791 %**, B **11,6805 %**. Der vorhandene Plottitel „Ähnliche Durchschnittsrendite“ ist angemessen; der nachfolgende Satz ist ungenau.

**Kleinste Korrektur:** „bei gleichem arithmetischem Mittel der Monatsrenditen“ statt „bei gleicher Rendite“. Keine Änderung der Illustration oder Beispieldaten.

**Auswirkung:** Schärft die Verbindung zum vorher erklärten geometrischen Mittel.

**Autorenentscheidung:** Keine neue Rechnungsauswahl nötig.

### R-011 – Historische pandas-Frequenzaliase sind als aktuelle Übersicht missverständlich

**Priorität/Status:** P2 · BESTÄTIGT als fehlender Versionskontext, nicht als Fehler der eingefrorenen Engine.

**Datei/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\notebooks\Theorie.ipynb`; 3.2.1.2 Frequenzen; Zelle `005fce46`.

**Originalauszug:** Alias-Tabelle unter anderem `M`, `BM`, `Q`, `BQ`, `A`, `BA`; Beleg Hilpisch 2019, S. 191–192.

**Problem/Beleg:** Diese historische Liste ist korrekt aus dem älteren Kontext, kann aber nicht ohne Versionsangabe als heute ausführbare pandas-Übersicht gelten. pandas 3.0 entfernt unter anderem alte Endaliase zugunsten `ME`, `BME`, `QE`, `BQE`, `YE`, `BYE`. Originalnachweis: [pandas 3.0 Release Notes](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html), Abschnitt zu entfernten Frequenzaliasen. Die Studienmanifeste halten pandas 2.3.3 fest und die Configs verwenden bereits `ME`.

**Kleinste Korrektur:** Tabelle ausdrücklich „historische Aliasübersicht nach Hilpisch 2019“ nennen und für die verwendeten Frequenzen aktuelle Schreibweise/Version ergänzen; alternativ auf die tatsächlich benötigten Aliase reduzieren. Keine pauschale Paketaktualisierung.

**Auswirkung:** Verständlichkeit und spätere Ausführbarkeit der Beispiele; kein Nachweis eines kaputten Studienlaufs.

**Autorenentscheidung:** Historische Liste mit Hinweis behalten oder didaktisch verkürzen.

### R-012 – Stand der manuellen Autorenkontrolle ist nicht eindeutig abgegrenzt

**Priorität/Status:** P2 · BESTÄTIGT als Dokumentationsmehrdeutigkeit.

**Datei/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\ki-nutzung.qmd`; Einleitung, Abschnitt „Erstellung der KI-Nutzungsdokumentation“ und spätere datierte Nachträge; entsprechender aktueller Log.

**Originalauszug:** „Der Autor hat diese Dokumentation gelesen und inhaltlich überprüft“; spätere Einsätze: „Autorenkontrolle ausstehend.“

**Problem/Beleg:** Die erste undatierte Aussage kann auf den gesamten aktuellen Anhang bezogen werden, obwohl spätere Teile ausdrücklich noch nicht geprüft sind. Belegt ist der unklare Geltungsbereich; es ist **nicht** belegt, dass der Autor nie gelesen oder falsch ausgesagt hätte.

**Kleinste Korrektur:** Geprüften Stand datieren und dessen Umfang nennen; neuere Nachträge bis zur tatsächlichen Kontrolle als ausstehend kennzeichnen. Kein vergangenes Prüfergebnis eigenmächtig widerrufen und keine neue manuelle Freigabe behaupten.

**Auswirkung:** Vertrauen in den KI-Nachweis und klarere Trennung von KI-Prüfung/Autorenverantwortung.

**Autorenentscheidung:** Autor muss bestätigen, welche Fassung beziehungsweise Einsätze er tatsächlich kontrolliert hat.

### R-013 – Absatz zur eingefrorenen Gegenrechnung steht zweimal unmittelbar hintereinander

**Priorität/Status:** P2 · BESTÄTIGT.

**Datei/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\notebooks\Analyse.ipynb`; 5.11 Abschluss der Studie; Zellen `a4355b5e` und `008ef22e`.

**Originalauszug:** „Anschliessend erfolgte eine zusätzliche KI-gestützte Gegenrechnung aus den eingefrorenen Eingaben und den Ergebnisdateien.“

**Problem/Beleg:** Der gesamte folgende Absatz ist zweimal identisch, einmal in `<p>` und einmal als Markdown. Das ist eine direkte Textdoppelung, keine zusätzliche unabhängige Prüfung.

**Kleinste Korrektur:** Eine der beiden Zellen entfernen; die andere unverändert behalten.

**Auswirkung:** Kein Informationsverlust, leicht geringerer Umfang; Zellbestand/Verweise später kontrollieren.

**Autorenentscheidung:** Keine inhaltliche Auswahl nötig; bestätigen, welche formale Zellfassung erhalten bleiben soll.

### R-014 – Überblick beschreibt noch das frühere QMD-Gerüst und künftige Ergebnisse

**Priorität/Status:** P2 · BESTÄTIGT.

**Datei/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\index.ipynb`; Projektbeschreibung/Quellen/Notebook-Nutzung/Verzeichnisstruktur; Zellen `3533c085`, `ae9ec038`, `e0eaae76`, `6b75ab19`.

**Originalauszug:** „spätere Ergebnisse in `outputs/`“; „Übertrage nur die relevanten, geprüften Ergebnisse in die `.qmd`-Kapitel“; Struktur enthält `index.qmd`, `einleitung.qmd`, `theorie.qmd`, `methodik.qmd`, `fazit.qmd`.

**Problem/Beleg:** Tatsächliche Buchkonfiguration und vorhandene Dateien verwenden sechs `.ipynb`-Kapitel; die eingefrorenen Exporte liegen unter `results/study_v1/`. Die Beschreibung ist nach der inhaltlich unveränderten Übertragung aus der README historisch stehen geblieben.

**Kleinste Korrektur:** Nur konkrete Kapitel-/Ergebnispfade und überholte Zukunftsformulierungen an den aktuellen Stand anpassen; Arbeitsanleitungen auf die wirklich verwendete Notebook-Form beziehen. Die allgemeine Möglichkeit weiterer QMD-Dateien ist weiterhin gültig und muss nicht verboten werden.

**Auswirkung:** Überblick/README-Synchronisation. Eine spätere README-Änderung wäre separat zu autorisieren; dieser Audit hat sie nicht durchgeführt.

**Autorenentscheidung:** Soll die technische Projektanleitung im Hauptbuch bleiben? Ein Verschieben in den Anhang ist optional und könnte bei R-002 helfen.

### R-015 – Historisches Schweizer Inflationsmittel wird als jährliche Kaufkraftschwelle verallgemeinert

**Priorität/Status:** P1 · BESTÄTIGT für die Schlussfolgerung, nicht für den gerundeten historischen Mittelwert.

**Datei/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\notebooks\Theorie.ipynb`; 3.2.2.4 Nominal und real; Zelle `621f9b9a`.

**Originalauszug:** „durchschnittliche Inflation von 0.8% in der Schweiz“; „Das heisst, ein Investment muss jährlich mindestens 0.8% erzielen, damit die Kaufkraft erhalten bleibt.“

**Problem:** Aus einem historischen Zehnjahresdurchschnitt folgt kein fester Mindestwert für jedes einzelne oder zukünftige Jahr. Kaufkrafterhalt hängt von der tatsächlich relevanten Inflation derselben Periode/Währung ab.

**Prüfnachweis:** Gespeicherte Original-BFS-Seite: Jahreswerte 2016–2025 `−0.4, 0.5, 0.9, 0.4, −0.7, 0.6, 2.8, 2.1, 1.1, 0.2` Prozent. Arithmetisches Mittel = **0,75 %**, auf eine Dezimalstelle **0,8 %**; diese Zahl ist plausibel. Gegenbeispiel 2022: nominal 0,8 %, Inflation 2,8 % ⇒ reale Rendite `(1.008/1.028)−1 = −1,9455 %`. Der historische Mittelwert schützt also nicht in jedem Jahr die Kaufkraft.

**Kleinste Korrektur:** Konkreten historischen Zeitraum nennen und den zweiten Satz durch die Periodenbedingung ersetzen; beispielsweise reale Rendite `r_real=(1+r_nominal)/(1+π)−1`. Keine nachträgliche automatische CHF-Inflationsbereinigung der USD-Studie.

**Auswirkung:** Theoriegrundlage und Erklärung der nominalen Ergebnisgrenze. Methodik/Fazit behandeln diese Grenze bereits angemessen.

**Autorenentscheidung:** Keine Änderung der Studienwährung oder realen Ergebnisdefinition nötig; ein kurzer historischer Beispielsatz genügt.

### R-016 – Mehrere ausdrücklich geforderte Abgabeteile fehlen noch

**Priorität/Status:** P1 · BESTÄTIGT für den aktuellen Buchstand; zusammengefasster formaler Befund.

**Dateien/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\_quarto.yml`, alle Buchquellen; `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\documents\Leitfaden_MA_für_SuS_KBW_2026.pdf`, Datei-Seiten 4–5, 18 und 21; `Maturarbeit_Vorgaben_2027.pdf`, Datei-Seite 3.

**Originalauszug:** Aktuelle Konfiguration `title`, `author`, `date: today`; vorhandener KI-Anhang, aber keine Abstract-/Eigenständigkeitserklärungsquelle und keine Abbildungs-/Tabellenverzeichnisse.

**Problem/Beleg:** Die Schule fordert auf der Titelseite zusätzlich Schulname, Kennzeichnung als Maturitätsarbeit, Klasse, Betreuungsperson und Abgabedatum. `today` ist ein Renderdatum und kein festes Abgabedatum. Abstract direkt nach Titelseite vor Inhaltsverzeichnis, höchstens eine Seite; getrennte elektronisch einzureichende Kurzfassung höchstens 700 Zeichen inkl. Leerzeichen. Abbildungen und Tabellen sollen getrennt nummeriert/verzeichnet sein. Einige Theorie-Tabellen (z. B. Aliasliste `005fce46`) und die Theorieillustration haben noch keine entsprechende automatisch nutzbare Beschriftung. Die unterzeichnete Eigenständigkeitserklärung soll am Ende stehen und sämtliche Hilfsmittel einschliesslich KI berücksichtigen. Diese Teile fehlen im gegenwärtigen Entwurf; Phase 1 hatte sie bewusst offen gelassen.

**Kleinste Korrektur:** Fehlende Front-/Endteile und eindeutige Beschriftungen ergänzen, nachdem der Autor die Inhalte/Angaben geliefert und den Umfangsplan entschieden hat. Die vorhandene Literaturverzeichnisposition vor dem KI-Anhang beibehalten; Unterschrift nicht durch KI fingieren.

**Auswirkung:** Buchreihenfolge, Seitennummerierung, Inhalts-/Abbildungs-/Tabellenverzeichnisse, Titelmetadaten und finaler Export.

**Autorenentscheidung:** Aktuelle Klasse, Betreuung, verbindliches Abgabedatum, Abstractfassung und Erklärung prüfen; eigenhändig unterschreiben. Die ältere Vereinbarung ersetzt diese Angaben nicht automatisch. Vollständige Checkliste in E.

### R-017 – Originaleingaben fehlen für eine vollständige unabhängige Daten-/Sharpe-Prüfung

**Priorität/Status:** P1 · NICHT VERIFIZIERBAR. Nachgewiesen ist die fehlende Zugänglichkeit; ein Fehler in den Daten oder Ergebnissen ist damit nicht bewiesen.

**Dateien/Stelle:** `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\results\study_v1\` mit allen fünf `run_manifest.json`; dortige `input_files`. Dokumentierter Archivort: `C:\Users\modic\Documents\GitHub\Maturarbeit_Engine\data\study_v1\archive\study-freeze-v1\`.

**Originalauszug:** H1-Manifest verweist auf `processed/main_market.csv`, `assets.csv`, `macro_g7.csv`, `rf_main.csv`; Z1 entsprechend `us_market.csv`/`rf_us.csv`, jeweils mit SHA-256.

**Problem/Beleg:** Das genannte Engine-Verzeichnis und die eingefrorenen Eingangsdateien sind hier nicht vorhanden. Der historische Freeze-Nachweis beschreibt 123 Archivdateien als lokale/externe Sicherung ausserhalb der Git-Versionierung. Im verfügbaren Git sind Code/Configs/Nachweise, aber nicht diese Raw-/Processed-Snapshots. Damit lassen sich nicht alle echten Sharpe-Werte, alle FRED-Transformationen und alle WEO/Yahoo-Originalbeobachtungen unabhängig nachvollziehen. Das ist eine konkrete Reproduzierbarkeitslücke dieser Prüfung, keine Feststellung dauerhaften Datenverlusts.

**Kleinste ausreichende Massnahme:** Vorhandenes versiegeltes Archiv aus der bestehenden Sicherung zugänglich machen und Dateien zuerst gegen die erwarteten Hashes prüfen. Dann gezielte nur lesende Nachprüfung von Rf-Alignment/Sharpe, BIP-Vintages und Markt-/SMA-Eingaben. Keine neuen Downloads, keine Ersatzdaten, keine neuen Backtests.

**Auswirkung:** Reichweite der fachlichen Freigabe und Reproduzierbarkeit. Exportrechnungen sowie bisherige historische Prüfberichte bleiben vorhandene Belege, ersetzen aber nicht die fehlende unabhängige Eingangsprüfung.

**Autorenentscheidung:** Bestehenden Archiv-/Backupstand finden und für einen späteren separaten Prüflauf bereitstellen; weder Datenfehler noch neue Studienfreigabe aus diesem Bericht ableiten.

## D. Offene Prüfungen

Diese Liste beschreibt Nachweise und Entscheidungen; sie erzeugt keine zusätzlichen gezählten Fehler. Unzugängliche Belege wurden nicht als gesicherte Fachfehler gewertet.

1. **Versiegelte Raw-/Processed-Daten (R-017):** Das bereits vorhandene Archiv suchen; erwartete Datei-/Manifest-Hashes verwenden. Nach Zugriff alle realen Sharpe-/Halbperioden-Sharpe-Werte aus zeitlich passenden Rf- und Portfolio-Renditen unabhängig prüfen; 468 dokumentierte Rf-Monatsbeobachtungen und Verzögerungs-/ACT365-Regel gegen die ursprünglichen Tageswerte prüfen.
2. **WEO-Vintages/Marktinputs (R-017):** Alle verwendeten NGDPD-Zellen, `actual`/Schätzungsgrenzen, Veröffentlichungstage und den gemeinsamen verfügbaren Datenjahrgang aus den archivierten Quellen nachweisen. Qualitäts- und Gewichtsexporte bestätigen innere Konsistenz, nicht die Originalquelle. Die dokumentierten 4’087 makroökonomischen Versionseinträge wurden hier nicht aus Raw-Dateien rekonstruiert. Yahoo-Split-/Dividendenereignisse, alle SMA-Werte und die reinen Einzel-Länder-CAGRs (unter anderem USA 13,78 % versus übrige Länder etwa 5,28–6,81 %) sind ohne Marktinput nicht vollständig unabhängig prüfbar.
3. **Ausgaben/Paginierung:** Bei konvertierten E-Book-PDFs tatsächliche Druckseiten mit der vom Autor verwendeten Ausgabe vergleichen. R-003 ist bereits als falsches Werk bestätigt; R-009 als falscher PDF-Locator. Andere identifizierte Themenstellen sind keine pauschale Bestätigung jedes präzisen Seitenverweises. Starterbuch 58–60 im EPUB nicht als exakt seitenverifiziert ausgeben.
4. **Historische Fondsdetails:** Vollständige frühere Benchmarkwechsel, Indexregeln und Zusammensetzungen wurden nicht über sämtliche Studienjahre rekonstruiert. Die aktuellen Originalanbieter-Seiten bestätigen Instrumentrollen; sie beweisen keine unveränderte historische Fondsdefinition. Die Arbeit benennt ETFs ohnehin als Proxys und Indexwechsel als Grenze.
5. **Historische KI-Nutzung (R-008/R-012):** Die 14 vorhandenen Originaleinträge zusammenführen; zusätzliche Einsätze zur Durchführung/Prüfung der echten Studie nur anhand vorhandener Originalnachweise ergänzen. Datum/Umfang der tatsächlichen Autorenkontrolle bestätigen. Nicht sämtliche historischen Prompts oder Gesprächsverläufe wurden neu vollständig gelesen.
6. **KI als Quelle versus Hilfsmittel:** Der Leitfaden verlangt bei inhaltlicher Quellenverwendung öffentlich zugängliche Abfragelinks und Quellenangabe. Die belegte ChatGPT-Erklärungs-/Formulierungsarbeit zum Lehrerfeedback ist genannt; der ursprüngliche öffentliche Gesprächslink liegt hier nicht vor. Autor/Betreuung sollen klären, ob diese Übernahme nach Schulregel als Inhaltquelle mit Internetzitation gilt oder als deklarierte Formulierungshilfe. Das betrifft nicht automatisch jede Formatierungs-/Programmierhilfe. Kein Link/Prompt wird erfunden und keine pauschale Plagiatsbehauptung erhoben.
7. **Umfang/Abgabefassung (R-002/R-016):** Allfällige Ausnahme, Anhangsbehandlung, endgültige Forschungsfrage, aktuelle Titelseitenangaben, Abstract und Unterschrift mit Betreuung klären. Die unverändert richtige aktuelle Forschungsfrage in Einleitung/Fazit ist davon getrennt zu beurteilen.
8. **QuantStats-Beispiel (R-006):** Falls es später neu ausgeführt werden soll, verwendete Version dokumentieren und Spaltenkonvention prüfen. Keine neue Bibliothek installieren, nur um eine historische Ausgabe als vermeintlich aktuell zu reproduzieren.

## E. Formale Abgabe-Checkliste

Grundlagen: [Leitfaden 2026](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/documents/Leitfaden_MA_für_SuS_KBW_2026.pdf), besonders Datei-Seiten 4–5 (gedruckt 2–3), 18 (gedruckt 16), 21 (gedruckt 19); [Vorgaben 2027](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/documents/Maturarbeit_Vorgaben_2027.pdf), Datei-Seiten 1 und 3; visuell gelesene [Vereinbarung](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/documents/Matura_Vereinbarung_Riccardo_2027.pdf). Persönliche Vertragsdetails sind nicht in diesen Bericht kopiert.

| Bestandteil | Stand | Nachweis/noch erforderlicher Schritt |
|:---|:---|:---|
| Titel und Autor | Vorhanden | Buchmetadaten; Titel passt zum Thema |
| Vollständige Titelseite | Offen, R-016 | Schule, Maturitätsarbeit, Klasse, Betreuung und festes Abgabedatum ergänzen; `today` reicht nicht |
| Abstract nach Titel/vor Inhaltsverzeichnis | Fehlt, R-016 | Höchstens eine Seite; Autor verfasst/prüft Kurzfassung |
| Elektronischer Abstract | Nicht vorhanden/nicht nachgewiesen | Separat höchstens 700 Zeichen inklusive Leerzeichen |
| Haupttextumfang 6’000–8’000 Wörter | Überschritten, R-002 | Zählung transparent dokumentiert; Ausnahme/Kürzungsplan entscheiden |
| Inhaltsverzeichnis und Kapitelhierarchie | Vorhanden | Automatische Nummern; bis vier Ebenen im Theoriekapitel nachvollziehbar, Phase-1-Nachweis gelesen |
| Haupttext mit arabischer Seitenzählung | Technisch eingerichtet | Phase 1 PDF/Word geprüft; nach Frontmatter-Ergänzungen erneut kontrollieren |
| Serifenschrift/Schriftgrad/Zeilenabstand | Technisch erfüllt | PDF/Word 11 pt und 1,2; keine neue ästhetische Umgestaltung nötig |
| Abbildungen/Tabellen getrennt nummeriert | Teilweise vorhanden | Einzelne Theorieobjekte noch ohne formale Beschriftung; keine automatische Neunummerierung in diesem Audit |
| Abbildungs-/Tabellenverzeichnis | Fehlt, R-016 | Aus vollständigen Beschriftungen generieren und gegen tatsächliche Objekte prüfen |
| Literaturverzeichnis alphabetisch, nur zitierte Werke | Vorhanden nach Phase-1-Ausgabenachweis | 29 aktive Keys auflösbar; zwei konkrete Quellenlocator korrigieren R-003/R-009 |
| Literaturverzeichnis vor Anhängen | Erfüllt | `bibliography.qmd` vor `ki-nutzung.qmd` in Buchkonfiguration |
| KI-Nutzung nach Literaturverzeichnis | Vorhanden, inhaltlich unvollständig | R-008/R-012, gegebenenfalls Quellenlink nach D.6 ergänzen |
| Eigenständigkeitserklärung am Ende | Fehlt, R-016 | Aktuelle Schulvorlage übernehmen, Hilfsmittel einschliesslich KI korrekt nennen, Autor unterschreibt |
| Finale PDF-Abgabe | Noch ausstehend | Technische Phase-1-PDF ist keine vollständige endgültige Abgabefassung |
| Gebundene Exemplare | Nicht aus dem Repository prüfbar | Vorgaben: zwei Abgabeexemplare und ein eigenes Exemplar vorbereiten |
| Schlusskontrolle/Autorenverantwortung | Ausstehend | Dieser Review ist keine Schul-/Autorenfreigabe |

Persönliche Ich-Formulierungen wurden nicht pauschal als Fehler markiert. Der Leitfaden empfiehlt überwiegend sachlich/unpersönlich zu schreiben; Motivation und eigene Entscheidungen können dennoch transparent persönlich formuliert sein. Eine generische Stilglättung ist weder erforderlich noch ausgeführt.

## F. Korrekturplan für einen späteren Auftrag – hier nicht ausgeführt

### 1. Zuerst vom Autor entscheiden lassen

- R-002: Umfangsregel/Ausnahme und inhaltliche Prioritäten. Möglicher Orientierungsrahmen nach Zustimmung: Einleitung 600–800, Theorie 1’600–2’000, Methodik 900–1’100, Analyse 2’400–3’000, Fazit 700–900 Wörter = etwa 6’200–7’800. Das ist ein Vorschlag, keine bereits angenommene Vorgabe. Detaillierte technische Architektur, lange Implementierungs-/Schemaschilderungen und ausführliche Codeerläuterungen könnten in einen Anhang; die wissenschaftlichen Vergleichsbedingungen, Ergebnisbelege und Grenzen müssen im Haupttext bleiben.
- R-016: Titelseitenangaben, Abgabedatum, Abstract-/Kurzabstractfassung, Erklärung und Unterschrift.
- R-008/R-012: Historische Kontrollen/Übernahmen und Dokumentationsstand bestätigen; Originaleinträge vollständig und ohne erfundene Freigaben zusammenführen.
- R-005/R-006/R-011/R-014: Rolle der lokalen Hilfsdatei, Bedarf an eigenständiger Recovery-Kennzahl, Umfang der Aliasliste und Platz der technischen Projektanleitung entscheiden.
- R-017/D: Vorhandenes Archiv zugänglich machen und Umfang eines separaten nur lesenden Eingangsprüflaufs freigeben. Fehlende Daten nicht durch neue Beschaffung ersetzen.

### 2. Danach eindeutig behebbare bestätigte Punkte gezielt korrigieren

R-001: isoliertes Portfolio-Beispiel und gespeicherte Ausgabe korrekt aktualisieren. R-003: zwei falsche Werkzuordnungen ändern. R-004: gültige Anfangsgewichte explizit erklären. R-007: S&P-Auswahlbeschreibung präzisieren. R-009: überprüften Ausgabe-/Kapitelbeleg setzen. R-010: arithmetisches Monatsmittel ausdrücklich nennen. R-013: einen identischen Absatz entfernen. R-015: historischen Inflationsdurchschnitt von tatsächlicher jährlicher Kaufkraftschwelle trennen. R-005/R-006/R-011/R-014 erst in der vom Autor gewählten Variante ausführen. Schulfrontmatter und Kürzungen nach abgestimmtem Plan, nicht nebenbei.

Das eingefrorene Studienmodell, die echten Ergebnisdateien, die ursprünglichen Parameter und die Engine bleiben auch bei diesen Textkorrekturen getrennt geschützt. Ein späterer notwendiger Fachwechsel wäre ein eigener ausdrücklicher Auftrag und darf nicht als blosse Formatierung deklariert werden.

### 3. Rein optionale Änderungen

Kurzer Warm-up-Hinweis beim SMA-Spielzeugbeispiel; technische Projektanleitung aus dem Haupttext verlagern; einzelne Übergänge nach den vom Autor gewählten Kürzungen verbessern. Kein pauschales Umschreiben des persönlichen sachlichen Tons, keine Mindestzahl stilistischer Eingriffe, keine Umschreibung zur Umgehung von Textähnlichkeitssystemen.

### 4. Nach jeder tatsächlichen Korrektur angemessen prüfen

- Notebook-Schema, Zell-IDs/Referenzen und Output-Provenienz bei betroffenen Zellen prüfen; R-001 darf nicht nur kosmetisch als angeblich neu ausgeführt etikettiert werden.
- Für R-005 Gegenfälle Anfangsverlust/späterer Peak/Erholung; für R-004 Gewichtsdrift-Beispiel; für R-006 Peak-/Unterwasser-/offene Episode getrennt prüfen. Keine Tests schreiben, die nur den Satzbau spiegeln.
- Citation Keys und ausgewählte Originalbelege erneut kontrollieren; Wortzählung mit derselben dokumentierten Methode wiederholen.
- Nach Struktur-/Frontmatter-Änderungen Nummern, interne Verweise, Verzeichnisse und HTML/PDF/DOCX-Darstellung ohne neue Hauptläufe prüfen. Für eine reine KI-Anhangsänderung genügt die gezielte HTML-Buchprüfung; die Phase-1-Layoutprüfung wird hier nicht vollständig wiederholt.
- Originalergebnis-/Freeze-Hashes, tatsächlichen Git-Diff und Grenzen der KI-Dokumentation prüfen. Ein allfälliger Originaldaten-Prüflauf ersetzt keine vorhandenen Studienresultate.

## Abschluss, Integrität und Stopppunkt

Für diesen Einsatz wurden nur vier erlaubte Dateien angelegt beziehungsweise ergänzt:

- `documentation/gesamtgegenlesen-phase2-2026-10-12.md`: dieser neue Bericht.
- `documentation/ai-usage/prompts/2026-10-12-gesamtgegenlesen-phase2.txt`: byteidentische Promptkopie; SHA-256 `4b06668215ac20aebf143bbe1d3ce05267aa40328ca2980b3b30ff6c08696264`.
- `documentation/ai-usage/ai-usage-log.md`: genau eine neue Zeile am Ende; bisherige Bytes vollständig erhalten.
- `ki-nutzung.qmd`: kurzer neuer Abschnitt am Ende; bisherige Bytes vollständig erhalten.

Die sechs Notebooks, alle Quellen-/Fachdateien, Konfiguration, Engine-Referenzdatei, fünf Ergebnisordner und historischen Nachweise wurden gegen die externe Ausgangssicherung per SHA-256 geprüft. Von den 74 ursprünglich versionierten Dateien unterscheiden sich ausschliesslich die beiden erlaubten KI-Dateien durch die neuen Anhänge; die übrigen 72 sind byteidentisch. Alle 70 bereits vorhandenen Dateien unter `_book`, `_freeze` und `.quarto` sind ebenfalls byteidentisch; es wurden dort keine neuen Dateien erzeugt. Git-Index, HEAD und Branch bleiben unverändert. Git-Diff und unversionierte Ziele beschränken sich auf die vier genannten Dateien; nichts gestaged, kein Commit/Push/Pull/Checkout/Reset/Clean/Merge.

Der neue KI-Abschnitt wurde nach `KI-DOKUMENTATION-BUCH-SYNC` im Log und Buch abgeglichen. Das vollständige HTML-Buch wurde in einer externen minimalen Projektkopie mit deaktivierter Codeausführung/Freeze und `quarto render --to html --no-execute --no-cache` erfolgreich gerendert (Exit 0). Der neue Abschnitt steht als A.4 im KI-Anhang und in dessen Inhaltsverzeichnis; die Buchnavigation ist korrekt. 1’426 lokale HTML-Verweise wurden auf vorhandene Dateien/Zielanker geprüft, ohne ungültiges Ziel. PDF/DOCX wurden in dieser Phase nicht neu gerendert; der vorhandene Phase-1-Nachweis ist als historische Layoutprüfung ausgewiesen.

Ausgangshashes, isolierte Rechnungen und temporäre Darstellungen liegen ausschliesslich ausserhalb des Repositorys im Prüfverzeichnis `C:\Users\modic\AppData\Local\Temp\codex-phase2-2026-10-12-87ndti3q`. Sie ersetzen weder Studieninputs noch Ergebnisdateien. Alle wesentlichen Rechnungen und Beweisgrenzen sind in diesem Bericht selbst dokumentiert.

**STOPP zur gemeinsamen Durchsicht.** Kein fachlicher Korrekturplan wurde ausgeführt; der Autor hat diesen Bericht und die vorgeschlagenen Änderungen noch nicht freigegeben.
