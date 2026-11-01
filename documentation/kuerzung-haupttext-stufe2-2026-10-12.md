# Abschliessende wissenschaftlich kontrollierte Kürzung – Stufe 2

Datum: 12. Oktober 2026. Verfasser: Codex. **Ergebnis: 7’849 Wort-/Zahlentoken einschliesslich Überblick, 151 unter 8’000. Zielspanne 7’700–7’850 erreicht. STOPP zur Autorenkontrolle.**

Der Haupttext wurde ausgehend von 8’948 um **1’099** gekürzt. Ohne Überblick umfasst er neu **7’724** statt 8’823. Es wurden ausschliesslich begründete Wiederholungen und ausführliche Formulierungen in **55 bestehenden Markdown-Zellen** verdichtet. Keine neuen Auslagerungen, Kapitelzusammenführungen, Fachkorrekturen, Codeausführungen oder wissenschaftlichen Neuberechnungen. T01, F02 und F04 bleiben vollständig unverändert.

## 1. Ausgangsstand und Sicherung

Tatsächlicher Ausgangs- und End-HEAD: `ab9ac731284f8217ae367996b3276c0aa2231d51`, Branch `dev`, zu Beginn sauberer Arbeitsbaum. Keine anwendbare `AGENTS.md` im Repository oder in seinen übergeordneten Verzeichnissen gefunden. Die Quellen entsprechen nach vollständigem JSON-Abgleich der geprüften Stufe-1-Fassung. Berücksichtigt wurden alle sechs Hauptkapitel, bestehende Anhänge, [Stufe-1-Bericht](kuerzung-haupttext-stufe1-2026-10-12.md), [Kürzungsplan](kuerzungsplan-haupttext-2026-10-12.md), [Phase-2-Gegenlesebericht](gesamtgegenlesen-phase2-2026-10-12.md) und die vorhandenen KI-Dokumentationsregeln.

Vor jeder Änderung wurde der gesamte Arbeitsstand ausser `.git`, `.venv` und `__pycache__` extern bytegetreu gesichert: `C:\Users\modic\AppData\Local\Temp\codex-kuerzung-stufe2-2026-10-12-skmeyl57\original`. Die Sicherung umfasst **156 Dateien**, darunter **85 versionierte Ausgangsdateien** und sämtliche **70** vorhandenen `_book`-/`_freeze`-/`.quarto`-Dateien. Alle Sicherungskopien wurden per SHA-256 gegen den Ausgangsstand geprüft und sind am Ende weiterhin identisch.

Der vollständig ausgeführte Auftrag ist byteidentisch unter [Promptkopie](ai-usage/prompts/2026-10-12-kuerzung-haupttext-stufe2.txt) gespeichert; SHA-256 `d2fc113b8eb980b436e7cd978447db7c4c4af3e820c8c95f51f61612ae7491dc`.

Intern wurden Originaltext, vorgeschlagene Verdichtung, Redundanzgrund, verbleibender Aussageort und Tokenzahlen vor der Übernahme gegenübergestellt. Vorschläge ohne Ersparnis beziehungsweise mit bloss drei Token Ersparnis und unnötiger neuer Kurzschreibweise wurden nicht übernommen. Eine letzte Lesbarkeitskorrektur stellte die natürliche Formulierung der Anhangszuordnung wieder her; die endgültige Fassung hat deshalb zwei Token mehr als die vorherige 7’847-Fassung. Danach wurden alle drei Formate vollständig neu gerendert. Keine weitere Kürzung erfolgte nach Erreichen der Zielspanne.

## 2. Vergleich mit unveränderter Zählmethode

Gezählt wird Markdown-Prosa der sechs Hauptnotebooks mit derselben Filterfolge wie im Plan/Stufe 1. Raw-/YAML-Zellen, ausführbare Codezellen und deren Outputs, Bilder, Codefences/HTML-`pre`, Überschriften, Markdown-Tabellenzeilen, Display-/Inline-Mathematik und Zitationsklammern werden ausgeschlossen. HTML-Tags, Linkziele und `@sec-…` werden entfernt, sichtbare Linkbeschriftungen bleiben; HTML-Entities werden entschlüsselt. Wort-/Zahlentoken folgen `\b\w+(?:[’'-]\w+)*\b`. Diese Methode reproduziert 8’948/8’823 am Ausgangsstand und ermöglicht den direkten Vergleich. Der Bericht selbst, KI-Anhang, Literatur und technische Anhänge zählen nicht zum Haupttext.

| Kapitel | Ausgang | Ende | Nettoersparnis | Geänderte Zellen |
|:---|---:|---:|---:|---:|
| 1 Überblick | 125 | 125 | 0 | 0 |
| 2 Einleitung | 629 | 430 | 199 | 8 |
| 3 Theorie | 2’985 | 2’659 | 326 | 14 |
| 4 Methodik | 905 | 855 | 50 | 4 |
| 5 Analyse | 3’448 | 2’949 | 499 | 28 |
| 6 Fazit | 856 | 831 | 25 | 1 |
| **Mit Überblick** | **8’948** | **7’849** | **1’099** | **55** |
| **Ohne Überblick** | **8’823** | **7’724** | **1’099** | **55** |
 
**Summenprüfung:** 0+199+326+50+499+25 = 1’099. Jeder Zellblock wird genau einmal berücksichtigt, auch wenn er intern mehrfach nachgeschärft wurde. Vorher-/Nachherzahlen wurden erneut direkt an den aktuellen Notebook-Quellen geprüft. Keine Code-/Formel-/Tabellenkürzung ist als Prosaersparnis angerechnet.

| Grenze | Ergebnis |
|:---|---:|
| Obergrenze 8’000, mit Überblick | **151 Token Reserve**, keine verbleibende Überschreitung |
| Obergrenze 8’000, ohne Überblick | **276 Token Reserve** |
| Gewünschte Spanne 7’700–7’850 | **Erfüllt: 7’849** |

Die Reserve bezieht sich auf die ausdrücklich verlangte bisherige Zählmethode. Die ergänzenden Abgabeteile aus R-016 wurden nicht erstellt; dieser Stand ist noch keine vollständige formale Abgabefassung.

## 3. Inhaltliche Eingriffsgrenzen und Vergleichsprüfung

**Theorie:** Wiederholte Wirkungs-/Interpretationsabsätze zu Diversifikation, Volatilität, Drawdown, Sharpe und Trend wurden zusammengeführt. Die zentrale Korrelationsdefinition mit −1/+1/0 und linearem Zusammenhang bleibt wörtlich; die Diversifikationsbedingung in 03486f6b bleibt ebenfalls wörtlich. Finanzdefinitionen, Stichprobenformel, Annualisierungsvoraussetzungen, Drawdown- und Sharpe-Variablen sowie vollständige Signalformeln bleiben erhalten. Bei 035b1ffe ändern sich nur die beiden nachfolgenden historischen Interpretationsabsätze; Formel, Variablenerklärung und Formelherkunft davor sind zeichengetreu erhalten. Keine historische Aussage über Länder-/Teilperiodenabhängigkeit, Kosten oder künftige Verlustgrenzen wurde absoluter formuliert.

**Analyse:** Verdichtet wurden wiederholte Einleitungen, ETF-Begründungen, doppelte K1-/Z1-Abgrenzungen und Ausführungs-/Interpretationsprosa. Ergebniswerte bleiben in denselben unveränderten Tabellen und Grafiken. Vorabfestlegung, H1/K1/Z1/S1/S2, Anlageuniversen, Perioden, Haupt-/Sensitivitätsparameter und Kontrollunterschiede sind erhalten. Trend- und Rebalancingmechanismen werden weiterhin mit denselben Beispielen erläutert. Der US-Anteil bleibt ein vorsichtiger Erklärungsansatz statt einer nachgewiesenen alleinigen Ursache. Tests bestätigen innerhalb ihres Umfangs die Berechnung gemäss Eingaben, nicht die gesamte unabhängige historische Datenherkunft.

**Einleitung/Methodik/Fazit:** Die Einleitung wiederholte detaillierte Strategieregeln und den Kapitelaufbau, die bereits vollständig im Hauptbuch stehen. Motivation, persönliches Interesse und Forschungsfrage blieben unberührt. Die Methodik spart nur 50 Token und behält sämtliche konkret festgelegten Strategie-, BIP-, Signal- und Vergleichsregeln; sie benötigt keine technischen Anhänge zum Verständnis. Im Fazit wurde nur der wiederholte Prüf-/Gültigkeitsabsatz 53c9f636 verdichtet. F02/F04 einschliesslich ihrer Formulierungen bleiben vollständig identisch. Forschungsantwort, eigene Schlussfolgerungen und Rückblick wurden nicht neu gefasst.

Die Gegenüberstellung je Zelle in Abschnitt 7 nennt den Redundanzgrund und die erhaltenen eigenständigen Aussagen. Es wurden keine neuen Finanzbehauptungen, Finanzzahlen oder kausalen Schlussfolgerungen ergänzt. Kodierte Regeln und eingefrorene Ergebnisse wurden nicht optimiert. Alle verbleibenden Quellenbelege bleiben wörtlich erhalten; Quellen wurden in diesem Kürzungsauftrag nicht erneut recherchiert oder fachlich berichtigt.

## 4. Integrität und Verweise

| Gegenstand | Tatsächlicher Nachweis |
|:---|:---|
| Code | Alle **28** Codezellobjekte im selben Notebook/in derselben Reihenfolge vollständig identisch: Quelle, ID, Metadaten, Execution Count und Outputs; auch nach den externen Renderläufen |
| Ausgaben | Alle **28** Outputobjekte und **acht PNGs** erhalten; keine erneute Notebook-/Backtest-/Engine-Testausführung |
| Mathematik/Variablen | Multimenge aller **95** mathematischen Ausdrücke identisch; **47** Formel-/Variablenzellen geprüft. Bei 46 Zellen vollständiges Objekt identisch, bei 035b1ffe unveränderter Formel-/Variablen-/Herkunftsvorspann und ausschliesslich verdichtete anschliessende Interpretation |
| Tabellen/Bilder im Word-Export | Dieselben **95** OMML-Formelobjekte, **23** Tabellen mit identischen Zeilendaten und **acht** Bilddateien mit identischen SHA-256 wie am Ausgangsstand |
| Markdown-Tabellen | Alle **14** Tabellenblöcke exakt identisch; sämtliche Ergebnis-/Parameterwerte erhalten |
| Quellen | Alle vollständigen aktiven Zitationsklammern als Multimenge identisch; **29** Citation Keys und **157** Vorkommen erhalten; Bibliographie/CSL byteidentisch |
| Notebooks | Neun Notebooks schemakonform, **495** Zellen; keine Zelle hinzugefügt/gelöscht/verschoben, alle IDs/reihenfolge-/zellübergreifenden Metadaten identisch. Nur `source` von 55 Markdown-Zellen geändert |
| Sperrstellen | Alle Originalzellen der Planblöcke **T01/F02/F04 vollständig identisch**; Forschungsfragen in Überblick/Einleitung/Fazit und die besonderen Raw-Titelzellen im Überblick identisch |
| Studienregeln | Unter anderem 38cbd5f3, 563f04bb, 8433fb9b, 18279f6c, 2565f88a, 4e93dcd6, e2aa1e8c, 89a22011, fee3f6b2 und dad07e04 vollständig identisch; zentrale Strategie-/Signal-/BIP-/RF-Regeln bewahrt |
| Bekannte Problemstellen | T01, 621f9b9a, 5a028097, 83fd3049, 990d4cd6, c269ad7f und alle betreffenden Code-/Outputzellen erhalten; kein R-Befund durch ersatzloses Entfernen verdeckt |
| Anhänge | A–C vollständig byteidentisch, kein neuer Anhang/Unterabschnitt/Transfer. Nur autorisierter neuer KI-Nachtrag **D.8**, bisherige D-Inhalte als unverändertes Bytepräfix erhalten |
| Engine/Resultate | Alle **30** versionierten Resultatdateien sowie Engine-Referenzen und Studienkonfigurationen SHA-256-identisch; keine neuen wissenschaftlichen Ergebnisse |

Hauptkapitel 1–6, Analyse 5.1–5.5 und Anhänge A–D behalten ihre Nummern. Alte aktive Verweise wurden nicht neu umnummeriert. Neue kurze Rückverweise auf 1.2, 3.2.6.3, 4.2.2 und 5.2.4/5.2.6/5.2.7 wurden gegen tatsächlich gerenderte Überschriften geprüft. 3.2.6.3 bezeichnet unverändert «Grenzen der Trendfolge». Die Original-Plotcodeeinbindung `{{< embed Analyse.ipynb#99cad7ec echo=true >}}` bleibt unverändert, ebenso alle sieben Plotaufrufe und gespeicherten Ergebnisgrafiken.

## 5. Renderprüfung und Sichtkontrolle

Sämtliche Renderbefehle liefen ausschliesslich in der vollständig externen Kopie `C:\Users\modic\AppData\Local\Temp\codex-kuerzung-stufe2-2026-10-12-skmeyl57\render-project`. Vor jedem Start wurden tatsächliches Arbeitsverzeichnis und `_book`-Ausgabeziel überprüft. Nur in dieser Kopie wurden `execute.enabled: false` und `freeze: false` gesetzt. `--no-execute --no-cache` deaktiviert Ausführung/Cache-Nutzung; der PDF-Lauf untersagt automatische Paketinstallation. Die ursprüngliche `_quarto.yml` bleibt byteidentisch.

```text
quarto render --to html --no-execute --no-cache
quarto render --to pdf --no-execute --no-cache --no-clean -M latex-auto-install:false -M latex-clean:false -M keep-tex:true
quarto render --to docx --no-execute --no-cache --no-clean
```

