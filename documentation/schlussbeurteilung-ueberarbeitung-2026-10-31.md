# Überarbeitung nach der ChatGPT Schlussbeurteilung vom 31. Oktober 2026

Die von ChatGPT gemeldeten Fundstellen wurden von Codex an den aktuellen Quellen untersucht und die bestätigten Text-, Beleg- und Formatmängel gezielt korrigiert. Die Originalbeurteilung stammt von ChatGPT; die anschliessenden Änderungen, Kontrollen und dieser Nachweis stammen von Codex. Eine persönliche Endkontrolle oder Abgabefreigabe durch den Autor wird nicht behauptet.

## Ausgangspunkt und Auftrag

- Öffentlicher Review-Chat: [ChatGPT – Prüfbericht Maturarbeit](https://chatgpt.com/share/6ae63fdb-e3b0-83eb-8465-345769041156), neuer Quellen-Key `chatgptSchlussbeurteilung20261031`, Kennzeichnung KI-46.
- Originaler 18-seitiger Prüfbericht und übermittelte Zusammenfassung sind unverändert unter `documentation/reviews/2026-10-31-chatgpt-pruefbericht.pdf` und `2026-10-31-chatgpt-schlussbeurteilung.txt` archiviert.
- Der ursprüngliche Überarbeitungsauftrag steht unter `documentation/ai-usage/prompts/2026-10-31-schlussbeurteilung-ueberarbeitung.txt`. Der Autor bestätigte zusätzlich Klasse **4gW** und reichte anschliessend die bereits ausgefüllte und sichtbar unterschriebene Ehrlichkeitserklärung nach.
- Der Bericht bezieht sich auf die 118-seitige Ausgangs-PDF mit SHA-256 `251173cc2473b6f870ca6861c5b7d1434437b304e0aca39361777cbb1710e937`; die lokale Ausgangs-PDF stimmt damit überein.
- Git-Ausgangsstand: `229166b485daa8c04a969d4a319d6eeb70da883f`, sauberer Arbeitsbaum. Keine Commits, Pushes oder Änderungen der Engine durchgeführt.

## Erledigung der Befunde

| Befund | Umsetzung und Grenze |
|---|---|
| A01 | Die nachgereichte Original-PDF mit Datum, sichtbarer Unterschrift und Mediothekswahl wurde bytegleich unter `assets/ehrlichkeitserklaerung-2026-27.pdf` bewahrt und als letzte Buchseite mit TOC-Eintrag eingebunden. Keine Unterschrift oder Mediotheksentscheidung von Codex erzeugt oder geändert. |
| A02 | PDF-Titelblatt ergänzt: Kantonsschule Büelrain Winterthur, Maturitätsarbeit, Klasse 4gW, Betreuung Jacques Mock. Titel, Autor, vorhandenes Datum und wortgetreuer Abstract erhalten. |
| A03 | Abbildungs- und Tabellenverzeichnis aktiviert und über KOMA `listof=totoc` ins Inhaltsverzeichnis aufgenommen. |
| A04 | 22 redaktionelle Tabellen mit echten Quarto-Captions und eindeutigen tbl-IDs sowie zugehörigen Textverweisen versehen; reine Codeausgaben bleiben Codeausgaben. Zeilendaten erhalten. |
| A05 | Synthetische Grafik mit fig-ID und Caption als eigene Darstellung gekennzeichnet; Verweise auf alle sieben Ergebnisgrafiken ergänzt. |
| A06 | 45 alte ChatGPT-Quellen über vorhandene Key/URL/Arbeitskontext-Matrix eindeutig mit KI-01 bis KI-45 redaktionell benannt. Keine Originalchattitel oder Abfragezeitpunkte erfunden. Historisches urldate 13.10.2026 bezeichnet weiter die Sicherung. Kurztitel bleiben auch bei Wiederholungsbelegen sichtbar. |
| A07 | Offizielle pandas-Release-Notes 2.2.0 als Vollbeleg ergänzt und am betreffenden Absatz regulär zitiert. |
| A08 | World Economic Outlook (WEO) bei der ersten Prosanennung ausgeschrieben. |
| B01 | Sharpe-Formel mit der passenden Primärdefinition «The Ex Post Sharpe Ratio» belegt; arithmetisches Mittel, Differenzrenditen und Annualisierung getrennt erklärt. Formel und Beispielergebnis nicht ungeprüft geändert. |
| B02 | Unbelegte Kurz-/Mittel-/Lang-Typologie für SMA entfernt; Fensterbedeutung ausdrücklich von der Datenfrequenz abhängig erklärt. |
| B03 | Overfitting-Warnung auf den überprüften Abschnitt und ausdrücklich PDF-S.698–699 bezogen; Optimierungsbeleg nicht pauschal als falsch entfernt. |
| B04–B09 | Maximaler Drawdown, Diversifikation bei nicht perfekter Korrelation, Renditereihen statt Kursen, Monatsendpreise, Verschiebung um Beobachtung/Periode und Sharpe als risikoadjustierte Rendite präzisiert. |
| B10–B12 | Acht Quellen-Satzreste, Long/Cash-Satz, 2022-Aussage, Herrn Mock, Yahoo-Fragezeichen und veraltete Vorwärtsverweise korrigiert. Hilpisch-/McKinney-Abschnitte präzisiert. |
| C01 | Zählmethode am Ausgangsstand mit 7’969 reproduziert; neu 7’926 mit / 7’839 ohne Überblick. Zählweise und alle Kapitelzahlen unten und als ausführbares Leseskript offengelegt. Schulische Auslegung bleibt zu klären. |
| C02 | Nur eindeutige Kurztitel und vorhandene Abrufdaten im CSL korrigiert. Keine pauschale Umstellung auf Vgl./Internet-Zusätze oder globale Fussnotenzählung; abweichende Vereinbarungen unbekannt. |
| C03 | Persönliche Endkontrolle offen belassen und im neuen Nachtrag ausdrücklich genannt. |
| C04 | Vier lokale Nachweise durch feste Links auf Commit `229166b485daa8c04a969d4a319d6eeb70da883f` ersetzt; anonymer Abruf und Inhaltsvergleich bestanden. |
| C05 | Alle 64 geprüften ChatGPT-/Repository-Links liefern anonym HTTP200. Die vollständige Lesbarkeit dynamischer Chatinhalte ist dadurch nicht bewiesen. Ein zusätzlich festgestellter alter IMF2009-Downloadlink mit HTTP404 wurde auf die offizielle Archivseite derselben Ausgabe korrigiert; die dort belegte Ausgabedatierung Oktober2009 und tatsächlicher Zugriff31.10.2026 werden getrennt geführt. IMF2024 HTTP429 ist eine Abrufbeschränkung, kein bewiesener toter Link. |
| C06 | Kurze KI-Übersicht direkt nach der Bibliografie ergänzt, mit Verweis auf den detaillierten Anhang. |
| D02–D03 | Die US-Drawdown-Grafik und ihr Quellenabsatz werden per LaTeX-only minipage/nopagebreak zusammengehalten; der einzelne Umgebungsabsatz ist in C.3 integriert und weiterhin über einen direkten Absatzlink erreichbar. |
| D04 | Vier wiederholte Ziel-/Aufbaupassagen zwischen Überblick und Einleitung um 78 Token gestrafft; Forschungsfrage und Motivation erhalten. |
| Sonstiges | Aktuelle Methodenbeschreibung auf tatsächlich erfolgte Schritte statt «vorgesehen/vorgeschlagen» angepasst. Historischer Originalplan A.7 nicht still korrigiert. Weitere freiwillige Stiländerungen nicht breit durchgeführt. |

## Wortumfang

Gezählt wird ausschliesslich die Markdown-Prosa der sechs Hauptnotebooks. Ausgeschlossen werden Raw-/YAML-Zellen, ausführbare Codezellen und ihre Ausgaben, Codefences und HTML-pre, Überschriften, Tabellenzeilen und Captionzeilen, Bilder, Display-/Inline-Mathematik und Zitationsklammern. HTML-Tags, Linkziele, Shortcodes und Querverweis-IDs werden entfernt; sichtbare Linkbeschriftungen bleiben. HTML-Entities werden aufgelöst. Wort-/Zahlentoken folgen `\b\w+(?:[’'-]\w+)*\b`. Literatur und Anhänge sind nicht enthalten. Die Methode reproduziert exakt die frühere Summe am aktuellen Ausgangsstand und ist keine Behauptung einer verbindlich vorgegebenen Schulzählung.

Aufruf aus dem Projektstamm: `python documentation/reviews/2026-10-31-wortzaehlung.py .`. Die JSON-Datei daneben enthält Ausgangs-/Endwerte und die Alternative nur mit buchstabenhaltigen Tokens.

| Kapitel | Ausgang | Nach Überarbeitung |
|---|---:|---:|
| `index.ipynb` | 125 | 87 |
| `notebooks/Einleitung.ipynb` | 435 | 396 |
| `notebooks/Theorie.ipynb` | 2771 | 2794 |
| `notebooks/Methodik.ipynb` | 853 | 859 |
| `notebooks/Analyse.ipynb` | 2956 | 2961 |
| `notebooks/Fazit.ipynb` | 829 | 829 |
| **Mit Überblick** | **7’969** | **7’926** |
| **Ohne Überblick** | **7’844** | **7’839** |

## Integrität und Prüfgrenzen

- Neun Buchnotebooks: Zellzahlen, Zell-IDs, Notebook- und Zellmetadaten erhalten.
- Alle 28 Codezellen: ausführbare Python-ASTs, Execution Counts und alle 28 gespeicherten Outputobjekte identisch. Quellenänderungen nur in den beiden Theorie-Codezellen `061f64f4` (Periodenkommentar) und `c09ff8c4` (Quarto-label/fig-cap).
- Kein Notebookcode, kein Datenadapter und kein Backtest ausgeführt; keine eingefrorenen Daten/Resultate neu berechnet. Redaktionelle Mathearrays wurden teilweise wertgleich in echte beschriftete Tabellen überführt; Berechnungsformeln wurden nicht geändert.
- Die Quarto-/PDF-Prüfergebnisse sind im Abschnitt «Abschliessende Ausgabekontrolle» dokumentiert. Die persönliche Kontrolle der Quellen, Aussagen und Schlussfolgerungen bleibt beim Autor.

## Konkrete Notebookänderungen

Die folgenden Vorher-/Nachher-Blöcke benennen die tatsächlich ersetzten Passagen, nicht nur allgemeine Tätigkeitsbeschreibungen. Neue Captions und Textverweise sind dabei ausdrücklich Darstellungs-/Belegänderungen; Tabellenwerte und gespeicherte Grafikdaten bleiben erhalten.

### Änderung 1: B04

Datei `notebooks/Einleitung.ipynb`, Zell-ID `f733daa1`.

Vorher:

````text
Der Drawdown beschreibt den grössten beobachteten Rückgang
````

Nachher:

````text
Der maximale Drawdown beschreibt den grössten beobachteten Rückgang
````

### Änderung 2: B03

Datei `notebooks/Einleitung.ipynb`, Zell-ID `a7ae04cd`.

Original-PDF, PDF-Seiten 698–699 neu eingesehen; keine gedruckten Seiten behauptet.

Vorher:

````text
Kapitel 15, «Optimization»
````

Nachher:

````text
Kapitel 15, «Optimization» und «Overfitting», PDF-S. 698–699
````

### Änderung 3: B03

Datei `notebooks/Methodik.ipynb`, Zell-ID `35c815dc`.

Original-PDF, PDF-Seiten 698–699 neu eingesehen; keine gedruckten Seiten behauptet.

Vorher:

````text
Kapitel 15, «Optimization»
````

Nachher:

````text
Kapitel 15, «Optimization» und «Overfitting», PDF-S. 698–699
````

### Änderung 4: A08

Datei `notebooks/Methodik.ipynb`, Zell-ID `e77f7db8`.

Vorher:

````text
archivierten WEO-Herbstausgaben des Internationalen Währungsfonds (IMF)
````

Nachher:

````text
archivierten Herbstausgaben des World Economic Outlook (WEO) des Internationalen Währungsfonds (IMF)
````

### Änderung 5: A04

Datei `notebooks/Methodik.ipynb`, Zell-ID `09fe7307`.

Vorher:

````text
Die fünf festgelegten Läufe werden durch Kürzel zugeordnet;
````

Nachher:

````text
Die fünf festgelegten Läufe in @tbl-studienlaeufe werden durch Kürzel zugeordnet;
````

### Änderung 6: A04

Datei `notebooks/Methodik.ipynb`, Zell-ID `b1b5cc99`.

Vorher:

````text
| **S2** | 2010–2025 | VT-Trend 6/12 |
````

Nachher:

````text
| **S2** | 2010–2025 | VT-Trend 6/12 |

: Festgelegte Vergleichsläufe. Quelle: Eigenes Untersuchungsdesign. {#tbl-studienlaeufe}
````

### Änderung 7: D05

Datei `notebooks/Theorie.ipynb`, Zell-ID `1941d2df`.

Wertende und unpräzise Ausdrücke durch präzise Beschreibung der Gesamtrendite ersetzt; keine Produktentscheidung geändert.

Vorher:

````text
<p>Marktbreite ETFs sind für diese Untersuchung gut geeignet, da sie ganze Anlageklassen mit geringem Aufwand abbilden. ETFs sind günstig, bequem und transparent. Für diese Untersuchung ist der Total Return besser geeignet als der Kursindex. Der Kursindex berücksichtigt keine Dividenden, die wichtig sind, um die wahre Performance nachzuweisen.</p>
````

Nachher:

````text
<p>Marktbreite ETFs bilden für diese Untersuchung ganze Anlageklassen mit geringem Aufwand ab. Für den Vergleich wird die Gesamtrendite einschliesslich reinvestierter Dividenden betrachtet. Ein reiner Kursindex berücksichtigt diese Ausschüttungen nicht.</p>
````

### Änderung 8: B10

Datei `notebooks/Theorie.ipynb`, Zell-ID `8e1550f8`.

Vorher:

````text
Quelle der kumulierten Vermögensformel: [@phamPerformance60402025, S. 51].
````

Nachher:

````text
Die kumulierte Vermögensformel folgt Pham et al. [@phamPerformance60402025, S. 51].
````

### Änderung 9: B11

Datei `notebooks/Theorie.ipynb`, Zell-ID `d510a002`.

Vorher:

````text
2022 verloren beide; Anleihen schützen nicht jede Phase.
````

Nachher:

````text
2022 verloren beide Anlageklassen an Wert; Anleihen schützen nicht in jeder Marktphase vor Verlusten.
````

### Änderung 10: B12

Datei `notebooks/Theorie.ipynb`, Zell-ID `005fce46`.

Stabiler Verweis für das bereits im Theorieteil stehende Resampling-Beispiel.

Vorher:

````text
#### Resampling

````

Nachher:

````text
#### Resampling {#sec-theorie-resampling}

````

### Änderung 11: B07

Datei `notebooks/Theorie.ipynb`, Zell-ID `e1888b20`.

Vorher:

````text
<p>Um Vorausschauverzerrung zu vermeiden, sollte man grundsätzlich immer den letzten verfügbaren Wert des Intervalls verwenden.</p>
````

Nachher:

````text
<p>Für Monatsendpreise wird der letzte verfügbare Preis des abgeschlossenen Monats verwendet. Tagesrenditen werden dagegen über ihre Wachstumsfaktoren zur Monatsrendite verknüpft. Signal- und Handelszeitpunkte müssen zusätzlich zeitlich korrekt festgelegt werden.</p>
````

### Änderung 12: B10

Datei `notebooks/Theorie.ipynb`, Zell-ID `4670f764`.

Vorher:

````text
Quelle der Formeln und der entsprechenden Pandas-Umsetzung: [@hilpischPythonFinanceMastering2019, S. 315-316; @PandasSeriespct_changePandas305].
````

Nachher:

````text
Die Formeln und die entsprechende pandas-Umsetzung folgen Hilpisch und der pandas-Dokumentation [@hilpischPythonFinanceMastering2019, S. 315-316; @PandasSeriespct_changePandas305].
````

### Änderung 13: B10

Datei `notebooks/Theorie.ipynb`, Zell-ID `6a341a65`.

Vorher:

````text
Quelle der Formeln: [@hilpischPythonFinanceMastering2019, S. 317-318].
````

Nachher:

````text
Die Formeln folgen Hilpisch [@hilpischPythonFinanceMastering2019, S. 317-318].
````

### Änderung 14: B08

Datei `notebooks/Theorie.ipynb`, Zell-ID `061f64f4`.

Ausschliesslich Kommentar geändert; ausführbarer Code und gespeicherte Ausgabe unverändert.

Vorher:

````text
# und shift(1) verschiebt die Serie um einen Tag zurück, um die Rendite zu berechnen
````

Nachher:

````text
# und shift(1) verschiebt die Serie um eine Beobachtung/Periode, um die Rendite zu berechnen
````

### Änderung 15: B01

Datei `notebooks/Theorie.ipynb`, Zell-ID `6889baa6`.

Vorher:

````text
Davon unterscheidet sich der arithmetische Mittelwert, der etwa bei der Sharpe Ratio verwendet wird [@phamPerformance60402025, S. 50-51].
````

Nachher:

````text
Die geometrische Definition folgt Pham et al. [@phamPerformance60402025, S. 50-51]. Die Sharpe Ratio verwendet dagegen das arithmetische Mittel der Überschussrenditen [@sharpe1994ExPost, Abschnitt «The Ex Post Sharpe Ratio»].
````

### Änderung 16: B10

Datei `notebooks/Theorie.ipynb`, Zell-ID `10386aae`.

Vorher:

````text
Quelle der Formel: [@hilpischPythonFinanceMastering2019, S. 694].
````

Nachher:

````text
Die Annualisierungsformel folgt Hilpisch [@hilpischPythonFinanceMastering2019, S. 694].
````

### Änderung 17: B01/Bibliografie

Datei `notebooks/Theorie.ipynb`, Zell-ID `10386aae`.

Vorher:

````text
[@sharpeSharpeRatioFall2021]
````

Nachher:

````text
[@sharpe1994ExPost, Abschnitt «Time Dependence»]
````

### Änderung 18: B05

Datei `notebooks/Theorie.ipynb`, Zell-ID `03486f6b`.

Vorher:

````text
Ein breit gestreutes Portfolio schwankt meist weniger, sofern die Renditen seiner Wertpapiere nicht untereinander zusammenhängen
````

Nachher:

````text
Die risikomindernde Wirkung hängt von Gewichten, Einzelvolatilitäten und Korrelationen ab; auch positive Korrelationen unter +1 können dazu beitragen
````

### Änderung 19: A05

Datei `notebooks/Theorie.ipynb`, Zell-ID `c09ff8c4`.

Nur Quarto-Darstellungsoptionen ergänzt; Python-Anweisungen, Metadaten und gespeicherte Ausgaben unverändert.

Vorher:

````text
#| fig-align: center

````

Nachher:

````text
#| fig-align: center
#| label: fig-volatilitaet-synthetisch
#| fig-cap: "Synthetische Monatsrenditen mit gleichem Mittel und unterschiedlicher Volatilität. Quelle: Eigene Darstellung."

````

### Änderung 20: A05/B06

Datei `notebooks/Theorie.ipynb`, Zell-ID `5a028097`.

Vorher:

````text
<p>Das Beispiel zeigt übertrieben, wie ein Kurs bei gleichem arithmetischem Mittel der Monatsrenditen eine ganz unterschiedliche Volatilität aufweisen kann.</p>
````

Nachher:

````text
<p>@fig-volatilitaet-synthetisch zeigt zwei synthetische Renditereihen mit gleichem arithmetischem Mittel der Monatsrenditen und unterschiedlicher Volatilität.</p>
````

### Änderung 21: B10

Datei `notebooks/Theorie.ipynb`, Zell-ID `3a60969c`.

Vorher:

````text
Quelle der relativen Drawdown-Formel: [@phamPerformance60402025, S. 51].
````

Nachher:

````text
Die relative Drawdown-Formel folgt Pham et al. [@phamPerformance60402025, S. 51].
````

### Änderung 22: B10

Datei `notebooks/Theorie.ipynb`, Zell-ID `2e6c469f`.

Vorher:

````text
Quelle der Formel: [@phamPerformance60402025, S. 51].
````

Nachher:

````text
Die Formel folgt Pham et al. [@phamPerformance60402025, S. 51].
````

### Änderung 23: B01

Datei `notebooks/Theorie.ipynb`, Zell-ID `909f608f`.

Sharpe-Autorenfassung direkt geprüft; Formel und Beispielrechnung unverändert.

Vorher:

````text
<p>Die periodische Sharpe Ratio ist bei Pham et al. angegeben [@phamPerformance60402025, S. 51]. Die Annualisierung mit der Quadratwurzel der Periodenzahl setzt insbesondere unkorrelierte periodische Überschussrenditen voraus [@sharpeSharpeRatioFall2021].</p>
````

Nachher:

````text
<p>Die periodische Ex-post-Sharpe-Ratio teilt das arithmetische Mittel der Überschussrenditen durch deren Stichproben-Standardabweichung [@sharpe1994ExPost, Abschnitt «The Ex Post Sharpe Ratio»]. Die getrennte Annualisierung mit $\sqrt{m}$ setzt insbesondere unkorrelierte periodische Überschussrenditen voraus [@sharpe1994ExPost, Abschnitt «Time Dependence»].</p>
````

### Änderung 24: A04

Datei `notebooks/Theorie.ipynb`, Zell-ID `52959a27`.

Vorher:

````text
Die einzelnen Zeichen der Formel bedeuten:
````

Nachher:

````text
Die Zeichen der Formel werden in @tbl-sharpe-symbole erklärt:
````

### Änderung 25: A04

Datei `notebooks/Theorie.ipynb`, Zell-ID `6e2866c3`.

Vorher:

````text
| $\sqrt{m}$ | Faktor für die Annualisierung unter den oben genannten Voraussetzungen. |
````

Nachher:

````text
| $\sqrt{m}$ | Faktor für die Annualisierung unter den oben genannten Voraussetzungen. |

: Zeichen der annualisierten Sharpe Ratio. Quelle: Eigene Erläuterung nach Sharpe. {#tbl-sharpe-symbole}
````

### Änderung 26: B10/B02

Datei `notebooks/Theorie.ipynb`, Zell-ID `c68fa307`.

Vorher:

````text
Quelle der Formel: [@hilpischPythonFinanceMastering2019, S. 326-328 und 689-692].
````

Nachher:

````text
Die Formel beschreibt Hilpischs gleitenden Mittelwert [@hilpischPythonFinanceMastering2019, Kapitel 8, «A Technical Analysis Example», PDF-S. 326–328].
````

### Änderung 27: B02

Datei `notebooks/Theorie.ipynb`, Zell-ID `c68fa307`.

Unbelegte Typologie entfernt; Original-PDF S.326–328 kontrolliert.

Vorher:

````text
Ein kurzer SMA (n=10-20) reagiert schneller als ein langer (n=100-200); mittelfristige Fenster (n=20-100) liegen dazwischen. Eine Kreuzung der Linien heisst Crossover [@hilpischPythonFinanceMastering2019, S. 326-328].
````

Nachher:

````text
Kürzere Fenster reagieren schneller; ihre zeitliche Bedeutung hängt von der Datenfrequenz ab. Hilpisch zeigt dies mit 42 und 252 Tagesbeobachtungen. Eine Kreuzung der Linien heisst Crossover [@hilpischPythonFinanceMastering2019, Kapitel 8, «A Technical Analysis Example», PDF-S. 326–328].
````

### Änderung 28: B11

Datei `notebooks/Theorie.ipynb`, Zell-ID `0c76df80`.

Vorher:

````text
Grundidee nach [@hilpischPythonFinanceMastering2019, S. 691-692];
````

Nachher:

````text
Die Grundidee folgt Hilpisch [@hilpischPythonFinanceMastering2019, S. 691-692];
````

### Änderung 29: B10

Datei `notebooks/Theorie.ipynb`, Zell-ID `2d7aee16`.

Vorher:

````text
Quelle der zeitlich verschobenen Anwendung des Signals: [@hilpischPythonFinanceMastering2019, S. 694].
````

Nachher:

````text
Die zeitlich verschobene Signalanwendung folgt Hilpisch [@hilpischPythonFinanceMastering2019, S. 694].
````

### Änderung 30: B03

Datei `notebooks/Theorie.ipynb`, Zell-ID `d513a003`.

Vorher:

````text
[@hilpischPythonFinanceMastering2019, S. 697]
````

Nachher:

````text
[@hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization» und «Overfitting», PDF-S. 698–699]
````

### Änderung 31: B03

Datei `notebooks/Anhang_Technische_Engine.ipynb`, Zell-ID `b1268cba`.

Vorher:

````text
[@hilpischPythonFinanceMastering2019, S. 697]
````

Nachher:

````text
[@hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization» und «Overfitting», PDF-S. 698–699]
````

### Änderung 32: Bibliografie

Datei `notebooks/Anhang_Technische_Engine.ipynb`, Zell-ID `d499d0c0`.

Original-PDF S.132–133 kontrolliert; unbelegte pauschale Ableitung einer Modularchitektur entfernt.

Vorher:

````text
Hilpisch zeigt ebenfalls, dass wiederverwendbarer Python-Code aus interaktiven Beispielen in Funktionen und Module ausgelagert werden kann [@hilpischPythonFinanceMastering2019].
````

Nachher:

````text
Hilpisch erläutert Funktionen mit festgelegten Ein- und Ausgaben [@hilpischPythonFinanceMastering2019, Kapitel 3, «Excursion: Functional Programming», PDF-S. 132–133]. Die konkrete Aufteilung in Module ist eine eigene Designentscheidung.
````

### Änderung 33: Bibliografie

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `7de96757`.

Offizielle Online-Ausgabe des Autors mit Abschnitt und Kapitelübersicht kontrolliert.

Vorher:

````text
[@mckinneyPythonDataAnalysis2022]
````

Nachher:

````text
[@mckinneyPythonDataAnalysis2022, Kapitel 1, «What Is This Book About?», und Kapitel 6–8]
````

### Änderung 34: Bibliografie

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `aa6eac7c`.

Vorher:

````text
[@mckinneyPythonDataAnalysis2022]
````

Nachher:

````text
[@mckinneyPythonDataAnalysis2022, Kapitel 6, «Reading and Writing Data in Text Format»]
````

### Änderung 35: Bibliografie

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `9c8038c2`.

Vorher:

````text
[@mckinneyPythonDataAnalysis2022]
````

Nachher:

````text
[@mckinneyPythonDataAnalysis2022, Kapitel 8, «Pivoting “Long” to “Wide” Format»]
````

### Änderung 36: A07

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `7afa023e`.

Vorher:

````text
Der dokumentierte Studienstand nutzt pandas 2.3.3 und ME.
````

Nachher:

````text
Der dokumentierte Studienstand nutzt pandas 2.3.3 und ME [@pandasReleaseNotes2202024, Abschnitt «Deprecate aliases M, Q, Y, etc. in favour of ME, QE, YE, etc. for offsets»].
````

### Änderung 37: B12

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `c8856345`.

Vorher:

````text
<p>Für das "Resampling" gibt es in pandas eine eingebaute Funktion, die oben stark vereinfacht dargestellt ist. Nun folgt ein konkretes Beispiel für die Nutzung dieser Funktion.</p>
````

Nachher:

````text
<p>Die Aufrufstruktur zeigt pandas-Resampling stark vereinfacht. Das konkrete Python-Beispiel steht in @sec-theorie-resampling.</p>
````

### Änderung 38: B12

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `7e670f16`.

Vorher:

````text
Quelle zur Nutzung von to_datetime() [@mckinneyPythonDataAnalysis2022, Kapitel 11, «Converting Between String and Datetime»].
````

Nachher:

````text
Die Datumsumwandlung mit <code>to_datetime()</code> im Beispiel in @sec-theorie-resampling folgt McKinney [@mckinneyPythonDataAnalysis2022, Kapitel 11, «Converting Between String and Datetime»].
````

### Änderung 39: B12

Datei `notebooks/Anhang_Tests_Validierung.ipynb`, Zell-ID `a4355b5e`.

Vorher:

````text
Die folgenden Tabellen und Grafiken werden daraus abgeleitet;
````

Nachher:

````text
Die Tabellen und Grafiken in Abschnitt 5.4 werden daraus abgeleitet;
````

### Änderung 40: A04

Datei `notebooks/Anhang_Technische_Engine.ipynb`, Zell-ID `b3e90889`.

Wertgleiche Umwandlung einer redaktionellen LaTeX-Mathearray-Tabelle in eine nummerierte Quarto-Tabelle; keine mathematische Formel geändert.

Vorher:

````text
$$
\begin{array}{l|l}
\textbf{Vorhandene Funktion} & \textbf{Geplante Verwendung} \\
\hline
\texttt{resample\_dataframe()} & \text{Datenfrequenz anpassen} \\
\texttt{prozentuale\_aenderung()} & \text{Periodische Renditen} \\
\texttt{kumulierte\_rendite()} \,/\, \texttt{wachstumsfaktor()} & \text{Kumulierte Entwicklung} \\
\texttt{geometrisches\_mittel()} \,/\, \texttt{annualisierte\_rendite()} & \text{Langfristige Rendite} \\
\texttt{standardabweichung()} \,/\, \texttt{annualisierte\_volatilitaet()} & \text{Volatilität} \\
\texttt{drawdown()} \,/\, \texttt{maximum\_drawdown()} & \text{Verlustphasen} \\
\texttt{sharpe\_ratio()} & \text{Risikobereinigte Rendite} \\
\texttt{korrelationsmatrix()} \,/\, \texttt{portfolio\_risiko()} & \text{Portfolioanalyse} \\
\texttt{neue\_gewichtung()} \,/\, \texttt{rebalancing()} & \text{Rebalancing} \\
\texttt{buy\_and\_hold()} & \text{Passive Benchmark} \\
\texttt{trendfolge()} & \text{SMA-Strategie}
\end{array}
$$
````

Nachher:

````text
| Vorhandene Funktion | Geplante Verwendung |
|:---|:---|
| `resample_dataframe()` | Datenfrequenz anpassen |
| `prozentuale_aenderung()` | Periodische Renditen |
| `kumulierte_rendite()` / `wachstumsfaktor()` | Kumulierte Entwicklung |
| `geometrisches_mittel()` / `annualisierte_rendite()` | Langfristige Rendite |
| `standardabweichung()` / `annualisierte_volatilitaet()` | Volatilität |
| `drawdown()` / `maximum_drawdown()` | Verlustphasen |
| `sharpe_ratio()` | Risikobereinigte Rendite |
| `korrelationsmatrix()` / `portfolio_risiko()` | Portfolioanalyse |
| `neue_gewichtung()` / `rebalancing()` | Rebalancing |
| `buy_and_hold()` | Passive Benchmark |
| `trendfolge()` | SMA-Strategie |

: Geplante Zuordnung vorhandener Funktionen. Quelle: Eigene Systemplanung. {#tbl-funktionszuordnung}

````

### Änderung 41: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `60522412`.

Wertgleiche Umwandlung einer redaktionellen LaTeX-Mathearray-Tabelle in eine nummerierte Quarto-Tabelle; keine mathematische Formel geändert.

Vorher:

````text
$$
\begin{array}{|l|l|}
\hline
\textbf{Feld} & \textbf{Bedeutung} \\
\hline
\texttt{date} & \text{Datum der Beobachtung} \\
\hline
\texttt{asset\_id} & \text{interne, anbieterunabhängige Kennung der Anlage} \\
\hline
\texttt{performance\_value} & \text{Wertreihe, aus der die Performance berechnet werden darf} \\
\hline
\end{array}
$$
````

Nachher:

````text
| Feld | Bedeutung |
|:---|:---|
| `date` | Datum der Beobachtung |
| `asset_id` | interne, anbieterunabhängige Kennung der Anlage |
| `performance_value` | Wertreihe, aus der die Performance berechnet werden darf |

: Pflichtfelder einer Marktzeitreihe. Quelle: Eigener Datenvertrag. {#tbl-marktdaten-pflichtfelder}

````

### Änderung 42: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `177c2351`.

Vorher:

````text
Für eine Marktzeitreihe sind zunächst drei Pflichtfelder definiert:
````

Nachher:

````text
Die drei Pflichtfelder einer Marktzeitreihe stehen in @tbl-marktdaten-pflichtfelder.
````

### Änderung 43: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `46890aea`.

Wertgleiche Umwandlung einer redaktionellen LaTeX-Mathearray-Tabelle in eine nummerierte Quarto-Tabelle; keine mathematische Formel geändert.

Vorher:

````text
$$
\begin{array}{|l|l|}
\hline
\textbf{Feld} & \textbf{Bedeutung} \\
\hline
\texttt{signal\_value} & \text{separate Wertreihe für technische Handelssignale} \\
\hline
\end{array}
$$
````

Nachher:

````text
| Feld | Bedeutung |
|:---|:---|
| `signal_value` | separate Wertreihe für technische Handelssignale |

: Optionales Feld für Handelssignale. Quelle: Eigener Datenvertrag. {#tbl-marktdaten-signalfeld}

````

### Änderung 44: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `7d852e65`.

Vorher:

````text
Optional kann eine vierte Spalte vorhanden sein:
````

Nachher:

````text
@tbl-marktdaten-signalfeld ergänzt die optionale vierte Spalte.
````

### Änderung 45: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `08d67f37`.

Wertgleiche Umwandlung einer redaktionellen LaTeX-Mathearray-Tabelle in eine nummerierte Quarto-Tabelle; keine mathematische Formel geändert.

Vorher:

````text
$$
\begin{array}{|c|c|c|c|}
\hline
\textbf{date} & \textbf{asset\_id} & \textbf{performance\_value} & \textbf{signal\_value} \\
\hline
2020\text{-}01\text{-}02 & \texttt{EQ\_DEMO} & 100.0 & 50.25 \\
\hline
2020\text{-}01\text{-}03 & \texttt{EQ\_DEMO} & 102.0 & 51.00 \\
\hline
2020\text{-}01\text{-}02 & \texttt{BD\_DEMO} & 100.0 & 104.80 \\
\hline
2020\text{-}01\text{-}03 & \texttt{BD\_DEMO} & 100.5 & 104.90 \\
\hline
\end{array}
$$
````

Nachher:

````text
| date | asset_id | performance_value | signal_value |
|:---|:---|:---|:---|
| 2020-01-02 | `EQ_DEMO` | 100.0 | 50.25 |
| 2020-01-03 | `EQ_DEMO` | 102.0 | 51.00 |
| 2020-01-02 | `BD_DEMO` | 100.0 | 104.80 |
| 2020-01-03 | `BD_DEMO` | 100.5 | 104.90 |

: Künstliches Beispiel einer Marktdatei. Quelle: Eigene Darstellung. {#tbl-marktdaten-beispiel}

````

### Änderung 46: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `57353424`.

Vorher:

````text
<p>Beispiel:</p>
````

Nachher:

````text
<p>@tbl-marktdaten-beispiel zeigt die Struktur an künstlichen Daten.</p>
````

### Änderung 47: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `b6cd7755`.

Wertgleiche Umwandlung einer redaktionellen LaTeX-Mathearray-Tabelle in eine nummerierte Quarto-Tabelle; keine mathematische Formel geändert.

Vorher:

````text
$$
\begin{array}{c|c}
\textbf{Feld} & \textbf{Bedeutung} \\
\hline
\texttt{asset\_id} & \text{Interne, anbieterunabhängige Kennung der Anlage} \\
\texttt{name} & \text{Name der Anlage} \\
\texttt{asset\_class} & \text{Anlageklasse, z. B. Aktien oder Anleihen} \\
\texttt{country} & \text{Zugeordnetes Land bzw. Markt} \\
\texttt{currency} & \text{Währung der Anlage} \\
\texttt{provider} & \text{Datenanbieter} \\
\texttt{provider\_symbol} & \text{Symbol bzw. Kennung beim Datenanbieter}
\end{array}
$$
````

Nachher:

````text
| Feld | Bedeutung |
|:---|:---|
| `asset_id` | Interne, anbieterunabhängige Kennung der Anlage |
| `name` | Name der Anlage |
| `asset_class` | Anlageklasse, z. B. Aktien oder Anleihen |
| `country` | Zugeordnetes Land bzw. Markt |
| `currency` | Währung der Anlage |
| `provider` | Datenanbieter |
| `provider_symbol` | Symbol bzw. Kennung beim Datenanbieter |

: Schema der Anlagenmetadaten. Quelle: Eigener Datenvertrag. {#tbl-assets-schema}

````

### Änderung 48: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `75920638`.

Vorher:

````text
Für diese Informationen ist eine Datei <code>assets.csv</code> vorgesehen:
````

Nachher:

````text
Für diese Informationen ist <code>assets.csv</code> mit dem Schema in @tbl-assets-schema vorgesehen.
````

### Änderung 49: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `69ec8b96`.

Wertgleiche Umwandlung einer redaktionellen LaTeX-Mathearray-Tabelle in eine nummerierte Quarto-Tabelle; keine mathematische Formel geändert.

Vorher:

````text
$$
\begin{array}{c|c}
\textbf{Feld} & \textbf{Bedeutung} \\
\hline
\texttt{date} & \text{Datum der Beobachtung} \\
\texttt{series\_id} & \text{Kennung der risikofreien Zinsreihe} \\
\texttt{value} & \text{Beobachteter Zinssatz} \\
\texttt{unit} & \text{Einheit des Wertes}
\end{array}
$$
````

Nachher:

````text
| Feld | Bedeutung |
|:---|:---|
| `date` | Datum der Beobachtung |
| `series_id` | Kennung der risikofreien Zinsreihe |
| `value` | Beobachteter Zinssatz |
| `unit` | Einheit des Wertes |

: Schema der Zinsquelldaten. Quelle: Eigener Datenvertrag. {#tbl-zinsquellen-schema}

````

### Änderung 50: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `6cc5e280`.

Vorher:

````text
Dafür ist eine getrennte Datei vorgesehen:
````

Nachher:

````text
Dafür ist eine getrennte Datei nach @tbl-zinsquellen-schema vorgesehen.
````

### Änderung 51: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `99053056`.

Wertgleiche Umwandlung einer redaktionellen LaTeX-Mathearray-Tabelle in eine nummerierte Quarto-Tabelle; keine mathematische Formel geändert.

Vorher:

````text
$$
\begin{array}{c|c}
\textbf{Feld} & \textbf{Bedeutung} \\
\hline
\texttt{period} & \text{Zeitraum der Beobachtung} \\
\texttt{country} & \text{Land, auf das sich der Wert bezieht} \\
\texttt{indicator} & \text{Makroökonomischer Indikator} \\
\texttt{value} & \text{Beobachteter Wert} \\
\texttt{unit} & \text{Einheit des Wertes} \\
\texttt{available\_from} & \text{Zeitpunkt, ab dem die Information verfügbar war}
\end{array}
$$
````

Nachher:

````text
| Feld | Bedeutung |
|:---|:---|
| `period` | Zeitraum der Beobachtung |
| `country` | Land, auf das sich der Wert bezieht |
| `indicator` | Makroökonomischer Indikator |
| `value` | Beobachteter Wert |
| `unit` | Einheit des Wertes |
| `available_from` | Zeitpunkt, ab dem die Information verfügbar war |

: Schema der Makrodaten. Quelle: Eigener Datenvertrag. {#tbl-makrodaten-schema}

````

### Änderung 52: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `63de8b18`.

Vorher:

````text
Sie werden deshalb separat gespeichert:
````

Nachher:

````text
Sie werden deshalb separat nach @tbl-makrodaten-schema gespeichert.
````

### Änderung 53: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `841c6786`.

Wertgleiche Umwandlung einer redaktionellen LaTeX-Mathearray-Tabelle in eine nummerierte Quarto-Tabelle; keine mathematische Formel geändert.

Vorher:

````text
$$
\begin{array}{c|c|c}
\textbf{Date} & \textbf{Ticker} & \textbf{TR} \\
\hline
\texttt{2020-01-02} & \texttt{ABC} & 100.0
\end{array}
$$
````

Nachher:

````text
| Date | Ticker | TR |
|:---|:---|:---|
| `2020-01-02` | `ABC` | 100.0 |

: Künstliches Beispiel einer fremden CSV-Datei. Quelle: Eigene Darstellung. {#tbl-csv-quellbeispiel}

````

### Änderung 54: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `7fb1292c`.

Vorher:

````text
Beispiel einer Quelldatei:
````

Nachher:

````text
@tbl-csv-quellbeispiel zeigt eine künstliche Quelldatei.
````

### Änderung 55: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `978bbfca`.

Vorher:

````text
| `U` | Microseconds |
````

Nachher:

````text
| `U` | Microseconds |

: Historische pandas-Frequenzaliase. Quelle: Hilpisch (2019), PDF-S. 191–192. {#tbl-frequenzaliase}
````

### Änderung 56: A04

Datei `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `7afa023e`.

Vorher:

````text
Die folgende historische Aliasübersicht stammt aus Hilpisch (2019).
````

Nachher:

````text
Die historische Aliasübersicht in @tbl-frequenzaliase stammt aus Hilpisch (2019).
````

### Änderung 57: A04

Datei `notebooks/Anhang_Technische_Engine.ipynb`, Zell-ID `bd94c0c8`.

Vorher:

````text
Sie bilden die Grundlage der späteren Engine.
````

Nachher:

````text
Ihre geplante Zuordnung in @tbl-funktionszuordnung bildet die Grundlage der späteren Engine.
````

### Änderung 58: D04/C01

Datei `index.ipynb`, Zell-ID `bfc2fb04`.

Auf ausdrücklichen Folgeauftrag von Root redundant erklärte Ziel-/Aufbaupassagen gestrafft; Forschungsfrage, Motivation, Methoden und Ergebnisse unverändert.

Vorher:

````text
Diese Arbeit verbindet Finanztheorie und Informatik. Untersucht wird, wie ein Python-Modell historische Finanzdaten aufbereitet und festgelegte Anlageregeln anwendet, um langfristige Strategien hinsichtlich Rendite und Risiko zu vergleichen.

````

Nachher:

````text
Diese Arbeit verbindet Finanztheorie und Informatik und vergleicht langfristige Anlageregeln mit historischen Daten in einem Python-Modell.

````

### Änderung 59: D04/C01

Datei `index.ipynb`, Zell-ID `af2cc3a8`.

Auf ausdrücklichen Folgeauftrag von Root redundant erklärte Ziel-/Aufbaupassagen gestrafft; Forschungsfrage, Motivation, Methoden und Ergebnisse unverändert.

Vorher:

````text
Die Einleitung beschreibt Motivation, Ziele und Untersuchungsrahmen. Die Theorie erklärt die benötigten Begriffe, Strategien und Berechnungen; die Methodik legt die Vergleichsbedingungen fest. Die Analyse begründet Daten und Parameter, stellt die Ergebnisse dar und interpretiert ihre Unterschiede. Das Fazit beantwortet die Forschungsfrage und enthält den Rückblick und Ausblick des Autors.

Technische Entwicklung, Datenaufbereitung und Prüfungen stehen in den Anhängen A–C, die KI-Nutzung in D. Installationshinweise, Quellen- und Werkzeugplanung sowie die ursprünglichen Pendenzen sind in @sec-projekt-anleitungen, @sec-projekt-quellenplanung und @sec-projekt-pendenzen als historischer Projektstand dokumentiert.

````

Nachher:

````text
Die Einleitung erläutert Motivation und Ziele, die Theorie Begriffe und Berechnungen. Methodik und Analyse führen von Vergleichsbedingungen und Datenwahl zu Ergebnissen und Interpretation. Das Fazit enthält Antwort, Rückblick und Ausblick.

Technische Entwicklung, Datenaufbereitung und Prüfungen stehen in A–C, die KI-Nutzung in D. Historische Installationshinweise, Quellenplanung und Pendenzen sind in @sec-projekt-anleitungen, @sec-projekt-quellenplanung und @sec-projekt-pendenzen dokumentiert.

````

### Änderung 60: D04/C01

Datei `notebooks/Einleitung.ipynb`, Zell-ID `a9f0792b`.

Auf ausdrücklichen Folgeauftrag von Root redundant erklärte Ziel-/Aufbaupassagen gestrafft; Forschungsfrage, Motivation, Methoden und Ergebnisse unverändert.

Vorher:

````text
<p>Die Arbeit verbindet zwei Ziele: ein Python-Modell zur Verarbeitung historischer Daten und Anwendung festgelegter Regeln sowie einen Vergleich von Rendite, Schwankungen und zwischenzeitlichen Verlusten. Neben dem Endwert sollen Investitionszeitpunkte und Veränderungen der Portfoliozusammensetzung nachvollzogen werden.</p>

````

Nachher:

````text
<p>Ziel sind ein überprüfbares Python-Modell und ein Vergleich von Rendite und Risiko. Neben dem Endwert werden Investitionszeitpunkte und Veränderungen der Portfoliozusammensetzung nachvollzogen.</p>

````

### Änderung 61: D04/C01

Datei `notebooks/Einleitung.ipynb`, Zell-ID `5f03e85d`.

Auf ausdrücklichen Folgeauftrag von Root redundant erklärte Ziel-/Aufbaupassagen gestrafft; Forschungsfrage, Motivation, Methoden und Ergebnisse unverändert.

Vorher:

````text
<p>Der Aufbau steht in Abschnitt 1.2. Python-Beispiele verbinden die Theorie mit der Anwendung; Methodik und Analyse führen von festgelegten Vergleichsbedingungen über Datenwahl und Durchführung zu Ergebnissen und Interpretation. Das Fazit beantwortet die Forschungsfrage und ordnet Grenzen sowie Weiterführungen ein.</p>

````

Nachher:

````text
<p>Abschnitt 1.2 beschreibt den Aufbau. Die Python-Beispiele verbinden dabei Theorie und Anwendung.</p>

````

### Änderung 62: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `a1781f55`.

Vorher:

````text
| Interne Kennung | Yahoo-Symbol | Verwendung | Produktnachweis |
|---|---|---|---|
| *`WORLD_EQ`* | *`VT`* | Weltweiter Aktienanteil | [@VanguardTotalWorld] |
| *`US_TREASURY_7_10`* | *`IEF`* | US-Staatsanleihen, 7–10 Jahre | [@IShares710Year] |
| *`US_EQ`* | *`VTI`* | US-Aktienproxy und längere US-Zusatzuntersuchung | [@VanguardMorningstarTotal] |
| *`CA_EQ`* | *`EWC`* | Kanada | [@ISharesMSCICanada] |
| *`JP_EQ`* | *`EWJ`* | Japan | [@ISharesMSCIJapan] |
| *`GB_EQ`* | *`EWU`* | Vereinigtes Königreich | [@ISharesMSCIUnited] |
| *`DE_EQ`* | *`EWG`* | Deutschland | [@ISharesMSCIGermany] |
| *`FR_EQ`* | *`EWQ`* | Frankreich | [@ISharesMSCIFrance] |
| *`IT_EQ`* | *`EWI`* | Italien | [@ISharesMSCIItaly] |
````

Nachher:

````text
| Interne Kennung | Yahoo-Symbol | Verwendung | Produktnachweis |
|---|---|---|---|
| *`WORLD_EQ`* | *`VT`* | Weltweiter Aktienanteil | [@VanguardTotalWorld] |
| *`US_TREASURY_7_10`* | *`IEF`* | US-Staatsanleihen, 7–10 Jahre | [@IShares710Year] |
| *`US_EQ`* | *`VTI`* | US-Aktienproxy und längere US-Zusatzuntersuchung | [@VanguardMorningstarTotal] |
| *`CA_EQ`* | *`EWC`* | Kanada | [@ISharesMSCICanada] |
| *`JP_EQ`* | *`EWJ`* | Japan | [@ISharesMSCIJapan] |
| *`GB_EQ`* | *`EWU`* | Vereinigtes Königreich | [@ISharesMSCIUnited] |
| *`DE_EQ`* | *`EWG`* | Deutschland | [@ISharesMSCIGermany] |
| *`FR_EQ`* | *`EWQ`* | Frankreich | [@ISharesMSCIFrance] |
| *`IT_EQ`* | *`EWI`* | Italien | [@ISharesMSCIItaly] |

: Verwendete ETF-Reihen und ihre Modellrollen {#tbl-etf-auswahl}

````

### Änderung 63: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `937d4e0c`.

Vorher:

````text
| Lauf | Zeitraum der Renditen | Vergleich | Funktion in der Arbeit |
|---|---|---|---|
| **H1** | 2010–2025 | VT Buy-and-Hold; VT/IEF 60/40; VT Trend 3/12; sieben Länder BIP-gewichtet | Hauptvergleich verschiedener Konzepte |
| **K1** | 2010–2025 | Gleiche sieben Länder: BIP versus jährliche Gleichgewichtung | Gewichtungsvergleich bei identischen Bausteinen |
| **Z1** | 2003–2025 | VTI Buy-and-Hold; VTI/IEF 60/40; VTI Trend 3/12 | Längerer regionaler Zusatzvergleich |
| **S1 / S2** | 2010–2025 | VT Trend 2/12 beziehungsweise 6/12 | Vorab festgelegte Sensitivität der Trendregel |
````

Nachher:

````text
| Lauf | Zeitraum der Renditen | Vergleich | Funktion in der Arbeit |
|---|---|---|---|
| **H1** | 2010–2025 | VT Buy-and-Hold; VT/IEF 60/40; VT Trend 3/12; sieben Länder BIP-gewichtet | Hauptvergleich verschiedener Konzepte |
| **K1** | 2010–2025 | Gleiche sieben Länder: BIP versus jährliche Gleichgewichtung | Gewichtungsvergleich bei identischen Bausteinen |
| **Z1** | 2003–2025 | VTI Buy-and-Hold; VTI/IEF 60/40; VTI Trend 3/12 | Längerer regionaler Zusatzvergleich |
| **S1 / S2** | 2010–2025 | VT Trend 2/12 beziehungsweise 6/12 | Vorab festgelegte Sensitivität der Trendregel |

: Studienblöcke und Vergleichszwecke {#tbl-studienbloecke}

````

### Änderung 64: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `19427df9`.

Vorher:

````text
| Lauf | Renditezeitraum | Vergleich | Bewertungen / Perioden |
|:---|:---|:---|---:|
| **H1** | 2010–2025 | VT Buy-and-Hold; VT/IEF 60/40; VT-Trend 3/12; BIP-G7 | 193 / 192 |
| **K1** | 2010–2025 | BIP-G7 gegenüber gleichen Ländergewichten | 193 / 192 |
| **Z1** | 2003–2025 | VTI Buy-and-Hold; VTI/IEF 60/40; VTI-Trend 3/12 | 277 / 276 |
| **S1** | 2010–2025 | VT-Trend 2/12 | 193 / 192 |
| **S2** | 2010–2025 | VT-Trend 6/12 | 193 / 192 |
````

Nachher:

````text
| Lauf | Renditezeitraum | Vergleich | Bewertungen / Perioden |
|:---|:---|:---|---:|
| **H1** | 2010–2025 | VT Buy-and-Hold; VT/IEF 60/40; VT-Trend 3/12; BIP-G7 | 193 / 192 |
| **K1** | 2010–2025 | BIP-G7 gegenüber gleichen Ländergewichten | 193 / 192 |
| **Z1** | 2003–2025 | VTI Buy-and-Hold; VTI/IEF 60/40; VTI-Trend 3/12 | 277 / 276 |
| **S1** | 2010–2025 | VT-Trend 2/12 | 193 / 192 |
| **S2** | 2010–2025 | VT-Trend 6/12 | 193 / 192 |

: Tatsächlich ausgeführte Untersuchungen {#tbl-ausgefuehrte-laeufe}

````

### Änderung 65: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `52fbe760`.

Vorher:

````text
| Strategie | Endvermögen (USD) | Gesamtrendite | Rendite p. a. | Volatilität p. a. | Sharpe | Max. Drawdown |
|:---|---:|---:|---:|---:|---:|---:|
| **Buy-and-Hold (VT)** | 466’061 | 366,06 % | 10,10 % | 14,77 % | 0,632 | -25,51 % |
| **60/40 (VT/IEF)** | 311’991 | 211,99 % | 7,37 % | 8,93 % | 0,685 | -21,57 % |
| **Trendfolge (VT, 3/12)** | 262’911 | 162,91 % | 6,23 % | 11,85 % | 0,452 | -29,69 % |
| **BIP-Gewichtung (G7)** | 469’842 | 369,84 % | 10,15 % | 14,98 % | 0,629 | -26,39 % |
````

Nachher:

````text
| Strategie | Endvermögen (USD) | Gesamtrendite | Rendite p. a. | Volatilität p. a. | Sharpe | Max. Drawdown |
|:---|---:|---:|---:|---:|---:|---:|
| **Buy-and-Hold (VT)** | 466’061 | 366,06 % | 10,10 % | 14,77 % | 0,632 | -25,51 % |
| **60/40 (VT/IEF)** | 311’991 | 211,99 % | 7,37 % | 8,93 % | 0,685 | -21,57 % |
| **Trendfolge (VT, 3/12)** | 262’911 | 162,91 % | 6,23 % | 11,85 % | 0,452 | -29,69 % |
| **BIP-Gewichtung (G7)** | 469’842 | 369,84 % | 10,15 % | 14,98 % | 0,629 | -26,39 % |

: Ergebnisse des Hauptlaufs H1 {#tbl-ergebnisse-h1}

````

### Änderung 66: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `304ab9af`.

Vorher:

````text
| Strategie | Endvermögen (USD) | Gesamtrendite | Rendite p. a. | Volatilität p. a. | Sharpe | Max. Drawdown |
|:---|---:|---:|---:|---:|---:|---:|
| **BIP-Gewichtung (G7)** | 469’842 | 369,84 % | 10,15 % | 14,98 % | 0,629 | -26,39 % |
| **Gleichgewichtung (je 1/7)** | 323’348 | 223,35 % | 7,61 % | 16,31 % | 0,446 | -27,09 % |
````

Nachher:

````text
| Strategie | Endvermögen (USD) | Gesamtrendite | Rendite p. a. | Volatilität p. a. | Sharpe | Max. Drawdown |
|:---|---:|---:|---:|---:|---:|---:|
| **BIP-Gewichtung (G7)** | 469’842 | 369,84 % | 10,15 % | 14,98 % | 0,629 | -26,39 % |
| **Gleichgewichtung (je 1/7)** | 323’348 | 223,35 % | 7,61 % | 16,31 % | 0,446 | -27,09 % |

: Ergebnisse des Kontrolllaufs K1 {#tbl-ergebnisse-k1}

````

### Änderung 67: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `a981fff3`.

Vorher:

````text
| Strategie | Endvermögen (USD) | Gesamtrendite | Rendite p. a. | Volatilität p. a. | Sharpe | Max. Drawdown |
|:---|---:|---:|---:|---:|---:|---:|
| **Buy-and-Hold (VTI)** | 1’224’167 | 1124,17 % | 11,51 % | 14,93 % | 0,693 | -50,84 % |
| **60/40 (VTI/IEF)** | 689’367 | 589,37 % | 8,76 % | 8,98 % | 0,792 | -26,79 % |
| **Trendfolge (VTI, 3/12)** | 733’370 | 633,37 % | 9,05 % | 11,12 % | 0,684 | -22,14 % |
````

Nachher:

````text
| Strategie | Endvermögen (USD) | Gesamtrendite | Rendite p. a. | Volatilität p. a. | Sharpe | Max. Drawdown |
|:---|---:|---:|---:|---:|---:|---:|
| **Buy-and-Hold (VTI)** | 1’224’167 | 1124,17 % | 11,51 % | 14,93 % | 0,693 | -50,84 % |
| **60/40 (VTI/IEF)** | 689’367 | 589,37 % | 8,76 % | 8,98 % | 0,792 | -26,79 % |
| **Trendfolge (VTI, 3/12)** | 733’370 | 633,37 % | 9,05 % | 11,12 % | 0,684 | -22,14 % |

: Ergebnisse des US-Zusatzlaufs Z1 {#tbl-ergebnisse-z1}

````

### Änderung 68: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `8af54f16`.

Vorher:

````text
| Strategie | Endvermögen (USD) | Gesamtrendite | Rendite p. a. | Volatilität p. a. | Sharpe | Max. Drawdown |
|:---|---:|---:|---:|---:|---:|---:|
| **VT SMA 2/12** | 261’863 | 161,86 % | 6,20 % | 11,28 % | 0,466 | -22,15 % |
| **VT SMA 3/12** | 262’911 | 162,91 % | 6,23 % | 11,85 % | 0,452 | -29,69 % |
| **VT SMA 6/12** | 338’011 | 238,01 % | 7,91 % | 12,79 % | 0,550 | -22,15 % |
````

Nachher:

````text
| Strategie | Endvermögen (USD) | Gesamtrendite | Rendite p. a. | Volatilität p. a. | Sharpe | Max. Drawdown |
|:---|---:|---:|---:|---:|---:|---:|
| **VT SMA 2/12** | 261’863 | 161,86 % | 6,20 % | 11,28 % | 0,466 | -22,15 % |
| **VT SMA 3/12** | 262’911 | 162,91 % | 6,23 % | 11,85 % | 0,452 | -29,69 % |
| **VT SMA 6/12** | 338’011 | 238,01 % | 7,91 % | 12,79 % | 0,550 | -22,15 % |

: Die drei vorab festgelegten VT-Trendvarianten, 2010–2025 {#tbl-sma-sensitivitaet}

````

### Änderung 69: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `59efb4f5`.

Vorher:

````text
| Strategie | Rendite p. a. 2010–2017 | Rendite p. a. 2018–2025 | Sharpe 2010–2017 | Sharpe 2018–2025 |
|:---|---:|---:|---:|---:|
| **Buy-and-Hold (VT)** | 9,52 % | 10,68 % | 0,723 | 0,555 |
| **60/40 (VT/IEF)** | 7,74 % | 7,00 % | 1,038 | 0,452 |
| **Trendfolge (VT, 3/12)** | 4,57 % | 7,91 % | 0,444 | 0,459 |
| **BIP-Gewichtung (G7)** | 9,45 % | 10,86 % | 0,719 | 0,555 |
````

Nachher:

````text
| Strategie | Rendite p. a. 2010–2017 | Rendite p. a. 2018–2025 | Sharpe 2010–2017 | Sharpe 2018–2025 |
|:---|---:|---:|---:|---:|
| **Buy-and-Hold (VT)** | 9,52 % | 10,68 % | 0,723 | 0,555 |
| **60/40 (VT/IEF)** | 7,74 % | 7,00 % | 1,038 | 0,452 |
| **Trendfolge (VT, 3/12)** | 4,57 % | 7,91 % | 0,444 | 0,459 |
| **BIP-Gewichtung (G7)** | 9,45 % | 10,86 % | 0,719 | 0,555 |

: Vergleich zweier gleich langer Abschnitte von H1 {#tbl-h1-teilperioden}

````

### Änderung 70: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `3337f340`.

Vorher:

````text
| Monat 2020 | VT-Rendite | Gehaltene Position | Neues Signal am Monatsende | Trendrendite |
|:---|---:|:---|:---|---:|
| **Februar** | -7,22 % | Long | Long | -7,22 % |
| **März** | -14,76 % | Long | Cash | -14,76 % |
| **April** | 10,37 % | Cash | Cash | 0,00 % |
| **Mai** | 5,21 % | Cash | Cash | 0,00 % |
| **Juni** | 3,07 % | Cash | Cash | 0,00 % |
| **Juli** | 5,29 % | Cash | Long | 0,00 % |
| **August** | 6,01 % | Long | Long | 6,01 % |
````

Nachher:

````text
| Monat 2020 | VT-Rendite | Gehaltene Position | Neues Signal am Monatsende | Trendrendite |
|:---|---:|:---|:---|---:|
| **Februar** | -7,22 % | Long | Long | -7,22 % |
| **März** | -14,76 % | Long | Cash | -14,76 % |
| **April** | 10,37 % | Cash | Cash | 0,00 % |
| **Mai** | 5,21 % | Cash | Cash | 0,00 % |
| **Juni** | 3,07 % | Cash | Cash | 0,00 % |
| **Juli** | 5,29 % | Cash | Long | 0,00 % |
| **August** | 6,01 % | Long | Long | 6,01 % |

: Signal und tatsächlich gehaltene Position der H1-Trendfolge im Jahr 2020 {#tbl-trendpositionen-2020}

````

### Änderung 71: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `e7f2d428`.

Vorher:

````text
| Land | BIP-Ziel Ende 2009 | BIP-Ziel Ende 2024 | Gleichgewichtetes Ziel |
|:---|---:|---:|---:|
| **USA** | 44,59 % | 58,55 % | 14,29 % |
| **Kanada** | 4,63 % | 4,53 % | 14,29 % |
| **Japan** | 15,16 % | 8,91 % | 14,29 % |
| **Vereinigtes Königreich** | 8,28 % | 7,14 % | 14,29 % |
| **Deutschland** | 11,34 % | 9,56 % | 14,29 % |
| **Frankreich** | 8,85 % | 6,45 % | 14,29 % |
| **Italien** | 7,14 % | 4,86 % | 14,29 % |
````

Nachher:

````text
| Land | BIP-Ziel Ende 2009 | BIP-Ziel Ende 2024 | Gleichgewichtetes Ziel |
|:---|---:|---:|---:|
| **USA** | 44,59 % | 58,55 % | 14,29 % |
| **Kanada** | 4,63 % | 4,53 % | 14,29 % |
| **Japan** | 15,16 % | 8,91 % | 14,29 % |
| **Vereinigtes Königreich** | 8,28 % | 7,14 % | 14,29 % |
| **Deutschland** | 11,34 % | 9,56 % | 14,29 % |
| **Frankreich** | 8,85 % | 6,45 % | 14,29 % |
| **Italien** | 7,14 % | 4,86 % | 14,29 % |

: Ausgewählte Zielgewichte des BIP-Portfolios und der Kontrolle {#tbl-bip-zielgewichte}

````

### Änderung 72: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `9a3b2312`.

Vorher:

````text
| Variante | Long-Monate | Cash-Monate | Positionswechsel |
|:---|---:|---:|---:|
| **2/12** | 153 | 39 | 18 |
| **3/12** | 156 | 36 | 12 |
| **6/12** | 153 | 39 | 12 |
````

Nachher:

````text
| Variante | Long-Monate | Cash-Monate | Positionswechsel |
|:---|---:|---:|---:|
| **2/12** | 153 | 39 | 18 |
| **3/12** | 156 | 36 | 12 |
| **6/12** | 153 | 39 | 12 |

: Investitionsdauer und Positionswechsel der VT-Trendvarianten {#tbl-sma-positionswechsel}

````

### Änderung 73: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `e433fc51`.

Vorher:

````text
<p>Die sieben Länder aus der folgenden Tabelle bilden nicht die Weltwirtschaft ab. Tatsächliche Datenabdeckung ist zu prüfen; Produktseiten beweisen keinen vollständigen oder richtigen Download.</p>

````

Nachher:

````text
<p>Die sieben Länder aus @tbl-etf-auswahl bilden nicht die Weltwirtschaft ab. Tatsächliche Datenabdeckung ist zu prüfen; Produktseiten beweisen keinen vollständigen oder richtigen Download.</p>

````

### Änderung 74: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `04f51bb8`.

Vorher:

````text
<p>Die fünf Läufe bilden den geplanten Umfang. Sensitivitätsvarianten ersetzen den Hauptparameter nicht nachträglich; auch ungünstige oder widersprüchliche Resultate werden gezeigt. Es sind historische Vergleiche, keine Out-of-Sample-Prognoseprüfung.</p>
````

Nachher:

````text
<p>Die fünf Läufe in @tbl-studienbloecke bilden den geplanten Umfang. Sensitivitätsvarianten ersetzen den Hauptparameter nicht nachträglich; auch ungünstige oder widersprüchliche Resultate werden gezeigt. Es sind historische Vergleiche, keine Out-of-Sample-Prognoseprüfung.</p>
````

### Änderung 75: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `4d5be989`.

Vorher:

````text
<strong>Tabelle: Tatsächlich ausgeführte Untersuchungen</strong>
````

Nachher:

````text
@tbl-ausgefuehrte-laeufe zeigt die tatsächlich ausgeführten Untersuchungen.

````

### Änderung 76: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `dd8fed61`.

Vorher:

````text
<strong>Tabelle: Ergebnisse des Hauptlaufs H1</strong>
````

Nachher:

````text
@tbl-ergebnisse-h1 zeigt die Ergebnisse des Hauptlaufs H1.

````

### Änderung 77: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `e566eb52`.

Vorher:

````text
<strong>Tabelle: Ergebnisse des Kontrolllaufs K1</strong>
````

Nachher:

````text
@tbl-ergebnisse-k1 zeigt die Ergebnisse des Kontrolllaufs K1.

````

### Änderung 78: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `096fba73`.

Vorher:

````text
<strong>Tabelle: Ergebnisse des US-Zusatzlaufs Z1</strong>
````

Nachher:

````text
@tbl-ergebnisse-z1 zeigt die Ergebnisse des US-Zusatzlaufs Z1.

````

### Änderung 79: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `2631d055`.

Vorher:

````text
<strong>Tabelle: Die drei vorab festgelegten VT-Trendvarianten, 2010–2025</strong>
````

Nachher:

````text
@tbl-sma-sensitivitaet zeigt die drei vorab festgelegten VT-Trendvarianten.

````

### Änderung 80: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `d6e33122`.

Vorher:

````text
<strong>Tabelle: Vergleich zweier gleich langer Abschnitte von H1</strong>
````

Nachher:

````text
@tbl-h1-teilperioden zeigt zwei gleich lange Abschnitte von H1.

````

### Änderung 81: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `928fe97f`.

Vorher:

````text
<strong>Tabelle: Signal und tatsächlich gehaltene Position der H1-Trendfolge im Jahr 2020</strong>
````

Nachher:

````text
@tbl-trendpositionen-2020 zeigt Signal und gehaltene Position der H1-Trendfolge im Jahr 2020.

````

### Änderung 82: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `82391240`.

Vorher:

````text
<strong>Tabelle: Ausgewählte Zielgewichte des BIP-Portfolios und der Kontrolle</strong>
````

Nachher:

````text
@tbl-bip-zielgewichte zeigt ausgewählte Zielgewichte des BIP-Portfolios und der Kontrolle.

````

### Änderung 83: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `8b805c66`.

Vorher:

````text
<strong>Tabelle: Investitionsdauer und Positionswechsel der VT-Trendvarianten</strong>
````

Nachher:

````text
@tbl-sma-positionswechsel zeigt Investitionsdauer und Positionswechsel der VT-Trendvarianten.

````

### Änderung 84: A04

Datei `notebooks/Analyse.ipynb`, Zell-ID `f7382b02`.

Vorher:

````text
<p>Die Tabelle zeigt die Signalverzögerung: Im März trägt die Trendstrategie noch den Verlust. Das Cash-Signal wirkt erst im April und lässt sie dessen Erholung verpassen. Das Long-Signal von Ende Juli gilt erst im August.</p>
````

Nachher:

````text
<p>@tbl-trendpositionen-2020 zeigt die Signalverzögerung: Im März trägt die Trendstrategie noch den Verlust. Das Cash-Signal wirkt erst im April und lässt sie dessen Erholung verpassen. Das Long-Signal von Ende Juli gilt erst im August.</p>
````

### Änderung 85: A05

Datei `notebooks/Analyse.ipynb`, Zell-ID `c7f40801`.

Vorher:

````text
<p>VT und BIP-G7 erzielen die höchsten Endvermögen mit nur rund 3’781 USD Abstand über 16 Jahre; ihre Jahresrenditen liegen nahe beieinander. 60/40 und Trend bleiben deutlich darunter.</p>
````

Nachher:

````text
<p>VT und BIP-G7 erzielen die höchsten Endvermögen mit nur rund 3’781 USD Abstand über 16 Jahre; ihre Jahresrenditen liegen nahe beieinander (@fig-h1-vermoegen). 60/40 und Trend bleiben deutlich darunter.</p>
````

### Änderung 86: A05

Datei `notebooks/Analyse.ipynb`, Zell-ID `570e592d`.

Vorher:

````text
<p>60/40 hat in H1 die niedrigste Volatilität (8,93 %), höchste Sharpe (0,685) und den kleinsten MDD (−21,57 %). Trend schwankt weniger als VT, hat aber mit −29,69 % den grössten MDD: Geringere Schwankung bedeutet hier keinen besseren Schutz vor dem stärksten Rückgang.</p>
````

Nachher:

````text
<p>60/40 hat in H1 die niedrigste Volatilität (8,93 %), höchste Sharpe (0,685) und den kleinsten MDD (−21,57 %; @fig-h1-rendite-risiko und @fig-h1-drawdown). Trend schwankt weniger als VT, hat aber mit −29,69 % den grössten MDD: Geringere Schwankung bedeutet hier keinen besseren Schutz vor dem stärksten Rückgang.</p>
````

### Änderung 87: A05

Datei `notebooks/Analyse.ipynb`, Zell-ID `c4dac399`.

Vorher:

````text
<p>BIP-G7 endet rund 146’494 USD über Gleichgewichtung, bei etwas niedrigerer Volatilität/MDD und höherer Sharpe. Gleiche Länderfonds erlauben einen gezielteren Vergleich der Regeln; Marktkapitalisierungsgewichte wurden in K1 nicht untersucht.</p>
````

Nachher:

````text
<p>BIP-G7 endet rund 146’494 USD über Gleichgewichtung, bei etwas niedrigerer Volatilität/MDD und höherer Sharpe (@fig-k1-vermoegen). Gleiche Länderfonds erlauben einen gezielteren Vergleich der Regeln; Marktkapitalisierungsgewichte wurden in K1 nicht untersucht.</p>
````

### Änderung 88: A05

Datei `notebooks/Analyse.ipynb`, Zell-ID `d7d0e101`.

Vorher:

````text
<p>VTI Buy-and-Hold erreicht aus 100’000 USD rund 1,22 Millionen, bei −50,84 % MDD. Zwischen Höchst- und Tiefstand verliert der Monatswert mehr als die Hälfte. Dies bedeutet keinen Endverlust der Hälfte des Startkapitals.</p>
````

Nachher:

````text
<p>VTI Buy-and-Hold erreicht aus 100’000 USD rund 1,22 Millionen, bei −50,84 % MDD (@fig-z1-vermoegen und @fig-z1-drawdown). Zwischen Höchst- und Tiefstand verliert der Monatswert mehr als die Hälfte. Dies bedeutet keinen Endverlust der Hälfte des Startkapitals.</p>
````

### Änderung 89: A05

Datei `notebooks/Analyse.ipynb`, Zell-ID `33d92987`.

Vorher:

````text
<p>6/12 erzielt das höchste Endvermögen. 2/12 und 3/12 haben ähnliche Renditen, aber unterschiedliche MDD. Der gleich gerundete MDD von 2/12 und 6/12 bedeutet keine identischen Verläufe.</p>
````

Nachher:

````text
<p>6/12 erzielt das höchste Endvermögen (@fig-sma-vermoegen). 2/12 und 3/12 haben ähnliche Renditen, aber unterschiedliche MDD. Der gleich gerundete MDD von 2/12 und 6/12 bedeutet keine identischen Verläufe.</p>
````

### Änderung 90: B09: Sharpe als risikoadjustierte Renditekennzahl

Datei `notebooks/Analyse.ipynb`, Zell-ID `6999a6d3`.

Vorher:

````text
<p>Das H1-Endvermögen spräche für BIP-G7 oder VT Buy-and-Hold. Sobald die Schwankungen und Rückgänge einbezogen werden, wird das Bild weniger eindeutig. 60/40 erreicht bei geringerem Ertrag günstigere Werte aller drei Risikokennzahlen als die übrigen H1-Strategien.</p>

````

Nachher:

````text
<p>Das H1-Endvermögen spräche für BIP-G7 oder VT Buy-and-Hold. Sobald die Schwankungen und Rückgänge einbezogen werden, wird das Bild weniger eindeutig. 60/40 erreicht bei geringerem Ertrag die niedrigste Volatilität, den kleinsten maximalen Drawdown und die höchste Sharpe Ratio der H1-Strategien.</p>

````

### Änderung 91: B03

Datei `notebooks/Analyse.ipynb`, Zell-ID `c50744c1`.

Vorher:

````text
Die Engine verbindet die theoretischen Berechnungen, trennt Datenaufbereitung, Strategieregeln, Kennzahlen und Export und soll unterschiedliche geeignete Daten und Einstellungen verarbeiten. Die Entwicklung beginnt mit dem Datenvertrag; die Reihenfolge ist eine Designentscheidung des Autors (@sec-technik-5-2).

Markt-, Zins- und BIP-Daten werden vereinheitlicht und geprüft, Rohdaten getrennt erhalten und Lücken nicht still interpoliert. Datenvertrag, Umwandlung, Aufbereitung und Prüfung stehen in @sec-daten-5-3, @sec-daten-5-4, @sec-daten-5-5 und @sec-pruefung-vor-simulation. Im Lauf werden keine neuen Marktdaten geladen.

Konfiguration, Ergebnisvertrag und Aufbau sind in @sec-technik-5-6, @sec-technik-5-7 und @sec-technik-5-8 dokumentiert. Gewichte und Signale dienen der Interpretation; das Manifest ordnet Daten, Einstellungen und Programmstand zu. Codex unterstützte wesentlich die Integration der vorgegebenen Bausteine und die Erstellung von Tests mit künstlichen Daten; finanzwissenschaftliche Vorgaben und Untersuchungsentscheidungen stammen vom Autor (@sec-technik-5-9).

Feste Daten und Parameter werden vorab gewählt, nicht nachträglich für gewünschte Resultate verändert [@hilpischPythonFinanceMastering2019, S. 697; @kommerSouveraenInvestierenMit2025, S. 607–608].

````

Nachher:

````text
Die Engine verbindet die theoretischen Berechnungen, trennt Datenaufbereitung, Strategieregeln, Kennzahlen und Export und soll unterschiedliche geeignete Daten und Einstellungen verarbeiten. Die Entwicklung beginnt mit dem Datenvertrag; die Reihenfolge ist eine Designentscheidung des Autors (@sec-technik-5-2).

Markt-, Zins- und BIP-Daten werden vereinheitlicht und geprüft, Rohdaten getrennt erhalten und Lücken nicht still interpoliert. Datenvertrag, Umwandlung, Aufbereitung und Prüfung stehen in @sec-daten-5-3, @sec-daten-5-4, @sec-daten-5-5 und @sec-pruefung-vor-simulation. Im Lauf werden keine neuen Marktdaten geladen.

Konfiguration, Ergebnisvertrag und Aufbau sind in @sec-technik-5-6, @sec-technik-5-7 und @sec-technik-5-8 dokumentiert. Gewichte und Signale dienen der Interpretation; das Manifest ordnet Daten, Einstellungen und Programmstand zu. Codex unterstützte wesentlich die Integration der vorgegebenen Bausteine und die Erstellung von Tests mit künstlichen Daten; finanzwissenschaftliche Vorgaben und Untersuchungsentscheidungen stammen vom Autor (@sec-technik-5-9).

Feste Daten und Parameter werden vorab gewählt, nicht nachträglich für gewünschte Resultate verändert [@hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization» und «Overfitting», PDF-S. 698–699; @kommerSouveraenInvestierenMit2025, S. 607–608].

````

### Änderung 92: B03

Datei `notebooks/Analyse.ipynb`, Zell-ID `762a3ac1`.

Vorher:

````text
Vorgesehen ist Engine 1.0.0 (Git-Tag engine-v1.0) mit dokumentierten Prüfungen. Daten und Parameter wählt der Autor; die Quellen begründen Konzepte, nicht genau diese Ticker, Zeiträume oder Einstellungen.

Zur Forschungsfrage in Abschnitt 2.2 beurteilt die Untersuchung unterschiedliche Aspekte mit Rendite, Volatilität, Sharpe und MDD [@kommerSouveraenInvestierenMit2025, Abschnitt 2.2]. Hauptparameter stehen vorab fest, statt günstige Ergebnisse nachträglich zu suchen [@kommerSouveraenInvestierenMit2025, Glossar «Data Snooping»; @hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization»].

````

Nachher:

````text
Vorgesehen ist Engine 1.0.0 (Git-Tag engine-v1.0) mit dokumentierten Prüfungen. Daten und Parameter wählt der Autor; die Quellen begründen Konzepte, nicht genau diese Ticker, Zeiträume oder Einstellungen.

Zur Forschungsfrage in Abschnitt 2.2 beurteilt die Untersuchung unterschiedliche Aspekte mit Rendite, Volatilität, Sharpe und MDD [@kommerSouveraenInvestierenMit2025, Abschnitt 2.2]. Hauptparameter stehen vorab fest, statt günstige Ergebnisse nachträglich zu suchen [@kommerSouveraenInvestierenMit2025, Glossar «Data Snooping»; @hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization» und «Overfitting», PDF-S. 698–699].

````

### Änderung 93: B03

Datei `notebooks/Analyse.ipynb`, Zell-ID `4001dccf`.

Vorher:

````text
<p>Der bessere historische 6/12-Wert ersetzt die Hauptvariante nicht. Die Zusatzläufe zeigen Parameterempfindlichkeit. Eine historisch erfolgreiche Kombination muss auf anderen Daten oder in der Praxis nicht ebenso gut funktionieren [@hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization»]. Drei Varianten sind eine begrenzte Sensitivitätsprüfung, keine Suche nach einem allgemein optimalen SMA.</p>
````

Nachher:

````text
<p>Der bessere historische 6/12-Wert ersetzt die Hauptvariante nicht. Die Zusatzläufe zeigen Parameterempfindlichkeit. Eine historisch erfolgreiche Kombination muss auf anderen Daten oder in der Praxis nicht ebenso gut funktionieren [@hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization» und «Overfitting», PDF-S. 698–699]. Drei Varianten sind eine begrenzte Sensitivitätsprüfung, keine Suche nach einem allgemein optimalen SMA.</p>
````

### Änderung 94: Weitere Redaktion, Prüfbericht S. 12: aktuelle Methodik statt historische Planung

Datei `notebooks/Analyse.ipynb`, Zell-ID `762a3ac1`.

Vorher:

````text
Vorgesehen ist Engine 1.0.0 (Git-Tag engine-v1.0) mit dokumentierten Prüfungen. Daten und Parameter wählt der Autor; die Quellen begründen Konzepte, nicht genau diese Ticker, Zeiträume oder Einstellungen.

Zur Forschungsfrage in Abschnitt 2.2 beurteilt die Untersuchung unterschiedliche Aspekte mit Rendite, Volatilität, Sharpe und MDD [@kommerSouveraenInvestierenMit2025, Abschnitt 2.2]. Hauptparameter stehen vorab fest, statt günstige Ergebnisse nachträglich zu suchen [@kommerSouveraenInvestierenMit2025, Glossar «Data Snooping»; @hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization» und «Overfitting», PDF-S. 698–699].

````

Nachher:

````text
Verwendet wurde Engine 1.0.0 (Git-Tag engine-v1.0) mit dokumentierten Prüfungen. Daten und Parameter wählt der Autor; die Quellen begründen Konzepte, nicht genau diese Ticker, Zeiträume oder Einstellungen.

Zur Forschungsfrage in Abschnitt 2.2 beurteilt die Untersuchung unterschiedliche Aspekte mit Rendite, Volatilität, Sharpe und MDD [@kommerSouveraenInvestierenMit2025, Abschnitt 2.2]. Hauptparameter stehen vorab fest, statt günstige Ergebnisse nachträglich zu suchen [@kommerSouveraenInvestierenMit2025, Glossar «Data Snooping»; @hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization» und «Overfitting», PDF-S. 698–699].

````

### Änderung 95: Weitere Redaktion, Prüfbericht S. 12: aktuelle Methodik statt historische Planung

Datei `notebooks/Analyse.ipynb`, Zell-ID `e3ace74b`.

Vorher:

````text
<p>Für den Sharpe-Vergleich wird die FRED-Reihe <code>DGS3MO</code> vorgeschlagen. Sie enthält täglich notierte Renditen dreimonatiger US-Treasuries auf Investmentbasis und wird in Prozent angegeben [@MarketYieldUS2026]. Diese Reihe ist <strong>noch keine monatliche Anlagerendite</strong> und darf deshalb nicht unverändert in den Risk-Free-Eingang der Engine geschrieben werden.
````

Nachher:

````text
<p>Für den Sharpe-Vergleich wird die FRED-Reihe <code>DGS3MO</code> verwendet. Sie enthält täglich notierte Renditen dreimonatiger US-Treasuries auf Investmentbasis und wird in Prozent angegeben [@MarketYieldUS2026]. Diese Reihe ist <strong>noch keine monatliche Anlagerendite</strong> und darf deshalb nicht unverändert in den Risk-Free-Eingang der Engine geschrieben werden.
````

### Änderung 96: A03

Datei `_quarto.yml`, Zell-ID ``.

Vorher:

````text
    documentclass: scrreprt


````

Nachher:

````text
    documentclass: scrreprt

    lof: true

    lot: true


````

### Änderung 97: A03

Datei `_quarto.yml`, Zell-ID ``.

Vorher:

````text
      - numbers=noenddot


````

Nachher:

````text
      - numbers=noenddot

      - listof=totoc


````

### Änderung 98: A02

Datei `_quarto.yml`, Zell-ID ``.

Vorher:

````text
    include-in-header:

      text: |


````

Nachher:

````text
    include-in-header:

      text: |

        \titlehead{Kantonsschule Büelrain Winterthur}

        \subject{Maturitätsarbeit}

        \publishers{\normalsize Klasse 4gW\\Betreuung: Jacques Mock}


````

## Änderungen an Bibliografie und Zitierstil

Die Kennzeichnungen KI-01 bis KI-45 stammen aus den bereits explizit dokumentierten Quellenkontexten. Sie sind redaktionelle Arbeitstitel. Die folgende Matrix bewahrt auch die vorherigen Werte der gezielt ersetzten IMF2009-URL und ihres Zugriffdatums.

````json
[
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhalt",
    "kennung": "KI-01",
    "title": "KI-01: Engine-Planung und Audit-Ablauf",
    "url": "https://chatgpt.com/s/t_6acd8441b0fc81918f751e8eb334a2cc",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-02",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhalta",
    "kennung": "KI-02",
    "title": "KI-02: Engine-Planung und Audit-Ablauf",
    "url": "https://chatgpt.com/s/t_6acd84c0f1748191b6431744f2b3886b",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-02",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltb",
    "kennung": "KI-03",
    "title": "KI-03: Engine-Planung und Audit-Ablauf",
    "url": "https://chatgpt.com/s/t_6acd851e7d7881918b55b8a1931af8a9",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-02",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltc",
    "kennung": "KI-04",
    "title": "KI-04: Engine-Planung und Audit-Ablauf",
    "url": "https://chatgpt.com/s/t_6acd857650848191834bc1a507108c38",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-02",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltd",
    "kennung": "KI-05",
    "title": "KI-05: Engine-Planung und Audit-Ablauf",
    "url": "https://chatgpt.com/s/t_6acd86090c7c8191ae2ee2c950c41b57",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-02",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhalte",
    "kennung": "KI-06",
    "title": "KI-06: Engine-Planung und Audit-Ablauf",
    "url": "https://chatgpt.com/s/t_6acd867ccf3c81918d2111ca1a6d0909",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-02",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltf",
    "kennung": "KI-07",
    "title": "KI-07: Kernimplementierung: Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd869b5a9c8191870f50d701c06cc1",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-03",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltg",
    "kennung": "KI-08",
    "title": "KI-08: Kernimplementierung: Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd86de8c2481919f9cd9bc933db1ac",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-03",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhalth",
    "kennung": "KI-09",
    "title": "KI-09: Kernimplementierung: Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd86fe9af481919cc18b1eaffe62d0",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-03",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhalti",
    "kennung": "KI-10",
    "title": "KI-10: Kernimplementierung: Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd870fc7c48191a9fde49f87e389f2",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-03",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltj",
    "kennung": "KI-11",
    "title": "KI-11: Rebalancing: Auftrag, Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd8728159c819181c4b11407d9612a",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltk",
    "kennung": "KI-12",
    "title": "KI-12: Rebalancing: Auftrag, Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd873acedc8191afa783c17195e04d",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltl",
    "kennung": "KI-13",
    "title": "KI-13: Rebalancing: Auftrag, Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd877bc82481919581e8bcf9a5027c",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltm",
    "kennung": "KI-14",
    "title": "KI-14: Rebalancing: Auftrag, Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd878f254c8191b0a8d33b9c2394d8",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltn",
    "kennung": "KI-15",
    "title": "KI-15: SMA-Trendfolge: Auftrag, Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd8b35011c8191b7f36a01b167de4a",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhalto",
    "kennung": "KI-16",
    "title": "KI-16: SMA-Trendfolge: Auftrag, Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd8b48605c8191b4bb390f8aabc5b1",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltp",
    "kennung": "KI-17",
    "title": "KI-17: SMA-Trendfolge: Auftrag, Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd8b567704819191935cd2baf30030",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltq",
    "kennung": "KI-18",
    "title": "KI-18: SMA-Trendfolge: Auftrag, Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd8b69f28c8191b5407ddb25ab6506",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltr",
    "kennung": "KI-19",
    "title": "KI-19: BIP-Gewichtung: Auftrag, Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd8b8235648191ab881e49cb4dfcc0",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhalts",
    "kennung": "KI-20",
    "title": "KI-20: BIP-Gewichtung: Auftrag, Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd8b97fbb8819190ba29eef74ebfc0",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltt",
    "kennung": "KI-21",
    "title": "KI-21: BIP-Gewichtung: Auftrag, Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd8bc54d78819192d15265a65bd880",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltu",
    "kennung": "KI-22",
    "title": "KI-22: BIP-Gewichtung: Auftrag, Kontrollen und Review",
    "url": "https://chatgpt.com/s/t_6acd8bd881c881918da6540384acc7d0",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltv",
    "kennung": "KI-23",
    "title": "KI-23: Engine-Gesamtaudit und Blocker",
    "url": "https://chatgpt.com/s/t_6acd8bf2ddf88191855f52573868cfe5",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltw",
    "kennung": "KI-24",
    "title": "KI-24: Engine-Gesamtaudit und Blocker",
    "url": "https://chatgpt.com/s/t_6acd8c071d688191a35d8a08773a409c",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltx",
    "kennung": "KI-25",
    "title": "KI-25: Blocker- und Portfoliozustandskorrekturen",
    "url": "https://chatgpt.com/s/t_6acd8c19d8388191b20ba6a135b7d196",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhalty",
    "kennung": "KI-26",
    "title": "KI-26: Blocker- und Portfoliozustandskorrekturen",
    "url": "https://chatgpt.com/s/t_6acd8c2de0708191bb233e4f7afc157b",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltz",
    "kennung": "KI-27",
    "title": "KI-27: Blocker- und Portfoliozustandskorrekturen",
    "url": "https://chatgpt.com/s/t_6acd8c44a9a48191ac15d84e954e3c3e",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltaa",
    "kennung": "KI-28",
    "title": "KI-28: Blocker- und Portfoliozustandskorrekturen",
    "url": "https://chatgpt.com/s/t_6acd8c57a66c8191b16bc21ee0532b05",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltab",
    "kennung": "KI-29",
    "title": "KI-29: Blocker- und Portfoliozustandskorrekturen",
    "url": "https://chatgpt.com/s/t_6acd8c7267c48191bba7a927ff307f98",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltac",
    "kennung": "KI-30",
    "title": "KI-30: Blocker- und Portfoliozustandskorrekturen",
    "url": "https://chatgpt.com/s/t_6acd8c813cd48191b35fabd10aea02b8",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltad",
    "kennung": "KI-31",
    "title": "KI-31: Re-Audit und CSV-NUL-Korrektur",
    "url": "https://chatgpt.com/s/t_6acd8c96f5c081918b851992aa3f43ac",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltae",
    "kennung": "KI-32",
    "title": "KI-32: Re-Audit und CSV-NUL-Korrektur",
    "url": "https://chatgpt.com/s/t_6acd8ca720508191a30c5abacf74a4ba",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltaf",
    "kennung": "KI-33",
    "title": "KI-33: Re-Audit und CSV-NUL-Korrektur",
    "url": "https://chatgpt.com/s/t_6acd8ccc4dc48191b55fe2bbbc9ac5c5",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltag",
    "kennung": "KI-34",
    "title": "KI-34: Re-Audit und CSV-NUL-Korrektur",
    "url": "https://chatgpt.com/s/t_6acd8cddc6e481918e85ba761be09802",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltah",
    "kennung": "KI-35",
    "title": "KI-35: Freeze-Re-Audit und Release-Prüfung",
    "url": "https://chatgpt.com/s/t_6acd8cefd8b881919ee1b191bfd1b554",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltai",
    "kennung": "KI-36",
    "title": "KI-36: Freeze-Re-Audit und Release-Prüfung",
    "url": "https://chatgpt.com/s/t_6acd8cfc67b481919d5728be71b9adfe",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltaj",
    "kennung": "KI-37",
    "title": "KI-37: Freeze-Re-Audit und Release-Prüfung",
    "url": "https://chatgpt.com/s/t_6acd8d0b53048191a5dab58096e2e540",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltak",
    "kennung": "KI-38",
    "title": "KI-38: Freeze-Re-Audit und Release-Prüfung",
    "url": "https://chatgpt.com/s/t_6acd8d179ea48191a85fa762da686595",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltal",
    "kennung": "KI-39",
    "title": "KI-39: Freeze-Re-Audit und Release-Prüfung",
    "url": "https://chatgpt.com/s/t_6acd8d3437ac81919e8220fefc55d992",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltam",
    "kennung": "KI-40",
    "title": "KI-40: Freeze-Re-Audit und Release-Prüfung",
    "url": "https://chatgpt.com/s/t_6acd8d620e4881919698680a05a0f0c4",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-04",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltao",
    "kennung": "KI-41",
    "title": "KI-41: Prüfung der ETF- und Zinsrohdaten",
    "url": "https://chatgpt.com/s/t_6acd98ec15f88191b6b7108cd5a58da0",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-08",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltan",
    "kennung": "KI-42",
    "title": "KI-42: Prüfung der historischen WEO-Rohdaten",
    "url": "https://chatgpt.com/s/t_6acd9b6c4aac8191b733f8cb425fc218",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-09",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltap",
    "kennung": "KI-43",
    "title": "KI-43: Prüfung der aufbereiteten Study-v1-Daten",
    "url": "https://chatgpt.com/s/t_6acda7ebe8608191acca957223db0fa0",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-10",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltaq",
    "kennung": "KI-44",
    "title": "KI-44: Prüfung des Study-v1-Freeze-Archivs",
    "url": "https://chatgpt.com/s/t_6acda86619608191a7289c979bcfe389",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-10",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "A06",
    "key": "ChatGPTGeteilterInhaltar",
    "kennung": "KI-45",
    "title": "KI-45: Prüfung der Backtestergebnisse H1/K1/Z1/S1/S2",
    "url": "https://chatgpt.com/s/t_6acda9395eac8191ae1a12850817f3a7",
    "kontextdatum_aus_historischem_nachtrag": "2026-10-10",
    "abfragedatum": "nicht neu rekonstruiert; vorhandenes Abrufdatum 2026-10-13 erhalten",
    "titelherkunft": "redaktionell nach ausdrücklicher Cite-Key-/URL-Zuordnung im historischen Nachtrag und KI-Anhang"
  },
  {
    "befund": "B11",
    "key": "yahooYahooFinanzenDeutschlandBoerse2026",
    "aenderung": "Importierten Seitentitel um fehlendes Leerzeichen bereinigt.",
    "vorher": "  title = {Yahoo FinanzenDeutschland | Börse live, Kurse, Nachrichten aus Wirtschafts- und Finanzwelt},\n  author = {{Yahoo}},\n  date = {2026-06-07},\n  url = {https://de.finance.yahoo.com/},\n  urldate = {2026-06-07},\n  abstract = {Yahoo Finanzen bietet Ihnen kostenlose Aktienkurse, topaktuelle Nachrichten, Portfolio-Management-Ressourcen, internationale Marktdaten, soziale Interaktion und Hypothekensätze, damit Sie Ihre Finanzen besser verwalten können.},\n  langid = {german},\n  organization = {Yahoo Finance},\n  file = {C:\\Users\\modic\\Zotero\\storage\\EZ6DTU9M\\de.finance.yahoo.com.html}",
    "nachher": "  title = {Yahoo Finanzen Deutschland | Börse live, Kurse, Nachrichten aus Wirtschafts- und Finanzwelt},\n  author = {{Yahoo}},\n  date = {2026-06-07},\n  url = {https://de.finance.yahoo.com/},\n  urldate = {2026-06-07},\n  abstract = {Yahoo Finanzen bietet Ihnen kostenlose Aktienkurse, topaktuelle Nachrichten, Portfolio-Management-Ressourcen, internationale Marktdaten, soziale Interaktion und Hypothekensätze, damit Sie Ihre Finanzen besser verwalten können.},\n  langid = {german},\n  organization = {Yahoo Finance},\n  file = {C:\\Users\\modic\\Zotero\\storage\\EZ6DTU9M\\de.finance.yahoo.com.html}"
  },
  {
    "befund": "C07",
    "key": "WorldEconomicOutlook",
    "aenderung": "Ausgabe Oktober 2024 aus bereits vorhandener URL eindeutig im Titel benannt; Daten nicht umgedeutet.",
    "vorher": "  title = {World {{Economic Outlook}} ({{WEO}}) {{Database}}},\n  url = {https://www.imf.org/en/publications/weo/weo-database/2024/october/download-entire-database},\n  urldate = {2026-10-07},\n  abstract = {Use this database to find data on national accounts, inflation, unemployment rates, balance of payments, fiscal indicators, trade for countries and country groups (aggregates), and commodity prices whose data are reported by the IMF.},\n  langid = {english},\n  organization = {IMF}",
    "nachher": "  title = {World {{Economic Outlook}} ({{WEO}}) {{Database}}, {{October}} 2024},\n  url = {https://www.imf.org/en/publications/weo/weo-database/2024/october/download-entire-database},\n  urldate = {2026-10-07},\n  abstract = {Use this database to find data on national accounts, inflation, unemployment rates, balance of payments, fiscal indicators, trade for countries and country groups (aggregates), and commodity prices whose data are reported by the IMF.},\n  langid = {english},\n  organization = {IMF}"
  },
  {
    "befund": "C07",
    "key": "PandasDataFrameresamplePandas305",
    "aenderung": "Zuständiges Dokumentationsprojekt ergänzt, vorhandene Version und Zugriff erhalten.",
    "vorher": "  title = {Pandas.{{DataFrame}}.Resample — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html},\n  urldate = {2026-08-04},\n  file = {C:\\Users\\modic\\Zotero\\storage\\D2VN33DA\\pandas.DataFrame.resample.html}",
    "nachher": "  author = {{pandas development team}},\n  title = {Pandas.{{DataFrame}}.Resample — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html},\n  urldate = {2026-08-04},\n  file = {C:\\Users\\modic\\Zotero\\storage\\D2VN33DA\\pandas.DataFrame.resample.html}"
  },
  {
    "befund": "C07",
    "key": "PandasDataFrameset_indexPandas305",
    "aenderung": "Zuständiges Dokumentationsprojekt ergänzt, vorhandene Version und Zugriff erhalten.",
    "vorher": "  title = {Pandas.{{DataFrame}}.Set\\_index — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index},\n  urldate = {2026-08-04},\n  file = {C:\\Users\\modic\\Zotero\\storage\\SJURHQ85\\pandas.DataFrame.set_index.html}",
    "nachher": "  author = {{pandas development team}},\n  title = {Pandas.{{DataFrame}}.Set\\_index — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index},\n  urldate = {2026-08-04},\n  file = {C:\\Users\\modic\\Zotero\\storage\\SJURHQ85\\pandas.DataFrame.set_index.html}"
  },
  {
    "befund": "C07",
    "key": "PandasSeriescummaxPandas305",
    "aenderung": "Zuständiges Dokumentationsprojekt ergänzt, vorhandene Version und Zugriff erhalten.",
    "vorher": "  title = {Pandas.{{Series}}.Cummax — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/docs/reference/api/pandas.Series.cummax.html#pandas.Series.cummax},\n  urldate = {2026-08-06},\n  file = {C:\\Users\\modic\\Zotero\\storage\\6K3KDU6D\\pandas.Series.cummax.html}",
    "nachher": "  author = {{pandas development team}},\n  title = {Pandas.{{Series}}.Cummax — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/docs/reference/api/pandas.Series.cummax.html#pandas.Series.cummax},\n  urldate = {2026-08-06},\n  file = {C:\\Users\\modic\\Zotero\\storage\\6K3KDU6D\\pandas.Series.cummax.html}"
  },
  {
    "befund": "C07",
    "key": "PandasSeriescumprodPandas305",
    "aenderung": "Zuständiges Dokumentationsprojekt ergänzt, vorhandene Version und Zugriff erhalten.",
    "vorher": "  title = {Pandas.{{Series}}.Cumprod — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/docs/reference/api/pandas.Series.cumprod.html#pandas.Series.cumprod},\n  urldate = {2026-08-06},\n  file = {C:\\Users\\modic\\Zotero\\storage\\DW76AAWB\\pandas.Series.cumprod.html}",
    "nachher": "  author = {{pandas development team}},\n  title = {Pandas.{{Series}}.Cumprod — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/docs/reference/api/pandas.Series.cumprod.html#pandas.Series.cumprod},\n  urldate = {2026-08-06},\n  file = {C:\\Users\\modic\\Zotero\\storage\\DW76AAWB\\pandas.Series.cumprod.html}"
  },
  {
    "befund": "C07",
    "key": "PandasSeriesdiffPandas305",
    "aenderung": "Zuständiges Dokumentationsprojekt ergänzt, vorhandene Version und Zugriff erhalten.",
    "vorher": "  title = {Pandas.{{Series}}.Diff — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.diff.html#pandas.Series.diff},\n  urldate = {2026-08-04}",
    "nachher": "  author = {{pandas development team}},\n  title = {Pandas.{{Series}}.Diff — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.diff.html#pandas.Series.diff},\n  urldate = {2026-08-04}"
  },
  {
    "befund": "C07",
    "key": "PandasSeriesminPandas305",
    "aenderung": "Zuständiges Dokumentationsprojekt ergänzt, vorhandene Version und Zugriff erhalten.",
    "vorher": "  title = {Pandas.{{Series}}.Min — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min},\n  urldate = {2026-08-06},\n  file = {C:\\Users\\modic\\Zotero\\storage\\BDLAKU9P\\pandas.Series.min.html}",
    "nachher": "  author = {{pandas development team}},\n  title = {Pandas.{{Series}}.Min — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min},\n  urldate = {2026-08-06},\n  file = {C:\\Users\\modic\\Zotero\\storage\\BDLAKU9P\\pandas.Series.min.html}"
  },
  {
    "befund": "C07",
    "key": "PandasSeriespct_changePandas305",
    "aenderung": "Zuständiges Dokumentationsprojekt ergänzt, vorhandene Version und Zugriff erhalten.",
    "vorher": "  title = {Pandas.{{Series}}.Pct\\_change — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.pct_change.html#pandas.Series.pct_change},\n  urldate = {2026-08-04},\n  file = {C:\\Users\\modic\\Zotero\\storage\\2KT95RAC\\pandas.Series.pct_change.html}",
    "nachher": "  author = {{pandas development team}},\n  title = {Pandas.{{Series}}.Pct\\_change — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.pct_change.html#pandas.Series.pct_change},\n  urldate = {2026-08-04},\n  file = {C:\\Users\\modic\\Zotero\\storage\\2KT95RAC\\pandas.Series.pct_change.html}"
  },
  {
    "befund": "C07",
    "key": "PandasSeriesstdPandas305",
    "aenderung": "Zuständiges Dokumentationsprojekt ergänzt, vorhandene Version und Zugriff erhalten.",
    "vorher": "  title = {Pandas.{{Series}}.Std — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html},\n  urldate = {2026-08-07},\n  file = {C:\\Users\\modic\\Zotero\\storage\\RUMMQIXI\\pandas.Series.std.html}",
    "nachher": "  author = {{pandas development team}},\n  title = {Pandas.{{Series}}.Std — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html},\n  urldate = {2026-08-07},\n  file = {C:\\Users\\modic\\Zotero\\storage\\RUMMQIXI\\pandas.Series.std.html}"
  },
  {
    "befund": "C07",
    "key": "Pandasto_datetimePandas305",
    "aenderung": "Zuständiges Dokumentationsprojekt ergänzt, vorhandene Version und Zugriff erhalten.",
    "vorher": "  title = {Pandas.To\\_datetime — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime},\n  urldate = {2026-08-04},\n  file = {C:\\Users\\modic\\Zotero\\storage\\Y6RWCA9H\\pandas.to_datetime.html}",
    "nachher": "  author = {{pandas development team}},\n  title = {Pandas.To\\_datetime — Pandas 3.0.5 Documentation},\n  url = {https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime},\n  urldate = {2026-08-04},\n  file = {C:\\Users\\modic\\Zotero\\storage\\Y6RWCA9H\\pandas.to_datetime.html}"
  },
  {
    "befund": "C07",
    "key": "MarketYieldUS2026",
    "aenderung": "Datenquelleninstitution und FRED-Bereitsteller nach offizieller Serienseite ergänzt; historische Daten erhalten.",
    "vorher": "  title = {Market {{Yield}} on {{U}}.{{S}}. {{Treasury Securities}} at 3-{{Month Constant Maturity}}, {{Quoted}} on an {{Investment Basis}}},\n  date = {2026-10-07},\n  url = {https://fred.stlouisfed.org/series/DGS3MO},\n  urldate = {2026-10-07},\n  abstract = {Graph and download economic data for Market Yield on U.S. Treasury Securities at 3-Month Constant Maturity, Quoted on an Investment Basis (DGS3MO) from 1981-09-01 to 2026-10-06 about bills, 3-month, maturity, Treasury, interest rate, interest, rate, and USA.},\n  langid = {english},\n  file = {C:\\Users\\modic\\Zotero\\storage\\T4K7FLI5\\DGS3MO.html}",
    "nachher": "  author = {{Board of Governors of the Federal Reserve System (US)}},\n  organization = {Federal Reserve Bank of St. Louis},\n  title = {Market {{Yield}} on {{U}}.{{S}}. {{Treasury Securities}} at 3-{{Month Constant Maturity}}, {{Quoted}} on an {{Investment Basis}}},\n  date = {2026-10-07},\n  url = {https://fred.stlouisfed.org/series/DGS3MO},\n  urldate = {2026-10-07},\n  abstract = {Graph and download economic data for Market Yield on U.S. Treasury Securities at 3-Month Constant Maturity, Quoted on an Investment Basis (DGS3MO) from 1981-09-01 to 2026-10-06 about bills, 3-month, maturity, Treasury, interest rate, interest, rate, and USA.},\n  langid = {english},\n  file = {C:\\Users\\modic\\Zotero\\storage\\T4K7FLI5\\DGS3MO.html}"
  },
  {
    "befund": "C07",
    "key": "FederalReserveBoard",
    "aenderung": "Im Titel und der offiziellen Domain bezeichnete Institution ergänzt; Ausgabedatum im Titel nicht umgedeutet.",
    "vorher": "  title = {Federal {{Reserve Board}} - {{H}}.15 - {{Selected Interest Rates}} ({{Daily}}) - {{October}} 07, 2026},\n  date = {2026-10-08},\n  url = {https://www.federalreserve.gov/releases/h15/},\n  urldate = {2026-10-07},\n  abstract = {The Federal Reserve Board of Governors in Washington DC.},\n  langid = {english},\n  file = {C:\\Users\\modic\\Zotero\\storage\\LMJRDI8R\\h15.html}",
    "nachher": "  author = {{Board of Governors of the Federal Reserve System}},\n  title = {Federal {{Reserve Board}} - {{H}}.15 - {{Selected Interest Rates}} ({{Daily}}) - {{October}} 07, 2026},\n  date = {2026-10-08},\n  url = {https://www.federalreserve.gov/releases/h15/},\n  urldate = {2026-10-07},\n  abstract = {The Federal Reserve Board of Governors in Washington DC.},\n  langid = {english},\n  file = {C:\\Users\\modic\\Zotero\\storage\\LMJRDI8R\\h15.html}"
  },
  {
    "befund": "C07",
    "key": "Preise",
    "aenderung": "Institution aus offizieller BFS-Domain ergänzt; kein erfundener Detailbeleg und kein rückdatiertes Abrufdatum.",
    "vorher": "  title = {Preise},\n  url = {https://www.bfs.admin.ch/content/bfs/de/home/statistiken/preise.html},\n  urldate = {2026-08-04},\n  abstract = {Die Preisstatistik liefert Konjunkturindikatoren zur Preisentwicklung und zum Preisniveau der Waren und Dienstleistungen in der schweizerischen Volkswirtschaft.},\n  langid = {ngerman},\n  file = {C:\\Users\\modic\\Zotero\\storage\\8NRJRVVL\\preise.html}",
    "nachher": "  author = {{Bundesamt für Statistik}},\n  title = {Preise},\n  url = {https://www.bfs.admin.ch/content/bfs/de/home/statistiken/preise.html},\n  urldate = {2026-08-04},\n  abstract = {Die Preisstatistik liefert Konjunkturindikatoren zur Preisentwicklung und zum Preisniveau der Waren und Dienstleistungen in der schweizerischen Volkswirtschaft.},\n  langid = {ngerman},\n  file = {C:\\Users\\modic\\Zotero\\storage\\8NRJRVVL\\preise.html}"
  },
  {
    "befund": "C07",
    "key": "DownloadEntireWorld",
    "aenderung": "IMF als verantwortliche Institution explizit ergänzt; vorhandene Datumsfelder erhalten.",
    "vorher": "  title = {Download Entire {{World Economic Outlook}} Database, {{October}} 2009},\n  date = {2026-10-08},\n  url = {https://www.imf.org/en/publications/weo/weo-database/2009/october/download-entire-database},\n  urldate = {2026-10-07},\n  langid = {english},\n  organization = {IMF},\n  file = {C:\\Users\\modic\\Zotero\\storage\\7XBJ2UM7\\download-entire-database.html}",
    "nachher": "  author = {{International Monetary Fund}},\n  title = {Download Entire {{World Economic Outlook}} Database, {{October}} 2009},\n  date = {2026-10-08},\n  url = {https://www.imf.org/en/publications/weo/weo-database/2009/october/download-entire-database},\n  urldate = {2026-10-07},\n  langid = {english},\n  organization = {IMF},\n  file = {C:\\Users\\modic\\Zotero\\storage\\7XBJ2UM7\\download-entire-database.html}"
  },
  {
    "befund": "C07",
    "key": "WorldEconomicOutlook",
    "aenderung": "IMF als verantwortliche Institution explizit ergänzt; vorhandene Datumsfelder erhalten.",
    "vorher": "  title = {World {{Economic Outlook}} ({{WEO}}) {{Database}}, {{October}} 2024},\n  url = {https://www.imf.org/en/publications/weo/weo-database/2024/october/download-entire-database},\n  urldate = {2026-10-07},\n  abstract = {Use this database to find data on national accounts, inflation, unemployment rates, balance of payments, fiscal indicators, trade for countries and country groups (aggregates), and commodity prices whose data are reported by the IMF.},\n  langid = {english},\n  organization = {IMF}",
    "nachher": "  author = {{International Monetary Fund}},\n  title = {World {{Economic Outlook}} ({{WEO}}) {{Database}}, {{October}} 2024},\n  url = {https://www.imf.org/en/publications/weo/weo-database/2024/october/download-entire-database},\n  urldate = {2026-10-07},\n  abstract = {Use this database to find data on national accounts, inflation, unemployment rates, balance of payments, fiscal indicators, trade for countries and country groups (aggregates), and commodity prices whose data are reported by the IMF.},\n  langid = {english},\n  organization = {IMF}"
  },
  {
    "befund": "C07",
    "key": "WorldEconomicOutlooka",
    "aenderung": "IMF als verantwortliche Institution explizit ergänzt; vorhandene Datumsfelder erhalten.",
    "vorher": "  title = {World {{Economic Outlook}} ({{WEO}}) - {{Frequently Asked Questions}}},\n  url = {https://www.imf.org/en/publications/weo/frequently-asked-questions},\n  urldate = {2026-10-07},\n  abstract = {Frequently Asked Questions (FAQs) are divided into four topics. Click on the corresponding question to view the answers. Submit all other questions and comments using WEO Data Question Form.},\n  langid = {english},\n  organization = {IMF}",
    "nachher": "  author = {{International Monetary Fund}},\n  title = {World {{Economic Outlook}} ({{WEO}}) - {{Frequently Asked Questions}}},\n  url = {https://www.imf.org/en/publications/weo/frequently-asked-questions},\n  urldate = {2026-10-07},\n  abstract = {Frequently Asked Questions (FAQs) are divided into four topics. Click on the corresponding question to view the answers. Submit all other questions and comments using WEO Data Question Form.},\n  langid = {english},\n  organization = {IMF}"
  },
  {
    "befund": "B11",
    "key": "WhatAdjustedClose",
    "aenderung": "Vorhandenen korrekten Titel durch zusätzliche BibTeX-Schutzklammern erhalten; so entsteht im LaTeX-Beleg Close?} statt Close?` und die Ligatur zu invertiertem Fragezeichen wird verhindert. Sichtbarer Titel bleibt What Is the Adjusted Close?.",
    "vorher": "title = {What Is the Adjusted Close?}",
    "nachher": "title = {{What Is the Adjusted Close?}}",
    "pruefung": "Pandoc citeproc -> LaTeX: Titel wird innerhalb der Zitatzeichen als eigene Gruppe ausgegeben."
  },
  {
    "befund": "A07",
    "key": "pandasReleaseNotes2202024",
    "aenderung": "Neue vollständige Quelle für pandas 2.2.0 Release Notes vom 19.01.2024; zuständiges Projekt; direkter Offset-Alias-Abschnitt; tatsächlicher Zugriff 31.10.2026.",
    "url": "https://pandas.pydata.org/docs/whatsnew/v2.2.0.html#deprecate-aliases-m-q-y-etc-in-favour-of-me-qe-ye-etc-for-offsets",
    "pruefung": "Live-Primärquelle bestätigt M -> ME, Q -> QE, Y -> YE."
  },
  {
    "befund": "B01/B12",
    "key": "sharpe1994ExPost",
    "aenderung": "Original-Autorenfassung von The Sharpe Ratio (1994), Stanford University, mit tatsächlichem Zugriff 31.10.2026 ergänzt. Die vorhandene 2021-Sammelbandfassung blieb für historische Zuordnung erhalten.",
    "url": "https://web.stanford.edu/~wfsharpe/art/sr/SR.htm",
    "pruefung": "Live-Primärquelle: The Ex Post Sharpe Ratio, AVERAGE/STDEV der Differenzrenditen; Time Dependence erläutert Annualisierung und Annahmen."
  },
  {
    "befund": "KI-Nachweis",
    "key": "chatgptSchlussbeurteilung20261031",
    "aenderung": "Vom Autor genannter ChatGPT-Chat der Schlussbeurteilung als KI-46 eindeutig aufgenommen.",
    "url": "https://chatgpt.com/share/6ae63fdb-e3b0-83eb-8465-345769041156",
    "pruefung": "Öffentlicher Webabruf liefert Seitentitel ChatGPT - Prüfbericht Maturarbeit, dynamischer Gesprächsinhalt im Werkzeug nicht auslesbar; bereitgestellter Bericht/Paste Grundlage der Befunde."
  },
  {
    "befund": "C07",
    "datei": "styles/chicago-shortened-notes-bibliography-17th-edition.csl",
    "aenderung": "Vorhandenes tatsächliches accessed für Webpages und Software auch bei vorhandenem issued im Literaturverzeichnis ausgeben; keine erfundenen oder rückdatierten Zugriffe. Andere Dokumenttypen behalten DOI-/Publikationspriorität.",
    "pruefung": "Pandoc-Proben bestätigen Webdatum 31.10.2026 und Softwarezugriff 06.08.2026 neben Publikationsdaten."
  },
  {
    "befund": "B12/A06",
    "datei": "styles/chicago-shortened-notes-bibliography-17th-edition.csl",
    "aenderung": "Kurztitel auch in unmittelbar wiederholten Fussnoten beibehalten; dadurch bleiben die zwei Kommer-Bücher und alle KI-Kennungen sichtbar unterscheidbar.",
    "pruefung": "Pandoc-Probe bestätigt Kommer Kurztitel bei S.58 und Folgezitat S.59; KI-01, KI-02, KI-46 eindeutig."
  },
  {
    "status": "offen",
    "befund": "C02/C07",
    "aenderung": "Keine pauschale Vgl.-/Internet-/Fussnotenzählungsänderung. Keine ungeprüfte Umdeutung alter Publikations-/Versionsdaten in Zugriffsdaten. Die historische Abrufrolle ist jetzt durch separate, bereits vorhandene urldate sichtbar, die genaue Herkunft mancher date-Felder bleibt anhand Originaldaten zu klären."
  },
  {
    "status": "pruefgrenze",
    "befund": "A06",
    "aenderung": "Eindeutige Titel sind redaktionell aus der bereits dokumentierten Key-/URL-/Kontext-Zuordnung vergeben; die einzelnen Originalabfragezeitpunkte wurden nicht neu erfunden. Historische Arbeitsschrittdaten stehen im bestehenden Nachtrag; bisheriges Sicherungsdatum 13.10.2026 bleibt erhalten."
  },
  {
    "status": "pruefgrenze",
    "befund": "C05",
    "aenderung": "Keine vollständige anonyme Browserkontrolle aller 45 alten Chatlinks. IMF-2024-Seite war beim aktuellen Toolabruf rate-limited (429). Der 2009-Download-Unterpfad lieferte 404; die offizielle Ausgabeübersicht derselben Datenbank war erreichbar und wurde gezielt als Referenz-URL eingesetzt (siehe ergänzenden Nachweis)."
  },
  {
    "befund": "C05/C07",
    "key": "DownloadEntireWorld",
    "aenderung": "Nicht erreichbare Download-Unterseite durch die erreichbare offizielle Archivübersicht derselben WEO-Ausgabe Oktober 2009 ersetzt. Keine Daten oder Jahrgänge ausgetauscht. Zugriff auf den tatsächlichen Tag dieser Nachprüfung aktualisiert; die alte tatsächliche Nutzung wird nicht neu datiert.",
    "url_vorher": "https://www.imf.org/en/publications/weo/weo-database/2009/october/download-entire-database",
    "url_nachher": "https://www.imf.org/en/publications/weo/weo-database/2009/october",
    "urldate_vorher": "2026-10-07",
    "urldate_nachher": "2026-10-31",
    "date_erhalten": "2026-10-08",
    "pruefung": "Offizielle Hauptseite explizit World Economic Outlook Database October 2009; lesbare Ausgabenbeschreibung. Von dortiger Entire Dataset-Verweis reproduzierte 404. Alte historische Nutzung und neue Linkprüfung klar getrennt.",
    "pruefgrenze": "Nur der Quellenlink ist aktualisiert. Keine neuen WEO-Eingabedaten geladen und keine Dateibytes der historischen Studie neu bestätigt."
  },
  {
    "befund": "C05 und Publikationsdatum",
    "key": "DownloadEntireWorld",
    "date_before": "2026-10-08 (bisherige Rolle nicht nachträglich als Zugriff ausgegeben)",
    "date_after": "2009-10 (belegte WEO-Ausgabe Oktober 2009)",
    "url_after": "https://www.imf.org/en/publications/weo/weo-database/2009/october",
    "urldate_after": "2026-10-31",
    "note": "Offizielle Archivseite derselben Ausgabe; kein neuer Datendownload oder Studienlauf."
  }
]
````

## Konfiguration und Kurzübersicht

````diff
diff --git a/.gitignore b/.gitignore
index 072e412..01c7d56 100644
--- a/.gitignore
+++ b/.gitignore
@@ -8,3 +8,6 @@ __pycache__/
 
 /.quarto/
 **/*.quarto_ipynb
+
+!assets/ehrlichkeitserklaerung-2026-27.pdf
+!documentation/reviews/2026-10-31-chatgpt-pruefbericht.pdf
diff --git a/_quarto.yml b/_quarto.yml
index 3f31ef3..435b3ba 100644
--- a/_quarto.yml
+++ b/_quarto.yml
@@ -67,9 +67,13 @@ format:
     fig-height: 5
   pdf:
     documentclass: scrreprt
+    latex-min-runs: 3
+    lof: true
+    lot: true
     classoption:
       - oneside
       - numbers=noenddot
+      - listof=totoc
     papersize: a4
     fontsize: 11pt
     linestretch: 1.2
@@ -87,8 +91,15 @@ format:
         Welche Anlagestrategie ist langfristig wirklich überzeugend? Ein hoher Endwert verrät wenig darüber, welche Schwankungen und Verluste auf dem Weg dorthin aufgetreten sind. Diese Maturarbeit vergleicht vier Ansätze: Buy-and-Hold, 60/40, Trendfolge und BIP-Gewichtung. Ein Python-Modell simuliert die Strategien mit historischen Finanzdaten und wertet Rendite sowie verschiedene Risikokennzahlen aus. Untersucht werden ein weltweiter Hauptvergleich von 2010 bis 2025 und ein längerer US-Vergleich von 2003 bis 2025. Dabei zeigt sich, wie stark die Beurteilung vom gewählten Massstab abhängt und weshalb auch die Datenwahl und die Grenzen eines Backtests berücksichtigt werden müssen.
 
         \clearpage
+    include-after-body:
+      text: |
+        \includepdf[pages=-,pagecommand={},addtotoc={1,chapter,0,Ehrlichkeitserklärung,sec-ehrlichkeitserklaerung}]{assets/ehrlichkeitserklaerung-2026-27.pdf}
     include-in-header:
       text: |
+        \titlehead{Kantonsschule Büelrain Winterthur}
+        \subject{Maturitätsarbeit}
+        \publishers{\normalsize Klasse 4gW\\Betreuung: Jacques Mock}
+        \usepackage{pdfpages}
         \usepackage{booktabs}
         \usepackage{float}
         \usepackage{fontawesome5}
diff --git a/bibliography.qmd b/bibliography.qmd
index ed36a20..9422ca5 100644
--- a/bibliography.qmd
+++ b/bibliography.qmd
@@ -2,3 +2,7 @@
 
 ::: {#refs}
 :::
+
+## Kurzübersicht zur KI-Nutzung {.unnumbered}
+
+ChatGPT unterstützte die Planung der Engine, die Vorbereitung von Arbeitsaufträgen sowie die Prüfung von Daten, Ergebnissen und der Schlussfassung. Codex wurde für technische Umsetzung, Tests, Formatierung, Text- und Belegkorrekturen sowie die KI-Dokumentation eingesetzt. Die jeweiligen Aufgaben, übernommenen Änderungen, Prüfgrenzen und öffentlichen Chatnachweise sind in @sec-ki-dokumentation aufgeführt. Die fachliche Kontrolle und Verantwortung für die endgültige Fassung bleiben beim Autor.
diff --git a/styles/chicago-shortened-notes-bibliography-17th-edition.csl b/styles/chicago-shortened-notes-bibliography-17th-edition.csl
index 21a3580..297af43 100644
--- a/styles/chicago-shortened-notes-bibliography-17th-edition.csl
+++ b/styles/chicago-shortened-notes-bibliography-17th-edition.csl
@@ -3875,6 +3875,17 @@
     <group delimiter=". ">
       <choose>
         <if variable="DOI"/>
+        <!-- For cited web pages and software, retain the documented access date even when an issue date exists. -->
+        <else-if type="webpage post-weblog software" match="any">
+          <choose>
+            <if variable="accessed URL">
+              <group delimiter=" ">
+                <text term="accessed" text-case="capitalize-first"/>
+                <date form="text" variable="accessed"/>
+              </group>
+            </if>
+          </choose>
+        </else-if>
         <else-if match="any" variable="available-date event-date issued status"/>
         <else-if variable="accessed URL">
           <group delimiter=" ">
@@ -4357,14 +4368,8 @@
   </macro>
   <citation disambiguate-add-givenname="true" disambiguate-add-names="true" et-al-min="4" et-al-use-first="1">
     <layout delimiter="; " suffix=".">
-      <choose>
-        <if match="any" position="ibid ibid-with-locator">
-          <text macro="citation-notes-shortened-author-only"/>
-        </if>
-        <else>
-          <text macro="citation-notes-shortened-author-title"/>
-        </else>
-      </choose>
+      <!-- Retain a short title in repeated notes so the cited work remains unambiguous. -->
+      <text macro="citation-notes-shortened-author-title"/>
     </layout>
   </citation>
   <!-- Bibliography -->

````

## Nachgereichte Ehrlichkeitserklärung

Die bereitgestellte Datei `Ehrlichkeitserklärung_MA_2026-27_Riccardo_Ambuehl.pdf` enthält eine Seite, Name/Vorname/Klasse 4gW, den aktuellen Arbeitstitel, Datum31.10.2026, eine sichtbare Unterschrift und eine markierte Mediotheksoption. Keine interaktiven Formularfelder und keine kryptografische PDF-Signatur festgestellt. Die Quelldatei wurde unverändert kopiert; SHA-256 `feaebe2907967697278e9d3e15cea03929a0f10cca7b303f62623a1628e425e4`. Die Einbindung erfolgt für PDF über pdfpages nach dem gesamten Buchinhalt. Eine sichtbare Unterschrift in der vom Autor gelieferten Datei wurde übernommen, nicht von Codex hergestellt. Anforderungen an die persönliche Unterzeichnung der Druckexemplare bleiben beim Autor.

## Genaue Umbruchkorrekturen

````json
"date"
````

````json
"changes"
````

````json
"integrity"
````

````json
"D02_method"
````

````json
"D03_method"
````

Die zwei eng begrenzten PDF-Ausnahmen in `.gitignore` erhalten die unveränderten Quellen für spätere reproduzierbare Buchausgaben; erzeugte PDFs bleiben sonst ausgeschlossen. `latex-min-runs:3` verhindert veraltete römische Verzeichnisseiten nach dem neu gewachsenen Inhaltsverzeichnis.

## Abschliessende Ausgabekontrolle

Die abschliessenden Ausgaben wurden ausschliesslich in einer externen Projektkopie erzeugt. Dort waren `execute.enabled:false` und `freeze:false` gesetzt; alle Renderaufrufe verwendeten `--no-execute --no-cache`. Keine Notebookberechnung und keine Engine-/Backtestausführung fand statt. Der PDF-Lauf deaktivierte automatische Paketinstallation. Die Quelldateien der eigentlichen Arbeit wurden vom Render nicht verändert.

| Kontrolle | Ergebnis |
|---|---|
| Quarto PDF | Exit0, 123 Seiten, drei LuaLaTeX-Durchläufe; aktuelle Verzeichnisse und Querverweise. |
| Inhalt | Titelblatt, exakter 681-Zeichen-Abstract, acht Figuren, 22 Redaktionstabellen, eindeutiger KI-46-Beleg und neuer KI-Nachtrag vorhanden. Ehrlichkeitserklärung letzte Seite und im Inhaltsverzeichnis. |
| Verzeichnisse | Abbildungsverzeichnis vi, Tabellenverzeichnis vii. Alle Caption-Seiten stimmen mit den Einträgen überein, auch Abb.5.6 auf gedruckt48 / Dateiseite56. Keine ??-Verweise. |
| Umbruchkorrekturen | Abb.5.6 mit vollständigem Quellenabsatz auf Dateiseite56. Ausführungsumgebung als Absatz in C.3 statt eigener fast leerer Seite. |
| Sichtkontrolle | Gesamte Seitenübersicht und gezielte Detailansichten geprüft; keine abgeschnittenen Tabellen/Grafiken oder Textüberlagerungen beobachtet. Signaturdarstellung der übernommenen Erklärung sichtbar; keine Authentizitätsprüfung behauptet. |
| HTML | Exit0, elf Buchseiten, 1907 lokale href/src/Ankerziele gültig, keine doppelten IDs. |
| Erhaltene Resultate | Alle 30 versionierten Ergebnisdateien ohne Änderung; Codezellen und gespeicherte Outputs wie oben geprüft. |
| Grenzen | Keine persönliche Autorenfreigabe, keine neue wissenschaftliche Ergebnisberechnung, keine vollständige Inhaltsprüfung der dynamischen historischen Chats; der vereinbarte schulische Zitierstil und die Auslegung der Wortzählung bleiben mit der Betreuung abzugleichen. |

Das LaTeX-Protokoll enthält keine fehlenden Zeichen oder undefinierten Verweise/Zitationen. Es bleiben 14 Overfull-hbox- und 9 Underfull-Meldungen sowie eine KOMA-Warnung zur Kapitelkopfdefinition. Die Überbreiten betragen höchstens1,095pt und führen in der Sichtkontrolle nicht zu abgeschnittenem Inhalt. Pypdf meldet beim Import der unveränderten Erklärung einmal die doppelte PDF-Dictionary-Definition `/Group`; die finale PDF ist lesbar und wurde gerastert. Diese Hinweise werden nicht als fehlerfreies Log ausgegeben.

Die vollständigen technischen Daten stehen unter `documentation/reviews/2026-10-31-technische-pruefung.json`. Die erzeugte PDF und das HTML-Buch wurden nach bestandener Kontrolle nach `_book/` übernommen. Ein neuer DOCX-Export war nicht Teil dieser Ausgabekontrolle. Die persönliche Endkontrolle der neuen Text- und Belegänderungen bleibt beim Autor.
