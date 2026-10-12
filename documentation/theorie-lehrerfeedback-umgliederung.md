# Theoriekapitel: Umgliederung nach Lehrerfeedback

Ausführung: 12. Oktober 2026 (Europe/Zurich). Autorenkontrolle ausstehend. Die Gliederung ist ein vom Autor angenommener optionaler Vorschlag des Lehrers.

## Ausgangsstand und Sicherung

- Repository: `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027`; Remote: `riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027`.
- Branch: `dev`; geprüfter Referenzcommit und tatsächlicher HEAD: `8a3f41b58ae42eb25e49e4b1cad267aba031d5a8`. Kein Pull, Checkout, Worktree-Wechsel oder Merge.
- Index ohne gestagte Änderungen. Einzige vorhandene lokale Änderung: `notebooks/Theorie.ipynb` (28 eingefügte, vier entfernte Git-Diff-Zeilen). Diese bereits eingearbeiteten Textkorrekturen sind der massgebliche Vorzustand; es wurde nicht auf den älteren Commit zurückgesetzt.
- Vorhandensein bestätigt: praktische Indexnachbildung (physisch, Sampling, Tauschverträge), ausgeschriebenes ETF, sichtbarer MDD-Zeitbereich und vollständige Sharpe-Zeichentabelle. Die Angabe zur Herkunft von ChatGPT stammt aus dem Auftrag; keine abgeschlossene Autoren-Fachprüfung bestätigt.
- Keine `AGENTS.md` im Repository oder in den geprüften übergeordneten Verzeichnissen vorhanden. Die im Auftrag genannten Projekt- und Dokumentationsdateien wurden gelesen.
- Externe Sicherung: `C:\Users\modic\AppData\Local\Temp\codex-theorie-2026-10-12_035048-_8lg73l_`. `manifest.json`, `local-diff-before.patch` und `index-diff-before.patch` halten lokale Dateien, Hashes, HEAD, Index und vorhandene Änderungen fest. Sicherung und Prüfkopie bleiben für die Nachkontrolle bestehen.
- Theorie vorher (SHA-256): `5d266387bc179830bd17ba54985ffb08b1dfcb05bdd61f00f3f4bdf124d11635`.
- Theorie nachher (SHA-256): `8dbe5ebf6430778bde6355d3d3bc1f895975f97a2c7d6ea24fd06cdcda166596`.
- Index-Snapshot (SHA-256 der Ausgabe von `git ls-files --stage`): `311ea562e8cecdbe097817bf3ebbc3d87e9776408a549609b8069c30563f292d`; nachher identisch.

Die Sicherung umfasst Theorie, alle weiteren eingebundenen Buchquellen, README, Konfiguration, Bibliografie und die vorgegebenen KI-Dokumentationsdateien. Die Einzelhashes stehen im externen Manifest.

## Vollständige Alt-neu-Zuordnung

Die Nummern sind sichtbare Quarto-Nummern. In den betroffenen Überschriften stehen jetzt native Markdown-Ebenen ohne manuell vorangestellte Nummern. `_quarto.yml`, globale Nummerierung, Inhaltsverzeichnistiefe und Formatvorlagen wurden nicht geändert.

Neu eingefügt: `3.1 Portfolio` (Ebene 2) und `3.2 Berechnungen und Daten` (Ebene 2). Die bisherige Hauptüberschrift 3.13 wird als `3.3 Methodische Grenzen` geführt. Die übrigen Untertitel behalten ihren Wortlaut.

