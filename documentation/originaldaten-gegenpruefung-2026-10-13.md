# Unabhängige Originaldaten-, Freeze- und Sharpe-Gegenprüfung (R-017)

Datum: **13. Oktober 2026**. Prüfer und Berichtverfasser: Codex. **R-017 teilweise geschlossen:** Die fehlende Zugänglichkeit und die unabhängigen Markt-, RF-, SMA-, BIP- und Sharpe-Rechnungen sind erledigt. Das versiegelte Archiv und die Ergebnisdateien sind intakt. Die bytegenaue Übereinstimmung des heutigen Engine-Checkouts mit dem historischen Laufstand scheitert bei 23 Dateien ausschliesslich an Zeilenenden. Die historische Herkunftsbeweiskraft bleibt begrenzt. **Keine pauschale Gesamtfreigabe und keine persönliche Autorenfreigabe. STOPP zur Autorenkontrolle.**

Die historischen Berichte werden als Soll-/Methodenreferenzen verwendet; ihre früheren PASS-Aussagen sind kein Beweis für die übertragenen Dateien. Referenzen: [Phase-2-Gegenlesen, R-017 und offene Prüfungen](gesamtgegenlesen-phase2-2026-10-12.md), [Fachkorrekturen](fachkorrekturen-phase2-2026-10-12.md), [vollständiger Originalauftrag](ai-usage/prompts/2026-10-13-originaldaten-gegenpruefung-r017.txt).

## 1. Umfang, Stände und Schutz

Der Auftrag wurde ohne Backtests, Strategieausführungen, Downloads, Datenaufbereitung, Notebook-Ausführung, Paketinstallation oder Update bearbeitet. Keine Engine-Funktion wurde importiert oder ausgeführt. Keine Git-Schreiboperation, kein Staging, Commit, Push, Merge, Reset oder Clean. Lediglich lesende Git-Abfragen mit `GIT_OPTIONAL_LOCKS=0`; die Eigentümerprüfung wurde für Engine und Backup ausschliesslich mit `git -c safe.directory=<Pfad>` pro Befehl überbrückt. Keine Änderung der globalen/lokalen Git-Konfiguration.

| Repository | Branch / HEAD | Ausgangsstatus | Erfasste Dateien / Bytes |
|:---|:---|:---|:---|
| C:\Users\modic\Documents\GitHub\Maturarbeit_Riccardo_Ambuehl_2027 | dev / `917abcf514be32696671c8ab780c7b49fd8182c8` | sauber | 18440 / 330125330 |
| C:\Users\modic\Documents\GitHub\Maturarbeit_Engine | study-v1 / `1954bfbcb257b51e7f9174aa824cb35e437de752` | sauber | 313 / 335190606 |
| C:\Users\modic\Documents\GitHub\Maturarbeit_Engine_Backup | study-v1 / `1954bfbcb257b51e7f9174aa824cb35e437de752` | 61 bereits geänderte versionierte Dateien; ein unversionierter outputs/-Eintrag | 8561 / 505216913 |

Die erwarteten Branches und HEADs stimmen. Engine-Tag `engine-v1.0` löst zu `4a98f3a1039c6ebf4f1bfa1202a1af2e8064b023` auf. Engine-Version laut Archiv, Wheel und allen fünf Run-Manifesten: **1.0.0**. Im Hauptrepository und seinen Vorfahren keine AGENTS.md; die Engine-AGENTS.md und KI-Regeln wurden berücksichtigt. Die direkte Autorenanweisung begrenzt die zulässigen Änderungen auf Bericht, Promptkopie und Logeintrag und verschiebt den Buch-Sync ausdrücklich.

Alle vier verlangten Notebooks wurden als JSON/Quelltext einschliesslich gespeicherter Textausgaben gelesen, nicht ausgeführt. Die 30 Ergebnisdateien, sämtliche fünf Configs/Run-Manifeste, Freeze-/Aufbereitungs-/Autorenfreigabenachweise, Register, Prüfhilfe, Adapter und relevante Quellen für Loader, Validierung, Periodenausrichtung, Signale, Makroauswahl, Kennzahlen und Export wurden gelesen bzw. geprüft. Frühere Engine-Tests und Studienläufe wurden nicht wiederholt.

| Notebook | Zellen | Codezellen, statisch gelesen |
|:---|:---|:---|
| Methodik | 30 | 0 |
| Analyse | 150 | 8 |
| Anhang_Datenaufbereitung | 69 | 2 |
| Anhang_Tests_Validierung | 15 | 0 |

Eigene Programme und sämtliche Vergleichsdateien liegen ausschliesslich in:

`C:\Users\modic\AppData\Local\Temp\R017-audit-2026-10-13-173ebe32`

Die Hauptrechnung `audit.py` verwendet nur Python-Standardbibliothek, `csv`, `Decimal` mit 60 Stellen und getrennte `statistics`-Rechnungen. Alle Python-Aufrufe erfolgten mit `-B`; Arbeitsverzeichnis war stets dieser externe Ordner. Zur gezielten Parserdiagnose wurde zusätzlich die **bereits vorhandene** Python-3.14.0-/pandas-2.3.3-Umgebung unter `C:\Users\modic\Documents\GitHub\Maturarbeit_Engine_Backup\.venv-study` nur gelesen. Für die Zeitzonenkontrolle wurde deren vorhandene tzdata verwendet. **Keine Backup-Daten, -Configs, -Enginequellen oder -Ergebnisse wurden als Ersatz für ein fehlgeschlagenes Hash-Gate verwendet.** Alle finanziellen Quellen stammen aus dem geprüften primären Archiv bzw. dem Hauptrepository. Keine historische Identität aller Drittanbieter-Paketbytes behauptet.

`verify_freeze.py` wurde vollständig auf Nebenwirkungen kontrolliert: Der CLI-Pfad prüft und erstellt statische Kontexte, während die im Modul ebenfalls vorhandene Kopierfunktion Dateien schreiben könnte, vom CLI aber nicht aufgerufen wird. Der CLI wurde nicht ausgeführt. Die ursprüngliche `.venv-study` fehlt im primären Engine-Ordner; eine Installation oder Anpassung wurde nicht vorgenommen. Der unabhängige Nachweis erfolgt direkt gegen die historischen Hashes und Rohdateien und hängt nicht von dieser Prüfhilfe ab.

## 2. Phase A: Freeze-Integrität und Quellenbindung

**PASS für das versiegelte Archiv und die ursprünglichen Daten/Ergebnisse. FAIL für die bytegleiche heutige Arbeitskopie des Codes, siehe Abschnitt 7.** Stop-Gate A ist bestanden: keine ungeklärte Abweichung im versiegelten Archiv.

Archiv: `C:\Users\modic\Documents\GitHub\Maturarbeit_Engine\data\study_v1\archive\study-freeze-v1`.

| Gegenstand | Historischer Soll-SHA-256 | Tatsächlicher SHA-256 |
|:---|:---|:---|
| freeze_manifest.json | `91d8fe30d1162bf467235a87d5688a13462277e31a6dcff1878ddc3bad0bd51c` | identisch |
| processed_manifest.json, Archiv und Arbeitskopie | `948865ea3302ced267c9828b9a459ba03cd1c62971c070a818fd4c356c629c28` | beide identisch |
| Engine-Wheel 1.0.0 | `045f0dda4fa4bdb4774390fd166140290ae061d1478e99c1a356c8fc91ed46d2` | identisch |

