# Arbeitsanweisung: README in die Überblick-Seite übernehmen

## Kurzname

`README-ÜBERBLICK-SYNC`

## Aufruf für spätere Aktualisierungen

> Führe `README-ÜBERBLICK-SYNC` aus.

## Historischer Ablauf der vollständigen Übertragung

Die folgenden Schritte dokumentieren die frühere vollständige Übertragung. Nach Kürzungsstufe 1 gilt für neue Synchronisationen der nachfolgende aktuelle Ablauf.

Bei diesem damaligen Auftrag ist `README.md` die Quelle und `index.ipynb` die Überblick-Seite des Quarto-Books. Die frühere QMD-Fassung liegt unverändert unter `archive/index.qmd`.

1. Alle Inhalte aus `README.md` in die Markdown-Zellen von `index.ipynb` übernehmen. Codebeispiele bleiben als Markdown-Codeblöcke erhalten und werden nicht als ausführbare Notebook-Zellen übernommen.
2. Den Titel `Überblick` in der ersten Raw-Zelle als Quarto-YAML-Frontmatter beibehalten; die Hauptüberschrift `# Maturarbeit` aus der README nicht zusätzlich einfügen. Die Abschnittsüberschriften wie in den übrigen Notebooks als HTML-Überschriften mit den Nummern `1.1`, `1.2` usw. beziehungsweise `1.x.1`, `1.x.2` usw. setzen.
   Die zweite Raw-Zelle mit `raw_mimetype: text/html` und `<h1>1 Überblick</h1>` ebenfalls beibehalten. Sie stellt den Kapiteltitel auf der HTML-Startseite dar. PDF und Word erzeugen den Kapiteltitel aus der ersten Titelzelle; eine zusätzliche Markdown-Hauptüberschrift würde dort ein zweites Kapitel erzeugen.
3. Den vorhandenen Text nicht fachlich umschreiben, erweitern oder als KI-generierten Inhalt ausgeben. Nur die für Quarto nötige Formatierung anpassen.
4. Nach der Übernahme prüfen, ob alle Überschriften, Absätze, Listen, Links und Codeblöcke der README in `index.ipynb` enthalten sind. Die zusätzliche Nummerierung und die Titelzelle dürfen die übrigen Inhalte nicht verändern.
5. Den Vorgang mit Datum im KI-Nutzungslog unter `documentation/ai-usage/ai-usage-log.md` dokumentieren. Dabei ausdrücklich festhalten, dass Codex die Inhalte nicht verfasst, sondern nur aus der README in die Buchversion übertragen hat.
6. Wenn sich Quell- und Zieltext widersprechen oder unklar ist, welche Version gelten soll, vor einer inhaltlichen Änderung nachfragen.

Diese Datei dokumentiert einen wiederverwendbaren Arbeitsablauf. Sie ist kein automatisch ausführbares Skript.


## Aktueller Ablauf ab Kürzungsstufe 1 vom 12. Oktober 2026

Kapitel 1 in `index.ipynb` ist jetzt eine kurze wissenschaftliche Überblicksseite. Die ausführliche technische Projektdokumentation steht in `notebooks/Anhang_Technische_Engine.ipynb`, Abschnitt A.7. Die frühere vollständige README-Übertragung bleibt oben als historischer Vorgang dokumentiert.

1. Wissenschaftlichen Überblick und technische Dokumentation getrennt synchronisieren. `index.ipynb` enthält Forschungsfrage, Untersuchungsweg und Buchaufbau; **nicht sämtliche README-Abschnitte automatisch wieder einfügen**.
2. Beide ursprünglichen Raw-Titelzellen des Überblicks und die wortgleiche Forschungsfrage erhalten. Wissenschaftliche Änderungen nur im ausdrücklich beauftragten Umfang übernehmen.
3. Installation, Quarto-/Zotero-Anleitungen, historische Quellen-/Werkzeugplanung und Pendenzen dem Bereich A.7 zuordnen. Bereits vorhandene Originalstände nicht überschreiben oder als aktuelle Konfiguration ausgeben. Bei neuen technischen Angaben einen datierten Nachtrag statt einer stillen historischen Ersetzung erstellen.
4. Die aktuelleren übernommenen Notebook-Pendenzen nicht durch ältere README-Checkboxen ersetzen. Bei ungeklärten widersprüchlichen neuen Angaben den geltenden Stand klären.
5. Danach aktuelle Nummern/Verweise, die Trennung der beiden Bereiche und den Schutz historischer Nachweise prüfen. Den konkreten Vorgang sachlich im KI-Log und Buch dokumentieren.

Die README bleibt eine Repository-Einstiegsseite. Dieser Ablauf verlangt keine allgemeine README-Überarbeitung und keine erneute Vollkopie in den wissenschaftlichen Haupttext.