| Prüfung | Ergebnis |
|:---|:---|
| Vollständiges HTML-Buch | Exit **0**, elf Buchdateien; **1’765** lokale `href`-/`src`-/Ankerziele geprüft, **0** ungültige Ziele, **0** doppelte IDs; D.8 im KI-Anhang und Inhaltsverzeichnis vorhanden |
| Vollständiges LuaLaTeX-PDF | Exit **0**, **107** Dateiseiten; keine LaTeX-Fehler, fehlenden Zeichen oder undefinierten Verweise/Zitationen |
| Vollständiger Quarto-DOCX-Export | Exit **0**, projektübliche DOCX-Nachbearbeitung erfolgreich, keine Formelkonvertierungswarnungen; 95 Formeln/23 Tabellen/8 Bilder identisch |
| Zusätzlicher paketierter DOCX-Prüfrenderer | **Fehlgeschlagen**, Exit **1**: `FileNotFoundError: LibreOffice soffice.exe was not found on PATH`. Keine Installation; nicht als bestandene Prüfung dargestellt |
| Microsoft-Word-Ersatzprüfung | Installiertes Word in eigener unsichtbarer Instanz; DOCX schreibgeschützt geöffnet, Felder/Inhaltsverzeichnis nur im Speicher aktualisiert, neu paginiert und in ein Prüf-PDF mit **91** Dateiseiten exportiert. Ohne Speichern geschlossen |

Nach der letzten Lesbarkeitskorrektur wurden HTML/PDF/DOCX vollständig erneut erzeugt. Sämtliche Seiten beider endgültigen PDF-Darstellungen wurden mit Poppler als PNG gerastert und sämtliche Seitenübersichten angesehen. Detailansichten umfassen besonders die Modellbrücke, Methodikregeln, Volatilitätsformel/Variablen, Ergebnisse und neuen KI-Nachtrag. Übersichtskontrolle umfasst alle Formeln/Tabellen/Grafiken, Seitenumbrüche, Titel/Inhaltsverzeichnis, Literatur und A–D. Keine abgeschnittenen Tabellen, fehlenden Formeln/Bilder oder Überlagerungen gefunden. Die Sichtprüfung ist eine vollständige Seitenübersicht mit gezielten Detailansichten, keine behauptete Kontrolle jedes Zeichens bei 100 % Zoom.

Literaturverzeichnis: PDF-Dateiseiten **62–64**, Word-Dateiseiten **55–56**, jeweils vor Anhang A. Geschützte Fazitpassagen sind vollständig enthalten. Die Word-Lauftabellen dürfen über Seiten umbrechen; ihre Zeilen-/Wertdaten sind vollständig und unverändert. Globale Styles, Filter, Seitenlayout und Word-Referenzvorlage wurden nicht angepasst.

Es verbleiben **19** LaTeX-Layoutmeldungen: zwölf `Overfull hbox` mit jeweils **0,11806 pt** Überbreite und sieben `Underfull`-Hinweise. Diese sind keine Kompilationsfehler; die betroffenen Darstellungen sind vorhanden und lesbar. Vollständiger Nachweis:

```text
Overfull \hbox (0.11806pt too wide) in alignment at lines 2607--2625
Overfull \hbox (0.11806pt too wide) in alignment at lines 2625--2627
Overfull \hbox (0.11806pt too wide) in alignment at lines 2627--2636
Overfull \hbox (0.11806pt too wide) in alignment at lines 2721--2739
Overfull \hbox (0.11806pt too wide) in alignment at lines 2739--2741
Overfull \hbox (0.11806pt too wide) in alignment at lines 2741--2746
Overfull \hbox (0.11806pt too wide) in alignment at lines 2794--2812
Overfull \hbox (0.11806pt too wide) in alignment at lines 2812--2814
Overfull \hbox (0.11806pt too wide) in alignment at lines 2814--2821
Overfull \hbox (0.11806pt too wide) in alignment at lines 2889--2907
Overfull \hbox (0.11806pt too wide) in alignment at lines 2907--2909
Overfull \hbox (0.11806pt too wide) in alignment at lines 2909--2916
Underfull \hbox (badness 4713) in paragraph at lines 3279--3285
Underfull \vbox (badness 10000) detected at line 4283
Underfull \vbox (badness 10000) detected at line 4283
Underfull \vbox (badness 10000) detected at line 4283
Underfull \vbox (badness 10000) detected at line 4283
Underfull \vbox (badness 10000) detected at line 4283
Underfull \vbox (badness 10000) detected at line 4283
```

Die HTML-Zielprüfung prüft lokale Verweise; externe URLs wurden nicht neu im Netz aufgerufen. Der Word-Ersatzexport ersetzt den hier nicht verfügbaren LibreOffice-Nachweis ausdrücklich und hängt von der vorhandenen Word-Version ab. Kein Paketdownload, keine neue Datenbeschaffung und keine fachliche Gesamtfreigabe.

## 6. Offene Fachbefunde und Endkontrolle

Die vorhandenen Phase-2-Befunde bleiben getrennt von dieser sprachlichen Kürzung:

- **R-001:** unpassende gespeicherte Portfolio-Beispielvolatilität unverändert.
- **R-002:** Haupttext liegt nach derselben bisherigen Methode nun unter 8’000; 151 Token Reserve einschliesslich Überblick. Keine zusätzlichen Abgabeteile hier ergänzt.
- **R-003/R-007:** falsche Kommer-Werk-/Seitenbezüge und S&P-Auswahlbeschreibung bleiben im gesperrten T01 erhalten.
- **R-004:** ursprüngliche 60/40-Anfangsgewichtsformel/-erklärung unverändert, Präzisierung offen.
- **R-005:** lokale Drawdown-Referenzfunktion unter `src` unverändert, Korrektur/Abgrenzung offen.
- **R-006:** QuantStats-Zeitdeutung, Originalcode und Output unverändert, vollständige Erholungsdauer weiterhin getrennt zu berichtigen.
- **R-008/R-012:** neue KI-Nutzung und ausstehende Autorenkontrolle korrekt dokumentiert; historische Loglücken/Kontrollnachweise nicht erfunden oder rückwirkend überschrieben.
- **R-009/R-011:** ursprünglicher `to_datetime`-Locator und historische pandas-Aliase in B.3.3 unverändert; spätere Quellen-/Versionskorrektur offen.
- **R-010/R-015:** «gleiche Rendite»-Beispiel und historische Inflationsmittel-Schwelle unverändert; fachliche Präzisierungen offen.
- **R-013:** beide Gegenrechnungsabsätze in C.3 unverändert, keine unautorisierte Bereinigung.
- **R-014:** historisch eingeordnete Projektangaben aus Stufe 1 in A.7 unverändert, keine README-Überarbeitung.
- **R-016:** vollständige Titelseite, Abstract/Verzeichnisse und unterschriebene Erklärung weiterhin ausstehend.
- **R-017:** Originaleingangs-/Sharpe-Nachweisgrenze bleibt; keine vollständige unabhängige Eingangsprüfung oder Datenverlustbehauptung, kein neuer Download/Backtest.

Am Ende unterscheiden sich genau **sieben** vorhandene Dateien: fünf Hauptnotebooks und die beiden angehängten KI-Nachweise. **78 von 85** versionierten Ausgangsdateien und **149 von 156** gesicherten Arbeitsdateien sind byteidentisch. Neu sind ausschliesslich dieser Bericht und die Promptkopie. Alle **70** bestehenden Ausgabe-/Freeze-/Cachedateien und deren Inventar bleiben identisch; keine neue Ausgabe im Schreibrepository. Überblick, Anhänge A–C, README/Synchronisationsregeln, alte Berichte/Prompts, `_quarto.yml`, Bibliographie/CSL, Styles/Filter, Engine und Ergebnisse unverändert. Bisherige KI-Buch-/Logbytes sind vollständig erhalten.

HEAD, Branch und Git-Index identisch zum Ausgangsstand; nichts gestaged. Kein Commit, Push, Merge, Reset oder Clean. Neues Log und D.8 wurden nach `KI-DOKUMENTATION-BUCH-SYNC` abgeglichen. KI-gestützte sprachliche Verdichtung ist als solche deklariert; keine neue wissenschaftliche Ergebnisarbeit oder persönliche Autorenfreigabe behauptet.

Originalsicherung, interne Gegenüberstellung, Hash-/Integritätsmanifeste, Renderlogs und Seitenbilder liegen ausschliesslich im externen Prüfverzeichnis `C:\Users\modic\AppData\Local\Temp\codex-kuerzung-stufe2-2026-10-12-skmeyl57`. Die wesentlichen Nachweise und sämtliche Textvergleiche stehen in diesem Bericht selbst.

## 7. Vollständige Gegenüberstellung aller geänderten Passagen

Die folgenden Blöcke zeigen die tatsächlichen ursprünglichen und endgültigen Markdown-Quellen einschliesslich ihrer Quellenbelege. Formeln/Überschriften innerhalb einer geänderten Zelle sind nur zur nachvollziehbaren Lokalisierung wiedergegeben, nicht gekürzt. Die Ersparnis wird für jede Zell-ID genau einmal gezählt.

| Notebook | Zell-ID | Vorher | Nachher | Ersparnis |
|:---|:---|---:|---:|---:|
| Einleitung | `a9f0792b` | 65 | 35 | 30 |
| Einleitung | `35ed2729` | 44 | 22 | 22 |
| Einleitung | `4d7593b1` | 63 | 34 | 29 |
| Einleitung | `e94c7abf` | 83 | 42 | 41 |
| Einleitung | `a7ae04cd` | 56 | 39 | 17 |
| Einleitung | `3223aafd` | 48 | 23 | 25 |
| Einleitung | `4a72f361` | 38 | 22 | 16 |
| Einleitung | `5f03e85d` | 59 | 40 | 19 |
| Theorie | `d507a002` | 92 | 75 | 17 |
| Theorie | `d508a002` | 24 | 20 | 4 |
| Theorie | `d509a002` | 29 | 21 | 8 |
| Theorie | `d510a002` | 69 | 54 | 15 |
| Theorie | `035b1ffe` | 80 | 72 | 8 |
| Theorie | `005fce46` | 101 | 62 | 39 |
| Theorie | `0a5b52df` | 44 | 11 | 33 |
| Theorie | `03486f6b` | 86 | 45 | 41 |
| Theorie | `f17d8f57` | 67 | 31 | 36 |
| Theorie | `d506a001` | 68 | 56 | 12 |
| Theorie | `d506a004` | 49 | 34 | 15 |
| Theorie | `d512a004` | 107 | 61 | 46 |
| Theorie | `d513a001` | 92 | 56 | 36 |
| Theorie | `d513a003` | 74 | 58 | 16 |
| Methodik | `35c815dc` | 42 | 30 | 12 |
| Methodik | `09fe7307` | 18 | 13 | 5 |
| Methodik | `60c85505` | 65 | 43 | 22 |
| Methodik | `0af0c786` | 43 | 32 | 11 |
| Analyse | `c50744c1` | 146 | 120 | 26 |
| Analyse | `762a3ac1` | 81 | 54 | 27 |
| Analyse | `c24d259b` | 46 | 23 | 23 |
| Analyse | `e433fc51` | 37 | 24 | 13 |
| Analyse | `3873238c` | 33 | 23 | 10 |
| Analyse | `406de6ae` | 45 | 25 | 20 |
| Analyse | `c72a0269` | 44 | 36 | 8 |
| Analyse | `8c5b7b44` | 76 | 45 | 31 |
| Analyse | `a0dcceaa` | 42 | 20 | 22 |
| Analyse | `31fc788f` | 53 | 32 | 21 |
| Analyse | `d4298767` | 22 | 13 | 9 |
| Analyse | `6f8b54af` | 54 | 29 | 25 |
| Analyse | `2d5c11d2` | 58 | 42 | 16 |
| Analyse | `b0ea1a50` | 48 | 39 | 9 |
| Analyse | `6402a9d2` | 20 | 15 | 5 |
| Analyse | `6999a6d3` | 49 | 35 | 14 |
| Analyse | `2b837f9a` | 30 | 18 | 12 |
| Analyse | `c48ec4c3` | 41 | 24 | 17 |
| Analyse | `4b05781f` | 36 | 27 | 9 |
| Analyse | `3425064c` | 36 | 18 | 18 |
| Analyse | `3df49dc6` | 81 | 42 | 39 |
| Analyse | `ab95d9b8` | 15 | 6 | 9 |
| Analyse | `53354686` | 65 | 39 | 26 |
| Analyse | `bc770851` | 53 | 31 | 22 |
| Analyse | `dfc835b7` | 36 | 23 | 13 |
| Analyse | `7012cb90` | 51 | 27 | 24 |
| Analyse | `f4051b34` | 60 | 40 | 20 |
| Analyse | `a3e4beef` | 37 | 26 | 11 |
| Fazit | `53c9f636` | 57 | 32 | 25 |

### 1. Einleitung – Zelle `a9f0792b`

Datei: `notebooks/Einleitung.ipynb`. **65→35; Ersparnis 30.**

Begründung: Endwertargument wiederholt Motivation und Kennzahlenabsatz; Modell-/Vergleichsziel verbunden.

Erhalt/Abgleich: Beide Ziele, nicht nur Endwert, Investitionszeiten, Portfoliozusammensetzung; Forschungsfrage und Kennzahlendefinitionen unverändert.

**Vorher:**

````markdown
<p>Die Arbeit verfolgt damit zwei zusammenhängende Ziele. Einerseits soll ein Python-Modell entstehen, das historische Daten verarbeitet und festgelegte Anlageregeln darauf anwendet. Andererseits soll dieses Modell einen Vergleich ermöglichen, bei dem neben der Rendite auch Schwankungen und zwischenzeitliche Verluste sichtbar werden. Ein einzelner Endwert genügt dafür nicht. Ich möchte auch nachvollziehen können, wann eine Strategie investiert war und wie sich die Zusammensetzung eines Portfolios verändert hat.</p>
````

**Nachher:**

````markdown
<p>Die Arbeit verbindet zwei Ziele: ein Python-Modell zur Verarbeitung historischer Daten und Anwendung festgelegter Regeln sowie einen Vergleich von Rendite, Schwankungen und zwischenzeitlichen Verlusten. Neben dem Endwert möchte ich Investitionszeitpunkte und Veränderungen der Portfoliozusammensetzung nachvollziehen.</p>
````


### 2. Einleitung – Zelle `35ed2729`

Datei: `notebooks/Einleitung.ipynb`. **44→22; Ersparnis 22.**

Begründung: Mehrere Sätze zur Wiederverwendbarkeit bündeln denselben Trennungsgrund.

Erhalt/Abgleich: Geeignete andere Daten/Einstellungen versus festgelegte eigentliche Untersuchung.

