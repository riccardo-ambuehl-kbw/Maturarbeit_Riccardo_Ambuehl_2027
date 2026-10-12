# Wissenschaftlich begründeter Kürzungsplan für den Haupttext

12. Oktober 2026 (Europe/Zurich). Verfasser: Codex. **Planungsstand; keine Kürzung umgesetzt, keine Autorenfreigabe behauptet.**

## 1. Ergebnis und Zielkonflikt

Der Haupttext umfasst bestätigt **12’742 Wort-/Zahlentoken einschliesslich Überblick** bzw. **11’886 ohne Überblick**. Für 7’700 wären 5’042 Wörter weniger nötig. Der hier auf konkrete Textbereiche begrenzte Plan ergibt **3’600–4’355 Wörter Einsparpotenzial** und somit **8’387–9’142 Wörter** Haupttext. Als Planungsgrössen sind dies ungefähr **3’600–4’350 Wörter Einsparung und 8’400–9’100 verbleibende Wörter**; die Intervallgrenzen sind Summen von Schätzungen, keine Genauigkeitsbehauptung.

**7’700 Wörter lassen sich mit diesen Massnahmen noch nicht wissenschaftlich sicher zusichern.** Selbst am oberen Ende des Potenzials fehlen dafür 687 Wörter, am unteren 1’442. Auch 8’000 wird um 387–1’142 überschritten. Zentrale Methodik oder eigene Ergebnisdeutung wird deshalb nicht als «technisch» ausgelagert. Eine spätere zweite Verdichtungsstufe braucht konkrete neue Fassungen und eine Autorenentscheidung; sie ist hier nicht als bereits verfügbare Einsparung angerechnet.

Die klare erste Priorität ist der technische Überblick. In der Analyse bringen die Zusammenführung der Modellbrücke, die wiederholten Einleitungs-/Definitionspassagen und Tabellen-Nacherzählungen mehr als die schon kurze Durchführung. Theorie und Fazit werden behutsamer behandelt: Lehrerergänzungen, Variablenerklärungen und persönliche Reflexion haben Vorrang.

## 2. Prüfstand und Arbeitsgrenzen

Arbeitsort: `C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027`. Tatsächlicher Branch: **dev**. HEAD: **32965a78543c641ff2bf3755c1987678843c829d**, identisch mit dem vom Autor genannten Ausgangscommit. Zu Beginn sauberer Git-Arbeitsstand. Keine `AGENTS.md` im Repository oder den geprüften übergeordneten Verzeichnissen.

Alle sechs Hauptkapitel, die drei technischen Anhangsnotebooks und der gesamte KI-Anhang wurden gelesen, einschliesslich Codequellen und vorhandener Textausgaben; keine Zellen ausgeführt. Zusätzlich wurden die beiden verlangten Berichte, die KI-Regeln, die Buch-Sync-Anweisung, `_quarto.yml`, das aktuelle KI-Log und die README gelesen. Die bestehende technische Auslagerung und ihre Prüfungen werden als historische Nachweise behandelt, nicht als hier erneut ausgeführter wissenschaftlicher Audit.

Die Lehrerantwort lautet gemäss dem dokumentierten Auftrag:

> Lagern Sie die technische Dokumentation, die Beschreibung der Datenaufbereitung sowie den Testbericht in den Anhang aus. Der Anhang zählt nicht zum Umfang.

Diese Erlaubnis deckt technische Anleitungen und ausführliche Verarbeitungs-/Prüfdetails. Sie deckt keine Verlagerung der wissenschaftlichen Datenwahl, Vergleichslogik oder Ergebnisinterpretation allein zugunsten der Wortzahl. In dieser Phase werden ausschliesslich dieser Plan, die vollständige Promptkopie und die sachlichen KI-Nachweise geschrieben. Hauptkapitel, Anhänge A–C, Formeln, Quellen, Code, gespeicherte Ausgaben, Daten, Resultate und Engine bleiben unverändert. Der KI-Anhang erhält nur einen neuen Nachtrag; seine früheren Abschnitte werden nicht umgeschrieben.

## 3. Zählung und belastbare Grenzen der Zahlen

Verwendet wurde dieselbe Ausschlussfolge wie im Auslagerungsbericht: nur Markdown-Fliesstext, ohne Raw/YAML, Überschriften, Markdown-Tabellenzeilen, Display-/Inline-Mathematik, Zitationsklammern, technische `@sec-...`-Kennungen, Codezellen, gespeicherte Outputs/Bildinhalte, Markdown-Codeblöcke und HTML-`pre`. HTML-Tags und Linkziele entfallen; sichtbare Linktexte, Listen, Zahlen und inline gesetzte Bezeichner zählen. Tokenregel: `\b\w+(?:[’'-]\w+)*\b`. Die Bibliographie sowie Repository-Berichte/KI-Log zählen nicht zum Haupttext. Dies ist keine abschliessend schulisch bestätigte Microsoft-Word-Zählung.

Für die unten vollständig formulierten Beispiele wurden Originalblock und Vorschlag tatsächlich gezählt. Alle anderen Massnahmen haben vorsichtige Intervalle; es existiert dafür noch keine fertige Ersatzfassung. **SICHER** bezeichnet die inhaltliche Entbehrlichkeit einer Wiederholung, nicht automatisch eine schon exakt gemessene Nettoersparnis. **GUT VERTRETBAR** erfordert die Prüfung der Äquivalenz, **AUTORENENTSCHEIDUNG** betrifft Schwerpunkt oder persönlichen Ausdruck. **NICHT EMPFOHLEN** hat keine angerechnete Einsparung.

| Hauptkapitel | Jetzt | Potenzial des Plans | Rest nach Umsetzung aller vorgeschlagenen Massnahmen |
|---|---:|---:|---:|
| 1 Überblick | 856 | 730 | 126 |
| 2 Einleitung | 785 | 151–171 | 614–634 |
| 3 Theorie | 3’670 | 605–860 | 2’810–3’065 |
| 4 Methodik | 1’080 | 153–198 | 882–927 |
| 5 Analyse | 5’399 | 1’751–2’111 | 3’288–3’648 |
| 6 Fazit | 952 | 210–285 | 667–742 |
| **Gesamt mit Überblick** | **12’742** | **3’600–4’355** | **8’387–9’142** |
| **Gesamt ohne Überblick** | **11’886** | **2’870–3’625** | **8’261–9’016** |

Die zehn ausformulierten Beispiele sind disjunkt und ergeben zusammen **1’687** gemessene Wörter weniger. Sie stehen vollständig oder als Teilblock bereits in den Massnahmenintervallen; ihre Summe wird **nicht zusätzlich** abgezogen. Davon sind A03 und A19 als sichere Wiederholungs-/Metakürzungen mit **226** Wörtern konkret beziffert. E04 ist sicher zu verdichten, seine 30–40 Wörter bleiben geschätzt. Alle als SICHER klassifizierten Massnahmen zusammen: **256–266**; GUT VERTRETBAR: **3’159–3’834**; AUTORENENTSCHEIDUNG: **185–255**. Ohne die Autorenentscheidungs-Massnahmen blieben **8’642–9’327** Wörter mit Überblick.

Für eine spätere Abgabefassung sollte ausserdem ungefähr **100 Wörter Reserve** für notwendige Bedingungssätze, Übergänge und fachlich getrennt freizugebende Präzisierungen vorgesehen werden. Mit dieser Reserve läge die erste Stufe ungefähr bei **8’500–9’200**. Die Reserve ist eine Planungsannahme, keine hier ausgeführte Fachkorrektur.

### Keine doppelte Anrechnung

Jede Massnahme besitzt einen eigenen, disjunkten Quellzellblock; diese Zuordnung wurde statisch geprüft. Bei gemischten Zellen bezeichnet der Block nur die vorgesehenen Prosa-/Technikteile, während Formeln, Tabellen und Code geschützt bleiben. A01 deckt 5.1–5.9 insgesamt ab; ein Wegfall der acht Überschriften wird nicht zusätzlich gezählt. Dasselbe gilt für C/D-Anteile derselben Massnahme. T09-Teil, A22-Teil und F03-Teil sind in T09/A22/F03 enthalten. Die schon erfolgte Auslagerung der 3’392 Originaltoken wird nicht ein zweites Mal abgezogen.

Zusammengeführte Überschriften, entfernte Codeanzeige und verschobene Tabellen ergeben nach dieser Zählmethode allein **null** Wörter Ersparnis. Die exakte Gegenrechnungsdoppelung in C.3 (`a4355b5e`/`008ef22e`, R-013) liegt bereits ausserhalb des Haupttexts: ihre etwaige spätere Bereinigung spart hier ebenfalls **null** und ist keine Massnahme dieses Kürzungsplans.

## 4. Massnahmen nach Kapitel

Typ A = zusätzliche technische Auslagerung; B = Zusammenführung; C = Wiederholungen; D = präzise sprachliche Verdichtung. «Heute» zählt jeweils den geschützten Quellblock mit derselben Methode; die vorgeschlagene Ersparnis betrifft nur seine zulässigen Teile. Zell-IDs sind die stabilen Anker für einen späteren Auftrag, keine Aufforderung zum pauschalen Löschen ganzer Zellen. Sämtliche Massnahmen sind noch Vorschläge.

### 1 Überblick — [Notebook](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/index.ipynb)

| ID / Typ / Priorität | Heutiger Abschnitt und Quellblock | Massnahme und Begründung | Erhaltene Hauptstelle / Schutz | Ersparnis |
|---|---|---|---|---:|
| **P01** · A/C/D · **GUT VERTRETBAR** | 1 gesamter Überblick; heute **856**. alle Markdown-Zellen | Technische Anleitung nach A.7.1, Quellen-/Werkzeugplanung nach A.7.2 und aktuelle Pendenzen nach A.7.3; README später nur verweisen. Kapitel 1 als kurze wissenschaftliche Überblicksseite mit wortgleicher Frage behalten. | Forschungsfrage in 1 und 2.2; Daten-/Quellenwahl in 4.3 und 5.10; ausführliche Nachweise in A.7 und D. | **730** (gemessen am vollständigen Beispiel) |

### 2 Einleitung — [Notebook](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Einleitung.ipynb)

| ID / Typ / Priorität | Heutiger Abschnitt und Quellblock | Massnahme und Begründung | Erhaltene Hauptstelle / Schutz | Ersparnis |
|---|---|---|---|---:|
| **E01** · D · **GUT VERTRETBAR** | 2.1 Motivation; heute **212**. `22d65606`, `686a445a`, `46680b47` | Drei Motivationsabsätze verdichten; persönliches Interesse, Risikoargument, drei Regeltypen und Informatikbezug erhalten. | Vollständiger Motivationskern bleibt in 2.1; Beispiel unten. | **106** (gemessen am vollständigen Beispiel) |
| **E02** · C/D · **GUT VERTRETBAR** | 2.2 Ziele; heute **165**. `a9f0792b`, `f733daa1`, `35ed2729` | Endwertargument und Trennung des Systems bündeln; Kennzahlen nennen, ihre Definitionen mit Theorieverweis statt erneutem Lehrabsatz. | Frage ef01feb0 unverändert; vollständige Kennzahlendefinitionen in 3.2.2–3.2.5; Investitions-/Zusammensetzungsziel bleibt. | **15–25** (geschätzt) |
| **E04** · C/D · **SICHER** | 2.4 Aufbau; heute **94**. `5f03e85d`, `48171093` | Aufbauhinweise mit Kapitel 1 abgleichen und auf kurze Orientierung zum Untersuchungsweg verdichten. Technischer Ablauf wird in A/B ausführlich erklärt. | Kapitelaufbau in P01; Übergang zu Methodik/Analyse hier kurz behalten. | **30–40** (geschätzt) |

### 3 Theorie — [Notebook](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Theorie.ipynb)

