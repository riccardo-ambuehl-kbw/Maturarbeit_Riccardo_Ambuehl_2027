# Gezielte Fachkorrekturen aus dem Gegenlesen – Phase 2

Datum: 12. Oktober 2026. Verfasser: Codex. **Elf von elf freigegebenen Befunden vollständig korrigiert und gezielt geprüft; null teilweise gelöst, null offen innerhalb dieses Auftrags. Haupttext 7’849→7’959 einschliesslich Überblick, 41 unter 8’000. Autorenkontrolle ausstehend.**

Ausgangspunkt und unveränderter HEAD: `6c9cb6991e95165744836d6da1c77c5280035ab5`, Branch `dev`, sauberer Arbeitsbaum. Keine anwendbare AGENTS.md im Repository/den Vorfahren gefunden. Der vollständige Gegenlesebericht, der Stufe-2-Kürzungsbericht, aktuelle betroffene Notebook-Passagen/Anhänge, src/funktionen.py, Originalbelege und KI-Regeln wurden gelesen. Frühere Kürzungen bleiben erhalten. Keine allgemeine Stilkorrektur oder zusätzliche Kürzung.

Externe vollständige Ausgangssicherung: `C:\Users\modic\AppData\Local\Temp\codex-fachkorrekturen-phase2-2026-10-12-9lr8x8_5\original`. 158 Arbeitsdateien und 87 versionierte Ausgangsdateien, einschliesslich 70 vorhandener Ausgabe-/Freeze-/Cachedateien; alle Kopien per SHA-256 bestätigt. .git/.venv/__pycache__ nicht kopiert, Git-Index/HEAD/Branch separat kontrolliert. Separate Studien-Worktrees wurden nicht bearbeitet.

Byteidentischer [Originalauftrag](ai-usage/prompts/2026-10-12-fachkorrekturen-phase2.txt); SHA-256 `c86dfde0ae541288b6ad0fe075beceec10295a5a74a8cac2f91d0b0111d92c93`. Dieser Bericht ist kein neues wissenschaftliches Studienergebnis und keine persönliche Autorenfreigabe.

## 1. Übersicht und Wortzahl

| Kategorie | Anzahl/Stand |
|:---|:---|
| Vollständig korrigiert | 11: R-001, R-003, R-004, R-005, R-006, R-007, R-009, R-010, R-011, R-013, R-015 |
| Teilweise korrigiert | 0 |
| Offen im freigegebenen Korrekturauftrag | 0 |
| Separate Befunde | R-008/R-012/R-016/R-017 bleiben ausstehend; R-002 im Umfangsrahmen, R-014 historisch eingeordnet |

Gezählt wird mit exakt der bisherigen Filterfolge und Tokenregel `\b\w+(?:[’'-]\w+)*\b`: nur Markdown-Prosa der sechs Hauptnotebooks; keine Überschriften, Tabellenzeilen, Mathematik, Citation-Klammern, Code, Outputs, Raw/YAML oder Anhänge. HTML-Tags/Linkziele/Abschnittsanker entfernt, sichtbare Beschriftungen und Zahlen zählen. Keine Gleichsetzung mit Word-Zählung.

| Kapitel | Vorher | Nachher | Änderung |
|:---|---:|---:|---:|
| index | 125 | 125 | +0 |
| Einleitung | 430 | 430 | +0 |
| Theorie | 2’659 | 2’769 | +110 |
| Methodik | 855 | 855 | +0 |
| Analyse | 2’949 | 2’949 | +0 |
| Fazit | 831 | 831 | +0 |
| **Mit Überblick** | **7’849** | **7’959** | **+110** |
| **Ohne Überblick** | **7’724** | **7’834** | **+110** |

Die Obergrenze bleibt eingehalten. Sämtliche Zunahme im Haupttext stammt aus den ausdrücklich beauftragten Fachkorrekturen im Theorie-Notebook. Die Entfernung der Doppelung betrifft nur Anhang C, keine zusätzliche Haupttextkürzung.

## 2. Einzelbefunde mit tatsächlichen Änderungen

### R-001 – Gespeicherte Volatilität veraltet

**Status:** Vollständig korrigiert und geprüft. **Änderung:** Einzige isolierte Notebook-Codeausführung: unveränderte Originalzelle in einem frischen bestehenden Python-Kernel; nur tatsächlicher Output, Execution Count und Ausführungszeiten übernommen.

**Begründung/Verifikation:** Gewichtete Renditen [0.024, −0.014, 0.004, 0.030, 0.006, 0.014]; unabhängige Standardbibliotheksrechnung mit N−1 ergibt Varianz 0.0002474666666666667 und Standardabweichung 0.015731073284002802. Ausgabe 1.57%.

**Grenze:** Frischer Kernel zählt den einen Lauf als 1; dies behauptet keine Gesamtausführung des Theorie-Notebooks. Python 3.14.0, pandas 3.0.3, NumPy 2.4.6 sind die vorhandene lokale Beispielumgebung, nicht der eingefrorene Studienstand pandas 2.3.3.

Datei: `notebooks/Theorie.ipynb`; Zell-ID `5b4e89ac`.

**Vorher:** Execution Count `null`, stdout `Volatilität: 1.15%`. **Nachher:** Execution Count `1`, tatsächlicher stdout `Volatilität: 1.57%`. Unveränderte Gewichte 0,20/0,40/0,40; unveränderter Code und Zell-ID.