**Vorher:**

````markdown
<p>Das Modell soll nicht nur für einen einzigen Datensatz funktionieren. Datenaufbereitung, Berechnung und Darstellung werden deshalb getrennt aufgebaut. So sollen später auch andere geeignete Daten und Einstellungen verwendet werden können. Für die eigentliche Untersuchung werden dagegen feste Bedingungen gewählt, damit die Vergleiche nachvollziehbar bleiben.</p>
````

**Nachher:**

````markdown
<p>Getrennte Datenaufbereitung, Berechnung und Darstellung sollen andere geeignete Daten und Einstellungen ermöglichen. In der Untersuchung gelten dagegen feste Bedingungen für nachvollziehbare Vergleiche.</p>
````


### 3. Einleitung – Zelle `4d7593b1`

Datei: `notebooks/Einleitung.ipynb`. **63→34; Ersparnis 29.**

Begründung: Einführende Strategieübersicht wiederholt ausführliche Regeln 4.2; Grundidee statt erneuter Regelerklärung.

Erhalt/Abgleich: Vier Konzepte, Staatsanleihen, jährliche Verteilung, vergangene Durchschnittsbeobachtungen, Aktien/Cash und BIP-Wirtschaftsleistung; genaue Regeln in 4.2 unverändert.

**Vorher:**

````markdown
<p>Im Mittelpunkt stehen vier Anlagekonzepte. Bei Buy-and-Hold bleibt die gewählte Aktienanlage über den Untersuchungszeitraum bestehen. Das 60/40-Portfolio kombiniert Aktien und Staatsanleihen und stellt ihre vorgesehene Verteilung jährlich wieder her. Die Trendfolge verwendet gleitende Durchschnitte, also Durchschnittswerte über zurückliegende Beobachtungen, um zwischen einer Aktienanlage und Cash zu wechseln. Bei der BIP-Gewichtung richtet sich die Verteilung auf ausgewählte Länder nach deren Wirtschaftsleistung, dem Bruttoinlandsprodukt.</p>
````

**Nachher:**

````markdown
<p>Ich vergleiche vier Konzepte: Buy-and-Hold hält die Aktienanlage; 60/40 kombiniert Aktien und Staatsanleihen mit jährlicher Anpassung. Trendfolge nutzt Durchschnitte zurückliegender Beobachtungen zum Aktien-/Cash-Wechsel. BIP-Gewichtung richtet ausgewählte Länderanteile nach ihrer Wirtschaftsleistung, dem Bruttoinlandsprodukt.</p>
````


### 4. Einleitung – Zelle `e94c7abf`

Datei: `notebooks/Einleitung.ipynb`. **83→42; Ersparnis 41.**

Begründung: Rahmenübersicht wiederholt ETF-Begriff und Laufdefinitionen 4.3/5.2.3; Begründung des Kontrollvergleichs bleibt.

Erhalt/Abgleich: ETF-Proxy, Welt/US und alle Jahre, monatliche Bewertung, sieben Länder, gleiche Fonds und isolierterer Gewichtungsvergleich, Sensitivität.

**Vorher:**

````markdown
<p>Als Datengrundlage dienen historische ETF-Reihen. Diese börsengehandelten Fonds vertreten in der Untersuchung bestimmte Aktienmärkte oder den Staatsanleihenanteil. Der Hauptvergleich umfasst die Jahre 2010 bis 2025 und bezieht eine weltweite Aktienanlage ein. Die Bewertung erfolgt monatlich. Eine zusätzliche Untersuchung des US-Marktes beginnt bereits 2003 und endet ebenfalls 2025. Für die Ländergewichtung werden sieben Länder betrachtet. Ein gesonderter Vergleich mit denselben Länderfonds und gleichen Länderanteilen soll den Einfluss der Gewichtungsregel gezielter untersuchen. Ergänzende Varianten der Trendregel dienen dazu, die Empfindlichkeit gegenüber ihren Einstellungen zu betrachten.</p>
````

**Nachher:**

````markdown
<p>Historische ETF-Reihen vertreten Aktienmärkte und Staatsanleihen. Der weltweite Hauptvergleich umfasst 2010 bis 2025 bei monatlicher Bewertung; der US-Zusatzlauf 2003 bis 2025. Sieben Länder werden BIP-gewichtet und mit gleichen Anteilen derselben Länderfonds verglichen, um die Gewichtung gezielter zu prüfen. Trendvarianten untersuchen die Parameterempfindlichkeit.</p>
````


### 5. Einleitung – Zelle `a7ae04cd`

Datei: `notebooks/Einleitung.ipynb`. **56→39; Ersparnis 17.**

Begründung: Mehrfaches Beispiel nachträglicher Erfolgssuche wiederholt 4.1/5.2.1; Definition und eigene Vorabentscheidung bleiben.

Erhalt/Abgleich: Erster Backtest-Definitionssatz wörtlich, feste Vorabregeln, keine Wunschoptimierung, historische Nichtübertragbarkeit und Originalquelle.

**Vorher:**

````markdown
<p>Die rückblickende Anwendung festgelegter Anlageregeln wird als Backtest bezeichnet. Dabei ist mir wichtig, die Regeln vor der Ergebnisauswertung festzuhalten. Es wäre wenig aussagekräftig, so lange andere Einstellungen auszuprobieren, bis eine gewünschte Strategie besonders gut aussieht. Hilpisch beschreibt diese Gefahr als Überanpassung: Eine auf bestimmten historischen Daten erfolgreiche Einstellung muss auf anderen Daten nicht ebenso gut funktionieren [@hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization»].</p>
````

**Nachher:**

````markdown
<p>Die rückblickende Anwendung festgelegter Anlageregeln wird als Backtest bezeichnet. Mir ist wichtig, die Regeln vor der Auswertung festzuhalten, statt gewünschte Erfolge durch nachträgliche Einstellungen zu suchen. Hilpisch beschreibt diese Überanpassungsgefahr: Historischer Erfolg muss auf andere Daten nicht übertragbar sein [@hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization»].</p>
````


### 6. Einleitung – Zelle `3223aafd`

Datei: `notebooks/Einleitung.ipynb`. **48→23; Ersparnis 25.**

Begründung: Beispiel zur damaligen BIP-Verfügbarkeit und wiederholbarem Stand schon in Methodik/Analyse ausführlich.

Erhalt/Abgleich: Kontrollnotwendigkeit, Zeitpunkt, keine späteren BIP-Angaben, drei Dokumentationsbestandteile, Einzelprüfung und identischer Wiederholungsstand.

**Vorher:**

````markdown
<p>Deshalb gehört zur Untersuchung auch die Kontrolle der Daten und ihrer zeitlichen Zuordnung. Beispielsweise darf eine historische Entscheidung nicht auf BIP-Angaben beruhen, die erst später veröffentlicht wurden. Die verwendeten Daten, Einstellungen und Ergebnisse werden dokumentiert, damit einzelne Berechnungen überprüft und die Untersuchung mit demselben Stand wiederholt werden können.</p>
````

**Nachher:**

````markdown
<p>Die Datenkontrolle umfasst ihre zeitliche Zuordnung: BIP-Entscheidungen benötigen damals verfügbare Angaben. Dokumentierte Daten, Einstellungen und Ergebnisse ermöglichen Einzelprüfungen und Wiederholung mit demselben Stand.</p>
````


### 7. Einleitung – Zelle `4a72f361`

Datei: `notebooks/Einleitung.ipynb`. **38→22; Ersparnis 16.**

Begründung: Mehrere identische Gültigkeits-/Zwecksätze aus 4.4/5.5.6 zusammengefasst.

Erhalt/Abgleich: Alle drei Einschränkungen, keine persönliche Kaufempfehlung/Prognose und begründete eigene Daten-/Modellwahl.

**Vorher:**

````markdown
<p>Der Vergleich bleibt auf die ausgewählten Märkte, Zeiträume und Modellannahmen beschränkt. Er soll keine persönliche Kaufempfehlung und keine Vorhersage künftiger Renditen liefern. Die Auswahl der Daten und die Vereinfachungen des Modells werden deshalb als Teil des Untersuchungsdesigns begründet.</p>
````

**Nachher:**

````markdown
<p>Der Vergleich gilt für ausgewählte Märkte, Zeiträume und Modellannahmen, ohne persönliche Kaufempfehlung oder Renditeprognose. Deshalb begründe ich Datenwahl und Modellvereinfachungen als Untersuchungsdesign.</p>
````


### 8. Einleitung – Zelle `5f03e85d`

Datei: `notebooks/Einleitung.ipynb`. **59→40; Ersparnis 19.**

Begründung: Doppelte Kapitelübersicht aus Überblick 1.2 auf Untersuchungsweg konzentriert.

Erhalt/Abgleich: Theorie/Python, Methodik, Daten/Parameter/Durchführung, Resultate/Interpretation und Fazitfunktionen in 1.2 vollständig vorhanden.

**Vorher:**

````markdown
<p>Die Theorie erklärt Finanzdaten, Kennzahlen und Strategien; Python-Beispiele verbinden Formeln und Anwendung. Die Methodik legt Vergleichsbedingungen fest. In der Analyse begründe ich Daten und Parameter, beschreibe die Durchführung und stelle Ergebnisse sowie Interpretation dar. Das Fazit führt die Erkenntnisse zur Forschungsfrage zusammen und ordnet Grenzen und mögliche Weiterführungen ein. So führt die Untersuchung von Anlageideen zu einem begründeten Rendite-Risiko-Vergleich.</p>
````

**Nachher:**

````markdown
<p>Der Aufbau steht in Abschnitt 1.2. Python-Beispiele verbinden die Theorie mit der Anwendung; Methodik und Analyse führen von festgelegten Vergleichsbedingungen über Datenwahl und Durchführung zu Ergebnissen und Interpretation. Das Fazit beantwortet die Forschungsfrage und ordnet Grenzen sowie Weiterführungen ein.</p>
````


### 9. Theorie – Zelle `d507a002`

Datei: `notebooks/Theorie.ipynb`. **92→75; Ersparnis 17.**

Begründung: Zweite Erläuterung zur Diversifikationswirkung bündelt parallele Aussagen; Korrelationsdefinition bleibt wörtlich.

Erhalt/Abgleich: Unter +1 genügt, negative Korrelation keine Voraussetzung, tendenzielle Wirkung; erster Definitionsabsatz unverändert.

**Vorher:**

````markdown


#### Korrelation


<p>Mit der Korrelation lässt sich untersuchen, wie eng die Renditen zweier Anlagen linear zusammenhängen. Ihr Koeffizient reicht von -1 bis +1: Am positiven Grenzwert bewegen sich beide Reihen vollständig in dieselbe Richtung, am negativen Grenzwert genau entgegengesetzt. Ein Wert von 0 zeigt, dass kein linearer Zusammenhang nachweisbar ist [@kommerSouveraenInvestierenMit2025, S. 82-83].</p>
<p>Ein Portfolio kann bereits von einer Korrelation unter +1 profitieren, da sich die Wertveränderungen seiner Bestandteile dann nicht vollkommen parallel entwickeln. Eine negative Korrelation ist somit keine Voraussetzung. Tendenziell nimmt die risikomindernde Wirkung der Kombination zu, wenn der Korrelationskoeffizient sinkt [@kommerSouveraenInvestierenMit2025, S. 82-83].</p>
<b>Formel für die Korrelation:</b>
````

**Nachher:**

````markdown


#### Korrelation


<p>Mit der Korrelation lässt sich untersuchen, wie eng die Renditen zweier Anlagen linear zusammenhängen. Ihr Koeffizient reicht von -1 bis +1: Am positiven Grenzwert bewegen sich beide Reihen vollständig in dieselbe Richtung, am negativen Grenzwert genau entgegengesetzt. Ein Wert von 0 zeigt, dass kein linearer Zusammenhang nachweisbar ist [@kommerSouveraenInvestierenMit2025, S. 82-83].</p>
<p>Schon unter +1 verlaufen die Bestandteile nicht vollkommen parallel; negative Korrelation ist nicht erforderlich. Mit sinkender Korrelation nimmt die risikomindernde Wirkung tendenziell zu [@kommerSouveraenInvestierenMit2025, S. 82-83].</p>
<b>Formel für die Korrelation:</b>
````


### 10. Theorie – Zelle `d508a002`

Datei: `notebooks/Theorie.ipynb`. **24→20; Ersparnis 4.**

Begründung: Gewichtungsdrift ist unmittelbar in der unveränderten Formel/Variablenerklärung und später im konkreten 60/40-Beispiel erläutert.

Erhalt/Abgleich: Besser gelaufene Anlage bekommt grösseres Gewicht, Abweichung vom Ziel, Beispiel nach einem Jahr; Rebalancing-Definition bleibt unverändert.

**Vorher:**

````markdown


#### Gewichtungsdrift und Rebalancing


<p>Unterschiedliche Renditen verschieben die Portfolioanteile: Die besser gelaufene Anlage erhält ein grösseres Gewicht. Kommer zeigt diese Abweichung von den Zielgewichten bereits nach einem Jahr [@kommerSouveraenInvestierenMit2025, S. 523].</p>
````

**Nachher:**

````markdown


#### Gewichtungsdrift und Rebalancing


<p>Unterschiedliche Renditen erhöhen das Gewicht der besser gelaufenen Anlage. Kommer zeigt diese Drift von den Zielgewichten schon nach einem Jahr [@kommerSouveraenInvestierenMit2025, S. 523].</p>
````


### 11. Theorie – Zelle `d509a002`

Datei: `notebooks/Theorie.ipynb`. **29→21; Ersparnis 8.**

Begründung: Vorteils-/Risikoaufzählung in einem Absatz statt wiederholter Strategieeinleitung.

Erhalt/Abgleich: Alle drei Vorteile, alle drei Risiken und Benchmarkrolle; Buy-and-Hold-Definition davor unverändert.

**Vorher:**

````markdown


#### Vorteile, Risiken und Benchmark


