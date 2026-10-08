from __future__ import annotations

import argparse
import csv
from datetime import date, datetime, timezone
from hashlib import sha256
from importlib import metadata
import io
import json
from pathlib import Path
import platform
import sys
import time
from typing import Any
from urllib.request import Request, urlopen

SCRIPT_VERSION = "1.1.0"

ASSETS = (
    ("VT", "WORLD_EQ", "2009-01-01"),
    ("IEF", "US_TREASURY_7_10", "2002-01-01"),
    ("VTI", "US_EQ", "2002-01-01"),
    ("EWC", "CA_EQ", "2009-01-01"),
    ("EWJ", "JP_EQ", "2009-01-01"),
    ("EWU", "GB_EQ", "2009-01-01"),
    ("EWG", "DE_EQ", "2009-01-01"),
    ("EWQ", "FR_EQ", "2009-01-01"),
    ("EWI", "IT_EQ", "2009-01-01"),
)

END_EXCLUSIVE = "2026-01-01"
FRED_START = "2002-01-01"
FRED_END = "2025-12-31"
FRED_URL = (
    "https://fred.stlouisfed.org/graph/fredgraph.csv?"
    f"id=DGS3MO&cosd={FRED_START}&coed={FRED_END}"
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_json(path: Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False, default=str) + "\n",
        encoding="utf-8",
    )


def installed_versions() -> dict[str, str]:
    result = {}
    for distribution in metadata.distributions():
        name = distribution.metadata.get("Name")
        if name:
            result[name] = distribution.version
    return dict(sorted(result.items(), key=lambda item: item[0].lower()))


def history_snapshot(frame: Any, start: str, end: str) -> tuple[Any, dict[str, Any]]:
    """Preserve provider fields and rows; add exchange-local date and timestamp."""
    import pandas as pd

    if frame is None or frame.empty:
        raise ValueError("Keine Kursbeobachtungen erhalten; kein Ersatzdatensatz.")
    if not frame.columns.is_unique:
        raise ValueError("Doppelte Quellspalten.")
    missing = {"Close", "Adj Close"} - set(frame.columns)
    if missing:
        raise ValueError(f"Erforderliche Quellspalten fehlen: {sorted(missing)}")
    if {"date", "source_timestamp"} & set(frame.columns):
        raise ValueError("Reservierte Herkunftsspalten bereits in der Quelle vorhanden.")
    index = pd.DatetimeIndex(frame.index)
    if not index.is_unique or not index.is_monotonic_increasing or index.hasnans:
        raise ValueError("Quellzeitpunkte nicht vollstaendig, eindeutig und aufsteigend.")
    local = index.tz_localize(None) if index.tz is not None else index
    labels = local.strftime("%Y-%m-%d")
    if len(set(labels)) != len(labels):
        raise ValueError("Mehr als eine Beobachtung je lokalem Boersendatum.")
    if min(labels) < start or max(labels) >= end:
        raise ValueError("Gelieferte Daten ausserhalb des angeforderten Zeitraums.")
    result = frame.copy()
    result.insert(0, "source_timestamp", [value.isoformat() for value in index])
    result.insert(0, "date", labels)
    return result.reset_index(drop=True), {
        "rows": len(result),
        "first_date": min(labels),
        "last_date": max(labels),
        "source_timezone": str(index.tz),
        "columns": list(result.columns),
        "missing_cells_by_column": {
            str(key): int(value) for key, value in result.isna().sum().items()
        },
        "data_quality": "NOT_YET_APPROVED",
    }


def inspect_fred(payload: bytes) -> dict[str, Any]:
    """Identify the raw series and interval, without calculating period returns."""
    if b"\x00" in payload:
        raise ValueError("FRED-Datei enthaelt NUL-Bytes.")
    rows = list(csv.reader(io.StringIO(payload.decode("utf-8-sig")), strict=True))
    if len(rows) < 2 or len(rows[0]) != 2:
        raise ValueError("FRED hat keine erwartete zweispaltige CSV geliefert.")
    if rows[0][0] not in {"observation_date", "DATE", "date"} or rows[0][1] != "DGS3MO":
        raise ValueError(f"Unerwarteter FRED-Header: {rows[0]!r}")
    if any(len(row) != 2 for row in rows[1:]):
        raise ValueError("Fehlerhafte FRED-Feldzahl.")
    dates = [date.fromisoformat(row[0]) for row in rows[1:]]
    if any(a >= b for a, b in zip(dates, dates[1:])):
        raise ValueError("FRED-Zeitpunkte nicht eindeutig aufsteigend.")
    if dates[0] < date.fromisoformat(FRED_START) or dates[-1] > date.fromisoformat(FRED_END):
        raise ValueError("FRED-Zeitraum ausserhalb der Anfrage; Originalantwort aufbewahrt.")
    return {
        "rows": len(dates), "columns": rows[0],
        "first_date": dates[0].isoformat(), "last_date": dates[-1].isoformat(),
        "missing_markers": sum(row[1] in {"", "."} for row in rows[1:]),
        "value_semantics": "RAW_ANNUAL_PERCENT_YIELD_NOT_PERIOD_RETURN",
        "data_quality": "NOT_YET_APPROVED",
    }