Der vollständige Manifesthash wurde **vor** Verwendung seiner Dateireferenzen geprüft. 122 eindeutige inventarisierte Archivdateien plus Manifest ergeben **123 Dateien und 165’404’958 Bytes**. Alle 122 Existenz-/Grössen-/SHA-256-Vergleiche bestanden. Null fehlende, zusätzliche, mehrfach aufgeführte oder hash-/grössenabweichende Archivdateien. Keine Symlinks, Junctions oder Hardlinks im Archiv; reguläre Dateien mit Linkzahl eins. Die historischen Sollwerte wurden nicht aus dem heutigen Ist-Zustand neu erzeugt.

Das Processed-Manifest bindet 54 Raw-Dateien und elf weitere Ausgaben; mit ihm selbst sind es zwölf Processed-Artefakte. Beide Herkunftsinventare wurden vollständig gegen Archiv **und** Arbeitsdaten geprüft: 54/54 Raw- und 12/12 Processed-Dateien stimmen. Das Acquisition-Manifest bindet zusätzlich seine 21 übrigen Snapshot-Dateien; mit sich selbst sind es 22, ergänzt durch 16 WEO-Dateien und 16 Downloadnotizen zu 54 Raw-Dateien. Keine Ersatzdatei eingesetzt.

| Archivkategorie | Dateien |
|:---|:---|
| approval_or_method_evidence | 8 |
| archive_layout | 1 |
| configuration_record | 5 |
| engine_versions | 2 |
| engine_source | 22 |
| engine_distribution | 1 |
| software_evidence | 1 |
| test_evidence | 4 |
| static_validation | 1 |
| execution_guard | 1 |
| independent_data_evidence | 2 |
| git_evidence | 1 |
| freeze_procedure | 1 |
| processed | 12 |
| raw | 54 |
| preparation_source | 4 |
| test_source | 2 |

Die fünf ausführbaren Configs stimmen bytegenau mit ihren versiegelten Aufzeichnungskopien überein. Ihre relativen Datenpfade lösen aus `Engine/configs/study_v1/` in das primäre Archiv auf. Die archivierten Config-Aufzeichnungen werden nicht fälschlich aus ihrem anderen Verzeichnis ausgeführt. Laufzeiten, Startkapital 100’000 USD, USD, ME/12, RF-Methode, SMA 3/12 bzw. 2/12 und 6/12 mit Lag 1 sowie aktivierte Strategien entsprechen den gebundenen Configs.

| Lauf | Config-SHA-256 | Bewertungen / Renditeperioden |
|:---|:---|:---|
| H1 | `cb74b62b49f4d246fa7eff5628315bb3e1923c924ec43544ab7de2942a72ae80` | 193 / 192 |
| K1 | `395982bfc5d4b40c3b8cccd5afeeceadeea91fda2d1a3e0fc1dac2f4ec04bead` | 193 / 192 |
| Z1 | `5d267c474e1d4ee7220f53f9341b52ef07fed51077352c9528e773ddebeb3527` | 277 / 276 |
| S1 | `bf55de18a2efa13f066d60710856023157189d36a447e6fe79f2f264aec68ea6` | 193 / 192 |
| S2 | `0cf0ad2c8b0e51c23a1be5a32487dc044274ed26b81bcf4b06ef4106410bdcca` | 193 / 192 |

| Tatsächlich verwendete eindeutige CSV | Historischer, bestätigter SHA-256 |
|:---|:---|
| assets.csv | `3f554cfe8945e09ef040838dac8585d259d1f43a2a98410eb302a1c6f1891a2b` |
| macro_g7.csv | `3d27f728d2b7465df415f332779e69418c35605c858f0cc4f4333a1f536e0e59` |
| main_market.csv | `6040c94e322c346ac9a8e0dfba7eb728bc58b77aa5b247a12ea87f43b8a6b21f` |
| rf_main.csv | `cd629e2df3ab9e6d4d9cd7667083a9998bb5120bd8a2dd4558fec2e6804c3baa` |
| rf_us.csv | `67ac6617bd91dccc9f4d5669b2bdc2af9ef6d3e57307855946dfa226b87c2e6c` |
| us_market.csv | `8ad63517b6ffca26fb6239290bf8f7730bdba63d1ffa113e57b8f75afcc3f8aa` |

Die fünf Run-Manifeste sind gegen die separat im bestehenden Analyse-Notebook festgehaltenen Hashes geprüft, die weiteren 25 Ergebnisdateien gegen deren Run-Hashes. **30/30 bestanden**, vollständiges Ergebnisinventar ohne Zusätze oder Verluste. 22 archivierte Engine-Pythonquellen stimmen byteweise mit dem vorhandenen Wheel überein. Sämtliche 24 Code-/Paketbindungen pro Run sind durch die Archivquellen bestätigt: **120/120 historische Vergleiche PASS**. Die fünf aggregierten Code-Fingerprints stimmen ebenfalls. Der Git-Quellstand wurde zusätzlich nach ausschliesslicher CRLF→LF-Normalisierung verglichen, ohne Dateien zu normalisieren oder zu speichern.

Freeze-Manifestzeit: `2026-10-10T01:31:52.401339+00:00`; Run-Manifeste nennen Studiencommit `1954bfbcb257b51e7f9174aa824cb35e437de752` und `dirty=false`. Die alten Manifestfelder `git_sealed=false`/`strategy_runs_executed=false` beschreiben den vorbereiteten Archivzeitpunkt und wurden unverändert erhalten; sie sind kein Widerspruch zu den späteren Run-Manifesten. Lokale Git-Zeitstempel oder heutige Hashes liefern keine unabhängige externe Zeitstempelversiegelung.

| Hashvergleichsgruppe | Vergleiche | PASS | FAIL |
|:---|:---|:---|:---|
| A acquisition | 21 | 21 | 0 |
| A approved manifest | 1 | 1 | 0 |
| A archive | 122 | 122 | 0 |
| A config binding | 5 | 5 | 0 |
| A engine archived source | 22 | 22 | 0 |
| A engine working source | 22 | 1 | 21 |
| A freeze seal | 1 | 1 | 0 |
| A preparation binding | 2 | 2 | 0 |
| A processed | 22 | 22 | 0 |
| A raw archive | 54 | 54 | 0 |
| A raw working | 54 | 54 | 0 |
| A results | 25 | 25 | 0 |
| A run code | 120 | 5 | 115 |
| A run code archived | 120 | 120 | 0 |
| A run input | 22 | 22 | 0 |
| A run manifest | 5 | 5 | 0 |
| A wheel | 1 | 1 | 0 |
| A working manifest | 1 | 1 | 0 |

Insgesamt **620 explizite historische Hashvergleiche**, davon **484 PASS und 136 FAIL**. Mehrfach verwendete Quellen werden pro Bindung gezählt. Die 136 FAIL-Vergleiche betreffen ausschliesslich **23 eindeutige heutige Code-/Paketdateien ausserhalb des Archivs**: 21 Pythondateien einmal gegen Freeze plus 23 Dateien in jedem der fünf Run-Manifeste. Sie bedeuten nicht 136 beschädigte Daten-/Archivdateien. Vollständige Zeilen in `hash-comparisons.csv`; eindeutige Abweichungen mit Soll-/Ist-Hash in Abschnitt 7.

## 3. Phase B: Marktdaten, Monatskalender und SMA

**PASS für Raw→Monat, Ausrichtung und gespeicherte Signale; PARTIAL für unabhängig bewiesene Anbieteradjustierung und tägliche Börsenkalendervollständigkeit.**