| ID / Typ / Priorität | Heutiger Abschnitt und Quellblock | Massnahme und Begründung | Erhaltene Hauptstelle / Schutz | Ersparnis |
|---|---|---|---|---:|
| **T01** · C/D · **AUTORENENTSCHEIDUNG** | 3.1.1 Finanzdaten/ETFs; heute **379**. `1941d2df` | Vorteilsaufzählung und ETF-Eignung bündeln; physische Nachbildung mit 5-%-Beispiel, Sampling, Tauschverträge und ETF-Ausschreibung erhalten. Keine pauschale Streichung des Lehrerfeedbacks. | Grundlegende Index-/Fondsunterscheidung bleibt hier; konkrete VT/IEF-Eignung in 5.10.2. R-003/R-007 separat. | **45–70** (geschätzt) |
| **T02** · C/D · **GUT VERTRETBAR** | 3.1.2 Diversifikation/Korrelation; heute **267**. `d507a001`, `d507a002`, `cecc3300`, `b6316a3d`, `d507a004` | Risikostreuung und Korrelation knapp verbinden; Spannweite, nichtlinearer Rest, Korrelation unter +1, veränderliche Korrelation und systematisches Risiko erhalten. | Korrelation von −1 bis +1, Bedeutung von 0 als fehlendem linearem Zusammenhang, Nutzen schon unter +1, Markt- versus Einzelrisiko und veränderliche Korrelationen. Formeln, Variablen und Codebeispiele bleiben in 3.1.2. | **40–60** (geschätzt) |
| **T03** · C/D · **GUT VERTRETBAR** | 3.1.3 Allokation/Rebalancing; heute **238**. `d508a001`, `c269ad7f`, `d508a002`, `bdef1563` | Driftbeschreibung kürzen und Zweck/regelhafte Anpassung in einem Absatz bündeln; Kalender-/Bandunterscheidung und jährliche eigene Wahl behalten. | Formeln, Variablen, Eigenanteil und Codes bleiben hier; Umsetzungszeitpunkte in 4.2.2. | **45–65** (geschätzt) |
| **T04** · C/D · **GUT VERTRETBAR** | 3.1.4 Buy-and-Hold; heute **183**. `d509a001`, `d509a002`, `8e1550f8` | Langfristiges Halten, Marktbreite, Ertragsreinvestition, praktische Vorteile und Verlustrisiko kompakt erklären. | Vermögensformel samt Erklärung/Quelle und Beispiel unverändert; konkrete Benchmarkfonds in 4.2.1/5.10.2. | **35–50** (geschätzt) |
| **T05** · C/D · **GUT VERTRETBAR** | 3.1.5 60/40; heute **215**. `d510a001`, `990d4cd6`, `d510a002` | Stabilisierungsabsicht und historische Grenzen sprachlich bündeln; Ländervariation, 2022 und fehlender garantierter Schutz bleiben. | Theoriebegründung hier; Quelle CFA/Kommer bleibt; Formel nicht durch Kürzung scheinbar korrigieren, R-004 separat. | **35–50** (geschätzt) |
| **T06** · D · **GUT VERTRETBAR** | 3.1.6 Ländergewichtung; heute **208**. `d511a001`, `d8350873`, `d511a002`, `035b1ffe` | Historische Gegenüberstellung und Kommers Vorbehalte zusammenziehen; MK versus BIP, Gewichtung innerhalb der Länder und fehlende Überlegenheit behalten. | Beide Formeln, Variablen und Quellen bleiben; konkrete G7-Regel in 4.2.4/5.10.8. | **35–50** (geschätzt) |
| **T07** · A/C/D · **GUT VERTRETBAR** | 3.2.1 Zeitreihen/Resampling; heute **235**. `005fce46`, `86c17661`, `c8856345`, `7e670f16`, `e1888b20` | Pandas-Biografie, Alias-/API-Anleitung und technische Beispiel-Einführung nach neuem B.3.3; Zeitordnung, Frequenzen und zeitgerechtes Downsampling kurz im Haupttext. Code physisch belassen. | Quellblock B.3.3 mit historischem Kontext; wissenschaftliche Monats-/Labelregeln weiterhin 5.10.4; R-009/R-011 separat. | **100–130** (geschätzt) |
| **T08** · D · **GUT VERTRETBAR** | 3.2.2.1–3 Rendite; heute **149**. `4670f764`, `6a341a65`, `6889baa6`, `c70a36fd` | Nur Übergänge und wiederholte Annualisierungserklärung verdichten. Keine Ersparnis für Formel-/Variablentext oder versteckten Code buchen. | Einfache, logarithmische, kumulierte und geometrische Rendite bleiben mit Formeln und Belegen hier. Nominal/real R-015 ausgespart. | **15–25** (geschätzt) |
| **T09** · C/D · **GUT VERTRETBAR** | 3.2.3 Volatilität; heute **476**. `6214eedc`, `0a5b52df`, `f2cafbc8`, `32e3c634`, `8fd22c41`, `10386aae`, `22fec44e`, `03486f6b`, `ae9df1ec`, `5a028097` | Bedeutung und Interpretation bündeln; Diversifikation mit kurzem Rückverweis auf 3.1.2; Grenze Volatilität als ein Risikotyp ausdrücklich erhalten. | Formel/Variablen, N−1, Renditen statt Preisänderung, Quadratwurzelvoraussetzung und Illustration bleiben; T09-Teil ist enthalten, nicht zusätzlich. | **80–110** (geschätzt) |
| **T10** · C/D · **GUT VERTRETBAR** | 3.2.4 Drawdown; heute **321**. `d501a001`, `bff7db06`, `3a60969c`, `d501a002`, `2e6c469f`, `d501a004`, `83fd3049`, `f17d8f57` | Doppelte Definition des Rückgangs/minimalen Wertes bündeln, Frequenz- und Zukunftsgrenze prägnant formulieren. | MDD-Zeitbereich, t/T-Erklärungen, Verlustzeichen, Ausgangswert, Erholungsdauer und Codes bleiben. QuantStats-Mehrdeutigkeit R-006 nicht wegkürzen. | **45–65** (geschätzt) |
| **T11** · C/D · **GUT VERTRETBAR** | 3.2.5 Sharpe; heute **217**. `d506a001`, `d506a002`, `909f608f`, `52959a27`, `6e2866c3`, `d506a004` | Rechenschritte nicht zugleich in Tabelle und langem Absatz erzählen; historische Deutung, Vergleichsbedingungen und Raw-Sharpe-Abgrenzung erhalten. | Formel, alle acht Zeichenerklärungen und Voraussetzungen bleiben; Tabelle kostet nach dieser Methode ohnehin keine Wörter. | **25–40** (geschätzt) |
| **T12** · C/D · **GUT VERTRETBAR** | 3.2.6 Trendfolge; heute **381**. `d512a001`, `c68fa307`, `d512a002`, `0c76df80`, `2d7aee16`, `d512a004` | Fenster-/Crossover-Erklärung und Grenzen sprachlich verdichten; Overfitting-Definition steht 3.3.3, hier kurze Anwendung. | SMA-Formel, Signalregel, Long/Short-Quelle versus eigene Long/Cash-Wahl, Gleichheit=CASH und Verzögerung bleiben. Keine Umdeutung Tages-/Monatsfenster. | **45–65** (geschätzt) |
| **T13** · C/D · **GUT VERTRETBAR** | 3.3.1–4 Methodische Grenzen; heute **343**. `d513a001`, `d513a002`, `d513a003`, `d513a004` | SMA-Beispiel und wiederholte Kostenbeispiele kurz rückverweisen; jede Bias-/Kosten-/Stichprobendefinition samt eigener Grenze bleibt eigenständig. | Allgemeine Definitionen hier; konkrete Umsetzung/Annahmen in 4 und 5.10, Auswirkung in 5.13.6. Keine methodische Auslagerung. | **60–80** (geschätzt) |

### 4 Methodik — [Notebook](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Methodik.ipynb)

| ID / Typ / Priorität | Heutiger Abschnitt und Quellblock | Massnahme und Begründung | Erhaltene Hauptstelle / Schutz | Ersparnis |
|---|---|---|---|---:|
| **M01** · C/D · **GUT VERTRETBAR** | 4.1 Untersuchungsansatz; heute **173**. `a233bc87`, `35c815dc`, `053fb431` | Einleitungsdefinition und System-/Studientrennung bündeln; Überanpassung nicht nochmals lang erklären. | Backtestansatz, vorgängige Festlegung, Theorie-/Analysebezug und dokumentierte KI-Rolle bleiben hier. | **73** (gemessen am vollständigen Beispiel) |
| **M02** · C/D · **GUT VERTRETBAR** | 4.2.1–4 Strategien; heute **407**. `873c66a1`, `38cbd5f3`, `1a52a943`, `563f04bb`, `8433fb9b`, `18279f6c`, `2565f88a` | Nur Grundbegriff-Erklärungen gegenüber Theorie reduzieren; konkrete Regeln in jedem Strategieabschnitt vollständig halten. | Alle Instrumentrollen, Drift, Jahresendtrade, fehlender Abschlusstrade, Cash=0, Lag, Warm-up, gemeinsame BIP-Istjahre und historische Versionen bleiben. | **30–45** (geschätzt) |
| **M03** · C/D · **GUT VERTRETBAR** | 4.3 Vergleichsbedingungen; heute **287**. `09fe7307`, `b1b5cc99`, `501e6677`, `f3204f93`, `60c85505`, `f672bdf5`, `e77f7db8` | Begleittext zur Lauftabelle kürzen, Datenquellen kompakt nennen und Detailbegründung nach 5.10 verweisen. | Fünf Läufe, K1≠MK, Z1-Markt-/Zeitwechsel, gleiche Termine, 100’000 USD, Monatsanfangswert, Adjustierung und WEO-Versionen bleiben. | **30–45** (geschätzt) |
| **M04** · C/D · **GUT VERTRETBAR** | 4.4 Auswertung/Grenzen; heute **213**. `a6b32280`, `e6ecde1b`, `62d2a3bd`, `0af0c786` | Kennzahlen-Rechenbeschreibung gegen 3.2 kürzen, Auswertungsprinzip und Modellgrenzen beibehalten. | Keine einzelne Rangliste, zwölf Monatsperioden, Teilperioden ohne Neustart, nominal USD, Kosten-/Steuer-/Monatsgrenzen, festgehaltener Stand und begrenzte Testaussage bleiben. | **20–35** (geschätzt) |

### 5 Analyse — [Notebook](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Analyse.ipynb)

