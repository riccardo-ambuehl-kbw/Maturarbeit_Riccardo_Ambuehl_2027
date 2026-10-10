# Study-v1: Datenadapter und Echtdatenprüfung

**Datum:** 2026-10-10. **Tool:** Codex.

Der folgende vollständige Auftrag wurde vom Autor vorgegeben. Er bestätigt insbesondere Auswahl, Zeiträume, RF-Näherung und WEO-Verfügbarkeitsregister; Codex entscheidet diese Werte nicht selbst.

## Vollständiger Auftrag

AUFTRAG: STUDY-V1 DATENADAPTER – IMPLEMENTIERUNG UND ECHTDATENPRÜFUNG

PROJEKT
Repository:
Maturarbeit_Riccardo_Ambuehl_2027

Lokaler Arbeitsordner:
C:\Users\modic\Documents\GitHub\Maturarbeit_Engine

Erwarteter Branch:
study-v1

Eingefrorene Engine:
engine-v1.0
Commit:
4a98f3a1039c6ebf4f1bfa1202a1af2e8064b023

ZIEL

Implementiere einen separaten, reproduzierbaren Datenadapter
für die wissenschaftliche Untersuchung meiner Maturarbeit.

Die allgemeinen Berechnungen und Strategien sind in Engine
v1.0 bereits fertiggestellt.

Der Adapter soll ausschliesslich die vorhandenen historischen
Rohdaten in die von der Engine erwarteten CSV-Dateien
umwandeln, die Verarbeitung dokumentieren und die Daten
umfassend prüfen.

Es dürfen noch KEINE echten Strategieläufe durchgeführt werden.

--------------------------------------------------
1. VORBEREITUNG UND GRENZEN
--------------------------------------------------

Lies zuerst:
- AGENTS.md
- documentation/engine/release-v1.0.md
- documentation/engine/decisions.md
- die tatsächlichen Engine-Datenverträge unter src/data/
- die tatsächliche Engine-Konfigurationsstruktur
- scripts/study_v1/download_studien_rohdaten.py

Prüfe:
- aktueller Branch ist study-v1
- Engine-Tag zeigt auf den erwarteten Commit
- vorhandene lokale Änderungen
- vollständige Rohdatenverzeichnisse

Keine Änderungen an:
- src/
- bestehender Engine v1.0
- Engine-Tests oder Engine-Auditnachweisen
- notebooks/
- methodik.qmd
- references.bib
- bestehenden Rohdateien

Keine neuen Strategie- oder Finanzformeln innerhalb
der Engine implementieren.

Keinen Commit, Push, Merge oder Tag ohne Freigabe.

Keine vorhandenen Dateien zurücksetzen.

Keine Dateien mit git clean oder vergleichbaren
Befehlen löschen.

Keine Daten aus dem Internet nachladen.
Ausschliesslich die vorhandenen lokalen Rohdaten verwenden.

Falls eine fachliche Entscheidung offen ist oder Daten
nicht mit den vereinbarten Regeln verarbeitet werden
können: STOPP mit konkretem Bericht.

--------------------------------------------------
2. VORHANDENE ROHDATEN
--------------------------------------------------

ETF- und FRED-Daten:

data/study_v1/raw/download_20261008T014620197765Z/

Darin:
- yahoo/VT.csv
- yahoo/IEF.csv
- yahoo/VTI.csv
- yahoo/EWC.csv
- yahoo/EWJ.csv
- yahoo/EWU.csv
- yahoo/EWG.csv
- yahoo/EWQ.csv
- yahoo/EWI.csv
- passende Metadaten
- fred/DGS3MO.csv
- acquisition_manifest.json

IMF-Daten:

data/study_v1/raw/imf/

Darin liegen 16 getrennte Ausgaben:

2009-10
2010-10
2011-09
2012-10
2013-10
2014-10
2015-10
2016-10
2017-10
2018-10
2019-10
2020-10
2021-10
2022-10
2023-10
2024-10

Jeder Ordner enthält die ursprüngliche WEO-Datei
und eine download_note.txt.

Alle Daten wurden bereits einer ersten Eingangsprüfung
unterzogen.

Trotzdem muss der Adapter die tatsächlichen Dateien
selbstständig validieren.

Insbesondere:
- Dateiformate
- Spalten
- Währungen
- Zahlenwerte
- Zeiträume
- Duplikate
- fehlende Beobachtungen
- SHA-256
- Quellenzuordnung

Die Rohdateien dürfen niemals verändert werden.

Keine automatische Auswahl eines anderen Rohdatenstands,
falls der ausdrücklich angegebene Ordner fehlt.

