# Wissenschaftlich kontrollierte Kürzung des Haupttexts – Stufe 1

Datum: 12. Oktober 2026. Verfasser: Codex. **Alle 46 freigegebenen Massnahmen umgesetzt; keine zweite Kürzungsstufe ausgeführt. STOPP zur Autorenkontrolle.**

Der Haupttext umfasst nach der bisherigen Methode neu **8’948 Wort-/Zahlentoken einschliesslich Überblick** beziehungsweise **8’823 ohne Überblick**. Die Nettoersparnis beträgt **3’794** beziehungsweise **3’063**. Wissenschaftliche Vollständigkeit hatte Vorrang vor der maximalen Kürzung. Die erwartete erste Zielspanne von 8’642–9’327 wird erreicht; die Obergrenze von 8’000 noch nicht.

## 1. Ausgangsstand und Arbeitsgrenzen

Branch `dev`; tatsächlicher Ausgangs- und End-HEAD `89a8fd130865fe40e2c33449efc6a8dacc2c0227`. Zu Beginn sauberer Arbeitsbaum. Keine anwendbare `AGENTS.md` im Repository oder seinen übergeordneten Verzeichnissen gefunden. Vollständig berücksichtigt wurden der [Kürzungsplan](kuerzungsplan-haupttext-2026-10-12.md), alle sechs Hauptkapitel, Anhänge A–D, der [Phase-2-Bericht](gesamtgegenlesen-phase2-2026-10-12.md), der [Auslagerungsbericht](auslagerung-technische-anhaenge-2026-10-12.md), KI-Regeln und README-Synchronisationsanweisung.

Der vollständige ausgeführte Auftrag ist byteidentisch unter [Promptkopie](ai-usage/prompts/2026-10-12-kuerzung-haupttext-stufe1.txt) gespeichert. SHA-256: `fd83d46c9dd8342b4fa64aa3ca62a311c37d8d20ab7090800573613bc0757087`.

Vor dem ersten Eingriff wurde eine vollständige externe Ausgangssicherung erstellt: `C:\Users\modic\AppData\Local\Temp\codex-kuerzung-stufe1-2026-10-12-uj0waob4\original`. Sie enthält 154 Arbeitsdateien, darunter alle 83 ursprünglich versionierten Dateien und alle 70 vorhandenen Dateien unter `_book`, `_freeze` und `.quarto`. Nur `.git`, `.venv` und `__pycache__` wurden vom Kopieren ausgeschlossen. Alle gesicherten Bytes wurden gegen SHA-256 des Ausgangsstands geprüft.

Freigabe: P01; E01/E02/E04; T02–T13; M01–M04; A01/A03/A04–A25; F01/F03. **T01 und F04 bleiben vollständig unverändert. F02 bleibt inhaltlich und sprachlich unverändert; ausschliesslich seine aktuellen Kapitelverweise wurden mechanisch angepasst.** Keine zusätzlichen Haupttextkürzungen, Fachkorrekturen, Notebook-Ausführung, Engine-Tests, Backtests, Optimierung, Datenbeschaffung, Netzwerkdownloads oder Paketinstallation. Kein Staging, Commit, Push, Merge, Reset oder Clean.

## 2. Gleiche Zählmethode und Umfang

Gezählt wurde sichtbare Markdown-Prosa in den sechs Notebook-Quellen. Raw-/YAML-Zellen, Codezellen und ihre Ausgaben, Bilder, Codefences, HTML-`pre`, Überschriften, Markdown-Tabellenzeilen, Display-/Inline-Mathematik und Zitationsklammern sind ausgeschlossen. HTML-Tags, Linkziele und `@sec-…`-Verweise werden entfernt; sichtbare Linkbeschriftungen bleiben. HTML-Entities werden entschlüsselt. Wort-/Zahlentoken folgen `\b\w+(?:[’'-]\w+)*\b`. Dieselbe Filterfolge reproduziert die bisherigen 12’742/11’886 Token. Dies ist eine dokumentierte Vergleichsmethode, keine unabhängig bestätigte schulische Zählkonvention.

Die Massnahmenblöcke sind disjunkt. Neu formulierte Überblicksprosa wird P01 zugerechnet; neu hinzugefügte Haupttextverweise zählen in den jeweiligen Nachherwert. Verschobene Prosa spart Haupttext, bleibt aber im Anhang. Reine Überschriften-, Tabellen-, Formel- und Codebewegungen erzeugen keine künstliche Wortersparnis.

| Kapitel | Vorher | Nachher | Nettoersparnis |
|:---|---:|---:|---:|
| 1 Überblick | 856 | 125 | 731 |
| 2 Einleitung | 785 | 629 | 156 |
| 3 Theorie | 3’670 | 2’985 | 685 |
| 4 Methodik | 1’080 | 905 | 175 |
| 5 Analyse | 5’399 | 3’448 | 1’951 |
| 6 Fazit | 952 | 856 | 96 |
| **Haupttext mit Überblick** | **12’742** | **8’948** | **3’794** |
| **Haupttext ohne Überblick** | **11’886** | **8’823** | **3’063** |
 
Die technische Anhangsprosa A–C steigt nach derselben Methode von 3’576 auf 4’815: A 1’067→2’039, B 1’954→2’204, C 555→572. Der Zuwachs von 1’239 enthält Originalübernahmen und neue Einleitungen/Zuordnungshinweise und wird nicht zusätzlich als Haupttextersparnis angerechnet. KI-Anhang, Literaturverzeichnis und dieser Bericht sind nicht Teil der Haupttextzählung.

## 3. Vollständiger Vergleich nach Massnahmen-ID

Abschnittsangaben beziehen sich hier auf die **alte** Gliederung des Plans, damit die Zuordnung eindeutig bleibt. Die aktuelle Analysegliederung steht in Abschnitt 5 dieses Berichts. Alle 46 Statusangaben lauten «umgesetzt»; keine Massnahme wurde ausgesetzt. Die tatsächliche Verdichtung fällt innerhalb der erlaubten Grenzen unterschiedlich stark aus.