Alle neun Yahoo-Dateien besitzen passende Herkunftsmetadaten: USD, ETF, US-Börse, `America/New_York`; Abrufparameter `auto_adjust=False`, `back_adjust=False`, `repair=False`, `actions=True`, `keepna=True`, `rounding=False`, Tagesintervall. Tatsächliche Abdeckung stimmt mit dem Acquisition-Manifest. **41’866 Tageszeilen** auf eindeutige, aufsteigende Tage, gültige positive OHLC-/Adj-Close-Werte und endliche weitere Werte geprüft. Alle 41’866 Zeitstempel stimmen zusätzlich mit lokalem US-Handelsdatum und dem tatsächlichen New-York-Zeitzonenoffset überein.

| Symbol / Asset | Tageszeilen | Erster / letzter Tag | Monatswerte in eigener Historie | Gespeicherte Ausschüttungsereignisse |
|:---|:---|:---|:---|:---|
| VT / WORLD_EQ | 4276 | 2009-01-02 / 2025-12-31 | 204 | 57 |
| IEF / US_TREASURY_7_10 | 5895 | 2002-07-30 / 2025-12-31 | 282 | 282 |
| VTI / US_EQ | 6039 | 2002-01-02 / 2025-12-31 | 288 | 96 |
| EWC / CA_EQ | 4276 | 2009-01-02 / 2025-12-31 | 204 | 34 |
| EWJ / JP_EQ | 4276 | 2009-01-02 / 2025-12-31 | 204 | 34 |
| EWU / GB_EQ | 4276 | 2009-01-02 / 2025-12-31 | 204 | 34 |
| EWG / DE_EQ | 4276 | 2009-01-02 / 2025-12-31 | 204 | 25 |
| EWQ / FR_EQ | 4276 | 2009-01-02 / 2025-12-31 | 204 | 35 |
| EWI / IT_EQ | 4276 | 2009-01-02 / 2025-12-31 | 204 | 34 |

Für jeden Asset-Monat wurde unabhängig die nach Datum letzte **tatsächlich beobachtete** Tageszeile gewählt; kein Überspringen eines ungültigen Monatsendwertes und kein Auffüllen. 1’836 Hauptmarktzeilen plus 570 US-Zeilen = **2’406 vollständige Original→Monat-Vergleiche und 2’406 Provenienzzeilen**, numerisch exakt gleicher Floatwert. Das sind 1’998 unterschiedliche Asset-Monatsbeobachtungen; 408 werden in beiden Marktdateien verwendet. Quellzeile, Original-Adj-Close-Text, Quellhash, Timestamp, tatsächlicher Handelstag, Monatsendlabel und Vorlauf-/Performance-Rolle stimmen vollständig.

`signal_value` ist in den Eingabe-CSV nicht als zweite Reihe vorhanden; alle vier Trendconfigs wählen ausdrücklich `performance_value`. Die gleichnamige Spalte in den gespeicherten Signalen ist der daraus verwendete Wert. Hauptdatei: neun vollständige Kalender Januar 2009–Dezember 2025, jeweils 204 Werte. US-Datei: VTI 288 Werte Januar 2002–Dezember 2025; IEF 282 Werte Juli 2002–Dezember 2025. Die sechs VTI-Monate ohne IEF bleiben eigene Signalhistorie. Gemeinsame Performancekalender vollständig und alle tatsächlichen Quellhandelstage pro Haupt-/US-Monat identisch; auch der gesamte gemeinsame Haupt-Vorlauf ist geprüft.

H1/K1/S1/S2: Anfangsbewertung 2009-12-31, 193 Bewertungen und 192 Renditeperioden Januar 2010–Dezember 2025. Z1: Anfangsbewertung 2002-12-31, 277 Bewertungen und 276 Renditeperioden Januar 2003–Dezember 2025. Am ersten SMA-Anker liegen elf streng frühere Beobachtungen plus die Dezemberbewertung vor: zwölf Beobachtungen für SMA 12. Vorlauf erzeugt keine Portfoliorendite.

SMA-Mittelwerte wurden direkt aus jeweils 2/3/6 und zwölf Originalwerten mit Decimal nachgerechnet. **856 Zeilen, 856 kurze und 856 lange Mittelwerte**, sämtliche Long/Cash-Entscheidungen exakt bestätigt. Jede verdiente Position entspricht exakt dem Signal der Vorperiode; Anfangsposition leer. Keine neuen Strategieergebnisse erzeugt.

| Lauf / Fenster | Signalzeilen | Verdiente Positionen | Long / Cash | Wechsel zwischen Perioden |
|:---|:---|:---|:---|:---|
| H1 / 3/12 | 193 | 192 | 156 / 36 | 12 |
| S1 / 2/12 | 193 | 192 | 153 / 39 | 18 |
| S2 / 6/12 | 193 | 192 | 153 / 39 | 12 |
| Z1 / 3/12 | 277 | 276 | 220 / 56 | 19 |

Numerische Restdifferenzen wurden nicht als exakte Gleichheit ausgegeben: 257/856 `signal_value`-Vergleiche, 37 kurze und sechs lange SMA-Vergleiche unterscheiden sich vom unabhängig korrekt gerundeten Wert. Maximal zwei ULP, absolut 5,684342×10⁻¹⁴ bei den Preisen/kurzen SMAs bzw. 1,421085×10⁻¹⁴ beim langen SMA. Die Eingabe-Zahlkonvertierung und Mittelwertarithmetik erklären diese Grössen; die Prüfbeschränkung betrug vier ULP und alle diskreten Signale stimmen ohne Toleranz. Einzelwerte stehen in `numeric-comparisons.csv` und `signal-comparisons.csv`.

Zusätzlich bestätigt die Endpunktrechnung für die in R-017 noch offenen einzelnen Länderproxies: VTI 13,777328 % p. a.; Kanada 6,812292 %, Japan 6,596140 %, GBR 5,956813 %, Deutschland 6,480231 %, Frankreich 6,386247 %, Italien 5,279427 %. Damit passt der gedruckte Bereich 13,78 % versus 5,28–6,81 %. Nur bestehende Anfangs-/Endwerte, keine neuen Portfoliozeitreihen.

**Beweisgrenze:** Vorhandene Dividenden-/Splitspalten wurden geprüft und gezählt; VTI-Split 2008 sowie EWJ/EWU/EWI-Splits 2016 sind im Snapshot sichtbar. Das beweist weder jede historische Yahoo-Anpassung noch die originale Total-Return-Berechnung. Der Snapshot ist ein yfinance-Export, keine ursprüngliche HTTP-Antwort. Auch ein unabhängiger vollständiger Börsenkalender bzw. die Echtheit jeder Anbieterbeobachtung liegt nicht vor. Monatliche Vollständigkeit, vollständige Transformation und eingefrorene Byteidentität sind nachgewiesen; tägliche Vollständigkeit und Anbieteradjustierung bleiben PARTIAL.

## 4. Phase C: alle 468 RF-Perioden

**PASS für vollständige Quote-/Datums-/Einheiten-/Approximationprüfung.** FRED-Raw: 6’261 Zeilen, 6’003 gültige Prozentquoten und 258 fehlende Quotes (`.` bzw. leer). Aufsteigende eindeutige Tage; fehlende Werte wurden ausgeschlossen und weder auf null gesetzt noch aufgefüllt.

Für jede der 192 Haupt- und 276 US-Perioden: Anfangs- und End-Monatslabel aus dem unabhängig geprüften Marktkalender; tatsächlicher Handelstag aus dem unabhängig gewählten Marktmonat; neueste gültige FRED-Quote **streng vor** diesem Handelstag; Alter höchstens sieben Kalendertage. Endperiodenquote und Quote am Anfangshandelstag sind ausgeschlossen. Alle 468 Zinsquoten, Raw-Texte, Quellzeilen/Hashes, Handelstage, Alter, Kalenderlängen und Provenienzfelder stimmen.

