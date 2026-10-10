# Study-v1: Autorenfreigabe, finale Configs und Freeze-Vorbereitung

**Datum:** 2026-10-10. **Status:** `FREEZE_CANDIDATE_READY_FOR_GIT_SEAL`.
Auftrag: [vollständiger Autorenauftrag](ai-usage/prompts/2026-10-10-study-v1-freeze-preparation.md).
Die Daten und Methoden sind vom Autor akzeptiert; technische Prüfungen bestanden. Git-Versiegelung und echte Hauptläufe stehen aus.

## A–B. Freigegebener Datenstand und Hashprüfung

Der verbindliche SHA-256 von `data/study_v1/processed/processed_manifest.json` ist bestätigt:
`948865ea3302ced267c9828b9a459ba03cd1c62971c070a818fd4c356c629c28`.
Alle **54 ursprünglichen Rohdateien** und **zwölf Processed-Artefakte** wurden anhand des akzeptierten Manifests in SHA-256, Dateigrösse und vollständigem Inventar geprüft; die tatsächlichen Aufbereitungsskript-/Registerhashes ebenfalls.
Keine Datenaufbereitung oder Nachbearbeitung ausgeführt. Insbesondere behalten die historischen Processed-Berichte ihren damaligen Status bytegleich; die spätere ausdrückliche Autorenentscheidung steht im [neuen Freigabenachweis](study-v1-author-approval.md).

Ausgangsbranch `study-v1`, HEAD `9b2bf65e2989b97d8ceea23393e0a271998bb09a`; Tag `engine-v1.0` löst exakt zum erwarteten Commit `4a98f3a1039c6ebf4f1bfa1202a1af2e8064b023` auf.
Der ursprüngliche Workspace enthielt bereits das ergänzte KI-Log und fünf neue Adapter-/Dokumentationsdateien. Deren Inhalte wurden vollständig geschützt, nicht zurückgesetzt.

## C. Neue und geänderte Dateien

Neu in diesem Auftrag:

- `configs/study_v1/H1.json`, `K1.json`, `Z1.json`, `S1.json`, `S2.json`.
- `documentation/study-v1-author-approval.md`, dieser Bericht und `documentation/study-v1-freeze-seal.md`.
- `documentation/ai-usage/prompts/2026-10-10-study-v1-freeze-preparation.md` als vollständige Auftragskopie.
- `scripts/study_v1/verify_freeze.py` als wiederverwendbare reine Prüfhilfe und `tests/study_v1/test_freeze.py` mit 16 fokussierten Fällen.
- `.gitattributes`, ausschliesslich LF-Regeln für Study-v1-Skripte, Register, Configs, Tests und zugehörige Nachweise. Der tatsächlich gesetzte Wert `core.autocrlf=true` könnte sonst nach einem Checkout die freigegebenen Byte-Hashes ändern. Alle betroffenen Dateien hatten bereits LF; keine Originalbytes wurden umgeschrieben.

Bestehende Dateien: `.gitignore` ausschliesslich um lokale Study-Umgebung, Raw, Processed, Archiv und temporäre Adapterkandidaten ergänzt; `outputs/runs/` und alle bisherigen Einträge erhalten. KI-Log um einen Eintrag ergänzt, bisherige Bytes als vollständiges Präfix erhalten.
Engine, bestehende Engine-/Adaptertests, wissenschaftliche Dateien, Auditnachweise, Originalskripte/Register und freigegebene Daten bleiben bytegleich. Keine Abhängigkeit installiert oder Engine-Version gebaut.

## D–E. Fünf endgültige Untersuchungskonfigurationen

Alle: Schema **1.0**, Startkapital **100’000 USD**, Basiswährung **USD**, **ME**, **12** Perioden pro Jahr, `output_dir=../../outputs/runs`.
Sämtliche aktivierten Rebalancing-Modelle sind `annual`. Sämtliche Trendvarianten haben `signal_lag=1` und `signal_source=performance_value`.