<p>Vorteile sind geringere Transaktionskosten, weniger Aufwand und vermiedene Timing-Fehler durch häufiges Handeln [@kommerSouveraenInvestierenMit2025, S. 447 und 450].</p>
<p>Markteinbrüche, Drawdowns und Erholungsphasen bleiben Teil eines reinen Aktienportfolios [@kommerSouveraenInvestierenMit2025, S. 447 und 452-458]. Die einfache passive Strategie dient hier als Benchmark.</p>
````

**Nachher:**

````markdown


#### Vorteile, Risiken und Benchmark


<p>Vorteile: weniger Transaktionskosten, Aufwand und Timing-Fehler häufigen Handelns [@kommerSouveraenInvestierenMit2025, S. 447 und 450]. Aktien bleiben Markteinbrüchen, Drawdowns und Erholungsphasen ausgesetzt [@kommerSouveraenInvestierenMit2025, S. 447 und 452-458]; die passive Strategie dient als Benchmark.</p>
````


### 12. Theorie – Zelle `d510a002`

Datei: `notebooks/Theorie.ipynb`. **69→54; Ersparnis 15.**

Begründung: Historische Korrelations-/60/40-Befunde bereits 3.1.2/3.3.1; ein kompakter Vergleich erhält alle Belege.

Erhalt/Abgleich: Nicht perfekt/konstant/immer negativ, Länderunterschiede, 2022, keine universelle Schutzwirkung, langfristige reale CFA-Werte und Kommers Tradeoff.

**Vorher:**

````markdown


#### Diversifikation und Grenzen


<p>Aktien und Anleihen verlaufen nicht perfekt gleichgerichtet. Ihre Korrelation ist aber weder konstant noch immer negativ und unterschied sich historisch zwischen Ländern [@phamPerformance60402025, S. 1-7].</p>
<p>2022 verloren beide Anlageklassen. Anleihen schützen daher nicht in jeder Phase. Über lange Zeiträume beobachtete das CFA-Paper trotzdem geringere Volatilitäten und Drawdowns sowie positive reale Renditen, mit Länderunterschieden [@phamPerformance60402025, S. 2-7].</p>
<p>Auch Kommer zeigt den Zielkonflikt: 60/40 hatte weniger Rendite, aber niedrigere Volatilität und MDD als ein globales Aktienportfolio [@kommerSouveraenInvestierenMit2025, S. 88].</p>
````

**Nachher:**

````markdown


#### Diversifikation und Grenzen


<p>Aktien und Anleihen verlaufen nicht perfekt gleichgerichtet; ihre Korrelation ist weder konstant noch immer negativ und variiert nach Land [@phamPerformance60402025, S. 1-7].</p>
<p>2022 verloren beide; Anleihen schützen nicht jede Phase. Langfristig fand das CFA-Paper geringere Volatilität und Drawdowns und positive reale Renditen mit Länderunterschieden [@phamPerformance60402025, S. 2-7]. Bei Kommer hatte 60/40 weniger Rendite, Volatilität und MDD als globale Aktien [@kommerSouveraenInvestierenMit2025, S. 88].</p>
````


### 13. Theorie – Zelle `035b1ffe`

Datei: `notebooks/Theorie.ipynb`. **80→72; Ersparnis 8.**

Begründung: Historische Bewertung knapp verbunden; derselbe Vergleich wird später in 3.3.1 eingeordnet.

Erhalt/Abgleich: Formel/Variablen/Formelherkunft unverändert; Teilperioden, Risiken, schwieriger Nachweis, Kosten und fehlender Überlegenheitsbeweis.

**Vorher:**

````markdown
$$
w_c^{BIP}=\frac{BIP_c}{\sum_d BIP_d}
$$
Dabei bezeichnet **$w_c^{\mathrm{BIP}}$** das BIP-Gewicht des Landes **$c$**, **$\mathrm{BIP}_c$** dessen Bruttoinlandsprodukt und **$\sum_d \mathrm{BIP}_d$** das gesamte Bruttoinlandsprodukt aller berücksichtigten Länder.
<p>Die Gleichung ist eine eigene formale Darstellung der von Kommer beschriebenen Ländergewichtung nach Bruttoinlandsprodukt [@kommerSouveraenInvestierenMit2025, S. 474-476].</p>
<p>In Kommers historischem Vergleich waren die Gesamtunterschiede gering; in Teilperioden wechselte die bessere Methode. Volatilität und MDD lagen nahe beieinander [@kommerSouveraenInvestierenMit2025, S. 474-476].</p>
<p>Kommer bevorzugt BIP-Gewichtung zur Begrenzung hoher Länderanteile und möglicher Klumpenrisiken, deren Nachweis er historisch selbst als schwierig bezeichnet. Mehr Komplexität und Transaktionskosten sind möglich [@kommerSouveraenInvestierenMit2025, S. 476-477]. Eine allgemeine Überlegenheit ist damit nicht bewiesen.</p>
````

**Nachher:**

````markdown
$$
w_c^{BIP}=\frac{BIP_c}{\sum_d BIP_d}
$$
Dabei bezeichnet **$w_c^{\mathrm{BIP}}$** das BIP-Gewicht des Landes **$c$**, **$\mathrm{BIP}_c$** dessen Bruttoinlandsprodukt und **$\sum_d \mathrm{BIP}_d$** das gesamte Bruttoinlandsprodukt aller berücksichtigten Länder.
<p>Die Gleichung ist eine eigene formale Darstellung der von Kommer beschriebenen Ländergewichtung nach Bruttoinlandsprodukt [@kommerSouveraenInvestierenMit2025, S. 474-476].</p>
<p>Kommers Gesamtunterschiede waren gering, die bessere Methode wechselte zwischen Teilperioden; Volatilität und MDD lagen nahe beieinander [@kommerSouveraenInvestierenMit2025, S. 474-476].</p>
<p>Er bevorzugt BIP zur Begrenzung hoher Länderanteile und Klumpenrisiken, deren historischen Nachweis er selbst schwierig nennt. Höhere Komplexität und Kosten sind möglich; allgemeine Überlegenheit ist nicht bewiesen [@kommerSouveraenInvestierenMit2025, S. 476-477].</p>
````


### 14. Theorie – Zelle `005fce46`

Datei: `notebooks/Theorie.ipynb`. **101→62; Ersparnis 39.**

Begründung: Mehrfache Beschreibung von Zeitordnung/Frequenz/Umwandlung zusammengefasst; technischer Verweis nur vorhandenes Ziel.

Erhalt/Abgleich: Zeitreihe, Datierung/Reihenfolge/Veränderung, vier Frequenzen, langfristiger Vergleich und Downsampling bleiben hier; Code und Foresight-Absatz unverändert.

**Vorher:**

````markdown
### Historische Finanzdaten und Zeitreihen

#### Zeitreihen

Historische Finanzdaten bilden die Grundlage meines Vergleichs. Eine finanzielle Zeitreihe entsteht etwa, wenn der Kurs eines Indexfonds über einen längeren Zeitraum erfasst wird. Die Beobachtungen sind bestimmten Daten zugeordnet. Ihre Reihenfolge zeigt die Veränderung von einer Beobachtung zur nächsten und ist für den Strategievergleich wichtig.

#### Frequenzen

Die Daten können täglich, wöchentlich, monatlich oder jährlich vorliegen. Für meinen langfristigen Vergleich sind kleinere Intervalle nicht wesentlich. Die technische Aliasübersicht steht in @sec-resampling-beispiele.

#### Resampling

Resampling bringt Daten in die gewünschte Frequenz, meist von kleineren zu grösseren Intervallen (Downsampling). So werden sie einheitlich und vergleichbar. Das folgende Python-Beispiel zeigt die Umwandlung; die technischen API-Hinweise und Belege stehen in @sec-resampling-beispiele.
````

**Nachher:**

````markdown
### Historische Finanzdaten und Zeitreihen

#### Zeitreihen

Historische Finanzdaten tragen meinen Vergleich. Über längere Zeit erfasste Indexfondskurse bilden eine Zeitreihe: Datierte, geordnete Beobachtungen zeigen ihre Veränderung.

#### Frequenzen

Mögliche Frequenzen sind täglich, wöchentlich, monatlich oder jährlich; kleinere Intervalle sind für meinen langfristigen Vergleich nicht wesentlich. Die Aliasübersicht steht in @sec-resampling-beispiele.

#### Resampling

Resampling vereinheitlicht die Frequenz, meist durch Downsampling von kleineren zu grösseren Intervallen. Das folgende Python-Beispiel zeigt dies; API-Hinweise und Belege stehen in @sec-resampling-beispiele.
````


### 15. Theorie – Zelle `0a5b52df`

Datei: `notebooks/Theorie.ipynb`. **44→11; Ersparnis 33.**

Begründung: Schrittbeschreibung wiederholt die anschliessende Formel und unveränderte Variablenerklärung 32e3c634. Verbliebener Formeleinleitungssatz ist ebenfalls in nachfolgender Formel/Variablenerklärung sichtbar.

Erhalt/Abgleich: Definitionssatz wörtlich; Mittelwert, Abweichungen, quadrierte Summation und Stichprobenformel unmittelbar danach unverändert. Definitionssatz wörtlich bis zur Satzgrenze; sämtliche Rechenschritte/Formel/Variablen bleiben unmittelbar danach.

**Vorher:**

````markdown


#### Berechnung der Volatilität


<p>Die historische Volatilität wird anhand der Standardabweichung der periodischen Renditen bestimmt. Dazu wird zuerst der arithmetische Mittelwert der betrachteten Renditen berechnet. Anschliessend wird untersucht, wie stark die Rendite jeder einzelnen Periode von diesem Durchschnitt abweicht. Die Standardabweichung fasst diese Abweichungen in einer Kennzahl zusammen [@kommerSouveraenInvestierenMit2025, S. 144].</p>
````

**Nachher:**

````markdown


#### Berechnung der Volatilität


<p>Die historische Volatilität wird anhand der Standardabweichung der periodischen Renditen bestimmt [@kommerSouveraenInvestierenMit2025, S. 144].</p>
````


### 16. Theorie – Zelle `03486f6b`

Datei: `notebooks/Theorie.ipynb`. **86→45; Ersparnis 41.**

Begründung: Fünf wiederholte Sätze zum beschränkten Risikoumfang in einen Absatz gebündelt.

Erhalt/Abgleich: Erster Diversifikationsabsatz und dessen Bedingung unverändert; positive/negative Ausschläge, Tiefe/Dauer und einzelner Risikotyp bleiben.

**Vorher:**

````markdown


#### Diversifikation


<p>Diversifikation kann die Portfoliovolatilität senken. Ein breit gestreutes Portfolio schwankt meist weniger, sofern die Renditen seiner Wertpapiere nicht untereinander zusammenhängen [@kommerSouveraenInvestierenMit2025, S. 148].</p>
<p>Die Volatilität kennt jedoch auch Grenzen. Da sowohl positive als auch negative Ausschläge gemessen werden, wird nicht zwischen unerwünschten Verlusten und erwünschten Gewinnen unterschieden. Ausserdem sagt sie nichts über die Stärke der Verluste und die Länge der Verlustphase aus. Sie misst nur einen Risikotyp und deckt nicht das ganze Risikospektrum ab. Deswegen kann man die Volatilität nicht als einzigen Faktor nutzen, um das Gesamtrisiko zu beurteilen [@kommerSouveraenInvestierenMit2025, S. 151].</p>
````

**Nachher:**

````markdown


#### Diversifikation


<p>Diversifikation kann die Portfoliovolatilität senken. Ein breit gestreutes Portfolio schwankt meist weniger, sofern die Renditen seiner Wertpapiere nicht untereinander zusammenhängen [@kommerSouveraenInvestierenMit2025, S. 148].</p>
<p>Volatilität unterscheidet positive und negative Ausschläge nicht. Sie beschreibt weder Verlusttiefe noch Verlustdauer und erfasst nur einen Risikotyp; allein genügt sie deshalb nicht zur Gesamtbeurteilung [@kommerSouveraenInvestierenMit2025, S. 151].</p>
````


### 17. Theorie – Zelle `f17d8f57`

Datei: `notebooks/Theorie.ipynb`. **67→31; Ersparnis 36.**

Begründung: Wiederholte Formulierungen zu historischer Gültigkeit gekürzt; Definitionen davor bleiben unverändert.

Erhalt/Abgleich: Zeitraum/Frequenz, mögliche deutliche Unterschätzung mit Jahresendwerten, langer Zeitraum/Monatsdaten, keine garantierte Zukunftsgrenze.

**Vorher:**

````markdown
<p>Der berechnete Maximum Drawdown hängt vom gewählten Zeitraum und von der Frequenz der Daten ab. Werden nur Jahresendwerte verwendet, können zwischenzeitliche Verluste übersehen und der tatsächliche Drawdown deutlich unterschätzt werden. Kommer empfiehlt deshalb einen langen Beobachtungszeitraum und weist auf die genauere Erfassung mit Monatsdaten hin. Der historische Maximum Drawdown beschreibt nur den schlimmsten Verlust in der untersuchten Stichprobe und stellt keine garantierte Verlustgrenze für die Zukunft dar [@kommerSouveraenInvestierenMit2025, S. 152-153].</p>
````

**Nachher:**

````markdown
<p>Der MDD hängt von Zeitraum und Frequenz ab. Jahresendwerte können zwischenzeitliche Verluste übersehen und ihn deutlich unterschätzen. Kommer empfiehlt lange Beobachtung und genauer erfassende Monatsdaten. Der Stichproben-MDD garantiert keine künftige Verlustgrenze [@kommerSouveraenInvestierenMit2025, S. 152-153].</p>
````


### 18. Theorie – Zelle `d506a001`

Datei: `notebooks/Theorie.ipynb`. **68→56; Ersparnis 12.**

Begründung: Interpretationssatz gestrafft; zentrale Sharpe-Definition bleibt wörtlich.

Erhalt/Abgleich: Historische Entschädigung, je Risikoeinheit und nur unter gleichen Berechnungsbedingungen; erster Definitionsabsatz/Formel/Variablen unverändert.

**Vorher:**

````markdown


### Sharpe Ratio




#### Bedeutung der Sharpe Ratio