| ID | Ursprünglicher Abschnitt | Vorher | Nachher | Ersparnis | Status | Ausführung und erhaltener Kern |
|:---|:---|---:|---:|---:|:---|:---|
| P01 | 1 gesamter Überblick | 856 | 125 | 731 | umgesetzt | Kurzer wissenschaftlicher Überblick; technische Originaltexte nach A.7, Forschungsfrage und beide Raw-Zellen unverändert. |
| E01 | 2.1 Motivation | 212 | 106 | 106 | umgesetzt | Motivation verdichtet; persönliches Interesse, Risikoargument, drei Regeltypen und Informatikbezug erhalten. |
| E02 | 2.2 Ziele | 165 | 150 | 15 | umgesetzt | Kennzahlenabsatz verdichtet; Endwertargument und Untersuchungsziele bleiben ausführlich erhalten. |
| E04 | 2.4 Aufbau | 94 | 59 | 35 | umgesetzt | Aufbauhinweise gebündelt; Theorie–Methodik–Analyse–Fazit und deren Funktion erhalten. |
| T02 | 3.1.2 Diversifikation/Korrelation | 267 | 207 | 60 | umgesetzt | Diversifikations-/Krisenabsätze verdichtet; Korrelationsspannweite, lineare Bedeutung von null, Nutzen unter +1 und Markt-/Einzelrisiko erhalten. |
| T03 | 3.1.3 Allokation/Rebalancing | 238 | 183 | 55 | umgesetzt | Drift und Rebalancing verdichtet; Formeln/Variablen, Eigenanteil, Kalender-/Bandregel und jährliche Modellwahl erhalten. |
| T04 | 3.1.4 Buy-and-Hold | 183 | 151 | 32 | umgesetzt | Nur Vorteile/Risiken knapp gefasst; Funktionsweise und historisches Risiko vollständig behalten. |
| T05 | 3.1.5 60/40 | 215 | 169 | 46 | umgesetzt | Grenzen des 60/40-Konzepts verdichtet; wechselnde Korrelation, 2022, Länderunterschiede und Rendite-Risiko-Konflikt erhalten. |
| T06 | 3.1.6 Ländergewichtung | 208 | 171 | 37 | umgesetzt | Gewichtungs-/Vergleichserläuterungen verdichtet; BIP-Formel/Variablen, Klumpenrisiken, Komplexität und fehlender Überlegenheitsbeweis erhalten. |
| T07 | 3.2.1 Zeitreihen/Resampling | 235 | 116 | 119 | umgesetzt | Zeitreihenprosa verdichtet; technische pandas-/Alias-/API-Belege nach B.3.3; Python-Zelle und Foresight-Absatz bleiben unverändert im Theorienotebook. |
| T08 | 3.2.2.1–3 Rendite | 149 | 129 | 20 | umgesetzt | Geometrische Rendite/Annualisierung knapper erklärt; alle Formeln, Variablen und arithmetisch-geometrische Unterscheidung erhalten. |
| T09 | 3.2.3 Volatilität | 476 | 379 | 97 | umgesetzt | Bedeutung, Annualisierung und Interpretation verdichtet; Standardabweichungsdefinition, Variablen, Voraussetzungen und Risikogrenzen erhalten. |
| T10 | 3.2.4 Drawdown | 321 | 273 | 48 | umgesetzt | Drawdown-/Erholungsprosa verdichtet; Formeln, Variablen und historische QuantStats-Ausgabe/-Deutung unverändert erhalten. |
| T11 | 3.2.5 Sharpe | 217 | 178 | 39 | umgesetzt | Vergleichs-/Grenzenabsatz verdichtet; Sharpe-Formel, Variablentabelle, RF/Raw-Unterscheidung und Zeit-/Frequenzvergleich erhalten. |
| T12 | 3.2.6 Trendfolge | 381 | 323 | 58 | umgesetzt | SMA-/Signalprosa verdichtet; Formel, Variablen, Fensterbereiche und eigene Long/Cash-Abwandlung erhalten. |
| T13 | 3.3.1–4 Methodische Grenzen | 343 | 269 | 74 | umgesetzt | Look-ahead-/Kosten-/Datenqualitätserklärungen verdichtet; Verfügbarkeit, Signalverzug, Overfitting und Inflationsgrenze erhalten. |
| M01 | 4.1 Untersuchungsansatz | 173 | 100 | 73 | umgesetzt | Untersuchungsansatz gebündelt; historische Untersuchung, allgemeine Engine, Vorabfestlegung und eigene Entscheidungen erhalten. |
| M02 | 4.2.1–4 Strategien | 407 | 358 | 49 | umgesetzt | Buy-and-Hold und 60/40 verdichtet; Trend-/BIP-Erklärungen vollständig belassen, jährliche Folgepositionen und fehlender Rebalancing-Kontrolllauf erhalten. |
| M03 | 4.3 Vergleichsbedingungen | 287 | 256 | 31 | umgesetzt | H1/K1/Z1-Vergleichsgrenzen gebündelt; Kapital, Zeitpunkte, Kosten, RF und BIP-Regeln sonst erhalten. |
| M04 | 4.4 Auswertung/Grenzen | 213 | 191 | 22 | umgesetzt | Ergänzende Verlaufsauswertung verdichtet; Teilperioden ohne Neustart und keine einzelne Gesamtrangliste erhalten. |
| A01 | 5.1–5.9 Modellbrücke | 485 | 146 | 339 | umgesetzt | Bisher 5.1–5.9 zu 5.1 zusammengeführt; Modellbrücke, Datenvertrag, Eigenentscheidungen und wesentliche KI-Integration/-Tests ausdrücklich erhalten. |
| A03 | 5.10.1 Untersuchungsentscheid | 214 | 81 | 133 | umgesetzt | Untersuchungsentscheid verdichtet; feste Engine, eigene Parameterwahl und Quellen-/Optimierungsgrenzen erhalten. |
| A04 | 5.10.2 Wertreihen | 237 | 154 | 83 | umgesetzt | Wertreihenprosa verdichtet; Ticker-/Produkttabelle, IEF-Risiko, G7-Begrenzung und historische Index-/Datenprüfung erhalten. |
| A05 | 5.10.3 Blöcke/Vergleich | 331 | 208 | 123 | umgesetzt | Läufe/Vergleichsgrenzen gebündelt; alle Märkte, Zeiträume, Anfangsbewertungen, Periodenzahlen, Kontrollunterscheidungen und Sensitivitätsgrenzen erhalten. |
| A06 | 5.10.4 Monatslogik/Kapital | 271 | 166 | 105 | umgesetzt | Monatslogik verdichtet; Engine-Frequenzangaben nach B.3.2, tatsächliche Quelltage, gemeinsamer Monatsstand, keine Interpolation und Monats-MDD-Grenze erhalten. |
| A07 | 5.10.5 Performance/Kosten | 165 | 110 | 55 | umgesetzt | Performance-/Kostenprosa verdichtet; Anbieterproxy, Split-/Dividendenprüfung, keine Doppelzählung und enthaltene versus zusätzliche Kosten erhalten. |
| A08 | 5.10.6 Trendparameter | 200 | 135 | 65 | umgesetzt | Trendparameter verdichtet; 3/12, 2/12, 6/12, Vorlauf, dieselbe Kursreihe, Long/Cash, Nullzins und Signalverzug erhalten. |
| A09 | 5.10.7 RF-Reihe | 209 | 145 | 64 | umgesetzt | RF-Text verdichtet; Dateifelder nach B.5.1, strikte Vorverfügbarkeit, sieben Tage, ACT/365-Approximation und RF≠Cash erhalten. |
| A10 | 5.10.8 BIP-Verfügbarkeit | 349 | 226 | 123 | umgesetzt | BIP-Text verdichtet; Vorprüfstand nach B.4.1 und Dateimetadaten nach B.5.2; NGDPD, Istjahrfilter, gemeinsamer Jahrgang und Veröffentlichung+1 erhalten. |
| A11 | 5.10.9 Festlegungen/Grenzen | 113 | 65 | 48 | umgesetzt | Vorabfestlegung/Aussagegrenzen gebündelt; Fehlerwiederholung bleibt von unerwünschter Rendite getrennt. |
| A12 | 5.11 Durchführung | 248 | 206 | 42 | umgesetzt | Durchführung gebündelt; Paketversionen nach C.3.1; Datum, Engine/Commit, unveränderter Laufstand und Perioden-/Vorlaufnachweise erhalten. |
| A13 | 5.12 Ergebnis-Einleitung | 215 | 108 | 107 | umgesetzt | Ergebniseinleitung verdichtet; technische Dateiprüfkette nach A.6.2; nominale Kennzahlen, Rundung und Monatsgrenze erhalten. |
| A14 | 5.12.1 H1 | 197 | 158 | 39 | umgesetzt | H1-Tabellenwiederholung gekürzt; Rendite-/Risikointerpretation, 60/40-Sharpe und Trend-MDD-Vergleich erhalten. |
| A15 | 5.12.2 K1 | 95 | 71 | 24 | umgesetzt | K1-Tabellenwiederholung gekürzt; 146’494-USD-Abstand und Vergleich derselben Fonds ohne Marktkapitalisierung erhalten. |
| A16 | 5.12.3 Z1 | 165 | 123 | 42 | umgesetzt | Z1-Ergebnisprosa verdichtet; 1,22 Mio., MDD vom Höchststand und unterschiedliche Rangfolgen erhalten. |
| A17 | 5.12.4 SMA-Sensitivität | 98 | 79 | 19 | umgesetzt | SMA-Ergebnisprosa verdichtet; 6/12-Endwert, ähnliche Renditen und gleiche gerundete MDD ohne gleiche Pfade erhalten. |
| A18 | 5.12.5 H1-Teilperioden | 142 | 106 | 36 | umgesetzt | Teilperiodenprosa verdichtet; 96/96 Renditen, kein Neustart und Volatilitäts-/Sharpe-Veränderung erhalten. |
| A19 | 5.13 Einleitung +5.13.7 | 150 | 57 | 93 | umgesetzt | Interpretationseingang/Überleitung gebündelt; Gewichte/Signale und abschliessende Begrenzung erhalten. |
| A20 | 5.13.1 Ertrag/Risiko | 144 | 101 | 43 | umgesetzt | Ertrag/Risiko verdichtet; Engine-Sharpe-Definition und Volatilität versus grösster Verlust erhalten. |
| A21 | 5.13.2 60/40-Deutung | 223 | 156 | 67 | umgesetzt | 60/40-Beispiel/Deutung verdichtet; konkrete Umschichtung, 2022-Werte und fehlende isolierte Rebalancing-Kausalität erhalten. |
| A22 | 5.13.3 Trend-Deutung | 375 | 279 | 96 | umgesetzt | Trenddeutung verdichtet; Signaltabelle, Verzögerung, 2020/2022 und verlustübergreifende Investitions-/Cash-Phasen erhalten. |
| A23 | 5.13.4 Länder-Deutung | 296 | 213 | 83 | umgesetzt | Länderdeutung verdichtet; H1-Universumsgrenze, K1-Kontrolle, US-Gewichte und vorhandene Einzel-CAGRs erhalten. |
| A24 | 5.13.5 Zeit/Parameter | 271 | 195 | 76 | umgesetzt | Zeit-/Parameterdeutung verdichtet; Z1-Markt-Zeit-Konfundierung, Long/Cash-Monate, Hauptparameter und Übertragbarkeitsgrenzen erhalten. |
| A25 | 5.13.6 Auswertungsgrenzen | 206 | 160 | 46 | umgesetzt | Auswertungsgrenzen verdichtet; Kosten/Steuern/Inflation, Monatsauflösung, RF/Cash, USD/CHF und fehlender Signifikanztest erhalten. |
| F01 | 6.1 Forschungsantwort | 166 | 100 | 66 | umgesetzt | Forschungsantwort gebündelt; Frage wortgleich, Daten-/Rechen-/Kontrollkette, Wiederholbarkeit und keine Prognose erhalten. |
| F03 | 6.3 Grenzen | 165 | 135 | 30 | umgesetzt | Grenzenabsatz verdichtet; Cash/RF, Kosten/Steuern/Inflation und Monatsrisiko erhalten; eigene Weiterführungen unverändert. |