Rechnung: `(annual_rate_percent / 100) * (calendar_days / 365)`. Decimal-Kontrolle mit 60 Stellen und getrennte Float-Operationen. Tatsächliche Monatsgrenzen bestimmen die Tage; Nenner auch in Schaltjahren 365. Exakte Intervallinventare in `rf_main.csv`, `rf_us.csv` und `risk_free_provenance.csv`; keine verlorene oder doppelte Studienperiode.

| Quotenalter in Kalendertagen | Anzahl |
|:---|:---|
| 1 | 385 |
| 2 | 14 |
| 3 | 62 |
| 4 | 7 |

| Periodenlänge in Tagen | Anzahl |
|:---|:---|
| 28 | 29 |
| 29 | 10 |
| 30 | 156 |
| 31 | 273 |

Maximum Quotenalter **vier Tage**. Die 468 Zeilen sind eindeutige `(Studie, Anfang, Ende)`-Perioden. Haupt- und US-Reihe haben **192 identische Kalenderintervalle und identische RF-Werte** gemeinsam; insgesamt sind es 276 verschiedene kalendarische Intervalle. Die vier Hauptstudienläufe verwenden dieselbe Haupt-RF-Datei. Weder ihre Mehrfachverwendung noch die Überschneidung mit Z1 wird als zusätzliche Originalbeobachtung gezählt.

**468/468 Float-Rechnungen stimmen bitgenau mit den korrekt geparsten gespeicherten Werten und ihrer Provenienz überein; absolute Differenz null.** Gegen exakte Dezimalarithmetik bleiben Darstellungsrundungen: maximal **8,684931506849315×10⁻¹⁹** als Abstand zum CSV-Dezimaltext, maximal zwei ULP beim Floatvergleich; keine fachliche RF-Abweichung. Die vier-ULP-Schranke ergibt sich aus den Divisionen/Multiplikationen, nicht aus einer pauschalen grosszügigen Renditetoleranz. Jede der 468 Zeilen und jeder Dezimalrest stehen in `rf-all-468.csv`; `rf-deviations.csv` enthält alle nicht-null Dezimalreste, auch zulässige Darstellungsreste.

Beispiel erste Hauptperiode: 2009-12-31→2010-01-31, tatsächlicher Anfangshandelstag 2009-12-31, Quote 2009-12-30, 0,05 %, Alter ein Tag, 31 Tage: `0.000042465753424657534...`; gespeichert `4.2465753424657536e-05`. Erste US-Periode: 2002-12-31→2003-01-31, 1,22 %, 31 Tage: `0.001036164383561643835...`, gespeichert `0.0010361643835616438`.

Diese Prüfung bestätigt die genehmigte ACT/365-Approximation. Sie verwandelt eine annualisierte Renditenotierung nicht in eine unabhängig gemessene Treasury-Bill-Halterendite. Die RF-Reihe verzinst weiterhin keine Trend-Cashposition.

## 5. Phase D: Sharpe und gespeicherte Vermögenspfade

**PASS für alle elf Gesamt- und acht ausgewiesenen H1-Halbperioden-Sharpes unter expliziter Berücksichtigung numerischer Darstellung.** Unabhängige Formel:

`mean(r_month − rf_month) / sample_sd(r_month − rf_month, ddof=1) * sqrt(12)`.

Die Anfangsbewertung besitzt in jeder der elf Reihen leere Rendite und wird ausgeschlossen. Die folgenden Datenlabels stimmen exakt und vollständig mit den zuvor kontrollierten RF-Intervallen. 192 bzw. 276 Renditen; die Halbperioden enthalten jeweils 96 Renditen, getrennt nach den tatsächlichen Labels. Keine Beobachtung geht verloren oder kommt doppelt vor. Arithmetisches Monatsmittel der Überschussrenditen und Stichproben-SD wurden separat mit 60-stelliger Decimal-Arithmetik und als zweite unabhängige Implementierung mit `statistics.mean/stdev` berechnet. Die Engine-Funktion `sharpe_ratio()` wurde nur gelesen. Mittelwerte und SDs je Vergleich stehen vollständig in `sharpe-comparisons.csv`.

### Numerischer Befund: pandas-Konvertierung des RF-Eingangs

Die Engine liest RF zunächst als Text und ruft in `src/data/validate.py::numeric` `pd.to_numeric(...).astype(float)` auf. Das vorhandene historische pandas 2.3.3 konvertiert manche Dezimaltexte anders als eine korrekt gerundete Python-/Decimal-Konvertierung: höchstens **9,974659986866641×10⁻¹⁷** pro RF-Rendite. Eine separat ausgeführte Parserdiagnose reproduziert alle 468 Konvertierungen ohne Engine-Import. Dadurch wird der mittlere Überschuss minimal verändert.

Die unabhängige Rechnung mit exakten RF-Dezimalwerten weicht deshalb von `summary.csv` maximal um **4,686154797451572×10⁻¹⁵** ab. Diese Abstände sind nicht blind als „innerhalb 10⁻¹²“ akzeptiert: Der tatsächliche Parsereffekt wurde separat gemessen; mit den damals tatsächlich konvertierten, zuvor unabhängig kontrollierten RF-Werten stimmen sechs der elf Sharpe-Werte exakt als Float, die übrigen fünf innerhalb maximal **2,220446049250313×10⁻¹⁶ bzw. zwei ULP**. Zulässiger Rest: vier ULP, nach Abzug des konkret nachgewiesenen Parsereffekts. Keine fachlich relevante Kennzahlen- oder Rundungsänderung, aber keine Behauptung vollständiger bitweiser Identität bei korrekt geparster RF-Dezimalarithmetik.

| Lauf / Strategie | Renditezeitraum; n | RF | Unabhängig, exakte RF | Gespeicherte Summary | Absolute Differenz | Unabhängig mit damaligem RF-Parser; Restdiff. |
|:---|:---|:---|:---|:---|:---|:---|
| H1 / buy_hold | 2010-01-31–2025-12-31; 192 | rf_main.csv | 0.6322212483306473 | 0.63222124833064974 | 2.413123e-15 | 0.63222124833064974; 0.000000e+00 |
| H1 / country_weighting | 2010-01-31–2025-12-31; 192 | rf_main.csv | 0.62874007970274604 | 0.62874007970274826 | 2.267732e-15 | 0.62874007970274848; 2.220446e-16 |
| H1 / rebalance | 2010-01-31–2025-12-31; 192 | rf_main.csv | 0.68487142351210573 | 0.68487142351210972 | 3.983203e-15 | 0.68487142351210972; 0.000000e+00 |
| H1 / trend | 2010-01-31–2025-12-31; 192 | rf_main.csv | 0.45230229360281554 | 0.45230229360281865 | 3.084528e-15 | 0.45230229360281854; 1.110223e-16 |
| K1 / country_weighting | 2010-01-31–2025-12-31; 192 | rf_main.csv | 0.62874007970274604 | 0.62874007970274826 | 2.267732e-15 | 0.62874007970274848; 2.220446e-16 |
| K1 / rebalance | 2010-01-31–2025-12-31; 192 | rf_main.csv | 0.44627845402121891 | 0.44627845402122107 | 2.179973e-15 | 0.44627845402122107; 0.000000e+00 |
| S1 / trend | 2010-01-31–2025-12-31; 192 | rf_main.csv | 0.46587373977171193 | 0.46587373977171509 | 3.162191e-15 | 0.46587373977171509; 0.000000e+00 |
| S2 / trend | 2010-01-31–2025-12-31; 192 | rf_main.csv | 0.55031996708074749 | 0.55031996708075026 | 2.822607e-15 | 0.55031996708075015; 1.110223e-16 |
| Z1 / buy_hold | 2003-01-31–2025-12-31; 276 | rf_us.csv | 0.69276890366618094 | 0.69276890366618382 | 2.878594e-15 | 0.69276890366618371; 1.110223e-16 |
| Z1 / rebalance | 2003-01-31–2025-12-31; 276 | rf_us.csv | 0.79165104808229447 | 0.79165104808229914 | 4.686155e-15 | 0.79165104808229914; 0.000000e+00 |
| Z1 / trend | 2003-01-31–2025-12-31; 276 | rf_us.csv | 0.68385473767285254 | 0.68385473767285643 | 3.832979e-15 | 0.68385473767285643; 0.000000e+00 |