--------------------------------------------------
3. IMPLEMENTIERUNG
--------------------------------------------------

Erstelle:

scripts/study_v1/prepare_data.py

Zusätzliche kleine Hilfsdateien sind erlaubt,
wenn sie technisch wirklich sinnvoll sind.

Keine umfangreiche neue Ordnerstruktur oder
generierte Projektvorlage erstellen.

Neue Tests gehören in den bestehenden Testbereich
oder einen klar abgegrenzten Study-v1-Testbereich.

Der Adapter soll über die Kommandozeile aufrufbar sein.

Rohdatenverzeichnis und Ausgabeordner müssen
explizit angegeben werden können.

Die Verarbeitung erfolgt vollständig offline.

Verwende die bestehende .venv-study mit
pandas 2.3.3 und NumPy 2.3.5.

Keine unnötigen neuen Abhängigkeiten installieren.

--------------------------------------------------
4. MARKTDATEN
--------------------------------------------------

Asset-Mapping:

VT  -> WORLD_EQ
IEF -> US_TREASURY_7_10
VTI -> US_EQ
EWC -> CA_EQ
EWJ -> JP_EQ
EWU -> GB_EQ
EWG -> DE_EQ
EWQ -> FR_EQ
EWI -> IT_EQ

Die verwendeten Kurse stammen aus:

Adj Close

Die Renditeberechnung wird später durch die Engine
aus diesen normalisierten Werten durchgeführt.

Der Adapter berechnet keine Strategieperformance.

Wichtig:
- Keine zusätzliche Dividendenrendite addieren.
- Keine doppelte Split- oder Dividendenanpassung.
- Kein automatisches Forward-Fill.
- Keine Interpolation.
- Keine erfundenen Handelstage.
- Fehlende notwendige Werte führen zur Datenprüfung
  beziehungsweise zum dokumentierten Abbruch.

Prüfe anhand der Metadaten die USD-Notierung.

Die USD-Notierung darf nicht mit einer vollständigen
Absicherung des wirtschaftlichen Wechselkursrisikos
verwechselt werden.

MONATLICHE BEWERTUNG

Für jeden Monat wird der letzte tatsächlich beobachtete
Handelstag des jeweiligen ETF ausgewählt.

Die normalisierte Bewertung erhält als Datum
das rechte Kalender-Monatsende.

Beispiel:
Letzter beobachteter Handelstag: 29.01.2010
Engine-Datum: 31.01.2010

Der tatsächliche Quellhandelstag wird separat
in der Provenienz gespeichert.

Das Monatslabel darf nicht als erfundene tatsächliche
Börsenbeobachtung ausgegeben werden.

Die vorhandenen ETFs sind US-notiert.

Prüfe für alle benötigten Assets, ob der letzte
beobachtete Handelstag je Monat übereinstimmt.

Bei Abweichungen nicht stillschweigend einen
anderen Bewertungstag auswählen.

Stattdessen den konkreten Sachverhalt mit
Asset, Monat und Quellbeobachtungen melden.

HAUPTUNTERSUCHUNG

Auswertungszeitraum:
01.01.2010 bis 31.12.2025

Anfängliche Bewertung:
31.12.2009

Erwartet:
193 Monatsbewertungen von Dezember 2009
bis Dezember 2025.

Daraus:
192 monatliche Renditeperioden.

Für den SMA-Vorlauf werden die vorhandenen
Beobachtungen aus 2009 benötigt.

Die Hauptmarktdatei muss alle neun Assets abdecken.

US-ZUSATZUNTERSUCHUNG

WICHTIG: Der Zeitraum wurde gegenüber alten
Entwürfen ausdrücklich korrigiert.

Renditezeitraum:
01.01.2003 bis 31.12.2025

Anfängliche Bewertung:
31.12.2002

Erwartet:
277 Bewertungen von Dezember 2002
bis Dezember 2025.

Daraus:
276 monatliche Renditeperioden.

VTI benötigt für den SMA-Vorlauf Beobachtungen
aus Januar bis Dezember 2002.

IEF ist erst seit Juli 2002 im vorhandenen
Rohdatensatz beobachtbar.

Daher:
- VTI-Vorlauf ab Januar 2002 erhalten.
- IEF nicht künstlich vor seine erste Beobachtung
  zurückverlängern.
- Ab Dezember 2002 benötigen beide ETFs
  gemeinsame Bewertungen.
- SMA-Vorlauf und eigentlicher Performancezeitraum
  müssen getrennt bleiben.