Ausgeführt 2026-10-12T21:37:10.148336+00:00 bis 2026-10-12T21:37:11.868279+00:00 (UTC) mit `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027\.venv\Scripts\python.exe`. Quell-SHA-256 `792751d4527a516a7ba2a6edca8d4d1fb37050b70e81dc157aa602690e231d19`. nbclient/iopub-Zeitstempel wurden direkt aus der tatsächlichen Kernelantwort übernommen:

```json
{
  "execution": {
    "iopub.status.busy": "2026-10-12T21:37:11.517518Z",
    "iopub.execute_input": "2026-10-12T21:37:11.517898Z",
    "iopub.status.idle": "2026-10-12T21:37:11.867582Z",
    "shell.execute_reply": "2026-10-12T21:37:11.867033Z"
  }
}
```

Erster externer Ausführungsaufbau stoppte vor der Zellenausführung, weil die JSON-Quellliste noch nicht in die von nbclient erwartete Zeichenkette umgewandelt war. Nach dieser Anpassung ausschliesslich im externen Hilfsskript genau eine Originalzelle erfolgreich ausgeführt. Kein Source-Fix im Notebook nötig.
### R-003 – Zwei Indexbelege dem falschen Kommer-Buch zugeordnet

**Status:** Vollständig korrigiert und geprüft. **Änderung:** Genau zwei unmögliche Starterbuch-Seitenverweise durch den vorhandenen Key kommerSouveraenInvestierenMit2025 mit Abschnitt 9.2 ersetzt; übrige Starterbuchbelege erhalten.

**Begründung/Verifikation:** Original-EPUB MZ4YACD4 nennt im OPF-Formatfeld 192 Seiten; 464–465 sind dort unmöglich. Original-PDF A8Q9SBUT: Datei-Seiten 464–465 vollständig gelesen, Abschnitt 9.2 «Das Wichtigste zu Wertpapierindizes» mit Referenzindex, Gewichtung und regelmässiger Auswahlprüfung. Titel/7. Auflage/2025 mit bestehendem Bib-Eintrag abgeglichen.

**Grenze:** Die verifizierbare Abschnittsangabe ersetzt die ungeklärte Druckpaginierung. Andere Seitenbelege des Starterbuchs wurden nicht pauschal neu geprüft oder verändert.

Datei: `notebooks/Theorie.ipynb`; Zell-ID `1941d2df`.

**Vorher:**

````markdown
<p>Ein Index bildet die Wertentwicklung eines festgelegten Marktbereichs als rechnerische Kennzahl ab. Der S&P 500 umfasst beispielsweise die 500 grössten Unternehmen der USA. Weil sich ein marktbreiter Index auf zahlreiche Titel stützt, hängt seine Entwicklung nicht von einem einzelnen Unternehmen ab. Ein Indexfonds versucht, seinen Referenzindex möglichst genau nachzubilden, anstatt ihn zu übertreffen [@kommerLeichteEinstiegWelt2025, S. 464-465].<br>Welche Wertpapiere im Index enthalten sind und wie stark sie gewichtet werden, bestimmt dessen Regelwerk. Es regelt ebenfalls, unter welchen Voraussetzungen Titel hinzukommen oder entfernt werden. Die Zusammensetzung wird üblicherweise in einem festen Rhythmus, etwa halb- oder vierteljährlich, überprüft [@kommerLeichteEinstiegWelt2025, S. 465].</p>
````

**Nachher:**

````markdown
<p>Ein Index bildet die Wertentwicklung eines festgelegten Marktbereichs als rechnerische Kennzahl ab. Der S&P 500 umfasst beispielsweise 500 führende grosse US-Unternehmen, die zusätzliche Indexauswahlkriterien erfüllen [@spdjThe500]. Weil sich ein marktbreiter Index auf zahlreiche Titel stützt, hängt seine Entwicklung nicht von einem einzelnen Unternehmen ab. Ein Indexfonds versucht, seinen Referenzindex möglichst genau nachzubilden, anstatt ihn zu übertreffen [@kommerSouveraenInvestierenMit2025, Abschnitt 9.2].<br>Welche Wertpapiere im Index enthalten sind und wie stark sie gewichtet werden, bestimmt dessen Regelwerk. Es regelt ebenfalls, unter welchen Voraussetzungen Titel hinzukommen oder entfernt werden. Die Zusammensetzung wird üblicherweise in einem festen Rhythmus, etwa halb- oder vierteljährlich, überprüft [@kommerSouveraenInvestierenMit2025, Abschnitt 9.2].</p>
````

### R-004 – 60/40-Formel ohne notwendige Anfangsbedingung

**Status:** Vollständig korrigiert und geprüft. **Änderung:** Bedingung tatsächlicher 60/40-Gewichte zu Periodenbeginn direkt im Formelabsatz ergänzt; jährliche Drift und allgemeine Gewichtung mit tatsächlichen Anfangsgewichten genannt. Formel selbst und allgemeine Formel in c269ad7f unverändert.

**Begründung/Verifikation:** Unabhängiger synthetischer Gegenfall: Start 60/40; Aktien +100 %, Anleihen 0 % ergibt 75/25. Danach Aktien −50 % ergibt tatsächlich −37,5 % statt der unzulässigen festen −30 %. Bestehender Pham-Beleg S. 50 bleibt erhalten.

**Grenze:** Keine Änderung der Rebalancing-Regel, Studienkonfiguration oder Engine; kein ausführliches neues Beispiel im Haupttext.

Datei: `notebooks/Theorie.ipynb`; Zell-ID `990d4cd6`.

**Vorher:**

