# Sachliche Überarbeitung persönlicher Formulierungen – 14. Oktober 2026

**Status:** Stilkorrektur umgesetzt; persönliche Endkontrolle des Autors ausstehend. Kein Staging, Commit oder Push.

## 1. Eingangslage und Auftrag

- Repository: `Maturarbeit_Riccardo_Ambuehl_2027`, Remote `https://github.com/riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027.git`; tatsächlicher Branch `dev`, HEAD `97045c6af65806145fc30117af5becc134ba93ae`. Der im Auftrag genannte historische HEAD stimmt mit dem tatsächlichen Ausgangsstand überein.
- Git-Ausgangsstatus: sauber; keine offenen oder kollidierenden Änderungen. Keine AGENTS.md im Hauptrepository oder seinen Vorfahren gefunden.
- Anlass: Rückmeldung der Betreuungsperson Herrn Mock vom 14.10.2026. Persönliche Autorenperspektive in wissenschaftlicher redaktioneller Prosa sachlich formulieren; Forschungsfrage, Inhalte und Anhangsumfang bewahren.
- Vollständiger tatsächlicher [Originalauftrag](ai-usage/prompts/2026-10-14-ich-formulierungen-wissenschaftlicher-stil.txt) bytegleich aus der genannten Download-Datei archiviert. SHA-256 `50cfa15ceb4f65b81e60a275cf962c044e8a3a8a25cae8ded5678c9ad24ac861`. Die direkte Nutzeranweisung erteilt die Freigabe für die stilistischen Anpassungen und den KI-Dokumentationsabgleich.
- Vorabgesicherte Dateien: 182 Hauptprojektdateien, einschliesslich ignorierter Render-/Freeze-/Cachedateien und vorhandener PDFs; alle Sicherungskopien hashbestätigt. Zusätzlich 317 Dateien des Engine-Ordners lesend gehasht. Arbeits- und Prüfhilfen ausschliesslich extern unter `C:\Users\modic\AppData\Local\Temp\codex-ich-stil-2026-10-14-epzmds7u`.
- Zielbereich: neun in `_quarto.yml` eingebundene Notebooks sowie `ki-nutzung.qmd`. README, historische Archive, Originalprompts und alte Logs werden nicht stilistisch verändert. `backtest-service` wurde weder betreten noch geprüft oder verändert.

## 2. Vollständiges Fundstelleninventar

Die Ausgangssuche erfasste «ich», «mich», «mir», alle geforderten Formen von «mein» und «unser» sowie «wir» und «uns», unabhängig von Gross-/Kleinschreibung, in den Markdown-Quellen. Alle Treffer wurden im Kontext gelesen.

| Einordnung | Fundstellen | Wortvorkommen | Ergebnis |
|---|---:|---:|---|
| Redaktionelle Autorenperspektive | 50 Markdown-Zellen | 72 | Durch 70 konkrete Umformulierungen ersetzt; ein wiederholter Ausdruck wird in einem Protokolleintrag zweimal berücksichtigt. |
| Historischer Originalstand | 4 Markdown-Zellen in Anhang A | 19 | Unverändert, ausdrücklich als historischer Original-Arbeitsnachweis markiert. |
| Zitierter ChatGPT-Ausdruck | 1 QMD-Abschnitt | 1 | «wir» bleibt als Bezeichnung der originalen ChatGPT-Ausdrucksweise erhalten. |
| Fachlich unklar / offene Einzelentscheidung | 0 | 0 | Keine Stelle wegen einer nicht bedeutungserhaltend möglichen Stiländerung offen. |
| **Gesamt** | **55 Fundstellen** | **92** | **20 bewusst unveränderte Vorkommen, keine verbliebene redaktionelle Ich-/Wir-Perspektive.** |

### 2.1 Geänderte Fundstellen

Zell-IDs sind die stabilen Notebook-Fundstellen. Die einzelnen tatsächlichen Textänderungen stehen vollständig in Abschnitt 3.