| ID / Typ / Priorität | Heutiger Abschnitt und Quellblock | Massnahme und Begründung | Erhaltene Hauptstelle / Schutz | Ersparnis |
|---|---|---|---|---:|
| **A01** · B/C/D · **GUT VERTRETBAR** | 5.1–5.9 Modellbrücke; heute **485**. `c50744c1`, `7375ca9d`, `548ffdcf`, `082f8e37`, `2b5f1700`, `3cd4f923`, `2ea901f9`, `a0492744`, `99bcfb9b` | Eine gemeinsame 5.1 statt Einführung plus acht Kurzabschnitte; vorhandene A/B/C-Inhalte verweisen, eigene Entscheidungen und KI-Abgrenzung erhalten. | Alle wissenschaftlichen Regeln weiterhin 4 und 5.10; volle technische Erklärung bereits in A.1–5/B.1–3/C.1. Eine einzige Einsparung für gesamten Quellblock. | **348** (gemessen am vollständigen Beispiel) |
| **A03** · C/D · **SICHER** | 5.10.1 Untersuchungsentscheid; heute **214**. `762a3ac1` | Wortgleiche Frage aus 2.2, erneute Risiko-/Overfitting-Grunddefinitionen und lange Übergänge durch Verweis ersetzen. | Frage vollständig 2.2/6.1; Definitionen 3.2/3.3; Version/Tag, eigene Daten-/Parameterentscheidung und vorgängige Festlegung bleiben hier. | **133** (gemessen am vollständigen Beispiel) |
| **A04** · C/D · **GUT VERTRETBAR** | 5.10.2 Wertreihen; heute **237**. `c24d259b`, `cbfcb887`, `e433fc51`, `a1781f55`, `3873238c` | Prosa zur Instrumenttabelle verdichten; Länderaufzählung nicht zusätzlich zur Tabelle ausschreiben. | Alle neun Instrumente und Produktbelege, VT-Auflage, IEF-Zinsrisiko, USD-Börsenlinie, Proxy-/Indexwechselgrenzen und begrenzte G7-Abdeckung. Die Instrumenttabelle bleibt in 5.10.2. | **65–85** (geschätzt) |
| **A05** · C/D · **GUT VERTRETBAR** | 5.10.3 Blöcke/Vergleich; heute **331**. `5e6f5c1d`, `7b9386c9`, `406de6ae`, `663b04db`, `c72a0269`, `937d4e0c`, `04f51bb8` | Fünf Läufe mit vorhandener Tabelle erläutern statt jeden erneut vollständig aufzuzählen; eigene Zeitwahl und Kontrollzweck knapp begründen. | Januar-/Dezembergrenzen, 192/276 Perioden, eigene Zeitwahl, H1 mit verschiedenen Universen, K1 mit gleichen Fonds und 1/7 statt MK, eigenständiger Z1 sowie S1/S2 ohne nachträgliche Optimalauswahl. | **110–140** (geschätzt) |
| **A06** · A/C/D · **GUT VERTRETBAR** | 5.10.4 Monatslogik/Kapital; heute **271**. `14bdd732`, `efe3b129`, `37207665`, `5d011745`, `8c5b7b44` | Technische Konfigurationsschreibweise 5d011745 nach B.3.2; Erklärungen zur Periodenbeschriftung knapp zusammenführen. | Monatswahl und ihre Grenze, letzter gemeinsamer tatsächlicher Handelstag, rechtes Monatslabel und Quelldatum, kein Interpolieren/Auffüllen, zwölf Perioden, 100’000 USD ohne Geldflüsse, nominal USD, keine CHF-Umrechnung oder behauptete Absicherung. | **80–100** (geschätzt) |
| **A07** · C/D · **GUT VERTRETBAR** | 5.10.5 Performance/Kosten; heute **165**. `a0dcceaa`, `34d0cf2f`, `9bc04a5f` | Total-Return-Begründung kurz auf Theorie beziehen; Adjustierungs-/Kostenabgrenzung in präzisen Sätzen bündeln. | Adj Close als Proxy mit Split-/Dividendenanpassung, keine doppelte Dividende, stichprobenweiser Abgleich von Marktpreis-/NAV-Rendite sowie enthaltene Fondskosten im Gegensatz zu zusätzlichen Kosten/Steuern. | **45–65** (geschätzt) |
| **A08** · C/D · **GUT VERTRETBAR** | 5.10.6 Trendparameter; heute **200**. `31fc788f`, `b2a49f5f`, `9e97be94`, `d4298767` | Regelbeschreibung 4.2.3 kurz rückverweisen; konkrete Fenster, Datenquelle, Vorlauf und Ausführung weiterhin explizit dokumentieren. | 3/12 und ergänzend 2/12 bzw. 6/12, keine Gleichsetzung mit 200 Tagen, performance_value, elf vorgelagerte Monatsbeobachtungen bzw. 2002, Signalverzögerung/Cash=0, idealisierte Ausführung und keine nachträgliche Hauptvariante. | **55–75** (geschätzt) |
| **A09** · A/D · **GUT VERTRETBAR** | 5.10.7 RF-Reihe; heute **209**. `e3ace74b`, `4e93dcd6`, `e2aa1e8c`, `e596730b` | Dateischema/Herkunftsfelder e596730b nach neuem B.5.1; Umrechnung präzise beschreiben. | DGS3MO-Einheit/Investmentbasis, Notierung strikt vor dem anfänglichen Handelstag, Sieben-Tage-Prüfgrenze, ACT/365 und 3-%-/31-Tage-Beispiel, Modellapproximation und RF≠Cash. | **55–75** (geschätzt) |
| **A10** · A/C/D · **GUT VERTRETBAR** | 5.10.8 BIP-Verfügbarkeit; heute **349**. `6f8b54af`, `b18171a7`, `89a22011`, `fee3f6b2`, `dad07e04`, `cf893ea2` | Vorprüfchronologie cf893ea2 nach B.4.1; Hash-/Dateimetadaten in B.5.2; Auswahlregeln knapp ohne Gegenbeispiele-Wiederholung erklären. | WEO 2009–2024, NGDPD nominal in USD-Milliarden statt PPP/Wachstum, Istwerte ohne Prognosen, abgeschlossenes gemeinsames Jahr, letzte damals verfügbare Version, Veröffentlichung+1 Tag, jährliche Informationspolitik und kein Ersetzen fehlender Länder durch Null. | **100–130** (geschätzt) |
| **A11** · C/D · **GUT VERTRETBAR** | 5.10.9 Festlegungen/Grenzen; heute **113**. `ce8d331f`, `265fbf59` | Freeze-/Änderungsregel in wenige Sätze; allgemeine Vergleichsgrenzen kurz auf 4.3 und spätere Interpretation verweisen. | Festlegung vor dem Lauf, dokumentierte Änderungen, technischer Fehler im Gegensatz zu ungünstiger Rendite, getrennte H1-/Z1-Beurteilung und richtige K1-Interpretation. | **35–50** (geschätzt) |
| **A12** · A/C/D · **GUT VERTRETBAR** | 5.11 Durchführung; heute **248**. `fd261ff9`, `e7844120`, `8c8859cc`, `4d5be989`, `19427df9`, `7b50e1bd`, `2d5c11d2`, `901e41cd` | Paketversionsdetails aus 8c8859cc nach C.3.1; Roh-/Normalisierungshinweise bündeln. Die bereits kurze Durchführung bleibt eigenständig verständlich. | 10.10.2026, Engine 1.0.0 und Stand 1954bfb, fünf Läufe, 193/192 bzw. 277/276, elf Strategiereihen, identischer BIP-Pfad, getrennte VTI-Signalhistorie und unveränderter Z1-Zeitraum. | **35–55** (geschätzt) |
| **A13** · A/C/D · **GUT VERTRETBAR** | 5.12 Ergebnis-Einleitung; heute **215**. `d49a8f28`, `b0ea1a50`, `1f781a01`, `9f463bb8` | Begriffsdefinitionen knapp zurückverweisen; vollständige Dateipfad-/Hashbeschreibung aus `1f781a01` nach A.6.2. | Gerundete Tabellen auf ungerundeter Berechnung, nominal 100’000 USD, geometrische Rate im Gegensatz zu jeder einzelnen Jahresrendite, negativer Monatsdrawdown, p. a. und sieben Grafiken aus fünf Originalruns. | **107** (gemessen am vollständigen Beispiel) |
| **A14** · C/D · **GUT VERTRETBAR** | 5.12.1 H1; heute **197**. `dd8fed61`, `52fbe760`, `3bb184b5`, `c7f40801`, `570e592d`, `f38848d3`, `dfd4709d`, `0f706c75` | Tabellen-Nacherzählung verdichten, Rangfolge und Risiko-Zielkonflikt statt nochmal aller Werte schildern. | Unveränderte Tabelle, drei Grafiken und Quellen. Endwertabstand 3’781 USD, H1-Rangfolgen sowie Unterschied zwischen Volatilität und MDD bleiben als Kernbefunde. | **35–50** (geschätzt) |
| **A15** · C/D · **GUT VERTRETBAR** | 5.12.2 K1; heute **95**. `e566eb52`, `304ab9af`, `f384a979`, `c4dac399`, `686c6388` | Kontrollzweck nur kurz zurückerinnern; Rendite-/Risikovergleich bündeln. | Unveränderte Tabelle, Grafik und Quellen, Endwertdelta 146’494 USD, BIP-Risikorangfolge und Abgrenzung K1≠Marktkapitalisierung. | **15–20** (geschätzt) |
| **A16** · C/D · **GUT VERTRETBAR** | 5.12.3 Z1; heute **165**. `096fba73`, `a981fff3`, `d943f6ea`, `d7d0e101`, `34f02b9f`, `dffffe93`, `8f9ef237` | Bekannte Risikobegriffe kürzen, aber Halbierungsinterpretation und andere Kriterienrangfolge behalten. | Unveränderte Tabelle und zwei Grafiken, Quellen, 23 versus 16 Jahre, MDD im Gegensatz zum Verlust des Startkapitals sowie unterschiedliche Rendite-/Sharpe-Rangfolge. | **30–45** (geschätzt) |
| **A17** · C/D · **GUT VERTRETBAR** | 5.12.4 SMA-Sensitivität; heute **98**. `2631d055`, `8af54f16`, `e33f8b0b`, `33d92987`, `0d5526ed` | Identisch gerundeten MDD und unterschiedliche Verläufe kurz erklären; keine erneute vollständige Regeldefinition. | Unveränderte Tabelle, Grafik und Quellen, 3/12 als Hauptvariante, historischer 6/12-Vorsprung und Grenze identisch gerundeter Drawdowns. | **15–20** (geschätzt) |
| **A18** · C/D · **GUT VERTRETBAR** | 5.12.5 H1-Teilperioden; heute **142**. `ee619640`, `d6e33122`, `59efb4f5`, `83fc757b`, `3ef40ec9` | Aufteilung aus bestehenden Pfaden prägnant beschreiben; Tabellenrangfolge nicht vollständig nacherzählen. | 2010–2017/2018–2025, jeweils 96 Perioden, kein Neustart und keine neuen Backtests, unveränderte Tabelle und zusätzliche Volatilitäten 7,27 %/10,37 %. Der Herkunftsnachweis darf nicht zur neuen RF-Validierung umgedeutet werden. | **35–50** (geschätzt) |
| **A19** · C/D · **SICHER** | 5.13 Einleitung +5.13.7; heute **150**. `6402a9d2`, `a3e4beef`, `1f328fd6` | Reine Kapitelankündigungen bündeln; Datenbasis der Interpretation und Verallgemeinerungsgrenze behalten. | Alle sieben Interpretationsabschnitte; Antwort und Reflexion in 6.1/6.4; Beispiel unten. | **93** (gemessen am vollständigen Beispiel) |
| **A20** · C/D · **GUT VERTRETBAR** | 5.13.1 Ertrag/Risiko; heute **144**. `6999a6d3`, `3972ae55`, `2b837f9a` | H1-Rangfolge nicht zweimal erklären; Cash-/Drawdown-Deutung und Sharpe-Abgrenzung behalten. | H1-Tabelle in 5.12.1, vollständige Sharpe-Definition in 3.2.5. Hier bleiben Sharpe≠CAGR/Volatilität und die Erklärung, weshalb Cash die Schwankung senken kann, ohne vergangene Verluste aufzuheben. | **35–50** (geschätzt) |
| **A21** · C/D · **GUT VERTRETBAR** | 5.13.2 60/40-Deutung; heute **223**. `c48ec4c3`, `8f8b4803`, `f9f6f912`, `4b05781f` | Grundregel mit Verweis auf 4.2.2 verkürzen; konkrete Umschichtung und Jahresbeispiel prägnant erläutern. | 67’849,53/43’743,87/893,49 USD, 60,80 %, Jahreswerte 2022 −16,86 %/−18,00 %, Quellen, konstantes Gesamtvermögen bei Umschichtung und fehlender isolierter Rebalancing-Kontrolllauf. | **50–70** (geschätzt) |
| **A22** · C/D · **GUT VERTRETBAR** | 5.13.3 Trend-Deutung; heute **375**. `3425064c`, `928fe97f`, `3337f340`, `8ee3e2ad`, `f7382b02`, `01923a4a`, `369f9481`, `3df49dc6` | Monatstabelle nicht Zeile für Zeile nacherzählen; verzögerte Reaktion und verpasste Erholung erklären. Jahres-/Drawdownbeispiele sprachlich verdichten. | Unveränderte Monatstabelle/Quellen, alle einzigartigen Jahreswerte, Verlauf 2011–2012 und US-Cashphase. Das Teilbeispiel mit 40 Wörtern Ersparnis steckt bereits im Intervall 90–110. | **90–110** (geschätzt) |
| **A23** · C/D · **GUT VERTRETBAR** | 5.13.4 Länder-Deutung; heute **296**. `709af16c`, `ab95d9b8`, `82391240`, `e7f2d428`, `6a27a355`, `10761822`, `53354686`, `4b5d4890` | Zielgewichtstabelle nicht erneut ausschreiben; höheren US-Anteil, unterschiedliche Fondserträge und Interpretationsgrenze direkt verbinden. | Unveränderte Gewichtstabelle/Quellen, VTI 13,78 % versus übrige Länder 5,28–6,81 %, keine vollständige Attribution, kein BIP-Renditeprognoseschluss, K1≠MK und H1 mit verschiedenen Universen. | **75–95** (geschätzt) |
| **A24** · C/D · **GUT VERTRETBAR** | 5.13.5 Zeit/Parameter; heute **271**. `bc770851`, `dfc835b7`, `b7c30f4b`, `8b805c66`, `9a3b2312`, `77126f6b`, `4001dccf` | Teilperiodenwerte auf 5.12.5 beziehen, Long-/Cash-Tabelle nicht nochmals ausschreiben; die Overfitting-Anwendung kurz halten. | Unveränderte Positionstabelle/Quellen, Investitionsdauer versus Timing, Markt-/Zeitraumkonfundierung und keine nachträgliche Auswahl von 6/12. | **75–95** (geschätzt) |
| **A25** · D · **GUT VERTRETBAR** | 5.13.6 Auswertungsgrenzen; heute **206**. `7012cb90`, `ef66a225`, `f4051b34`, `2285674e` | Alle vier Grenzabsätze sprachlich verdichten; keine dieser Grenzen allein in den Anhang verlagern. | Tests≠Quellenwahrheit/Veröffentlichungsnachweis, enthaltene versus zusätzliche Kosten, Monats-MDD, idealisierte Schlussausführung, Cash≠RF, USD≠CHF/Absicherung und fehlender Signifikanznachweis. | **35–50** (geschätzt) |

