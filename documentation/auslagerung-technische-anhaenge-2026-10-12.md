# Technische Dokumentation in die Anhänge ausgelagert

Datum: 12. Oktober 2026, Europe/Zurich. Bearbeitung durch Codex; Autorenkontrolle ausstehend.

Die technische Planung, die ausführliche Datenaufbereitung und die vorhandenen Prüf- und Ausführungsnachweise stehen jetzt in drei Notebook-Anhängen. Der Haupttext enthält weiterhin die wissenschaftliche Untersuchung, ihre Vergleichsregeln, Parameter, Ergebnisse und Interpretation. Sein Umfang sinkt nach derselben Zählmethode von **14’838 auf 11’886 Wort-/Zahlentoken ohne Überblick** beziehungsweise von **15’694 auf 12’742 mit Überblick**. Die Obergrenze von 8’000 ist damit noch nicht erreicht.

Codex hat vorhandene Inhalte strukturell ausgelagert, kurze Zusammenfassungen und Anhangseinleitungen formuliert sowie die technische Prüfung und Dokumentation erstellt. **Die wissenschaftlichen Ergebnisse wurden nicht neu erarbeitet.** Es fanden keine Notebook-Codeausführung, Datenbeschaffung, Backtests oder Änderungen von Studienkonfigurationen statt.

## 1. Ausgangszustand und Auftrag

Arbeitsort war das normale Repository `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027`, Branch `dev`, HEAD **`7a166fbb80fb3c83dfab763e2134bd361f14b170`**. Der Git-Arbeitsstand war zu Beginn sauber. In den geprüften Projekt- und übergeordneten Verzeichnissen lagen keine `AGENTS.md`-Anweisungen vor. HEAD, Branch und Git-Index blieben unverändert; kein Staging, Commit, Push, Merge, Reset oder Clean.

Die vom Autor im Auftrag wiedergegebene Antwort von Herrn Mock lautet:

> Lagern Sie die technische Dokumentation, die Beschreibung der Datenaufbereitung sowie den Testbericht in den Anhang aus. Der Anhang zählt nicht zum Umfang.

Dies erlaubt die Auslagerung der ausführlichen Implementierungsbeschreibung, jedoch keine beliebige Kürzung der wissenschaftlichen Untersuchung. Daher bleiben insbesondere die vollständige Daten- und Parameterfestlegung in 5.10, die wesentlichen Durchführungsschritte in 5.11 sowie Ergebnisse und Interpretation in 5.12/5.13 im Haupttext. Das Überblickskapitel bleibt als Kapitel 1 bestehen.

Gelesen wurden die vollständigen Analyse-, Methodik-, Theorie- und Überblick-Notebooks, die Buchkonfiguration, der [Gegenlesebericht aus Phase 2](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/documentation/gesamtgegenlesen-phase2-2026-10-12.md), der [Formatierungsbericht aus Phase 1](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/documentation/formatierung-gesamtbuch-2026-10-12.md) sowie die KI-Regeln und die Arbeitsanweisung `KI-DOKUMENTATION-BUCH-SYNC`.

Die 76 versionierten Ausgangsdateien wurden ausserhalb des Repositorys gesichert; zusätzlich wurden die SHA-256-Werte der 70 vorhandenen Dateien in `_book`, `_freeze` und `.quarto` erfasst. Prüfordner: `C:\Users\modic\AppData\Local\Temp\codex-auslagerung-2026-10-12-bk_s81hh`. Der separate Engine-Worktree auf `study-v1` wurde nicht bearbeitet. Die Ausnahme bei einer erzeugten DOCX-Datei ist in Abschnitt 7 ausdrücklich dokumentiert.

## 2. Neue Anhänge und Buchstruktur