**Summenprüfung:** 731+156+685+175+1’951+96 = 3’794. Die gemessene Ersparnis liegt in der erwarteten Spanne 3’415–4’100. T04 spart 32 statt der geschätzten 35–50 Wörter, weil die grundlegende Buy-and-Hold-Erklärung vollständig bleibt. A01 spart 339 statt der Beispielersparnis 348: Neun zusätzliche Wörter halten die tatsächliche wesentliche KI-Integration und Testarbeit ausdrücklich sichtbar. Mehrere andere Massnahmen bleiben bewusst am unteren Schätzrand. Besonders die Trend-/BIP-Regeln in der Methodik und notwendige Quellen-/Interpretationsgrenzen wurden nicht zugunsten einer Zielzahl weiter komprimiert.

### Zuordnung zu Originalzellen

Die folgenden IDs sind die im Plan abgegrenzten ursprünglichen Massnahmenblöcke; sie bezeichnen auch erhaltene Kontext-/Formelzellen innerhalb eines Blocks. Die Aufzählung bedeutet nicht, dass jede genannte Zelle verändert wurde. Ausgelagerte Originalzellen behalten ihre IDs, geteilte technische Auszüge erhalten eigene neue IDs. Die drei neuen Überblicks-Prosa-/Aufbauzellen werden ausschliesslich P01 zugerechnet.