<p>Die Rendite allein zeigt nicht, mit welchen Schwankungen ein Anlageergebnis erreicht wurde. Für einen risikobereinigten Vergleich wird deshalb zunächst die risikofreie Rendite von der Anlagenrendite abgezogen. Die Sharpe Ratio stellt den Durchschnitt dieser Überschussrenditen der Volatilität gegenüber [@kommerSouveraenInvestierenMit2025, S. 165-166].</p>
<p>Das Ergebnis lässt sich als historische Entschädigung für eine Einheit des gemessenen Schwankungsrisikos interpretieren. Unter ansonsten gleichen Berechnungsbedingungen weist ein höherer Wert auf ein vorteilhafteres Verhältnis zwischen Überschussrendite und Volatilität hin [@kommerSouveraenInvestierenMit2025, S. 166].</p>
````

**Nachher:**

````markdown


### Sharpe Ratio




#### Bedeutung der Sharpe Ratio


<p>Die Rendite allein zeigt nicht, mit welchen Schwankungen ein Anlageergebnis erreicht wurde. Für einen risikobereinigten Vergleich wird deshalb zunächst die risikofreie Rendite von der Anlagenrendite abgezogen. Die Sharpe Ratio stellt den Durchschnitt dieser Überschussrenditen der Volatilität gegenüber [@kommerSouveraenInvestierenMit2025, S. 165-166].</p>
<p>Historisch lässt sich der Wert als Entschädigung je Einheit Schwankungsrisiko deuten. Ein höherer Wert ist unter gleichen Berechnungsbedingungen günstiger [@kommerSouveraenInvestierenMit2025, S. 166].</p>
````


### 19. Theorie – Zelle `d506a004`

Datei: `notebooks/Theorie.ipynb`. **49→34; Ersparnis 15.**

Begründung: Doppelte Nichtvergleichbarkeit verschiedener Zeiträume entfernt, verbleibende Vergleichsbedingung explizit.

Erhalt/Abgleich: Alle drei Quellenbelege, RF/Raw-Abgrenzung, Volatilitätsbegrenzung und separate Rendite-/Drawdownbeurteilung.

**Vorher:**

````markdown


#### Interpretation und Grenzen


<p>Sharpe Ratios sind nur bei gleichem Zeitraum, gleicher Frequenz und Berechnungsweise sinnvoll vergleichbar. Kennzahlen verschiedener Zeiträume dürfen nicht direkt gegenübergestellt werden [@kommerSouveraenInvestierenMit2025, S. 166].</p>
<p>Die vereinfachte Raw Sharpe Ratio zieht keine risikofreie Rendite ab; beide Varianten dürfen nicht vermischt werden [@kommerSouveraenInvestierenMit2025, S. 165-166]. Sharpe erfasst nur Volatilitätsrisiko. Rendite und Drawdown werden deshalb zusätzlich getrennt betrachtet [@kommerSouveraenInvestierenMit2025, S. 166].</p>
````

**Nachher:**

````markdown


#### Interpretation und Grenzen


<p>Sharpe Ratios sind nur bei gleichem Zeitraum, gleicher Frequenz und Berechnungsweise vergleichbar [@kommerSouveraenInvestierenMit2025, S. 166].</p>
<p>Raw Sharpe zieht keine risikofreie Rendite ab; beide Varianten sind zu trennen [@kommerSouveraenInvestierenMit2025, S. 165-166]. Sharpe erfasst nur Volatilitätsrisiko; Rendite und Drawdown werden zusätzlich betrachtet [@kommerSouveraenInvestierenMit2025, S. 166].</p>
````


### 20. Theorie – Zelle `d512a004`

Datei: `notebooks/Theorie.ipynb`. **107→61; Ersparnis 46.**

Begründung: Trendgrenzen bündeln dieselben Bedingungen wie 3.3.3/3.3.4 ohne Begriffs- oder Quellenverlust.

Erhalt/Abgleich: Nachlauf, Seitwärtsfehlsignale, wiederholte Wechsel, Auswahl-/Bewertungsdaten, Vorabbegründung, Kosten/Spannen mit Bid-Ask-Erklärung und mögliche Begünstigung.

**Vorher:**

````markdown


#### Grenzen der Trendfolge


<p>Gleitende Durchschnitte sind nachlaufende Indikatoren, weil sie nur vergangene Kurse verwenden. Ein Trend wird somit erst erkannt, nachdem die Kursbewegung bereits begonnen hat. In Seitwärtsphasen können häufige Kreuzungen zu Fehlsignalen und wiederholten Positionswechseln führen [@hilpischPythonFinanceMastering2019, S. 326-328 und 689-694].</p>
<p>Hilpisch zeigt, dass viele Kombinationen von kurzen und langen Fenstern nachträglich getestet werden können [@hilpischPythonFinanceMastering2019, S. 697]. Wird nur die historisch beste Kombination ausgewählt und danach mit denselben Daten beurteilt, besteht ein Overfitting-Risiko. Die Hauptparameter müssen deshalb vor dem eigentlichen Vergleich begründet und festgelegt werden.</p>
<p>Der vereinfachte Beispiel-Backtest von Hilpisch lässt unter anderem Gebühren, Geld-Brief-Spannen (Differenz zwischen Bid und Ask) und weitere Marktmechanismen weg [@hilpischPythonFinanceMastering2019, S. 696]. Solche Vereinfachungen können eine Strategie mit häufigen Transaktionen im historischen Vergleich begünstigen.</p>
````

**Nachher:**

````markdown


#### Grenzen der Trendfolge


<p>SMAs verwenden vergangene Kurse und erkennen Trends erst nach deren Beginn. Seitwärtsphasen können Fehlsignale und häufige Positionswechsel auslösen [@hilpischPythonFinanceMastering2019, S. 326-328 und 689-694].</p>
<p>Viele Fensterkombinationen lassen sich nachträglich testen [@hilpischPythonFinanceMastering2019, S. 697]. Auswahl des historischen Siegers und Bewertung auf denselben Daten riskieren Overfitting; Hauptparameter müssen vorab begründet feststehen.</p>
<p>Hilpischs Beispiel lässt Gebühren, Geld-Brief-Spannen (Differenz zwischen Bid und Ask) und weitere Marktmechanismen weg [@hilpischPythonFinanceMastering2019, S. 696]. Dies kann häufig handelnde Strategien historisch begünstigen.</p>
````


### 21. Theorie – Zelle `d513a001`

Datei: `notebooks/Theorie.ipynb`. **92→56; Ersparnis 36.**

Begründung: Bereits in 3.1.5/3.1.6 beschriebene historische Unterschiede knapp zusammengeführt, Vergleichsbedingungen vollständig.

Erhalt/Abgleich: Genau definierte Strategie/Stichprobe im unveränderten Einleitungs-Backtestbegriff; keine Zukunftsgarantie, Land/Generation/Marktphase, wechselnder Gewichtungssieger, fünf Vergleichsbedingungen.

**Vorher:**

````markdown


## Methodische Grenzen




### Historische Stichprobe und Vergleichbarkeit


<p>Ein Backtest zeigt, wie eine genau definierte Strategie innerhalb einer gewählten historischen Stichprobe abgeschnitten hätte. Das Ergebnis garantiert nicht, dass dieselbe Beziehung auch in der Zukunft gilt. Das CFA-Paper zeigt beispielsweise unterschiedliche Ergebnisse des 60/40-Portfolios je nach Land, Generation und Marktphase [@phamPerformance60402025, S. 1-7]. Auch beim Vergleich von Marktkapitalisierungs- und BIP-Gewichtung wechselte die besser abschneidende Methode zwischen den Teilperioden [@kommerSouveraenInvestierenMit2025, S. 474-476].</p>
<p>Für einen fairen Vergleich müssen alle Strategien auf derselben Grundlage untersucht werden. Dazu gehören ein identischer Zeitraum, eine einheitliche Datenfrequenz je Kennzahl, dieselbe Währung, dieselbe Behandlung von Dividenden und eine einheitliche nominale oder reale Berechnung [@kommerSouveraenInvestierenMit2025, S. 22-23, 166 und 466-467; @hilpischPythonFinanceMastering2019, S. 319-321].</p>
````

**Nachher:**

````markdown


## Methodische Grenzen




### Historische Stichprobe und Vergleichbarkeit


<p>Ein Backtest zeigt, wie eine genau definierte Strategie innerhalb einer gewählten historischen Stichprobe abgeschnitten hätte. Dies garantiert keine künftige Gültigkeit. Das CFA-Paper findet je nach Land, Generation und Marktphase andere 60/40-Ergebnisse [@phamPerformance60402025, S. 1-7]; bei Marktkapitalisierungs-/BIP-Gewichtung wechselt der Sieger zwischen Teilperioden [@kommerSouveraenInvestierenMit2025, S. 474-476].</p>
<p>Faire Vergleiche verlangen gleichen Zeitraum, gleiche Frequenz je Kennzahl, Währung, Dividendenbehandlung und nominale oder reale Berechnung [@kommerSouveraenInvestierenMit2025, S. 22-23, 166 und 466-467; @hilpischPythonFinanceMastering2019, S. 319-321].</p>
````


### 22. Theorie – Zelle `d513a003`

Datei: `notebooks/Theorie.ipynb`. **74→58; Ersparnis 16.**

Begründung: Ausführliches identisches SMA-Suchbeispiel aus 3.2.6.3 durch kurze Erklärung mit Verweis ersetzt.

Erhalt/Abgleich: Data-Snooping-Definition und Kommers Overfitting-/Out-of-Sample-Aussage wörtlich; identische Auswahl-/Bewertungsdaten und Zufall versus stabile Regel bleiben.

**Vorher:**

````markdown


### Data Snooping und Overfitting


<p>Data Snooping entsteht, wenn historische Daten bewusst oder unbewusst so lange durchsucht werden, bis ein gewünschtes Ergebnis erscheint. Kommer verbindet den Begriff unter anderem mit Backtesting with Overfitting und verweist auf Out-of-Sample-Tests als Gegenmassnahme [@kommerSouveraenInvestierenMit2025, S. 607-608].</p>
<p>Ein Beispiel ist die nachträgliche Suche nach der besten Kombination zweier SMA-Fenster. Wenn dieselben Daten sowohl zur Auswahl der Parameter als auch zur Bewertung der Strategie genutzt werden, kann das Modell zufällige Eigenschaften der Vergangenheit statt einer stabilen Regel abbilden [@hilpischPythonFinanceMastering2019, S. 697].</p>
````

**Nachher:**

````markdown


### Data Snooping und Overfitting


<p>Data Snooping entsteht, wenn historische Daten bewusst oder unbewusst so lange durchsucht werden, bis ein gewünschtes Ergebnis erscheint. Kommer verbindet den Begriff unter anderem mit Backtesting with Overfitting und verweist auf Out-of-Sample-Tests als Gegenmassnahme [@kommerSouveraenInvestierenMit2025, S. 607-608].</p>
<p>Bei SMA-Fenstern können dieselben Auswahl- und Bewertungsdaten zufällige Vergangenheitseigenschaften statt stabiler Regeln hervorheben [@hilpischPythonFinanceMastering2019, S. 697]; die nachträgliche Fenstersuche ist in Abschnitt 3.2.6.3 erläutert.</p>
````


### 23. Methodik – Zelle `35c815dc`

Datei: `notebooks/Methodik.ipynb`. **42→30; Ersparnis 12.**

Begründung: Generik und Vorabentscheidung in mehreren Kapiteln wiederholt; methodischer Eigenentscheid bleibt vollständig.

Erhalt/Abgleich: Geeignete Daten/Einstellungen, eigene Anlagen-/Zeit-/Regelwahl vor Auswertung, nachträgliche Erfolgssuche und Übertragbarkeitsgrenze.

**Vorher:**

````markdown
<p>Das allgemeine Rechensystem soll unterschiedliche geeignete Daten und Einstellungen verarbeiten können. Für diese Untersuchung lege ich Anlagen, Zeiträume und Regeln vor der Auswertung fest. So vermeide ich die nachträgliche Auswahl besonders erfolgreicher Einstellungen, die auf anderen Daten nicht ebenso gut funktionieren müssen [@hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization»].</p>
````

**Nachher:**

````markdown
<p>Das System soll unterschiedliche geeignete Daten und Einstellungen verarbeiten. Anlagen, Zeiträume und Regeln lege ich vorab fest, statt nachträglich erfolgreiche Einstellungen auszuwählen, die auf andere Daten nicht übertragbar sein müssen [@hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization»].</p>
````


### 24. Methodik – Zelle `09fe7307`

Datei: `notebooks/Methodik.ipynb`. **18→13; Ersparnis 5.**

Begründung: Einleitung der unveränderten Lauftabelle bündelt Zuordnungsbeschreibung.

Erhalt/Abgleich: Fünf vorab festgelegte Läufe, Identifikationsfunktion und keine zusätzliche Finanzmethode.

**Vorher:**

````markdown
<p>Die Untersuchung besteht aus fünf festgelegten Läufen. Die Kürzel dienen ihrer eindeutigen Zuordnung; sie bezeichnen keine zusätzlichen Finanzmethoden.</p>
````

**Nachher:**

````markdown
<p>Die fünf festgelegten Läufe werden durch Kürzel zugeordnet; diese bezeichnen keine zusätzlichen Finanzmethoden.</p>
````


### 25. Methodik – Zelle `60c85505`

Datei: `notebooks/Methodik.ipynb`. **65→43; Ersparnis 22.**

Begründung: Datenbezug erklärt dieselben Schritte später in 5.2.4/5.2.5; hier vollständig, aber gebündelt.

Erhalt/Abgleich: Quelle/API, Adj Close, Dividenden/Splits, keine Doppelzählung, Monatsbewertung/Quelldatum, keine stille Ergänzung, Produktabgleich.

**Vorher:**

````markdown
<p>Die täglichen ETF-Daten beziehe ich über <code>yfinance</code> von Yahoo Finance. Ausgewertet wird <code>Adj Close</code>, das Yahoo als um Dividenden und Splits bereinigten Schlusskurs beschreibt [@WhatAdjustedClose]. Dividenden werden deshalb nicht nochmals hinzuaddiert. Für jeden Monat wird die letzte tatsächlich vorhandene Bewertung übernommen; ihr ursprüngliches Datum bleibt dokumentiert. Fehlende notwendige Werte werden nicht still aufgefüllt. Produktangaben von Vanguard und iShares ergänzen die Prüfung, welche Anlagen die Fonds vertreten.</p>
````