| Bisher | Neu | Titel | Neue Ebene | Ursprüngliche Zell-ID |
|---|---|---|---|---|
| 3.1 | 3.1.1 | Grundlagen historischer Finanzdaten | 3 | `1941d2df` |
| 3.1.1 | 3.1.1.1 | Indexfonds und ETFs | 4 | `1941d2df` |
| 3.1.2 | 3.1.1.2 | Eignung für die Untersuchung | 4 | `1941d2df` |
| 3.2 | 3.2.1 | Historische Finanzdaten und Zeitreihen | 3 | `1941d2df` |
| 3.2.1 | 3.2.1.1 | Zeitreihen | 4 | `1941d2df` |
| 3.2.2 | 3.2.1.2 | Frequenzen | 4 | `1941d2df` |
| 3.2.3 | 3.2.1.3 | Resampling | 4 | `1941d2df` |
| 3.3 | 3.2.2 | Rendite | 3 | `13e3a739` |
| 3.3.1 | 3.2.2.1 | Einfache Rendite | 4 | `4670f764` |
| 3.3.2 | 3.2.2.2 | Logarithmische Rendite und kumulierte Rendite | 4 | `6a341a65` |
| 3.3.3 | 3.2.2.3 | Geometrische Rendite | 4 | `6889baa6` |
| 3.3.4 | 3.2.2.4 | Nominal und real | 4 | `621f9b9a` |
| 3.4 | 3.2.3 | Volatilität | 3 | `6214eedc` |
| 3.4.1 | 3.2.3.1 | Bedeutung der Volatilität | 4 | `6214eedc` |
| 3.4.2 | 3.2.3.2 | Berechnung der Volatilität | 4 | `0a5b52df` |
| 3.4.3 | 3.2.3.3 | Annualisierung | 4 | `8fd22c41` |
| 3.4.4 | 3.2.3.4 | Interpretation | 4 | `22fec44e` |
| 3.4.5 | 3.2.3.5 | Diversifikation | 4 | `03486f6b` |
| 3.4.6 | 3.2.3.6 | Beispiel | 4 | `ae9df1ec` |
| 3.5 | 3.2.4 | Drawdown | 3 | `f8ed3fb2` |
| 3.5.1 | 3.2.4.1 | Bedeutung des Drawdowns | 4 | `d501a001` |
| 3.5.2 | 3.2.4.2 | Berechnung | 4 | `bff7db06` |
| 3.5.3 | 3.2.4.3 | Erholungsdauer und Grenzen | 4 | `d501a004` |
| 3.6 | 3.2.5 | Sharpe Ratio | 3 | `d506a001` |
| 3.6.1 | 3.2.5.1 | Bedeutung der Sharpe Ratio | 4 | `d506a001` |
| 3.6.2 | 3.2.5.2 | Berechnung | 4 | `d506a002` |
| 3.6.3 | 3.2.5.3 | Interpretation und Grenzen | 4 | `d506a004` |
| 3.7 | 3.1.2 | Diversifikation und Korrelation | 3 | `d507a001` |
| 3.7.1 | 3.1.2.1 | Diversifikation | 4 | `d507a001` |
| 3.7.2 | 3.1.2.2 | Korrelation | 4 | `d507a002` |
| 3.7.3 | 3.1.2.3 | Veränderliche Korrelationen | 4 | `d507a004` |
| 3.8 | 3.1.3 | Asset-Allokation und Rebalancing | 3 | `d508a001` |
| 3.8.1 | 3.1.3.1 | Asset-Allokation | 4 | `d508a001` |
| 3.8.2 | 3.1.3.2 | Gewichtungsdrift und Rebalancing | 4 | `d508a002` |
| 3.9 | 3.1.4 | Marktbreites Buy-and-Hold | 3 | `d509a001` |
| 3.9.1 | 3.1.4.1 | Funktionsweise | 4 | `d509a001` |
| 3.9.2 | 3.1.4.2 | Vorteile, Risiken und Benchmark | 4 | `d509a002` |
| 3.10 | 3.1.5 | Das 60/40-Portfolio | 3 | `d510a001` |
| 3.10.1 | 3.1.5.1 | Aufbau und Ziel | 4 | `d510a001` |
| 3.10.2 | 3.1.5.2 | Diversifikation und Grenzen | 4 | `d510a002` |
| 3.11 | 3.1.6 | Marktkapitalisierungs- und BIP-Gewichtung | 3 | `d511a001` |
| 3.11.1 | 3.1.6.1 | Marktkapitalisierungsgewichtung | 4 | `d511a001` |
| 3.11.2 | 3.1.6.2 | BIP-Gewichtung | 4 | `d511a002` |
| 3.12 | 3.2.6 | Trendfolge mit gleitenden Durchschnitten | 3 | `d512a001` |
| 3.12.1 | 3.2.6.1 | Einfacher gleitender Durchschnitt | 4 | `d512a001` |
| 3.12.2 | 3.2.6.2 | Handelssignal | 4 | `d512a002` |
| 3.12.3 | 3.2.6.3 | Grenzen der Trendfolge | 4 | `d512a004` |
| 3.13 | 3.3 | Aussagegrenzen historischer Vergleiche und Backtests → Methodische Grenzen | 2 | `d513a001` |
| 3.13.1 | 3.3.1 | Historische Stichprobe und Vergleichbarkeit | 3 | `d513a001` |
| 3.13.2 | 3.3.2 | Foresight Bias | 3 | `d513a002` |
| 3.13.3 | 3.3.3 | Data Snooping und Overfitting | 3 | `d513a003` |
| 3.13.4 | 3.3.4 | Kosten, Inflation und Datenqualität | 3 | `d513a004` |