- **P01** – `index.ipynb`: `3533c085`, `5cc38f47`, `845cba4b`, `c73c89c7`, `7dd61677`, `3d335647`, `151c337e`, `e7e0fc70`, `99be5e48`, `c5c67308`, `ae9ec038`, `07151010`, `a0ace267`, `f2c504cd`, `e0eaae76`, `f859a9ec`, `6b75ab19`, `41b584e0`, `830ece39`, `725443c8`, `ddad650d`, `17476257`, `ef2baad3`, `876b0021`, `da89528d`, `6f782e72`, `b99cf154`, `01b061a8`, `4b93919d`, `310a8c1b`, `d23b699a`, `8389728d`, `68c70d93`, `c1515f6e`, `0f54cf80`, `7c098ca4`, `3acfa996`, `5c023149`.
- **E01** – `notebooks/Einleitung.ipynb`: `22d65606`, `686a445a`, `46680b47`.
- **E02** – `notebooks/Einleitung.ipynb`: `a9f0792b`, `f733daa1`, `35ed2729`.
- **E04** – `notebooks/Einleitung.ipynb`: `5f03e85d`, `48171093`.
- **T02** – `notebooks/Theorie.ipynb`: `d507a001`, `d507a002`, `cecc3300`, `b6316a3d`, `d507a004`.
- **T03** – `notebooks/Theorie.ipynb`: `d508a001`, `c269ad7f`, `d508a002`, `bdef1563`.
- **T04** – `notebooks/Theorie.ipynb`: `d509a001`, `d509a002`, `8e1550f8`.
- **T05** – `notebooks/Theorie.ipynb`: `d510a001`, `990d4cd6`, `d510a002`.
- **T06** – `notebooks/Theorie.ipynb`: `d511a001`, `d8350873`, `d511a002`, `035b1ffe`.
- **T07** – `notebooks/Theorie.ipynb`: `005fce46`, `86c17661`, `c8856345`, `7e670f16`, `e1888b20`.
- **T08** – `notebooks/Theorie.ipynb`: `4670f764`, `6a341a65`, `6889baa6`, `c70a36fd`.
- **T09** – `notebooks/Theorie.ipynb`: `6214eedc`, `0a5b52df`, `f2cafbc8`, `32e3c634`, `8fd22c41`, `10386aae`, `22fec44e`, `03486f6b`, `ae9df1ec`, `5a028097`.
- **T10** – `notebooks/Theorie.ipynb`: `d501a001`, `bff7db06`, `3a60969c`, `d501a002`, `2e6c469f`, `d501a004`, `83fd3049`, `f17d8f57`.
- **T11** – `notebooks/Theorie.ipynb`: `d506a001`, `d506a002`, `909f608f`, `52959a27`, `6e2866c3`, `d506a004`.
- **T12** – `notebooks/Theorie.ipynb`: `d512a001`, `c68fa307`, `d512a002`, `0c76df80`, `2d7aee16`, `d512a004`.
- **T13** – `notebooks/Theorie.ipynb`: `d513a001`, `d513a002`, `d513a003`, `d513a004`.
- **M01** – `notebooks/Methodik.ipynb`: `a233bc87`, `35c815dc`, `053fb431`.
- **M02** – `notebooks/Methodik.ipynb`: `873c66a1`, `38cbd5f3`, `1a52a943`, `563f04bb`, `8433fb9b`, `18279f6c`, `2565f88a`.
- **M03** – `notebooks/Methodik.ipynb`: `09fe7307`, `b1b5cc99`, `501e6677`, `f3204f93`, `60c85505`, `f672bdf5`, `e77f7db8`.
- **M04** – `notebooks/Methodik.ipynb`: `a6b32280`, `e6ecde1b`, `62d2a3bd`, `0af0c786`.
- **A01** – `notebooks/Analyse.ipynb`: `c50744c1`, `7375ca9d`, `548ffdcf`, `082f8e37`, `2b5f1700`, `3cd4f923`, `2ea901f9`, `a0492744`, `99bcfb9b`.
- **A03** – `notebooks/Analyse.ipynb`: `762a3ac1`.
- **A04** – `notebooks/Analyse.ipynb`: `c24d259b`, `cbfcb887`, `e433fc51`, `a1781f55`, `3873238c`.
- **A05** – `notebooks/Analyse.ipynb`: `5e6f5c1d`, `7b9386c9`, `406de6ae`, `663b04db`, `c72a0269`, `937d4e0c`, `04f51bb8`.
- **A06** – `notebooks/Analyse.ipynb`: `14bdd732`, `efe3b129`, `37207665`, `5d011745`, `8c5b7b44`.
- **A07** – `notebooks/Analyse.ipynb`: `a0dcceaa`, `34d0cf2f`, `9bc04a5f`.
- **A08** – `notebooks/Analyse.ipynb`: `31fc788f`, `b2a49f5f`, `9e97be94`, `d4298767`.
- **A09** – `notebooks/Analyse.ipynb`: `e3ace74b`, `4e93dcd6`, `e2aa1e8c`, `e596730b`.
- **A10** – `notebooks/Analyse.ipynb`: `6f8b54af`, `b18171a7`, `89a22011`, `fee3f6b2`, `dad07e04`, `cf893ea2`.
- **A11** – `notebooks/Analyse.ipynb`: `ce8d331f`, `265fbf59`.
- **A12** – `notebooks/Analyse.ipynb`: `fd261ff9`, `e7844120`, `8c8859cc`, `4d5be989`, `19427df9`, `7b50e1bd`, `2d5c11d2`, `901e41cd`.
- **A13** – `notebooks/Analyse.ipynb`: `d49a8f28`, `b0ea1a50`, `1f781a01`, `9f463bb8`.
- **A14** – `notebooks/Analyse.ipynb`: `dd8fed61`, `52fbe760`, `3bb184b5`, `c7f40801`, `570e592d`, `f38848d3`, `dfd4709d`, `0f706c75`.
- **A15** – `notebooks/Analyse.ipynb`: `e566eb52`, `304ab9af`, `f384a979`, `c4dac399`, `686c6388`.
- **A16** – `notebooks/Analyse.ipynb`: `096fba73`, `a981fff3`, `d943f6ea`, `d7d0e101`, `34f02b9f`, `dffffe93`, `8f9ef237`.
- **A17** – `notebooks/Analyse.ipynb`: `2631d055`, `8af54f16`, `e33f8b0b`, `33d92987`, `0d5526ed`.
- **A18** – `notebooks/Analyse.ipynb`: `ee619640`, `d6e33122`, `59efb4f5`, `83fc757b`, `3ef40ec9`.
- **A19** – `notebooks/Analyse.ipynb`: `6402a9d2`, `a3e4beef`, `1f328fd6`.
- **A20** – `notebooks/Analyse.ipynb`: `6999a6d3`, `3972ae55`, `2b837f9a`.
- **A21** – `notebooks/Analyse.ipynb`: `c48ec4c3`, `8f8b4803`, `f9f6f912`, `4b05781f`.
- **A22** – `notebooks/Analyse.ipynb`: `3425064c`, `928fe97f`, `3337f340`, `8ee3e2ad`, `f7382b02`, `01923a4a`, `369f9481`, `3df49dc6`.
- **A23** – `notebooks/Analyse.ipynb`: `709af16c`, `ab95d9b8`, `82391240`, `e7f2d428`, `6a27a355`, `10761822`, `53354686`, `4b5d4890`.
- **A24** – `notebooks/Analyse.ipynb`: `bc770851`, `dfc835b7`, `b7c30f4b`, `8b805c66`, `9a3b2312`, `77126f6b`, `4001dccf`.
- **A25** – `notebooks/Analyse.ipynb`: `7012cb90`, `ef66a225`, `f4051b34`, `2285674e`.
- **F01** – `notebooks/Fazit.ipynb`: `ed6169f5`, `d59cbe8c`, `4ac7465f`.
- **F03** – `notebooks/Fazit.ipynb`: `53c9f636`, `b3aa03a1`, `c6d53830`.

## 4. Technische Auslagerungen und Schutz historischer Angaben

**P01 nach A.7:** A.7.1 erhält Installation, Quarto, Zotero/Better BibTeX, Zitieren, Kapitel-/Notebook-/Projektstruktur und KI-Hinweise; A.7.2 die damalige Quellen-/Werkzeugplanung mit acht Quellengruppen und Bibliotheken; A.7.3 die ursprünglichen Notebook-Pendenzen einschliesslich sämtlicher Häkchen und Termine. Veraltbare Angaben sind ausdrücklich historischer dokumentierter Stand. Sie wurden weder modernisiert noch mit der älteren README-Pendenzenliste überschrieben. Titel-/Autorhinweis und technische Originalbeispiele sind erhalten. Überschriften wurden an die Anhangshierarchie angepasst. Kapitel 1 behält seinen Titel, beide Raw-Zellen und seine wortgleiche Forschungsfrage.

**README-Regel:** Die sechs alten Übertragungsschritte in `documentation/readme-ueberblick-sync.md` bleiben als historischer Vorgang erhalten. Ein neuer Hinweis trennt die wissenschaftliche Überblicksseite von A.7 und untersagt künftiges automatisches vollständiges Wiederauffüllen von `index.ipynb`. Neue Notebook-Pendenzen dürfen nicht durch alte README-Häkchen ersetzt werden. Die README selbst bleibt byteidentisch; andere historische Nachweise wurden nicht überarbeitet.