### 6 Fazit — [Notebook](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Fazit.ipynb)

| ID / Typ / Priorität | Heutiger Abschnitt und Quellblock | Massnahme und Begründung | Erhaltene Hauptstelle / Schutz | Ersparnis |
|---|---|---|---|---:|
| **F01** · C/D · **GUT VERTRETBAR** | 6.1 Forschungsantwort; heute **166**. `ed6169f5`, `d59cbe8c`, `4ac7465f` | Zwei Antwortabsätze zusammenführen; wortgleiche Forschungsfrage und Erkenntnis des überprüfbaren Vergleichs behalten. | Wortgleiche Frage, Daten-/Regel-/Kontrollkette, historische BIP-Verfügbarkeit, Wiederholbarkeit und Abgrenzung zur Prognose. | **40–55** (geschätzt) |
| **F02** · C/D · **AUTORENENTSCHEIDUNG** | 6.2 Kernerkenntnisse; heute **398**. `64f46030`, `1d5284b5`, `49dfa9f7`, `481f7871`, `5b3da683`, `18699c4a` | Je Strategie Erkenntnis und Grenze formulieren, statt die Ergebnisdarstellung zu wiederholen. Erste und letzte übergreifende Aussage bündeln. | Alle vier Erkenntnisse, SMA-Sensitivität, K1≠MK, fehlender isolierter Rebalancingnutzen sowie Markt-/Zeitraumkonfundierung. Ausführliche Belege bleiben in 5.12/5.13; eine kurze Rückerinnerung bleibt im Fazit. | **110–140** (geschätzt) |
| **F03** · C/D · **GUT VERTRETBAR** | 6.3 Grenzen; heute **165**. `53c9f636`, `b3aa03a1`, `c6d53830` | Modellannahmen mit kurzem Verweis auf 5.13.6 erläutern; die Kernvorbehalte im Fazit eigenständig erkennbar halten. | Tests≠Datenwahrheit und fehlende statistische Absicherung kleiner Abstände. Das Teilbeispiel mit 30 Wörtern Ersparnis steckt bereits im Intervall 30–45. | **30–45** (geschätzt) |
| **F04** · C/D · **AUTORENENTSCHEIDUNG** | 6.4 Rückblick/Ausblick; heute **223**. `b2aceda6`, `aab69502`, `dc04838e`, `7d7827e1` | Nur wiederholtes Werkzeugnutzen-/Grenzenargument kürzen; persönliche Reflexion und konkrete Weiterführungen erhalten. | Persönlicher Finanzen-/Informatikbezug, Daten-/Zeit-/Kontrollerfahrung, tatsächliche KI-Rolle, eigene Verantwortung und konkrete Weiterführungen zu Rebalancing, Kosten, Cash und Weboberfläche. | **30–45** (geschätzt) |

### Geprüfte Abschnitte ohne Kürzungsauftrag

Die vier Einleitungsabschnitte sind abgedeckt: 2.1/2.2/2.4 durch E01/E02/E04; **2.3 bleibt grundsätzlich erhalten**, weil dort der Untersuchungsrahmen, die vier Konzepte, die fünf Laufrollen, Verfügbarkeit und Abgrenzung erstmals zusammenkommen. Seine 288 Wörter erhalten keinen pauschalen Sparansatz.

Alle drei Theorie-Hauptbereiche bleiben bestehen, wie nach Lehrerfeedback eingerichtet. 3.1.1–3.1.6 und 3.2.1–3.2.6 sind einzeln erfasst, 3.3.1–3.3.4 gemeinsam in T13. **3.2.2.4 «Nominal und real» (`621f9b9a`) wird nicht zur Behebung von R-015 verkürzt oder gelöscht**; seine 58 Wörter haben hier kein Potenzial. Ebenso werden die Code-/Outputprobleme R-001/R-006/R-010 nicht durch Verstecken der Beispiele scheinbar gelöst. Gruppenüberschriften sind bereits von der Zählung ausgeschlossen.

Methodik 4.1–4.4 bleibt ein eigenständiges Kapitel mit tatsächlichen Regeln. Analyse 5.1–5.13 ist vollständig erfasst, darunter jede Untergruppe von 5.10, die bereits kurze Durchführung, alle fünf Ergebnisblöcke und sieben Interpretationsblöcke. Fazit 6.1–6.4 ist vollständig erfasst. Die Technikanhänge und der historische KI-Nachweis werden nicht zur Haupttextentlastung gekürzt.

## 5. Präzise Zielstellen zusätzlicher Auslagerungen

Die folgenden Stellen sind **geplante Ergänzungen bestehender Anhangsnotebooks**, keine schon angelegten Überschriften. Die Originaltexte sollen dort nachvollziehbar übernommen, nicht fachlich korrigiert werden. Technischer Originaltext und kurzer wissenschaftlicher Hinweis sind bewusst unterschiedliche Detaillierungsstufen. Bei gemischten Zellen muss ein späterer Lauf die Schnittgrenze dokumentieren und neue Teilzell-IDs vergeben; Codezellen und ihre Abhängigkeiten bleiben unangetastet.

| Massnahme | Originalquelle / abgegrenzter Teil | Exaktes geplantes Ziel | Im Haupttext verbleibend |
|---|---|---|---|
| P01 | 1.2–1.8, `7dd61677`, `151c337e`, `99be5e48`, `ae9ec038`, `a0ace267`, `e0eaae76`, `6b75ab19`; technischer Teil von `3533c085`; KI-Arbeitsanleitung `830ece39` | A.7 «Technische Projekt- und Arbeitsdokumentation», A.7.1 «Installation, Quarto und Quellenverwaltung», neue ID `sec-projekt-anleitungen` | Kurzer Überblick, wortgleiche Forschungsfrage, wissenschaftlicher Aufbau und Anhangsverweis; vollständige technische Anleitung nicht im Haupttext |
| P01 | 1.11.1–8, `876b0021`, `6f782e72`, `01b061a8`, `310a8c1b`, `8389728d`, `c1515f6e`, `7c098ca4`, `5c023149` | A.7.2 «Historische Quellen- und Werkzeugplanung», `sec-projekt-quellenplanung` | Tatsächlich verwendete Quellen/Instrumente in 4.3 und 5.10, theoretische Belege bei ihren Aussagen |
| P01 | 1.10, `ddad650d` mit dem derzeitigen Status der Checkboxen | A.7.3 «Projektpendenzen — Stand 12. Oktober 2026», `sec-projekt-pendenzen` | Keine Arbeitsliste in Kapitel 1; nachvollziehbare Dokumentation des Arbeitsprozesses bleibt |
| T07 | Pandas-Biografie, Alias-Tabelle und technische Resampling-Anleitung aus `005fce46`, `86c17661`, `c8856345`, zugehöriger API-Beleg `7e670f16`; nicht die wissenschaftliche Zeit-/Frequenzdefinition | B.3.3 «Technische Zeitreihen- und Resampling-Beispiele», `sec-resampling-beispiele` | «Finanzzeitreihen ordnen Beobachtungen zeitlich. Ihre Frequenz legt die Beobachtungsintervalle fest. Für den Vergleich müssen die Reihen in ein einheitliches Format gebracht werden. Beim Downsampling wird ein abgeschlossener Zeitraum auf den letzten verfügbaren Wert verdichtet; die zeitliche Zuordnung bleibt entscheidend (vgl. 5.10.4). Technische Beispiele stehen in Anhang B.3.3.» Quellen an den übernommenen Aussagen belassen. |
| A06 | Nur technische Schreibweise `period_frequency="ME"`/`periods_per_year=12` und Log-Verweis aus `5d011745`; keine Verlagerung der Monatsentscheidung | B.3.2, bestehende ID `sec-daten-5-5-4`, zusätzliche Passage zur konkreten Studienkonfiguration | «Die Auswertung verwendet zwölf Monatsintervalle pro Jahr. Monatslabel und tatsächlicher Handelstag bleiben unterscheidbar; technische Konfigurationsangaben stehen in Anhang B.3.2.» Die übrigen Monats-/Währungsregeln bleiben. |
| A09 | Nur Dateifelder/Quelleintrag aus `e596730b` | B.5.1 «RF-Dateischema und Herkunftsnachweis», `sec-rf-herkunft` | «Die RF-Reihe dient der Sharpe-Berechnung; sie verzinst die Cash-Position nicht. Ihre Datums-/Quelldokumentation steht in Anhang B.5.1.» Die vollständige Verzögerungs-, Sieben-Tage- und ACT/365-Regel verbleibt in 5.10.7. |
| A10 | Vorprüfchronologie `cf893ea2`; nur Dateimetadaten-/Hashsatz aus `fee3f6b2` | B.4.1 «Dokumentierter Vorprüfstand der WEO-Ausgaben», `sec-weo-vorpruefung`; B.5.2 «WEO-Dateimetadaten», `sec-weo-metadaten` | «Verwendet werden nur bereits verfügbare historische Istwerte aus den WEO-Ständen. Dateimetadaten und Vorprüfung sind im Datenanhang dokumentiert.» Tatsächliche Veröffentlichung, Informationspuffer und gemeinsame Jahres-/Versionsregel bleiben in 5.10.8. |
| A12 | Nur Python-/NumPy-/pandas-Versionsliste aus `8c8859cc` | C.3.1 «Ausführungsumgebung», `sec-ausfuehrungsumgebung` | «Die fünf Läufe wurden am 10. Oktober 2026 mit Engine 1.0.0 und dem versiegelten Stand 1954bfb ausgeführt. Die Paketversionen stehen in Anhang C.3.1.» Lauf- und Periodentabelle bleibt. |
| A13 | Vollständige technische Herkunfts-/Dateipfad-/SHA-Beschreibung `1f781a01` | A.6.2 «Dateipfade und technische Prüfkette der Abbildungen», `sec-abbildungs-pruefkette` | Originalgrafiken bleiben im Haupttext; kurze Herkunftserklärung im vollständigen A13-Beispiel. A.6 und die Einbindung der Originalcodezelle bleiben erhalten. |

Die Kurzformulierungen dieser Tabelle sind **Beispiele für die im Haupttext notwendige Mindestinformation**, keine zusätzlichen Massnahmen mit eigener Ersparnis. Die Nettoersparnis stammt ausschliesslich aus dem jeweils zugeordneten Quellblock in Abschnitt 4.

### README und historische Arbeitsstände

Die README enthält die meisten technischen Überblickstexte bereits. Bei den Pendenzen sind ihre Checkboxen jedoch älter als in `index.ipynb`. Eine spätere Zusammenführung darf **nicht die aktuelleren Notebook-Checkboxen durch den alten README-Stand ersetzen**. Bevorzugt wird ein nachvollziehbarer Stand in A.7.3 und ein kurzer README-Verweis; keine zweite vollständige Kopie im Buch. Quellen-/Library-Erwartungen sind als damalige Planung kenntlich zu machen, nicht als Liste tatsächlich eingesetzter Werkzeuge. Die fachliche Quellen-/Datenwahl bleibt im Haupttext. Veraltete Pfade werden hier nicht still aktualisiert: ihre Korrektur R-014 ist ein getrennter Auftrag. Weder README noch Anhänge werden jetzt verändert.

## 6. Gezielt belegte Wiederholungen und notwendige Rückerinnerungen

