# Arbeitsanweisung: KI-Nutzungslog in die Buchversion übernehmen

## Kurzname

`KI-DOKUMENTATION-BUCH-SYNC`

## Aufruf für spätere Aktualisierungen

> Führe `KI-DOKUMENTATION-BUCH-SYNC` aus.

## Bedeutung

Bei diesem Auftrag ist `documentation/ai-usage/ai-usage-log.md` der ausführliche, laufende Nachweis. `ki-nutzung.qmd` ist die für Leserinnen und Leser aufbereitete Fassung im Anhang des Quarto-Books.

1. Zuerst prüfen, ob alle seit dem letzten Abgleich erfolgten KI-Einsätze im ausführlichen Log eingetragen sind.
2. Fehlende Einsätze mit Datum, Tool, Zweck, Ergebnis, übernommenen Teilen, manueller Kontrolle und klarer Abgrenzung der KI-Leistung ergänzen.
3. Danach `ki-nutzung.qmd` aktualisieren, sodass jeder Logeintrag in verständlicher und sachlich korrekter Form berücksichtigt ist.
4. Keine KI-Nutzung erfinden, verallgemeinern oder stärker darstellen, als sie im Log dokumentiert ist.
5. Deutlich unterscheiden zwischen technischer Unterstützung, Übertragung vorhandener Inhalte, sprachlicher Korrektur, Umformulierung und fachlicher Inhaltserstellung.
6. Einschränkungen und die manuelle Verantwortung des Autors beibehalten.
7. Prüfen, ob `ki-nutzung.qmd` in `_quarto.yml` unter `book: appendices:` eingebunden ist.
8. Die Buchversion rendern und kontrollieren, ob der Anhang in Navigation, Inhaltsverzeichnis und Ausgabe korrekt erscheint.
9. Auch den jeweiligen Abgleich selbst im KI-Nutzungslog dokumentieren, wenn Codex ihn ausgeführt hat.

Diese Datei dokumentiert einen wiederverwendbaren Arbeitsablauf. Sie ist kein automatisch ausführbares Skript.