| Massnahme | Neues Ziel | Übertragen | Im Haupttext ausdrücklich behalten |
|:---|:---|:---|:---|
| T07 | B.3.3 | pandas-Biografie, vollständige historische Aliasliste samt Quellen, vereinfachte API-Zeile, API-Einleitung und `to_datetime`-Beleg | Zeitreihen/Frequenzen/Downsampling, wissenschaftliche Bedeutung, originaler Foresight-Absatz; ausführbare Beispielzelle samt Output bleibt physisch in Theorie |
| A06 | B.3.2 | Originalabsatz zu `period_frequency="ME"`, `periods_per_year=12` und protokollierten Quelltagen | Monatliche Bewertung/Annualisierung, echter gemeinsamer Schlussstand, keine Interpolation, zwölf Perioden und begrenzter MDD |
| A09 | B.5.1 | Zwei technische Sätze zu Dateifeldern/Monatsgrenzen/ursprünglicher Zinsbeobachtung | RF-Verfügbarkeit, Prozent→Dezimal, Kalendertage/365, sieben Tage, Beispiel 0,2548 %, Approximation und RF≠unverzinste Cash-Position |
| A10 | B.4.1 und B.5.2 | Vollständiger damaliger WEO-Vorprüfabsatz; separater Satz zu Ausgabe, Originaldatei, Hash und Veröffentlichungsbeleg | NGDPD-Einheit, tatsächliche Vorjahre, keine Prognosen, gemeinsamer verfügbarer Jahrgang, damalige Vintage, Veröffentlichung+1, kein Rückdatieren heutiger Revisionen |
| A12 | C.3.1 | Originalsatz Python 3.14.0/NumPy 2.3.5/pandas 2.3.3 | Laufdatum 10.10.2026, Engine 1.0.0, Commit `1954bfb`, unveränderter Arbeitsstand, fünf Läufe/elf Portfolioreihen/Perioden-/Vorlaufnachweise |
| A13 | A.6.2 | Vollständiger technischer Absatz zur Quellen-/Dateipfad-Prüfkette der Ergebnisbilder | Ergebnisdefinition, nominale USD-Interpretation, Rundung/Monatsgrenze, sämtliche sieben Ergebnisgrafiken |

Bei gemischten Zellen wurden nur klar abgegrenzte technische Originalteile übernommen. B.4.1 bezeichnet den alten Vorprüfabsatz ausdrücklich als damaligen Planungsstand, nicht als neue Behauptung über den bereits abgeschlossenen Studienlauf. B.3.3 bezeichnet die Aliasübersicht als historischen Stand; die alten Aliase und der offene Seitenbeleg R-009 bleiben unverändert. Kein Python-Code wurde verschoben oder neu ausgeführt.

### Vollständiger Transfernachweis

46 Transferdatensätze dokumentieren Originalzellen beziehungsweise abgegrenzte Originalauszüge; diese Zahl ist von den 46 freigegebenen Massnahmen zu unterscheiden. Der technische Körper jeder Ganzzellenübernahme ist identisch, abgesehen von erlaubten aktiven Kapitelverweisen. Überschriften sind an die Anhangshierarchie angepasst. Geteilte Auszüge stimmen zeichengetreu mit den abgegrenzten Originalteilen überein. Keine Originalübernahme wurde doppelt eingefügt; jede ID existiert im aktuellen Buch genau einmal.

| Originaldatei / Zelle oder Teil | Zielnotebook / ID | Art |
|:---|:---|:---|
| `notebooks/Analyse.ipynb` / `1f781a01` | `notebooks/Anhang_Technische_Engine.ipynb` / `1f781a01` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `3533c085` | `notebooks/Anhang_Technische_Engine.ipynb` / `3533c085` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `c73c89c7` | `notebooks/Anhang_Technische_Engine.ipynb` / `c73c89c7` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `7dd61677` | `notebooks/Anhang_Technische_Engine.ipynb` / `7dd61677` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `3d335647` | `notebooks/Anhang_Technische_Engine.ipynb` / `3d335647` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `151c337e` | `notebooks/Anhang_Technische_Engine.ipynb` / `151c337e` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `e7e0fc70` | `notebooks/Anhang_Technische_Engine.ipynb` / `e7e0fc70` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `99be5e48` | `notebooks/Anhang_Technische_Engine.ipynb` / `99be5e48` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `c5c67308` | `notebooks/Anhang_Technische_Engine.ipynb` / `c5c67308` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `ae9ec038` | `notebooks/Anhang_Technische_Engine.ipynb` / `ae9ec038` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `07151010` | `notebooks/Anhang_Technische_Engine.ipynb` / `07151010` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `a0ace267` | `notebooks/Anhang_Technische_Engine.ipynb` / `a0ace267` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `f2c504cd` | `notebooks/Anhang_Technische_Engine.ipynb` / `f2c504cd` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `e0eaae76` | `notebooks/Anhang_Technische_Engine.ipynb` / `e0eaae76` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `f859a9ec` | `notebooks/Anhang_Technische_Engine.ipynb` / `f859a9ec` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `6b75ab19` | `notebooks/Anhang_Technische_Engine.ipynb` / `6b75ab19` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `41b584e0` | `notebooks/Anhang_Technische_Engine.ipynb` / `41b584e0` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `830ece39` | `notebooks/Anhang_Technische_Engine.ipynb` / `830ece39` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `17476257` | `notebooks/Anhang_Technische_Engine.ipynb` / `17476257` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `ef2baad3` | `notebooks/Anhang_Technische_Engine.ipynb` / `ef2baad3` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `876b0021` | `notebooks/Anhang_Technische_Engine.ipynb` / `876b0021` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `da89528d` | `notebooks/Anhang_Technische_Engine.ipynb` / `da89528d` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `6f782e72` | `notebooks/Anhang_Technische_Engine.ipynb` / `6f782e72` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `b99cf154` | `notebooks/Anhang_Technische_Engine.ipynb` / `b99cf154` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `01b061a8` | `notebooks/Anhang_Technische_Engine.ipynb` / `01b061a8` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `4b93919d` | `notebooks/Anhang_Technische_Engine.ipynb` / `4b93919d` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `310a8c1b` | `notebooks/Anhang_Technische_Engine.ipynb` / `310a8c1b` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `d23b699a` | `notebooks/Anhang_Technische_Engine.ipynb` / `d23b699a` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `8389728d` | `notebooks/Anhang_Technische_Engine.ipynb` / `8389728d` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `68c70d93` | `notebooks/Anhang_Technische_Engine.ipynb` / `68c70d93` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `c1515f6e` | `notebooks/Anhang_Technische_Engine.ipynb` / `c1515f6e` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `0f54cf80` | `notebooks/Anhang_Technische_Engine.ipynb` / `0f54cf80` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `7c098ca4` | `notebooks/Anhang_Technische_Engine.ipynb` / `7c098ca4` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `3acfa996` | `notebooks/Anhang_Technische_Engine.ipynb` / `3acfa996` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `5c023149` | `notebooks/Anhang_Technische_Engine.ipynb` / `5c023149` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `725443c8` | `notebooks/Anhang_Technische_Engine.ipynb` / `725443c8` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `index.ipynb` / `ddad650d` | `notebooks/Anhang_Technische_Engine.ipynb` / `ddad650d` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `notebooks/Theorie.ipynb` / `005fce46` | `notebooks/Anhang_Datenaufbereitung.ipynb` / `978bbfca` | Pandas-Biografie und historische Aliasübersicht |
| `notebooks/Theorie.ipynb` / `86c17661` | `notebooks/Anhang_Datenaufbereitung.ipynb` / `86c17661` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `notebooks/Theorie.ipynb` / `c8856345` | `notebooks/Anhang_Datenaufbereitung.ipynb` / `c8856345` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `notebooks/Theorie.ipynb` / `7e670f16` | `notebooks/Anhang_Datenaufbereitung.ipynb` / `7e670f16` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `notebooks/Analyse.ipynb` / `5d011745` | `notebooks/Anhang_Datenaufbereitung.ipynb` / `5d011745` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `notebooks/Analyse.ipynb` / `e596730b` | `notebooks/Anhang_Datenaufbereitung.ipynb` / `f8419d01` | RF-Dateifelder und Quellenbeobachtung |
| `notebooks/Analyse.ipynb` / `cf893ea2` | `notebooks/Anhang_Datenaufbereitung.ipynb` / `cf893ea2` | Originalzelle; Überschrift/aktiver Verweis falls nötig angepasst |
| `notebooks/Analyse.ipynb` / `fee3f6b2` | `notebooks/Anhang_Datenaufbereitung.ipynb` / `d675cf87` | WEO-Ausgabe, Originaldatei, Hash und Veröffentlichungsbeleg |
| `notebooks/Analyse.ipynb` / `8c8859cc` | `notebooks/Anhang_Tests_Validierung.ipynb` / `1a6efdf6` | Python-, NumPy- und pandas-Version |