## Geteilte und verschobene Zellen

- `1941d2df` enthielt 3.1 und Teile von 3.2. Geteilt wurde ausschliesslich vor dem ursprünglichen HTML-Kopf `3.2 Historische Finanzdaten und Zeitreihen`: Quelltext-Arrayelemente 0–7 bleiben bei `1941d2df`, die Elemente ab 8 stehen in der neuen Zelle `005fce46`. Zusammengesetzt sind beide Teile exakt der alte Quelltext; kein Text, Anhang oder Output wurde verworfen.
- Neue Gruppenzellen: `2d33a821` für Portfolio und `fa0bef57` für Berechnungen und Daten. Sämtliche anderen ursprünglichen IDs blieben erhalten. 83 → 86 Zellen, davon unverändert 17 Codezellen. Die Reihenfolge innerhalb jedes alten Themenblocks blieb gleich.
- Die bestehende Raw-/YAML-Titelzelle blieb vollständig unverändert; kein doppelter Kapitelkopf. Keine globale JSON-Neuformatierung: unveränderte Zellen wurden als vorhandene JSON-Textblöcke verschoben, insbesondere sämtliche Codezellen bytegleich.

| Alter Block | Neuer Block | Zellfolge nach der notwendigen Teilung, innerhalb des Blocks unverändert |
|---|---|---|
| 3.1 | 3.1.1 | `1941d2df` |
| 3.7 | 3.1.2 | `d507a001`, `d507a002`, `cecc3300`, `b6316a3d`, `d507a003`, `5b4e89ac`, `d507a004` |
| 3.8 | 3.1.3 | `d508a001`, `c269ad7f`, `d508a002`, `bdef1563`, `d508a003`, `98df818c` |
| 3.9 | 3.1.4 | `d509a001`, `d509a002`, `8e1550f8`, `d509a003` |
| 3.10 | 3.1.5 | `d510a001`, `990d4cd6`, `d510a002` |
| 3.11 | 3.1.6 | `d511a001`, `d8350873`, `d511a002`, `035b1ffe` |
| 3.2 | 3.2.1 | `005fce46`, `86c17661`, `c8856345`, `701bf03e`, `7e670f16`, `e1888b20` |
| 3.3 | 3.2.2 | `13e3a739`, `4670f764`, `8c314bde`, `6a341a65`, `061f64f4`, `6889baa6`, `c70a36fd`, `52b6d8f5`, `cfa8c385`, `621f9b9a` |
| 3.4 | 3.2.3 | `6214eedc`, `0a5b52df`, `f2cafbc8`, `32e3c634`, `7927b0c2`, `8fd22c41`, `10386aae`, `62c541e2`, `22fec44e`, `03486f6b`, `ae9df1ec`, `c09ff8c4`, `5a028097` |
| 3.5 | 3.2.4 | `f8ed3fb2`, `d501a001`, `bff7db06`, `3a60969c`, `d501a002`, `2e6c469f`, `d501a003`, `d501a004`, `83fd3049`, `d606f0f5`, `f17d8f57` |
| 3.6 | 3.2.5 | `d506a001`, `d506a002`, `909f608f`, `52959a27`, `6e2866c3`, `d506a003`, `d506a004` |
| 3.12 | 3.2.6 | `d512a001`, `c68fa307`, `d512a002`, `0c76df80`, `2d7aee16`, `d512a003`, `d512a004` |
| 3.13 | 3.3 | `d513a001`, `d513a002`, `d513a003`, `d513a004` |