**Nachher:**

````markdown
<p>Tägliche ETF-Daten beziehe ich mit <code>yfinance</code> von Yahoo Finance. <code>Adj Close</code> berücksichtigt laut Yahoo Dividenden und Splits [@WhatAdjustedClose]; Dividenden werden nicht nochmals addiert. Monatlich gilt die letzte tatsächliche Bewertung mit dokumentiertem Quelldatum; notwendige Lücken werden nicht still aufgefüllt. Vanguard-/iShares-Produktangaben prüfen die vertretenen Anlagen.</p>
````


### 26. Methodik – Zelle `0af0c786`

Datei: `notebooks/Methodik.ipynb`. **43→32; Ersparnis 11.**

Begründung: Vorabfestlegung und Gültigkeitsgrenze werden in 5.2.9/5.5.6 ausführlich erläutert; hier vollständiger Kern.

Erhalt/Abgleich: Drei dokumentierte Vorabkomponenten, Prüfzweck, begrenzte Schlussfolgerungen und beide ausgeschlossenen Überlegenheitsbehauptungen.

**Vorher:**

````markdown
<p>Daten, Einstellungen und Programmstand werden vor den Hauptläufen festgehalten. Tests und Gegenrechnungen prüfen, ob die Berechnungen den vorgegebenen Regeln entsprechen. Die Schlussfolgerungen bleiben auf die untersuchten Daten und Annahmen begrenzt; eine statistisch nachgewiesene oder künftig sichere Überlegenheit einer Strategie wird damit nicht beansprucht.</p>
````

**Nachher:**

````markdown
<p>Daten, Einstellungen und Programmstand stehen vor Hauptläufen fest. Tests und Gegenrechnungen prüfen die Regeleinhaltung der Berechnungen. Schlussfolgerungen gelten für untersuchte Daten und Annahmen; statistisch nachgewiesene oder künftig sichere Überlegenheit wird nicht beansprucht.</p>
````


### 27. Analyse – Zelle `c50744c1`

Datei: `notebooks/Analyse.ipynb`. **146→120; Ersparnis 26.**

Begründung: Modellbrücke enthält mehrfaches technisches Framing; derselbe Aufbau ist in bestehenden Anhängen dokumentiert.

Erhalt/Abgleich: Alle elf Original-Anhangsverweise, Trennung/Generik, eigene Reihenfolge, Datenprüfung, Rohstände/Lücken, kein Laufdownload, Manifest, wesentliche Codex-Arbeit/Eigenvorgaben, feste Vorabwahl.

**Vorher:**

````markdown
Für die Analyse führe ich die theoretischen Berechnungen in einer gemeinsamen Engine zusammen. Sie trennt Datenaufbereitung, Strategieregeln, Kennzahlen und Export und soll unterschiedliche geeignete Daten und Einstellungen verarbeiten können. Die Entwicklung beginnt mit dem Datenvertrag; ihre Reihenfolge ist meine eigene Designentscheidung (@sec-technik-5-2).

Markt-, Zins- und BIP-Daten werden vereinheitlicht und geprüft. Rohdaten bleiben getrennt erhalten; fehlende Werte werden nicht still interpoliert. Datenvertrag, Umwandlung und Aufbereitung stehen in @sec-daten-5-3, @sec-daten-5-4 und @sec-daten-5-5, Prüfregeln in @sec-pruefung-vor-simulation. Während eines Laufs werden keine neuen Marktdaten geladen.

Konfiguration, Ergebnisvertrag und Aufbau sind in @sec-technik-5-6, @sec-technik-5-7 und @sec-technik-5-8 dokumentiert. Gewichte und Signale helfen bei der Interpretation; das Run-Manifest ordnet Daten, Einstellungen und Programmstand zu. Codex unterstützte wesentlich die technische Integration der vorgegebenen Bausteine und die Erstellung von Tests mit künstlichen Daten; die finanzwissenschaftlichen Vorgaben und Untersuchungsentscheidungen stammen von mir (@sec-technik-5-9).

Für die eigentliche Untersuchung werden feste Daten und Parameter vor der Auswertung gewählt. Sie werden nicht nachträglich zugunsten eines gewünschten Resultats verändert [@hilpischPythonFinanceMastering2019, S. 697; @kommerSouveraenInvestierenMit2025, S. 607–608].
````

**Nachher:**

````markdown
Die Engine verbindet die theoretischen Berechnungen, trennt Datenaufbereitung, Strategieregeln, Kennzahlen und Export und soll unterschiedliche geeignete Daten und Einstellungen verarbeiten. Die Entwicklung beginnt mit dem Datenvertrag; die Reihenfolge ist meine Designentscheidung (@sec-technik-5-2).

Markt-, Zins- und BIP-Daten werden vereinheitlicht und geprüft, Rohdaten getrennt erhalten und Lücken nicht still interpoliert. Datenvertrag, Umwandlung, Aufbereitung und Prüfung stehen in @sec-daten-5-3, @sec-daten-5-4, @sec-daten-5-5 und @sec-pruefung-vor-simulation. Im Lauf werden keine neuen Marktdaten geladen.

Konfiguration, Ergebnisvertrag und Aufbau sind in @sec-technik-5-6, @sec-technik-5-7 und @sec-technik-5-8 dokumentiert. Gewichte und Signale dienen der Interpretation; das Manifest ordnet Daten, Einstellungen und Programmstand zu. Codex unterstützte wesentlich die Integration der vorgegebenen Bausteine und die Erstellung von Tests mit künstlichen Daten; finanzwissenschaftliche Vorgaben und Untersuchungsentscheidungen stammen von mir (@sec-technik-5-9).

Feste Daten und Parameter werden vorab gewählt, nicht nachträglich für gewünschte Resultate verändert [@hilpischPythonFinanceMastering2019, S. 697; @kommerSouveraenInvestierenMit2025, S. 607–608].
````


### 28. Analyse – Zelle `762a3ac1`

Datei: `notebooks/Analyse.ipynb`. **81→54; Ersparnis 27.**

Begründung: Wiederholte Trennung von Engine/Eigenentscheidungen und Vorabfestlegung aus 5.1/4.1 verkürzt.

Erhalt/Abgleich: Engine/Tag/Prüfung, eigene Auswahl und Quellenrolle, Frage, vier Kennzahlen und alle Originalbelege.

**Vorher:**

````markdown
Für die Untersuchung ist Engine 1.0.0 mit dem Git-Tag engine-v1.0 vorgesehen; ihre technischen Prüfungen sind dokumentiert. Ich trenne den Berechnungsablauf von meinen eigenen Entscheidungen über Daten und Parameter. Die Quellen begründen die Konzepte, schreiben aber nicht genau diese Ticker, Zeiträume oder Einstellungen vor.

Zur Forschungsfrage aus Abschnitt 2.2 vergleiche ich Rendite, Volatilität, Sharpe Ratio und maximalen Drawdown, die unterschiedliche Aspekte erfassen [@kommerSouveraenInvestierenMit2025, Abschnitt 2.2]. Die Hauptparameter werden vor der Auswertung festgelegt, um eine nachträgliche Suche nach günstigen Ergebnissen zu vermeiden [@kommerSouveraenInvestierenMit2025, Glossar «Data Snooping»; @hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization»].
````

**Nachher:**

````markdown
Vorgesehen ist Engine 1.0.0 (Git-Tag engine-v1.0) mit dokumentierten Prüfungen. Daten und Parameter wähle ich; die Quellen begründen Konzepte, nicht genau diese Ticker, Zeiträume oder Einstellungen.

Zur Forschungsfrage in Abschnitt 2.2 beurteile ich unterschiedliche Aspekte mit Rendite, Volatilität, Sharpe und MDD [@kommerSouveraenInvestierenMit2025, Abschnitt 2.2]. Hauptparameter stehen vorab fest, statt günstige Ergebnisse nachträglich zu suchen [@kommerSouveraenInvestierenMit2025, Glossar «Data Snooping»; @hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization»].
````


### 29. Analyse – Zelle `c24d259b`

Datei: `notebooks/Analyse.ipynb`. **46→23; Ersparnis 23.**

Begründung: ETF-Begründung wiederholt Theorie/Einleitung und benennt mehrfach dieselbe Stellvertreterrolle.

Erhalt/Abgleich: Breite Positionen statt Einzeltitel, Proxycharakter und ETF≠kostenfreier Index.

**Vorher:**

````markdown
<p>Für die praktische Umsetzung verwende ich historische ETF-Reihen statt einzelner ausgewählter Unternehmen. Dadurch untersuche ich breit angelegte Markt- beziehungsweise Länderpositionen. Die ETFs sind dabei Stellvertreter für die jeweiligen Anlagebereiche. Ein ETF ist nicht dasselbe wie ein kostenfreier theoretischer Index. Diese Unterscheidung bleibt bei der Interpretation wichtig.</p>
````

**Nachher:**

````markdown
<p>Historische ETF-Reihen vertreten breite Markt- und Länderpositionen statt ausgewählter Einzelunternehmen. Diese Proxys sind keine kostenfreien theoretischen Indizes; das bleibt für die Interpretation wichtig.</p>
````


### 30. Analyse – Zelle `e433fc51`

Datei: `notebooks/Analyse.ipynb`. **37→24; Ersparnis 13.**

Begründung: Länderaufzählung steht vollständig in unmittelbar folgender Tabelle und Methodik 4.2.4.

Erhalt/Abgleich: Alle sieben Länder bleiben in Tabelle/Methodik; begrenztes Universum und Abdeckung versus Produktnachweis.

**Vorher:**

````markdown
<p>Die Länderstrategie ist auf USA, Kanada, Japan, Vereinigtes Königreich, Deutschland, Frankreich und Italien begrenzt und bildet nicht die ganze Weltwirtschaft ab. Die geplante Abdeckung muss anhand der Daten geprüft werden; Produktseiten beweisen keinen vollständigen oder richtigen Download.</p>
````

**Nachher:**

````markdown
<p>Die sieben Länder aus der folgenden Tabelle bilden nicht die Weltwirtschaft ab. Tatsächliche Datenabdeckung ist zu prüfen; Produktseiten beweisen keinen vollständigen oder richtigen Download.</p>
````


### 31. Analyse – Zelle `3873238c`

Datei: `notebooks/Analyse.ipynb`. **33→23; Ersparnis 10.**

Begründung: Gleiche Quellen-/Proxygrenzen knapper verbunden, keine Fondsrolle geändert.

Erhalt/Abgleich: US/USD, zwei Kennungstypen, verschiedene Konstruktionen und historische Änderungen.

**Vorher:**

````markdown
Ich verwende US-notierte USD-Linien und dokumentiere Modellrolle und Anbietersymbol getrennt. Länderfonds unterscheiden sich in Indexabgrenzungen und Begrenzungsregeln; sie vertreten daher nicht sämtliche Unternehmen nach derselben Methode. Historische Produkt-/Benchmarkänderungen bleiben Teil des Datennachweises.
````

**Nachher:**

````markdown
US-notierte USD-Linien werden mit getrennter Modellrolle und Anbietersymbol dokumentiert. Unterschiedliche Indexabgrenzungen und Begrenzungsregeln bilden Unternehmen nicht einheitlich ab; historische Produkt-/Benchmarkänderungen bleiben dokumentiert.
````


### 32. Analyse – Zelle `406de6ae`

Datei: `notebooks/Analyse.ipynb`. **45→25; Ersparnis 20.**

Begründung: Doppelte Beschreibung gleicher Bausteine und zweimal dieselbe Abgrenzungsfrage gestrichen.

Erhalt/Abgleich: Identische Fonds, jährliche gleiche Anteile 1/7, bestehende Strategie, Gewichtungskontrolle und Ausschluss Marktkapitalisierung.

**Vorher:**

````markdown
<p>K1 vergleicht BIP-Gewichtung mit jährlich je 1/7 derselben sieben Länder-ETFs. Die Gleichgewichtung ist eine zusätzliche Konfiguration der bestehenden Rebalancing-Strategie, keine neue Engine-Strategie. Die Bausteine bleiben gleich; variiert wird die Gewichtung. Sie ist <strong>keine Marktkapitalisierungsgewichtung</strong>: K1 prüft «BIP oder gleiche Länderanteile?», nicht «BIP oder Marktkapitalisierung?».</p>
````

**Nachher:**

````markdown
<p>K1 variiert BIP versus jährlich je 1/7 derselben sieben Länder-ETFs. Gleichgewichtung ist eine Konfiguration der bestehenden Rebalancing-Strategie, keine neue Engine-Strategie. Untersucht wird <strong>keine Marktkapitalisierungsgewichtung</strong>.</p>
````


### 33. Analyse – Zelle `c72a0269`

Datei: `notebooks/Analyse.ipynb`. **44→36; Ersparnis 8.**

Begründung: Doppelte Nichtverlängerung in 5.5.5 gebündelt; sämtliche Zeit-/Modellparameter bleiben.

Erhalt/Abgleich: Alle Strategien/Zeitpunkte/Periodenzahl, getrennte Stichprobe und keine rückwirkende Weltmarktverlängerung.

**Vorher:**

````markdown
<p>Z1 vergleicht VTI Buy-and-Hold, VTI/IEF 60/40 und VTI-Trend von Januar 2003 bis Dezember 2025: Anfangsbewertung Ende Dezember 2002, 276 Monatsrenditen. Es bleibt eine getrennte längere US-Stichprobe. VT wird weder rückwirkend mit einer anderen Reihe verlängert noch mit Z1 zu einer Weltmarktgeschichte verbunden.</p>
````

**Nachher:**

````markdown
<p>Z1 vergleicht VTI Buy-and-Hold, VTI/IEF 60/40 und VTI-Trend von Januar 2003 bis Dezember 2025: Anfangsbewertung Ende Dezember 2002, 276 Monatsrenditen. Diese getrennte längere US-Stichprobe verlängert VT weder durch andere Reihen noch zu einer Weltmarktgeschichte.</p>
````


### 34. Analyse – Zelle `8c5b7b44`

Datei: `notebooks/Analyse.ipynb`. **76→45; Ersparnis 31.**

Begründung: Währungs-/Nettoabgrenzung und Anfangskapital wiederholen Methodik und 5.5.6; vollständig gebündelt.

