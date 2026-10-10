# Study-v1: Autorenfreigabe, finale Konfigurationen und Freeze-Vorbereitung

Datum: 2026-10-10. Tool: Codex.

## Vollständiger Auftrag

AUFTRAG: STUDY-V1 – AUTORENFREIGABE, FINALE KONFIGURATIONEN
UND VORBEREITUNG DES STUDIEN-FREEZE

PROJEKT

Repository:
Maturarbeit_Riccardo_Ambuehl_2027

Lokaler Arbeitsordner:
C:\Users\modic\Documents\GitHub\Maturarbeit_Engine

Erwarteter Branch:
study-v1

Eingefrorene Engine:
engine-v1.0

Engine-Commit:
4a98f3a1039c6ebf4f1bfa1202a1af2e8064b023


AUSGANGSLAGE

Die historischen Rohdaten wurden vollständig beschafft.

Der separate Datenadapter wurde implementiert und
mit den tatsächlichen Daten ausgeführt.

30 Adaptertests wurden laut Abschlussbericht bestanden.

Zusätzlich wurde eine unabhängige Kontrolle der
normalisierten Daten durchgeführt.

Dabei wurden insbesondere geprüft:

- 54 ursprüngliche Rohdateien
- 2'406 ETF-Monatswerte
- 468 risikofreie Monatsrenditen
- 4'087 historische BIP-Versionen
- 112 historische G7-Gewichtungsentscheidungen

Bei den unabhängig überprüften Daten und
Berechnungen wurden keine Abweichungen gefunden.

Der Autor hat den geprüften Datenstand und
die dokumentierten Annahmen sowie Grenzen
am 10. Oktober 2026 ausdrücklich freigegeben.

Der freigegebene SHA-256-Hash von

data/study_v1/processed/processed_manifest.json

lautet:

948865ea3302ced267c9828b9a459ba03cd1c62971c070a818fd4c356c629c28

WICHTIG:

Dieser Hash ist verbindlich.

Bei einer Abweichung SOFORT STOPP.

Keine automatische Neuberechnung oder Änderung
des freigegebenen Datenstands.


ZIEL

1. Autorenfreigabe dokumentieren.
2. Fünf endgültige Untersuchungskonfigurationen erstellen.
3. Konfigurationen ohne Backtests validieren.
4. Den vollständigen Studien-Freeze lokal vorbereiten.
5. Rohdaten, normalisierte Daten, Skripte und
   Konfigurationen kryptografisch dokumentieren.
6. Einen kompakten Abschlussbericht erstellen.

KEINE echten Strategieergebnisse berechnen.


--------------------------------------------------
1. VERBINDLICHE ARBEITSREGELN
--------------------------------------------------

Lies zuerst:

AGENTS.md

documentation/engine/release-v1.0.md

documentation/engine/decisions.md

documentation/study-v1-data-preparation.md

scripts/study_v1/prepare_data.py

scripts/study_v1/weo_release_register.csv

data/study_v1/processed/processed_manifest.json

Prüfe ausserdem die tatsächlichen Config-Verträge
und die bestehenden Datenvalidatoren der Engine.

Schütze sämtliche bereits vorhandenen Änderungen
im Arbeitsverzeichnis.

Nicht verändern:

- src/
- eingefrorene Engine v1.0
- bestehende Engine-Tests
- notebooks/
- methodik.qmd
- references.bib
- ursprüngliche Rohdaten
- bisherige normalisierte Daten
- ursprüngliche Download- und Aufbereitungsskripte
- bisherige Engine-Auditnachweise

Keine Dateien zurücksetzen.

Kein git clean.

Keine Daten herunterladen.

Keine neuen Finanzmethoden festlegen.

Keine SMA-Optimierung durchführen.

Keine Backtests starten.

Keinen Commit, Push, Merge oder Tag erstellen.

Bei neuen fachlichen Fragen stoppen und berichten.


--------------------------------------------------
2. DATENSTAND VERIFIZIEREN
--------------------------------------------------

Prüfe:

data/study_v1/processed/processed_manifest.json

SHA-256 muss exakt sein:

948865ea3302ced267c9828b9a459ba03cd1c62971c070a818fd4c356c629c28

Verifiziere anschliessend sämtliche
im Manifest dokumentierten Rohdaten-
und Ergebnisdateien.

Auch Dateigrössen prüfen.

Die freigegebenen Eingabedateien sind:

assets.csv
main_market.csv
us_market.csv
rf_main.csv
rf_us.csv
macro_g7.csv