## Interne Verweise und Anker

- Geprüft wurden die tatsächlichen lokalen Vorzustände von `index.ipynb`, `Einleitung.ipynb`, `Theorie.ipynb`, `Methodik.ipynb`, `Analyse.ipynb`, `Fazit.ipynb`, README und dem bestehenden KI-Anhang. Keine eindeutigen betroffenen Abschnittsverweise, Sammelverweise oder expliziten Theorie-Ankerlinks gefunden; folglich keine Verweisersetzungen.
- Nicht ersetzt: `index.ipynb`, Zelle 6, ID `7dd61677`, und README, Zeile 19: «Python 3.11 oder neuer» ist eine Versionsangabe. `Methodik.ipynb`, Zelle 2, ID `a233bc87`: «Kapitel 3» bleibt eine gültige Referenz auf das gesamte Theoriekapitel. Zellindizes sind nullbasiert.
- Literaturangaben wie «Abschnitt 9.3» und Quellen-Seitenzahlen wurden unverändert belassen. Die ursprünglichen Theorie-Überschriften hatten keine expliziten IDs. Neu automatisch erzeugte HTML-IDs sind eindeutig; alle 1298 geprüften internen HTML-Datei-/Fragmentlinks der sieben Buchseiten sind gültig.
- Keine unklaren betroffenen Abschnittsverweise zur Autorenprüfung gefunden. Historische Prompts, Archive, Prüfberichte und Engine-Nachweise wurden nicht umnummeriert.

## Integrität und tatsächlich ausgeführte Prüfungen

| Prüfung | Ergebnis und Grenze |
|---|---|
| Korrigierter Vorzustand | PASS: die genannten Korrekturstellen waren bereits vorhanden; nur der korrigierte lokale Stand wurde als Vergleichsbasis verwendet. |
| Fachtexte, Formeln und Quellen | PASS: alle Originalzellen beziehungsweise exakt zugeordneten Teilzellen wurden gegen die Sicherung geprüft. Unterschiede beschränken sich auf neue Gruppenüberschriften und dokumentierte Überschriftenänderungen. Keine internen Verweisänderungen nötig. |
| Zitationen | PASS: 101 Vorkommen von 11 Keys unverändert; Bibliografie bytegleich. |
| Code, Outputs, Anhänge | PASS: 17 vollständige Codezellen inklusive Quelltext, Metadaten, gespeicherten Ausgaben und execution_count identisch; ursprüngliche JSON-Zellblöcke bytegleich. Sämtliche vorhandenen Attachments unverändert. |
| Gespeicherte Bilder | PASS: 1 PNG-Output erhalten; decodierter PNG-Hash in den temporär gerenderten Abbildungsdateien nachgewiesen. |
| Titel und Notebook-Metadaten | PASS: bestehende Titelzelle und alle Metadaten ausserhalb des Zellarrays unverändert. 86 eindeutige Zell-IDs. |
| Notebook-Format | PASS: `nbformat.validate` mit bereits vorhandener lokaler venv-Bibliothek; keine Installation oder Upgrades. |
| Definitionen und Reihenfolge | PASS für die ausgeführte statische AST-Prüfung: alle 20 geprüften eigenen Funktionsaufrufe samt transitiv benötigten eigenen Funktionen erfolgen nach deren Definition. Keine Codekorrektur. Dies ist kein neuer Laufzeitnachweis. |
| HTML | PASS: 54 sichtbare Abschnittsüberschriften jeweils genau einmal, richtige h2/h3/h4-Hierarchie und Nummerierung; Sharpe-Tabelle mit acht Einträgen; Fragment- und Dateilinks geprüft. |
| PDF | PASS: 88 Seiten, LuaLaTeX erfolgreich. Sichtprüfung der Seiten 11, 20, 30, 32, 33 und 36: vierte Nummerierungsebene sichtbar, Zeitbereich unter dem MDD-Minimum, vollständige Sharpe-Tabelle (Fortsetzung auf Seite 33) und methodische Grenzen. Inhaltsverzeichnistiefe unverändert. |
| Arbeitsrepository | PASS: Konfiguration, übrige Buchquellen und geschützte Bibliografie unverändert; Hashvergleich aller 67 ursprünglichen Dateien unter _book, _freeze und .quarto identisch. Index-Snapshot unverändert. |
| Neue Ausführung der Theorie-Beispiele | NICHT GEPRÜFT / absichtlich nicht ausgeführt. Gespeicherte Outputs belegen ausschliesslich den vorherigen Ausführungsstand. |
| Fünf Echtdaten-Backtests, Engine, Downloads, Optimierung | NICHT GEPRÜFT / absichtlich nicht ausgeführt und nicht verändert. |
| Fachliche Gesamtvalidierung und manuelle Autorenprüfung | NICHT GEPRÜFT; Autorenkontrolle ausstehend. |