Erhalt/Abgleich: 100’000, keine Zahlungsströme, Proportionalität ohne feste Kosten, nominal/USD, Inflation/CHF, fehlende Absicherung, keine persönliche Nettorendite.

**Vorher:**

````markdown
<p>Jeder Lauf startet mit 100’000 USD und enthält keine weiteren Einzahlungen oder Entnahmen. Der Betrag macht die Ergebnisse anschaulich; bei den hier verwendeten proportionalen Portfolios ohne feste Handelskosten beeinflusst er nicht die prozentuale Strategierendite. Alle Ergebnisse werden nominal in USD betrachtet. Es findet weder eine Inflationsbereinigung noch eine Umrechnung in Schweizer Franken statt. USD-Notierung allein bedeutet zudem keine Absicherung der im Fonds enthaltenen Fremdwährungsrisiken. Die Untersuchung stellt somit nicht die persönliche Nettorendite eines Schweizer Anlegers dar.</p>
````

**Nachher:**

````markdown
<p>Jeder Lauf startet mit 100’000 USD ohne weitere Ein- oder Auszahlungen. Bei proportionalen Portfolios ohne feste Handelskosten ist der anschauliche Betrag für die prozentuale Rendite unerheblich. Ergebnisse sind nominale USD-Werte ohne Inflationsbereinigung oder CHF-Umrechnung. USD-Notierung sichert Fonds-Fremdwährungsrisiken nicht ab; dies sind keine persönlichen Schweizer Nettorenditen.</p>
````


### 35. Analyse – Zelle `a0dcceaa`

Datei: `notebooks/Analyse.ipynb`. **42→20; Ersparnis 22.**

Begründung: Mehrfache Performance-/Ausgangsreihenbeschreibung aus 4.3 konzentriert; gleiche Begründung/Belege.

Erhalt/Abgleich: Gesamtertrag/Ausschüttung, Kursindexgrenze, konkrete Ausgangsspalte, Anbieterbehauptung und beide Quellen.

**Vorher:**

````markdown
<p>Für die Performance benötige ich eine Reihe, die Ausschüttungen berücksichtigt. Ein reiner Kursindex genügt nicht, um den Gesamtertrag einer Aktienanlage darzustellen [@kommerSouveraenInvestierenMit2025, Abschnitt zu Wertpapierindizes]. Als Ausgangspunkt verwende ich die Spalte <code>Adj Close</code> von Yahoo Finance. Yahoo beschreibt diese als um Splits und Dividenden bereinigten Schlusskurs [@WhatAdjustedClose].</p>
````

**Nachher:**

````markdown
<p>Gesamtertrag verlangt Ausschüttungen; ein reiner Kursindex genügt nicht [@kommerSouveraenInvestierenMit2025, Abschnitt zu Wertpapierindizes]. Ich verwende Yahoos <code>Adj Close</code>, laut Anbieter um Splits und Dividenden bereinigt [@WhatAdjustedClose].</p>
````


### 36. Analyse – Zelle `31fc788f`

Datei: `notebooks/Analyse.ipynb`. **53→32; Ersparnis 21.**

Begründung: Hauptparameterbeschreibung wiederholt 4.2.3; eigene Begründung und Frequenzabgrenzung bleiben.

Erhalt/Abgleich: Drei/zwölf, kurz/lang aus 4.2.3, Quartal/Jahr, eigene Wahl, nicht optimal/quellenübernommen, alle drei Frequenzangaben.

**Vorher:**

````markdown
<p>Die Hauptvariante verwendet einen kurzen SMA über drei Monatsbeobachtungen und einen langen SMA über zwölf Monatsbeobachtungen. Damit vergleiche ich eine ungefähr quartalsbezogene mit einer jahresbezogenen Entwicklung. Diese Werte sind eine eigene einfache Festlegung, keine aus einer Quelle übernommene optimale Kombination. Ein 12-Monats-SMA darf nicht als 12-Tage-SMA oder als exakt gleichwertiger 200-Tage-SMA beschrieben werden.</p>
````

**Nachher:**

````markdown
<p>Ich lege den kurzen SMA über drei, den langen über zwölf Monatsbeobachtungen fest: ungefähr quartals- und jahresbezogen, keine quellenbasierte optimale Kombination. Ein 12-Monats-SMA ist weder ein 12-Tage-SMA noch einem 200-Tage-SMA exakt gleichwertig.</p>
````


### 37. Analyse – Zelle `d4298767`

Datei: `notebooks/Analyse.ipynb`. **22→13; Ersparnis 9.**

Begründung: Vorab festgelegte Sensitivitätsvarianten und Verbot historischer Siegerersetzung sind mehrfach erläutert: 4.2.3, 5.2.3 und vollständig in 5.5.5.

Erhalt/Abgleich: Alle drei Parameterwerte, Hauptvariante und Bericht beider Zusatzvarianten; ausdrückliche Nicht-Siegerersetzung und begrenzter Prüfcharakter bleiben in unverändertem 4001dccf.

**Vorher:**

````markdown
<p>2/12 und 6/12 ergänzen die Sensitivitätsbetrachtung. Alle Varianten werden berichtet; 3/12 wird nicht nachträglich durch den historischen Sieger ersetzt.</p>
````

**Nachher:**

````markdown
<p>3/12 bleibt Hauptvariante; 2/12 und 6/12 werden als Sensitivitätsvarianten berichtet.</p>
````


### 38. Analyse – Zelle `6f8b54af`

Datei: `notebooks/Analyse.ipynb`. **54→29; Ersparnis 25.**

Begründung: Zwei gleichartige Sätze zum damaligen Datenstand und wiederholter Quellenname zusammengeführt.

Erhalt/Abgleich: Damals verfügbare Vintage, archivierte Herbst-WEO/IMF, historische Werte versus Schätzung/Prognose, Revisionen; folgende vier Verfügbarkeits-/Berechnungszellen bleiben vollständig unverändert.

**Vorher:**

````markdown
<p>Für die Länderstrategie reicht eine heutige Tabelle historischer BIP-Werte nicht aus. Benötigt werden Datenstände, die zum damaligen Entscheidungszeitpunkt verfügbar waren. Dazu verwende ich als zusätzliche Datenquelle die archivierten Herbst-Ausgaben der IMF-Datenbank <i>World Economic Outlook</i> (WEO). Der IMF erläutert, dass historische Werte revidiert werden können und dass seine Tabellen historische Angaben, Schätzungen und Prognosen enthalten [@WorldEconomicOutlooka].</p>
````

**Nachher:**

````markdown
<p>Heutige historische BIP-Tabellen reichen wegen Revisionen nicht: Für damalige Entscheide verwende ich die archivierten IMF-WEO-Herbstausgaben. Der IMF unterscheidet historische Angaben, Schätzungen und Prognosen und weist auf mögliche Revisionen hin [@WorldEconomicOutlooka].</p>
````


### 39. Analyse – Zelle `2d5c11d2`

Datei: `notebooks/Analyse.ipynb`. **58→42; Ersparnis 16.**

Begründung: Ausführliche identische H1/K1-Resultat- und Vorlaufabgrenzung gebündelt.

Erhalt/Abgleich: Fünf/elf, beide identischen BIP-Reihen, sechs Monatswerte/Jan–Juni2002/nichtgemeinsamer IEF-Stand, Signalhistorie und unveränderter eigentlicher Beginn.

**Vorher:**

````markdown
<p>Die fünf Läufe erzeugten elf Strategie-Zeitreihen. Die BIP-Strategie ist dabei sowohl in H1 als auch in K1 enthalten; ihre beiden Verläufe sind zahlenmässig identisch. Bei Z1 werden sechs VTI-Monatswerte aus Januar bis Juni 2002 als nicht gemeinsam mit IEF ausgewiesen. Sie bleiben für die separate Signalhistorie erhalten. Der eigentliche Untersuchungszeitraum ab Ende Dezember 2002 wurde dadurch nicht verkürzt.</p>
````

**Nachher:**

````markdown
<p>Die fünf Läufe ergeben elf Strategie-Zeitreihen; BIP verläuft in H1 und K1 identisch. In Z1 werden sechs VTI-Monatswerte Januar–Juni 2002 als nicht gemeinsam mit IEF ausgewiesen; sie bleiben in der separaten Signalhistorie. Der Untersuchungszeitraum ab Ende Dezember 2002 ist nicht verkürzt.</p>
````


### 40. Analyse – Zelle `b0ea1a50`

Datei: `notebooks/Analyse.ipynb`. **48→39; Ersparnis 9.**

Begründung: Identische Monats-MDD-Grenze steht vollständig in 5.2.4 und 5.5.6; reine Wiederholung zwischen Definition und Rundung.

Erhalt/Abgleich: Annualisierung, p.a.-Bedeutung, negative Höchststandsverluste/näher-null und ungerundete Berechnung bleiben wörtlich; Monatsgrenze weiterhin in diesem Kapitel.

**Vorher:**

````markdown
<p>Volatilität und Sharpe werden ebenfalls annualisiert ausgewiesen; «p. a.» bedeutet «pro Jahr». Der negative Drawdown misst den Rückgang vom bisherigen Höchststand. Ein Wert näher bei null bedeutet einen geringeren maximalen Verlust. Die Monatsbewertungen erfassen keine vollständigen Verluste innerhalb eines Monats. Tabellenwerte sind gerundet; berechnet wurde mit ungerundeten Ergebnissen.</p>
````

**Nachher:**

````markdown
<p>Volatilität und Sharpe werden ebenfalls annualisiert ausgewiesen; «p. a.» bedeutet «pro Jahr». Der negative Drawdown misst den Rückgang vom bisherigen Höchststand. Ein Wert näher bei null bedeutet einen geringeren maximalen Verlust. Tabellenwerte sind gerundet; berechnet wurde mit ungerundeten Ergebnissen.</p>
````


### 41. Analyse – Zelle `6402a9d2`

Datei: `notebooks/Analyse.ipynb`. **20→15; Ersparnis 5.**

Begründung: Interpretationseingang bündelt wiederholten Bezug auf eigene gespeicherte Ergebnisse.

Erhalt/Abgleich: Eigene Interpretation, alle drei Nachweise und begrenzte Funktion der Jahresbeispiele.

**Vorher:**

````markdown
<p>Ich interpretiere die Ergebnisse anhand der gespeicherten Verläufe, Gewichte und Signale. Jahresbeispiele erläutern die Funktionsweise; sie ersetzen den Gesamtvergleich nicht.</p>
````

**Nachher:**

````markdown
<p>Ich interpretiere gespeicherte Verläufe, Gewichte und Signale. Jahresbeispiele erläutern Mechanismen, ersetzen aber den Gesamtvergleich nicht.</p>
````


### 42. Analyse – Zelle `6999a6d3`

Datei: `notebooks/Analyse.ipynb`. **49→35; Ersparnis 14.**

Begründung: Bereits beschriebene H1-Rangfolge auf den Rendite-Risiko-Zielkonflikt konzentriert.

Erhalt/Abgleich: Persönlicher Satz zur weniger eindeutigen Beurteilung wörtlich; beide Ertragssieger, geringerer 60/40-Ertrag und alle drei Risikovergleiche.

**Vorher:**

````markdown
<p>Im Hauptlauf hätte eine ausschliessliche Betrachtung des Endvermögens für BIP-G7 oder VT Buy-and-Hold gesprochen. Sobald ich die Schwankungen und Rückgänge einbeziehe, wird das Bild weniger eindeutig. Das 60/40-Portfolio gibt einen Teil des Ertrags auf, erreicht aber bei allen drei ausgewiesenen Risikokennzahlen ein günstigeres Ergebnis als die anderen H1-Strategien.</p>
````

**Nachher:**

````markdown
<p>Das H1-Endvermögen spräche für BIP-G7 oder VT Buy-and-Hold. Sobald ich die Schwankungen und Rückgänge einbeziehe, wird das Bild weniger eindeutig. 60/40 erreicht bei geringerem Ertrag günstigere Werte aller drei Risikokennzahlen als die übrigen H1-Strategien.</p>
````


### 43. Analyse – Zelle `2b837f9a`

Datei: `notebooks/Analyse.ipynb`. **30→18; Ersparnis 12.**

Begründung: Dritter Satz wiederholt die unveränderten ersten beiden und den expliziten Vergleich in 5.4.1.

Erhalt/Abgleich: Erste beiden Sätze wörtlich: H1-Volatilität/MDD-Kontrast und mögliche Schwankungssenkung mit verbleibenden Verlusten; Verlustschutz-Fazit in 5.4.1.

**Vorher:**

````markdown
<p>Trend zeigt niedrigere H1-Volatilität, aber grösseren MDD als VT. Cash-Monate können die Schwankung senken, während Verluste bestehen bleiben. «Schwankt weniger» bedeutet daher nicht automatisch «schützt besser vor dem grössten Verlust».</p>
````

**Nachher:**

````markdown
<p>Trend zeigt niedrigere H1-Volatilität, aber grösseren MDD als VT. Cash-Monate können die Schwankung senken, während Verluste bestehen bleiben.</p>
````


### 44. Analyse – Zelle `c48ec4c3`

Datei: `notebooks/Analyse.ipynb`. **41→24; Ersparnis 17.**

Begründung: 60/40-Definition und Kalenderregel schon 4.2.2/5.2.3 erklärt; hier Funktion vor unverändertem Zahlenbeispiel.

Erhalt/Abgleich: 40 % IEF, jährliche Rücksetzung, Driftmechanismus; 60 %/Folgeperiode/kein Abschlusstrade vollständig in 4.2.2.

**Vorher:**

````markdown
<p>Das 60/40-Portfolio besteht nicht nur aus Aktien, sondern zu 40 % aus dem Staatsanleihen-ETF IEF. Am Jahresende wird die ursprüngliche Verteilung wiederhergestellt. So verhindert die Regel, dass die besser gelaufene Anlage den Anteil der anderen über die Jahre immer weiter verdrängt.</p>
````

**Nachher:**

````markdown
<p>40 % IEF und jährliche Wiederherstellung der Aktien-/Anleihenanteile verhindern, dass die besser gelaufene Anlage die andere dauerhaft verdrängt (Regeln in Abschnitt 4.2.2).</p>
````