| Datei | Zell-ID / Index (0-basiert) | Gefundene persönliche Wörter |
|---|---|---|
| [index.ipynb](../index.ipynb) | `bfc2fb04` / 2 | Ich |
| [index.ipynb](../index.ipynb) | `af2cc3a8` / 6 | ich, meinen |
| [notebooks/Einleitung.ipynb](../notebooks/Einleitung.ipynb) | `686a445a` / 3 | Mich |
| [notebooks/Einleitung.ipynb](../notebooks/Einleitung.ipynb) | `46680b47` / 4 | mich, Ich |
| [notebooks/Einleitung.ipynb](../notebooks/Einleitung.ipynb) | `a9f0792b` / 8 | ich |
| [notebooks/Einleitung.ipynb](../notebooks/Einleitung.ipynb) | `f733daa1` / 9 | ich |
| [notebooks/Einleitung.ipynb](../notebooks/Einleitung.ipynb) | `4d7593b1` / 12 | Ich |
| [notebooks/Einleitung.ipynb](../notebooks/Einleitung.ipynb) | `a7ae04cd` / 14 | Mir |
| [notebooks/Einleitung.ipynb](../notebooks/Einleitung.ipynb) | `4a72f361` / 16 | ich |
| [notebooks/Theorie.ipynb](../notebooks/Theorie.ipynb) | `1941d2df` / 2 | meine, meine |
| [notebooks/Theorie.ipynb](../notebooks/Theorie.ipynb) | `bdef1563` / 13 | mein, ich |
| [notebooks/Theorie.ipynb](../notebooks/Theorie.ipynb) | `005fce46` / 28 | meinen, meinen |
| [notebooks/Theorie.ipynb](../notebooks/Theorie.ipynb) | `d512a002` / 74 | Ich |
| [notebooks/Methodik.ipynb](../notebooks/Methodik.ipynb) | `a233bc87` / 2 | Ich, ich, ich |
| [notebooks/Methodik.ipynb](../notebooks/Methodik.ipynb) | `35c815dc` / 3 | ich |
| [notebooks/Methodik.ipynb](../notebooks/Methodik.ipynb) | `18279f6c` / 15 | meine, ich |
| [notebooks/Methodik.ipynb](../notebooks/Methodik.ipynb) | `2565f88a` / 16 | Ich |
| [notebooks/Methodik.ipynb](../notebooks/Methodik.ipynb) | `60c85505` / 22 | ich |
| [notebooks/Methodik.ipynb](../notebooks/Methodik.ipynb) | `a6b32280` / 26 | ich, ich, ich |
| [notebooks/Analyse.ipynb](../notebooks/Analyse.ipynb) | `c50744c1` / 2 | meine, mir |
| [notebooks/Analyse.ipynb](../notebooks/Analyse.ipynb) | `762a3ac1` / 4 | ich, ich |
| [notebooks/Analyse.ipynb](../notebooks/Analyse.ipynb) | `7b9386c9` / 13 | ich |
| [notebooks/Analyse.ipynb](../notebooks/Analyse.ipynb) | `663b04db` / 15 | unser |
| [notebooks/Analyse.ipynb](../notebooks/Analyse.ipynb) | `efe3b129` / 21 | ich |
| [notebooks/Analyse.ipynb](../notebooks/Analyse.ipynb) | `a0dcceaa` / 25 | Ich |
| [notebooks/Analyse.ipynb](../notebooks/Analyse.ipynb) | `31fc788f` / 29 | Ich |
| [notebooks/Analyse.ipynb](../notebooks/Analyse.ipynb) | `e3ace74b` / 34 | ich |
| [notebooks/Analyse.ipynb](../notebooks/Analyse.ipynb) | `6f8b54af` / 39 | ich |
| [notebooks/Analyse.ipynb](../notebooks/Analyse.ipynb) | `8c8859cc` / 53 | ich |
| [notebooks/Analyse.ipynb](../notebooks/Analyse.ipynb) | `6402a9d2` / 107 | Ich |
| [notebooks/Analyse.ipynb](../notebooks/Analyse.ipynb) | `6999a6d3` / 109 | ich |
| [notebooks/Analyse.ipynb](../notebooks/Analyse.ipynb) | `53354686` / 133 | Ich |
| [notebooks/Fazit.ipynb](../notebooks/Fazit.ipynb) | `64f46030` / 5 | mich |
| [notebooks/Fazit.ipynb](../notebooks/Fazit.ipynb) | `b2aceda6` / 16 | mich |
| [notebooks/Fazit.ipynb](../notebooks/Fazit.ipynb) | `aab69502` / 17 | ich, mir, ich, meine |
| [notebooks/Anhang_Technische_Engine.ipynb](../notebooks/Anhang_Technische_Engine.ipynb) | `f3aca6f3` / 2 | mich |
| [notebooks/Anhang_Technische_Engine.ipynb](../notebooks/Anhang_Technische_Engine.ipynb) | `df5ab974` / 4 | ich, meine |
| [notebooks/Anhang_Technische_Engine.ipynb](../notebooks/Anhang_Technische_Engine.ipynb) | `61f81690` / 8 | meiner |
| [notebooks/Anhang_Technische_Engine.ipynb](../notebooks/Anhang_Technische_Engine.ipynb) | `d499d0c0` / 39 | meines |
| [notebooks/Anhang_Datenaufbereitung.ipynb](../notebooks/Anhang_Datenaufbereitung.ipynb) | `7de96757` / 2 | meiner, meine |
| [notebooks/Anhang_Datenaufbereitung.ipynb](../notebooks/Anhang_Datenaufbereitung.ipynb) | `aa6eac7c` / 3 | ich, mein, ich |
| [notebooks/Anhang_Datenaufbereitung.ipynb](../notebooks/Anhang_Datenaufbereitung.ipynb) | `9c8038c2` / 4 | ich, meinem, ich |
| [notebooks/Anhang_Datenaufbereitung.ipynb](../notebooks/Anhang_Datenaufbereitung.ipynb) | `12a65682` / 6 | Meine |
| [notebooks/Anhang_Datenaufbereitung.ipynb](../notebooks/Anhang_Datenaufbereitung.ipynb) | `177c2351` / 8 | ich |
| [notebooks/Anhang_Datenaufbereitung.ipynb](../notebooks/Anhang_Datenaufbereitung.ipynb) | `860e3b19` / 19 | meine, meiner |
| [notebooks/Anhang_Datenaufbereitung.ipynb](../notebooks/Anhang_Datenaufbereitung.ipynb) | `10960123` / 21 | meine |
| [notebooks/Anhang_Datenaufbereitung.ipynb](../notebooks/Anhang_Datenaufbereitung.ipynb) | `86fce6da` / 33 | meine |
| [notebooks/Anhang_Datenaufbereitung.ipynb](../notebooks/Anhang_Datenaufbereitung.ipynb) | `7fb1292c` / 38 | meiner |
| [notebooks/Anhang_Datenaufbereitung.ipynb](../notebooks/Anhang_Datenaufbereitung.ipynb) | `cdb92e52` / 46 | mein |
| [notebooks/Anhang_Tests_Validierung.ipynb](../notebooks/Anhang_Tests_Validierung.ipynb) | `353de6dd` / 4 | meine |

### 2.2 Berechtigt unveränderte Fundstellen