Die Engine unterstützt einen eigenen beobachteten
SMA-Vorlauf für das Signal-Asset.

Die US-Marktdatei muss diese Eigenschaft
korrekt berücksichtigen.

--------------------------------------------------
5. RISK-FREE-ADAPTER
--------------------------------------------------

Quelle:
FRED DGS3MO

Die Rohdaten enthalten tägliche annualisierte
Zinsnotierungen in Prozent.

Sie sind keine fertigen monatlichen Renditen.

Die folgende Methode ist vom Autor bestätigt:

Für jede monatliche Renditeperiode:

1. Bestimme den tatsächlichen Quellhandelstag
   der anfänglichen Portfolio-Bewertung.

2. Wähle die letzte gültige DGS3MO-Notierung,
   deren Datum strikt VOR diesem Handelstag liegt.

3. Wenn keine passende Notierung existiert
   oder sie mehr als sieben Kalendertage zurückliegt:
   dokumentierter Abbruch.

4. Berechne die einfache Periodenapproximation:

   period_return =
       (annual_rate_percent / 100)
       * (calendar_days / 365)

calendar_days ist die Anzahl Kalendertage zwischen
den beiden Kalender-Monatsendlabels.

Diese Methode heisst:
DGS3MO_LAGGED_ACT365_APPROX

Sie ist eine ausdrücklich gewählte Näherung,
keine gemessene Rendite eines konkret gehaltenen
dreimonatigen Staatsanleihenportfolios.

Fehlende tägliche Zinsbeobachtungen nicht
als Null interpretieren.

Erzeuge exakte Engine-Perioden:

period_start,period_end,series_id,period_return

Die Grenzen müssen zu den Monatsbewertungen passen.

Für Haupt- und US-Untersuchung separate Dateien
vorbereiten.

Die Zinsverarbeitung darf keine Informationen
aus dem Ende einer noch nicht begonnenen Periode
verwenden.

--------------------------------------------------
6. HISTORISCHE IMF-BIP-DATEN
--------------------------------------------------

Verwende ausschliesslich:

Indikator:
NGDPD

Bedeutung:
Nominales Bruttoinlandsprodukt in laufenden USD.

Einheit für die Engine:
USD_billions

Länder:
USA
CAN
JPN
GBR
DEU
FRA
ITA

Für jede der 16 Ausgaben:
- Originaldatei lesen
- Dateikodierung erkennen
- Ausgabe eindeutig zuordnen
- benötigte Länder extrahieren
- NGDPD eindeutig identifizieren
- Einheiten kontrollieren
- Estimates Start After auswerten
- historische Jahreswerte extrahieren

DATEIKODIERUNGEN

Die untersuchten Rohdateien sind trotz .xls-Endung
tabulatorgetrennte Textdateien.

Die meisten sind als Latin-1 lesbar.

2020 und 2024 verwenden UTF-16 LE ohne BOM.

Diese Unterschiede korrekt behandeln.

NUL-Bytes der UTF-16-Dateien sind normal.
Sie dürfen nicht durch blindes Entfernen
"repariert" werden.

Mögliche Fusszeilen dürfen nicht als Datenzeilen
interpretiert werden.

Fehlwerte dürfen nicht als Nullwerte übernommen werden.

HISTORISCHE ISTWERTE

Verwende je Ausgabe und Land nur Referenzjahre,
die gemäss Estimates Start After zum damaligen
historischen Datenbestand gehören.

Beispiel:
Estimates Start After = 2008

Dann gelten Referenzjahre bis einschliesslich
2008 gemäss diesem Feld als historische Istwerte.

Spätere Jahre werden für diese Ausgabe ausgeschlossen.

Die Einordnung als Istwert bedeutet nicht,
dass spätere Revisionen ausgeschlossen sind.

Alle zulässigen historischen Versionen behalten
ihr jeweiliges Verfügbarkeitsdatum.

Keine modernen BIP-Daten rückwirkend einsetzen.

VERÖFFENTLICHUNGSDATEN

Der Autor hat folgende historische Datierung
und die konservative Verfügbarkeitsregel bestätigt:

Ausgabe    Datierung     Verwendbar ab
2009-10    2009-10-01    2009-10-02
2010-10    2010-10-06    2010-10-07
2011-09    2011-09-20    2011-09-21
2012-10    2012-10-08    2012-10-10
2013-10    2013-10-08    2013-10-09
2014-10    2014-10-07    2014-10-08
2015-10    2015-10-06    2015-10-07
2016-10    2016-10-04    2016-10-05
2017-10    2017-10-10    2017-10-11
2018-10    2018-10-09    2018-10-10
2019-10    2019-10-15    2019-10-16
2020-10    2020-10-13    2020-10-14
2021-10    2021-10-12    2021-10-13
2022-10    2022-10-11    2022-10-12
2023-10    2023-10-10    2023-10-11
2024-10    2024-10-22    2024-10-23

