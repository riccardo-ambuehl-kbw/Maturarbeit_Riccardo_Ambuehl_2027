# Formatierung des gesamten Quarto-Buchs – 12. Oktober 2026

## Auftrag und Ausgangsstand

**PASS – technische Durchführung und Integrität. Autorenkontrolle OFFEN.** Dieser Einsatz betraf ausschliesslich die formale Gestaltung und technische Darstellungsprüfung, keine fachliche Verfassung, sprachliche Überarbeitung oder fachliche Gesamtvalidierung.

- Repository: `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027`.
- Branch: `dev`; tatsächlicher HEAD: `99ea85b415c58b70a0997d6f1b700babecbd0817`.
- Ausgangszustand: `git status --short` leer; Git-Index unverändert.
- Keine `AGENTS.md` im Projekt oder in den geprüften übergeordneten Verzeichnissen gefunden. Projektregeln aus `documentation/ai-usage/README.md`, `book-sync.md` und `documentation/readme-ueberblick-sync.md` berücksichtigt.
- Vollständiger Prompt: [2026-10-12-formatierung-gesamtbuch.txt](ai-usage/prompts/2026-10-12-formatierung-gesamtbuch.txt), byteidentisch mit der Benutzeranlage.
- Externe Sicherung, Hashmanifest, Ausgangskopien, Renderprotokolle und Sichtprüfungen: `C:\Users\modic\AppData\Local\Temp\codex-formatierung-2026-10-12_050019-4wq_blmx`. `manifest.json` erfasst 67 versionierte Dateien und 67 vorhandene Dateien aus `_book`, `_freeze` und `.quarto`; relevante Buchquellen wurden zusätzlich unter `baseline/` kopiert.

## Geprüfte Schulvorgaben

**PASS – zugängliche Vorgaben gelesen.** `documents/Leitfaden_MA_für_SuS_KBW_2026.pdf`, `Maturarbeit_Vorgaben_2027.pdf`, `EinführungMA_26.pdf` und `Matura_Vereinbarung_Riccardo_2027.pdf` wurden gelesen; extrahierte Texte liegen in der externen Sicherung.

Der Leitfaden verlangt beziehungsweise empfiehlt auf den PDF-Seiten 4–5 (gedruckte Seiten 2–3) vollständige Angaben auf der Titelseite, ein Abstract vor dem Inhaltsverzeichnis, römische Seitenzahlen für den Vorspann, arabische Textseiten ab 1, Blocksatz mit sauberer Trennung, gut lesbare Schrift in 11–12 pt und 1,2–1,5-fachen Zeilenabstand. Eine Serifenschrift und höchstens vier Überschriftenebenen werden empfohlen. Literaturverzeichnis und Anhänge sollen getrennt und in dieser Reihenfolge erscheinen. Abbildungs-/Tabellenverzeichnisse und eine abschliessende unterzeichnete Eigenständigkeitserklärung sind ebenfalls vorgesehen. Die Maturarbeitsvorgaben nennen 6000–8000 Wörter im Hauptteil und eine ansprechende, lesbare Gestaltung.

Diese Angaben begründen die gemeinsamen Druck-/Word-Einstellungen. Fehlende Autorenangaben und formale Textbestandteile wurden nicht erfunden oder ergänzt; siehe offene Punkte. Der bestehende Chicago-Zitierstil wurde beibehalten. Eine Bewertung von Umfang, Fachqualität oder endgültiger Abgabereife ist **NICHT GEPRÜFT**.

## Bestandsaufnahme und Änderungen

Die vorhandene Version liess sich bereits vor den Änderungen in HTML, PDF und DOCX rendern. Ein erfolgreicher Exit-Code allein belegte aber keine einheitliche Darstellung: 100 bereits nummerierte HTML-Zwischenüberschriften erschienen in Word als `BodyText`/`FirstParagraph` statt als Überschriften. Auch im PDF fehlte dadurch die reguläre Überschriftenformatierung und TOC-Einbindung. Das Theoriekapitel besass dagegen bereits 54 native, automatisch nummerierte Zwischenüberschriften.