Anhang A, Abschnitt `sec-projekt-dokumentation`, sagt ausdrücklich: «Sie werden hier unverändert als Arbeitsnachweis bewahrt und sind keine aktuelle Installations- oder Studienkonfiguration.» Die vier betroffenen Quellenplanungszellen gehören zu diesem Originalbestand aus dem damaligen Überblick. Die im Auftrag geschützten Archivtexte werden daher nicht nachträglich umformuliert.

| Datei / Fundstelle | Unveränderte Wörter | Begründung |
|---|---|---|
| `notebooks/Anhang_Technische_Engine.ipynb`, `8389728d` / Index 91 | Ich, mir, meine, mir (4) | Historische Quellen-/Werkzeugplanung, als unveränderter Originalstand bewahrt. |
| `notebooks/Anhang_Technische_Engine.ipynb`, `c1515f6e` / Index 93 | Ich, mir, meiner, Ich (4) | Historische Quellen-/Werkzeugplanung, als unveränderter Originalstand bewahrt. |
| `notebooks/Anhang_Technische_Engine.ipynb`, `7c098ca4` / Index 95 | Ich, mir, ich, mir, ich (5) | Historische Quellen-/Werkzeugplanung, als unveränderter Originalstand bewahrt. |
| `notebooks/Anhang_Technische_Engine.ipynb`, `5c023149` / Index 97 | Ich, mir, meine, Ich, ich, ich (6) | Historische Quellen-/Werkzeugplanung, als unveränderter Originalstand bewahrt. |
| `ki-nutzung.qmd`, Grundsätze, ursprüngliche Zeile 13 | «wir» (1) | Gegenstand der Einordnung geteilter ChatGPT-Antworten, keine persönliche Erzählperspektive. |

Die erneute Suche bestätigt diese 20 verbliebenen Vorkommen. In den Codequellen stehen keine weiteren Treffer der verwendeten Wortliste. Dateinamen des neuen Originalprompts beziehungsweise Berichts enthalten die Zeichenfolge `ich-formulierungen`; sie sind Linkziele, keine redaktionelle Autorenperspektive.

## 3. Vollständiges Vorher-/Nachherprotokoll

69 Protokolleinträge dokumentieren 70 Textstellen: Der Ausdruck «meine Untersuchung» kommt in E12 zweimal in derselben Zelle vor. Die Umformulierungen betreffen 50 Zellen; sonstige Satzteile, Quellen, Daten, Zahlen und technische Inhalte bleiben erhalten.

### E01 — `index.ipynb`, Zell-ID `bfc2fb04`

**Vorher:** Ich untersuche, wie

**Nachher:** Untersucht wird, wie

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E02 — `index.ipynb`, Zell-ID `af2cc3a8`

**Vorher:** In der Analyse begründe ich Daten und Parameter, stelle die Ergebnisse dar und interpretiere ihre Unterschiede.

**Nachher:** Die Analyse begründet Daten und Parameter, stellt die Ergebnisse dar und interpretiert ihre Unterschiede.

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E03 — `index.ipynb`, Zell-ID `af2cc3a8`

**Vorher:** meinen Rückblick und Ausblick

**Nachher:** den Rückblick und Ausblick des Autors

**Prüfung:** Der persönliche Rückblick bleibt dem Autor zugeordnet.

### E04 — `notebooks/Einleitung.ipynb`, Zell-ID `686a445a`

**Vorher:** Mich interessiert deshalb, wie sich unterschiedliche Anlageregeln mit historischen Daten untersuchen lassen:

**Nachher:** Die Motivation liegt deshalb darin, unterschiedliche Anlageregeln mit historischen Daten zu untersuchen:

**Prüfung:** Der ursprüngliche Untersuchungsanreiz bleibt als Motivation erkennbar; keine allgemeine Wertung ergänzt.

### E05 — `notebooks/Einleitung.ipynb`, Zell-ID `46680b47`

**Vorher:** Besonders reizt mich die Verbindung von Finanzen und Informatik.

**Nachher:** Ein besonderer Anreiz ist die Verbindung von Finanzen und Informatik.

**Prüfung:** Die persönliche Motivation bleibt erhalten, ohne eine allgemeine fachliche Behauptung daraus abzuleiten.

### E06 — `notebooks/Einleitung.ipynb`, Zell-ID `46680b47`

**Vorher:** Ich möchte die Anlageideen so genau verstehen, dass

**Nachher:** Ziel ist, die Anlageideen so genau zu verstehen, dass

**Prüfung:** Die Absicht bleibt ein Ziel und wird nicht als bereits erreicht dargestellt.

### E07 — `notebooks/Einleitung.ipynb`, Zell-ID `a9f0792b`

**Vorher:** Neben dem Endwert möchte ich Investitionszeitpunkte und Veränderungen der Portfoliozusammensetzung nachvollziehen.

**Nachher:** Neben dem Endwert sollen Investitionszeitpunkte und Veränderungen der Portfoliozusammensetzung nachvollzogen werden.

**Prüfung:** Der Zielcharakter bleibt erhalten.

### E08 — `notebooks/Einleitung.ipynb`, Zell-ID `f733daa1`

**Vorher:** Dafür verwende ich Rendite, Volatilität, maximalen Drawdown und Sharpe Ratio.

**Nachher:** Dafür dienen Rendite, Volatilität, maximaler Drawdown und Sharpe Ratio.

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E09 — `notebooks/Einleitung.ipynb`, Zell-ID `4d7593b1`

**Vorher:** Ich vergleiche vier Konzepte:

**Nachher:** Die Arbeit vergleicht vier Konzepte:

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E10 — `notebooks/Einleitung.ipynb`, Zell-ID `a7ae04cd`

**Vorher:** Mir ist wichtig, die Regeln

**Nachher:** Für die Arbeit ist wichtig, die Regeln

**Prüfung:** Die Priorität bezieht sich weiterhin auf diese Arbeit, nicht auf eine neue allgemeine Forderung.