| Config | Startbewertung bis Ende | Bewertungen / RF-Perioden | Ausschliesslich aktivierte Strategien |
|---|---|---:|---|
| H1 | 2009-12-31 bis 2025-12-31 | 193 / 192 | Buy-and-Hold WORLD_EQ; jährliches WORLD_EQ/IEF 60/40; WORLD_EQ SMA 3/12 Long/Cash; historische G7-BIP-Gewichtung |
| K1 | 2009-12-31 bis 2025-12-31 | 193 / 192 | Jährliches Fixed Rebalancing der sieben Länderproxies, jedes Gewicht 1/7; dieselbe historische G7-BIP-Gewichtung wie H1 |
| Z1 | **2002-12-31** bis 2025-12-31 | 277 / 276 | Buy-and-Hold US_EQ; jährliches US_EQ/IEF 60/40; US_EQ SMA 3/12 Long/Cash; kein BIP-Modell |
| S1 | 2009-12-31 bis 2025-12-31 | 193 / 192 | Nur WORLD_EQ SMA **2/12** Long/Cash |
| S2 | 2009-12-31 bis 2025-12-31 | 193 / 192 | Nur WORLD_EQ SMA **6/12** Long/Cash |

IEF ist `US_TREASURY_7_10`. Länderzuordnung H1/K1: USA → US_EQ, CAN → CA_EQ, JPN → JP_EQ, GBR → GB_EQ, DEU → DE_EQ, FRA → FR_EQ, ITA → IT_EQ; NGDPD, `USD_billions`.
K1 ist eine Gleichgewichtung der sieben Länderproxies, kein Marktkapitalisierungsportfolio. `0.14285714285714285` stellt das vom Autor vorgegebene 1/7 in der Engine-Floatdarstellung dar; keine nachträgliche Zielnormalisierung.
Diese Auswahl einschliesslich Sensitivitäten stammt ausdrücklich vom Autor und wurde nicht anhand von Ergebnissen optimiert.

## F. Tatsächliche Config-Pfade

Die Eingaben werden relativ zur jeweils beauftragten Datei unter `configs/study_v1/` aufgelöst:
`../../data/study_v1/archive/study-freeze-v1/processed/<Dateiname>`.
Alle fünf Ausführungsconfigs lesen tatsächlich die eingefrorenen Kopien; kein Eingabepfad zeigt auf die normale Arbeitskopie unter `data/study_v1/processed/`.
H1/K1 referenzieren main_market, assets, rf_main und macro_g7; Z1 us_market, assets und rf_us; S1/S2 main_market, assets und rf_main. RF-Serie überall `DGS3MO_LAGGED_ACT365_APPROX`.
Alle passenden aufgelösten Dateien existieren, besitzen die genehmigten Hashes und wurden durch die öffentlichen Loader/Validatoren gelesen.

Die bytegleichen Archivkopien unter `configuration-records/` dokumentieren diese ursprünglichen Configdateien mitsamt deren Repository-Auflösungsbasis. Sie werden nicht als weitere, an einen anderen relativen Ort verschobene Ausführungskonfigurationen behandelt. Bei Wiederherstellung gehören sie zurück nach `project/configs/study_v1/`; diese Basis ist im Manifest und Archiv-README festgehalten.

## G–H. Archivvollständigkeit und neuer Manifesthash

Neu erstellt, kein vorheriger Archivstand überschrieben:
`data/study_v1/archive/study-freeze-v1/`, **123 Dateien**, **165’404’958 Bytes** einschliesslich Manifest.
Alle Archivdateien sind reguläre Dateien mit Linkzahl eins; sämtliche 118 Kopien sind bytegleich zu ihren Quellen und besitzen eine andere Dateiidentität. Keine symbolischen Links, Junctions oder Hardlinks.

| Archivbereich | Enthalten |
|---|---|
| raw/ | Alle 54 Originaldateien, getrennt nach eindeutigem Yahoo/FRED-Snapshot und 16 IMF-Ausgaben |
| processed/ | Alle zwölf genehmigten CSV-/JSON-Artefakte einschliesslich Herkunftstabellen und Processed-Manifest |
| scripts/study_v1/ | Tatsächlicher Downloader, Adapter, WEO-Register und neue Prüfhilfe |
| configuration-records/ | Fünf unveränderte Config-Aufzeichnungskopien; alle fünf SHA-256 im Manifest |
| engine/ | Vorhandenes geprüftes Engine-1.0.0-Wheel, 22 unveränderte Pythonquellen, pyproject.toml und requirements.lock |
| documentation/ und AGENTS.md | Autorenfreigabe, Aufbereitung, fachliche Entscheidungen, Release, KI-Regeln und beide vollständigen Aufträge |
| tests/, evidence/, procedure/, environment/ | Tests und tatsächliche Protokolle, unabhängiger vorheriger Datenprüfer samt Ergebnis, gesperrte Ausführungseinstiege, Erstellungscode, statische Config-Abnahme, Git-Ausgangszustand sowie Python-/Paketversionen |