Weitere konkrete Befunde: HTML-Stile berücksichtigten die vierte Überschriftenebene nicht ausdrücklich; lange Inline-Dateinamen, Ausgaben und Formeln benötigten geeignete Umbrüche beziehungsweise Scrollflächen. Die Word-Ausgangsdatei hatte keine ausdrückliche Seitengrösse in `sectPr`, Office-Themeschrift und deaktivierten Code-Zeilenumbruch. Das Literaturverzeichnis stand ohne eigenen Kapitelkopf am Ende des KI-Anhangs. Drei breite Ergebnistabellen verursachten PDF-Textüberbreiten bis 9,2388 pt.

**Acht Formatierungsverbesserungen wurden umgesetzt:**

| Bereich | Massnahme und Begründung | Geltungsbereich |
|---|---|---|
| Echte Zwischenüberschriften | Renderfilter erkennt ausschliesslich vorhandene nummerierte HTML-Überschriften h2–h4. Ihre Texte und Nummern bleiben erhalten; `unnumbered` verhindert eine zusätzliche Nummer. Bestehende IDs werden übernommen, fehlende Anker erhalten `abschnitt-…`. Native Theorie-Überschriften werden nicht umgeschrieben. | HTML/PDF/DOCX, global |
| Überschriftenhierarchie und Abstände | Gemeinsame HTML-Abstände und h4-Stil; echte Word-Vorlagen für Ebenen 1–4 mit Folgeabsatzbindung. KOMA `numbers=noenddot` vereinheitlicht die PDF-Nummern ohne nachgestellte Punkte. | HTML/PDF/DOCX |
| Drucktypografie | PDF: bestehende Serifenschrift, 11 pt, Zeilenabstand 1,2, A4 und 2,5 cm Ränder. Word: Times New Roman 11 pt, Blocksatz, 1,2-facher Zeilenabstand, A4, gleiche Ränder, Überschriften 16/13/11,5/11 pt. Office-Themeschrift wird zuverlässig überschrieben. | PDF/DOCX |
| Code, Ausgaben und lange Dateinamen | HTML-Ausgaben mit Umbruch und Abständen; vorhandenes Folding beibehalten. PDF-Verbatim-Ausgaben umbruchfähig; lange einfache Inline-Pfade mit `nolinkurl` umbrechbar. Word: Consolas 9 pt, heller Hintergrund und aktivierter Umbruch. Keine Codequelle geändert. | HTML/PDF/DOCX |
| Bilder und Mathematik im Browser | Bilder proportional auf verfügbare Breite begrenzt und zentriert; Display-Math erhält eine horizontale Scrollfläche für schmale Ansichten. Formeltexte und Bilddaten bleiben unverändert. | HTML |
| Breite Ergebnistabellen | Nur die vier sieben-spaltigen Vergleiche in Analyse 5.12.1–5.12.4 erhalten im PDF `small` und 4 pt Spaltenabstand. Damit verschwinden die bisherigen Überbreiten von 9,2388 beziehungsweise 4,14813 pt. Word erhält ungeteilte Tabellenzeilen und behält echte wiederholbare Kopfzeilen. | gezielt PDF; Word global |
| Vorspann und Seitenzählung | Titelblatt ohne sichtbare Nummer; Inhaltsverzeichnis römisch; erster Textteil arabisch ab 1. Word-Helfer setzt entsprechende Abschnitte, Seitenzahlfelder und automatische Trennung, vermeidet doppelte erste Kapitelumbrüche sowie auseinandergezogene Zeilen bei vorhandenen manuellen Zeilenumbrüchen. | PDF/DOCX |
| Literaturverzeichnis | Neue rein formale Seite `bibliography.qmd` mit unnummeriertem Titel und vorhandenem `refs`-Block, nach Fazit und vor KI-Anhang eingebunden. Inhalte stammen weiterhin unverändert aus derselben Bibliografie und CSL-Datei. | HTML/PDF/DOCX |

