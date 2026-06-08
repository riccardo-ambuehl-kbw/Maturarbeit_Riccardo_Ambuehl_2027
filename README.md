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

- [ ] :date: Einleitung schreiben
- [ ] :date: Theorie
- [ ] :date: Daten importieren
- [ ] :date: Daten verarbeiten
- [ ] :date: Analyse
    - [ ] :date: Funktionen für die Formeln erstellen
    - [ ] :date: Alle Funktionen bündeln und eine Simulations Funktion erstellen
    - [ ] :date: Simulation verschiedener Strategien
- [ ] :date: Auswertung
    - [ ] :date: Auswertungen bündeln
    - [ ] :date: Auswertungen Grafisch darstellen (SVG)
- [ ] :date: Fazit
- [ ] :date: Erste Fassung
- [ ] :date: Gegenlesen
- [ ] :date: Überarbeitung
- [ ] :date: Export PDF/Webseite hochladen (Abgabe)
- [ ] :date: Präsentation

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

### Mit Handelssystemen zum Börsenerfolg (ISBN: 978-3-98609-292-4)
Ich erhoffe mir von diesem Buch das theoretische Fundament für meine Trendfolgestrategie. Es soll mir dabei helfen, die mathematischen Hintergründe von Indikatoren wie dem RSI und dem MA exakt zu definieren und zu erklären.

### Der leichte Einstieg in die Welt der ETFs (ISBN: 978-3-95972-842-3)
Ich erhoffe mir von Gerd Kommers Buch das theoretische Fundament für mein passives Portfolio. Es soll mir dabei helfen, verständlich und wissenschaftlich zu erklären, warum breit gestreutes Investieren mit ETFs funktioniert, wie das 60/40-Portfolio aufgebaut ist und worin genau die Vorteile einer BIP-Gewichtung liegen.

@MaximumDrawdown