### E11 — `notebooks/Einleitung.ipynb`, Zell-ID `4a72f361`

**Vorher:** Deshalb begründe ich

**Nachher:** Deshalb begründet die Arbeit

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E12 — `notebooks/Theorie.ipynb`, Zell-ID `1941d2df` (2 Vorkommen)

**Vorher:** meine Untersuchung

**Nachher:** diese Untersuchung

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E13 — `notebooks/Theorie.ipynb`, Zell-ID `bdef1563`

**Vorher:** Für mein Modell wähle ich eine feste jährliche Regel zur Reproduzierbarkeit.

**Nachher:** Für dieses Modell wird eine feste jährliche Regel zur Reproduzierbarkeit gewählt.

**Prüfung:** Die jährliche Regel bleibt eine eigene Modellwahl, keine universelle Empfehlung.

### E14 — `notebooks/Theorie.ipynb`, Zell-ID `005fce46`

**Vorher:** meinen Vergleich

**Nachher:** diesen Vergleich

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E15 — `notebooks/Theorie.ipynb`, Zell-ID `005fce46`

**Vorher:** meinen langfristigen Vergleich

**Nachher:** diesen langfristigen Vergleich

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E16 — `notebooks/Theorie.ipynb`, Zell-ID `d512a002`

**Vorher:** Ich passe dies methodisch zu Long/Cash an:

**Nachher:** Für dieses Modell wird dies methodisch zu Long/Cash angepasst:

**Prüfung:** Die eigene Abweichung von Hilpischs Long-/Short-Regel bleibt ausdrücklich bestehen.

### E17 — `notebooks/Methodik.ipynb`, Zell-ID `a233bc87`

**Vorher:** Ich untersuche mit

**Nachher:** Die Arbeit untersucht mit

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E18 — `notebooks/Methodik.ipynb`, Zell-ID `a233bc87`

**Vorher:** betrachte ich ihren Verlauf

**Nachher:** betrachtet sie ihren Verlauf

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E19 — `notebooks/Methodik.ipynb`, Zell-ID `a233bc87`

**Vorher:** verbinde ich die Finanzgrundlagen

**Nachher:** verbindet sie die Finanzgrundlagen

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E20 — `notebooks/Methodik.ipynb`, Zell-ID `35c815dc`

**Vorher:** Anlagen, Zeiträume und Regeln lege ich vorab fest,

**Nachher:** Anlagen, Zeiträume und Regeln werden vorab festgelegt,

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E21 — `notebooks/Methodik.ipynb`, Zell-ID `18279f6c`

**Vorher:** Für meine Untersuchung verwende ich die USA, Kanada, Japan, das Vereinigte Königreich, Deutschland, Frankreich und Italien.

**Nachher:** Für diese Untersuchung werden die USA, Kanada, Japan, das Vereinigte Königreich, Deutschland, Frankreich und Italien verwendet.

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E22 — `notebooks/Methodik.ipynb`, Zell-ID `2565f88a`

**Vorher:** Ich verwende das neueste gemeinsame Jahr

**Nachher:** Verwendet wird das neueste gemeinsame Jahr

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E23 — `notebooks/Methodik.ipynb`, Zell-ID `60c85505`

**Vorher:** Tägliche ETF-Daten beziehe ich mit &lt;code&gt;yfinance&lt;/code&gt; von Yahoo Finance.

**Nachher:** Tägliche ETF-Daten werden mit &lt;code&gt;yfinance&lt;/code&gt; von Yahoo Finance bezogen.

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E24 — `notebooks/Methodik.ipynb`, Zell-ID `a6b32280`

**Vorher:** Für den Ertrag betrachte ich Endvermögen, Gesamtrendite und annualisierte geometrische Rendite.

**Nachher:** Für den Ertrag werden Endvermögen, Gesamtrendite und annualisierte geometrische Rendite betrachtet.

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E25 — `notebooks/Methodik.ipynb`, Zell-ID `a6b32280`

**Vorher:** Für das Risiko verwende ich Volatilität und maximalen Drawdown.

**Nachher:** Für das Risiko dienen Volatilität und maximaler Drawdown.

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E26 — `notebooks/Methodik.ipynb`, Zell-ID `a6b32280`

**Vorher:** Für die Sharpe Ratio ziehe ich von jeder Monatsrendite die risikofreie Vergleichsrendite ab.

**Nachher:** Für die Sharpe Ratio wird von jeder Monatsrendite die risikofreie Vergleichsrendite abgezogen.

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E27 — `notebooks/Analyse.ipynb`, Zell-ID `c50744c1`

**Vorher:** meine Designentscheidung

**Nachher:** eine Designentscheidung des Autors

**Prüfung:** Die eigene Designentscheidung bleibt dem Autor zugeordnet.

### E28 — `notebooks/Analyse.ipynb`, Zell-ID `c50744c1`

**Vorher:** stammen von mir

**Nachher:** stammen vom Autor

**Prüfung:** Die Abgrenzung zwischen Codex-Integration und Autorenverantwortung bleibt ausdrücklich erhalten.

### E29 — `notebooks/Analyse.ipynb`, Zell-ID `762a3ac1`

**Vorher:** Daten und Parameter wähle ich;

**Nachher:** Daten und Parameter wählt der Autor;

**Prüfung:** Die eigene Daten-/Parameterwahl bleibt sichtbar und wird nicht der Literatur zugeschrieben.

### E30 — `notebooks/Analyse.ipynb`, Zell-ID `762a3ac1`

**Vorher:** beurteile ich unterschiedliche Aspekte

**Nachher:** beurteilt die Untersuchung unterschiedliche Aspekte

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E31 — `notebooks/Analyse.ipynb`, Zell-ID `7b9386c9`