Die Daten stammen aus der bereits durchgeführten
Prüfung offizieller IMF-Publikationsnachweise.

Erstelle daraus ein kleines versioniertes Register,
das Ausgabe, belegte Datierung, Verfügbarkeit
und Quellenbeleg getrennt dokumentiert.

Nutze vorhandene Original-Downloadnotizen für
die eindeutige Ausgabezuordnung.

WICHTIGE AUSNAHME 2012:

Die IMF-Publikationsseite nennt den 08.10.2012.

Die öffentliche Vorstellung ist für den
09.10.2012 dokumentiert.

Deshalb gilt für die Untersuchung vorsichtig
der 10.10.2012 als available_from.

Nicht behaupten, dies sei das eindeutig
nachgewiesene erste Veröffentlichungsdatum
der konkreten CSV-Dateibytes.

Die Datierung einer IMF-Ausgabe belegt nicht
kryptografisch das damalige Vorliegen exakt
derselben heute archivierten Dateiversion.

Diese Grenze im Provenienzbericht dokumentieren.

BIP-ENGINE-FORMAT

period,country,indicator,value,unit,available_from

Mehrere historische Versionen desselben
BIP-Bezugsjahres müssen erhalten bleiben.

--------------------------------------------------
7. G7-KONTROLLRECHNUNG
--------------------------------------------------

Zusätzlich zur Macro-CSV eine Kontrolltabelle
für alle tatsächlich benötigten Jahresendentscheidungen
erstellen.

Für jede Entscheidung prüfen:

- Welche WEO-Ausgabe war damals verfügbar?
- Welches ist das jüngste gemeinsame zulässige
  historische BIP-Jahr der sieben Länder?
- Welche konkreten historischen Datenversionen
  werden verwendet?
- Sind alle sieben Werte positiv und gültig?
- Ergeben die berechneten Zielgewichte zusammen 1?

Keine BIP-Werte unterschiedlicher Bezugsjahre
innerhalb einer Entscheidung mischen.

WICHTIGER REGRESSIONSTEST:

WEO-Ausgabe Oktober 2022.

Estimates Start After:
GBR = 2020
übrige sechs G7-Länder = 2021

Daraus muss für den Jahresendentscheid 2022
das gemeinsame BIP-Referenzjahr 2020 folgen.

Die Werte stammen dabei aus der WEO-Ausgabe 2022,
nicht aus einer älteren Ausgabe mit gleichem Bezugsjahr.

Insbesondere:
GBR, 2020, WEO 2022 = 2,758.87 Mrd. USD.

Dies ist ein echter Kontrollfall aus den Rohdaten.

Die Jahreswahl nicht als feste Ausnahmeliste
programmieren, sondern aus den tatsächlichen
historischen Informationen ableiten.

Diese Kontrollrechnung ist noch kein Backtest.

--------------------------------------------------
8. ERWARTETE AUSGABEDATEIEN
--------------------------------------------------

Unter:

data/study_v1/processed/

werden folgende Dateien benötigt:

assets.csv
main_market.csv
us_market.csv
rf_main.csv
rf_us.csv
macro_g7.csv

Zusätzliche Herkunftsnachweise:

observation_provenance.csv
risk_free_provenance.csv
macro_provenance.csv
g7_decision_check.csv

Zusätzlich:

normalization_report.json
processed_manifest.json

Die Engine-Eingaben müssen exakt die jeweils
erforderlichen Pflichtspalten besitzen.

Zusatzspalten nur verwenden, wenn sie
mit dem Engine-Vertrag vereinbar sind.

Die Herkunftstabellen dürfen weitere
technische Kontrollfelder enthalten.

Für jede verwendete Rohdatei den SHA-256
und die tatsächliche Herkunft dokumentieren.

Auch das verwendete Aufbereitungsskript
und seine Softwareumgebung dokumentieren.

CSV-Dateien:
- UTF-8
- saubere Header
- eindeutige Zuordnung
- ISO-Datumsformat
- keine NaN/Infinity-Ausgaben
- keine fehlenden notwendigen Werte

Ergebnisdateien nicht still überschreiben.

Bei vorhandenen Ausgaben mit abweichendem Inhalt
neuen Kandidatenstand erzeugen oder stoppen.

Noch keinen endgültigen Study-Freeze durchführen.

