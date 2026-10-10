# Study-v1: Datenadapter und Echtdatenprüfung

**Stand:** 2026-10-10. **Status:** `NORMALIZED_PENDING_AUTHOR_APPROVAL`.
Technische Eingabeprüfung bestanden; keine wissenschaftliche Datenfreigabe und kein Study-Freeze.
Auftrag: [vollständiger Autorenauftrag](ai-usage/prompts/2026-10-10-study-v1-data-adapter.md).

Ausgangszustand sauber auf `study-v1`, HEAD `9b2bf65e2989b97d8ceea23393e0a271998bb09a`.
Der annotierte Tag `engine-v1.0` löst zu `4a98f3a1039c6ebf4f1bfa1202a1af2e8064b023` auf.
AGENTS.md, Releasevertrag, OD-01 bis OD-13, tatsächliche Datenvalidatoren, Konfigurationsstruktur und vorhandener Downloader wurden gelesen.

## A. Erstellte und geänderte Dateien

Neu und für eine spätere Versionierung vorgesehen:

- [Adapter 0.1.0](../scripts/study_v1/prepare_data.py).
- [WEO-Ausgabenregister](../scripts/study_v1/weo_release_register.csv), 16 Autorendatierungen mit getrennten Verfügbarkeitsdaten und Quellenzuordnung.
- [30 Adaptertests](../tests/study_v1/test_prepare_data.py) im abgegrenzten Study-v1-Testbereich.
- Dieser Abschlussbericht und die vollständige Auftragskopie.

Nur `documentation/ai-usage/ai-usage-log.md` wurde als Bestandsdatei durch einen Eintrag ergänzt; bisherige Bytes bleiben vollständig erhalten.
Engine, bisherige Tests, Configs, Downloader, Auditnachweise, wissenschaftliche Dateien und Rohdateien bleiben bytegleich.
HEAD und sämtliche Tags unverändert. Kein Commit, Push, Merge, Tag oder Staging vorgenommen.

Unter `data/study_v1/processed/` entstanden ausschliesslich lokal diese zwölf Dateien:

| Datei | Datenzeilen | Zweck |
|---|---:|---|
| assets.csv | 9 | Asset-/Länder-/USD-Metadaten |
| main_market.csv | 1’836 | 204 Monatswerte je neun Assets, einschliesslich Vorlauf |
| us_market.csv | 570 | VTI: 288; IEF: 282 Monatswerte, einschliesslich eigener Historie |
| rf_main.csv | 192 | Hauptperioden, Dezimalrenditen |
| rf_us.csv | 276 | US-Perioden, Dezimalrenditen |
| macro_g7.csv | 4’087 | Historische G7-NGDPD-Versionen |
| observation_provenance.csv | 2’406 | Jede verwendete ETF-Quellbeobachtung |
| risk_free_provenance.csv | 468 | Jede verwendete Quote und deren Umrechnung |
| macro_provenance.csv | 4’087 | Originalzelle, Ausgabe, Cutoff, Einheit, Verfügbarkeit, Hash |
| g7_decision_check.csv | 112 | 16 Entscheidungen × sieben Länder |
| normalization_report.json | – | Datenkontrollen, Grenzen und Engine-Abnahme |
| processed_manifest.json | – | Rohdaten-, Code-, Umgebungs- und Ausgabehashes |

Die bestehenden lokalen Git-Ausschlüsse halten Rohdaten, Ausgaben und Prüfarbeitsablage aus der Versionierung heraus; Ausschlüsse wurden nicht verändert.
Der zweite identische Ausgabestand und temporäre Prüfprogramme/-protokolle liegen unter `.venv/study_v1_adapter_check/`.

## B. Tatsächlich verwendeter Rohdatenstand

Genau `data/study_v1/raw/download_20261008T014620197765Z/`: neun Yahoo-Tagesdateien, neun passende Metadaten, FRED DGS3MO, Acquisition-Manifest sowie archivierter Downloader und dessen Umgebung.
Alle Manifestgrössen und SHA-256 wurden kontrolliert. Dazu genau die 16 WEO-Ordner unter `data/study_v1/raw/imf/`, jeweils Original-TSV mit .xls-Endung und Downloadnotiz: insgesamt **54 Rohdateien**.
Kein anderer Snapshot, kein Download, keine Rohdatenänderung. Die Notizen stimmen mit Originalnamen, Ausgaben und Downloadseiten des Registers überein.

