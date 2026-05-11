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
├── analyse.qmd
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