| Anhang | Notebook | Inhalt |
|---|---|---|
| A | [Anhang_Technische_Engine.ipynb](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Anhang_Technische_Engine.ipynb) | Entwicklungsreihenfolge, Einstellungen, Ergebnisvertrag, Engine-Struktur, Übergabe an Codex und Darstellungscode der Ergebnisgrafiken |
| B | [Anhang_Datenaufbereitung.ipynb](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Anhang_Datenaufbereitung.ipynb) | Datenverträge, Quellenadapter, Formate, Roh-/Verarbeitungsdaten, Resampling, Beschaffung und Normalisierung |
| C | [Anhang_Tests_Validierung.ipynb](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Anhang_Tests_Validierung.ipynb) | Geplante Eingangsregeln, fehlende Werte, WEO-Eingangsprüfung, dokumentierte Ausführung und Gegenrechnung |
| D | [ki-nutzung.qmd](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/ki-nutzung.qmd) | Bisheriger KI-Anhang mit neuem Nachtrag zu diesem Auftrag |

Die Reihenfolge in `_quarto.yml` ist Hauptkapitel 1–6, Literaturverzeichnis, Anhänge A–D. Die neuen Notebooks besitzen eine Raw-YAML-Titelzelle und native Markdown-Überschriften mit stabilen Abschnitts-IDs. Quarto erzeugt ihre Anhangsnummern automatisch. Die übernommenen Überschriften verlieren ihre alten manuellen `5.*`-Nummern; ihre Titel bleiben erhalten.

Die Hauptabschnitte **5.1 bis 5.13 bleiben lückenlos**. In 5.2–5.9 stehen jetzt kurze Zusammenfassungen unter den bisherigen Abschnittsnummern. Auch 5.11.1/5.11.2 bleiben als Zusammenfassungen erhalten. Damit bleiben vorhandene Verweise aus Methodik und Fazit auf die Hauptkapitel gültig. In Methodik wurde nur der strukturelle Zuordnungsabsatz, Zelle `053fb431`, angepasst. Die übrigen Methodik-Zellen bleiben identisch.

Für DOCX wurde ausschliesslich die Option `format.docx.crossref.appendix-title: Anhang` ergänzt: Die tatsächlich erzeugten Word-Überschriften zeigen dadurch ebenfalls «Anhang A» bis «Anhang D». Die Formatierungsfilter, CSS-/SCSS-Dateien und Word-Vorlage aus Phase 1 wurden nicht geändert.

## 3. Zuordnung der Originalabschnitte

Die Zellindizes beziehen sich auf das ursprüngliche Analyse-Notebook und beginnen bei 0. Jeder der 269 ursprünglichen Analyse-Zell-IDs ist genau einmal in den vier heutigen Analyse-/Anhangsnotebooks vorhanden. Gemischte Zellen wurden nicht durch das Abtrennen fachlicher Absätze neu formuliert.

