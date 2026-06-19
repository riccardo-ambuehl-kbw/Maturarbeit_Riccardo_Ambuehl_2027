# Maturarbeit

**Titel:** Langfristige Anlagestrategien anhand historischer Finanzdaten 
**Autor:** Riccardo Ambühl

Dieses Repository enthält ein Quarto-Book-Setup für die Maturarbeit. Die Arbeit ist in einzelne Kapitel aufgeteilt, Python-Experimente liegen in `notebooks/`, Quellen in `references.bib`, Styles in `styles/` und spätere Ergebnisse in `outputs/`.

## Forschungsfrage

Wie können historische Finanzdaten mithilfe eines Python-basierten Modells verwendet werden, um langfristige Investmentstrategien hinsichtlich Risiko und Rendite zu vergleichen?

## Installationsempfehlungen

Installiere lokal:

- [Quarto](https://quarto.org/)
- [VS Code](https://code.visualstudio.com/)
- VS-Code-Erweiterungen: Quarto, Python, Jupyter
- Python 3.11 oder neuer
- Python-Pakete: `jupyter`, `pandas`, `matplotlib`
- Zotero mit Better BibTeX

Beispiel für eine lokale Python-Umgebung:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install jupyter pandas matplotlib
```

## Quarto-Befehle

Vorschau im Browser:

```powershell
quarto preview
```

Alle Formate rendern:

```powershell
quarto render
```

Nur HTML rendern:

```powershell
quarto render --to html
```

Nur PDF rendern:

```powershell
quarto render --to pdf
```

## Zotero und Better BibTeX Workflow

1. Quellen in Zotero sammeln.
2. Better BibTeX installieren.
3. Eine Sammlung für die Maturarbeit anlegen.
4. Die Sammlung als BibLaTeX oder BibTeX nach `references.bib` exportieren.
5. Wenn möglich automatische Aktualisierung aktivieren.
6. Kurze, stabile Citation Keys verwenden, zum Beispiel `markowitz1952`.

## Quellen verwenden

Quellen werden in den `.qmd`-Kapiteln mit Quarto-Zitationssyntax eingebunden:

```markdown
Die moderne Portfoliotheorie beschreibt Diversifikation systematisch [@markowitz1952].
```

Die globale Bibliographie ist in `_quarto.yml` über `references.bib` eingebunden.

## Neue Kapitel hinzufügen

1. Neue Datei erstellen, zum Beispiel `resultate.qmd`.
2. Kapitelüberschrift mit `# Resultate` beginnen.
3. Datei in `_quarto.yml` unter `book: chapters:` ergänzen.
4. Mit `quarto preview` prüfen.

## Notebooks sinnvoll auslagern

Nutze `notebooks/` für explorative Arbeit, Zwischenschritte und Tests. Übertrage nur die relevanten, geprüften Ergebnisse in die `.qmd`-Kapitel. Dadurch bleibt das Book lesbar, während der Analyseprozess trotzdem nachvollziehbar bleibt.

## Projektstruktur

```text
.
├── _quarto.yml
├── index.qmd
├── einleitung.qmd
├── theorie.qmd
├── methodik.qmd
├── fazit.qmd
├── references.bib
├── styles/
├── notebooks/
├── data/
├── images/
├── outputs/
└── documentation/ai-usage/
```

## KI-Nachweise

Die Nutzung von KI-Tools wird unter `documentation/ai-usage/` dokumentiert. Dort wird festgehalten, wann KI eingesetzt wurde, wofür sie genutzt wurde, welche Inhalte übernommen wurden und was manuell geprüft werden muss.

## Pendenzenliste

- [x] :date: Spätestens KW 27 Disposition abgeben
- [ ] :date: KW 27-29 Theorie
- [ ] :date: KW 30 Daten importieren
- [ ] :date: KW 31 Daten verarbeiten
- [ ] :date: KW 32-38 Analyse
    - [ ] :date: KW 32-33 Funktionen für die Formeln erstellen
    - [ ] :date: KW 34 Alle Funktionen bündeln und eine Simulations Funktion erstellen
    - [ ] :date: KW 35-38 Simulation verschiedener Strategien
- [ ] :date: 25.09.2026 Probekapitel abgeben
- [ ] :date: KW 39-40 Auswertung
    - [ ] :date: KW 39 Auswertungen bündeln
    - [ ] :date: KW 40 Auswertungen Grafisch darstellen (SVG)
- [ ] :date: KW 41 Einleitung
- [ ] :date: KW 42 Fazit
- [ ] :date: 19.–30.10.2026 / KW 43–44 Definitiven Titel im Intranet eingeben
- [ ] :date: KW 43-44, spätestens 30.10.2026 Erste Fassung
- [ ] :date: KW 45 Gegenlesen
- [ ] :date: KW 46 Überarbeitung
- [ ] :date: KW 47 Schlusskontrolle und Abgabe vorbereiten
    - [ ] Abstract fertigstellen und elektronisch abgeben
    - [ ] Titelblatt kontrollieren
    - [ ] Inhaltsverzeichnis und Seitenzahlen kontrollieren
    - [ ] Abbildungs- und Tabellenverzeichnis kontrollieren
    - [ ] Literatur- und Quellenverzeichnis kontrollieren
    - [ ] Ehrlichkeitserklärung ausfüllen, unterschreiben und als letzte Seite einfügen
    - [ ] PDF exportieren und vollständig kontrollieren
    - [ ] Zwei gebundene Exemplare drucken lassen
    - [ ] Eigenes drittes Exemplar für die Präsentation vorbereiten
- [ ] :date: Mittwoch, 25.11.2026, mittags Maturitätsarbeit abgeben
    - [ ] Zwei gebundene Exemplare abgeben
    - [ ] Elektronische PDF-Version abgeben
    - [ ] Webseite hochladen
- [ ] :date: KW 2–3 2027 Präsentation erstellen
- [ ] :date: KW 4 2027: Präsentation üben und auf Fragen vorbereiten
- [ ] :date: Samstag, 30.01.2027 Präsentation

**Optional:**
- [ ] :date: Simulation Tool basierend auf der Simulation Funktion
- [ ] :date: Automatisiertes testen von weiteren Strategien auf dem Server
- [ ] :date: Verschiedene anschauliche Grafik Typen (SVG)

## Quellen

### Yahoo Finance
Yahoo Finance bietet historische Kursdaten für eine Vielzahl von Finanzinstrumenten, darunter Aktien, ETFs und Anleihen. Diese Daten können für die Berechnung von Renditen, Volatilität und anderen Kennzahlen verwendet werden.

### FRED (Federal Reserve Economic Data)
FRED ist eine umfangreiche Datenbank der Federal Reserve Bank of St. Louis, die wirtschaftliche und finanzielle Daten bereitstellt. Hier können makroökonomische Indikatoren wie das Bruttoinlandsprodukt (BIP), Arbeitslosenzahlen und Zinssätze abgerufen werden, die für die Analyse von Anlagestrategien relevant sein können.

### Vanguard
Vanguard ist einer der grössten Anbieter von ETFs und bietet umfangreiche Informationen zu seinen Produkten, einschliesslich historischer Renditen, Kostenquoten und Fondsinformationen. Diese Daten können für die Analyse von ETF-basierten Anlagestrategien verwendet werden.

### Fidelity Investments
Fidelity ist ein internationaler Online-Anbieter im Finanzsektor, der neben Finanzdienstleistungen auch fundiertes Fachwissen über verschiedene Anlagestrategien vermittelt. Für die vorliegende Arbeit dient die Plattform als wertvolle Quelle, um tiefere Einblicke in die praktische Nutzung und Anwendung dieser Finanztheorien zu gewinnen.

### Souverän investieren mit Indexfonds und ETFs (Autor: Gerd Kommer, ISBN: 978-3-593-52064-3)
Ich erhoffe mir von diesem Buch das theoretische Fundament für meine passiven Anlagestrategien. Es soll mir dabei helfen, das breit gestreute Investieren mit ETFs, das 60/40-Portfolio und die BIP-Gewichtung zu erklären.

### Der leichte Einstieg in die Welt der ETFs (Autor: Gerd Kommer, ISBN: 978-3-95972-543-9)
Ich erhoffe mir von diesem Buch ganz einfache Definitionen für die Grundlagen meiner Arbeit. Ich will damit Begriffe wie "ETF" oder die Reinvestition von Dividenden erklären.

### Python for Data Analysis (Autor: Wes McKinney, ISBN: 978-1-09-810403-0)
Ich erhoffe mir von diesem Buch das Wissen, wie ich die historischen Kurse von Yahoo Finance und FRED richtig verarbeite. Es soll mir zeigen, wie ich die Daten filtere und anpasse.

### Python for Finance (Autor: Yves Hilpisch, ISBN: 978-1-4920-2433-0)
Ich erhoffe mir von diesem Buch die mathematische Erklärung für meine Trendfolgestrategie. Ich will daraus lernen, wie Indikatoren wie der MA und der RSI genau funktionieren und wie man Kennzahlen wie die Sharpe Ratio und den maximalen Drawdown berechnet.

**Python Libraries und wie ich sie anwende:**

- yfinance (Yahoo Finance Kursdaten)
- fredapi (Zugriff auf FRED)
- pandas (Datenverarbeitung, zentrales Werkzeug für Zeitreihen, Renditen, Resampling)
- numpy (numerische Basis, Volatilität, kumulierte Renditen)
- quantstats (Performance Reports: Sharpe, Drawdown, CAGR)
- empyrical (Risiko-/Renditkennzahlen)
- vectorbt oder backtesting.py (Backtesting)
- pandas-ta (Technische Indikatoren)
- matplotlib (Visualisierung)
- plotly (interaktive Kursverläufe)

Das ist eine Auswahl an Libraries, die ich testen möchte, jedoch nicht unbedingt alle schlussendlich verwenden werde. Es ist sinnvoll, möglichst viele geeignete Libraries zu nutzen, um den Aufwand gering zu halten. Das Ziel ist es, etwas Neues zu schaffen und nicht bereits Vorhandenes erneut zu programmieren.