| ETF | Asset | Tageszeilen | Beobachteter Tageszeitraum |
|---|---|---:|---|
| VT | WORLD_EQ | 4’276 | 2009-01-02 bis 2025-12-31 |
| IEF | US_TREASURY_7_10 | 5’895 | 2002-07-30 bis 2025-12-31 |
| VTI | US_EQ | 6’039 | 2002-01-02 bis 2025-12-31 |
| EWC | CA_EQ | 4’276 | 2009-01-02 bis 2025-12-31 |
| EWJ | JP_EQ | 4’276 | 2009-01-02 bis 2025-12-31 |
| EWU | GB_EQ | 4’276 | 2009-01-02 bis 2025-12-31 |
| EWG | DE_EQ | 4’276 | 2009-01-02 bis 2025-12-31 |
| EWQ | FR_EQ | 4’276 | 2009-01-02 bis 2025-12-31 |
| EWI | IT_EQ | 4’276 | 2009-01-02 bis 2025-12-31 |

Die Metadaten bestätigen USD, ETF, US-Börse und `America/New_York` für alle neun Instrumente.

## C–D. Beobachtungen, Vollständigkeit und Vorlauf

`main_market.csv`: Januar 2009 bis Dezember 2025 für jedes der neun Assets vollständig, 204 Monate × neun.
Der Performancekalender enthält **193 gemeinsame Bewertungen vom 2009-12-31 bis 2025-12-31** und genau **192 Folgeperioden** für Januar 2010 bis Dezember 2025.

`us_market.csv`: VTI Januar 2002 bis Dezember 2025 vollständig; IEF Juli 2002 bis Dezember 2025 vollständig.
Der Performancekalender enthält **277 gemeinsame Bewertungen vom 2002-12-31 bis 2025-12-31** und **276 Folgeperioden** für Januar 2003 bis Dezember 2025.
VTI Januar bis Juni 2002 bleibt in der Datei als eigene Signalhistorie erhalten. Die öffentliche gemeinsame Kalenderausrichtung weist diese sechs Termine als nicht gemeinsam mit IEF aus; es sind keine entfernten Performanceperioden und keine fehlenden IEF-Werte ersetzt worden.

Beide Kalender sind `ME`, USD, zwölf Perioden pro Jahr. Kein Zeitraum wurde verkürzt.
Alle letzten beobachteten Quellhandelstage stimmen für die jeweils benötigten Assets und Monate überein, auch für alle neun Hauptreihen im Jahr 2009.
Das Engine-Datum ist ausschliesslich das rechte Kalender-Monatsendlabel; Provenienz enthält tatsächliches Handelsdatum, Zeitstempel, CSV-Zeile und Original-Adj-Close.
`performance_value` entspricht unverändert dem numerischen `Adj Close`; keine zusätzliche Dividenden-/Splitanpassung, Renditeberechnung, Interpolation oder Auffüllung.

Die vorgeschriebenen zwölf Signalbeobachtungen sind Januar–Dezember 2009 beziehungsweise Januar–Dezember 2002, **einschliesslich der anfänglichen Dezemberbewertung**.
Das sind elf Beobachtungen strikt vor der Startbewertung und zwölf vor der ersten auszuwertenden Renditeperiode.
Diese Zählung entspricht den vorgegebenen Zeiträumen und dem Engine-Vertrag `long_window - 1` vor dem Anker; SMA-Fenster und Signale wurden weder gewählt noch berechnet.

## E. Tatsächlich umgesetzte Zinsumrechnung

`DGS3MO_LAGGED_ACT365_APPROX`: letzte gültige tägliche Prozentquote strikt vor dem tatsächlichen Quellhandelstag der Startbewertung, höchstens sieben Kalendertage alt.
Die einfache Dezimal-Periodenapproximation lautet `(annual_rate_percent / 100) * (Tage zwischen den beiden Kalender-Monatsendlabels / 365)`.
Schaltjahrperioden behalten ihre tatsächliche Tageszahl und den bestätigten Nenner 365. Kein Endperiodenzins und keine Nullersetzung fehlender Quotes.

FRED enthält 6’261 Tageszeilen, davon 6’003 gültige Quotes und 258 fehlende Quotes, 2002-01-02 bis 2025-12-31.
Alle 468 Perioden besitzen passende Quotes und exakte Marktperiodengrenzen. Quotenalter: 385 × ein Tag, 14 × zwei, 62 × drei, sieben × vier; Maximum **vier Tage**.
Dies ist die vom Autor gewählte Näherung, keine gemessene Rendite eines gehaltenen Treasury-Bill-Portfolios.

## F. Übernommene historische BIP-Daten