Das maschinenlesbare `freeze_manifest.json` enthält **122 Einzeldateieinträge** mit Dateipfad, Kategorie, Grösse und SHA-256, die fünf Config-Hashes, Engine-/Freigabebindung, Datum/Zeit und Prüfnachweisreferenzen. Es enthält keinen Selbsthash.
Zeitpunkt: **2026-10-10T01:31:52.401339+00:00**; `git_sealed=false`, `strategy_runs_executed=false`.

SHA-256 des fertigen Freeze-Manifests:

```text
91d8fe30d1162bf467235a87d5688a13462277e31a6dcff1878ddc3bad0bd51c
```

Separater Nachweis für die spätere Git-Versionierung: [study-v1-freeze-seal.md](study-v1-freeze-seal.md), einschliesslich fünf Config-Hashes und Prüfbefehl. Die abschliessenden Berichte/Git-Steuerdateien bleiben ausserhalb des unveränderten Archivs, um keinen zyklischen Bericht-/Manifesthash zu erzeugen.
Das vorhandene Wheel wurde kopiert und gegen alle aktuellen Pythonquellen geprüft, nicht neu gebaut; sein SHA-256 bleibt `045f0dda4fa4bdb4774390fd166140290ae061d1478e99c1a356c8fc91ed46d2`.

## I. Tatsächlich ausgeführtes Prüfprogramm

| Prüfung | Ergebnis |
|---|---|
| Erneute unveränderte Adaptertests | **30 bestanden, 17.988 s, keine Skips** |
| Neue physische Kopier-/Inventar-/Pfad-/Freeze-Schutztests | **16 bestanden, 0.607 s, keine Skips** |
| Öffentlicher Config-Loader und `prepare_context` für H1/K1/Z1/S1/S2 | Alle bestanden; exakte Kalender, USD, ME/12, Assets, RF-Intervalle und gültiger SMA-Anker |
| SMA-Vorlauf H1/S1/S2 und Z1 | Elf eigene Beobachtungen vor der Dezemberbewertung plus Startwert = zwölf am Anker; VTI-Historie ab Januar 2002, keine IEF-Verlängerung |
| Historische GDP-Abnahme H1/K1 | Je 16 As-of-Kontrollen, identische vollständige G7-Zuordnung und positive Ziele mit Summe eins; 2022 gemeinsam 2020, GBR 2’758.87 aus Verfügbarkeit 2022-10-12 |
| Archiv- und Quellenintegrität | Alle Hashes/Grössen, Inventare und echten Kopien erfolgreich geprüft; freigegebener Datenstand weiterhin unverändert |
| Reiner Prüf-CLI mit separat vorgegebenem Manifesthash | Exit 0, `verification=passed`, keine Strategieausführung |
| Erneuter Erstellungsaufruf auf vorhandenem Archiv | Vollständiges Inventar geprüft, danach erwarteter Exit 1; kein Überschreiben, Manifesthash unverändert |
| Prüf-CLI mit falschem externen Manifesthash | Erwarteter Exit 1 vor Verwendung des Archivs; konkrete Hashabweichung gemeldet |
| `pip check`, Python-Syntaxprüfung, Git-Diff-/Ignore-/Attributkontrollen | Bestanden; keine neuen Paketinstallationen oder Indexeinträge für Daten/Archiv |

