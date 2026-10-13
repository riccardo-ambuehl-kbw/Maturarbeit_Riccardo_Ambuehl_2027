# Nachtrag der historischen KI-Nutzung – 13. Oktober 2026

Dieser Nachtrag verbindet das Engine-Log mit dem KI-Anhang des Quarto-Buchs. Grundlage sind 14 archivierte Codex-Prompts, die zugehörigen Entwicklungs-/Studienberichte, die Git-Historie, 45 geteilte ChatGPT-Einzelantworten und die ergänzenden historischen Angaben im aktuellen Auftrag. Der Nachtrag betrifft die Dokumentation der KI-Leistungen. Die persönliche Arbeitsdokumentation wird nicht erweitert; der Verantwortungsabsatz steht am Ende des KI-Anhangs.

## Datierung und Nachweisgrenzen

- Historische Einsätze wurden am 13.10.2026 nachgetragen. Das Abrufdatum der ChatGPT-Quellen ist kein Datum der damaligen Prüfung.
- Der Core-Prompt ist mit 02.10.2026 beschriftet; Engine-Log und Commit `1a19309` dokumentieren die Umsetzung am 03.10.2026. Die Reihenfolge am 04.10.2026 folgt den Prompt-/Review-Commits, nicht der alphabetischen Dateiliste.
- Die Studienprüfungen vom 08./09./10.10.2026 sind nun durch die fünf tatsächlich vorhandenen neuen Share-Links belegt. Die ungefähre Uhrzeit 04:15 Uhr Schweizer Zeit stammt aus der ergänzenden historischen Angabe; die Share-Antwort selbst enthält keinen genauen Prüfzeitstempel.
- Eigenständige Gegenrechnungen durch ChatGPT sind von einer Wiederholung der originalen Backtests zu unterscheiden. Bei der Freeze-Prüfung wurden laut Antwort tatsächlich Konfigurationen mit der archivierten Engine geladen und statische Kontexte geprüft; deshalb wird dort keine vollständige Nichtausführung von Engine-Code behauptet.
- 25 Ergebnisdateien plus fünf Run-Manifeste erklären die 30 Dateien der Ergebnisordner. Die elf Strategie-Zeitreihen sind keine elf getrennten Hauptläufe.
- Hinweise zu künftigen Kapiteln und Formulierungen sowie ChatGPTs „wir“ werden als Vorschläge eingeordnet; eine automatische oder wörtliche Übernahme wird daraus nicht abgeleitet.
- R-017 vom 13.10.2026 bleibt teilweise geschlossen: intakte Archiv-/Daten-/Ergebnishashes, aber 23 CRLF-/LF-Abweichungen der heutigen Codearbeitskopie sowie historische Herkunfts-/Umgebungsgrenzen. Kein neuer Backtest oder neuer Finanzdaten-Audit wurde für diesen Dokumentationsnachtrag ausgeführt.

## Vollständige Codex-Prompts in chronologischer Reihenfolge

Alle Links verweisen auf tatsächlich vorhandene Dateien im unveränderlichen Git-Stand `1954bfbcb257b51e7f9174aa824cb35e437de752`. Beide lokalen Ordner sind Checkouts desselben GitHub-Repositorys; der Engine-Ordner ist kein separates GitHub-Repository. Die Originalprompts werden nicht in den Buchanhang kopiert.