Zusätzliche Herkunftsnachweise und Berichte
müssen ebenfalls erhalten bleiben.

Keine Daten nachbearbeiten.

Keine neue Version von prepare_data.py ausführen,
um den freigegebenen Stand zu ersetzen.

Wenn ein Hash abweicht:
STOPP und konkreten Befund ausgeben.


--------------------------------------------------
3. AUTORENFREIGABE DOKUMENTIEREN
--------------------------------------------------

Erstelle eine kurze Datei:

documentation/study-v1-author-approval.md

Inhalt:

- Datum der Freigabe: 10.10.2026
- ausdrücklich vom Autor bestätigt
- freigegebener Manifest-SHA-256
- verwendete Rohdatenstände
- Untersuchungszeiträume
- ETF- und Länder-Proxies
- historische WEO-Daten
- DGS3MO-LAGGED-ACT365-Approximation
- dokumentierte Aussagegrenzen
- Status der unabhängigen Datenprüfung

Unterscheide ausdrücklich:

Technische Datenprüfung:
bestanden in den dokumentierten Bereichen.

Autorenentscheidung:
Daten und Methoden zur Untersuchung akzeptiert.

Noch nicht erfolgt:
Studien-Freeze in Git und echte Hauptläufe.

Keine falschen Aussagen über bereits
berechnete Ergebnisse aufnehmen.

Keine Behauptung, dass historische
Yahoo-Adjustierungen vollständig unabhängig
rekonstruiert wurden.

Keine Behauptung, dass die historischen
IMF-Dateibytes kryptografisch auf ihren
ursprünglichen Veröffentlichungstag datiert
werden könnten.


--------------------------------------------------
4. FÜNF ENDGÜLTIGE KONFIGURATIONEN
--------------------------------------------------

Erstelle:

configs/study_v1/H1.json
configs/study_v1/K1.json
configs/study_v1/Z1.json
configs/study_v1/S1.json
configs/study_v1/S2.json

Verwende das tatsächliche JSON-Schema
der eingefrorenen Engine 1.0.0.

Alle Konfigurationen:

schema_version = 1.0

start_capital = 100000

base_currency = USD

periods_per_year = 12

period_frequency = ME

Die Datenpfade müssen relativ zur
jeweiligen Config-Datei korrekt aufgelöst werden.

Die Konfigurationen sollen auf die später
im Studien-Freeze archivierten Kopien
der normalisierten Eingaben zeigen.

NICHT auf eine möglicherweise später
veränderte Arbeitskopie unter processed/.

Ausgabeordner:

outputs/runs/

Die bestehende Gitignore-Regel für
outputs/runs/ muss erhalten bleiben.


H1 – HAUPTUNTERSUCHUNG

Startbewertung:
2009-12-31

Ende:
2025-12-31

Erwartet:
193 Bewertungen, 192 Renditeperioden.

Daten:
main_market.csv
assets.csv
rf_main.csv
macro_g7.csv

Aktivierte Strategien:

A. Buy-and-Hold
WORLD_EQ

B. Jährliches 60/40-Rebalancing

WORLD_EQ = 0.60
US_TREASURY_7_10 = 0.40

C. SMA Long/Cash

Asset:
WORLD_EQ

short_window = 3
long_window = 12
signal_lag = 1
signal_source = performance_value

D. BIP-Ländergewichtung

country_assets:

USA -> US_EQ
CAN -> CA_EQ
JPN -> JP_EQ
GBR -> GB_EQ
DEU -> DE_EQ
FRA -> FR_EQ
ITA -> IT_EQ

indicator = NGDPD
unit = USD_billions

rebalance_frequency = annual


K1 – KONTROLLVERGLEICH

Startbewertung:
2009-12-31

Ende:
2025-12-31

Daten:
main_market.csv
assets.csv
rf_main.csv
macro_g7.csv

Aktivierte Strategien:

A. Jährliches Fixed Rebalancing

Je eines der sieben Länder-Assets
mit einem Zielgewicht von 1/7.

B. BIP-G7-Gewichtung

Dieselben Länder, dieselben ETFs,
dieselben Daten und dieselben
historischen BIP-Regeln wie H1.

Keine Buy-and-Hold- oder Trendstrategie
in K1 aktivieren.

Wichtig:

Die Gleichgewichtung ist kein
Marktkapitalisierungsportfolio.


Z1 – LÄNGERER US-VERGLEICH

WICHTIGE KORREKTUR:

Startbewertung:
2002-12-31

Ende:
2025-12-31

Erwartet:
277 Bewertungen, 276 Renditeperioden.