Alle 16 Ausgaben von Oktober 2009 bis Oktober 2024, mit September 2011: pro Ausgabe eindeutig sieben G7-NGDPD-Reihen in `U.S. dollars / Billions`, normalisiert zu `USD_billions`.
Die historischen Zellen beginnen 1980; je Land/Ausgabe wurden nur Jahre bis einschliesslich `Estimates Start After` behalten, insgesamt **4’087 Versionen**. Prognosezellen sind ausgeschlossen; spätere historische Revisionen bleiben separate Versionen mit ihrer eigenen Verfügbarkeit.
2020 und 2024 wurden als UTF-16 LE ohne BOM gelesen, die übrigen als Latin-1; NUL-Bytes nicht entfernt. Erkannte IMF-Fusszeilen werden separat gezählt, ungültige Daten oder unbekannte Fusszeilen abgelehnt.

Die 16 Datierungen/Verfügbarkeiten sind **Autorenentscheidungen aus Auftragsabschnitt 6**, im Register mit `AUTHOR_CONFIRMED_PROMPT_SECTION_6` bezeichnet.
Die vorherige Prüfung offizieller Publikationsnachweise wird als Autorenvorgabe übernommen; keine neue unabhängige Internetprüfung behauptet.
Insbesondere 2012: Publikationsseite 8. Oktober, öffentliche Vorstellung 9. Oktober, konservative Verfügbarkeit 10. Oktober.
Downloadnotizen beweisen die Ausgabezuordnung. Die historische Datierung beweist nicht kryptografisch, dass genau diese heute archivierten Dateibytes bereits damals vorlagen.

## G. Referenzjahre der 16 Entscheidungen

| Entscheidungsdatum | BIP-Jahr | WEO-Version |
|---|---:|---|
| 2009-12-31, initial | 2008 | 2009-10 |
| 2010-12-31 | 2009 | 2010-10 |
| 2011-12-31 | 2010 | 2011-09 |
| 2012-12-31 | 2011 | 2012-10 |
| 2013-12-31 | 2012 | 2013-10 |
| 2014-12-31 | 2013 | 2014-10 |
| 2015-12-31 | 2014 | 2015-10 |
| 2016-12-31 | 2015 | 2016-10 |
| 2017-12-31 | 2016 | 2017-10 |
| 2018-12-31 | 2017 | 2018-10 |
| 2019-12-31 | 2018 | 2019-10 |
| 2020-12-31 | 2019 | 2020-10 |
| 2021-12-31 | 2020 | 2021-10 |
| 2022-12-31 | **2020** | **2022-10** |
| 2023-12-31 | 2022 | 2023-10 |
| 2024-12-31 | 2023 | 2024-10 |

Je Entscheidung: jüngstes gemeinsames zulässiges Jahr, letzte damals verfügbare Version je Land, sieben positive Werte, Zielgewichtssumme innerhalb 1e-12 gleich eins; vollständige Einzelwerte und Herkunft in `g7_decision_check.csv`.
WEO 2022 hat GBR-Cutoff 2020, übrige sechs Länder 2021. Daher gemeinsame Auswahl 2020 aus **WEO 2022**, GBR **2’758.87 Mrd. USD**. Die Auswahl wird aus den Daten abgeleitet; keine programmierte Jahresausnahme.
Die 16 Entscheidungen sind die initiale Entscheidung 2009 plus 15 wirksame Jahresendentscheidungen 2010–2024. Am terminalen 2025-12-31 folgt gemäss eingefrorenem OD-06 kein weiterer Trade; eine WEO-Ausgabe 2025 wird hierfür nicht benötigt.

## H–I. Ausgeführte Tests und Ergebnisse

Final: `.venv-study/Scripts/python.exe -m unittest discover -s tests/study_v1 -v` → **30 Tests bestanden, 17.667 s, keine Skips**.
Abgedeckt sind alle 17 Auftragsgruppen: Monatsauswahl/Quellhandelstag, fehlende Monate und abweichende Handelstage, unverändertes Adj Close, strikt verzögerte Quotes, Prozent-/ACT/365-Umrechnung und exakte Perioden, beide WEO-Kodierungen, historische Cutoffs/Prognoseausschluss, Versionierung/Look-ahead, gemeinsames G7-Jahr, echter 2022-Fall, Kennungen, bytegleiche Wiederholung, Hashes und unveränderte Rohdaten.
Zusätzlich: Duplikate, ungültige Zahlen, NUL/CSV-Breite, Timestamp-Widersprüche, Einheiten/Fusszeilen, sieben-/acht-Tage-Grenze, fehlender G7-Nenner, unveränderte negative Quotes, explizit fehlende Rohpfade, Überschreibschutz und eingefrorener Engine-Vergleich.