**Vorher:** Auf derselben Zeitachse vergleiche ich VT Buy-and-Hold, jährlich 60 % VT/40 % IEF, VT-Long/Cash-Trend und BIP-G7.

**Nachher:** Auf derselben Zeitachse werden VT Buy-and-Hold, jährlich 60 % VT/40 % IEF, VT-Long/Cash-Trend und BIP-G7 verglichen.

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E32 — `notebooks/Analyse.ipynb`, Zell-ID `663b04db`

**Vorher:** unser Resultat

**Nachher:** das Resultat dieser Untersuchung

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E33 — `notebooks/Analyse.ipynb`, Zell-ID `efe3b129`

**Vorher:** Aus täglichen Rohdaten wähle ich die letzte gemeinsame tatsächliche Handelstagsbewertung des Monats mit rechtem Kalender-Monatsendlabel.

**Nachher:** Aus täglichen Rohdaten wird die letzte gemeinsame tatsächliche Handelstagsbewertung des Monats mit rechtem Kalender-Monatsendlabel gewählt.

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E34 — `notebooks/Analyse.ipynb`, Zell-ID `a0dcceaa`

**Vorher:** Ich verwende Yahoos

**Nachher:** Verwendet wird Yahoos

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E35 — `notebooks/Analyse.ipynb`, Zell-ID `31fc788f`

**Vorher:** Ich lege den kurzen SMA über drei, den langen über zwölf Monatsbeobachtungen fest:

**Nachher:** Festgelegt sind der kurze SMA über drei und der lange über zwölf Monatsbeobachtungen:

**Prüfung:** Drei-/Zwölf-Monatsfenster und die Einordnung als eigene, nicht optimale Quellenkombination bleiben unverändert.

### E36 — `notebooks/Analyse.ipynb`, Zell-ID `e3ace74b`

**Vorher:** Für den Sharpe-Vergleich schlage ich die FRED-Reihe &lt;code&gt;DGS3MO&lt;/code&gt; vor.

**Nachher:** Für den Sharpe-Vergleich wird die FRED-Reihe &lt;code&gt;DGS3MO&lt;/code&gt; vorgeschlagen.

**Prüfung:** Der historische Vorschlagsstatus bleibt erhalten; keine Umdeutung in eine bereits fertige Monatsrendite.

### E37 — `notebooks/Analyse.ipynb`, Zell-ID `6f8b54af`

**Vorher:** Für damalige Entscheide verwende ich die archivierten IMF-WEO-Herbstausgaben.

**Nachher:** Für damalige Entscheide werden die archivierten IMF-WEO-Herbstausgaben verwendet.

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E38 — `notebooks/Analyse.ipynb`, Zell-ID `8c8859cc`

**Vorher:** führte ich H1, K1, Z1, S1 und S2

**Nachher:** führte der Autor H1, K1, Z1, S1 und S2

**Prüfung:** Der tatsächliche Ausführende bleibt erkennbar; keine neue Ausführung oder KI-Autorschaft behauptet.

### E39 — `notebooks/Analyse.ipynb`, Zell-ID `6402a9d2`

**Vorher:** Ich interpretiere gespeicherte

**Nachher:** Die Auswertung interpretiert gespeicherte

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E40 — `notebooks/Analyse.ipynb`, Zell-ID `6999a6d3`

**Vorher:** Sobald ich die Schwankungen und Rückgänge einbeziehe,

**Nachher:** Sobald die Schwankungen und Rückgänge einbezogen werden,

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E41 — `notebooks/Analyse.ipynb`, Zell-ID `53354686`

**Vorher:** Ich behandle ihn als wichtigen Erklärungsansatz, nicht als nachgewiesene alleinige Ursache.

**Nachher:** Er wird als wichtiger Erklärungsansatz behandelt, nicht als nachgewiesene alleinige Ursache.

**Prüfung:** Die kausale Einschränkung bleibt wörtlich erhalten.

### E42 — `notebooks/Fazit.ipynb`, Zell-ID `64f46030`

**Vorher:** Das ist für mich die wichtigste inhaltliche Erkenntnis:

**Nachher:** Die wichtigste inhaltliche Erkenntnis lautet:

**Prüfung:** Die Priorisierung dieser Erkenntnis bleibt auf den vorangehenden Ergebnisvergleich bezogen.

### E43 — `notebooks/Fazit.ipynb`, Zell-ID `b2aceda6`

**Vorher:** Für mich liegt der Beitrag der Arbeit

**Nachher:** Aus Autorensicht liegt der Beitrag der Arbeit

**Prüfung:** Die Einschätzung des Beitrags bleibt ausdrücklich eine Autorenbewertung.

### E44 — `notebooks/Fazit.ipynb`, Zell-ID `aab69502`

**Vorher:** Dadurch konnte ich sicherstellen,

**Nachher:** Dadurch konnte sichergestellt werden,

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E45 — `notebooks/Fazit.ipynb`, Zell-ID `aab69502`

**Vorher:** liegt weiterhin bei mir.

**Nachher:** liegt weiterhin beim Autor.

**Prüfung:** Die Verantwortung des Autors bleibt ausdrücklich benannt.

### E46 — `notebooks/Fazit.ipynb`, Zell-ID `aab69502`

**Vorher:** Dabei muss ich besonders darauf achten,

**Nachher:** Dabei muss der Autor besonders darauf achten,

**Prüfung:** Keine persönliche Freigabe oder bereits abgeschlossene Endkontrolle behauptet.

### E47 — `notebooks/Fazit.ipynb`, Zell-ID `aab69502`

**Vorher:** meine Schlussfolgerungen

**Nachher:** seine Schlussfolgerungen

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E48 — `notebooks/Anhang_Technische_Engine.ipynb`, Zell-ID `f3aca6f3`