## 5. Nummerierung und aktuelle Verweise

| Bisher | Jetzt |
|:---|:---|
| 5.1–5.9 technische Brückenabschnitte | **5.1 Vom Modell zur Untersuchung** |
| 5.10 Daten-/Parameterfestlegung | **5.2**, Unterabschnitte 5.2.1–5.2.9 |
| 5.11 Durchführung | **5.3**, Unterabschnitte 5.3.1–5.3.3 |
| 5.12 Ergebnisdarstellung | **5.4**, Unterabschnitte 5.4.1–5.4.5 |
| 5.13 Interpretation | **5.5**, Unterabschnitte 5.5.1–5.5.7 |

Aktuelle Verweise in Analyse, Methodik, Fazit und Anhangseinleitungen wurden angepasst. F02 nennt nun 5.4/5.5, F03 die Grenzen in 5.5.6. Hauptkapitel bleiben 1–6; Literaturverzeichnis bleibt danach vor den Anhängen A–D. Die sieben Ergebnisabbildungen und ihre Nummern bleiben vorhanden. Die neue KI-Dokumentation erscheint als D.7.

Historische Berichte, Promptkopien und bisherige KI-Nachträge behalten ihre damaligen Nummern und Wortzahlen. Die bisherigen KI-Nachträge wurden nicht umgeschrieben; D.7 erklärt den Zeitbezug. Originalcode-Kommentare behalten ausdrücklich ihre frühere Nummer `5.12`; ein Hinweis ausserhalb des Codes in A.6 ordnet sie dem heutigen Ergebnisabschnitt 5.4 zu. Die Einbindung `{{< embed Analyse.ipynb#99cad7ec echo=true >}}` und die sieben Original-Plotaufrufe sind erhalten.

Der HTML-Abgleich prüft alle Überschriften/Zielanker und ergibt keine doppelten IDs. Sichtbare Analysehauptabschnitte sind genau 5.1–5.5 mit der beschriebenen Untergliederung. Neue Anhangsziele A.6.2/A.7.1–3/B.3.3/B.4.1/B.5.1–2/C.3.1 und ihre Verweise sind aufgelöst. Alte Zahlen in historischen Belegen, technischen Identifikatoren und unverändertem Originalcode sind keine aktiven Verweisfehler.

## 6. Inhaltliche und technische Integrität

Die Ersatzbeispiele wurden am Original geprüft und an Informationsgehalt, Quellen und eigene Entscheidungen angepasst. Insbesondere wurden die Originalerklärungen zu Trend/BIP in der Methodik und mehrere Interpretationsabsätze vollständig behalten. Die Prosa wurde hinsichtlich Bedingungen, Kausalität und Übertragbarkeit verglichen; Tabellenwerte wurden nicht als Anlass genutzt, eigenständige Deutungen zu entfernen.

| Schutzbereich | Nachweis |
|:---|:---|
| Forschungsfrage/Titel | Originalfragen in Überblick, Einleitung und Fazit zeichengetreu; beide besonderen index-Raw-Zellen und Notebookmetadaten identisch |
| Strategien und Vergleichsdesign | BH, 60/40, Long/Cash und BIP-Regeln; H1/K1/Z1/S1/S2; Fondsuniversen, Zeiträume, Anfangsbewertungen, Periodenzahlen, Vorlauf, feste Hauptparameter und separate Kontrollen erhalten |
| Zeit-/Datenlogik | Monatsstand, Signalverzug, BIP-Vintage/Istjahr/gemeinsamer Datenjahrgang, Veröffentlichungsdatum+1 und RF-Vorverfügbarkeit/ACT365/Abgrenzung zu Cash erhalten |
| Kosten und Ergebnisse | Split-/Dividendenproxy, keine Doppelzählung, enthaltene versus zusätzliche Kosten, nominale USD-Ergebnisse, fehlende Inflations-/Steuerbereinigung und alle Ergebnisvergleiche erhalten |
| Mathematik | Multimengenvergleich aller **95** Markdown-Mathematikausdrücke identisch; alle zugehörigen Variablenerklärungen erhalten; Word enthält dieselben **95** OMML-Formelobjekte |
| Tabellen/Bilder | Alle **14** Markdown-Tabellenblöcke identisch, einschliesslich verschobener Aliasliste; Word enthält dieselben **23** Tabellen mit identischen Zeilendaten und **acht** Bilddateien mit identischen SHA-256 |
| Code/gespeicherte Ausgaben | Alle **28** ursprünglichen Codezellobjekte vollständig identisch, im selben Notebook und in derselben Reihenfolge: Quelle, ID, Metadaten, Execution Count, **28** Outputobjekte und **acht PNGs**; auch nach allen externen Renderläufen identisch |
| Notebookstruktur | Neun Notebooks mit **495** Zellen statt 499; JSON und nbformat-Schema gültig, alle IDs buchweit eindeutig; Differenz betrifft Markdown-Zusammenführung/-Auslagerung, keine Codezellen |
| Quellen | Alle **29** aktiven Citation Keys und **157** Vorkommen in den Notebook-Texten erhalten; Quellenbelege bleiben an den jeweiligen wissenschaftlichen Aussagen bzw. übernommenen technischen Originalen; Bibliographie/CSL unverändert |
| Sperrstellen | T01 und F04 vollständige Zellen identisch; F02 identisch nach ausschliesslich mechanischem Vergleich seiner aktuellen Kapitelverweise |
| Bekannte Fachbefunde | Betroffene Definitionen/Beispiele/Outputs wurden nicht ersatzlos beseitigt; offene R-Befunde siehe Abschnitt 9 |
| Engine/Studienartefakte | `src`, Studienkonfigurationen und alle **30** versionierten Ergebnisdateien SHA-256-identisch; keine neuen wissenschaftlichen Ergebnisse |

Codex verfasste die verdichtete Prosa und strukturelle Einleitungen. Die Modellbrücke benennt wesentliche frühere KI-Unterstützung bei Integration und künstlichen Tests. Eigene finanzwissenschaftliche Vorgaben/Untersuchungsentscheidungen werden davon getrennt dem Autor zugeordnet. Diese technische und textliche Prüfung ist **keine behauptete persönliche Autorenprüfung und keine abschliessende wissenschaftliche Freigabe**. Die Eingangs-/Sharpe-Nachweisgrenze aus R-017 bleibt bestehen; die Studie wurde nicht neu gerechnet.