def file_records(root: Path, excluded: Path) -> list[dict[str, Any]]:
    return [
        {"path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size,
         "sha256": sha256(path.read_bytes()).hexdigest()}
        for path in sorted(root.rglob("*")) if path.is_file() and path != excluded
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True, help="Parent directory for new raw snapshots.")
    parser.add_argument("--download", action="store_true", help="Run the explicitly listed downloads.")
    args = parser.parse_args(argv)
    if not args.download:
        parser.error("Zum Start --download angeben; keine Daten werden automatisch geladen.")
    try:
        import yfinance as yf
        import pandas
    except ImportError as exc:
        print(f"Download-Abhaengigkeit fehlt: {exc}. Separate .venv-study verwenden.", file=sys.stderr)
        return 2

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    root = args.out.resolve() / f"download_{stamp}"
    root.mkdir(parents=True, exist_ok=False)
    (root / "yahoo").mkdir()
    (root / "fred").mkdir()
    manifest_path = root / "acquisition_manifest.json"
    manifest: dict[str, Any] = {
        "script_version": SCRIPT_VERSION,
        "created_at_utc": utc_now(), "status": "IN_PROGRESS",
        "python": sys.version, "platform": platform.platform(),
        "backtest_executed": False,
        "purpose": "Raw acquisition only; no normalization or data approval.",
        "yahoo_snapshot_kind": "yfinance output, not original HTTP response bytes",
        "requests": [], "files": [], "warnings": [],
    }
    write_json(manifest_path, manifest)
    print(f"Neuer Rohdatenstand: {root}", flush=True)
    try:
        
        (root / "acquisition_script_used.py").write_bytes(Path(__file__).read_bytes())
        write_json(root / "environment_versions.json", installed_versions())
        for symbol, asset_id, start in ASSETS:
            params = {
                "start": start, "end": END_EXCLUSIVE, "interval": "1d",
                "auto_adjust": False, "back_adjust": False, "repair": False,
                "actions": True, "keepna": True, "rounding": False,
                "timeout": 30, "raise_errors": True,
            }
            entry: dict[str, Any] = {
                "provider": "Yahoo Finance via yfinance", "symbol": symbol,
                "proposed_asset_id": asset_id, "parameters": params,
                "source_page": f"https://finance.yahoo.com/quote/{symbol}/history/",
                "started_at_utc": utc_now(),
            }
            manifest["requests"].append(entry)
            write_json(manifest_path, manifest)
            print(f"{symbol}: {start} bis 2025-12-31 ...", flush=True)
            ticker = yf.Ticker(symbol)
            history = ticker.history(**params)
            snapshot, report = history_snapshot(history, start, END_EXCLUSIVE)
            snapshot.to_csv(root / "yahoo" / f"{symbol}.csv", index=False,
                            encoding="utf-8", lineterminator="\n", float_format="%.17g", na_rep="")
            
            try:
                raw_meta = ticker.get_history_metadata()
                fields = ("symbol", "currency", "exchangeName", "fullExchangeName", "instrumentType",
                          "firstTradeDate", "exchangeTimezoneName", "longName", "shortName")
                selected = {key: raw_meta[key] for key in fields if key in raw_meta}
            except Exception as exc:
                selected = {"metadata_status": "UNAVAILABLE", "error": str(exc)}
            write_json(root / "yahoo" / f"{symbol}_metadata.json", selected)
            if selected.get("currency") != "USD":
                manifest["warnings"].append(f"{symbol}: USD-Notierung in Metadaten noch zu pruefen.")
            entry.update({"finished_at_utc": utc_now(), "coverage": report,
                          "currency_reported": selected.get("currency")})
            write_json(manifest_path, manifest)
            time.sleep(2)

        entry = {"provider": "FRED", "series_id": "DGS3MO", "url": FRED_URL,
                 "started_at_utc": utc_now()}
        manifest["requests"].append(entry)
        write_json(manifest_path, manifest)
        print("FRED DGS3MO: 2002-01-01 bis 2025-12-31 ...", flush=True)
        request = Request(FRED_URL, headers={"User-Agent": "MaturarbeitResearchAcquisition/1.1"})
        with urlopen(request, timeout=45) as response:
            payload = response.read()
            entry["response_url"] = response.geturl()
            entry["content_type"] = response.headers.get("Content-Type")
        (root / "fred" / "DGS3MO.csv").write_bytes(payload)
        entry["coverage"] = inspect_fred(payload)
        entry["finished_at_utc"] = utc_now()
        manifest["status"] = "ACQUIRED_PENDING_DATA_REVIEW"
    except KeyboardInterrupt:
        manifest["status"] = "FAILED_PARTIAL_SNAPSHOT"
        manifest["error"] = "Manuell unterbrochen; erhaltene Dateien bleiben gespeichert."
    except Exception as exc:
        manifest["status"] = "FAILED_PARTIAL_SNAPSHOT"
        manifest["error"] = {"type": type(exc).__name__, "message": str(exc)}
    finally:
        manifest["finished_at_utc"] = utc_now()
        manifest["files"] = file_records(root, manifest_path)
        write_json(manifest_path, manifest)

    print(f"Status: {manifest['status']}", flush=True)
    print(f"Manifest: {manifest_path}", flush=True)
    if manifest["status"] != "ACQUIRED_PENDING_DATA_REVIEW":
        print(f"STOPP: {manifest.get('error')}", file=sys.stderr)
        print("Teildownload nicht loeschen und nicht endlos neu starten.", file=sys.stderr)
        return 1
    print("Download abgeschlossen. Daten sind noch nicht zur Untersuchung freigegeben.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