**Vorher:** Aus den Anforderungen ergibt sich für mich folgende Reihenfolge:

**Nachher:** Der Autor leitet aus den Anforderungen folgende Reihenfolge ab:

**Prüfung:** Der Architekturentwurf bleibt eine Ableitung des Autors.

### E49 — `notebooks/Anhang_Technische_Engine.ipynb`, Zell-ID `df5ab974`

**Vorher:** Würde ich zuerst die Simulationsfunktion programmieren und erst danach entscheiden,

**Nachher:** Würde zuerst die Simulationsfunktion programmiert und erst danach entschieden,

**Prüfung:** Die hypothetische Bedingung bleibt im Konjunktiv; keine tatsächlich erfolgte Fehlplanung behauptet.

### E50 — `notebooks/Anhang_Technische_Engine.ipynb`, Zell-ID `df5ab974`

**Vorher:** meine eigene Designentscheidung

**Nachher:** eine eigene Designentscheidung des Autors

**Prüfung:** Eigene Architekturentscheidung bleibt sichtbar.

### E51 — `notebooks/Anhang_Technische_Engine.ipynb`, Zell-ID `61f81690`

**Vorher:** meiner Untersuchung

**Nachher:** dieser Untersuchung

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E52 — `notebooks/Anhang_Technische_Engine.ipynb`, Zell-ID `d499d0c0`

**Vorher:** meines eigenen Systems

**Nachher:** des eigenen Systems

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E53 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `7de96757`

**Vorher:** meiner Untersuchung

**Nachher:** dieser Untersuchung

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E54 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `7de96757`

**Vorher:** meine technische Schlussfolgerung

**Nachher:** die technische Schlussfolgerung des Autors

**Prüfung:** Der Datenvertrag bleibt die eigene technische Ableitung und keine Vorschrift McKinneys.

### E55 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `aa6eac7c`

**Vorher:** Für den Austausch zwischen Import, Kontrolle und späterer Benutzeroberfläche verwende ich in der ersten Version CSV-Dateien.

**Nachher:** Für den Austausch zwischen Import, Kontrolle und späterer Benutzeroberfläche werden in der ersten Version CSV-Dateien verwendet.

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E56 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `aa6eac7c`

**Vorher:** mein Projekt

**Nachher:** dieses Projekt

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E57 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `aa6eac7c`

**Vorher:** Beim Entwickeln kann ich leicht kontrollieren,

**Nachher:** Beim Entwickeln lässt sich leicht kontrollieren,

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E58 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `9c8038c2`

**Vorher:** Für die Marktzeitreihen verwende ich als Austauschformat eine lange Tabelle.

**Nachher:** Für die Marktzeitreihen dient als Austauschformat eine lange Tabelle.

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E59 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `9c8038c2`

**Vorher:** Diese Beschreibung passt direkt zu meinem Problem.

**Nachher:** Diese Beschreibung passt direkt zur Problemstellung dieser Untersuchung.

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E60 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `9c8038c2`

**Vorher:** Deshalb lege ich nicht fest,

**Nachher:** Deshalb wird nicht festgelegt,

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E61 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `12a65682`

**Vorher:** Meine Entscheidung ist,

**Nachher:** Die Entscheidung für dieses Modell ist,

**Prüfung:** Long-/Wide-Aufteilung bleibt eine eigene Modellentscheidung.

### E62 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `177c2351`

**Vorher:** Für eine Marktzeitreihe definiere ich zunächst drei Pflichtfelder:

**Nachher:** Für eine Marktzeitreihe sind zunächst drei Pflichtfelder definiert:

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E63 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `860e3b19`

**Vorher:** meine Untersuchung

**Nachher:** diese Untersuchung

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E64 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `860e3b19`

**Vorher:** meiner Methodik

**Nachher:** dieser Methodik

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E65 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `10960123`

**Vorher:** meine Untersuchung

**Nachher:** diese Untersuchung

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E66 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `86fce6da`

**Vorher:** meine Untersuchung

**Nachher:** diese Untersuchung

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E67 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `7fb1292c`

**Vorher:** meiner später ausgewählten Anbieter

**Nachher:** der für diese Arbeit später ausgewählten Anbieter

**Prüfung:** Der geplante Auswahlzeitpunkt bleibt erkennbar; keine allgemeine Anbieterentscheidung behauptet.

### E68 — `notebooks/Anhang_Datenaufbereitung.ipynb`, Zell-ID `cdb92e52`

**Vorher:** mein Projekt

**Nachher:** dieses Projekt

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

### E69 — `notebooks/Anhang_Tests_Validierung.ipynb`, Zell-ID `353de6dd`

**Vorher:** meine Simulation

**Nachher:** diese Simulation

**Prüfung:** Persönliche Perspektive durch eine sachliche, untersuchungsspezifische Formulierung ersetzt; Aussage und Zeitbezug bleiben erhalten.

## 4. Wortzahl mit unveränderter Zählmethode

Die tatsächliche ursprüngliche Funktion `count()` aus der früheren Fachkorrektur-Arbeitsablage wurde gelesen und für die reine Zählung unverändert übernommen. Der aktuelle Ausgangswert reproduziert die dokumentierten 7’959/7’834 exakt; keine Abweichung oder neue Tokenregel.

Filterfolge: nur Markdown-Prosa der sechs Hauptnotebooks; Codefences/HTML-`pre`, HTML-/Markdown-Überschriften, Markdown-Tabellenzeilen, Display-/Inline-Mathematik und Zitationsklammern ausschliessen; `@sec-…` entfernen; Linkziele entfernen und sichtbare Beschriftungen erhalten; HTML-Tags entfernen und Entities entschlüsseln. Raw/YAML, Codezellen und Outputs sowie technische/KI-Anhänge zählen nicht. Tokenregel: `\b\w+(?:[’'-]\w+)*\b`.