````markdown
$$
r_{60/40,t}=0{,}60r_{\mathrm{Aktien},t}+0{,}40r_{\mathrm{Anleihen},t}
$$
<p>Dabei bezeichnet <b>r<sub>60/40,t</sub></b> die Rendite des Gesamtportfolios zum Zeitpunkt <b>t</b>. <b>r<sub>Aktien,t</sub></b> und <b>r<sub>Anleihen,t</sub></b> sind die Renditen der beiden Anlageklassen; 0,60 und 0,40 sind ihre Zielgewichte.</p>
<p>Die Formel ist der 60/40-Spezialfall der gewichteten Portfoliorendite [@phamPerformance60402025, S. 50]. Durch unterschiedliche Renditen verschieben sich die Anteile im Zeitablauf. Das Portfolio muss deshalb regelmässig auf die Zielgewichte von 60% und 40% zurückgesetzt werden [@kommerSouveraenInvestierenMit2025, S. 523-526].</p>
````

**Nachher:**

````markdown
$$
r_{60/40,t}=0{,}60r_{\mathrm{Aktien},t}+0{,}40r_{\mathrm{Anleihen},t}
$$
<p>Dabei bezeichnet <b>r<sub>60/40,t</sub></b> die Rendite des Gesamtportfolios zum Zeitpunkt <b>t</b>. <b>r<sub>Aktien,t</sub></b> und <b>r<sub>Anleihen,t</sub></b> sind die Renditen der beiden Anlageklassen; 0,60 und 0,40 sind ihre Zielgewichte. Die Formel gilt nur, wenn die tatsächlichen Gewichte zu Periodenbeginn 60/40 betragen. Zwischen jährlichen Rebalancing-Terminen driften sie; die allgemeine Portfoliorendite verwendet die tatsächlichen Anfangsgewichte.</p>
<p>Die Formel ist der 60/40-Spezialfall der gewichteten Portfoliorendite [@phamPerformance60402025, S. 50]. Durch unterschiedliche Renditen verschieben sich die Anteile im Zeitablauf. Das Portfolio muss deshalb regelmässig auf die Zielgewichte von 60% und 40% zurückgesetzt werden [@kommerSouveraenInvestierenMit2025, S. 523-526].</p>
````

### R-005 – Lokales drawdown() ignoriert anfänglichen Verlust gegenüber Startwert 1

**Status:** Vollständig korrigiert und geprüft. **Änderung:** Genau eine Codezeile geändert: cummax().clip(lower=1.0). maximum_drawdown() und alle anderen Finanzfunktionen unverändert.

**Begründung/Verifikation:** Drei gezielte Tests führen die tatsächlichen beiden Funktionen aus dem aktuellen Quelltext isoliert aus: Anfangsverlust [−10 %,0] → MDD −10 %; neuer Peak/−10 %/Erholung → MDD −10 %; Anfangsverlust/neuer Peak/−25 %/Erholung → MDD −25 %. Alle Zeilenwerte mit Toleranz 10⁻¹² bestätigt.

**Grenze:** QuantStats fehlt lokal; deshalb kein Vollimport des Moduls und keine anderen Funktionen getestet. Nur die zwei unveränderten/korrigierten AST-Funktionsobjekte wurden mit vorhandenem pandas geladen. Keine Installation, kein Engine-Test oder Studienlauf.

Datei: `src/funktionen.py`, Funktion `drawdown()`; keine Notebook-Zell-ID.

```diff
-    bisheriger_hoechststand = vermoegen.cummax()
+    bisheriger_hoechststand = vermoegen.cummax().clip(lower=1.0)
```

| Synthetische Renditen | Erwarteter Drawdown-Verlauf | MDD |
|:---|:---|---:|
| −0,1; 0 | −0,1; −0,1 | −10 % |
| 0,2; −0,1; 1/9 | 0; −0,1; 0 | −10 % |
| −0,1; 1/3; −0,25; 1/3 | −0,1; 0; −0,25; 0 | −25 % |

Geprüft mit lokal vorhandenem pandas 3.0.3. Kleine Gleitkommaabweichung am letzten Erholungspunkt −2,22×10⁻¹⁶ innerhalb der Toleranz.
### R-006 – Vollständige Erholungsdauer mit QuantStats-Unterwasser-Episoden vermischt

**Status:** Vollständig korrigiert und geprüft. **Änderung:** Definition um den konkreten Peak→Recovery-Zeitraum ergänzt; gespeicherte Spalten und vereinfachende Codeüberschrift erklärt. Offene letzte Episode ausdrücklich benannt. Zelle d606f0f5 samt Output vollständig identisch.

