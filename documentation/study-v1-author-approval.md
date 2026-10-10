# Study-v1: ausdrückliche Autorenfreigabe

**Freigabedatum:** 10.10.2026. **Entscheider:** Autor der Maturarbeit.
Die ausdrückliche Freigabe steht im [vollständigen Folgeauftrag](ai-usage/prompts/2026-10-10-study-v1-freeze-preparation.md), Abschnitt Ausgangslage.
Codex dokumentiert diese Autorenentscheidung; die Freigabe wurde nicht durch Codex erteilt.

Verbindlicher SHA-256 des akzeptierten `data/study_v1/processed/processed_manifest.json`:

```text
948865ea3302ced267c9828b9a459ba03cd1c62971c070a818fd4c356c629c28
```

Der Autor akzeptiert die Daten und die dokumentierten Methoden, Annahmen und Grenzen für die Untersuchung:

- Rohdaten genau aus `data/study_v1/raw/download_20261008T014620197765Z/` und den 16 WEO-Ausgaben unter `data/study_v1/raw/imf/`; 54 ursprüngliche Dateien.
- Hauptzeitraum: Renditeperioden Januar 2010–Dezember 2025, Startbewertung 2009-12-31. US-Zusatzzeitraum: Januar 2003–Dezember 2025, Startbewertung 2002-12-31. Bewertung ME, USD, zwölf Perioden pro Jahr; Signalhistorie 2009 beziehungsweise VTI 2002 einschliesslich Startbewertung, IEF erst ab Juli 2002.
- ETF-Proxies: VT → WORLD_EQ, IEF → US_TREASURY_7_10, VTI/USA → US_EQ, EWC/CAN → CA_EQ, EWJ/JPN → JP_EQ, EWU/GBR → GB_EQ, EWG/DEU → DE_EQ, EWQ/FRA → FR_EQ, EWI/ITA → IT_EQ. Unverändertes Adj Close der letzten beobachteten Monatsbeobachtung; Kalenderlabel und tatsächlicher Handelstag getrennt.
- Historische G7-WEO-Daten: NGDPD, `USD_billions`, je Ausgabe/Land nur Jahre bis einschliesslich `Estimates Start After`; historische Versionen mit den bestätigten Verfügbarkeitsdaten. WEO 2022 wählt gemeinsam 2020, GBR 2’758.87 Mrd. USD. Die konservative Verfügbarkeit 2012 ist 2012-10-10.
- `DGS3MO_LAGGED_ACT365_APPROX`: letzte gültige Prozentquote strikt vor dem tatsächlichen Start-Handelstag, höchstens sieben Kalendertage alt; `(Quote / 100) × Kalendertage / 365`. Eine akzeptierte Approximation, keine gemessene Treasury-Bill-Halterendite.
- Der Folgeauftrag legt Startkapital 100’000 USD und die fünf Configs H1/K1/Z1/S1/S2 samt SMA 3/12, 2/12 und 6/12 ausdrücklich fest; keine ergebnisabhängige Optimierung.

**Technische Datenprüfung:** bestanden in den dokumentierten Bereichen des [Aufbereitungsberichts](study-v1-data-preparation.md): 30 Adaptertests sowie unabhängige Kontrollen von 54 Raw-Dateien, 2’406 ETF-Monatswerten, 468 RF-Perioden, 4’087 historischen BIP-Versionen und 112 G7-Entscheidungszeilen, ohne festgestellte Abweichungen. Die erneute Hash-/Grössen- und Config-Prüfung gehört zum Folgeauftrag und wird gesondert dokumentiert.

**Akzeptierte Aussagegrenzen:** Yahoo-Adjustierungen wurden nicht vollständig unabhängig rekonstruiert; USD-Notierung ist keine wirtschaftliche FX-Absicherung. Tägliche Vollständigkeit gegenüber einem unabhängigen Börsenkalender ist nicht belegt. Historische IMF-Ausgabendatierung beweist nicht kryptografisch die damalige Existenz exakt der heute archivierten Dateibytes. Geprüfte Plattform ist Windows/CPython 3.14.0. Die Veröffentlichungstermine wurden als geprüfte Autorenvorgabe übernommen.

**Noch nicht erfolgt:** zeitliche Versiegelung des Studien-Freeze in Git, externe Sicherung und echte Hauptläufe. Die historischen Processed-Dateien behalten ihren damaligen Status `NORMALIZED_PENDING_AUTHOR_APPROVAL` bytegleich; diese zusätzliche Freigabedokumentation hält die spätere Autorenentscheidung fest. Keine Ergebnisse oder Durchführung von Hauptläufen werden behauptet; deren Ausführung benötigt einen gesonderten Auftrag.