Befehle der zwei Testgruppen: `.venv-study/Scripts/python.exe -m unittest discover -s tests/study_v1 -p test_prepare_data.py -v` und entsprechend `-p test_freeze.py`.
Die echten Erstellungs-/Prüfprozesse liefen mit zuvor bestätigten Sperren für Socket/DNS/URL, `run_simulation`, alle vier Strategie-`run`-Methoden und `export_run`.
Nur Config-/Datenkontexte, SMA-Gültigkeit und GDP-Kontrollziele wurden berechnet. Kein Strategieportfolio, Renditepfad, Kennzahlvergleich, Run-Verzeichnis oder Strategieexport erstellt.
Software: vorhandene `.venv-study`, Windows 11 Build 26300, Python 3.14.0, pandas 2.3.3, NumPy 2.3.5; vollständige Paketversionen im Archiv.

## J. Fehler, Entscheidungen und Grenzen

Keine offenen fachlichen Entscheidungen oder methodischen Abweichungen festgestellt.
Ein neuer Test versuchte zunächst einen synthetischen Hardlink anzulegen; dies verweigerte die Sandbox (ein Fehler, 15 Tests bestanden). Die Hardlink-Erkennung wird nun durch injizierte tatsächliche Stat-Metadaten `st_nlink=2` geprüft und lehnt die Kopie weiterhin vor Erstellung ab. Alle 16 Tests danach bestanden; die tatsächlichen 123 Archivdateien haben unabhängig davon Linkzahl eins. Bestehende Tests blieben unverändert.
Die neue LF-Bindung ist eine technische Reproduzierbarkeitsentscheidung und verändert keine Studie oder Datei-Inhalte.
Die vom Autor akzeptierten Grenzen von Yahoo-Adjustierung, täglichem Börsenkalender, USD/FX, DGS3MO-Approximation und historischer IMF-Bytezeit bleiben bestehen. Keine Behauptung vollständig unabhängiger Total-Return-Rekonstruktion, ursprünglicher kryptografischer IMF-Dateidatierung, allgemeiner Fehlerfreiheit oder plattformübergreifender Reproduzierbarkeit.

## K–L. Git-Status, Sicherung und Ausführungsbereitschaft

Die fünf Configs sind **technisch für die spätere ausdrücklich beauftragte Ausführung bereit**. Die jetzige Freigabe akzeptiert Daten/Methoden; sie startet keine Hauptläufe automatisch.
Vorher erforderlich: den vorgesehenen Git-Stand kontrollieren und ausdrücklich versiegeln; das vollständige lokale Archiv samt Manifest extern sichern und die spätere Commit-Kennung dokumentieren. Zusätzlich Python-/Paketdistributionen oder die passende Ausführungsumgebung extern erhalten; nicht sämtliche Abhängigkeits-Wheels sind im Archiv vorhanden.
Danach vor dem Hauptlauf die reine Prüfhilfe mit dem separat dokumentierten Manifest-Sollhash erneut ausführen. Keine Ist-Hashes als neue Sollwerte übernehmen und keine Configs anhand späterer Resultate verändern.

Tatsächlicher abschliessender Git-Status, einschliesslich der geschützten Änderungen aus dem vorherigen Auftrag:

```text
 M .gitignore
 M documentation/ai-usage/ai-usage-log.md
?? .gitattributes
?? configs/study_v1/
?? documentation/ai-usage/prompts/2026-10-10-study-v1-data-adapter.md
?? documentation/ai-usage/prompts/2026-10-10-study-v1-freeze-preparation.md
?? documentation/study-v1-author-approval.md
?? documentation/study-v1-data-preparation.md
?? documentation/study-v1-freeze-preparation.md
?? documentation/study-v1-freeze-seal.md
?? scripts/study_v1/prepare_data.py
?? scripts/study_v1/verify_freeze.py
?? scripts/study_v1/weo_release_register.csv
?? tests/study_v1/
```

Die 17 unversionierten Einzeldateien in diesen Pfaden sowie `.gitignore` und das ergänzte KI-Log sind für spätere Versionierung vorgesehen. Die ursprünglichen Skripte bleiben bereits versioniert und bytegleich. Wissenschaftliche Dateien und bestehende Engine-Nachweise wurden nicht bearbeitet.
Raw, Processed, Archiv, `.venv-study` und `outputs/runs/` sind ignoriert; kein Daten-/Archiveintrag im Git-Index, keine Dateien staged. HEAD und sämtliche Tags unverändert. Kein Commit, Push, Merge oder Tag erstellt.