### H1-Halbperioden aus den durchgehenden gespeicherten Pfaden

Die „gespeicherten“ Halbperiodenwerte stehen auf drei Dezimalstellen im bestehenden Text, Zelle `59efb4f5` von Analyse.ipynb; kein ungerundeter Halbperiodenexport existiert in den 30 Ergebnisdateien. Deshalb wird korrekt gegen das jeweilige Rundungsintervall ±0,0005 und die tatsächliche Dreistellenrundung geprüft. Keine fiktive exakte Übereinstimmung mit ungerundeten Ursprungswerten behauptet.

| Lauf / Strategie | Zeitraum; n | RF | Unabhängige Sharpe | Textwert | Absolute Differenz |
|:---|:---|:---|:---|:---|:---|
| H1 / buy_hold | 2010-2017; 96 | rf_main.csv | 0.72307674072606876 | 0.723 | 7.674073e-05 |
| H1 / buy_hold | 2018-2025; 96 | rf_main.csv | 0.55467913446138206 | 0.555 | 3.208655e-04 |
| H1 / country_weighting | 2010-2017; 96 | rf_main.csv | 0.71913930800643899 | 0.719 | 1.393080e-04 |
| H1 / country_weighting | 2018-2025; 96 | rf_main.csv | 0.55497274318206724 | 0.555 | 2.725682e-05 |
| H1 / rebalance | 2010-2017; 96 | rf_main.csv | 1.0380042243303094 | 1.038 | 4.224330e-06 |
| H1 / rebalance | 2018-2025; 96 | rf_main.csv | 0.45238085710642434 | 0.452 | 3.808571e-04 |
| H1 / trend | 2010-2017; 96 | rf_main.csv | 0.44433394291722383 | 0.444 | 3.339429e-04 |
| H1 / trend | 2018-2025; 96 | rf_main.csv | 0.45902501925387323 | 0.459 | 2.501925e-05 |

Alle acht runden auf den Textwert. Insbesondere 60/40: **1.0380042243303094→1,038**, danach **0.45238085710642434→0,452**. Ausserdem **12** Sharpe-Tabellenfelder der vier vollständigen Ergebnistabellen gegen die unabhängigen Gesamtwerte gerundet bestätigt; die Haupt-Trendvariante erscheint dabei zweimal. Wiederholte Sharpe-Aussagen im Fliesstext sind mit diesen bestätigten Werten konsistent.

**2’364 gespeicherte Vermögensübergänge** in allen elf Reihen unabhängig mit `V_t/V_(t−1)−1` gegen `period_return` geprüft; alle Anfangswerte 100’000 USD. Höchster numerischer Abstand **2,498001805406602×10⁻¹⁶**, erklärbar durch Division/Subtraktion und den 17-stelligen Float-CSV-Export. Bei nahezu null Rendite ist ein relativer ULP-Vergleich irreführend; geprüft wurde ein expliziter Vorwärtsfehler-Bound `8*eps*abs(V_t/V_(t−1))`. Keine widersprüchliche gespeicherte Rendite festgestellt. Vergleiche in `portfolio-return-consistency.csv`. Keine neuen Backtests oder Vermögenspfade erstellt.

## 6. Phase E: historische WEO-/BIP-Daten und zeitliche Auswahl

**PASS für alle archivierten Zellen, Provenienz und As-of-Auswahl gegen das genehmigte Register; PARTIAL für unabhängige historische Publikations-/Bytezeitbeweiskraft.**

Alle 16 ursprünglichen TSV-Dateien mit `.xls`-Endung direkt gelesen. 2020/2024 als UTF-16 LE ohne BOM aus tatsächlichen Headerbytes erkannt, übrige als Latin-1; keine NUL-Byteentfernung oder Excel-Neuspeicherung. Je Ausgabe genau sieben eindeutige G7-`NGDPD`-Reihen; Beschreibung „Gross domestic product, current prices“, Originaleinheiten `U.S. dollars`/`Billions`, normiert `USD_billions`. Downloadnotizen, Originalnamen, Ausgaben und Downloadseiten stimmen; vorhandene IMF-Fusszeilen stimmen mit der jeweiligen Ausgabe.

Für jedes Land/Ausgabe wurden alle vorhandenen Jahre bis einschliesslich dessen tatsächlichem `Estimates Start After` rekonstruiert. Jahre danach wurden ausgeschlossen; keine prognostizierten bzw. nach genehmigter Regel nicht zugelassenen Zellen in den normalisierten Daten. **4’087/4’087 Werte** und **4’087/4’087 Provenienzzeilen** vollständig gegen ihre Originalzellen abgeglichen, numerisch genau gleicher Floatwert. Ausgabe, Cutoff, Originaltext, Quellzeile/-spalte, Kodierung, Einheit, Verfügbarkeit, Publikationsdatum, Registerevidenz, Quell-/Notizhash stimmen; null fehlende oder doppelte Versionen. **673** Zellen oberhalb der Cutoffs ausgeschlossen. Die Grenze ist die ausdrücklich genehmigte Operationalisierung; sie beweist nicht, dass historische BIP-Zahlen keinerlei Revision oder Messschätzung enthalten.

| Ausgabe | Publikationsdatum im genehmigten Register | available_from | Kodierung | Behalten / oberhalb Cutoff ausgeschlossen |
|:---|:---|:---|:---|:---|
| 2009-10 | 2009-10-01 | 2009-10-02 | latin-1 | 203 / 42 |
| 2010-10 | 2010-10-06 | 2010-10-07 | latin-1 | 210 / 42 |
| 2011-09 | 2011-09-20 | 2011-09-21 | latin-1 | 217 / 42 |
| 2012-10 | 2012-10-08 | 2012-10-10 | latin-1 | 224 / 42 |
| 2013-10 | 2013-10-08 | 2013-10-09 | latin-1 | 231 / 42 |
| 2014-10 | 2014-10-07 | 2014-10-08 | latin-1 | 238 / 42 |
| 2015-10 | 2015-10-06 | 2015-10-07 | latin-1 | 245 / 42 |
| 2016-10 | 2016-10-04 | 2016-10-05 | latin-1 | 252 / 42 |
| 2017-10 | 2017-10-10 | 2017-10-11 | latin-1 | 259 / 42 |
| 2018-10 | 2018-10-09 | 2018-10-10 | latin-1 | 266 / 42 |
| 2019-10 | 2019-10-15 | 2019-10-16 | latin-1 | 273 / 42 |
| 2020-10 | 2020-10-13 | 2020-10-14 | utf-16-le | 280 / 42 |
| 2021-10 | 2021-10-12 | 2021-10-13 | latin-1 | 287 / 42 |
| 2022-10 | 2022-10-11 | 2022-10-12 | latin-1 | 293 / 43 |
| 2023-10 | 2023-10-10 | 2023-10-11 | latin-1 | 301 / 42 |
| 2024-10 | 2024-10-22 | 2024-10-23 | utf-16-le | 308 / 42 |