## 7. Vollständige Renderprüfung in externer Kopie

Alle Renderbefehle liefen ausschliesslich im vorab vollständig kopierten Ordner `C:\Users\modic\AppData\Local\Temp\codex-kuerzung-stufe1-2026-10-12-uj0waob4\render-project`; Ausgabeziel ausschliesslich dessen `_book`. Vor jedem Start wurden tatsächliches `Get-Location`, `output-dir: _book`, deaktivierte Ausführung und deaktiviertes Freeze geprüft. Nur in dieser Kopie wurden `execute.enabled: false` und `freeze: false` gesetzt; die ursprüngliche `_quarto.yml` bleibt identisch. Notebook-Code wurde auch beim Plotcode-Embedding nicht ausgeführt.

Die abschliessenden vollständigen Befehle:

```text
quarto render --to html --no-execute --no-cache
quarto render --to pdf --no-execute --no-cache --no-clean -M latex-auto-install:false -M latex-clean:false -M keep-tex:true
quarto render --to docx --no-execute --no-cache --no-clean
```

| Prüfung | Tatsächliches Ergebnis |
|:---|:---|
| HTML | Exit **0**, alle elf Buchdateien gerendert; **1’764** lokale `href`-/`src`-/Ankerziele geprüft, **0** Fehlziele, **0** doppelte IDs; Navigation, aktuelle Überschriften, neue Anhangsziele, Bibliographie und D.7 geprüft |
| Quarto/LuaLaTeX-PDF | Exit **0**, **108** Dateiseiten; keine LaTeX-Fehler, fehlenden Zeichen oder undefinierten Verweise/Zitationen; keine Paketinstallation |
| Quarto-DOCX | Exit **0**, projektübliche DOCX-Nachbearbeitung erfolgreich; keine Formelkonvertierungswarnung; 95 Formeln/23 Tabellen/8 Bilder gegen Ausgangs-DOCX identisch |
| Zusätzlicher paketierter DOCX-Prüfrenderer | **Fehlgeschlagen**: `render_docx.py`, Exit **1**, `FileNotFoundError: LibreOffice soffice.exe was not found on PATH`. LibreOffice wurde nicht installiert; dieser Prüfschritt wird nicht als bestanden ausgegeben |
| Microsoft-Word-Ersatzprüfung | Installiertes Word in eigener unsichtbarer Instanz, DOCX **schreibgeschützt**, Felder/Inhaltsverzeichnis nur im Speicher aktualisiert, neu paginiert und als Prüf-PDF exportiert: **93** Dateiseiten. Dokument ohne Speichern geschlossen; DOCX bleibt unverändert |

Für PDF und den tatsächlichen Word-Prüfexport wurden sämtliche Seiten mit Poppler als PNG gerastert und alle Seitenübersichten angesehen. Detailprüfungen betreffen besonders Überblick/Forschungsfrage, Modellbrücke, Formeln/Variablen, Tabellen und sieben Resultatgrafiken, Literaturverzeichnis, A.6/A.7, B.3.3/B.4.1/B.5, C.3.1 und den neuen KI-Nachtrag. Nach einer Straffung ausschliesslich des neuen KI-Nachtrags wurden alle drei Formate vollständig erneut gerendert; der kurze isolierte Schlussrest auf einer zusätzlichen PDF-Seite entfällt. Haupttextzählung und sämtliche Fachquellen blieben dabei gleich. Das ist eine vollständige Seitenübersicht mit gezielten Detailansichten, keine behauptete Sichtprüfung jedes Zeichens jeder Seite bei 100 % Zoom.

Kapitelanfänge, Seitenzahlen und Anhangshierarchie sind nachvollziehbar. Das Literaturverzeichnis liegt im PDF auf Dateiseiten 64–66, in Word auf 58–59, jeweils vor Anhang A. Im Word-Prüfexport läuft der unveränderte Schluss von F04 auf Dateiseite 57 weiter; wegen der Sperre wurde daraus keine zusätzliche Textkürzung abgeleitet. In der PDF bleiben **21 Layout-Hinweise**: zwölf `Overfull hbox` mit jeweils nur 0,11806 pt Überbreite sowie neun `Underfull`-Hinweise. Die geprüften Darstellungen zeigen keine abgeschnittenen Tabellen, fehlenden Formeln/Bilder oder Überlagerungen. Vorhandene globale Formatregeln wurden nicht geändert.

### Vollständige verbleibende LaTeX-Layoutmeldungen

```text
Underfull \vbox (badness 10000) detected at line 1454
Underfull \vbox (badness 10000) detected at line 1454
Overfull \hbox (0.11806pt too wide) in alignment at lines 2703--2721
Overfull \hbox (0.11806pt too wide) in alignment at lines 2721--2723
Overfull \hbox (0.11806pt too wide) in alignment at lines 2723--2732
Overfull \hbox (0.11806pt too wide) in alignment at lines 2817--2835
Overfull \hbox (0.11806pt too wide) in alignment at lines 2835--2837
Overfull \hbox (0.11806pt too wide) in alignment at lines 2837--2842
Overfull \hbox (0.11806pt too wide) in alignment at lines 2890--2908
Overfull \hbox (0.11806pt too wide) in alignment at lines 2908--2910
Overfull \hbox (0.11806pt too wide) in alignment at lines 2910--2917
Overfull \hbox (0.11806pt too wide) in alignment at lines 2985--3003
Overfull \hbox (0.11806pt too wide) in alignment at lines 3003--3005
Overfull \hbox (0.11806pt too wide) in alignment at lines 3005--3012
Underfull \hbox (badness 4713) in paragraph at lines 3402--3408
Underfull \vbox (badness 10000) detected at line 4409
Underfull \vbox (badness 10000) detected at line 4409
Underfull \vbox (badness 10000) detected at line 4409
Underfull \vbox (badness 10000) detected at line 4409
Underfull \vbox (badness 10000) detected at line 4409
Underfull \vbox (badness 10000) detected at line 4409
```

Die HTML-Prüfung betrifft lokale Ziele. Externe URLs wurden in diesem Auftrag nicht erneut über das Netz aufgerufen. Die Datei- und Seitenzahl des Word-Prüfexports hängt vom vorhandenen Microsoft Word ab; der fehlgeschlagene LibreOffice-Schritt bleibt eine ausdrücklich benannte Prüfeinschränkung.

## 8. Verbleibender Umfang und nächste Stufe

| Bezugsgrösse | Verbleibende notwendige Kürzung |
|:---|---:|
| 8’000, Haupttext mit Überblick | **948** |
| 8’000, Haupttext ohne Überblick | **823** |
| 7’700 Planungsziel, mit Überblick | **1’248** |
| 7’700 Planungsziel, ohne Überblick | **1’123** |

Diese Lücke wurde nicht durch zusätzliche, unfreigegebene Kürzungen geschlossen. Eine zweite Stufe benötigt einen eigenen gezielten Beschluss. Konkrete Prüfstellen dafür:

1. **Theorie 3.1.2–3.1.6 und 3.2.3–3.2.6:** Wiederholte Risiko-/Vergleichshinweise zwischen Strategieerklärungen und Kennzahlen bündeln. Indexfonds-/ETF-Ergänzungen T01, mathematische Voraussetzungen, Variablen, Quellen und eigenständige Begriffsabgrenzungen bleiben geschützt. Kürzerer Code oder entfernte Tabellen sparen nach dieser Methode keine Prosa.
2. **Analyse 5.2 gegenüber Methodik 4.2/4.3:** Doppelte Erläuterungen derselben Vorabfestlegung, Fondsrollen und Vergleichsgrenzen genau gegenüberstellen. Jede zentrale Regel muss an einer klar verweisbaren Stelle im Haupttext ausführlich bleiben; die Markt-/Zeit-/Gewichtungsunterschiede und Datenverfügbarkeit dürfen nicht auf blosse technische Anhänge reduziert werden.
3. **Analyse 5.4/5.5:** Verbleibende Tabellenwert-Wiederholungen und wiederholte Ergebnisüberleitungen prüfen, insbesondere H1, K1 und Sensitivität. Wirkliche Deutung, konkrete Signal-/Rebalancing-Beispiele und Einschränkungen behalten. Kein isolierter Schluss «beste Strategie» aus einer gekürzten Rangliste.
4. **Grenzen 3.3/4.4/5.5.6/6.3:** Gleiche Grenzen geordnet zusammenführen und mittels Verweisen verbinden, ohne ihre Bedeutung für Theorie, Ergebnisinterpretation und Fazit zu verlieren. F02/F04 werden in dieser Stufe weiterhin nicht als Kürzungsreserve behandelt.

Diese Hinweise sind noch keine gezählten Massnahmen und keine Zusicherung, dass alle 948 beziehungsweise 1’248 Wörter sicher einsparbar sind. Ein zweiter Plan muss Informationsvergleich und tatsächliche Messung erneut leisten. Die Fachkorrekturen aus Phase 2 bleiben davon getrennt.

## 9. Offene Fachkorrekturen aus Phase 2

Der alte Gegenlesebericht bleibt unverändert. Seine Befunde wurden nicht durch Löschen der betroffenen Passage verdeckt. Auslagerung kann den Ort oder die historische Kennzeichnung ändern, ersetzt aber keine fachliche Berichtigung.

| Befund | Stand nach Stufe 1 |
|:---|:---|
| R-001 Portfolio-Beispielvolatilität | Gespeicherter Wert und Beispielcode unverändert; spätere gezielte Korrektur offen |
| R-002 Haupttextumfang | Deutlich reduziert, aber 8’000 weiterhin um 948 Token einschliesslich Überblick überschritten; Zähl-/Schulfreigabe und zweite Stufe offen |
| R-003 falsches Kommer-Werk/Seiten | Betroffene ETF-/Indexpassagen in T01 unverändert; Quellenkorrektur offen |
| R-004 60/40-Anfangsgewichte | Formel und ihre ursprüngliche Erklärung unverändert; Präzisierung der Anfangsbedingung offen |
| R-005 lokale Drawdown-Referenzfunktion | `src` unverändert; Abgrenzung/Korrektur offen, keine Engine-Änderung |
| R-006 QuantStats-Erholungszeit | Originalcode, gespeicherte Ausgabe und betroffene Zeitdeutung erhalten; fachliche Korrektur offen |
| R-007 S&P-500-Auswahlbeschreibung | T01 gesperrt und unverändert; spätere Fachkorrektur offen |
| R-008 historische KI-Loglücken | Aktueller Einsatz vollständig ergänzt, wesentliche Rolle in neuer Modellbrücke sichtbar; alte fehlende Originaleinsätze nicht erfunden/nachgetragen |
| R-009 `to_datetime`-Seitenlocator | Originalbeleg unverändert nach B.3.3 übertragen; falscher Locator nicht still berichtigt |
| R-010 arithmetisches Monatsmittel | Betroffene gespeicherte Illustration/Erklärung unverändert; fachliche Präzisierung offen |
| R-011 alte pandas-Aliase | Vollständige Liste nach B.3.3 übertragen und ausdrücklich historisch eingeordnet; keine Aktualisierung/Versionsprüfung behauptet |
| R-012 Autorenkontrollstand | Neuer Einsatz als noch nicht vom Autor geprüft markiert; frühere Kontrollangaben bleiben historisch und weiterhin separat zu klären |
| R-013 doppelter Gegenrechnungsabsatz | Beide Originalabsätze im technischen Nachweis C.3 erhalten; keine unerlaubte Doppelungsbereinigung |
| R-014 altes QMD-Gerüst/Planungsstand | Originalangaben vollständig in A.7 historisch eingeordnet; kurzer aktueller Überblick gemäss P01. Historische Angaben bleiben erhalten, README nicht allgemein überarbeitet |
| R-015 Inflationsmittel als Schwelle | Betroffene ursprüngliche Theoriezelle unverändert; fachliche Präzisierung offen |
| R-016 formale Abgabeteile | Titel-/Abstract-/Verzeichnis-/Eigenständigkeitserklärungsaufgaben weiter offen; keine Angaben/Unterschrift erfunden |
| R-017 fehlende Originaleingaben | Nachweisgrenze unverändert; keine vollständige unabhängige Raw-/Sharpe-Prüfung oder Datenverlustbehauptung, keine Ersatzbeschaffung |

## 10. Endkontrolle, KI-Nachweis und Stopppunkt

Geändert wurden ausschliesslich die neun vorhandenen Notebook-Quellen, die minimale Synchronisationsanweisung, der angehängte KI-Buchnachtrag und eine neue Logzeile; neu sind dieser Bericht und die unveränderte Promptkopie. Von den 83 ursprünglich versionierten Dateien sind **71 byteidentisch**, genau zwölf autorisierte Bestandsdateien unterscheiden sich. Von den insgesamt 154 gesicherten Arbeitsdateien bleiben **142 byteidentisch**. Alle **70** ursprünglichen `_book`-/`_freeze`-/`.quarto`-Dateien und deren Inventar sind unverändert; keine neue Ausgabedatei wurde im Schreibrepository erzeugt. Die vollständige externe Ausgangssicherung ist weiterhin byteidentisch.

`_quarto.yml`, README, Bibliographie, CSL, Filter/Styles/Word-Referenzvorlage, Engine-Referenzdateien, Studienkonfigurationen, eingefrorene Ergebnisse und alle alten Berichte/Promptkopien bleiben erhalten. Bisherige Bytes von KI-Log und KI-Buchdokumentation sind unveränderte Präfixe der aktuellen Dateien. HEAD, Branch und Git-Index sind identisch zum Ausgangsstand; nichts gestaged.

Der aktuelle Einsatz ist nach den vorhandenen KI-Regeln in `documentation/ai-usage/ai-usage-log.md` und D.7 abgeglichen. Technische Originalauslagerung, Strukturänderung und KI-gestützte sprachliche Verdichtung sind getrennt beschrieben. Keine neue wissenschaftliche Ergebnisarbeit und keine persönliche Autorenfreigabe werden behauptet.

Prüfmanifest, Massnahmen-/Transferzählungen, Originalhashes, Renderprotokolle und Seitenbilder liegen nur im externen Prüfverzeichnis `C:\Users\modic\AppData\Local\Temp\codex-kuerzung-stufe1-2026-10-12-uj0waob4`. Dieser Bericht enthält die wesentlichen Ergebnisse und Grenzen unabhängig vom Fortbestand dieser temporären Dateien.

**STOPP zur Autorenkontrolle.** Inhaltliche Prüfung der gekürzten Fassung und Entscheidung über eine zweite Stufe stehen aus.