| Information | Vollständige Hauptstelle, die bestehen bleibt | Kürzbare Wiederholung | Didaktisch notwendiger Rest |
|---|---|---|---|
| Forschungsfrage | 2.2 `ef01feb0`; wortgleich in 6.1 `ed6169f5` und kurz im Überblick | Ausgeschriebene Frage in 5.10.1 `762a3ac1` | Direkter Verweis auf 2.2 und Hinweis, welche Risiko-/Renditedimensionen verglichen werden |
| Allgemeine Engine versus festgelegte Studie | 4.1 `35c815dc`/`053fb431`; technische Details A.1–5 | 5.1 und acht Modell-Kurzabschnitte, anschliessend 5.10.1 | Eine Modellbrücke und eigener Untersuchungsentscheid, keine erneute Vollbeschreibung |
| Overfitting/Data Snooping | 3.3.3 `d513a003` | Definition erneut in 4.1, 5.1, 5.10.1 und 5.13.5 | Konkrete vorab festgelegte Parameter und Begründung, weshalb 6/12 nicht nachträglich Hauptvariante wird |
| Kennzahlendefinitionen | 3.2.2–5, Formeln/Variablen | 2.2 `f733daa1`, 4.4 `a6b32280`, 5.12 `d49a8f28`/`b0ea1a50` | Namen in Einleitung; tatsächlich verwendete Frequenz/Einheit in Methodik; gerundet/nominal/Monatsdrawdown in Ergebnissen |
| K1/H1/Z1-Vergleichslogik | 4.3 `501e6677` und begründete Datenwahl 5.10.3 | Vollaufzählungen in 5.10.3 sowie Erklärungen zu jeder Tabelle | Kurze direkte Erinnerung: H1 andere Universen, K1 gleiche Fonds≠MK, Z1 anderer Markt und Zeitraum |
| Trendregel und Verzögerung | 3.2.6 Definition/Formeln; 4.2.3 konkrete Monatsregel; 5.10.6 eigene Parameter | Wiederholung der Regel vor jeder Ergebnisdeutung | Mechanismus im März/April 2020 an der unveränderten Tabelle zeigen; kein blosses «siehe Theorie» statt Interpretation |
| Ländergewichte | 5.13.4 `e7f2d428` und Quellen | Zahlen nochmals in `10761822` ausschreiben | Verknüpfung hoher US-Anteile mit beobachteter VTI-Entwicklung und ausdrückliche Grenze der Attribution |
| Teilperioden/SMA-Investitionsdauer | 5.12.5 Tabelle `59efb4f5`, 5.13.5 Tabelle `9a3b2312` | Vollständige Nacherzählung in `bc770851`/`b7c30f4b` | Unterschiedliche Zeit-/Timingwirkung interpretieren; gleiche Anzahl Long-Monate ist nicht derselbe Verlauf |
| Modellgrenzen | 4.4 Design; 5.10 konkrete Entscheidungen; 5.13.6 Auswirkung | Ausführliche erneute Liste in Fazit `b3aa03a1` | Fazit bleibt mit kurzen zentralen Vorbehalten allein verständlich; historische Gültigkeit/fehlende Signifikanz nicht streichen |
| Keine eindeutige Siegerstrategie | 5.13.1 belegte Deutung; 6.2 wichtigste eigene Erkenntnis | Mehrere Kapitelankündigungen in 5.13.7 und letzte Wiederholung von 6.2 | Eine verbindende Schlussaussage und die persönliche Schlussbewertung bleiben |

Ein Verweis ersetzt nur wiederholte Definitionen, nicht die konkrete Anwendung. Die eigene Untersuchung darf nicht voraussetzen, dass Leserinnen und Leser erst den technischen Anhang konsultieren, um die Vergleichslogik zu verstehen.

## 7. Gezählt formulierte Ersatzbeispiele — ausschliesslich im Plan

Diese Fassungen stehen nur in diesem Bericht. Sie sind weder neue Notebook-Inhalte noch schon angenommene Autorenformulierungen. Vor Übernahme sind persönlicher Ton, Quellenanschluss und Verständlichkeit zu prüfen. Alte Abschnittsnummern in den Beispielen dienen der Zuordnung zum aktuellen Stand und müssen bei einer späteren Umnummerierung angepasst werden. Die vollständigen Beispiele P01/E01/M01/A01/A03/A13/A19 beziehen sich jeweils auf den ganzen angegebenen Quellblock; die drei Teilbeispiele ersetzen nur die benannte Einzelzelle.

### P01: 856 → 126 Wörter, gemessene Ersparnis 730

Quelle: [index.ipynb](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/index.ipynb); `3533c085`, `5cc38f47`, `845cba4b`, `c73c89c7`, `7dd61677`, `3d335647`, `151c337e`, `e7e0fc70`, `99be5e48`, `c5c67308`, `ae9ec038`, `07151010`, `a0ace267`, `f2c504cd`, `e0eaae76`, `f859a9ec`, `6b75ab19`, `41b584e0`, `830ece39`, `725443c8`, `ddad650d`, `17476257`, `ef2baad3`, `876b0021`, `da89528d`, `6f782e72`, `b99cf154`, `01b061a8`, `4b93919d`, `310a8c1b`, `d23b699a`, `8389728d`, `68c70d93`, `c1515f6e`, `0f54cf80`, `7c098ca4`, `3acfa996`, `5c023149`. Vollständiger künftiger Überblick; technische Originalteile werden ausgelagert, Fragestellung bleibt wortgleich.

> Diese Arbeit verbindet Finanztheorie und Informatik. Ich untersuche, wie ein Python-Modell historische Finanzdaten aufbereitet und festgelegte Anlageregeln anwendet, um langfristige Strategien hinsichtlich Rendite und Risiko zu vergleichen.
>
> Meine Forschungsfrage lautet: «Wie können historische Finanzdaten mithilfe eines Python-basierten Modells verwendet werden, um langfristige Investmentstrategien hinsichtlich Risiko und Rendite zu vergleichen?»
>
> Die Einleitung beschreibt Motivation, Ziele und Untersuchungsrahmen. Die Theorie erklärt die benötigten Begriffe, Strategien und Berechnungen; die Methodik legt die Vergleichsbedingungen fest. In der Analyse begründe ich Daten und Parameter, stelle die Ergebnisse dar und interpretiere ihre Unterschiede. Das Fazit beantwortet die Forschungsfrage und enthält meinen Rückblick und Ausblick.
>
> Technische Entwicklung, Datenaufbereitung und Prüfungen sind in den Anhängen A–C dokumentiert. Anhang D erläutert die KI-Unterstützung. Installationshinweise, Projektanleitungen, Quellenplanung und Pendenzen bleiben in der technischen Projektdokumentation nachvollziehbar.

### E01: 212 → 106 Wörter, gemessene Ersparnis 106

Quelle: [notebooks/Einleitung.ipynb](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Einleitung.ipynb); `22d65606`, `686a445a`, `46680b47`. Vollständige drei Motivationsabsätze; Forschungsfrage und folgende Zielsetzung unberührt.

> Wer langfristig Geld anlegt, interessiert sich für die Vermögensentwicklung. Ein hoher Endwert zeigt jedoch nicht, welche Schwankungen und zwischenzeitlichen Verluste damit verbunden waren. Zwei Strategien können denselben Gewinn erzielen und auf dem Weg dorthin unterschiedliche Risiken aufweisen. Kommer erläutert, dass keine einzelne Kennzahl das gesamte Anlagerisiko beschreibt [@kommerSouveraenInvestierenMit2025, Abschnitt 2.2].
>
> Mich interessiert deshalb, wie sich unterschiedliche Anlageregeln mit historischen Daten untersuchen lassen: langfristiges Halten, die Kombination von Aktien und Anleihen mit regelmässiger Anpassung sowie regelgebundene Ein- und Ausstiege.
>
> Besonders reizt mich die Verbindung von Finanzen und Informatik. Ich möchte die Anlageideen so genau verstehen, dass daraus eindeutige, überprüfbare Programmabläufe entstehen. Damit ist auch die technische Entwicklung Teil der Untersuchung.

### T09-Teil: 60 → 33 Wörter, gemessene Ersparnis 27

Quelle: [notebooks/Theorie.ipynb](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Theorie.ipynb); `22fec44e`. Nur Interpretationsabsatz; übriger Abschnitt, Formeln und Variablen bleiben erhalten.

> Eine tiefe Volatilität zeigt, dass die periodischen Renditen nahe am Mittelwert liegen; eine hohe weist auf stärkere positive und negative Ausschläge hin. Daraus folgt noch keine Aussage über die Höhe der erzielten Rendite [@kommerSouveraenInvestierenMit2025, S. 147-149].

### M01: 173 → 100 Wörter, gemessene Ersparnis 73

Quelle: [notebooks/Methodik.ipynb](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Methodik.ipynb); `a233bc87`, `35c815dc`, `053fb431`. Vollständiger 4.1-Fliesstext; methodische Eigenständigkeit, vorgängige Festlegung und KI-Nachweis erhalten.

> Ich untersuche mit einem historischen Backtest, wie sich Portfolios unter festgelegten Regeln entwickelt hätten. Neben dem Ertrag betrachte ich ihren Verlauf. Dafür verbinde ich die Finanzgrundlagen aus Kapitel 3 mit einem Python-Modell.
>
> Das allgemeine Rechensystem soll unterschiedliche geeignete Daten und Einstellungen verarbeiten können. Für diese Untersuchung lege ich Anlagen, Zeiträume und Regeln vor der Auswertung fest. So vermeide ich die nachträgliche Auswahl besonders erfolgreicher Einstellungen, die auf anderen Daten nicht ebenso gut funktionieren müssen [@hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization»].
>
> Dieses Kapitel beschreibt die Vergleichsregeln. Datenwahl, Parameter und Durchführung stehen in Kapitel 5; technische Entwicklung, Datenaufbereitung, Prüfungen und die dokumentierte KI-Unterstützung in den Anhängen und Arbeitsnachweisen.

### A01: 485 → 137 Wörter, gemessene Ersparnis 348

Quelle: [notebooks/Analyse.ipynb](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Analyse.ipynb); `c50744c1`, `7375ca9d`, `548ffdcf`, `082f8e37`, `2b5f1700`, `3cd4f923`, `2ea901f9`, `a0492744`, `99bcfb9b`. Gemeinsame Fassung für 5.1–5.9; keine zweite Einsparung für Zusammenführung von Überschriften.

> Für die Analyse führe ich die theoretischen Berechnungen in einer gemeinsamen Engine zusammen. Sie trennt Datenaufbereitung, Strategieregeln, Kennzahlen und Export und soll unterschiedliche geeignete Daten und Einstellungen verarbeiten können. Die Entwicklung beginnt mit dem Datenvertrag; ihre Reihenfolge ist meine eigene Designentscheidung (@sec-technik-5-2).
>
> Markt-, Zins- und BIP-Daten werden vereinheitlicht und geprüft. Rohdaten bleiben getrennt erhalten; fehlende Werte werden nicht still interpoliert. Datenvertrag, Umwandlung und Aufbereitung stehen in @sec-daten-5-3, @sec-daten-5-4 und @sec-daten-5-5, Prüfregeln in @sec-pruefung-vor-simulation. Während eines Laufs werden keine neuen Marktdaten geladen.
>
> Konfiguration, Ergebnisvertrag und Aufbau sind in @sec-technik-5-6, @sec-technik-5-7 und @sec-technik-5-8 dokumentiert. Gewichte und Signale helfen bei der Interpretation; das Run-Manifest ordnet Daten, Einstellungen und Programmstand zu. Codex unterstützt Integration und Tests mit künstlichen Daten; die finanzwissenschaftlichen Vorgaben und Untersuchungsentscheidungen stammen von mir (@sec-technik-5-9).
>
> Für die eigentliche Untersuchung werden feste Daten und Parameter vor der Auswertung gewählt. Sie werden nicht nachträglich zugunsten eines gewünschten Resultats verändert [@hilpischPythonFinanceMastering2019, S. 697; @kommerSouveraenInvestierenMit2025, S. 607–608].

### A03: 214 → 81 Wörter, gemessene Ersparnis 133

Quelle: [notebooks/Analyse.ipynb](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Analyse.ipynb); `762a3ac1`. Vollständiger 5.10.1-Text; künftige Nummernverweise nach Strukturentscheid anpassen, keine Fachkorrektur.