Es gab **keine lokalen Notebook-Änderungen**. Die besondere YAML-/HTML-Titelkonstruktion von `index.ipynb` blieb byteidentisch: HTML zeigt den Buchtitel und genau einen Überblick-Kapitelkopf; PDF und DOCX erzeugen jeweils genau ein erstes Kapitel. Die 154 vorhandenen Zwischenüberschriftentexte und ihre Reihenfolge blieben erhalten.

## Tatsächlich geänderte Dateien

| Datei | Änderung |
|---|---|
| `_quarto.yml` | Filter, Word-Helfer/-Vorlage, Druckeinstellungen, Seitenzählung und Literaturverzeichniseinbindung |
| `styles/styles.css` | Gemeinsame HTML-Abstände, h4, Code-/Textumbrüche, Mathematik-Scrollflächen und proportionale Bilder |
| `filters/book-format.lua` (neu) | Renderformatierung der vorhandenen Überschriften, langen Inline-Pfade und vier breiten PDF-Tabellen |
| `styles/build-reference-docx.py` (neu) | Nachvollziehbarer manueller Builder der Word-Vorlage aus Pandocs Standardvorlage; benötigt vorhandenes Quarto und python-docx |
| `styles/reference.docx` (neu) | Dauerhafte Word-Formatvorlage; kein Untersuchungsresultat |
| `filters/docx-layout.py` (neu) | Standardbibliothek-Helfer für die erzeugte DOCX-Datei: Abschnitte, Fusszeilen-/Seitenzählung, Tabellenzeilen und Word-Einstellungen |
| `bibliography.qmd` (neu) | Formaler Literaturverzeichnis-Kopf und Einfügeposition |
| `documentation/ai-usage/ai-usage-log.md` | Neuer Eintrag, ältere Bytes vollständig erhalten |
| `ki-nutzung.qmd` | Neue sachliche Zusammenfassung des Formatierungseinsatzes, Autorenkontrolle ausdrücklich ausstehend |
| `documentation/ai-usage/prompts/2026-10-12-formatierung-gesamtbuch.txt` (neu) | Vollständiger ausgeführter Originalauftrag |
| `documentation/formatierung-gesamtbuch-2026-10-12.md` (neu) | Dieser Abschlussbericht |

`styles/custom.scss` und `filters/date-icon.lua` wurden geprüft und blieben unverändert. Auch README, bestehende Arbeitsanweisungen und historische KI-Nachweise wurden nicht umgeschrieben. Alle Änderungen liegen im Arbeitsverzeichnis, nicht im Git-Index.

## Integritätskontrolle

**PASS – anhand der gesicherten Ausgangsdateien geprüft.**

| Notebook | Zellen | Codezellen | Gespeicherte Output-Objekte | PNGs |
|---|---:|---:|---:|---:|
| `index.ipynb` | 40 | 0 | 0 | 0 |
| `notebooks/Einleitung.ipynb` | 21 | 0 | 0 | 0 |
| `notebooks/Theorie.ipynb` | 86 | 17 | 18 | 1 |
| `notebooks/Methodik.ipynb` | 30 | 0 | 0 | 0 |
| `notebooks/Analyse.ipynb` | 269 | 11 | 10 | 7 |
| `notebooks/Fazit.ipynb` | 21 | 0 | 0 | 0 |
| **Gesamt** | **467** | **28** | **28** | **8** |

Alle sechs vollständigen Notebook-Dateien haben vor/nach der Bearbeitung denselben SHA-256. Das belegt unveränderte Markdown-/Raw-/Codequellen, Formeln, Tabellenwerte, Zitationen, Zell-IDs, Metadaten, Execution Counts, Outputs sowie etwaige eingebettete Attachments; es fand keine Notebook-Serialisierung statt. `nbformat.validate` bestand für alle sechs Dateien; alle Zell-IDs sind eindeutig. Einzelhashes und Zählungen stehen in `integrity.json` der externen Sicherung.

