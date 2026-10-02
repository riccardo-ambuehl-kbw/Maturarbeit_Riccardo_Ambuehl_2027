# Maturarbeit Backtesting Engine – Arbeitsregeln

## Projektkontext

Dieses Repository enthält sowohl die schriftliche Maturarbeit als auch den Python-Code für ein reproduzierbares Backtesting-System.

Für Arbeiten an der Engine gelten folgende Quellen als fachlicher Kontext:

- `notebooks/Analyse.ipynb`, insbesondere Kapitel 5.3 bis 5.9:
  Datenformat, Verarbeitung, Konfiguration, Ergebnisformat und geplante Architektur.
- `notebooks/Theorie.ipynb`, insbesondere Kapitel 3.2 bis 3.13:
  finanzmathematische Definitionen, Strategien und Backtesting-Regeln.
- `src/funktionen.py`:
  bestehende Implementierungen aus dem Theorieteil, die geprüft und soweit fachlich korrekt wiederverwendet werden sollen.
- `methodik.qmd`:
  bestehende methodische Rahmenbedingungen der Untersuchung.
- `documentation/ai-usage/`:
  Regeln zur transparenten Dokumentation der KI-Nutzung.

Wenn sich Theorie, Analyse, Methodik und bestehender Code widersprechen, darf der Widerspruch nicht still aufgelöst werden. Er muss dokumentiert und als offene Entscheidung gemeldet werden.

## Fachliche Grenzen

Codex darf keine finanzwirtschaftlichen oder methodischen Regeln still verändern oder selbst festlegen.

Insbesondere darf Codex nicht selbst auswählen:

- die endgültigen Wertpapiere oder Indizes,
- den endgültigen Untersuchungszeitraum,
- die endgültige risikofreie Serie,
- die endgültigen SMA-Parameter,
- andere Parameter der eigentlichen Maturarbeits-Untersuchung.

Diese Werte werden erst nach Fertigstellung und Prüfung der allgemeinen Engine festgelegt.

Technische Entscheidungen darf Codex selbst treffen, wenn sie die festgelegte Methodik und die beschriebenen Schnittstellen nicht verändern. Technische Entscheidungen sollen kurz dokumentiert werden.

## Bestehende Funktionen

`src/funktionen.py` ist der Ausgangspunkt für die mathematischen Berechnungen.

Bestehende Funktionen sollen nicht ohne Grund durch eine zweite unabhängige Implementierung ersetzt werden.

Wenn eine Funktion fachlich falsch, unvollständig oder für die neue Schnittstelle ungeeignet erscheint:

1. Problem mit einem kleinen reproduzierbaren Beispiel nachweisen.
2. Bezug zur Theorie bzw. Analyse nennen.
3. Änderung vorschlagen.
4. Keine methodische Änderung still durchführen.

Wrapper oder zusätzliche Hilfsfunktionen sind erlaubt.

## Daten und Reproduzierbarkeit

Ein Backtest darf während seiner Ausführung keine neuen Marktdaten aus dem Internet laden.

Datenimport und Simulation müssen getrennt bleiben.

Fehlende Marktwerte dürfen nicht still interpoliert, vorwärtsgefüllt oder anderweitig erfunden werden.

Ein Simulationslauf muss auf einen konkreten Datenstand, eine konkrete Konfiguration und eine konkrete Codeversion zurückgeführt werden können.

## Qualität und Tests

Neue oder geänderte Engine-Funktionalität muss durch Tests abgedeckt werden.

Tests dürfen nicht lediglich angepasst oder abgeschwächt werden, damit fehlerhafter Code erfolgreich erscheint.

Vor der Aussage, dass ein Arbeitsschritt abgeschlossen ist, müssen die relevanten Tests tatsächlich ausgeführt werden.

Codex soll technische Fehler innerhalb eines bestätigten Arbeitsauftrags selbstständig untersuchen, korrigieren und erneut testen.

Bei einer neuen fachlichen oder methodischen Entscheidung muss Codex stoppen und die Entscheidung melden.

## Geschützte Inhalte

Ohne ausdrücklichen Auftrag dürfen folgende Dateien in Engine-Arbeitsschritten nicht inhaltlich verändert werden:

- `notebooks/Analyse.ipynb`
- `notebooks/Theorie.ipynb`
- `methodik.qmd`
- `references.bib`
- die fertigen Buchkapitel

Änderungen an der technischen Engine sollen primär in folgenden Bereichen erfolgen:

- `src/`
- `tests/`
- `configs/`
- `scripts/`
- `documentation/engine/`
- notwendigen Python-Abhängigkeitsdateien

## KI-Dokumentation

Relevante Codex-Arbeitsschritte müssen gemäss `documentation/ai-usage/README.md` dokumentiert werden.

Dabei ist klar zwischen
- vom Autor vorgegebenen Entscheidungen,
- technischer Umsetzung durch Codex,
- von Codex vorgeschlagenen Entscheidungen,
- Tests und manueller Kontrolle
zu unterscheiden.