### 45. Analyse – Zelle `4b05781f`

Datei: `notebooks/Analyse.ipynb`. **36→27; Ersparnis 9.**

Begründung: Rebalancing-Kausalitätsgrenze bereits 4.2.2/5.5.2 erläutert; beide konkurrierenden Einflüsse bleiben.

Erhalt/Abgleich: IEF-Allokation, fehlender sonst identischer Kontrolllauf, keine Alleinkausalität und Scope 60/40 mit jährlichem Rebalancing.

**Vorher:**

````markdown
<p>Die geringere Schwankung darf nicht Rebalancing allein zugeschrieben werden: Zugleich verändert IEF die Allokation. Ein identisches 60/40-Portfolio ohne Umschichtungen fehlt als Kontrolllauf. Die Aussage gilt daher für das gesamte Konzept «60/40 mit jährlichem Rebalancing».</p>
````

**Nachher:**

````markdown
<p>IEF verändert zugleich die Allokation. Ohne Kontrolllauf desselben 60/40-Portfolios ohne Umschichtungen lässt sich die geringere Schwankung nicht Rebalancing allein zuschreiben; sie gilt für das gesamte Konzept.</p>
````


### 46. Analyse – Zelle `3425064c`

Datei: `notebooks/Analyse.ipynb`. **36→18; Ersparnis 18.**

Begründung: Bereits erklärte nachlaufende Kursreaktion aus 3.2.6 und 5.2.6 auf beobachtetes Beispiel konzentriert.

Erhalt/Abgleich: Keine Voraussicht über Fortgang/Erholung, H1/2020 und folgende vollständig erhaltene Tabelle/Verzögerungsdeutung.

**Vorher:**

````markdown
<p>Die Trendregel reagiert auf die bereits beobachtete Entwicklung. Sie weiss nicht im Voraus, ob ein Rückgang weitergeht oder ob sich der Markt schnell erholt. Besonders verständlich wird das an den H1-Signalen im Frühjahr und Sommer 2020.</p>
````

**Nachher:**

````markdown
<p>Die nachlaufende Trendregel kennt Fortgang oder schnelle Erholung nicht. Das zeigen die H1-Signale im Frühjahr und Sommer 2020.</p>
````


### 47. Analyse – Zelle `3df49dc6`

Datei: `notebooks/Analyse.ipynb`. **81→42; Ersparnis 39.**

Begründung: Mehrere Vor-/Nachsätze wiederholen US-Ergebnisrangfolge; Mechanismus mit allen Zeitpunkten/Zahlen behalten.

Erhalt/Abgleich: Mindestens Juni2009, grosser Teil nicht ganze Krise, beide Rückgangsgrenzen, 22,14/50,84 und begrenzte Rangfolge.

**Vorher:**

````markdown
<p>Im längeren US-Lauf zeigt sich eine andere Seite derselben Regel. Dort liegt die Trendstrategie von Februar 2008 bis mindestens Juni 2009 in Cash. Sie ist damit während eines grossen Teils des in Z1 beobachteten Rückgangs von Oktober 2007 bis Februar 2009 nicht investiert. Ihr maximaler Drawdown über den gesamten US-Lauf beträgt 22,14 % statt 50,84 % bei Buy-and-Hold. Dass der grösste Rückgang kleiner ist, bedeutet aber auch hier nicht, dass die Trendfolge das höchste Endvermögen oder die höchste Sharpe Ratio erreicht.</p>
````

**Nachher:**

````markdown
<p>In Z1 bleibt Trend von Februar 2008 bis mindestens Juni 2009 in Cash: über einen grossen Teil des Rückgangs Oktober 2007 bis Februar 2009. Ihr Gesamt-MDD beträgt 22,14 % statt 50,84 % bei Buy-and-Hold, ohne höchstes Endvermögen oder höchste Sharpe zu erreichen.</p>
````


### 48. Analyse – Zelle `ab95d9b8`

Datei: `notebooks/Analyse.ipynb`. **15→6; Ersparnis 9.**

Begründung: Definition desselben Fondsuniversums und jährlicher Gewichtung steht bereits vollständig in 5.2.3 und Tabellenquelle.

Erhalt/Abgleich: US-Gewichtungsunterschied als Einleitung zur folgenden unveränderten Tabelle; K1-Kontrast in 5.2.3/Tabellenquelle.

**Vorher:**

````markdown
<p>K1 vergleicht dieselben Fonds unter BIP- und jährlicher Gleichgewichtung. Die Gewichtsdaten zeigen besonders unterschiedliche US-Anteile.</p>
````

**Nachher:**

````markdown
<p>Die K1-Gewichte zeigen besonders unterschiedliche US-Anteile.</p>
````


### 49. Analyse – Zelle `53354686`

Datei: `notebooks/Analyse.ipynb`. **65→39; Ersparnis 26.**

Begründung: Gleiche vorsichtige Kausalaussage wurde in mehreren Sätzen wiederholt.

Erhalt/Abgleich: Stichprobenbezug, Erklärungsansatz statt Alleinkausalität, keine vollständige Attribution, variable Gewichte/Rebalancing/Reihenfolge und eigenes Urteil.

**Vorher:**

````markdown
<p>Die stärkere Gewichtung des in dieser Stichprobe besser gelaufenen US-Proxys macht den Vorsprung des BIP-Portfolios gegenüber der Gleichgewichtung nachvollziehbar. Damit ist aber noch nicht der gesamte Mehrertrag rechnerisch auf einzelne Länder zerlegt. Die Gewichte verändern sich, und auch die jährlichen Umschichtungen und die Reihenfolge der Renditen wirken auf das Ergebnis. Ich behandle den US-Anteil deshalb als wichtigen Erklärungsansatz und nicht als vollständig nachgewiesene alleinige Ursache.</p>
````

**Nachher:**

````markdown
<p>Der stärkere Anteil des hier erfolgreicheren US-Proxys erklärt den BIP-Vorsprung gegenüber Gleichgewichtung mit, ist aber keine vollständige Länderzerlegung des Mehrertrags. Wechselnde Gewichte, jährliche Umschichtungen und Renditereihenfolge wirken ebenfalls. Ich behandle ihn als wichtigen Erklärungsansatz, nicht als nachgewiesene alleinige Ursache.</p>
````


### 50. Analyse – Zelle `bc770851`

Datei: `notebooks/Analyse.ipynb`. **53→31; Ersparnis 22.**

Begründung: Teilperiodentabelle bereits 5.4.5 beschrieben; hier knappe Begründung der zeitabhängigen Bewertung.

Erhalt/Abgleich: Alle Jahre/vier Kennzahlenwerte, Jahresbasis und Endwertgrenze; keine Gleichsetzung mit anderen Universen.

**Vorher:**

````markdown
<p>Die beiden H1-Teilzeiträume zeigen, dass selbst innerhalb derselben Untersuchung nicht jede Regel durchgehend gleich gut abschneidet. Die 60/40-Sharpe liegt in 2010–2017 bei 1,038, in 2018–2025 dagegen bei 0,452. Zugleich verbessert sich die annualisierte Trendrendite von 4,57 % auf 7,91 %. Solche Unterschiede würden in einem einzelnen Endwert untergehen.</p>
````

**Nachher:**

````markdown
<p>Innerhalb H1 ändern sich Ergebnisse: 60/40-Sharpe 1,038 in 2010–2017 und 0,452 in 2018–2025; Trendrendite p. a. 4,57 % beziehungsweise 7,91 %. Ein Endwert verdeckt diese Teilperiodenunterschiede.</p>
````


### 51. Analyse – Zelle `dfc835b7`

Datei: `notebooks/Analyse.ipynb`. **36→23; Ersparnis 13.**

Begründung: Abgrenzung aus 5.2.3 wiederholt; hier kurz als Interpretationsgrenze.

Erhalt/Abgleich: Gleichzeitiger Markt-/Zeitwechsel, VTI/VT, kein isolierter Einfluss und keine globale Verlängerung.

**Vorher:**

````markdown
<p>Z1 verändert gegenüber H1 sowohl Zeitraum als auch Aktienmarkt (VTI statt VT). Unterschiede der Trendbewertung lassen sich deshalb nicht eindeutig auf Markt oder Zeitraum zurückführen. Es bleibt ein ergänzender längerer US-Lauf, keine Verlängerung des globalen Datensatzes.</p>
````

**Nachher:**

````markdown
<p>Z1 verändert zugleich Zeitraum und Markt (VTI statt VT); deren Einflüsse sind nicht trennbar. Der ergänzende längere US-Lauf verlängert den globalen Datensatz nicht.</p>
````


### 52. Analyse – Zelle `7012cb90`

Datei: `notebooks/Analyse.ipynb`. **51→27; Ersparnis 24.**

Begründung: Datenvalidierung-versus-Originalprovenienz-Abgrenzung wiederholt ausführlich 6.3/C.3; hier alle spezifischen Grenzen.

Erhalt/Abgleich: Prüfumfang, keine unabhängige Komplettrekonstruktion von Yahoo, Hash≠historische Publikation und fortbestehende Grenze.

**Vorher:**

````markdown
<p>Die Tests und Gegenrechnungen zeigen, dass die berechneten Ergebnisse zu den festgehaltenen Eingaben und Regeln passen. Sie beweisen nicht, dass jede historische Anpassung der Yahoo-Reihen unabhängig rekonstruiert wurde oder dass ein heutiger Hash den ursprünglichen Veröffentlichungszeitpunkt einer WEO-Datei beweist. Diese Grenzen der Datenherkunft bleiben auch nach einem technisch erfolgreichen Lauf bestehen.</p>
````

**Nachher:**

````markdown
<p>Tests und Gegenrechnungen bestätigen Ergebnisse gemäss Eingaben und Regeln, nicht jede unabhängig rekonstruierte Yahoo-Anpassung oder einen WEO-Veröffentlichungszeitpunkt aus heutigem Hash. Grenzen der Datenherkunft bleiben trotz technischer Erfolge.</p>
````


### 53. Analyse – Zelle `f4051b34`

Datei: `notebooks/Analyse.ipynb`. **60→40; Ersparnis 20.**

Begründung: Dreifach bereits präzisierte Monats-/Ausführungs-/RF-Grenzen zusammengeführt und rückverwiesen.

Erhalt/Abgleich: Monats-MDD gegenüber Tagesverlusten, idealisierte Schlussausführung, unverzinste Cash-Position und RF nur Vergleich; alle konkreten Regeln 5.2.4/6/7 unverändert.

**Vorher:**

````markdown
<p>Die monatliche Beobachtung vereinfacht den Vergleich, blendet aber Bewegungen innerhalb des Monats aus. Der ausgewiesene maximale Drawdown ist der grösste Rückgang zwischen den beobachteten Monatswerten und kann kleiner sein als ein mit Tagesdaten gemessener Rückgang. Auch die angenommene Ausführung zu Schlussbewertungen ist idealisiert. Das Cash-Modell verzichtet auf eine Verzinsung, während die RF-Reihe nur eine Vergleichsnäherung für die Sharpe Ratio liefert.</p>
````

**Nachher:**

````markdown
<p>Monatsbewertungen vereinfachen den Vergleich, übersehen aber innermonatliche Bewegungen: Ihr MDD kann kleiner als der aus Tagesdaten sein. Ausführung zu Schlussbewertungen ist idealisiert. Cash bleibt unverzinst; RF ist nur Sharpe-Vergleichsnäherung (Abschnitte 5.2.4, 5.2.6 und 5.2.7).</p>
````


### 54. Analyse – Zelle `a3e4beef`

Datei: `notebooks/Analyse.ipynb`. **37→26; Ersparnis 11.**

Begründung: Ergebnisüberleitung wiederholt drei unmittelbar erläuterte Einflussbereiche.

Erhalt/Abgleich: Alle drei Einflussarten, Nachvollziehbarkeit und begrenzte Fazitreflexion.

**Vorher:**

````markdown
<p>Die Rangfolgen ändern sich mit Kennzahl, Datensatz und teilweise bereits mit kleinen Parameteränderungen. Gewichte und Signale helfen, die Unterschiede nachzuvollziehen. Kapitel 6 führt diese Beobachtungen zur Forschungsfrage zusammen und enthält die abschliessende Reflexion innerhalb der untersuchten Aussagegrenzen.</p>
````

**Nachher:**

````markdown
<p>Kennzahl, Datensatz und kleine Parameteränderungen verändern Rangfolgen; Gewichte und Signale machen dies nachvollziehbar. Kapitel 6 verbindet die Beobachtungen mit Forschungsfrage und abschliessender Reflexion innerhalb dieser Grenzen.</p>
````


### 55. Fazit – Zelle `53c9f636`

Datei: `notebooks/Fazit.ipynb`. **57→32; Ersparnis 25.**

Begründung: Wiederholung der Prüf-/Gültigkeitsgrenze aus 5.5.6/C.3 gebündelt, keine persönliche Schlussfolgerung umgeschrieben.

Erhalt/Abgleich: Fonds/Zeitraum/Regeln, innerhalb Prüfumfang, keine Zukunftsfreigabe, Originaldatenqualität und Modellrealität getrennt.

**Vorher:**

````markdown
<p>Die Ergebnisse gelten für die ausgewählten Fonds, Zeiträume und Regeln. Auch die bestandenen Tests und Gegenrechnungen machen daraus keinen Beweis für eine künftige Überlegenheit. Sie zeigen innerhalb ihres Prüfumfangs, dass die Berechnungen zu den festgehaltenen Eingaben passen. Ob die ursprünglichen Finanzdaten vollständig richtig sind und wie gut die vereinfachten Annahmen die Wirklichkeit abbilden, ist davon zu unterscheiden.</p>
````

**Nachher:**

````markdown
<p>Für die gewählten Fonds, Zeiträume und Regeln bestätigen Tests und Gegenrechnungen innerhalb ihres Prüfumfangs nur die Berechnung aus festgehaltenen Eingaben. Sie beweisen weder künftige Überlegenheit noch vollständig richtige Originaldaten oder realistische Modellannahmen.</p>
````


**STOPP zur Autorenkontrolle.** Keine weitere Kürzung und keine Phase-2-Fachkorrektur ausgeführt.