Von 67 ursprünglichen versionierten Dateien blieben 63 byteidentisch. Die vier erlaubten Änderungen sind Konfiguration, CSS, KI-Log und KI-Anhang. Dadurch sind insbesondere `references.bib`, CSL, `src/funktionen.py`, sämtliche versionierten Ergebnisdateien und Archive unverändert. Auch alle 67 gesicherten vorhandenen Cache-/Ausgabedateien sind byteidentisch. Der Git-Index wurde gegen den vollständigen ursprünglichen `git ls-files --stage`-Snapshot verglichen: identisch.

Zusätzliche Prüfungen der tatsächlichen Ausgaben:

- **PASS:** Texte und Reihenfolge aller 154 Zwischenüberschriften, aller 16 HTML-Tabellen und aller 95 HTML-Mathematikausdrücke entsprechen der Ausgangsausgabe. Davon sind 47 Display-Formeln. Kein ursprünglicher Anker der sechs Hauptkapitel ging verloren.
- **PASS:** Alle 100 zuvor nur als Text ausgegebenen Word-Zwischenüberschriften besitzen jetzt `Heading2`/`Heading3`/`Heading4`.
- **PASS:** Word-Mathematiktexte in 95 `oMath`-Objekten, Zelltexte in 23 OOXML-Tabellen und die Hashes aller acht Word-Bilder sind vor/nach identisch. Word bildet zusätzlich zu den normalen Tabellen auch Ablaufdarstellungen als Tabellen ab. Alle 869 Text-Runs des Word-Fussnotenbereichs und alle 29 ausgegebenen Bibliografieeinträge sind unverändert.
- **PASS:** Originalprompt byteidentisch kopiert; KI-Log nur angehängt; bestehende KI-Anhangtexte unverändert erhalten.
- **NICHT GEPRÜFT:** neue fachliche Richtigkeit, Reproduzierbarkeit der Berechnungen und neue Laufzeitergebnisse. Keine Codezelle, Engine, Datenbeschaffung oder Backtest wurde ausgeführt.

## Renderprüfung

**PASS – alle Formate in einer getrennten temporären Projektkopie.** Ausgeführt wurde nacheinander:

```text
quarto render --to html --no-execute --no-cache
quarto render --to pdf --no-execute --no-cache --no-clean -M latex-auto-install:false -M latex-clean:false -M keep-tex:true
quarto render --to docx --no-execute --no-cache --no-clean
```

Ein abschliessender PDF-Lauf mit denselben Flags prüfte zusätzlich `numbers=noenddot`; sein vollständiges LaTeX-Protokoll wurde als `final-pdf-tex.log` gesichert. Es wurden keine Pakete installiert, kein `tlmgr`-Update und keine automatische LaTeX-Installation ausgeführt. Der neue Post-Render-Helfer führt ausschliesslich Formatierung der erzeugten Word-Datei aus; `--no-execute` verhindert Notebook-Codeausführung. Vorhandene Cache- und `_book`-Dateien des Arbeitsrepositorys wurden nicht verwendet oder überschrieben.

Quarto ersetzt bei getrennten Formatrenderläufen die unterstützenden `figure-html`-/`figure-pdf`-Ordner. Deshalb wurde jede fertige Ausgabe sofort als `final-html`, `final-pdf` beziehungsweise `final-docx` gesichert. Die vollständige HTML-Kopie behält ihre acht Bilder; fertige PDF/DOCX wurden für die vorhandenen Downloadlinks zusätzlich dorthin kopiert. Ein vorübergehender Bildfehlbefund nach einem späteren PDF-Lauf war damit als Artefakt der Prüfkopie erklärt und behoben.