Die Renderläufe fanden ausschliesslich in der externen Kopie `render-project` statt. Ausgeführt wurden:

```powershell
quarto render --to html --no-execute --no-cache
quarto render --to pdf --no-clean --no-execute --no-cache -M latex-auto-install:false -M latex-clean:false -M keep-tex:true
```

Beide beendeten sich mit Exit-Code 0. Die unveränderte Projektkonfiguration wurde verwendet; die PDF-Optionen galten nur für den Prüfaufruf. Ein anfänglicher kombinierter Aufruf `--to html,pdf` wurde von Quarto 1.9.37 als unbekanntes Format abgewiesen; er erzeugte keinen Darstellungsnachweis. Die Formate wurden daraufhin separat erfolgreich geprüft. Protokolle: `render-html-log.txt`, `render-pdf-log.txt`, `render-project/index.log` in der externen Sicherung.

Das abschliessende LaTeX-Protokoll enthält keine Fehler oder fehlenden Zeichen. Verblieben sind sechs Underfull- und 15 Overfull-Layout-Hinweise. Keine globalen Formatänderungen zur Unterdrückung dieser Hinweise.

## Ergänzte KI-Nachweise

- [Ausgeführter Originalauftrag](ai-usage/prompts/2026-10-12-theorie-lehrerfeedback-umgliederung.txt): unveränderte Kopie der eingefügten Anweisung; keine frühere Promptdatei überschrieben.
- [KI-Nutzungslog](ai-usage/ai-usage-log.md): zwei neue, ausschliesslich angehängte Zeilen. Der vorangegangene ChatGPT-Beitrag und der Codex-Strukturauftrag werden getrennt dokumentiert; frühere Einträge blieben bytegleich erhalten.
- `ki-nutzung.qmd`: ein neuer Abschnitt «Umgliederung des Theoriekapitels nach Lehrerfeedback»; alle übrigen Anhangsinhalte unverändert. Lehrer-Rückmeldung, Autorenentscheidung, ChatGPT-Erklärungsarbeit und Codex-Strukturarbeit sind getrennt benannt. Der Anhang ist in den temporären Ausgaben enthalten.

## Separat beobachtete, nicht korrigierte Punkte

- Zelle `d501a003`: die vorhandene Drawdown-Funktion erzeugt die Vermögensreihe ausschliesslich mit `cumprod()` der periodischen Renditen; ein expliziter Anfangswert V0 wird nicht vorangestellt. Die vorhandene Formel nennt V0 im Maximum. Dieser Unterschied wurde beim Lesen gesehen, aber nicht fachlich weiter geprüft oder korrigiert.
- Zelle `5b4e89ac`: die Beispielgewichte für `portfolio_risiko()` sind 0,20 / 0,40 / 0,20 und summieren sich zu 0,80. Dies wurde nicht geändert; die beabsichtigte Beispielannahme ist vom Autor zu prüfen.
- Diese Hinweise sind keine Ergebnisse neuer Beispielrechnungen. Keine zusätzliche fachliche Überarbeitung beauftragt oder ausgeführt.

## Git-Abschlusskontrolle

`git diff --check`: PASS (Exit-Code 0).

`git status --short`:

```text
 M documentation/ai-usage/ai-usage-log.md
 M ki-nutzung.qmd
 M notebooks/Theorie.ipynb
?? documentation/ai-usage/prompts/
?? documentation/theorie-lehrerfeedback-umgliederung.md
```

Kein `git add`, Commit, Push, Merge, Reset oder Clean. Nach diesem Bericht endet der Auftrag; der Autor kontrolliert und übernimmt den Diff selbst.