| Ausgangsstelle | Originalzellen | Ziel in der Buchausgabe | Im Haupttext erhalten |
|---|---|---|---|
| 5.2 Reihenfolge der technischen Entwicklung | 3–5 | A.1 | Kurze Beschreibung des Aufbaus mit Verweis |
| 5.3 Entwicklung eines einheitlichen Datenformats | 6–33 | B.1 | Bedeutung des gemeinsamen Formats für vergleichbare Berechnungen |
| 5.4 Datenquellen und Umwandlung | 34–46 | B.2 | Quellenwahl und einheitliche Umwandlung zusammengefasst |
| 5.5 Einleitung, 5.5.1 Rohdaten, 5.5.4 Resampling | 47–50, 55–56 | B.3, B.3.1–B.3.2 | Rohdatenbezug, Prüfung und Monatsfrequenz zusammengefasst |
| 5.5.2 Validierung, 5.5.3 fehlende Werte | 51–54 | C.1.1–C.1.2 | Wesentliche Qualitätsregeln in 5.5; konkrete Studiengrenzen weiterhin in 5.10 |
| 5.6 Veränderbare Einstellungen | 57–72 | A.2 | Allgemeine Konfigurierbarkeit; tatsächliche Parameter vollständig in 5.10 |
| 5.7 Einheitliches Ergebnisformat | 73–87 | A.3 | Gemeinsame Ergebnisbasis und Vergleichskennzahlen |
| 5.8 Grundgerüst der Simulationsengine | 88–102 | A.4 | Trennung der Verarbeitungsschritte zusammengefasst |
| 5.9 Vorbereitung der Implementierung | 103–110 | A.5 | Vorhandene Funktionen und dokumentierte KI-Unterstützung zusammengefasst |
| 5.10 Untersuchungsdaten und Parameter | 111–156 | **Unverändert in 5.10** | Vollständige Datenwahl, Universen, Laufvarianten, Annahmen und Grenzen |
| 5.11.1 Beschaffung und unveränderte Ablage | 158–161 | B.4 | Kurze Übersicht über Bezug, Rohdaten und Herkunftsnachweise |
| WEO-Eingangsprüfung aus 5.11.1 | 162 | C.2 | Datenwahl und ihre Grenzen weiterhin in 5.10 |
| 5.11.2 Normalisierung und Datenkontrolle | 163–166 | B.5 | Kurze Übersicht über Normalisierung, Prüfung und fixierten Datenstand |
| Ausführungs-/Gegenrechnungsnachweise aus 5.11 | 169, 173, 175–176 | C.3 | Durchführung 5.11.3, Programmstand, Laufübersicht, Provenienz und elf ausgewertete Strategiereihen |
| Darstellungscode in 5.12 | Codezelle 181 und sieben spätere Plotaufrufe | A.6–A.6.1 als sichtbare Code-Dokumentation | Originalcodezellen physisch erhalten; Tabellen, sieben Grafiken und deren Erklärung weiterhin in 5.12 |
| Ergebnistext 5.12 und Interpretation 5.13 | 177–268 | **Unverändert im Haupttext**, ergänzt um einen Anhangsverweis | Alle Originaltexte, Ergebnistabellen, Abbildungen und Interpretation |

Im ursprünglichen 5.11 verbleiben zusätzlich die Zellen 157, 167–168, 170–172 und 174. Die Tabellenzeile zur Ergebnisdarstellung bezeichnet eine Änderung der Ausgabe des Codes; die ursprünglichen Quellen dieser Zellen wurden nicht verändert.

Anhang C enthält den **vorhandenen** Prüf- und Nachweistext. Er ist kein neu durchgeführter vollständiger Testbericht der Engine. Geplante Prüfregeln und bereits dokumentierte Nachweise bleiben unterscheidbar. Neue Tests oder zusätzliche Prüfergebnisse wurden nicht erfunden.

## 4. Codeabhängigkeiten und Darstellung der Grafiken

Das Long-/Wide-Beispiel besteht aus den beiden Codezellen `03390b5c` und `f2805855`. Die erste importiert Pandas/StringIO und erzeugt `markt_long`; die zweite verwendet dieses Objekt. Beide stehen in dieser Reihenfolge zusammen in B.1. Der Konfigurationscode `d7ee4cd7` mit seiner gespeicherten JSON-Ausgabe steht in A.2. Diese drei Zellen wurden einschliesslich IDs, Code, Metadaten, Execution Counts und Ausgaben unverändert verschoben.

Die Ergebnisgrafiken hängen von der umfangreichen Import-/Lade-/Funktionszelle `99cad7ec` ab. Diese Zelle und die sieben nachfolgenden Plotzellen bleiben physisch und in ursprünglicher Reihenfolge im Analyse-Notebook. Die YAML-Ausgabeoption `execute.echo: false` blendet ihre Quellen im Haupttext aus; die sieben gespeicherten PNG-Ausgaben bleiben sichtbar.