Die Auswahl wurde ohne Jahresausnahmen rekonstruiert: Versionen nach dem Entscheidungsdatum ausschliessen; abgeschlossene zulässige Bezugsjahre je Land bestimmen; jüngstes gemeinsames Jahr wählen; je Land neueste damals zulässige Version wählen; sieben positive BIP-Werte durch deren gemeinsame Summe teilen. Alle 16 Entscheidungen und 112 Länderzeilen stimmen mit `g7_decision_check.csv`, den H1-/K1-Makroentscheidungen und den dort gespeicherten Zielgewichten. In allen Fällen `available_from <= decision_date`; keine spätere Version rückwirkend eingesetzt. Alle unabhängigen Gewichtssummen sind eins; maximale Float-Summen-/Divisionsdarstellung: Nenner ein ULP (7,275958×10⁻¹² Mrd. USD), Einzelgewichte zwei ULP (1,110223×10⁻¹⁶). Dieselben Gewichte in beiden Runs bestätigt. Exakte Werte und alle Gewichte in `g7-all-112.csv`.

| Entscheidungsdatum | Jüngstes gemeinsames BIP-Jahr | Verwendete Ausgabe |
|:---|:---|:---|
| 2009-12-31 | 2008 | 2009-10 |
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
| 2022-12-31 | 2020 | 2022-10 |
| 2023-12-31 | 2022 | 2023-10 |
| 2024-12-31 | 2023 | 2024-10 |

Sonderfälle ergeben sich aus den normalen Regeln und Rohdateien:

- **2012:** Register-Publikationsdatum 2012-10-08, konservative Verfügbarkeit **2012-10-10**; die Originalzellen tragen diesen gebundenen Verfügbarkeitswert. Diese zweitägige Sonderdatierung ist eine dokumentierte Autorenvorgabe, keine neu erfundene Lauf-Ausnahme.
- **Entscheid 2022:** Sechs G7-Länder haben Cutoff 2021, GBR **2020**. Somit gemeinsames Jahr **2020**, aber neueste damals verfügbare **Ausgabe 2022-10 / available_from 2022-10-12**. Original-GBR-Zelle **2’758,87 Mrd. USD** bestätigt. Kein pauschaler Zwei-Jahres-Lag und kein hartcodierter Austausch gegen WEO 2021.
- **Ende 2025:** kein terminaler Umschichtungsentscheid; letzte wirksame Auswahl 2024-12-31. Keine WEO-2025-Datei erforderlich.

**Historische Beweisgrenze:** Die 16 Publikationsdaten und Verfügbarkeiten stammen aus dem bereits genehmigten Register (`AUTHOR_CONFIRMED_PROMPT_SECTION_6`). Ihre unveränderte Übernahme und die korrekte zeitliche Verwendung sind vollständig kontrolliert. Es wurde keine neue unabhängige Internet-Publikationsprüfung vorgenommen. Downloadnotizen aus Oktober 2026 sowie heutige SHA-256-Werte beweisen die jetzige Snapshot-Identität und Zuordnung, aber nicht kryptografisch, dass exakt dieselben Bytes bereits 2009–2024 öffentlich vorlagen. Dieser Unterschied bleibt ausdrücklich PARTIAL; keine Herkunftsfreigabe aus innerer Konsistenz abgeleitet.

## 7. Vollständige Abweichungen und verbleibende Grenzen

### F-01: FAIL der bytegenauen heutigen Code-/Paketübereinstimmung

**23 eindeutige Dateien**, ausserhalb des versiegelten Archivs; 21 Pythonquellen plus pyproject.toml und requirements.lock. Die heutigen Dateien verwenden zusätzliche CRLF-Zeilenenden. Nach ausschliesslicher Entfernung des `CR` vor `LF` stimmen ihre Bytes exakt mit den versiegelten Originalen überein. Alle 22 Pythonquellen stimmen so zusätzlich mit den Git-Blobs des Engine-Tags überein. `src/funktionen.py` besitzt schon im historischen Snapshot CRLF und stimmt bytegenau; es gehört nicht zu den 23 abweichenden Dateien.

Damit ist **kein inhaltlicher Engine-Wechsel** nachgewiesen. Ein sauberer Git-Status genügt aber nicht zum Beweis gleicher Laufbytes: Git normalisiert Zeilenenden. Die direkte byteweise Quellfingerprint-Prüfung gegen Run-Hashes würde im heutigen primären Checkout scheitern. Archiv/Wheel bestätigen den historischen Code; die übertragenen aktuellen Dateien werden nicht still repariert oder als bytegleich ausgegeben. Auswirkungen: keine nachgewiesene Änderung der Daten, Signale, Sharpe oder Ergebnisrangfolge; Einschränkung der unmittelbaren bytegenauen Laufumgebungsreproduktion. Alle Soll-/Ist-Hashes folgen; `line-ending-discrepancies.csv` enthält zusätzlich Bytegrössen und CRLF-Zählungen.