| Format | Status | Tatsächliche Prüfung |
|---|---|---|
| HTML | **PASS**, Exit 0 | Alle acht Buchseiten im vorhandenen Chrome geöffnet. Kapitelanfänge, Navigation, Hierarchie, Schriftgrössen, Formeln und Abbildungen geprüft; alle acht Bilder geladen. DOM-Breitenkontrolle aller Tabellen, Codeblöcke, Bilder und Display-Formeln bei 1440 px ohne Überstand. 1425 lokale Datei-/Ankerlinks geprüft, keine ungültigen Ziele. Sichtstichproben für MDD, Sharpe, Ergebnistabellen, Code-Folding und Literaturverzeichnis. |
| PDF | **PASS**, Exit 0 | LuaLaTeX, A4, 106 physische Seiten. Alle Seiten als PNG erzeugt; Seitenübersichten und ausgewählte vollständige Seiten geprüft. Titel/TOC, alle Kapitelanfänge, vierte Überschriftenebene, lange Codeblöcke, alle Diagramme, Tabellen, MDD und Sharpe, Literaturverzeichnis und KI-Anhang berücksichtigt. Keine leeren Seiten, fehlenden Zeichen, undefinierten Verweise oder LaTeX-Fehler festgestellt. |
| DOCX | **PASS**, Exit 0 | OOXML-Inhalte und Styles geprüft; im installierten Microsoft Word schreibgeschützt geöffnet. Felder und TOC ausschliesslich im Arbeitsspeicher aktualisiert, danach in ein temporäres 92-seitiges A4-PDF exportiert und ohne Speichern geschlossen. Alle Seiten rasterisiert; Seitenübersichten und ausgewählte vollständige Seiten einschliesslich Tabellen, Formeln, Code und Bildern kontrolliert. |

Der Standardhelfer `render_docx.py` konnte nicht rendern: `FileNotFoundError: LibreOffice soffice.exe was not found on PATH`. Dieser Weg ist **NICHT GEPRÜFT**; stattdessen fand die tatsächliche Word-Sichtprüfung mit dem bereits installierten Microsoft Word statt. Keine Installation wurde vorgenommen. Die erzeugte DOCX fordert beim Öffnen eine Feldaktualisierung an; die endgültigen TOC-Seitenzahlen hängen von der aktualisierten Word-Paginierung ab.

Geprüfte physische Kapitelanfänge im PDF: Überblick 6, Einleitung 12, Theorie 15, Methodik 45, Analyse 49, Fazit 96; Literaturverzeichnis 99, KI-Anhang 102. Im Word-Prüfexport: 7, 12, 14, 41, 45, 84; Literaturverzeichnis 87, KI-Anhang 89. Das sind physische PDF-Seiten, keine Textseitennummern. Der erste Textteil zeigt in beiden Formaten die Seitennummer 1. PDF-Vorspann i–iv, Word-Vorspann i–v. Keine identische Paginierung zwischen unterschiedlichen Ausgabeformaten wird behauptet.

Besondere Detailprüfungen: vollständige MDD-Zeitbereichsformel im PDF auf Seite 36 und in Word auf Seite 32; Sharpe-Zeichentabelle mit acht Einträgen auf PDF-Seite 39 und Word-Seite 35; breite Ergebnistabellen auf PDF-Seiten 82, 85, 86 und 88; mehrseitiger langer Analysecode auf PDF-Seiten 78–82 beziehungsweise Word-Seiten 69–72. Die Seitenübersichten dienen der Prüfung von Umbrüchen und Gesamtkomposition; eine fachliche Zeile-für-Zeile-Abnahme aller Seiten erfolgte nicht.

Prüfnachweise im temporären Ordner: `final-html.log`, `final-pdf.log`, `final-docx.log`, `render-project/index.log`, `render-status.json`, `integrity.json`, `structure-qa.json`, `html-qa.json`, Browser-Screenshots unter `html-qa/` und Rasterbilder unter `pdf-final-qa/` sowie `word-final-qa/`.

## Verbleibende Warnungen und offene Punkte