> Für die Untersuchung ist Engine 1.0.0 mit dem Git-Tag engine-v1.0 vorgesehen; ihre technischen Prüfungen sind dokumentiert. Ich trenne den Berechnungsablauf von meinen eigenen Entscheidungen über Daten und Parameter. Die Quellen begründen die Konzepte, schreiben aber nicht genau diese Ticker, Zeiträume oder Einstellungen vor.
>
> Zur Forschungsfrage aus Abschnitt 2.2 vergleiche ich Rendite, Volatilität, Sharpe Ratio und maximalen Drawdown, die unterschiedliche Aspekte erfassen [@kommerSouveraenInvestierenMit2025, Abschnitt 2.2]. Die Hauptparameter werden vor der Auswertung festgelegt, um eine nachträgliche Suche nach günstigen Ergebnissen zu vermeiden [@kommerSouveraenInvestierenMit2025, Glossar «Data Snooping»; @hilpischPythonFinanceMastering2019, Kapitel 15, «Optimization»].

### A13: 215 → 108 Wörter, gemessene Ersparnis 107

Quelle: [notebooks/Analyse.ipynb](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Analyse.ipynb); `d49a8f28`, `b0ea1a50`, `1f781a01`, `9f463bb8`. Vollständige Ergebnis-Einleitung; technische Dateipfade/Hashprüfung zusätzlich nach A.6.2 verschieben.

> Die Tabellen zeigen nominale USD-Ergebnisse bei 100’000 USD Startkapital. Neben Endvermögen und Gesamtrendite steht die annualisierte geometrische Rendite: die gleichmässige Jahreswachstumsrate mit demselben Endwert, keine tatsächlich jedes Jahr erzielte Rendite (vgl. Abschnitt 3.2.2).
>
> Volatilität und Sharpe werden ebenfalls annualisiert ausgewiesen; «p. a.» bedeutet «pro Jahr». Der negative Drawdown misst den Rückgang vom bisherigen Höchststand. Ein Wert näher bei null bedeutet einen geringeren maximalen Verlust. Die Monatsbewertungen erfassen keine vollständigen Verluste innerhalb eines Monats. Tabellenwerte sind gerundet; berechnet wurde mit ungerundeten Ergebnissen.
>
> Die sieben gespeicherten Grafiken verwenden die unveränderten Ergebnisdateien der fünf Studienläufe. Darstellungscode und technische Herkunftsprüfung stehen in @sec-abbildungs-code; dafür werden keine neuen Marktdaten oder Backtests benötigt.

### A22-Teil: 74 → 34 Wörter, gemessene Ersparnis 40

Quelle: [notebooks/Analyse.ipynb](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Analyse.ipynb); `f7382b02`. Nur Tabellen-Nacherzählung; alle Monatswerte und Positionen bleiben in Tabelle 3337f340, weitere Jahres-/Drawdownbeispiele unberührt.

> Die Tabelle zeigt die Signalverzögerung: Im März trägt die Trendstrategie noch den Verlust. Das Cash-Signal wirkt erst im April und lässt sie dessen Erholung verpassen. Das Long-Signal von Ende Juli gilt erst im August.

### F03-Teil: 78 → 48 Wörter, gemessene Ersparnis 30

Quelle: [notebooks/Fazit.ipynb](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Fazit.ipynb); `b3aa03a1`. Nur Modellannahmenabsatz; Datenherkunft und fehlende statistische Absicherung in den anderen 6.3-Absätzen bleiben.

> Die Grenzen aus Abschnitt 5.13.6 bleiben für das Fazit entscheidend: Zusätzliche Transaktionskosten, persönliche Steuern und Inflation fehlen, enthaltene Fondskosten bleiben berücksichtigt. Cash ist unverzinst, die Sharpe-Vergleichsrendite angenähert. Monatswerte zeigen keine vollständigen Verluste innerhalb des Monats. Die Ergebnisse sind deshalb weder persönliche Nettorenditen noch eine vollständige Risikodarstellung.

### A19: 150 → 57 Wörter, gemessene Ersparnis 93

Quelle: [notebooks/Analyse.ipynb](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/notebooks/Analyse.ipynb); `6402a9d2`, `a3e4beef`, `1f328fd6`. Nur Einleitung zu 5.13 und Abschluss 5.13.7; alle fachlichen Interpretationsabschnitte bleiben.

> Ich interpretiere die Ergebnisse anhand der gespeicherten Verläufe, Gewichte und Signale. Jahresbeispiele erläutern die Funktionsweise; sie ersetzen den Gesamtvergleich nicht.
>
> Die Rangfolgen ändern sich mit Kennzahl, Datensatz und teilweise bereits mit kleinen Parameteränderungen. Gewichte und Signale helfen, die Unterschiede nachzuvollziehen. Kapitel 6 führt diese Beobachtungen zur Forschungsfrage zusammen und enthält die abschliessende Reflexion innerhalb der untersuchten Aussagegrenzen.

### Weitere Teilformulierungen zu den übrigen Massnahmen

Jeder folgende Text illustriert nur einen Teil des jeweiligen Quellblocks. Er ist **keine vollständige Ersatzfassung** für alle zugeordneten Zellen. Die in Abschnitt 4 geschützten Informationen und Quellen bleiben zusätzlich erhalten. Diese Ausschnitte wurden nicht als Nettoersparnis des Gesamtblocks berechnet; die dortigen Intervalle bleiben Schätzungen. A22/F03 zeigen ergänzende Ausschnitte zu ihren bereits gezählten Teilbeispielen.

- **E02** (Teilformulierung): «Das Modell soll historische Daten unter festgelegten Anlageregeln vergleichen. Neben Rendite, Volatilität, Sharpe Ratio und maximalem Drawdown betrachte ich Investitionsphasen und Portfoliozusammensetzung. Die Kennzahlen werden im Theorieteil erklärt.»

- **E04** (Teilformulierung): «Die Theorie führt die benötigten Begriffe und Berechnungen ein. Die Methodik legt Vergleichsbedingungen fest; die Analyse begründet Daten und Parameter, stellt Ergebnisse dar und interpretiert sie. Das Fazit beantwortet die Forschungsfrage und ordnet Grenzen sowie Weiterführungen ein.»

- **T01** (Teilformulierung): «ETF steht für Exchange Traded Fund, also börsengehandelter Fonds. Marktbreite ETFs bilden Anlagebereiche mit vergleichsweise geringem Aufwand ab. Für den Vergleich verwende ich eine ausschüttungsbereinigte Entwicklung statt einer reinen Kursbetrachtung.»

- **T02** (Teilformulierung): «Eine Streuung kann unternehmens- und branchenspezifische Risiken verringern; marktweite Schwankungen bleiben. Ihr Nutzen hängt vom Zusammenwirken der Renditen ab. Bereits eine Korrelation unter +1 kann das Portfoliorisiko senken; negative Korrelation ist keine Voraussetzung.»

- **T03** (Teilformulierung): «Unterschiedliche Renditen verschieben die Portfolioanteile. Rebalancing stellt die festgelegten Zielgewichte wieder her und dient der Erhaltung des gewählten Rendite-Risiko-Profils. Im Modell erfolgt es jährlich nach einer festen Regel.»

- **T04** (Teilformulierung): «Buy-and-Hold hält ein marktbreites Portfolio langfristig, ohne laufend aufgrund kurzfristiger Prognosen zu handeln. Reinvestierte Dividenden gehören zur Gesamtrendite. Die einfache Referenzstrategie vermeidet jedoch keine Markteinbrüche.»

- **T05** (Teilformulierung): «Aktien und Anleihen verlaufen nicht perfekt gleichgerichtet; ihre Korrelation verändert sich jedoch. Gleichzeitige Verluste wie 2022 zeigen, dass der Anleihenanteil nicht in jeder Marktphase schützt.»

- **T06** (Teilformulierung): «Die BIP-Methode verändert vor allem die Länderanteile; innerhalb der Länder bleibt die Marktkapitalisierungsgewichtung bestehen. Historisch wechselte die besser abschneidende Gewichtungsmethode. Kommers Präferenz belegt deshalb keine allgemeine Überlegenheit.»

- **T07** (Teilformulierung): «Zeitreihen ordnen Beobachtungen bestimmten Daten zu; Reihenfolge und Frequenz sind für den Vergleich wichtig. Beim Downsampling werden Daten zu grösseren Intervallen zusammengefasst. Die wissenschaftliche Monatsregel steht in 5.10.4, technische Beispiele in Anhang B.3.3.»

- **T08** (Teilformulierung): «Die geometrische Rendite beschreibt das durchschnittliche realisierte Wachstum pro Periode. Die annualisierte Rendite rechnet dieses Wachstum auf ein Jahr um. Davon ist der arithmetische Mittelwert zu unterscheiden, der etwa bei der Sharpe Ratio verwendet wird.»

- **T10** (Teilformulierung): «Der Drawdown setzt den aktuellen Vermögenswert zum bisherigen Höchststand ins Verhältnis. Am Höchststand beträgt er null, darunter ist er negativ. Der Maximum Drawdown ist der stärkste beobachtete Rückgang innerhalb des Untersuchungszeitraums.»

- **T11** (Teilformulierung): «Eine höhere Sharpe Ratio zeigt unter gleichen Berechnungsbedingungen ein günstigeres Verhältnis von Überschussrendite und deren Schwankung. Sie erfasst damit nur diesen Risikoblick; Rendite und Drawdown werden zusätzlich betrachtet.»

- **T12** (Teilformulierung): «SMA reagieren auf vergangene Kurse und erkennen eine Bewegung erst nach ihrem Beginn. Häufige Kreuzungen können in Seitwärtsphasen Fehlsignale erzeugen. Nachträglich gewählte Fenster bergen das in 3.3.3 erläuterte Überanpassungsrisiko.»

- **T13** (Teilformulierung): «Ein Backtest gilt zunächst für seine historische Stichprobe. Zukunftsaussagen sind daraus nicht garantiert. Vergleichbare Ergebnisse verlangen gleiche Zeiträume, Datenfrequenzen, Währungen sowie Dividenden- und Inflationsbehandlung.»

- **M02** (Teilformulierung): «Das 60/40-Portfolio beginnt mit 60 % Aktien-ETF und 40 % IEF. Die Anteile driften zwischen den jährlichen Anpassungen; die neuen Positionen gelten für die Folgeperiode. Am letzten Untersuchungsdatum wird nicht erneut umgeschichtet.»

- **M03** (Teilformulierung): «H1 vergleicht verschiedene Anlagekonzepte. K1 hält die sieben Länderfonds gleich und prüft BIP- gegen Gleichgewichtung, keine Marktkapitalisierungsregel. In Z1 ändern sich gegenüber H1 sowohl Markt als auch Zeitraum.»

- **M04** (Teilformulierung): «Ich beurteile Ertrag, Schwankungen und Verluste gemeinsam und ergänze die Kennzahlen durch Verläufe, Gewichte und Signale. Teilperioden entstehen aus durchgehenden Portfoliopfaden, ohne Neustart. Die Ergebnisse beanspruchen keine künftige oder statistisch nachgewiesene Überlegenheit.»

- **A04** (Teilformulierung): «Die ETF-Reihen vertreten bestimmte Anlagebereiche und sind keine kostenfreien theoretischen Indizes. Die sieben Länder bilden eine begrenzte Fallstudie. Die Fondstabelle dokumentiert die Instrumente; unterschiedliche Indexabgrenzungen bleiben eine Vergleichsgrenze.»

- **A05** (Teilformulierung): «H1 umfasst Januar 2010 bis Dezember 2025 mit der Anfangsbewertung Ende 2009 und 192 Monatsrenditen. Der Beginn folgt auf die VT-Auflage und erlaubt einen SMA-Vorlauf; das Ende schliesst das unvollständige Jahr 2026 aus.»

- **A06** (Teilformulierung): «Die Monatsauswertung passt zum langfristigen Vergleich, erfasst jedoch keine vollständigen Verluste innerhalb eines Monats. Verwendet wird die letzte gemeinsame tatsächliche Handelstagsbewertung mit rechtem Monatslabel und dokumentiertem Quelldatum; fehlende Monate werden nicht still ergänzt.»