Erster Lauf: 29 Tests, 40 technische Fehler durch gesperrten globalen Sandbox-Tempordner. Zweiter Lauf nach Verlagerung der neuen Testfixtures in den Workspace: 28 bestanden, ein Fehler durch CRLF/LF-Vergleich der eingefrorenen Engine.
Der Adapter vergleicht nun Engine-Pythonbytes nach ausschliesslicher Git-Zeilenendnormalisierung; tatsächliche Laufzeit- und Git-Blob-Hashes bleiben getrennt dokumentiert. Zusätzlicher Test belegt die Ablehnung inhaltlicher Abweichungen. Engine-Dateien und bestehende Tests wurden nicht verändert oder abgeschwächt.

Zwei erfolgreiche Echtdaten-CLI-Aufrufe mit aktiv geprüftem Socket-/DNS-/URL- und Simulationseinstiegs-Guard:

```powershell
.venv-study/Scripts/python.exe scripts/study_v1/prepare_data.py `
  --raw-dir data/study_v1/raw/download_20261008T014620197765Z `
  --imf-dir data/study_v1/raw/imf `
  --output-dir data/study_v1/processed
```

Der Wiederholungslauf verwendete `.venv/study_v1_adapter_check/repeat-output` als neuen Ausgabeordner; **alle zwölf Dateien bytegleich**.
Bestehende Ausgabeordner werden ausdrücklich abgelehnt; neue Kandidaten werden erst nach vollständiger Prüfung per Rename veröffentlicht. Ein fehlgeschlagener Kandidat wird zur Diagnose erhalten.
Das temporäre unabhängige Prüfprogramm hat alle 2’406 ETF-Originalbeobachtungen, 468 RF-Umrechnungen mit Decimal-Kontrolle, 4’087 Original-BIP-Zellen und 112 Entscheidungszeilen nachgerechnet, Kalender/CSV-Schemas geprüft und sämtliche SHA-/Grössenangaben sowie unveränderte Raw-/Projekt-/Git-Stände bestätigt.

Öffentliche Engine-1.0.0-Validatoren/Aligner für Assets, Markt, RF und Makro, `check_period_logic` sowie `select_gdp_targets` bestätigen die fertigen Eingaben; kein Simulationsaufruf und keine SMA-/Strategieperformance.
Die bestehende Engine-Suite wurde in diesem reinen Adapterauftrag nicht erneut ausgeführt; ihre Dateien und die eingefrorene Implementierung sind unverändert.
`pip check` erfolgreich. Verwendet: vorhandene `.venv-study`, CPython 3.14.0, pandas 2.3.3, NumPy 2.3.5, dateutil 2.9.0.post0, tzdata 2026.5, Windows 11 Build 26300.
Für die öffentlichen Validatoren wurde ausschliesslich das bereits lokal vorhandene Engine-1.0.0-Wheel offline mit `--no-index --no-deps` installiert; keine externe Abhängigkeit heruntergeladen.

Manifest-SHA-256: `948865ea3302ced267c9828b9a459ba03cd1c62971c070a818fd4c356c629c28`.
Adapter-/Register-, Rohdatei- und alle elf übrigen Ausgabehashes sowie genaue Codeversion/Umgebung stehen im Manifest; sein eigener Hash wird wegen Zirkularität separat hier genannt.

## J–K. Grenzen, Status und nächster Schritt

**Keine offenen technischen Datenblocker oder Abweichungen von den bestätigten Regeln festgestellt.**
Monatsvollständigkeit ist geprüft; tägliche Vollständigkeit gegenüber einem unabhängigen Börsenkalender wurde nicht nachgewiesen. Die Auswahl bezeichnet den letzten tatsächlich vorhandenen Handelstag.
USD-Notierung bedeutet keine vollständige wirtschaftliche FX-Absicherung. Adj Close ist die heute archivierte adjustierte Anbieterreihe, kein unabhängig rekonstruiertes Total-Return-Portfolio. Historische WEO-Veröffentlichungsnachweise ersetzen keinen kryptografischen Bytezeitnachweis. Weitere Plattformen und wissenschaftliche Eignung wurden nicht bestätigt.

Der Stand ist technisch bereit für die **manuelle Autorenkontrolle** von Monats-/Quellhandelstagen und Vorlauf, RF-Provenienz und Näherung, Ausgabenregister/Publikationsbelegen sowie G7-Kontrolltabelle, insbesondere 2012 und 2022.
Erst nach ausdrücklicher Freigabe dieses Datenstands und der endgültigen Untersuchungsparameter können in einem separaten Auftrag finale Konfigurationen vorbereitet und geprüft werden.
Keine fünf Hauptläufe, Strategieergebnisse, automatische Datenfreigabe, wissenschaftliche Freigabe, finalen Configs, Commit oder Push in diesem Auftrag.
Codex setzte ausschliesslich die vorgegebenen Mappings, Zeiträume, Zins- und WEO-Regeln technisch um; keine neue fachliche Entscheidung getroffen.