| Hauptkapitel | Vorher | Nachher | Änderung |
|---|---:|---:|---:|
| index.ipynb | 125 | 125 | +0 |
| notebooks/Einleitung.ipynb | 430 | 435 | +5 |
| notebooks/Theorie.ipynb | 2’769 | 2’771 | +2 |
| notebooks/Methodik.ipynb | 855 | 853 | -2 |
| notebooks/Analyse.ipynb | 2’949 | 2’956 | +7 |
| notebooks/Fazit.ipynb | 831 | 829 | -2 |
| **Mit Überblick** | **7’959** | **7’969** | **+10** |
| **Ohne Überblick** | **7’834** | **7’844** | **+10** |

Reserve zu 8’000: **31** Wort-/Zahlentoken mit Überblick, **156** ohne. Keine fachliche Kürzung zur Einhaltung der Obergrenze durchgeführt. Dies ist die projektspezifische Zählung, keine Word-Zählung.

## 5. Wissenschaftliche und technische Schutzprüfung

Alle 70 Stellen wurden anhand des Originals geprüft. Eigenentscheidungen bleiben eigene Untersuchungs-/Modellentscheidungen; Autorenbewertung bleibt beispielsweise als «Aus Autorensicht» erkennbar. Der historische FRED-Vorschlag bleibt ein Vorschlag. Die hypothetische Reihenfolge im Engine-Entwurf bleibt im Konjunktiv. Die Einschränkung des US-Anteils als Erklärungsansatz, nicht alleinige nachgewiesene Ursache, bleibt bestehen.

Die Zuordnung von KI- und Autorenleistungen bleibt ausdrücklich erhalten: «stammen vom Autor», «führte der Autor» und «liegt weiterhin beim Autor» ersetzen die persönliche Pronomenform ohne die Verantwortung zu anonymisieren. Die Endkontrolle der neuen KI-Fassung bleibt ausstehend.

| Prüfung | Resultat |
|---|---|
| Notebookstruktur | Alle neun Notebooks syntaktisch gültig; insgesamt 494 Zellen, IDs/Reihenfolge/Metadaten/Formatversionen erhalten. Nur `source`-Strings der 50 Markdown-Zellen verändert. |
| Code und Outputs | Alle 28 vollständigen Codezellobjekte und 28 Outputobjekte unverändert, einschliesslich Execution Counts und Metadaten. Keine Ausführung. |
| Formeln | Alle 95 Display-/Inline-Mathematikblöcke wörtlich unverändert. |
| Zahlen und technische Inhalte | Zahlen, Tabellenzeilen, Codefences/Inline-Code, HTML-Tags/Attribute, Zitatspannen, Link-/Bildpfade, Abschnittsanker und Querverweise je Markdown-Zelle vor/nachher identisch. |
| Zitationsquelltext | Alle 149 Zitationsklammerntreffer identisch; die statische Quellsuche schliesst die unveränderte Zitationssyntax im historischen Markdown-Codebeispiel ein. Aktive Auflösung wird zusätzlich im Render kontrolliert. |
| Forschungsfrage / Ergebnisbestände | Forschungsfrage-Zelle unverändert; alle gespeicherten Grafiken, Ergebnisse, Manifeste und Studienlaufnamen/Parameter unangetastet. |
| Bytevergleich | Nach Maskierung ausschliesslich der `source`-Stringtokens geänderter Markdown-Zellen ist jede Notebookdatei bytegleich zum Original. Kein JSON-Reformatting und kein Re-Saving. |
| Historische KI-Dokumentation | QMD-Ausgangsbytes nach Entfernen genau des neuen Abschnitts vollständig identisch; bestehender Verantwortungsabsatz am Schluss erhalten. KI-Log als originales Bytepräfix bewahrt. |
| Weitere geschützte Dateien | Bibliografie, CSL, Quarto-Konfiguration, Styles/Filter, README, Archive, alte Prompts/Logs/Berichte, generierte TeX-Quelle und vorhandene Ausgabe-/Freeze-/Cachedateien hashidentisch. |
| Engine / historischer Studienstand | 317 erfasste Engine-Dateien unverändert, darunter Datenarchiv, Wheel, Inputs, Configs, Originalprompts und Nachweise; HEAD unverändert. Keine Engine-Funktion importiert oder ausgeführt. |

## 6. KI-Nachweis und persönliche Endkontrolle

ChatGPT: Vorbereitung des Auftrags laut bereitgestellter Arbeitsanweisung. Codex: tatsächliche Analyse, Formulierungsarbeit, Schutz-/Wortzahlprüfungen, Bericht und KI-Dokumentationsabgleich. Die übernommenen Ersatzformulierungen und die Dokumentation stammen von Codex. Keine neue finanzwissenschaftliche Forschung, Datenbeschaffung, Optimierung oder Ergebnisberechnung.

KI-DOKUMENTATION-BUCH-SYNC: neuer datierter Logeintrag und neuer sachlicher Buchabschnitt wurden im selben Auftrag ergänzt und auf denselben Umfang, dieselben Zahlen und dieselben Grenzen abgeglichen. Der [Originalprompt](ai-usage/prompts/2026-10-14-ich-formulierungen-wissenschaftlicher-stil.txt) enthält den vollständigen Auftrag einschliesslich ursprünglicher persönlicher Formulierungen; er wurde nicht stilistisch verändert.

Der Autor muss insbesondere die Umformulierungen der Motivation, die Einordnung des wichtigsten Befunds und des Arbeitsbeitrags sowie die weiterhin sichtbaren eigenen Entscheidungen und Verantwortungszuordnungen persönlich gegenlesen. Die technischen Vergleiche ersetzen diese Endkontrolle nicht.