| Heutiger Engine-Pfad | Historischer Soll-SHA-256 | Tatsächlicher SHA-256 | Historische / heutige Bytes |
|:---|:---|:---|:---|
| pyproject.toml | `54067d49e7515f95dec27c52b50a1ec42fd9a709c646f94298abd3cec4061a58` | `ff9a539bbf6f3cd05dfb2d8372605c16852179da83def12bb4b40395c1afefbd` | 763 / 785 |
| requirements.lock | `5854ff8091c3d4d73b5f35baf66c55279b41e363550234bcf548008585772eaa` | `4ea103169d46a23d19b9a1cb815ad4a4eb337222a23d74e97ec969b12907d813` | 436 / 451 |
| src/__init__.py | `dd5e668e7ec8d8feffff2c77a7a6f463394f1692920398d3d3338721dc7db309` | `0c07a0272a1e755a319227637bcb6e722b1e2789d93ebce61a1338188388b1d5` | 101 / 104 |
| src/__main__.py | `433af79aef67b86ec37a2dfa500ace7d9f8d285b2b2f819056924c2f91eb7122` | `5ec080216ab8dcc62c9dacba185b17d2283296e324e927b7c0b14f1204ead04b` | 747 / 770 |
| src/analysis/__init__.py | `a11362736df2309044bf156076d4fb4259fb7dc34b3e0edc09e4819deff3ad99` | `855d99167c6225bb54ef503d35a94cbc1b4cc3b7315e8f7d8816e13733c64d57` | 67 / 68 |
| src/analysis/metrics.py | `c955eb9a3157a946de58e9cdd3b397ba851eb104744402c824114964d64ec454` | `f4d9372910509d75c2f707b194e98c3f109b498d26cdec3ecbf13f6b6459c825` | 4686 / 4768 |
| src/data/__init__.py | `a452c43bc2c059d9c856148c2ee40aebb88853a3b109ba392870869119880ee2` | `51d344bdcc860073a5f115c93c6efac2393d595137d872811c05667bdc7ddb42` | 46 / 47 |
| src/data/macro.py | `b6c36625ee591d8053c49f4c4ef185c89e8445747b67afd7e661b0625d0bf961` | `32915241e64cfbcc4bb9e81dbcc6cfee691dc0263a2f55575e97b47f4e82072f` | 2214 / 2251 |
| src/data/normalize.py | `42afd037e91f3fc0b8d68d3170c6fcee6712b7230ba1536a7a9d280efab7b996` | `3d583f7f9a8829d789ac27d1280576759d0410fcc99fa7b873a6d5588e619329` | 6390 / 6500 |
| src/data/validate.py | `22ded40e463a70e194d4e5514b1bf2a49145c121bc11eb23af1a8e5ccca3d76a` | `6d646f77a9ee87e85bca5a8959808ca50b43c48748941a682d810d8ffebdf891` | 4499 / 4597 |
| src/engine/__init__.py | `acde14569fa368b317836dd52dec56b36fb360fa456de4190aeb755ee6c2f3b6` | `698c06848c4f1b5c51f22f1e08a895a1c992a3281087469cd1e114e2844e4a83` | 59 / 60 |
| src/engine/config.py | `3e1304d32b827e25235b009ed8481631a0c7782365af9b884481a6ca17600580` | `0452b9007806ce5f672c757f801ddd453118356e8e239bac33221a1f9845402f` | 13271 / 13529 |
| src/engine/context.py | `2d787f4b3a81ee3f9c69e391a3f939749ae68077eb0b6ada19b687db76d016ba` | `ffca5775401d1f100307b172832478f9b84ca74392fb5263f76befccf3a77992` | 4495 / 4579 |
| src/engine/portfolio.py | `9456a06e00204c94364630ef4bc7058b5222f40b5d82384e1847f6be5c5a8cd9` | `864ed8b8a92c5535770ca7926756b36522727571a68d89dec5b58d44bf286bf5` | 4715 / 4791 |
| src/engine/result.py | `03a831cb330fd88545ab81d8e0fb0020bc3a7e2ffb061833af96908136269c30` | `2c0fc6e48f2a75cf52fa35cae30f077b76bfc7fd24c5e7ad0ac4517be8a333f4` | 12982 / 13169 |
| src/engine/simulation.py | `dcdd7f20f8210e0bb3339c9d30740a624e927e45713ccde0827b53413520586f` | `3a8468a90b9b6ccd2a4a724ee8c12fd6454ecaef5bebe1e50c85b72f51b21fe2` | 2004 / 2049 |
| src/export/__init__.py | `46ac359a7e65b21b643763faf4f71d486458449c405a19d4ec29d1cf9f67bb4b` | `243f7ebcd1e02bcefa291f788bd4bcebc7479e195f77911a95f6ea6957de2676` | 50 / 51 |
| src/export/results.py | `7470781d55d3111d8ec970e4e62a41a1b79bb6b2af06a83f05eccbae756cdbc3` | `796e05973b3743371623ce8a8b60707cc2c92240085b480e9949057e6d7cd948` | 5648 / 5753 |
| src/strategies/__init__.py | `1dfe627e6ba9925e92a8977b72285e6945ee31361e4e51cb5542fefe129f8041` | `07daaa2b7bd5d8dd0fc94fbb00db65b550ea0e4e099df011eb36138300c3a633` | 75 / 76 |
| src/strategies/buy_hold.py | `01eca8c59da976097e33f62c59ffe7f59775d57336f921225bab5d761534ab74` | `0af9047f219fecb034e3d5842cb218a82ed77f51d8ba90200810ab01ac571188` | 1256 / 1280 |
| src/strategies/country_weighting.py | `bc2d996c6652ffce2124d85453cc0a0a22dc9b6f6617e6c7448a3dbaea036a4d` | `a851425ea32520a108a17faba30b6d8b8121aa034802b604206c4ceecddd7c50` | 872 / 892 |
| src/strategies/rebalance.py | `24a4b8a6c48b6a2424997d7dcfddc4a9508041ed0f81cb484bea2acf42befc88` | `fca4b9405fde9fc66d66b66c599b76863f3bef29255b19fc599406023b57617f` | 642 / 654 |
| src/strategies/trend.py | `0824da2d4724abf2e081d2b0273840bf42b5275903c1d6fdb7f8d011dd673f79` | `9a82feb9df727600ff231f5f3e70329c3fc538daf06b39d5fb00d91021dab9ec` | 1803 / 1833 |

### N-01: erklärte numerische Darstellungsunterschiede

Keine ungeklärte fachliche numerische Abweichung. Vollständiges Protokoll auch der kleinen Unterschiede in `numeric-comparisons.csv`, `rf-deviations.csv` und den jeweiligen Detailtabellen. Die RF-Floatwerte entsprechen der genehmigten Formel exakt. Unterschiedliche dezimale/binary64-Rundung, SMA-Mittelarithmetik, pandas-RF-Zahlkonvertierung sowie Wertquotienten erklären die konkret ausgewiesenen Reste. Die ursprüngliche strenge Sharpe-Vorprüfung markierte drei Werte oberhalb eines vorläufigen 16-eps-Bounds; die anschliessende konkrete Parserdiagnose erklärte diese vollständig. Die Grenze wurde nicht pauschal erhöht.

### P-01 bis P-04: PARTIAL-Nachweise

1. **P-01, Yahoo-Adjustierung:** Transformation aller archivierten Adj-Close-Werte bestätigt; kein unabhängiger vollständiger Dividenden-/Split-/Total-Return-Nachbau und kein unabhängiger Original-HTTP-Beweis.
2. **P-02, tägliche Vollständigkeit:** eindeutige Tagesbeobachtungen, alle letzten vorhandenen Monatshandelstage und vollständige Monatskalender bestätigt; kein vollständiger Abgleich mit einem unabhängigen Börsenkalender.
3. **P-03, historische WEO-Veröffentlichung:** alle Originalzellen und As-of-Regeln gegen das genehmigte historische Register bestätigt; keine neue externe Publikationsprüfung und kein kryptografischer damaliger Bytezeitbeweis.
4. **P-04, vollständige damalige Laufumgebung:** Archiviertes Wheel, Code, Lock-/Versionsnachweise sind intakt; alle Dependency-Wheels/Installer und die ursprüngliche primäre `.venv-study` sind nicht als vollständige hashgebundene Wiederherstellungsumgebung verfügbar. Vorhandene Backup-pandas-Version nur für Parserdiagnose verwendet; keine vollständige Umgebungswiederherstellung oder bitidentische Drittanbieter-Paketprüfung behauptet.

**BLOCKED:** keine erforderliche Originaldaten-/RF-/Sharpe-/BIP-Teilrechnung aufgrund fehlenden Dateizugangs oder ungeklärter Archivintegrität. Der optionale vorhandene Freeze-CLI wurde nicht ausgeführt und wird nicht als Voraussetzung für die vollständig ausgeführte unabhängige Hash-/Rechenprüfung dargestellt.

**Aussagegrenze des Backtests:** Mathematische Richtigkeit unter genehmigten Eingaben ist von wirtschaftlicher Eignung/Prognosekraft verschieden. ETF-Proxys, nominale USD-Werte, unverzinste Cashphasen, ACT/365-Näherung, Monatsfrequenz, idealisierte Schlussausführung, fehlende zusätzliche Handelskosten/Steuern und fehlende statistische/out-of-sample-Überlegenheitsprüfung bleiben bestehen. Diese Grenzen werden durch den Audit nicht aufgehoben und sind keine neu erfundenen Rechenfehler.

## 8. Entscheidung zu R-017 und Autorenkontrolle

**Teilweise geschlossen, präzise abgegrenzt:** Die damalige fehlende Zugänglichkeit ist behoben. Die offenen direkten Original→Monat-/SMA-, RF-, Sharpe-/Halbperioden- und historischen BIP-Zell-/Auswahlrechnungen sind nun vollständig unabhängig nachgewiesen. Alle geschützten Archivdaten und ursprünglichen Ergebnisse besitzen die historischen Soll-Hashes. Es gibt keinen nachgewiesenen fachlichen Ergebnisfehler und keinen Anlass aus dieser Prüfung, Studienwerte zu ersetzen oder Läufe zu wiederholen.

