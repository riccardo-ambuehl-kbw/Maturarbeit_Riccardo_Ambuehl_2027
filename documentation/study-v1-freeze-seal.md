# Study-v1: vorbereiteter Nachweis für die Git-Versiegelung

**Stand:** 2026-10-10. **Status:** `FREEZE_CANDIDATE_READY_FOR_GIT_SEAL`.
Die Daten-/Methodenfreigabe stammt ausdrücklich vom Autor: [Freigabenachweis](study-v1-author-approval.md).
Der lokale Kandidat ist vorbereitet; **kein Git-Commit, Tag, Push, Hauptlauf oder Ergebnisexport erfolgt**.

Archiv: `data/study_v1/archive/study-freeze-v1/`, 123 Dateien einschliesslich Manifest.
Manifestzeitpunkt: **2026-10-10T01:31:52.401339+00:00**.
Das Archiv bleibt lokal und muss separat extern gesichert werden.

SHA-256 des fertigen `freeze_manifest.json`, separat vom Manifest festgehalten:

```text
91d8fe30d1162bf467235a87d5688a13462277e31a6dcff1878ddc3bad0bd51c
```

Verbindlich freigegebener Processed-Manifest-SHA-256:

```text
948865ea3302ced267c9828b9a459ba03cd1c62971c070a818fd4c356c629c28
```

Engine **1.0.0**, Tag **engine-v1.0**, Commit **4a98f3a1039c6ebf4f1bfa1202a1af2e8064b023**.
Archiviertes vorhandenes Wheel `engine/wheels/maturarbeit_engine-1.0.0-py3-none-any.whl`:
`045f0dda4fa4bdb4774390fd166140290ae061d1478e99c1a356c8fc91ed46d2`.

| Ausführungsconfig im Repository | SHA-256 der bytegleichen Archivkopie |
|---|---|
| configs/study_v1/H1.json | cb74b62b49f4d246fa7eff5628315bb3e1923c924ec43544ab7de2942a72ae80 |
| configs/study_v1/K1.json | 395982bfc5d4b40c3b8cccd5afeeceadeea91fda2d1a3e0fc1dac2f4ec04bead |
| configs/study_v1/Z1.json | 5d267c474e1d4ee7220f53f9341b52ef07fed51077352c9528e773ddebeb3527 |
| configs/study_v1/S1.json | bf55de18a2efa13f066d60710856023157189d36a447e6fe79f2f264aec68ea6 |
| configs/study_v1/S2.json | 0cf0ad2c8b0e51c23a1be5a32487dc044274ed26b81bcf4b06ef4106410bdcca |

Die fünf Repository-Configs lesen ausschliesslich die sechs passenden CSV-Kopien unter dem Archivordner `processed/`, jeweils über relative Pfade.
`configuration-records/` enthält unveränderte bytegleiche Sicherungskopien, deren relative Auflösungsbasis weiterhin `project/configs/study_v1/` ist. Bei Wiederherstellung an diese Repository-Stelle zurückkopieren; die Aufzeichnungskopien sind kein zweiter Satz direkt aus ihrem Archivunterordner auszuführender Configs.
Alle Ausführungspfad-, Kalender-, RF-, SMA- und GDP-Prüfungen gelten für die fünf ausdrücklich beauftragten Repository-Configdateien.

**Vor einer später ausdrücklich beauftragten Ausführung erneut prüfen:**

```powershell
.venv-study/Scripts/python.exe scripts/study_v1/verify_freeze.py `
  --archive data/study_v1/archive/study-freeze-v1 `
  --manifest-sha256 91d8fe30d1162bf467235a87d5688a13462277e31a6dcff1878ddc3bad0bd51c
```

Der erwartete Manifesthash muss aus diesem separat versionierten Nachweis stammen; keinen neu berechneten Ist-Hash als Sollwert übernehmen.
Die Prüfhilfe startet keine Simulation. Sie prüft Archiv, Arbeitsdaten-/Aufbereitungshashes, installierte Engine, Config-Hashes und die statischen Eingabekontexte.

Für die Git-Versiegelung vorgesehen: `.gitignore`, `.gitattributes`, die fünf Configs, ursprüngliche Study-v1-Skripte/Register/Tests, neue Prüfhilfe/Tests, beide Auftragskopien, Aufbereitungs-/Autorenfreigabe-/Freeze-Berichte, dieser Nachweis und das append-only KI-Log.
`.gitattributes` fixiert die bereits vorhandenen LF-Zeilenenden der Study-v1-Dateien trotz lokalem `core.autocrlf=true`; SHA-256 `310233ac35cfe7131f758000412f3c53d9d7acb0a8a955dd3931579c9b47c089`.
Diese beiden Git-Steuerdateien und die abschliessenden Nachweise liegen ausserhalb des unveränderten Archivs; so entsteht kein zyklischer Manifest-/Berichtshash.

Vor dem Hauptlauf: vollständiges Archiv extern sichern, Prüfnachweise/Configs kontrollieren und den vorgesehenen Git-Stand ausdrücklich versiegeln. Python-Installer und benötigte Paketdistributionen beziehungsweise die passende Umgebung ebenfalls extern erhalten; archiviert sind Versionsnachweise und das vorhandene Engine-Wheel, nicht sämtliche Abhängigkeits-Wheels.
Die tatsächliche Commit-Kennung ist anschliessend gesondert festzuhalten. Bis dahin `git_sealed=false`; eine automatische Freigabe der Hauptläufe ist damit nicht verbunden.

Prüfumfang und tatsächlicher Git-Status: [Abschlussbericht A–L](study-v1-freeze-preparation.md).