--------------------------------------------------
9. TESTS UND ECHTDATENPRÜFUNG
--------------------------------------------------

Erstelle fokussierte Tests für den neuen Adapter.

Mindestens prüfen:

1. Tagesdaten zu monatlichen Bewertungen.
2. Tatsächlicher Quellhandelstag bleibt erhalten.
3. Fehlende Monate führen zum Abbruch.
4. Unterschiedliche letzte Handelstage werden erkannt.
5. Adj Close wird ohne doppelte Dividendenanpassung verwendet.
6. RF-Auswahl liegt strikt vor dem Quellhandelstag.
7. RF-Umrechnung Prozent zu Dezimal.
8. ACT/365 mit tatsächlichen Kalendertagen.
9. RF-Perioden stimmen exakt mit Marktperioden überein.
10. Latin-1- und UTF-16-WEO-Dateien.
11. Historische Istwerte und Ausschluss von Prognosen.
12. Historische BIP-Versionen ohne Look-ahead.
13. Gemeinsames G7-BIP-Jahr.
14. Echter WEO-Sonderfall 2022.
15. Konsistente Länder- und Asset-Kennungen.
16. Reproduzierbare Ausgabedateien und Hashes.
17. Rohdateien bleiben bytegleich.

Danach den Adapter mit den vorhandenen echten
Rohdaten ausführen.

Prüfe die fertigen Engine-Eingaben möglichst mit
den bestehenden öffentlichen Validierungsfunktionen
der eingefrorenen Engine.

Dabei ausdrücklich keine Simulation starten.

Kontrolliere:

HAUPTLAUF:
193 Monatsbewertungen
192 Monatsrenditeperioden
Start 2009-12-31
Ende 2025-12-31

US-ZUSATZLAUF:
277 Monatsbewertungen
276 Monatsrenditeperioden
Start 2002-12-31
Ende 2025-12-31

Beide:
USD
ME
12 Perioden pro Jahr

Zusätzlich:
vollständiger SMA-Vorlauf von zwölf
Monatsbeobachtungen am jeweiligen Start.

Bei Problemen:
nicht die Zeiträume automatisch verkürzen.

Stattdessen konkrete Fehlerursache melden.

--------------------------------------------------
10. ABSCHLUSSBERICHT
--------------------------------------------------

Nach Implementierung und Echtdatenprüfung
einen kompakten Bericht erstellen.

Berichte:

A. Welche Dateien wurden erstellt oder geändert?

B. Welche Rohdaten wurden tatsächlich verwendet?

C. Wie viele Beobachtungen enthält jede
   normalisierte Marktdatei?

D. Welche Monatszeiträume sind vollständig?

E. Welche Zinsumrechnung wurde tatsächlich umgesetzt?

F. Welche historischen BIP-Daten wurden übernommen?

G. Welche BIP-Referenzjahre werden bei den
   16 Jahresendentscheidungen ausgewählt?

H. Welche Tests wurden tatsächlich ausgeführt?

I. Welche Tests sind bestanden oder fehlgeschlagen?

J. Gibt es Datenprobleme, Unsicherheiten oder
   Abweichungen von den Vorgaben?

K. Sind die normalisierten Daten technisch
   bereit für die anschliessende manuelle Freigabe?

Das Ergebnis darf höchstens den Status

NORMALIZED_PENDING_AUTHOR_APPROVAL

erhalten.

Nicht als wissenschaftlich freigegeben bezeichnen.

Keine Strategieergebnisse berechnen.

Keine fünf Hauptläufe starten.

Keine finalen Untersuchungskonfigurationen
ungeprüft übernehmen.

Keine automatische Datenfreigabe.

Kein Commit oder Push.

--------------------------------------------------
11. ARBEITSWEISE
--------------------------------------------------

Arbeite eigenständig innerhalb dieser bestätigten
technischen und methodischen Grenzen.

Untersuche und behebe technische Programmfehler.

Schwäche keine Tests ab, damit sie bestehen.

Melde neue fachliche Entscheidungsfragen,
anstatt sie selbst zu beantworten.

Das Repository soll übersichtlich bleiben.

Versioniere die tatsächlichen Aufbereitungsskripte,
kleine notwendige Quellenregister und Tests.

Keine umfangreichen generierten Planordner.

Die normalisierten Daten bleiben zunächst lokal.

Dokumentiere die KI-Unterstützung gemäss
documentation/ai-usage/README.md.

Am Ende den vollständigen Prüfstatus und
die konkreten nächsten Schritte ausgeben.

ENDE DES AUFTRAGS