## 7. Darstellungsprüfung und abschliessender Git-Status

- **HTML:** Exit 0, elf Buchseiten, 1652 lokale Link-/Ankervorkommen mit null ungültigen Zielen. Die Suche im tatsächlich sichtbaren Hauptinhalt findet ausschliesslich 19 Wörter im historischen Originalbestand und das eine zitierte «wir» im KI-Hinweis. In den sechs Hauptkapiteln und sonstiger redaktioneller Prosa verbleibt keine Ich-/Wir-Perspektive.
- **PDF:** Exit 0, 117 A4-Seiten. Alle Seiten gerastert und in sechs Gesamtübersichten geprüft; Detailprüfung von Inhaltsverzeichnis, Motivation/Forschungsfrage, Rückblick/Verantwortung und KI-Nachtrag. Die 20 verbliebenen Wörter stehen auf physischen PDF-Seiten 85/86 (historischer Originalstand) und 103 (zitierter KI-Ausdruck). Neuer KI-Nachtrag auf physischen Seiten 116–117. Sämtliche 45 vorhandenen ChatGPT-Share-URLs bleiben tatsächliche PDF-Linkziele.
- **Rendergrenze:** Ausschliesslich externe vollständige Projektkopie. Profile setzen `execute.enabled=false`, `freeze=false`, `cache=false`; zusätzlich `--no-execute --no-cache`. `latex-auto-install=false` verhindert automatische TeX-Paketinstallation. Die Quarto-Post-Render-Hilfe lief nur auf den Kopien. Kein Notebook-/Engine-Code, historische Tests oder Backtests ausgeführt; kein Download, keine Installation und kein Serverzugriff. DOCX wurde nicht erneut gerendert.
- **Notebook-Schema:** Alle neun Notebooks mit dem bereits vorhandenen `nbformat` der Projekt-`.venv` erfolgreich geprüft; Aufruf mit `-B`, ohne Kernel. Der erste Versuch im gebündelten Python meldete `ModuleNotFoundError: nbformat`. Keine Installation vorgenommen; die verfügbare Projektumgebung wurde für diese reine JSON-Schemaprüfung verwendet.
- **Sprachliche Kontrolle:** Bei den Konstruktionen mit «dienen» wurden die grammatisch erforderlichen Nominativformen («maximaler Drawdown») mitgeführt; diese Anpassungen sind in E08/E25 vollständig enthalten. Keine fachliche Begriffskorrektur.
- **Prüffassung:** [PDF zur Autorenkontrolle](../Ich-Formulierungen-Prueffassung-2026-10-14.pdf); neue Datei, keine bestehende Ausgabe ersetzt. Die alten Render-/Freeze-/Cachedateien und frühere Prüffassungen bleiben unverändert.
- **Git:** Branch/HEAD/Git-Index unverändert; ausschliesslich die elf unten genannten Bestandsdateien geändert, zwei neue versionierbare Nachweise angelegt. `git diff --check` erfolgreich; nur bestehende Windows-Zeilenendhinweise möglich. Kein Staging, Commit, Push, Checkout, Reset, Clean oder weitere Git-Schreiboperation.

### Betroffene Dateien

| Bestandsdatei | Änderung |
|---|---|
| [index.ipynb](../index.ipynb) | 2 Markdown-Zellen |
| [notebooks/Einleitung.ipynb](../notebooks/Einleitung.ipynb) | 7 Markdown-Zellen |
| [notebooks/Theorie.ipynb](../notebooks/Theorie.ipynb) | 4 Markdown-Zellen |
| [notebooks/Methodik.ipynb](../notebooks/Methodik.ipynb) | 6 Markdown-Zellen |
| [notebooks/Analyse.ipynb](../notebooks/Analyse.ipynb) | 13 Markdown-Zellen |
| [notebooks/Fazit.ipynb](../notebooks/Fazit.ipynb) | 3 Markdown-Zellen |
| [notebooks/Anhang_Technische_Engine.ipynb](../notebooks/Anhang_Technische_Engine.ipynb) | 4 Markdown-Zellen |
| [notebooks/Anhang_Datenaufbereitung.ipynb](../notebooks/Anhang_Datenaufbereitung.ipynb) | 10 Markdown-Zellen |
| [notebooks/Anhang_Tests_Validierung.ipynb](../notebooks/Anhang_Tests_Validierung.ipynb) | 1 Markdown-Zellen |
| [ki-nutzung.qmd](../ki-nutzung.qmd) | Genau ein neuer Abschnitt zur stilistischen Bearbeitung; historische Fassung unverändert erhalten. |
| [documentation/ai-usage/ai-usage-log.md](ai-usage/ai-usage-log.md) | Neuer datierter KI-Eintrag, altes Bytepräfix erhalten. |

Neu: dieser Abschlussbericht und die bytegleiche Originalpromptkopie. Die neue PDF-Prüffassung ist über die bestehende `*.pdf`-Regel ignoriert. Alle Änderungen bleiben zur Autorenkontrolle uncommitted.

## 8. Abschluss und offene persönliche Kontrolle

**70 Textstellen in 50 Markdown-Zellen überarbeitet; 72 persönliche Wortvorkommen entfernt. 20 berechtigt unveränderte Vorkommen. Keine fachlich unklare Einzelentscheidung offen. Haupttext 7’969 mit / 7’844 ohne Überblick. STOPP zur Autorenkontrolle.**

Die persönliche Endkontrolle betrifft die Übernahme der von Codex formulierten Stilfassungen und die korrekte Beschreibung dieses Einsatzes. Eine solche Freigabe wird durch diesen Bericht nicht vorweggenommen.