Eine umfassende Originalherkunfts- und heutige Laufbytes-Gesamtfreigabe wird wegen F-01 und P-01–P-04 nicht erteilt. Das Teilurteil schliesst die konkrete Zugangs-/Rechenlücke, ohne die ausdrücklich akzeptierten Herkunftsgrenzen in ein pauschales PASS umzudeuten. Der historische Befundbericht wird nicht umgeschrieben; dieser Bericht ist sein aktueller ergänzender Nachweis.

Für den Autor verbleiben:

- Diesen Bericht und die dokumentierte reine Zeilenendabweichung kontrollieren; entscheiden, ob der Nachweis der Inhaltsidentität plus intaktem Archiv/Wheel genügt oder eine getrennte bytegetreue Laufumgebungsrekonstruktion gewünscht ist. Eine solche Reparatur/Wiederherstellung ist nicht Teil dieses Auftrags.
- Die schon am 10.10.2026 akzeptierten Anbieter-, Kalender-, WEO- und RF-Näherungsgrenzen in der endgültigen Arbeit beibehalten; keine unzulässige historische/ökonomische Vollbeweisbehauptung hinzufügen.
- **Buch-Sync offen:** neuen KI-Einsatz später autorengeführt in `ki-nutzung.qmd` und die persönliche Reflexion konsolidieren. Beide jetzt unverändert. Der allgemeine Ablauf in `documentation/ai-usage/book-sync.md` wird aufgrund des ausdrücklichen aktuellen Auftrags nicht ausgeführt.
- Externes Prüfverzeichnis und Originalarchiv dauerhaft sichern; der Windows-Tempordner ist der tatsächliche jetzige Ablageort, keine zugesicherte dauerhafte Aufbewahrung.

R-008/R-012/R-016 und andere ausserhalb dieses Datenprüfauftrags liegende formale/historische Pendenzen bleiben ausserhalb des Urteils. Die historische Freigabe vom 10.10.2026 wird als damalige dokumentierte Autorenentscheidung erwähnt; eine neue persönliche Kontrolle oder Freigabe am 13.10.2026 wurde nicht erfunden.

## 9. Reproduzierbare Prüfablage und Ablauf

Programme: `baseline.py` (Ausgangsinventar/Gitkontrollen), `inspect_sources.py` (nur statische Quell-/Schemalesung), `audit.py` (unabhängige A–E-Prüfung), `parser_diagnostic.py` (isolierte historische pandas-Zahlkonvertierung), `supplement.py` (Zeitzone/CRLF/Endpunkte), `deliver.py` (nur die drei erlaubten Dokumentationsziele), `final_verify.py` (Abschlussvergleich).

Nachvollziehbare Befehle, jeweils im oben genannten externen Verzeichnis:

```powershell
python -B baseline.py
python -B inspect_sources.py
& 'C:\Users\modic\Documents\GitHub\Maturarbeit_Engine_Backup\.venv-study\Scripts\python.exe' -B parser_diagnostic.py
python -B audit.py
& 'C:\Users\modic\Documents\GitHub\Maturarbeit_Engine_Backup\.venv-study\Scripts\python.exe' -B supplement.py
python -B final_verify.py
```

`baseline.py` gehört vor die Prüfung, sein ursprünglicher Nachweis darf bei Wiederholung nicht durch neue Ist-Hashes ersetzt werden. Die Datei `baseline.json` ist nur der Vorher-/Nachher-Schutzbeleg dieses Auftrags; historische Freigabehashes stehen weiterhin in Freeze-/Processed-/Acquisition-/Run-Manifesten und den separaten versiegelten Nachweisen. `deliver.py` dient nur der bereits autorisierten Dokumentation, nicht einer erneuten Quellenverarbeitung.

Maschinenbelege: `baseline.json`, `git-before.json`, `hash-comparisons.csv`, `line-ending-discrepancies.csv`, `market-comparisons.csv`, `signal-comparisons.csv`, `rf-all-468.csv`, `rf-deviations.csv`, `sharpe-comparisons.csv`, `sharpe-text-comparisons.csv`, `portfolio-return-consistency.csv`, `weo-all-4087.csv`, `g7-all-112.csv`, `numeric-comparisons.csv`, `failures.csv`, `audit-summary.json`, `parser-diagnostic.json`, `supplement-summary.json`, `final-verification.json` und Laufprotokolle. CSV-Dateien enthalten Vergleichswerte und Abweichungen, keine neuen Studienausgaben.

Vorläufige Fassungen des eigenen Prüfers wurden bei einem falschen JSON-Schlüssel und bei Zuordnungen von Pfad-/Textreferenzen korrigiert; keine Originalquelle geändert. Der anfängliche externe Dateiname `inspect.py` kollidierte mit dem Standardbibliotheksmodul und wurde im externen Verzeichnis umbenannt; dadurch wurden lediglich statische Quellen erneut gelesen, keine Notebook-Zelle oder Studie ausgeführt. Die endgültige vollständige A–E-Ausführung ist `audit-run-final.txt`; sie enthält ausschliesslich die 136 nachvollziehbaren Byte-FAIL-Vergleiche aus F-01, keine fachlichen Rechen-FAILs. Diese externe Prüferentwicklung ist kein Eingriff in die eingefrorene Engine.

## 10. Abschliessende Integritätsprüfung und STOPP

**PASS, tatsächlicher Abschlussvergleich:** Alle **27’313** geschützten ursprünglichen Dateien sind hinsichtlich vollständigem Inventar, Bytegrösse, SHA-256 und Linkmetadaten unverändert: Hauptrepository **18’439/18’440** (einzige erlaubte Bestandsänderung ist das KI-Log), Engine **313/313**, Sicherung **8561/8561**. Unter Raw, Processed, Archiv, Ergebnissen, Notebooks, Buchquellen, bestehenden Ausgaben, virtuellen Umgebungen und Caches keine Änderung, kein Verlust und kein neuer Cache. Die vorhandenen 61 Backup-Änderungen und dessen outputs/-Eintrag bleiben genau im ursprünglichen Zustand. Besonders alle 123 Archiv- und 30 Ergebnisdateien gegen ihre vor der Prüfung gesicherten tatsächlichen Hashes erneut bestätigt.

Genau **drei zulässige Dokumentationsziele**: neuer Bericht, neue byteidentische Promptkopie und genau eine neue Logzeile. Alle 18’440 ursprünglichen Hauptrepository-Dateien ausser dem Log sind bytegleich; **88/89** ursprüngliche versionierte Dateien unverändert. Das vorherige Log mit **45517 Bytes** ist vollständiges identisches Präfix. Prompt-SHA-256: `9188649825aaa7fb62e27fd7b7148550092274882774b23bf922540f9884172b`. `ki-nutzung.qmd` und sämtliche Notebooks/Reflexionsquellen unverändert; Buch-Sync bleibt offen.

HEAD, Branch, Engine-Tag sowie vorhandene Git-HEAD-/Index-/Konfigurations-/commondir-Dateihashes in allen drei Checkouts unverändert. Git-Diff nennt ausschliesslich das KI-Log; die zwei unversionierten Dateien sind Bericht und Promptkopie. Kein gestagter Diff. Der neue Bericht erhielt nach diesem Vergleich nur diesen Abschlussabsatz; keine geschützte Datei wurde danach geschrieben. Vollständiger Nachweis: `C:\Users\modic\AppData\Local\Temp\R017-audit-2026-10-13-173ebe32\final-verification.json`.

Keine Backtests, Downloads, Datenaufbereitung, Notebook-Ausführung, Engine-Änderungen, Paketinstallation/-updates oder Git-Schreibaktionen. Die 23 historischen Soll-/Ist-Codebyteabweichungen bestanden bereits im Ausgangszustand und wurden durch diesen Auftrag weder verursacht noch repariert.

**STOPP zur Autorenkontrolle. Keine Commits und keine Pushes.**