- **A07** (Teilformulierung): «Adj Close dient als um Dividenden und Splits bereinigter Anbieter-Proxy. Ausschüttungen werden nicht nochmals addiert. Zusätzliche Handelskosten und persönliche Steuern werden nicht simuliert; in den ETF-Reihen enthaltene Kosten werden nicht rückgängig gemacht.»

- **A08** (Teilformulierung): «Die Hauptregel verwendet SMA über drei und zwölf Monatsbeobachtungen. Das Signal entsteht aus derselben bereinigten Reihe wie die Performance und wirkt im Folgemonat. Cash bleibt unverzinst. 2/12 und 6/12 prüfen die Sensitivität, ohne 3/12 nachträglich zu ersetzen.»

- **A09** (Teilformulierung): «Die vorher bekannte Jahreszinsquote wird durch 100 geteilt und mit den Kalendertagen des Monatsintervalls geteilt durch 365 multipliziert. Bei 3 % und 31 Tagen ergibt dies ungefähr 0,2548 %. Das ist eine eigene Approximation, keine exakt realisierte Treasury-Monatsrendite.»

- **A10** (Teilformulierung): «Für die BIP-Gewichte zählt das jüngste gemeinsame zulässige historische Jahr aller sieben Länder. Verwendet wird je Land die zuletzt verfügbare Version aus den WEO-Herbstständen; Schätzungen und Prognosen sind ausgeschlossen. Die jährliche Auswahl verarbeitet nicht laufend alle nationalen Veröffentlichungen.»

- **A11** (Teilformulierung): «Datenliste, Parameter und Auswertungsblöcke werden vor den Hauptläufen versioniert; nach der Datenprüfung werden die verwendeten Dateien mit Hashes festgehalten. Änderungen brauchen einen dokumentierten Grund. Eine ungünstige Rendite allein ist kein Fehlergrund.»

- **A12** (Teilformulierung): «Die fünf Läufe erzeugten elf Strategie-Zeitreihen. Die BIP-Verläufe in H1 und K1 sind identisch. Die separate VTI-Signalhistorie vor der gemeinsamen IEF-Abdeckung verkürzt den eigentlichen US-Untersuchungszeitraum ab Ende 2002 nicht.»

- **A14** (Teilformulierung): «H1 zeigt einen Zielkonflikt: VT Buy-and-Hold und BIP-G7 liegen beim Endvermögen nahe beieinander, das 60/40-Portfolio schneidet bei Volatilität, Sharpe und MDD günstiger ab. Die geringere Trendvolatilität bedeutet dagegen keinen kleineren maximalen Verlust.»

- **A15** (Teilformulierung): «In K1 erzielt BIP-G7 rund 146’494 USD mehr Endvermögen und günstigere Risikokennzahlen als die Gleichgewichtung. Die identischen Länderfonds machen den Gewichtungsvergleich gezielter; Marktkapitalisierungsgewichte wurden nicht untersucht.»

- **A16** (Teilformulierung): «In Z1 erreicht Buy-and-Hold das höchste Endvermögen, verliert zwischen Höchst- und Tiefstand aber zeitweise mehr als die Hälfte seines Werts. Dieser Drawdown bezieht sich auf den früheren Höchststand, nicht auf das Startkapital. Trend hat den kleinsten MDD, 60/40 die niedrigste Volatilität und höchste Sharpe.»

- **A17** (Teilformulierung): «6/12 erzielt das höchste Endvermögen der drei Trendvarianten. 2/12 und 3/12 liegen bei der Rendite nahe beieinander, unterscheiden sich aber beim MDD. Gleich gerundete Drawdowns von 2/12 und 6/12 bedeuten keine identischen Verläufe.»

- **A18** (Teilformulierung): «Die beiden H1-Teilperioden umfassen je 96 Monatsrenditen. Die vorhandenen Pfade werden Ende 2017 geteilt, ohne Portfolios, Gewichte oder Signale neu zu starten. Die Teilkennzahlen stammen aus bestehenden Ergebnissen und nicht aus neuen Backtests.»

- **A20** (Teilformulierung): «Die Sharpe Ratio nutzt monatliche Überschussrenditen zur RF-Reihe und deren Standardabweichung. Sie ist nicht der Quotient aus geometrischer Jahresrendite und Portfoliovolatilität. Cash kann Schwankungen verringern, während entstandene Verluste fortbestehen.»

- **A21** (Teilformulierung): «Die niedrigere Volatilität gilt für das gesamte Konzept aus Aktien, IEF und jährlichem Rebalancing. Weil kein ansonsten identisches Portfolio ohne Umschichtungen untersucht wurde, lässt sich der Nutzen des Rebalancings allein nicht bestimmen.»

- **A22** (Teilformulierung): «Die 2020-Tabelle zeigt, dass die Reaktion auf den Rückgang erst nach dessen Beginn erfolgt und ein Cash-Signal danach einen Teil der Erholung verpassen lässt. Das erklärt den Mechanismus, nicht sämtliche wirtschaftlichen Ursachen des Jahres.»

- **A23** (Teilformulierung): «Der hohe US-Anteil und die stärkere VTI-Entwicklung machen den BIP-Vorsprung gegenüber Gleichgewichtung nachvollziehbar. Dies ist ein Erklärungsansatz, keine vollständige Zerlegung des Mehrertrags: Gewichtsdrift, Umschichtungen und Renditereihenfolge wirken ebenfalls.»

- **A24** (Teilformulierung): «S1 und S2 haben gleich viele Long- und Cash-Monate, aber unterschiedliche Endvermögen. Für das Ergebnis zählt somit auch, in welchen Monaten investiert wurde. Der historische 6/12-Vorsprung ersetzt die vorab festgelegte Hauptvariante nicht.»

- **A25** (Teilformulierung): «Bestandene Rechenprüfungen bestätigen die Übereinstimmung mit Eingaben und Regeln, nicht die Wahrheit jeder historischen Quelle. Auch ein heutiger Hash beweist kein damaliges Veröffentlichungsdatum. Diese Herkunftsgrenzen bleiben nach einem technisch erfolgreichen Lauf bestehen.»

- **F01** (Teilformulierung): «Das entwickelte Modell ermöglicht einen nachvollziehbaren historischen Vergleich, wenn Daten vereinheitlicht und Regeln vorab festgelegt werden. Verläufe, Gewichte und Signale zeigen neben dem Ertrag auch Risiken und Entscheidungen. Das Werkzeug ist keine Renditeprognose.»

- **F02** (Teilformulierung): «Für mich ist entscheidend, dass keine Strategie in allen Kriterien überlegen ist. Höherer historischer Ertrag, geringere Schwankung und kleinerer maximaler Verlust führen zu unterschiedlichen Rangfolgen. Die Einordnung bleibt an Daten, Markt und Regeln gebunden.»

- **F03** (Teilformulierung): «Kleine Abstände wie zwischen VT und BIP-G7 sollten nicht überbewertet werden. Ihre Verlässlichkeit über die untersuchte Stichprobe hinaus wurde nicht statistisch nachgewiesen.»

- **F04** (Teilformulierung): «Der Beitrag liegt für mich in der Verbindung von Finanztheorie und Informatik. Neben den Formeln waren eindeutige Daten, zeitlich passende Entscheidungen und überprüfbare Abläufe entscheidend. Die Verantwortung für Methode und Interpretation bleibt bei mir.»

## 8. Strukturentscheid und Folgen für Nummern/Verweise

Für A01 ist eine zusammengeführte **5.1 «Vom Modell zur Untersuchung»** vorgesehen. Es werden nicht acht Abschnitte gelöscht und anschliessend sichtbare Nummernlücken stehen gelassen. Bei Zustimmung ergibt sich folgende Zuordnung:

| Heute | Späterer Abschnitt |
|---|---|
| 5.1–5.9 | 5.1 gemeinsame Modellbrücke |
| 5.10.1–9 | 5.2.1–9 Daten und Parameter |
| 5.11.1–3 | 5.3.1–3 Durchführung |
| 5.12.1–5 | 5.4.1–5 Ergebnisdarstellung |
| 5.13.1–7 | 5.5.1–7 Interpretation |

Kapitel 1 bleibt Kapitel 1. Kapitel 2–6 und die Anhangsbuchstaben A–D ändern sich dadurch nicht. Die drei Theorie-Hauptbereiche und die vom Lehrer ergänzten Finanz-/Mathematikerklärungen bleiben bestehen. Theorie-Unterüberschriften können nur nach Freigabe zusammengeführt werden; dafür ist hier kein zusätzlicher Wortgewinn gebucht.

Ein späterer Lauf muss **alle betroffenen aktiven Buchverweise** prüfen: Methodik nennt beispielsweise 5.10.2/5.10.7/5.10.8; Fazit nennt 5.12/5.13/5.13.6; Anhangseinleitungen nennen 5.10–5.13. Dazu kommen Ergebnis-/Anhangstexte und sichtbare Inhaltsverzeichnisse. Historische Berichte, Promptkopien und Logs werden nicht rückwirkend umnummeriert. Bei ihnen bezeichnet «5.12» den damaligen Stand.

Die originalen Plotcode-Kommentare nennen ebenfalls Kapitel 5.12. Die Codeobjekte bleiben geschützt. Im technischen Anhang kann ein kurzer Hinweis die alte Kommentarstelle der neuen Ergebnisstelle zuordnen, statt den Originalcode nur für eine Nummer zu ändern. Die Einbindung `Analyse.ipynb#99cad7ec`, alle Grafiklabels und Zellabhängigkeiten müssen erhalten bleiben. Neue technische Anhangsziele erhalten stabile IDs; die gegenwärtigen 14 Anhangsverweise werden nach A01 sinnvoll gebündelt und in den tatsächlichen HTML/PDF/DOCX-Ausgaben erneut aufgelöst.

## 9. Nicht empfohlene Einsparungen und fachliche Sperrstellen

| Nicht empfohlen | Konkrete Stellen | Warum keine Ersparnis angerechnet wird |
|---|---|---|
| Ganze Formeln oder Variablenerklärungen streichen | u. a. `cecc3300`, `b6316a3d`, `bdef1563`, `c70a36fd`, `32e3c634`, `10386aae`, `2e6c469f`, `6e2866c3`, `c68fa307`, `0c76df80`, `2d7aee16` | Mathematische Nachvollziehbarkeit und Lehrerhinweise; Formeln/Tabelle selbst zählen ohnehin nicht zum Wortumfang |
| ETFs/Indexnachbildung pauschal verkürzen | `1941d2df` | Physische Nachbildung, Beispiel, Sampling, Tauschverträge und ausgeschriebener ETF-Begriff wurden bewusst nach Lehrerfeedback ergänzt |
| BIP-Verfügbarkeitsregeln als Technik auslagern | `89a22011`, `fee3f6b2`, `dad07e04` | Ist-/Prognosegrenze, gemeinsame Jahres-/Versionenauswahl und Informationspuffer bestimmen die wissenschaftliche Strategie |
| RF-Regel durch «FRED-Zins» ersetzen | `e3ace74b`, `4e93dcd6`, `e2aa1e8c` | Einheit, vorherige Verfügbarkeit, ACT/365-Approximation und Abgrenzung zu Cash sind für die Sharpe-Werte wesentlich |
| Methodik durch Anhangsverweis ersetzen | 4.2–4.4 | Regeln, Vergleichsdesign und Grenzen müssen ohne technischen Anhang verständlich bleiben |
| Ergebnisse/Mechanismen wegverschieben | Alle vier Hauptkennzahlentabellen, Teilperioden-, Signal-, Gewichts- und Positionswechsel-Tabellen, sieben Analyse-Grafiken; besonders 5.13.2–5 | Eigene wissenschaftliche Befunde und Erklärung; Daten/Tabellen/Grafiken zählen ohnehin nicht als Fliesstext |
| Ungünstige Trendresultate oder Grenzen streichen | 5.12.1, 5.13.3, 5.13.5–6 | Würde die Auswahl verzerren; H1-MDD, Parameterempfindlichkeit, fehlende Attribution und Signifikanz bleiben |
| Fazit-/Reflexionskapitel auf Rangliste reduzieren | 6.1/6.3/6.4, insbesondere `aab69502` | Antwort, begrenzte Aussagekraft, KI-Rolle und persönliche Verantwortung sind wissenschaftlich bzw. persönlich wesentlich |
| Technischen Anhang kürzen und als Haupttextersparnis zählen | A–C, insbesondere C.3-Doppelung | Die Anhänge sind bereits vom Umfang ausgeschlossen; kein Beitrag zur 7’700-Grenze |