| Status | Punkt | Bedeutung / Folgearbeit |
|---|---|---|
| **OFFEN** | Zwölf `Overfull hbox`-Hinweise von jeweils 0,11806 pt in den vier breiten PDF-Tabellen | Rund 0,04 mm durch Spalten-/Linienrundung; kein sichtbares Abschneiden in den geprüften Tabellen. Nicht unterdrückt. |
| **OFFEN** | Ein `Overfull vbox`-Hinweis von 1,25362 pt am Theoriecode zum geometrischen Mittel; sechs `Underfull vbox`-Hinweise im langen Analysecode | Kleine vertikale beziehungsweise Umbruchmeldungen; in den geprüften Seiten keine Überlagerung oder abgeschnittene Zeile. Keine pauschale Unterdrückung oder globalen Leerraum-Manipulationen. |
| **OFFEN** | Vollständigkeit der formalen Abgabeteile | Titelseite enthält derzeit Titel, Autor und Datum, aber nicht alle Leitfadenangaben; Abstract, separate Abbildungs-/Tabellenverzeichnisse und unterzeichnete Eigenständigkeitserklärung fehlen. Nicht automatisch ergänzt, weil zusätzliche Angaben und Autorenentscheidungen nötig sind. |
| **OFFEN** | Manche Tabellen besitzen nur eine vorhandene Textüberschrift statt einer automatisch nummerierten Quarto-Beschriftung; die Theorieabbildung besitzt keinen nummerierten Quellen-/Caption-Block | Werte und vorhandene Hinweise bleiben erhalten. Eine definitive Liste/Beschriftung sollte der Autor bei der Abgabevorbereitung festlegen. |
| **OFFEN** | Formatabhängige Umbrüche und Bildbeschriftungsgrössen | Acht gespeicherte Bilder sind unverändert und proportional dargestellt. Bei einer späteren Druckfreigabe nochmals Achsen/Legenden in tatsächlicher Druckgrösse prüfen; keine Neuberechnung vorgenommen. |
| **NICHT GEPRÜFT** | Mobile Browseransichten, andere Word-/Office-Versionen, LibreOffice-Kompatibilität, physischer Druck | Browser-Breitenprüfung erfolgte bei 1440 px, Word-Prüfung mit der vorhandenen Windows-Installation. Keine weitergehende Kompatibilitätsbehauptung. |
| **OFFEN** | Autorenkontrolle | Technische Prüfungen sind durchgeführt; eine persönliche Prüfung oder Freigabe des Autors wird nicht behauptet. |

## Getrennte fachliche oder technische Auffälligkeiten

**OFFEN – Phase 2:** Im Theorie-Portfolio-Beispiel stehen Gewichte 0,20/0,40/0,40; die gespeicherte Ausgabe lautet weiterhin `Volatilität: 1.15%`. Es wurde weder nachgerechnet noch behauptet, dass diese Ausgabe den geänderten Gewichten entspricht. Gewichte und Ausgabe wurden vollständig bewahrt. Eine spätere gezielte Neuausführung liegt ausserhalb dieses Auftrags.

**NICHT GEPRÜFT:** Umfang und fachliche Plausibilität des gesamten Texts, Formeln, Ergebnisinterpretation, Quellenqualität und Konsistenz sämtlicher Backtests. Bestehende Hinweise aus dem vorangegangenen Umgliederungsbericht bleiben gültige Folgepunkte und wurden nicht korrigiert. Auch historische Formulierungen im KI-Nachweis wurden nicht sprachlich nachbearbeitet.

## Git-Abschluss und Übergabe

**PASS:** `git diff --check` ohne Fehler; Branch und HEAD unverändert; Git-Index identisch zur Sicherung. Vier bestehende Dateien geändert und sieben Dateien ergänzt, insgesamt elf Dateien. Davon betreffen sieben die Formatierung/Buchstruktur und vier die verlangte Dokumentation. Die neue Word-Vorlage ist binär; ihre Gestaltung ist im beigefügten Builder und den geprüften OOXML-Einstellungen nachvollziehbar. Git meldet lediglich den üblichen Hinweis auf eine spätere LF→CRLF-Normalisierung im KI-Log; ältere Log-Bytes wurden ausdrücklich bewahrt. Kein Commit, Push, Merge, Pull, Checkout, Reset, Staging oder Clean.

Die vorhandenen Notebook-, Quellen-, Studien-, Ergebnis-, Archiv-, Freeze- und Repository-Ausgabedateien bleiben unverändert. Alle Änderungen stehen zur Autorenkontrolle im Arbeitsverzeichnis. Der Auftrag endet hier ohne automatische Veröffentlichung oder weitere inhaltliche Bearbeitung.