A.6 bindet die unveränderte Originalzelle mit `{{< embed Analyse.ipynb#99cad7ec echo=true >}}` ein. A.6.1 dokumentiert die sieben Originalaufrufe wörtlich in einem gewöhnlichen Markdown-Codeblock. Dieser Block ist nicht ausführbar und erzeugt keine zweite Ausgabe der Grafiken. So erscheint die technische Beschreibung im Anhang, während die Notebook-Abhängigkeiten bestehen bleiben. Die Einbindung anhand einer Zell-ID und die Option `echo=true` sind in der [offiziellen Quarto-Dokumentation](https://quarto.org/docs/authoring/notebook-embed.html) beschrieben.

Die HTML-Ausgabe des Analysekapitels enthält sieben PNG-Grafiken und keinen sichtbaren Python-Quellblock. A.6 enthält den zugehörigen Darstellungscode und keine Grafikduplikate. Der ursprüngliche Hinweis zur Herkunft der Grafiken bleibt in 5.12 erhalten; ein zusätzlicher Satz verweist auf A.6. Die unveränderten Funktionen wurden statisch auf Abhängigkeiten geprüft und nicht ausgeführt.

## 5. Wortzahlen und Zählmethode

Gezählt wurde vor und nach der Umgliederung identisch aus den Markdown-Quellen. Die Methode reproduziert die **14’838** aus Phase 2. «Wörter» bezeichnet hier Wort-/Zahlentoken nach dem Muster `\b\w+(?:[’'-]\w+)*\b`, einschliesslich Zahlen, Listen und kurzen Quellenhinweisen im Fliesstext.

Ausgeschlossen sind Raw-Zellen/YAML, ausführbare Codezellen, gespeicherte Outputs und Bildinhalte, Markdown-Codeblöcke, HTML-`pre`-Blöcke, Überschriften, Markdown-Tabellenzeilen, Display- und Inline-Mathematik sowie Zitationsklammern und technische `@sec-...`-Kennungen. Sichtbare Linktexte zählen; URL-Ziele und HTML-Tags zählen nicht. Die gerenderte Bibliographie und von Citeproc erzeugte Fussnoten gehören nicht zu dieser Haupttextzählung. Kurze inline gesetzte Bezeichner im Fachtext zählen dagegen als Wörter. Dies ist keine Behauptung einer identischen Microsoft-Word-Zählung oder einer abschliessend schulisch bestätigten Zählkonvention.

| Hauptkapitel | Vorher | Nachher | Veränderung |
|---|---:|---:|---:|
| 1 Überblick | 856 | 856 | 0 |
| 2 Einleitung | 785 | 785 | 0 |
| 3 Theorie | 3’670 | 3’670 | 0 |
| 4 Methodik | 1’068 | 1’080 | +12 |
| 5 Analyse | 8’363 | 5’399 | −2’964 |
| 6 Fazit | 952 | 952 | 0 |
| **Haupttext ohne Überblick** | **14’838** | **11’886** | **−2’952** |
| **Haupttext einschliesslich Überblick** | **15’694** | **12’742** | **−2’952** |

| Ausserhalb des Haupttexts | Übernommener Originaltext | Heutiger Umfang |
|---|---:|---:|
| A technische Engine und Darstellungscode | 976 | 1’067 |
| B Datenbeschaffung und Aufbereitung | 1’908 | 1’954 |
| C Tests und Nachweise | 508 | 555 |
| **Neue technische Anhänge insgesamt** | **3’392** | **3’576** |
| Übriger Anhang: KI-Dokumentation | 1’540 vorher | 1’680 nachher |

Die **3’392** übernommenen Originaltoken erklären nicht allein die Nettoentlastung: Die neuen Zusammenfassungen und Verweise im Analyse-Haupttext umfassen 428 Token, die Methodik-Anpassung zusätzlich 12. Somit beträgt die Entlastung `3’392 − 428 − 12 = 2’952`. Die 184 zusätzlichen Token in den technischen Anhängen stammen aus Einleitungen und der Erklärung zur Codeeinbindung; Quellcode und Überschriften zählen dort ebenfalls nicht.

Die Markdown-Quellen der Hauptkapitel enthalten vor den genannten Ausschlüssen 20’313 Token vorher und 15’835 nachher. Davon entfallen 4’619 beziehungsweise 3’093 auf ausgeschlossene Bestandteile/Markup. In den technischen Anhängen stehen vor den Ausschlüssen 5’255, danach 3’576 Token. Diese Differenzen sind keine saubere Aufteilung in «Codewörter» und «Formelwörter»: Sie enthalten auch Markup und Überschriften. Separat nachgewiesen sind 28 ausführbare Codezellen, 28 Outputobjekte, acht gespeicherte PNGs und 95 mathematische Ausdrücke; sie werden nicht zum Fliesstext gerechnet. Der Änderungsbericht und das ausführliche KI-Log sind Repository-Dokumentation und keine Buchkapitel.

Die genaue Ausschlussfolge lässt sich mit folgendem Kern nachvollziehen, angewandt auf die aneinandergehängten Markdown-Zellquellen; für QMD wird zuerst das YAML-Frontmatter entfernt:

```python
import html, re
s = re.sub(r'(?ms)^\s*```[^\n]*\n.*?^\s*```\s*$', ' ', s)
s = re.sub(r'<pre\b[^>]*>.*?</pre>', ' ', s, flags=re.S | re.I)
s = re.sub(r'<h[1-6]\b[^>]*>.*?</h[1-6]>', ' ', s, flags=re.S | re.I)
s = re.sub(r'(?m)^\s*#{1,6}\s+.*$', ' ', s)
s = re.sub(r'(?m)^\s*\|.*\|\s*$', ' ', s)
s = re.sub(r'\$\$.*?\$\$', ' ', s, flags=re.S)
s = re.sub(r'(?<!\\)\$[^$\n]*?(?<!\\)\$', ' ', s)
s = re.sub(r'\[[^\]]*@[^\]]*\]', ' ', s)
s = re.sub(r'(?<!\w)@sec-[\w-]+', ' ', s)
s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
s = html.unescape(re.sub(r'<[^>]+>', ' ', s))
n = len(re.findall(r"\b\w+(?:[’'-]\w+)*\b", s))
```

## 6. Integrität und Renderkontrollen

Die Kontrollen vergleichen den aktuellen Stand mit den gesicherten Ausgangsdateien, nicht nur mit der Git-Differenz.

| Kontrolle | Ergebnis |
|---|---|
| Ursprüngliche Notebook-Zellen | Alle **467** IDs genau einmal erhalten; jetzt **499** Zellen in neun Notebooks durch neue Titel-/Einleitungs-/Zusammenfassungszellen |
| Analyse vollständig | Alle 269 Originalzellen erhalten; an verschobenen Fachtexten nur Überschriften geändert, nicht ihre Textkörper |
| Code/Outputs | Alle **28 Codezellobjekte strukturell identisch**, einschliesslich IDs, Metadaten, Execution Counts und gespeicherten Ausgaben; **28 Outputobjekte**, acht PNGs erhalten |
| Haupttextschutz | Index, Einleitung, Theorie und Fazit byteidentisch; alle Originalzellen von 5.10 und 5.12/5.13 unverändert; Methodik nur ein struktureller Absatz geändert |
| Formeln und Zitationen | Multimengenvergleich: **95** Mathematikausdrücke und **157 aktive Zitationsvorkommen mit 29 Keys** unverändert; das wörtliche Zitationsbeispiel im Überblick-Codeblock ist keine aktive Zitation |
| Bibliographie | `references.bib` mit 52 Einträgen und CSL-Datei byteidentisch; 29 verwendete Werke in der Bibliographie erhalten |
| Notebook-Schema | Alle neun Notebooks mit `nbformat.validate` erfolgreich geprüft |
| Fachliche Studienartefakte | Alle **30** versionierten Dateien unter `results/study_v1` SHA-256-identisch; `_freeze`, `src/funktionen.py`, vorhandene Konfigurationen und historische Nachweise unverändert |
| DOCX-Objektvergleich | Alle 95 Mathematikobjekte, 23 Tabellen-Zelltextfolgen und acht Bildhashes gegen die Phase-1-Ausgabe erhalten; Reihenfolge darf durch Auslagerung wechseln |
| Verweise | 14 neue Haupttext-Querverweise vollständig aufgelöst; alle 14 internen DOCX-Hyperlinkziele vorhanden; **1’554** lokale HTML-Datei-/Ankerlinks ohne ungültiges Ziel |
| Git | Branch, HEAD und Index unverändert; `git diff --check` erfolgreich |

Die endgültigen Autorenquellen wurden in einer **externen temporären Projektkopie** mit `execute.enabled: false`, `freeze: false`, `--no-execute` und `--no-cache` geprüft. Die PDF-Prüfung schaltete automatische LaTeX-Paketinstallation aus. Die produktive Ausführungs-/Freeze-Konfiguration wurde nicht dauerhaft verändert. Der vorhandene DOCX-Nachbearbeitungsfilter lief; er führt keine Notebook-Zellen aus.

| Format | Endgültiger Prüfstand |
|---|---|
| HTML | Quarto Exit 0; Navigation, Anhangshierarchie, DOM, Bilder, Mathematik und lokale Links geprüft. Hauptkapitel 1–6, A–D und Ergebnisabschnitte korrekt. |
| PDF | Quarto/LuaLaTeX Exit 0; **111 physische Seiten**; keine LaTeX-Fehler, fehlenden Zeichen oder undefinierten Verweise. |
| DOCX | Quarto Exit 0; deutsch beschriftete Anhänge und interne Ziele korrekt; schreibgeschützter Export mit installiertem Microsoft Word ergab **97 physische Seiten**. |

Im endgültigen LaTeX-Protokoll verbleiben **20 Layout-Hinweise**: zwölf `Overfull hbox` von 0,11806 pt an den vier breiten Ergebnistabellen, eine `Overfull hbox` von 1,09496 pt, eine `Overfull vbox` von 1,25362 pt sowie sechs `Underfull vbox` am langen Darstellungscode in Anhang A. Sie verhindern den Build nicht und wurden nicht durch weitere globale Formatänderungen unterdrückt.

Die erste umgegliederte PDF-/Word-Prüffassung wurde vollständig in Seitenübersichten angesehen und an Formeln, Abläufen und Datenbeispielen im Detail geprüft. Nach der abschliessenden Verlagerung der sichtbaren Plotquellen wurden die betroffenen endgültigen Bereiche erneut visuell kontrolliert: PDF physisch 78–93, Word 69–91 sowie der Ergebnisbeginn mit Tabelle und Grafik (PDF 60–61, Word 54–55). Detailkontrollen betrafen insbesondere PDF 87/91 und Word 81. In diesen Ansichten waren keine abgeschnittenen Texte/Bilder oder überlappenden Elemente erkennbar. Diese Kombination aus Übersicht und gezielter Nachprüfung ersetzt keine abschliessende Autorenprüfung jeder Seite.

Der vorgesehene LibreOffice-basierte DOCX-Renderer war wegen fehlendem `soffice.exe` nicht nutzbar. Die Sichtprüfung erfolgte deshalb über das tatsächlich installierte Microsoft Word in einer privaten, unsichtbaren, schreibgeschützten Instanz. Felder und Inhaltsverzeichnis wurden nur dort aktualisiert, anschliessend als Prüf-PDF exportiert und das DOCX ohne Speichern geschlossen.

## 7. Abweichung bei einem Renderlauf und Wiederherstellung

**Eine Schutzvorgabe wurde bei einem Zwischenlauf verletzt:** Ein DOCX-Prüflauf wurde versehentlich mit dem Repository als Arbeitsverzeichnis gestartet. Dadurch wurden die vorhandene ignorierte `_book`-DOCX und vier Quarto-Cachedateien überschrieben; drei neue Anhangs-Indexdateien kamen hinzu. Der Lauf verwendete ebenfalls `--no-execute`; Notebook-Code und Backtests liefen nicht. Dieser Fehler wurde dem Autor während der Bearbeitung mitgeteilt.

Die vier vorhandenen Cachedateien wurden anhand der Ausgangssicherung und einer Rekonstruktion **byteidentisch zu ihren anfänglichen SHA-256-Werten wiederhergestellt**. Die drei neu entstandenen Indexdateien wurden gezielt entfernt. Die Zeitstempel der vier rekonstruierten Cachedateien wurden zurückgesetzt, damit Quarto sie bei Bedarf erneuert; ihre Inhalte sind identisch. Das Dateiinventar in `_book`, `_freeze` und `.quarto` enthält abschliessend wieder dieselben 70 Dateien.

Die ursprünglichen Bytes der überschriebenen `_book/Langfristige-Anlagestrategien-anhand-historischer-Finanzdaten.docx` waren nicht gesichert und liessen sich nicht exakt rekonstruieren. An ihrem Pfad liegt deshalb eine **erneut aus sämtlichen gesicherten Ausgangsquellen erzeugte DOCX des Ausgangsbuchs**, ohne Notebook-Ausführung. Sie ist nicht die neu umgegliederte Prüfausgabe und nicht byteidentisch zur früheren DOCX. Ausgangs-SHA-256: `eaa4fe401ae58f8a3c44edc3b4cddd597351feedfb4e43907b35c32ce85ac8de`; jetzige SHA-256: `99e62bddcad332db905acdf1c9ffbcd0fb2c45107c24a57d8a00cc6ae4f58b41`.

Damit sind **69 von 70 vorhandenen Cache-/Ausgabedateien inhaltlich byteidentisch**, mit genau dieser einen bekannten DOCX-Ausnahme. Studienresultate, eingefrorene Daten, ursprüngliche PDF-/HTML-Ausgaben und wissenschaftliche Quellen wurden durch den Zwischenlauf nicht verändert. Alle weiteren und endgültigen Renderprüfungen erfolgten ausserhalb des Repositorys. Die Schutzvorgabe «keine Änderung ausserhalb des Aufgabenbereichs» ist wegen dieses Vorfalls nicht uneingeschränkt erfüllt; eine vollständige Byte-Wiederherstellung aller Ausgabedateien wird ausdrücklich nicht behauptet.

## 8. Überblickskapitel und weitere Kürzung

`index.ipynb` bleibt vollständig und byteidentisch als reguläres Kapitel 1 erhalten. Seine Installationserklärungen, Quarto-/Zotero-Hinweise, Repository-Struktur, Arbeitsabläufe und Aufgabenlisten passen überwiegend zur README beziehungsweise zur technischen Projektdokumentation. Die Empfehlung lautet, diese später dorthin zu verlagern und Kapitel 1 auf ungefähr 150 Wörter zu Projektziel und Aufbau zu begrenzen. Kapitel 1 sollte dabei als Kapitel bestehen bleiben, um die Nummern aller folgenden Kapitel zu erhalten. Dies wurde nicht umgesetzt.

Ohne Überblick fehlen noch **3’886 Wörter** bis zur Obergrenze von 8’000; einschliesslich des unveränderten Überblicks fehlen **4’742**. Zusätzliche Kürzungen müssen gezielt abgestimmt werden. Ein möglicher Arbeitsrahmen ist:

| Kapitel | Jetzt | Möglicher Zielumfang | Ansatz für spätere Autorenentscheidung |
|---|---:|---:|---|
| Überblick | 856 | 150 | Technische Nutzungshinweise in README/Projektdokumentation; kurzer Kapitelkern bleibt |
| Einleitung | 785 | 650 | Motivation bündeln, Forschungsfrage und Ziele vollständig erhalten |
| Theorie | 3’670 | 2’100 | Vergleichsrelevante Definitionen/Formeln erhalten, wiederholte Erläuterungen und ausführliche Lernbeispiele prüfen |
| Methodik | 1’080 | 1’000 | Wiederholungen mit 5.10 vermeiden, Vergleichsregeln eigenständig lesbar erhalten |
| Analyse | 5’399 | 3’200 | Wiederholungen zwischen Datenfestlegung, Ergebniserklärung und Interpretation reduzieren; entscheidende Tabellen/Grafiken, Parameter und Grenzen erhalten |
| Fazit | 952 | 800 | Forschungsfrage beantworten, wiederholte Ergebnisbeschreibungen bündeln |
| **Ohne Überblick** | **11’886** | **7’750** | Vorschlag, keine ausgeführte Kürzung |
| **Mit Überblick** | **12’742** | **7’900** | Vorschlag, keine ausgeführte Kürzung |

Diese Zahlen sind Planungswerte, keine bereits inhaltlich ausgearbeitete Abgabefassung. Erst nach Prüfung der tatsächlich erforderlichen Aussagen sollte der Autor Absätze auswählen. Die Genehmigung zur technischen Auslagerung wird nicht als Genehmigung beliebiger weiterer Textstreichungen ausgelegt.

## 9. Offene Punkte, KI-Nachweis und Abschluss

Die fachlichen Korrekturen aus Phase 2 wurden nicht ausgeführt. Dessen Befunde bleiben grundsätzlich offen, insbesondere das Portfolio-Beispiel mit der gespeicherten Volatilität von 1,15 %, Quellen-/Seitenzuordnungen, Präzisierungen von Formeln und historischen KI-Nachweisen sowie die formalen Abgabeteile. R-002 ist durch die dokumentierte Anhangsgenehmigung und Umfangsentlastung teilweise adressiert; die Obergrenze bleibt überschritten. Die fehlende Zugänglichkeit versiegelter Eingangsdaten aus R-017 wurde durch diese Umgliederung nicht behoben.

Die bereits zuvor doppelte Beschreibung der eingefrorenen Gegenrechnung (R-013, ursprüngliche Zellen `a4355b5e` und `008ef22e`) steht jetzt unverändert in C.3. Ihre Entfernung wäre eine separate redaktionelle Korrektur und wurde nicht nebenbei vorgenommen. Auch die historische KI-Dokumentation wurde nicht durch unbelegte Ergänzungen neu zusammengesetzt. Titelseitenangaben, Abstract/Kurzfassung, Verzeichnisse, Eigenständigkeitserklärung und endgültige Fach-/Abgabekontrolle bleiben Autorenaufgaben.

Der [vollständige ausgeführte Prompt](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/documentation/ai-usage/prompts/2026-10-12-auslagerung-technische-anhaenge.txt) wurde byteidentisch gespeichert; SHA-256: `8f3c9550301cb1cd33f6222f625661fc2d0b8aad498ebfb56921bd7c22b117bb`. Das [laufende KI-Log](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/documentation/ai-usage/ai-usage-log.md) enthält den neuen Einsatz und den Render-Vorfall. Der vorhandene Buchanhang wurde um «Auslagerung der technischen Dokumentation» ergänzt. Alle bisherigen Log- und Buchnachweise bleiben als identischer Dateipräfix erhalten; der Abgleich wurde durch Codex ausgeführt. Eine abgeschlossene manuelle Autorenkontrolle wird nicht behauptet.

Geänderte versionierte Quellen: `_quarto.yml`, Analyse, Methodik, `ki-nutzung.qmd` und KI-Log. Neu: drei Anhangsnotebooks, dieser Bericht und die Promptkopie. Die übrigen 71 versionierten Ausgangsdateien sind byteidentisch. Zusätzlich besteht die dokumentierte Ausnahme bei der ignorierten erzeugten DOCX. Die Bearbeitung endet hier zur Autorenkontrolle, ohne weitere Kürzungen, Fachkorrekturen oder Git-Veröffentlichung.