**Begründung/Verifikation:** Unabhängige skalare Vermögensrekursion der künstlichen Beispielreihe: Peak 31.01.2024, Erholung 30.04.2024 = 90 Kalendertage; Unterwasser 29.02.–31.03. inklusive Randtage = 32. Am 31.12.2024 noch −2,40544 %. [QuantStats-Originalcode drawdown_details](https://github.com/ranaroussi/quantstats/blob/main/quantstats/stats.py) bestätigt Episoden, inklusive Tageszählung und Ausreisserfilter.

**Grenze:** Keine lokal festgehaltene Version des gespeicherten QuantStats-Outputs; keine Neuausführung oder heutige Versionsgarantie. «99% max drawdown» ist der gefilterte minimale Drawdown in Prozent, kein Konfidenzintervall und keine Erholungsdauer.

Datei: `notebooks/Theorie.ipynb`; Zell-ID `d501a004`.

**Vorher:**

````markdown


#### Erholungsdauer und Grenzen


<p>Die Erholungsdauer reicht vom früheren Höchststand bis zu dessen vollständiger Wiedererreichung. Tiefe und Dauer sind verschiedene Eigenschaften: Ein Verlust kann tief und kurz oder weniger tief und lang sein [@kommerSouveraenInvestierenMit2025, S. 163-164].</p>
````

**Nachher:**

````markdown


#### Erholungsdauer und Grenzen


<p>Die Erholungsdauer reicht vom früheren Höchststand bis zu dessen vollständiger Wiedererreichung: im folgenden Beispiel vom 31.01.2024 bis 30.04.2024, also 90 Kalendertage. Tiefe und Dauer sind verschiedene Eigenschaften: Ein Verlust kann tief und kurz oder weniger tief und lang sein [@kommerSouveraenInvestierenMit2025, S. 163-164].</p>
````

Datei: `notebooks/Theorie.ipynb`; Zell-ID `83fd3049`.

**Vorher:**

````markdown
<p>Für die Erholungsdauer und alle wichtigen Daten dazu nutzen wir zwei Funktionen aus QuantStats: <code>.to_drawdown_series()</code> und <code>.drawdown_details()</code> [@aroussiRanaroussiQuantstats2026].</p>
````

**Nachher:**

````markdown
<p>QuantStats liefert mit <code>.to_drawdown_series()</code> und <code>.drawdown_details()</code> Unterwasser-Episoden [@aroussiRanaroussiQuantstats2026]. In der gespeicherten Tabelle bezeichnet <code>start</code> den ersten Unterwasserzeitpunkt, <code>valley</code> den Zeitpunkt des tiefsten Rückgangs und <code>end</code> den letzten beobachteten Unterwasserzeitpunkt. <code>days</code> zählt Kalendertage einschliesslich beider Randtage: 29.02.–31.03. ergibt 32, nicht die vollständige Erholungsdauer. <code>max drawdown</code> ist das Minimum in Prozent; <code>99% max drawdown</code> das Minimum nach QuantStats-Ausreisserfilter. Die letzte Episode endet am Datenende 31.12.2024 mit −2,4054 % noch unerholt. Die Code-Überschrift «Erholungsphasen» bezeichnet diese Episoden vereinfachend.</p>
````

### R-007 – S&P 500 als Rangliste der 500 grössten US-Unternehmen vereinfacht

**Status:** Vollständig korrigiert und geprüft. **Änderung:** Nur den betroffenen Satz in T01 präzisiert: 500 führende grosse US-Unternehmen mit zusätzlichen Indexauswahlkriterien. Genau ein neuer institutioneller Anbieterbeleg spdjThe500 angehängt.

**Begründung/Verifikation:** [S&P Dow Jones Indices, The 500](https://www.spglobal.com/spdji/en/landing/investment-themes/the-500/), Abschnitt «What’s Inside?»: Auswahl berücksichtigt unter anderem Liquidität, Streubesitz und Gewinnfähigkeit. [Offizielle S&P-500-Indexbeschreibung](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) bestätigt 500 führende Unternehmen. Zugriff 12.10.2026.

**Grenze:** Kein erfundenes Veröffentlichungsjahr, kein Seitenlocator; die Datumsangabe einzelner Webdaten ist nicht als Publikationsdatum ausgegeben. Alle bestehenden Bib-Einträge als Bytepräfix erhalten; keine Rekonstruktion historischer Zusammensetzungen.

Datei: `notebooks/Theorie.ipynb`; Zell-ID `1941d2df`.

**Vorher:**

````markdown
<p>Ein Index bildet die Wertentwicklung eines festgelegten Marktbereichs als rechnerische Kennzahl ab. Der S&P 500 umfasst beispielsweise die 500 grössten Unternehmen der USA. Weil sich ein marktbreiter Index auf zahlreiche Titel stützt, hängt seine Entwicklung nicht von einem einzelnen Unternehmen ab. Ein Indexfonds versucht, seinen Referenzindex möglichst genau nachzubilden, anstatt ihn zu übertreffen [@kommerLeichteEinstiegWelt2025, S. 464-465].<br>Welche Wertpapiere im Index enthalten sind und wie stark sie gewichtet werden, bestimmt dessen Regelwerk. Es regelt ebenfalls, unter welchen Voraussetzungen Titel hinzukommen oder entfernt werden. Die Zusammensetzung wird üblicherweise in einem festen Rhythmus, etwa halb- oder vierteljährlich, überprüft [@kommerLeichteEinstiegWelt2025, S. 465].</p>
````

**Nachher:**

````markdown
<p>Ein Index bildet die Wertentwicklung eines festgelegten Marktbereichs als rechnerische Kennzahl ab. Der S&P 500 umfasst beispielsweise 500 führende grosse US-Unternehmen, die zusätzliche Indexauswahlkriterien erfüllen [@spdjThe500]. Weil sich ein marktbreiter Index auf zahlreiche Titel stützt, hängt seine Entwicklung nicht von einem einzelnen Unternehmen ab. Ein Indexfonds versucht, seinen Referenzindex möglichst genau nachzubilden, anstatt ihn zu übertreffen [@kommerSouveraenInvestierenMit2025, Abschnitt 9.2].<br>Welche Wertpapiere im Index enthalten sind und wie stark sie gewichtet werden, bestimmt dessen Regelwerk. Es regelt ebenfalls, unter welchen Voraussetzungen Titel hinzukommen oder entfernt werden. Die Zusammensetzung wird üblicherweise in einem festen Rhythmus, etwa halb- oder vierteljährlich, überprüft [@kommerSouveraenInvestierenMit2025, Abschnitt 9.2].</p>
````

Bibliografie neu, bisherige 52 Einträge unverändert:

```bibtex
@online{spdjThe500,
  author = {{S\&P Dow Jones Indices}},
  title = {The 500},
  url = {https://www.spglobal.com/spdji/en/landing/investment-themes/the-500/},
  urldate = {2026-10-12},
  langid = {english}
}
```

### R-009 – to_datetime-Verweis auf PDF-Kapitelanfang

**Status:** Vollständig korrigiert und geprüft. **Änderung:** Nur den Locator von S. 511 auf Kapitel 11, «Converting Between String and Datetime» umgestellt; aktueller Pfad ist Anhang B.3.3.

**Begründung/Verifikation:** Original-PDF PJA9S9HY vollständig an den relevanten Stellen gelesen: Datei-Seite 511 beginnt «Chapter 11. Time Series»; to_datetime-Beispiele auf Datei-Seite 516 unter dem auf Datei-Seite 514 beginnenden geprüften Unterabschnitt.

**Grenze:** Datei-Seite 516 wird nicht als gedruckte Buchseite ausgegeben. Funktion/Beispielcode und Nachbarquellen unverändert.

Datei: `notebooks/Anhang_Datenaufbereitung.ipynb`; Zell-ID `7e670f16`.

**Vorher:**

````markdown
Quelle zur Nutzung von to_datetime() [@mckinneyPythonDataAnalysis2022, S. 511].
````

**Nachher:**

````markdown
Quelle zur Nutzung von to_datetime() [@mckinneyPythonDataAnalysis2022, Kapitel 11, «Converting Between String and Datetime»].
````

### R-010 – Gleiche Rendite statt gleiches arithmetisches Monatsmittel

**Status:** Vollständig korrigiert und geprüft. **Änderung:** Ausschliesslich «bei gleicher Rendite» durch «bei gleichem arithmetischem Mittel der Monatsrenditen» ersetzt.

**Begründung/Verifikation:** Bestehender Phase-2-Rechennachweis: beide Monatsmittel 1 %, geometrisch aufmultipliziert A 12,6791 % und B 11,6805 %. Plotzelle c09ff8c4 einschliesslich Daten, Code, Output und PNG identisch.

**Grenze:** Die Illustration wurde nicht erneut ausgeführt; keine neue wissenschaftliche Kennzahl oder Ergebnisreihe erstellt.

Datei: `notebooks/Theorie.ipynb`; Zell-ID `5a028097`.

**Vorher:**

````markdown
<p>Das Beispiel zeigt übertrieben, wie ein Kurs bei gleicher Rendite eine ganz unterschiedliche Volatilität aufweisen kann.</p>
````

**Nachher:**

````markdown
<p>Das Beispiel zeigt übertrieben, wie ein Kurs bei gleichem arithmetischem Mittel der Monatsrenditen eine ganz unterschiedliche Volatilität aufweisen kann.</p>
````

### R-011 – Historische pandas-Aliasübersicht ohne ausdrückliche aktuelle Schreibweise/Studienversion

**Status:** Vollständig korrigiert und geprüft. **Änderung:** Vorhandenen historischen Hinweis bewahrt und genau am Tabellenstandort Hilpisch (2019), ME statt M sowie Studienstand pandas 2.3.3/ME ergänzt. Alias-Tabelle und Literaturbelege vollständig identisch.

**Begründung/Verifikation:** [Offizielle pandas-2.2.0-Release Notes](https://pandas.pydata.org/docs/whatsnew/v2.2.0.html#deprecate-aliases-m-q-y-etc-in-favour-of-me-qe-ye-etc-for-offsets): M→ME seit 2.2 deprecated. Alle fünf unveränderten Studienmanifeste dokumentieren pandas 2.3.3; bestehende finale Config-/Studiennachweise nennen ME.

**Grenze:** Der vorherige Hinweis ordnete die Liste historisch ein, nannte jedoch weder ME noch die Studienversion am Tabellenstandort. Deshalb kurze gezielte Ergänzung statt Tabellenänderung. Kein Paket-/Engine-/Frequenzwechsel; lokale Testversion 3.0.3 ausdrücklich getrennt.

Datei: `notebooks/Anhang_Datenaufbereitung.ipynb`; Zell-ID `7afa023e`.

**Vorher:**

````markdown
### Technische Zeitreihen- und Resampling-Beispiele {#sec-resampling-beispiele}

Diese Originalangaben dokumentieren die technische Einführung aus dem Theoriekapitel. Die Aliasliste und ihre Quellenbelege bleiben im historischen Kontext erhalten; die vorhandene Python-Codezelle und ihre gespeicherte Ausgabe verbleiben im Theoriekapitel.

````

**Nachher:**

````markdown
### Technische Zeitreihen- und Resampling-Beispiele {#sec-resampling-beispiele}

Diese Originalangaben dokumentieren die technische Einführung aus dem Theoriekapitel. Die Aliasliste und ihre Quellenbelege bleiben im historischen Kontext erhalten; die vorhandene Python-Codezelle und ihre gespeicherte Ausgabe verbleiben im Theoriekapitel.

Die folgende historische Aliasübersicht stammt aus Hilpisch (2019). Neuere pandas-Versionen verwenden unter anderem [ME statt M für das Monatsende](https://pandas.pydata.org/docs/whatsnew/v2.2.0.html#deprecate-aliases-m-q-y-etc-in-favour-of-me-qe-ye-etc-for-offsets). Der dokumentierte Studienstand nutzt pandas 2.3.3 und ME.

````

### R-013 – Identischer Gegenrechnungsabsatz zweimal unmittelbar hintereinander

**Status:** Vollständig korrigiert und geprüft. **Änderung:** Genau die Markdown-Zelle 008ef22e entfernt; unmittelbar vorausgehende HTML-Absatzzelle a4355b5e als vollständiges Originalobjekt erhalten.

**Begründung/Verifikation:** Textvergleich: a4355b5e = <p> + vollständiger Text von 008ef22e + </p>. Gelöschte Zelle hat weder Überschrift noch Abschnittsanker; übrige IDs/Reihenfolge/aktive Querverweise erhalten. Zellzahl 495→494.

**Grenze:** Keine Codezelle entfernt; keine zusätzliche Gegenrechnung behauptet. Historischer Absatz einmal vollständig erhalten.

Datei: `notebooks/Anhang_Tests_Validierung.ipynb`; Zell-ID `008ef22e`.

**Vorher:**

````markdown
Anschliessend erfolgte eine zusätzliche KI-gestützte Gegenrechnung aus den eingefrorenen Eingaben und den Ergebnisdateien. Dabei wurden unter anderem Portfoliowerte, Renditen, Risikokennzahlen, Signalverzögerungen und jährliche Umschichtungen geprüft. Innerhalb dieses dokumentierten Prüfumfangs wurden keine rechnerischen Abweichungen gefunden. Die fünf Ergebnisordner bleiben unverändert erhalten. Die folgenden Tabellen und Grafiken werden daraus abgeleitet; für ihre Darstellung werden keine neuen Hauptläufe ausgeführt.
````

**Nachher:**

````markdown
[Textzelle entfernt; vollständige Originalzelle a4355b5e unverändert erhalten.]
````

### R-015 – Historisches Inflationsmittel als feste jährliche Kaufkraftschwelle verwendet

**Status:** Vollständig korrigiert und geprüft. **Änderung:** Nur Zeitraum 2016–2025 und notwendige tatsächliche Inflation desselben Zeitraums präzisiert; BFS-Key Preise erhalten.

**Begründung/Verifikation:** Gespeicherte BFS-Originalseite 8NRJRVVL, Konsumentenpreise 2016–2025: −0,4 / 0,5 / 0,9 / 0,4 / −0,7 / 0,6 / 2,8 / 2,1 / 1,1 / 0,2 %. Arithmetisches Mittel 0,75 %, gerundet 0,8 %. Kaufkrafterhalt verlangt passende nominale Rendite und tatsächliche Inflation derselben Periode/Währung.

**Grenze:** Live-BFS-Seite über Browserwerkzeug nicht lesbar; zugänglicher gespeicherter Originalbeleg verwendet und gehasht. Keine nachträgliche CHF-Inflationsbereinigung der nominalen USD-Studie.

Datei: `notebooks/Theorie.ipynb`; Zell-ID `621f9b9a`.

**Vorher:**

````markdown


#### Nominal und real


<p>Die reale Rendite ist die inflationsbereinigte Rendite. Vor allem über längere Zeiträume ist es sehr wichtig, das zu berücksichtigen. Aus der Grafik des Bundesamts für Statistik kann man für die letzten 10 Jahre eine durchschnittliche Inflation von 0.8% in der Schweiz ablesen [@Preise]. Das heisst, ein Investment muss jährlich mindestens 0.8% erzielen, damit die Kaufkraft erhalten bleibt.</p>
````

**Nachher:**

````markdown


#### Nominal und real


<p>Die reale Rendite ist die inflationsbereinigte Rendite. Vor allem über längere Zeiträume ist es sehr wichtig, das zu berücksichtigen. Aus der Grafik des Bundesamts für Statistik kann man für 2016–2025 eine durchschnittliche Inflation von 0.8% in der Schweiz ablesen [@Preise]. Zur Erhaltung der Kaufkraft muss die nominale Rendite die tatsächliche Inflation desselben Zeitraums erreichen; 0.8% sind keine feste jährliche Schwelle.</p>
````

## 3. Nicht beauftragte Befunde

| Befund | Aktueller Stand; keine inhaltliche Bearbeitung |
|:---|:---|
| R-002 | Nach derselben Methode weiterhin unter 8’000: 7’959 mit Überblick; keine zusätzlichen Kürzungen |
| R-008 | Historische Programmier-/Adaptereinträge weiterhin Gegenstand eines separaten Dokumentationsauftrags |
| R-012 | Datum und Umfang tatsächlicher persönlicher Autorenkontrolle bleiben vom Autor zu bestätigen; keine Freigabe erfunden |
| R-014 | Früherer QMD-Projektüberblick bleibt als historischer Stand in Anhang A.7; Originale/README unverändert |
| R-016 | Vollständige Titelseite, Abstract/Verzeichnisse und unterschriebene Eigenständigkeitserklärung weiterhin separat offen |
| R-017 | Unabhängige Originaldaten-/Sharpe-Prüfung im Studienarchiv weiterhin separat ausstehend; kein realer Ergebnisfehler hier behauptet oder neu geprüft |

## 4. Integrität und Quellen

| Gegenstand | Nachweis |
|:---|:---|
| Notebook-Schema und IDs | 9 gültige Notebooks, 495→494 Zellen; genau 008ef22e entfernt, übrige IDs/Reihenfolge/metadatenidentisch |
| Code/Outputs | 28 Codezellen; 27 vollständige Codezellobjekte und 27 Outputs identisch. R-001 einzig zulässige Output-/Execution-Metadatenabweichung; dessen Source/ID unverändert |
| Bilder | Alle acht gespeicherten PNGs exakt identisch; insbesondere c09ff8c4 und alle sieben Ergebnisgrafiken |
| Formeln/Tabellen | Multimenge aller 95 Mathematikausdrücke und 14 Markdown-Tabellenblöcke exakt identisch |
| Quellen | 53 eindeutige Bib-Einträge, 30 aktive Citation Keys/158 Vorkommen, null fehlende Keys. Änderungen nur zwei Kommer-Locatoren, ein McKinney-Locator und ein neuer S&P-Beleg; ursprüngliche Bib-Bytes als Präfix erhalten |
| Abschnittsverweise | Alle 22 expliziten aktiven sec-Ziele definiert; Entfernung betrifft keinen Abschnittsanker. Nummerierung und Einbindung unverändert |
| Fachstruktur/Sperrstellen | Über alle Zellen vollständiger Objektvergleich ausser erlaubten IDs: F02/F04, Forschungsfragen, Strategieregeln, übrige Lehrerfeedback-Ergänzungen identisch. T01 nur R-003/R-007 |
| Studiennachweise | Alle 30 Ergebnisdateien einschliesslich fünf Manifeste, Studienkonfigurationen und historische Freeze-Nachweise byteidentisch. Separate study-v1-Worktrees unverändert |
| Produktive Ausgaben | Alle 70 ursprünglichen _book/_freeze/.quarto-Dateien und das Inventar identisch; keine neuen generierten Dateien im Schreibrepository |
| KI-Historie | Alte KI-/Logbytes und Originalprompts/Berichte erhalten; neuer D.9-Nachtrag und eine neue Logzeile, Prompt byteidentisch |
| Git | HEAD/dev/Git-Index identisch; kein Staging, Commit, Push, Merge, Reset oder Clean |

Originalquellen-Hashes und Ausführungs-/Testbelege liegen extern in `C:\Users\modic\AppData\Local\Temp\codex-fachkorrekturen-phase2-2026-10-12-9lr8x8_5`. Die wesentlichen Zahlen/Quellstellen stehen hier vollständig. Quellenkontrolle beschränkt sich auf beauftragte Fundstellen; keine pauschale erneute Seitenfreigabe sämtlicher Literaturbelege.

### Kontrollierte Originaldateien

| Beleg | Vollständiger Pfad | SHA-256 |
|:---|:---|:---|
| Kommer, Souverän investieren (2025), Abschnitt 9.2 | `C:\Users\modic\Zotero\storage\A8Q9SBUT\Kommer - 2025 - Souverän investieren mit Indexfonds und ETFs Ein Investmentbuch für fortgeschrittene Privatanleger.pdf` | `bc8812c64e9aab82a13c6cce02cbaa479940be2c778e6916426f1ae7ebd54ef6` |
| McKinney (2022), Kapitel 11/Datumskonvertierung | `C:\Users\modic\Zotero\storage\PJA9S9HY\McKinney - 2022 - Python for data analysis data wrangling with pandas, NumPy, and Jupyter.pdf` | `2676c3991593a8c27f6aa90809f93e4d018d11ff86cc6267816e5a79d2ba33b9` |
| BFS, gespeicherte Originalseite Preise | `C:\Users\modic\Zotero\storage\8NRJRVVL\preise.html` | `25c8d270939c941fa82c7e7e8dfac636918df346e591d993978e22928654dcfb` |

Der EPUB-Seitenumfang 192 wurde zusätzlich aus dem tatsächlichen OPF-Feld dc:format bestätigt. Abschnittslocatoren vermeiden die ungeprüfte Gleichsetzung von Datei- und Druckseite. Der vollständige Stufe-2-Bericht und Phase-2-Bericht bleiben als historische Nachweise byteidentisch.

## 5. Externe Renderprüfung

Alle drei Quarto-Läufe ausschliesslich in `C:\Users\modic\AppData\Local\Temp\codex-fachkorrekturen-phase2-2026-10-12-9lr8x8_5\render-project`. Vor jedem Start tatsächlichen Arbeitsort und _book-Ziel geprüft. Nur in dieser Kopie execute.enabled:false/freeze:false; --no-execute/--no-cache, für PDF latex-auto-install:false. _quarto.yml im Schreibrepository unverändert.

```text
quarto render --to html --no-execute --no-cache
quarto render --to pdf --no-execute --no-cache --no-clean -M latex-auto-install:false -M latex-clean:false -M keep-tex:true
quarto render --to docx --no-execute --no-cache --no-clean
```

| Format/Prüfung | Ergebnis |
|:---|:---|
| HTML | Exit 0; 11 Buchseiten, 1769 lokale href/src/Ankerziele, 0 ungültig, 0 doppelte IDs. Neuer D.9-Nachtrag in Inhalt/Navigation/TOC |
| LuaLaTeX-PDF | Exit 0; 108 Dateiseiten, 0 LaTeX-/Glyphen-/undefinierte Referenzfehler |
| DOCX | Exit 0; Projekt-Nachbearbeitung erfolgreich. 95 Formeln/23 Tabellen/8 Bilder; identische Formel-/Tabellen-/Bildobjekte gegenüber vorhandenem Vergleichsexport |
| Zusätzlicher paketierter DOCX-Prüfrenderer | Fehlgeschlagen: LibreOffice soffice.exe fehlt; keine Installation |
| Microsoft-Word-Ersatzprüfung | Installiertes Word unsichtbar, DOCX schreibgeschützt, Felder/TOC im Speicher aktualisiert, ohne Speichern geschlossen; Prüf-PDF 91 Seiten |

LaTeX verbleiben 21 Layoutmeldungen (keine Kompilationsfehler):

```text
Underfull \vbox (badness 10000) detected at line 1413
Underfull \vbox (badness 10000) detected at line 1413
Overfull \hbox (0.11806pt too wide) in alignment at lines 2619--2637
Overfull \hbox (0.11806pt too wide) in alignment at lines 2637--2639
Overfull \hbox (0.11806pt too wide) in alignment at lines 2639--2648
Overfull \hbox (0.11806pt too wide) in alignment at lines 2733--2751
Overfull \hbox (0.11806pt too wide) in alignment at lines 2751--2753
Overfull \hbox (0.11806pt too wide) in alignment at lines 2753--2758
Overfull \hbox (0.11806pt too wide) in alignment at lines 2806--2824
Overfull \hbox (0.11806pt too wide) in alignment at lines 2824--2826
Overfull \hbox (0.11806pt too wide) in alignment at lines 2826--2833
Overfull \hbox (0.11806pt too wide) in alignment at lines 2901--2919
Overfull \hbox (0.11806pt too wide) in alignment at lines 2919--2921
Overfull \hbox (0.11806pt too wide) in alignment at lines 2921--2928
Underfull \hbox (badness 4713) in paragraph at lines 3291--3297
Underfull \vbox (badness 10000) detected at line 4299
Underfull \vbox (badness 10000) detected at line 4299
Underfull \vbox (badness 10000) detected at line 4299
Underfull \vbox (badness 10000) detected at line 4299
Underfull \vbox (badness 10000) detected at line 4299
Underfull \vbox (badness 10000) detected at line 4299
```

Alle Seiten beider PDF-Darstellungen wurden mit Poppler als PNG gerastert; vollständige Seitenübersichten sowie gezielte Detailansichten der geänderten Fachstellen, Originaltabellen/-grafiken, Literatur und KI-Nachtrag geprüft. Dies ist keine Kontrolle jedes Zeichens bei 100 % Zoom. Keine abgeschnittenen Tabellen, fehlenden Formeln/Bilder oder Überlagerungen gefunden. Geänderte Stellen in den endgültigen Detailansichten bestätigt: PDF 9/12/16/23/29–30/93–94/107–108, Word 27/80/91; ergänzend sämtliche 108 PDF- und 91 Word-Seiten in Übersichten. Literatur PDF 62–64, Word 55–56 vor Anhang A. Die ursprünglichen Formatvorlagen/Filter blieben unverändert. Zwölf Overfull-Meldungen haben jeweils nur 0,11806 pt Überbreite; neun Underfull-Meldungen betreffen Satzverteilung. Externe URLs sind Quellenbelege; die automatische HTML-Prüfung überprüft lokale Ziele, keine vollständige Erreichbarkeitsgarantie aller historischen Internetseiten.

Nach der letzten Präzisierung von valley als Tiefpunktdatum wurden HTML/PDF/DOCX vollständig erneut gerendert und deren endgültige Quellen-/Ausgabestände geprüft. Ein externer Kopierhelfer stoppte nach erfolgreichem HTML-Render (Quarto Exit 0), weil html-final bereits existierte; ausschliesslich die Sicherungskopie mit erlaubtem Überschreiben vervollständigt. Das ist kein Quarto-Renderfehler. Finale lokale HTML-Ziele erneut vollständig geprüft.

## 6. Geänderte Dateien und Abschluss

Bestehende Dateien:

- `notebooks/Theorie.ipynb`
- `notebooks/Anhang_Datenaufbereitung.ipynb`
- `notebooks/Anhang_Tests_Validierung.ipynb`
- `src/funktionen.py`
- `references.bib`
- `documentation/ai-usage/ai-usage-log.md`
- `ki-nutzung.qmd`

Neu:

- `documentation/fachkorrekturen-phase2-2026-10-12.md`
- `documentation/ai-usage/prompts/2026-10-12-fachkorrekturen-phase2.txt`

KI-Arbeit getrennt dokumentiert: fachliche Erklärungs-/Textkorrekturen, Originalquellenkontrolle, lokale Programmkorrektur, tatsächliche isolierte Beispielausführung und Integritäts-/Renderprüfung. Keine persönliche Autorenfreigabe. Keine Datenbeschaffung, Paketdownloads/-installation oder neuen Studienläufe. Historische Nachweise bleiben unverändert.

Endkontrolle: Genau sieben vorhandene Dateien und zwei neue Nachweise im Git-Arbeitsbaum. **80 von 87** ursprünglichen versionierten Dateien und **151 von 158** gesicherten Arbeitsdateien byteidentisch. Alle **70** vorhandenen Ausgabe-/Freeze-/Cachedateien und alle **30** Ergebnisdateien sowie ihre Inventare identisch; ursprüngliche Sicherung vollständig bestätigt. Aktuelle Render-Eingaben (neun Notebooks, KI-Anhang, Bib und lokale Hilfsdatei) entsprechen bytegenau dem Schreibstand, ausser der bewusst nur extern deaktivierten Ausführungs-/Freeze-Konfiguration. Finaler Haupttext erneut direkt aus den Quellen gezählt: **7’959 / 7’834**, Reserve **41** mit Überblick. Git-Diff ohne Whitespacefehler. HEAD/dev/Git-Index identisch, kein Staging oder Git-Schreibvorgang.

Autorenkontrolle und fachliche Gesamtfreigabe bleiben ausstehend. Die separat offenen R-008/R-012/R-016/R-017 wurden nicht bearbeitet. **STOPP.**