Daten:
us_market.csv
assets.csv
rf_us.csv

Strategien:

A. Buy-and-Hold

US_EQ

B. Jährliches 60/40-Rebalancing

US_EQ = 0.60
US_TREASURY_7_10 = 0.40

C. SMA Long/Cash

Asset:
US_EQ

short_window = 3
long_window = 12
signal_lag = 1
signal_source = performance_value

Kein BIP-Modell für Z1 aktivieren.

Die vorhandene US-Aktienreihe muss
den Signalvorlauf aus dem Jahr 2002 behalten.

Keine künstlichen IEF-Werte vor Juli 2002.


S1 – ERSTE SMA-SENSITIVITÄT

Startbewertung:
2009-12-31

Ende:
2025-12-31

Nur Trendstrategie aktivieren.

Asset:
WORLD_EQ

short_window = 2
long_window = 12
signal_lag = 1
signal_source = performance_value

Daten:
main_market.csv
assets.csv
rf_main.csv


S2 – ZWEITE SMA-SENSITIVITÄT

Identisch mit S1 ausser:

short_window = 6
long_window = 12

Keine Parameter aufgrund
späterer Renditen verändern.


--------------------------------------------------
5. STUDIEN-FREEZE VORBEREITEN
--------------------------------------------------

Erstelle einen eigenständigen lokalen Archivstand:

data/study_v1/archive/study-freeze-v1/

Der vollständige Ordner muss lokal bleiben
und darf nicht versehentlich nach GitHub
hochgeladen werden.

Erstelle echte Dateikopien.

Keine symbolischen Links oder Hardlinks,
über die spätere Änderungen unbemerkt
auf die archivierten Dateien wirken könnten.

Archiviere mindestens:

- sämtliche 54 ursprünglichen Rohdateien
- alle zwölf normalisierten Datenartefakte
  einschliesslich processed_manifest.json
- tatsächliches Downloadskript
- tatsächliches Aufbereitungsskript
- WEO-Veröffentlichungsregister
- die fünf endgültigen Config-Dateien
- relevante Software-/Versionsnachweise
- Herkunfts- und Prüfberichte

Engine-Version und Engine-Tag dokumentieren.

Wenn die passende lokale Engine-Distribution
bereits vorhanden ist, ihre genaue Datei und
ihren Hash ebenfalls archivieren.

Keine neue Engine-Version bauen,
falls das eine Änderung oder eine zusätzliche
fachliche Entscheidung erfordern würde.

Das Archiv muss so aufgebaut sein,
dass eindeutig erkennbar ist:

1. Welche Daten ursprünglich heruntergeladen wurden.
2. Wie sie verarbeitet wurden.
3. Welche Daten die Engine tatsächlich lesen wird.
4. Mit welchen fünf Konfigurationen gerechnet wird.
5. Welche Version der Engine verwendet wird.

Vorhandene Archivstände nicht überschreiben.

Falls study-freeze-v1 bereits existiert,
zuerst auf Vollständigkeit und bestehende
Hashes prüfen und bei Konflikten stoppen.

Wichtig:

Die Eingabepfade der fünf endgültigen
Konfigurationen müssen tatsächlich
zu den eingefrorenen Kopien führen.

Die Hauptläufe dürfen später nicht
versehentlich die normalen Arbeitsdateien
statt des Freeze-Archivs lesen.


--------------------------------------------------
6. FREEZE-MANIFEST
--------------------------------------------------

Erstelle ein maschinenlesbares
Freeze-Manifest.

Es soll unter anderem enthalten:

- Freeze-Kennung study-freeze-v1
- Datum und Zeitpunkt
- Freigabestatus
- Engine-Version 1.0.0
- Engine-Tag engine-v1.0
- Engine-Commit
- freigegebenen Processed-Manifest-Hash
- alle archivierten Dateipfade
- Dateigrössen
- SHA-256 je Datei
- SHA-256 der fünf Konfigurationen
- dokumentierte Python-/Paketversionen
- Verweise auf Autorenfreigabe und Prüfnachweise

Keinen zyklischen Selbsthash speichern.

Den SHA-256 des fertigen Freeze-Manifests
separat ausgeben und in einem kurzen
Freigabenachweis für die spätere
Git-Versionierung festhalten.

Bis zum abschliessenden Git-Commit ist dies
ein vorbereiteter Freeze-Kandidat.

Nicht behaupten, dass die zeitliche
Fixierung in Git bereits abgeschlossen sei.


--------------------------------------------------
7. GIT-SCHUTZ
--------------------------------------------------

