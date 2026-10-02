# Codex-Prompt: Audit vor der Engine-Implementierung

**Datum:** 2026-10-02
**Tool:** Codex
**Zweck:** Prüfung der fachlichen und technischen Anforderungen vor der Implementierung der Backtesting-Engine

## Vollständiger Prompt

Führe vor jeder Implementierung zunächst einen vollständigen Audit der geplanten Backtesting-Engine durch.

WICHTIG:
In diesem Arbeitsschritt darf noch keine Engine implementiert und kein bestehender fachlicher Code verändert werden.

Lies zuerst den lokalen Projektkontext. Besonders wichtig sind:

1. `notebooks/Analyse.ipynb`
   - Kapitel 5.1 bis 5.9 vollständig lesen.
   - Kapitel 5.3 bis 5.9 sind für Datenvertrag, Datenverarbeitung, Konfiguration, Ergebnisformat und Systemarchitektur besonders wichtig.

2. `notebooks/Theorie.ipynb`
   - die für die Engine relevanten Kapitel 3.2 bis 3.13 lesen.
   - Besonders prüfen: Renditen, Annualisierung, Volatilität, Drawdown, Sharpe Ratio, Korrelation, Rebalancing, Buy-and-Hold, 60/40, BIP-Gewichtung, Trendfolge sowie Look-ahead Bias und Data Snooping.

3. `src/funktionen.py`
   - jede bestehende Funktion mit den Definitionen im Theoriekapitel vergleichen.
   - Eingaben, Ausgaben, Annahmen, Randfälle und mögliche Integrationsprobleme untersuchen.

4. `methodik.qmd`
   - die bisher festgelegten Rahmenbedingungen berücksichtigen.
   - Falls die Methodik noch unvollständig oder im Konflikt mit Theorie/Analyse ist, nicht selbst entscheiden, sondern melden.

5. `documentation/ai-usage/README.md`
   - die Regeln zur KI-Dokumentation berücksichtigen.

6. `AGENTS.md`
   - die dort festgelegten Arbeitsregeln einhalten.

ZIEL DES AUDITS

Prüfe, ob aus dem aktuellen Stand eindeutig eine reproduzierbare Backtesting-Engine implementiert werden kann.

Unterscheide dabei konsequent zwischen:

A) bereits fachlich festgelegten Anforderungen,
B) technischen Entscheidungen, die du später selbst treffen darfst,
C) noch offenen fachlichen oder methodischen Entscheidungen, die der Autor treffen muss,
D) Widersprüchen zwischen Theorie, Analyse, Methodik und bestehendem Code.

PRÜFE INSBESONDERE

- den Datenvertrag aus Kapitel 5.3,
- Trennung von performance_value und signal_value,
- Metadaten, Risk-Free- und Makrodaten,
- Datenimport und Datenvalidierung,
- Umgang mit fehlenden Werten,
- Resampling und Datenfrequenzen,
- JSON-Konfiguration,
- alle vorgesehenen Strategien,
- gemeinsames Ergebnisformat aus Kapitel 5.7,
- strategieabhängige Outputs,
- run_manifest.json,
- Architektur aus Kapitel 5.8,
- Ablauf eines Simulationslaufs,
- Wiederverwendung der bestehenden Funktionen aus Kapitel 5.9 und `src/funktionen.py`,
- Reproduzierbarkeit,
- mögliche Look-ahead-Fehler,
- mögliche Probleme beim Beginn einer SMA-Strategie,
- zeitliche Logik des Rebalancings,
- Risk-Free-Ausrichtung für die Sharpe Ratio,
- Startwert und High-Water-Mark bei Drawdowns,
- Datenkalender und unterschiedliche Handelstage,
- BIP-Daten und deren zeitliche Verfügbarkeit,
- sinnvolle automatisierte Tests.

Untersuche auch die aktuelle Python-/Projektumgebung und nenne Abhängigkeiten, die für die Engine tatsächlich notwendig sind. Neue Bibliotheken sollen nur vorgeschlagen werden, wenn sie einen klaren Nutzen haben. Die vorhandenen mathematischen Funktionen sollen nicht ohne Grund durch externe Backtesting-Frameworks ersetzt werden.

ERSTELLE AUSSCHLIESSLICH FOLGENDE DOKUMENTATION:

1. `documentation/engine/audit.md`

Diese Datei soll enthalten:

- gelesene Dateien und relevante Kapitel,
- zusammengefasste bereits festgelegte Anforderungen,
- Zuordnung:
  Anforderung -> bestehende Funktion -> nötige Integration/Erweiterung -> geplanter Test,
- erkannte Widersprüche oder Risiken,
- vorgeschlagene technische Architektur innerhalb des in Kapitel 5.8 beschriebenen Rahmens,
- notwendige Abhängigkeiten,
- vorgeschlagene Implementierungsreihenfolge,
- Kriterien, anhand derer die Engine später als technisch fertig gelten kann.

2. `documentation/engine/open-decisions.md`

Jede offene Entscheidung soll folgende Struktur besitzen:

- ID
- Frage
- Warum die Entscheidung notwendig ist
- Betroffene Kapitel/Funktionen
- mögliche Optionen
- technische bzw. methodische Auswirkungen
- deine Empfehlung
- Klassifikation:
  - BLOCKING = muss vor der Implementierung geklärt werden
  - NON-BLOCKING = kann später entschieden werden

Keine offene fachliche Entscheidung selbst endgültig treffen.

3. Ergänze am Ende einen sachlichen Eintrag in
   `documentation/ai-usage/ai-usage-log.md`
   für genau diesen Audit.

NICHT ERLAUBT IN DIESEM SCHRITT:

- keine Änderungen an `src/`,
- keine Änderungen an Theorie oder Analyse,
- keine Änderungen an `methodik.qmd`,
- keine endgültige Auswahl von Wertpapieren,
- keine endgültige Auswahl des Untersuchungszeitraums,
- keine endgültige Auswahl von SMA-Parametern,
- keine Implementierung der Engine,
- keine Änderung bestehender mathematischer Definitionen.

Führe am Ende selbst `git diff` aus und bestätige ausdrücklich, dass ausser der erlaubten Dokumentation keine Dateien verändert wurden.

Deine Abschlussantwort soll nur zusammenfassen:

1. welche Dokumentationsdateien erstellt/geändert wurden,
2. wie viele BLOCKING-Entscheidungen gefunden wurden,
3. welche davon besonders wichtig sind,
4. ob Widersprüche im bestehenden Code gefunden wurden,
5. ob ausser Dokumentation irgendetwas verändert wurde.

Danach STOPPEN. Noch nichts implementieren.