| Historischer Einsatz | Prompt | KI-Leistung / Ergebnis |
|---|---|---|
| 2026-10-02 | [Audit vor der Implementierung](https://github.com/riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027/blob/1954bfbcb257b51e7f9174aa824cb35e437de752/documentation/ai-usage/prompts/2026-10-02-engine-audit.md) | Anforderungen, Architektur, Gegenbeispiele und 13 offene Regeln dokumentiert; keine Implementierung. |
| 2026-10-03 | [Kernimplementierung](https://github.com/riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027/blob/1954bfbcb257b51e7f9174aa824cb35e437de752/documentation/ai-usage/prompts/2026-10-02-engine-v1-core-implementation.md) | Paket, lokale Datenvalidierung, Buy-and-Hold, Kennzahlen, Exporte und 93 Tests; Promptkopf noch 02.10., Umsetzung im Log/Git am 03.10. |
| 2026-10-04 | [Multi-Asset und Rebalancing](https://github.com/riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027/blob/1954bfbcb257b51e7f9174aa824cb35e437de752/documentation/ai-usage/prompts/2026-10-04-engine-v1-rebalancing-implementation.md) | Gewichtungsdrift, jährliche Umschichtungen, Gewichte/Trades und 71 neue Tests; insgesamt 164. |
| 2026-10-04 | [SMA-Trendfolge](https://github.com/riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027/blob/1954bfbcb257b51e7f9174aa824cb35e437de752/documentation/ai-usage/prompts/2026-10-04-engine-v1-trend-implementation.md) | Signal-/Performance-Trennung, Vorlauf, Lag 1, unverzinstes Cash und 78 neue Tests; insgesamt 242. |
| 2026-10-04 | [Historische BIP-Ländergewichtung](https://github.com/riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027/blob/1954bfbcb257b51e7f9174aa824cb35e437de752/documentation/ai-usage/prompts/2026-10-04-engine-v1-country-weighting-implementation.md) | As-of-Versionen, gemeinsames BIP-Jahr, initiale/jährliche Gewichte und 102 neue Tests; insgesamt 344. |
| 2026-10-04 | [Gesamtaudit](https://github.com/riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027/blob/1954bfbcb257b51e7f9174aa824cb35e437de752/documentation/ai-usage/prompts/2026-10-04-engine-v1-final-audit.md) | Zusätzliche Gegenbeispiele, Paket-/Demo-Prüfung; drei technische Engine-Blocker dokumentiert. |
| 2026-10-04 | [Blocker-Korrekturen](https://github.com/riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027/blob/1954bfbcb257b51e7f9174aa824cb35e437de752/documentation/ai-usage/prompts/2026-10-04-engine-v1-blocker-fixes.md) | Allokationsunterläufe, Result-/Exportvertrag und CSV-Zeilenbreite korrigiert; 406 Tests. |
| 2026-10-04 | [Portfoliozustands-Korrektur](https://github.com/riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027/blob/1954bfbcb257b51e7f9174aa824cb35e437de752/documentation/ai-usage/prompts/2026-10-04-engine-v1-portfolio-state-validation-fix.md) | Resultate mit Markt-/Portfoliozustandsfolge abgeglichen; 428 Tests. |
| 2026-10-04 | [Blocker-Re-Audit](https://github.com/riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027/blob/1954bfbcb257b51e7f9174aa824cb35e437de752/documentation/ai-usage/prompts/2026-10-04-engine-v1-blocker-reaudit.md) | Neue NUL-Feldkürzung nachgewiesen; Freeze noch nicht empfohlen. |
| 2026-10-04 | [CSV-NUL-Korrektur](https://github.com/riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027/blob/1954bfbcb257b51e7f9174aa824cb35e437de752/documentation/ai-usage/prompts/2026-10-04-engine-v1-csv-nul-fix.md) | NUL-haltige Eingaben vor Parsing abgelehnt; 13 neue Tests, insgesamt 441. |
| 2026-10-04 | [Finaler Freeze-Re-Audit](https://github.com/riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027/blob/1954bfbcb257b51e7f9174aa824cb35e437de752/documentation/ai-usage/prompts/2026-10-04-engine-v1-final-freeze-reaudit.md) | Dokumentierte Engine-Blocker im gezielt geprüften Umfang geschlossen; keine pauschale Echtdatenfreigabe. |
| 2026-10-04 | [Release und technischer Freeze](https://github.com/riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027/blob/1954bfbcb257b51e7f9174aa824cb35e437de752/documentation/ai-usage/prompts/2026-10-04-engine-v1-release-freeze.md) | Version 1.0.0, 441 Quell-/441 Wheeltests und Offline-Demos dokumentiert; noch keine reale Studie. |
| 2026-10-10 | [Datenadapter und Originaldatenprüfung](https://github.com/riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027/blob/1954bfbcb257b51e7f9174aa824cb35e437de752/documentation/ai-usage/prompts/2026-10-10-study-v1-data-adapter.md) | Zwölf normalisierte Artefakte, Originaldaten-/Provenienz-Gegenrechnungen und 30 Adaptertests; keine Backtests. |
| 2026-10-10 | [Freeze-Vorbereitung und statische Config-Prüfung](https://github.com/riccardo-ambuehl-kbw/Maturarbeit_Riccardo_Ambuehl_2027/blob/1954bfbcb257b51e7f9174aa824cb35e437de752/documentation/ai-usage/prompts/2026-10-10-study-v1-freeze-preparation.md) | Fünf Configs, Archiv mit 123 Dateien/122 inventarisierten Hashes und 16 Freeze-Tests; keine Backtests. |

## Zuordnung aller 45 ChatGPT-Quellen

24 der älteren Antworten wurden anhand lokaler Zotero-Snapshots gelesen; die übrigen 16 älteren und fünf neu ergänzten Antworten wurden im angemeldeten Browser geöffnet. Allgemeine Empfehlungen in diesen Antworten gelten als historische Quelleninhalte, nicht als neue Arbeitsaufträge.

| Historischer Zeitraum | BibTeX-Key / geteilte Antwort | Verwendung im Nachtrag |
|---|---|---|
| 2026-10-02 | [ChatGPTGeteilterInhalt](https://chatgpt.com/s/t_6acd8441b0fc81918f751e8eb334a2cc) | Planung, Audit-Ablauf und Entscheidungsvorschläge |
| 2026-10-02 | [ChatGPTGeteilterInhalta](https://chatgpt.com/s/t_6acd84c0f1748191b6431744f2b3886b) | Planung, Audit-Ablauf und Entscheidungsvorschläge |
| 2026-10-02 | [ChatGPTGeteilterInhaltb](https://chatgpt.com/s/t_6acd851e7d7881918b55b8a1931af8a9) | Planung, Audit-Ablauf und Entscheidungsvorschläge |
| 2026-10-02 | [ChatGPTGeteilterInhaltc](https://chatgpt.com/s/t_6acd857650848191834bc1a507108c38) | Planung, Audit-Ablauf und Entscheidungsvorschläge |
| 2026-10-02 | [ChatGPTGeteilterInhaltd](https://chatgpt.com/s/t_6acd86090c7c8191ae2ee2c950c41b57) | Planung, Audit-Ablauf und Entscheidungsvorschläge |
| 2026-10-02 | [ChatGPTGeteilterInhalte](https://chatgpt.com/s/t_6acd867ccf3c81918d2111ca1a6d0909) | Planung, Audit-Ablauf und Entscheidungsvorschläge |
| 2026-10-03 | [ChatGPTGeteilterInhaltf](https://chatgpt.com/s/t_6acd869b5a9c8191870f50d701c06cc1) | Core-Kontrollen und Code-Review |
| 2026-10-03 | [ChatGPTGeteilterInhaltg](https://chatgpt.com/s/t_6acd86de8c2481919f9cd9bc933db1ac) | Core-Kontrollen und Code-Review |
| 2026-10-03 | [ChatGPTGeteilterInhalth](https://chatgpt.com/s/t_6acd86fe9af481919cc18b1eaffe62d0) | Core-Kontrollen und Code-Review |
| 2026-10-03 | [ChatGPTGeteilterInhalti](https://chatgpt.com/s/t_6acd870fc7c48191a9fde49f87e389f2) | Core-Kontrollen und Code-Review |
| 2026-10-04 | [ChatGPTGeteilterInhaltj](https://chatgpt.com/s/t_6acd8728159c819181c4b11407d9612a) | Rebalancing-Prompt, Kontrollen und Review |
| 2026-10-04 | [ChatGPTGeteilterInhaltk](https://chatgpt.com/s/t_6acd873acedc8191afa783c17195e04d) | Rebalancing-Prompt, Kontrollen und Review |
| 2026-10-04 | [ChatGPTGeteilterInhaltl](https://chatgpt.com/s/t_6acd877bc82481919581e8bcf9a5027c) | Rebalancing-Prompt, Kontrollen und Review |
| 2026-10-04 | [ChatGPTGeteilterInhaltm](https://chatgpt.com/s/t_6acd878f254c8191b0a8d33b9c2394d8) | Rebalancing-Prompt, Kontrollen und Review |
| 2026-10-04 | [ChatGPTGeteilterInhaltn](https://chatgpt.com/s/t_6acd8b35011c8191b7f36a01b167de4a) | Trendfolge-Prompt, Kontrollen und Review |
| 2026-10-04 | [ChatGPTGeteilterInhalto](https://chatgpt.com/s/t_6acd8b48605c8191b4bb390f8aabc5b1) | Trendfolge-Prompt, Kontrollen und Review |
| 2026-10-04 | [ChatGPTGeteilterInhaltp](https://chatgpt.com/s/t_6acd8b567704819191935cd2baf30030) | Trendfolge-Prompt, Kontrollen und Review |
| 2026-10-04 | [ChatGPTGeteilterInhaltq](https://chatgpt.com/s/t_6acd8b69f28c8191b5407ddb25ab6506) | Trendfolge-Prompt, Kontrollen und Review |
| 2026-10-04 | [ChatGPTGeteilterInhaltr](https://chatgpt.com/s/t_6acd8b8235648191ab881e49cb4dfcc0) | BIP-Prompt, Kontrollen und Review |
| 2026-10-04 | [ChatGPTGeteilterInhalts](https://chatgpt.com/s/t_6acd8b97fbb8819190ba29eef74ebfc0) | BIP-Prompt, Kontrollen und Review |
| 2026-10-04 | [ChatGPTGeteilterInhaltt](https://chatgpt.com/s/t_6acd8bc54d78819192d15265a65bd880) | BIP-Prompt, Kontrollen und Review |
| 2026-10-04 | [ChatGPTGeteilterInhaltu](https://chatgpt.com/s/t_6acd8bd881c881918da6540384acc7d0) | BIP-Prompt, Kontrollen und Review |
| 2026-10-04 | [ChatGPTGeteilterInhaltv](https://chatgpt.com/s/t_6acd8bf2ddf88191855f52573868cfe5) | Gesamtaudit-Prompt und Einordnung der Blocker |
| 2026-10-04 | [ChatGPTGeteilterInhaltw](https://chatgpt.com/s/t_6acd8c071d688191a35d8a08773a409c) | Gesamtaudit-Prompt und Einordnung der Blocker |
| 2026-10-04 | [ChatGPTGeteilterInhaltx](https://chatgpt.com/s/t_6acd8c19d8388191b20ba6a135b7d196) | Blocker-Fix, Portfoliozustands-Fix und Reviews |
| 2026-10-04 | [ChatGPTGeteilterInhalty](https://chatgpt.com/s/t_6acd8c2de0708191bb233e4f7afc157b) | Blocker-Fix, Portfoliozustands-Fix und Reviews |
| 2026-10-04 | [ChatGPTGeteilterInhaltz](https://chatgpt.com/s/t_6acd8c44a9a48191ac15d84e954e3c3e) | Blocker-Fix, Portfoliozustands-Fix und Reviews |
| 2026-10-04 | [ChatGPTGeteilterInhaltaa](https://chatgpt.com/s/t_6acd8c57a66c8191b16bc21ee0532b05) | Blocker-Fix, Portfoliozustands-Fix und Reviews |
| 2026-10-04 | [ChatGPTGeteilterInhaltab](https://chatgpt.com/s/t_6acd8c7267c48191bba7a927ff307f98) | Blocker-Fix, Portfoliozustands-Fix und Reviews |
| 2026-10-04 | [ChatGPTGeteilterInhaltac](https://chatgpt.com/s/t_6acd8c813cd48191b35fabd10aea02b8) | Blocker-Fix, Portfoliozustands-Fix und Reviews |
| 2026-10-04 | [ChatGPTGeteilterInhaltad](https://chatgpt.com/s/t_6acd8c96f5c081918b851992aa3f43ac) | Re-Audit, CSV-NUL-Fix und Review |
| 2026-10-04 | [ChatGPTGeteilterInhaltae](https://chatgpt.com/s/t_6acd8ca720508191a30c5abacf74a4ba) | Re-Audit, CSV-NUL-Fix und Review |
| 2026-10-04 | [ChatGPTGeteilterInhaltaf](https://chatgpt.com/s/t_6acd8ccc4dc48191b55fe2bbbc9ac5c5) | Re-Audit, CSV-NUL-Fix und Review |
| 2026-10-04 | [ChatGPTGeteilterInhaltag](https://chatgpt.com/s/t_6acd8cddc6e481918e85ba761be09802) | Re-Audit, CSV-NUL-Fix und Review |
| 2026-10-04 | [ChatGPTGeteilterInhaltah](https://chatgpt.com/s/t_6acd8cefd8b881919ee1b191bfd1b554) | Freeze-Re-Audit, Release, Tagprüfung und Ausblick |
| 2026-10-04 | [ChatGPTGeteilterInhaltai](https://chatgpt.com/s/t_6acd8cfc67b481919d5728be71b9adfe) | Freeze-Re-Audit, Release, Tagprüfung und Ausblick |
| 2026-10-04 | [ChatGPTGeteilterInhaltaj](https://chatgpt.com/s/t_6acd8d0b53048191a5dab58096e2e540) | Freeze-Re-Audit, Release, Tagprüfung und Ausblick |
| 2026-10-04 | [ChatGPTGeteilterInhaltak](https://chatgpt.com/s/t_6acd8d179ea48191a85fa762da686595) | Freeze-Re-Audit, Release, Tagprüfung und Ausblick |
| 2026-10-04 | [ChatGPTGeteilterInhaltal](https://chatgpt.com/s/t_6acd8d3437ac81919e8220fefc55d992) | Freeze-Re-Audit, Release, Tagprüfung und Ausblick |
| 2026-10-04 | [ChatGPTGeteilterInhaltam](https://chatgpt.com/s/t_6acd8d620e4881919698680a05a0f0c4) | Freeze-Re-Audit, Release, Tagprüfung und Ausblick |
| 2026-10-08 | [ChatGPTGeteilterInhaltao](https://chatgpt.com/s/t_6acd98ec15f88191b6b7108cd5a58da0) | Rohdaten-Eingangsprüfung ETF/FRED und zwei WEO-Ausgaben |
| 2026-10-09 | [ChatGPTGeteilterInhaltan](https://chatgpt.com/s/t_6acd9b6c4aac8191b733f8cb425fc218) | Eingangsprüfung der 16 historischen WEO-Ausgaben |
| 2026-10-10 | [ChatGPTGeteilterInhaltap](https://chatgpt.com/s/t_6acda7ebe8608191acca957223db0fa0) | Unabhängige Prüfung der normalisierten Study-v1-Daten |
| 2026-10-10 | [ChatGPTGeteilterInhaltaq](https://chatgpt.com/s/t_6acda86619608191a7289c979bcfe389) | Unabhängige Prüfung des Freeze-Kandidaten |
| 2026-10-10 | [ChatGPTGeteilterInhaltar](https://chatgpt.com/s/t_6acda9395eac8191ae1a12850817f3a7) | Gegenrechnung der echten Hauptläufe H1/K1/Z1/S1/S2 |

## Lokal vorhandene historische ChatGPT-Berichte

Die folgenden vier Dateien wurden im Engine-Ordner gefunden und gelesen. Sie waren bereits vor diesem Nachtrag unversioniert vorhanden und werden weder geändert noch als bereits auf GitHub veröffentlicht dargestellt. Die Zuordnung zu ChatGPT ist durch den aktuellen Auftrag und die jeweils passende geteilte Antwort belegt.

- [weo-eingangspruefung.md](<C:/Users/modic/Documents/GitHub/Maturarbeit_Engine/documentation/study_v1/weo-eingangspruefung.md>) — SHA-256 `2d95d18651d049c80a8592802e04890a26eb9d001a536977241301bafdf6781a`.
- [study-v1-independent-review.md](<C:/Users/modic/Documents/GitHub/Maturarbeit_Engine/documentation/study-v1-independent-review.md>) — SHA-256 `dec3765dbff93015191dd7dbdc09cb401fe8398a94f8a82f11985d614fc0a497`.
- [study_v1_freeze_2026-10-10.md](<C:/Users/modic/Documents/GitHub/Maturarbeit_Engine/documentation/study_v1_freeze_2026-10-10.md>) — SHA-256 `7e8b9fd7b82631b8b44265e0fb41905455e8b26de9591c2445dbebbc0ee8dba7`.
- [Study_v1_Hauptlaeufe_Unabhaengige_Pruefung_2026-10-10 (1).md](<C:/Users/modic/Documents/GitHub/Maturarbeit_Engine/documentation/Study_v1_Hauptlaeufe_Unabhaengige_Pruefung_2026-10-10 (1).md>) — SHA-256 `13109bd6f04b891d0a709bffcd155899392cc64952ca01137e71579a59b4aa50`.

Eine zusätzliche Hauptlauf-Berichtkopie liegt in Downloads. Der Rohdaten-Prüfbericht vom 08.10.2026 und das WEO-JSON-Prüfregister sind in den geteilten Antworten als erstellte Dateien erkennbar; eine aktuelle lokale Kopie wurde bei der gezielten Suche in den beiden Repositorys und Downloads nicht gefunden. Ihre historischen Inhalte werden daher über die tatsächlichen Share-Quellen belegt, ohne einen lokalen Dateilink zu erfinden.

## Änderungen und Prüfung dieses Nachtrags

- `ki-nutzung.qmd`: Einleitung/Grundsätze auf beide Tools erweitert, kurze Einordnung der ChatGPT-Ausdrucksweise ergänzt, historische Schritte vor dem 11.10.2026 eingesetzt, R-017 und diesen Nachtrag ergänzt, vorhandenen Verantwortungsabsatz an das Ende verschoben.
- `documentation/ai-usage/ai-usage-log.md`: heutige Dokumentationsarbeit und nachträgliche historische Übersicht ergänzt; bisherige Logbytes bleiben erhalten.
- Der tatsächliche Auftrag und seine Ergänzungen sind unter `documentation/ai-usage/prompts/2026-10-13-ki-dokumentation-nachtrag.txt` dokumentiert.
- Bereits vorhandene Änderungen an `references.bib` und `notebooks/Anhang_Tests_Validierung.ipynb` stammen vom Ausgangsstand und werden erhalten. Der Bibliografieexport hatte den bereits im Theoriekapitel zitierten Eintrag `spdjThe500` entfernt. Nach der Citeproc-Warnung wurde genau dieser bestehende Eintrag unverändert aus HEAD wieder angehängt; sämtliche neu importierten Quellen bleiben erhalten. Der Engine-Checkout, Originalprompts, Rohdaten, Configs und Studienergebnisse werden nicht verändert.
- Die technischen Endprüfungen und Rendernachweise werden nach dem Renderlauf unten ergänzt.

## Abschliessende technische Prüfungen

- Alle 14 Engine-Promptdateien lokal und mit `git cat-file -e` im verlinkten unveränderlichen Commit bestätigt; alle 45 ChatGPT-Keys im Anhang auflösbar.
- Historische Logzeilen bleiben als ursprüngliches Bytepräfix erhalten; die neue historische Tabelle ordnet insbesondere am 10.10. den Codex-Adapter vor die ChatGPT-Datenprüfung und die Codex-Freeze-Vorbereitung vor die ChatGPT-Freeze-/Run-Prüfung.
- Endgültiger HTML-Render: Exit 0, elf Buchseiten, 1649 lokale Link-/Ankervorkommen, null ungültige Ziele. Alle 45 ChatGPT-Keys sind in der gerenderten KI-Seite aufgelöst. Navigation und Inhaltsverzeichnis enthalten Anhang D und die neuen Abschnitte.
- Endgültiger PDF-Render: Exit 0, 116 A4-Seiten, KI-Anhang auf physischen Seiten 103–116. Alle 45 Share-URLs sind als tatsächliche PDF-Linkziele enthalten. PNG-Sichtprüfung des gesamten KI-Anhangs und Detailkontrolle von Inhaltsverzeichnis, Daten-/Freeze-Prüfungen sowie letzter Seite; lange neue Überschriften wurden verkürzt und endgültig ohne Überlappung geprüft.
- Beide Formate wurden in einer externen vollständigen Projektkopie mit deaktivierter Ausführung, Freeze und Cache sowie `--no-execute --no-cache` erstellt. Kein Notebook-Code, keine Engine-Funktion, historische Tests oder Backtests ausgeführt. DOCX wurde in diesem Dokumentationsauftrag nicht neu gerendert.
- Lesbare PDF-Prüffassung: [KI-Nachtrag-Prueffassung-2026-10-13.pdf](../../KI-Nachtrag-Prueffassung-2026-10-13.pdf). Die bisherigen 70 Ausgabe-/Freeze-/Cachedateien bleiben byteidentisch; die neue Prüffassung ersetzt keine bestehende Ausgabe.
- Alle übrigen versionierten Hauptdateien einschliesslich der bereits bearbeiteten Prüfanhang-Datei sowie sämtliche erfassten Engine-Dateien, die vier dort vorhandenen unversionierten ChatGPT-Berichte, Prompts, Configs und Studienresultate bleiben gegenüber dem gesicherten Ausgangsstand unverändert. HEAD und Git-Index bleiben unverändert; kein Commit, Push, Tag oder Änderung der Git-Konfiguration.