**Phase-2-Fachkorrekturen sind ein getrennter Auftrag.** T01 betrifft eine Zelle mit R-003 (falsche Quellenzuordnung) und R-007 (S&P-Auswahlvereinfachung); T03/T05 berühren R-004 (Gewichtszeitpunkt/Bedingung). R-006/R-010 betreffen gespeicherte Beispieldeutung; R-009/R-011 die technischen Zeitreihenbelege. R-015 in Nominal/real ist ausdrücklich ausgespart. Solche Punkte dürfen nicht beim Kürzen still «mitverbessert» oder durch Löschen der beanstandeten Passage verborgen werden. Wo eine geplante Verdichtung davon abhängt, die Fassung bis zur gesonderten Autorenentscheidung zurückstellen und neu zählen. R-008/R-012/R-016/R-017 werden ebenfalls nicht als erledigt ausgegeben.

## 10. Annäherung an 7’700 und notwendige Autorenentscheidungen

Der frühere Auslagerungsbericht nannte grobe Ziele von 2’100 Theorie- und 3’200 Analysewörtern. Diese waren ausdrücklich noch nicht textstellengenau geprüft. Dieser Plan **ersetzt die früheren Orientierungsbudgets** durch konkrete disjunkte Massnahmen: insbesondere ein Haupttext mit nur 2’100 Theoriewörtern ist unter Schutz aller relevanten Erklärungen bisher nicht durch ausführbare Einzelmassnahmen belegt.

Eine denkbare Verteilung bei 7’700 wäre folgende. Sie ist eine **Zielrechnung**, keine zweite Massnahmenliste und keine zusätzlich anrechenbare Ersparnis:

| Kapitel | Diskussionsbudget für 7’700 | Bestmöglicher Rest aus den bisher belegten Massnahmen | Noch nicht durch diesen Plan gedeckt |
|---|---:|---:|---|
| Überblick | 126 | 126 | Durch P01-Beispiel abgedeckt |
| Einleitung | ca. 640 | 614 | Innerhalb des Potenzials; nicht maximal kürzen |
| Theorie | ca. 2’400 | 2’810 | **Weitere ca. 410** Wörter, bisher ohne wissenschaftlich sichere Streichstellen |
| Methodik | ca. 920 | 882 | Innerhalb des Potenzials; Eigenständigkeit erhalten |
| Analyse | ca. 2’850 | 3’288 | **Weitere ca. 438** Wörter, bisher ohne wissenschaftlich sichere Streichstellen |
| Fazit | ca. 764 | 667 | Personalität/Reflexion stärker erhalten, nicht maximal kürzen |
| **Summe** | **7’700** | **8’387** | Insgesamt **687** Wörter Abstand; Theorie/Analyse benötigen zusammen ca. 848 zusätzliche Wörter, andere Kapitel werden gegenüber maximaler Kürzung um ca. 161 entlastet |

Die Rechnung zeigt den Zielkonflikt sichtbar. Es wäre nicht seriös, die fehlenden 410 bzw. 438 durch blosses Setzen niedrigerer Kapitelbudgets als «gefunden» zu deklarieren. Für eine zweite Stufe könnten nach einem ersten vollständigen Entwurf noch engere Verbindungen zwischen Definition, Formel und Anwendung oder zwischen Tabellenbefund und Interpretation geprüft werden. Dafür muss jede neue Ersatzfassung gegen die vollständige Aussage-/Parameterliste geprüft werden. **Kein Wegfall ganzer wissenschaftlicher Mechanismen oder nur im Anhang versteckter Grenzen ist vorab empfohlen.** Der natürliche Autorenton ist ein zusätzlicher Grund, diese Stufe nicht als garantierte automatische Reduktion zu behandeln.

Vor einem Umsetzungsauftrag sind folgende Entscheidungen festzuhalten:

1. P01: kurze wissenschaftliche Kapitel-1-Fassung und historische technische Dokumentation in A.7; README nur verweisen, aktuellere Checkboxen erhalten.
2. A01: gemeinsame Modellbrücke und die dargestellte Unterabschnitts-Umnummerierung akzeptieren; Hauptkapitelnummern bleiben.
3. T01: Umfang der Index-/ETF-Erläuterung nach Lehrerfeedback; keine Kürzung an diesen Stellen ohne Prüfung der didaktischen Wirkung.
4. F02/F04: gewünschte Gewichtung der Erkenntnisse, persönlichen Erfahrung und Weiterführungen; Ich-Form nicht pauschal entfernen.
5. 7’700: erste Stufe mit ungefähr 8’400–9’100 als Zwischenfassung bearbeiten und danach eine zweite konkrete Verdichtungsanalyse freigeben, statt bereits jetzt ungesicherte zusätzliche Streichungen anzuordnen.
6. Fachliche Sperrstellen: getrennten Fachkorrekturauftrag beziehungsweise deren Zurückstellung eindeutig festlegen; Kürzungsplan ist keine Freigabe dieser Korrekturen.

## 11. Empfohlene Reihenfolge eines späteren Codex-Laufs

1. **Freigegebene Massnahmen-IDs als verbindlichen Umfang übernehmen.** HEAD/Branch/Status erneut prüfen; veränderte Quellzellen seit 32965a7… melden und neu zählen. Extern alle Quellen und erzeugten Ausgaben sichern, nicht nur deren Hashes. Aktive Code-/Output-/Bild-/Formel-/Quellen- und Tabellenbestände erfassen.
2. **P01 und technische A-Anteile zuerst.** Zielüberschriften A.7/B.3.3/B.5.1–2/C.3.1/A.6.2 anlegen, Originalteile mit Zell-/Teilzellzuordnung übernehmen, Haupttext-Zusammenfassungen halten. Keine methodischen Regeln versehentlich mitverschieben. Keine neuen Ausführungen oder Ersatzdaten.
3. **Sichere Wiederholungen A03/A19 und die freigegebene Struktur A01.** Eine einzige Nummern-/Verweismigration durchführen. Alle aktiven Buchverweise und Codekommentar-Zuordnungen kontrollieren; historische Nachweise konservieren.
4. **Definitionen und Design verdichten:** E01/E02/E04, freigegebene T-/M-Massnahmen und A04–A11. Die allgemeine Erklärung erhält einen festen Hauptort; konkrete untersuchte Werte bleiben im Analyse-Haupttext. Gesperrte Fachstellen nicht nebenbei korrigieren.
5. **Ergebnisprosa und Interpretation getrennt bearbeiten:** A13–A25. Tabellen, Grafiken, Quellen und alle einzigartigen Zahlen schützen. Zuerst reine Nacherzählung kürzen, dann sprachlich verdichten; die erklärende Anwendung bleibt. Keine nicht nachgewiesene Kausalität formulieren.
6. **Fazit zuletzt:** F01/F03 und ausdrücklich freigegebene F02/F04. Ergebnisbelege nicht erneut ausschreiben; Forschungsantwort, erforderliche Vorbehalte und persönliche Reflexion eigenständig erhalten.
7. **Neu zählen und nur tatsächliche Nettoersparnis berichten.** Mit disjunktem Ledger vergleichen; bei Untererfüllung nicht automatisch weitere Absätze streichen. Weder Tabellen-/Codeverschiebung noch Anhangsbereinigung als Fliesstextgewinn buchen. Eventuelle Zusatzsätze einrechnen.
8. **Integrität und Darstellung in externer Projektkopie prüfen.** Originale Codeobjekte/IDs/Reihenfolge/Execution Counts/Outputs und Bildhashes unverändert; Formeln, alle relevanten Variablen, numerische Studienbefunde, Tabellen, Quellenbelege und Grenzen vollständig. Notebook-Schema prüfen. Nach der Strukturänderung HTML, PDF und DOCX mit deaktivierter Notebook-Ausführung und ohne neue Hauptläufe rendern; echte Nummern, Verweise, Anhangsziele und Seiten kontrollieren. SHA-256 der Studienresultate und des Freeze-/Engine-Stands abgleichen.
9. **KI-Nachweis und tatsächlichen Git-Diff prüfen, dann zur Autorenkontrolle stoppen.** Kein Commit/Push/Merge/Reset/Clean. Ist 7’700 noch nicht erreicht, eine neue konkrete Abwägung dokumentieren; keine unfreigegebene zweite Kürzungsrunde.

## 12. Dokumentation und Kontrollen dieses Planungsauftrags

Die Notebook-Texte wurden nur gelesen und mit einem separaten Standardbibliotheksskript gezählt; die Notebook-Codezellen wurden nicht ausgeführt. Eine statische Zuordnungsprüfung stellt sicher, dass die 49 Massnahmen disjunkte Quellzellblöcke besitzen und kein Intervall den gesamten jeweiligen Fliesstext übersteigt. Die zehn Beispiele wurden nach derselben Methode gezählt. Ihre Quellen und die beschriebenen Anhangsziele wurden anhand der tatsächlichen Zell-IDs geprüft.

Die vollständige Promptkopie liegt unter [2026-10-12-kuerzungsplan-haupttext.txt](C:/Users/modic/Documents/GitHub/Maturarbeit_Riccardo_Ambuehl_2027/documentation/ai-usage/prompts/2026-10-12-kuerzungsplan-haupttext.txt); SHA-256: `ebb71cff87e0d761909543422b54dd996823fff290bd58f9029550a4672c7e14`. Das laufende KI-Log und der Buchanhang enthalten einen sachlichen Nachtrag zu **Analyse/Planung und den von Codex formulierten Beispielen**, ohne eine ausgeführte Kürzung oder neue wissenschaftliche Ergebnisarbeit zu behaupten. Bisherige Nachweise bleiben erhalten.

Die abschliessende Prüfung vergleicht mit der externen Ausgangserfassung von 81 versionierten und 70 vorhandenen Cache-/Ausgabedateien. Erlaubte Dateidifferenzen: dieser neue Plan und die neue Promptkopie sowie ausschliesslich angehängte Ergänzungen an `documentation/ai-usage/ai-usage-log.md` und `ki-nutzung.qmd`. Alle 79 übrigen versionierten Ausgangsdateien, einschliesslich der neun Notebooks, müssen byteidentisch bleiben; ebenso alle 70 vorhandenen Dateien unter `_book`, `_freeze` und `.quarto`. Branch, HEAD und Git-Index bleiben unverändert. **Abschlussergebnis:** Alle 79 übrigen versionierten Ausgangsdateien, einschliesslich der neun Notebooks, sind SHA-256-identisch. Sämtliche 70 vorhandenen Ausgabe-/Freeze-/Cachedateien sind ebenfalls byteidentisch; ihr Dateiinventar ist unverändert. Die früheren KI-Dateiinhalte bleiben als identischer Dateipräfix erhalten. Der Diff beschränkt sich auf genau vier erlaubte Dateien. Branch dev, HEAD 32965a78543c641ff2bf3755c1987678843c829d und Git-Index sind unverändert; `git diff --check` bestanden.

Der neue KI-Nachtrag wurde nach `KI-DOKUMENTATION-BUCH-SYNC` im Log und Buch abgeglichen. Das HTML-Buch wurde in einer externen Kopie mit `execute.enabled: false`, `freeze: false` und `quarto render --to html --no-execute --no-cache` erfolgreich gerendert (Exit 0). Der neue Abschnitt steht als **D.6 «Wissenschaftlicher Kürzungsplan»** im KI-Anhang und Inhaltsverzeichnis. **1’770 lokale Dateiverweis-/Anker-Vorkommen** wurden geprüft, ohne ungültiges Ziel. PDF/DOCX wurden für diesen reinen Planungs-/KI-Nachtrag nicht neu gerendert; die frühere Dreiformatprüfung ist im Auslagerungsbericht dokumentiert.

Temporäre Zählungen, Massnahmenledger, Beispielzählungen, Ausgangshashes und HTML-Prüfung liegen ausschliesslich unter `C:\Users\modic\AppData\Local\Temp\codex-kuerzungsplan-2026-10-12-w47wazz9`. Sie sind keine veränderten Studienartefakte und ersetzen keine Autorenfreigabe.

**STOPP zur gemeinsamen Prüfung und Freigabe des Kürzungsplans. Kein vorgeschlagener Fachtext wurde in die Arbeit übernommen.**