Prüfe die vorhandene .gitignore.

Ergänze nur die erforderlichen Regeln
für lokale Studienumgebungen,
Rohdaten, normalisierte Daten,
Archive und temporäre Ausgaben.

Bereits vorhandene Einträge erhalten.

Achte darauf, dass folgende Dateien
versionierbar bleiben:

- scripts/study_v1/*.py
- scripts/study_v1/weo_release_register.csv
- configs/study_v1/*.json
- tests/study_v1/
- wissenschaftliche und technische Berichte
- Dokumentation der KI-Nutzung

Die umfangreichen Datenarchive
dürfen nicht im Git-Index landen.

Prüfe dies ausdrücklich mit git status
und geeigneten Git-Ignore-Kontrollen.

Kein automatischer Commit.
Kein Push.
Kein Tag.


--------------------------------------------------
8. VALIDIERUNG OHNE BACKTESTS
--------------------------------------------------

Verwende die bestehenden öffentlichen
Validatoren und Config-Loader der Engine.

Prüfe jede der fünf JSON-Dateien.

Die Prüfung muss nachweisen:

- gültiges Engine-Schema
- gültige Assetkennungen
- gültige Datenpfade
- korrekte Währung
- vollständige Bewertungsperioden
- exakt passende RF-Perioden
- vollständigen SMA-Vorlauf
- korrekte Länderzuordnungen
- gültige historische BIP-Versionen
- korrektes G7-Referenzjahr 2020 für 2022
- korrekte Monatsfrequenz ME
- Annualisierung mit 12 Perioden pro Jahr

Die erwarteten Zeiträume:

H1:
2009-12-31 bis 2025-12-31
193 Bewertungen.

K1:
2009-12-31 bis 2025-12-31
193 Bewertungen.

Z1:
2002-12-31 bis 2025-12-31
277 Bewertungen.

S1 und S2:
2009-12-31 bis 2025-12-31
193 Bewertungen.

Alle Referenzen müssen auf Dateien
innerhalb des vorbereiteten Freeze-Archivs
zeigen.

Führe ausschliesslich statische
Daten- und Konfigurationsprüfungen aus.

prepare_context ist zur Prüfung erlaubt,
sofern dadurch keine Strategieperformance
berechnet oder ein Run exportiert wird.

Verboten:

run_simulation

python -m maturarbeit_engine run

Aufruf der konkreten Strategieklassen
zur Berechnung tatsächlicher Ergebnisse.

Auch keine testweisen
Echtdaten-Backtests ausführen.

Vorhandene Adaptertests erneut ausführen.

Neue fokussierte Tests für Archivintegrität,
Config-Pfade und Freeze-Schutz erstellen,
soweit dafür notwendig.

Keine bestehenden Tests abschwächen.


--------------------------------------------------
9. ABSCHLUSSBERICHT
--------------------------------------------------

Erstelle einen kompakten Bericht:

documentation/study-v1-freeze-preparation.md

Beantworte ausdrücklich:

A. Wurde der freigegebene Manifest-Hash bestätigt?

B. Wurden alle Rohdaten- und Processed-Hashes
   erfolgreich geprüft?

C. Welche neuen Dateien wurden erstellt?

D. Welche fünf Config-Dateien wurden erzeugt?

E. Welche genauen Zeiträume und
   Strategien sind eingestellt?

F. Zeigen alle Config-Dateipfade auf
   den vorbereiteten Archivstand?

G. Ist das Archiv vollständig?

H. Wie lautet der SHA-256 des
   neuen Freeze-Manifests?

I. Welche Tests wurden tatsächlich ausgeführt?

J. Gab es Fehler, offene Entscheidungen
   oder methodische Auffälligkeiten?

K. Welche Dateien müssen vor dem Hauptlauf
   noch versioniert beziehungsweise
   extern gesichert werden?

L. Sind die fünf Konfigurationen technisch
   für die spätere Ausführung bereit?

Abschlussstatus nur bei vollständig
bestandenem Prüfprogramm:

FREEZE_CANDIDATE_READY_FOR_GIT_SEAL

Andernfalls:

FREEZE_PREPARATION_BLOCKED

Keine automatische Freigabe
der eigentlichen Hauptläufe.

Keine Strategieresultate erzeugen.

Keine Änderungen an der eingefrorenen Engine.

Keine Commits, Pushes, Merges oder Tags.

Gib am Ende den tatsächlichen Git-Status,
den neuen Manifest-Hash und die
konkreten nächsten Schritte an.

ENDE DES AUFTRAGS