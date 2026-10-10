"""Offline Study-v1 normalization and input checks; never execute a strategy.

Dates, mappings and conversion rules are author instructions, not adapter defaults
for other studies. Output directories must be new. No download library is used.
"""
from __future__ import annotations

import argparse
import csv
from datetime import date, datetime
from hashlib import sha256
from importlib import metadata
import io
import json
import math
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import tempfile

import numpy as np
import pandas as pd

SCRIPT_VERSION = "0.1.0"
ENGINE_COMMIT = "4a98f3a1039c6ebf4f1bfa1202a1af2e8064b023"
SNAPSHOT_NAME = "download_20261008T014620197765Z"
STATUS = "NORMALIZED_PENDING_AUTHOR_APPROVAL"
RF_METHOD = "DGS3MO_LAGGED_ACT365_APPROX"
ASSETS = {
    "VT": ("WORLD_EQ", "GLOBAL"), "IEF": ("US_TREASURY_7_10", "USA"),
    "VTI": ("US_EQ", "USA"), "EWC": ("CA_EQ", "CAN"),
    "EWJ": ("JP_EQ", "JPN"), "EWU": ("GB_EQ", "GBR"),
    "EWG": ("DE_EQ", "DEU"), "EWQ": ("FR_EQ", "FRA"),
    "EWI": ("IT_EQ", "ITA"),
}
COUNTRY_ASSETS = {country: asset for symbol, (asset, country) in ASSETS.items()
                  if symbol not in {"VT", "IEF"}}
EDITIONS = tuple(["2009-10", "2010-10", "2011-09"]
                 + [f"{year}-10" for year in range(2012, 2025)])
STUDIES = {
    "main": {"start": "2009-12-31", "end": "2025-12-31", "count": 193,
             "symbols": tuple(ASSETS), "history_start": "2009-01-01"},
    "us": {"start": "2002-12-31", "end": "2025-12-31", "count": 277,
           "symbols": ("VTI", "IEF"), "history_start": "2002-01-01"},
}


class PreparationError(ValueError):
    """A concrete input/contract problem; do not invent a replacement."""


def fail(message):
    raise PreparationError(message)


def digest(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def strict_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                fail(f"Duplicate JSON key {key}: {path}")
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding="utf-8-sig"), object_pairs_hook=unique,
                      parse_constant=lambda value: fail(f"Nonfinite JSON {value}: {path}"))


def iso(value, description):
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
        fail(f"Invalid ISO date in {description}: {value!r}")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise PreparationError(f"Invalid date in {description}: {value!r}") from exc


def number(value, description, positive=False, grouped=False):
    if grouped:
        if not re.fullmatch(r"(?:[0-9]+|[0-9]{1,3}(?:,[0-9]{3})+)(?:\.[0-9]+)?", value):
            fail(f"Invalid IMF number in {description}: {value!r}")
        value = value.replace(",", "")
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise PreparationError(f"Missing/invalid number in {description}: {value!r}") from exc
    if not math.isfinite(result) or (positive and result <= 0):
        fail(f"Nonfinite/nonpositive number in {description}: {value!r}")
    return result


def read_csv(path):
    content = Path(path).read_bytes()
    if b"\x00" in content:
        fail(f"NUL byte in UTF-8 CSV: {path}")
    reader = csv.reader(io.StringIO(content.decode("utf-8-sig")), strict=True)
    try:
        header = next(reader)
        if not header or len(set(header)) != len(header) or any(not h.strip() for h in header):
            fail(f"Invalid CSV header: {path}")
        rows = []
        for row in reader:
            if len(row) != len(header):
                fail(f"CSV width mismatch: {path}, line {reader.line_num}")
            rows.append(dict(zip(header, row)))
    except (StopIteration, csv.Error) as exc:
        raise PreparationError(f"Invalid CSV: {path}") from exc
    if not rows:
        fail(f"Empty CSV: {path}")
    return pd.DataFrame(rows, columns=header)


def raw_inventory(raw_dir, imf_dir):
    records = []
    for kind, folder in [("acquisition", raw_dir), ("imf", imf_dir)]:
        if not folder.is_dir():
            fail(f"Explicit raw directory missing; no fallback: {folder}")
        for path in sorted(folder.rglob("*")):
            if path.is_file():
                if path.is_symlink():
                    fail(f"Raw file must not be a symlink: {path}")
                records.append({"root": kind, "path": path.relative_to(folder).as_posix(),
                                "bytes": path.stat().st_size, "sha256": digest(path)})
    return records


def verify_acquisition(raw_dir):
    if raw_dir.name != SNAPSHOT_NAME:
        fail(f"Only the author-selected snapshot {SNAPSHOT_NAME} is allowed: {raw_dir}")
    manifest = strict_json(raw_dir / "acquisition_manifest.json")
    if manifest.get("status") != "ACQUIRED_PENDING_DATA_REVIEW" or manifest.get("backtest_executed") is not False:
        fail("Acquisition manifest is incomplete or not a raw-only acquisition.")
    found = set()
    for item in manifest["files"]:
        path = (raw_dir / item["path"]).resolve()
        if not path.is_relative_to(raw_dir) or item["path"] in found:
            fail("Unsafe/duplicate acquisition manifest path.")
        found.add(item["path"])
        if digest(path) != item["sha256"] or path.stat().st_size != item["bytes"]:
            fail(f"Acquisition SHA/size mismatch: {item['path']}")
    actual = {p.relative_to(raw_dir).as_posix() for p in raw_dir.rglob("*") if p.is_file()}
    if actual != found | {"acquisition_manifest.json"}:
        fail("Acquisition manifest/file inventory differs.")
    requests = {}
    for request in manifest["requests"]:
        key = request.get("symbol", request.get("series_id"))
        if key in requests:
            fail(f"Duplicate acquisition request: {key}")
        requests[key] = request
    if set(requests) != set(ASSETS) | {"DGS3MO"}:
        fail("Acquisition must identify exactly nine ETFs and DGS3MO.")
    for symbol, (asset, _) in ASSETS.items():
        request = requests[symbol]
        params = request["parameters"]
        expected_start = "2002-01-01" if symbol in {"IEF", "VTI"} else "2009-01-01"
        if (request.get("proposed_asset_id") != asset or params.get("start") != expected_start
                or params.get("end") != "2026-01-01" or params.get("interval") != "1d"
                or any(params.get(k) is not False for k in ["auto_adjust", "back_adjust", "repair"])
                or params.get("keepna") is not True or params.get("actions") is not True):
            fail(f"Unexpected acquisition/adjustment settings: {symbol}")
    fred = requests["DGS3MO"]
    if fred.get("provider") != "FRED" or "id=DGS3MO" not in fred.get("url", ""):
        fail("FRED request does not identify DGS3MO.")
    return requests


def monthly_observations(frame, symbol, start, end):
    """Select the last *observed* row, without skipping invalid Adj Close cells."""
    required = {"date", "source_timestamp", "Close", "Adj Close"}
    if not required <= set(frame.columns):
        fail(f"Missing Yahoo fields for {symbol}: {sorted(required - set(frame.columns))}")
    dates = [iso(v, f"{symbol} date") for v in frame.date]
    if any(a >= b for a, b in zip(dates, dates[1:])):
        fail(f"Duplicate/unordered Yahoo observations: {symbol}")
    values = [number(v, f"{symbol} {d} Adj Close", positive=True) for d, v in zip(dates, frame["Adj Close"])]
    for d, stamp in zip(dates, frame.source_timestamp):
        try:
            ts = pd.Timestamp(stamp)
            if ts.tzinfo is None or ts.tz_convert("America/New_York").date() != d:
                fail(f"Source timestamp/date disagreement: {symbol}, {d}, {stamp}")
        except (ValueError, TypeError) as exc:
            raise PreparationError(f"Invalid source timestamp: {symbol}, {stamp}") from exc
    for column in ["Open", "High", "Low", "Close", "Volume", "Dividends", "Stock Splits", "Capital Gains"]:
        if column in frame:
            for d, value in zip(dates, frame[column]):
                number(value, f"{symbol} {d} {column}", positive=column in {"Open", "High", "Low", "Close"})
    selected = {}
    for index, (d, value) in enumerate(zip(dates, values)):
        month = pd.Period(d, freq="M")
        if pd.Period(start, freq="M") <= month <= pd.Period(end, freq="M"):
            selected[month] = {"date": month.end_time.date().isoformat(),
                               "source_trade_date": d.isoformat(), "source_timestamp": frame.source_timestamp.iloc[index],
                               "source_row": index + 2, "performance_value": value,
                               "raw_adj_close": frame["Adj Close"].iloc[index]}
    expected = pd.period_range(start, end, freq="M")
    missing = [str(p) for p in expected if p not in selected]
    if missing:
        fail(f"Missing months for {symbol}: {missing}; period not shortened.")
    return pd.DataFrame([selected[p] for p in expected])


def shared_trade_dates(monthly, symbols, start, end):
    result = {}
    for label in pd.date_range(start, end, freq="ME").strftime("%Y-%m-%d"):
        observations = {}
        for symbol in symbols:
            rows = monthly[symbol].loc[monthly[symbol].date == label]
            if len(rows) != 1:
                fail(f"Missing/duplicate month-end: {symbol}, {label}")
            observations[symbol] = rows.iloc[0].source_trade_date
        if len(set(observations.values())) != 1:
            fail(f"Different last observed trading days for month {label}: {observations}; no replacement selected.")
        result[label] = next(iter(observations.values()))
    return result


def read_fred(path):
    frame = read_csv(path)
    if list(frame.columns) not in [["observation_date", "DGS3MO"], ["DATE", "DGS3MO"], ["date", "DGS3MO"]]:
        fail("Unexpected FRED columns; expected dates and DGS3MO.")
    dates = [iso(v, "FRED") for v in frame.iloc[:, 0]]
    if any(a >= b for a, b in zip(dates, dates[1:])):
        fail("FRED dates are duplicate or unordered.")
    observations, missing = [], []
    for index, (d, raw) in enumerate(zip(dates, frame.DGS3MO)):
        if raw in {"", "."}:
            missing.append(d.isoformat())
        else:
            observations.append({"quote_date": d.isoformat(), "annual_rate_percent": number(raw, f"DGS3MO {d}"),
                                 "raw_quote": raw, "source_row": index + 2})
    if not observations:
        fail("No valid FRED quotes.")
    return observations, {"daily_rows": len(frame), "valid_daily_quotes": len(observations),
                          "missing_daily_quotes": len(missing), "missing_quote_dates": missing,
                          "first_date": dates[0].isoformat(), "last_date": dates[-1].isoformat()}


def risk_free_periods(quotes, trade_dates, study):
    rows, provenance = [], []
    labels = list(trade_dates)
    for start, end in zip(labels, labels[1:]):
        trade = iso(trade_dates[start], "source trade day")
        eligible = [q for q in quotes if iso(q["quote_date"], "FRED quote") < trade]
        if not eligible:
            fail(f"No strictly earlier DGS3MO quote for {study}: {start}, source trade {trade}")
        quote = max(eligible, key=lambda q: q["quote_date"])
        age = (trade - iso(quote["quote_date"], "FRED quote")).days
        if age > 7:
            fail(f"DGS3MO quote older than seven days: {study}, {start}, {quote['quote_date']}, age {age}")
        days = (iso(end, "period end") - iso(start, "period start")).days
        result = number(quote["annual_rate_percent"], "annual FRED rate") / 100 * (days / 365)
        if not math.isfinite(result):
            fail(f"RF conversion nonfinite: {study}, {start}")
        row = {"period_start": start, "period_end": end, "series_id": RF_METHOD, "period_return": result}
        rows.append(row)
        provenance.append({"study": study, **row, "source_trade_date": trade.isoformat(), **quote,
                           "quote_age_calendar_days": age, "calendar_days": days, "method": RF_METHOD})
    return pd.DataFrame(rows), provenance


def read_register(path):
    frame = read_csv(path)
    required = {"edition", "publication_date", "available_from", "publication_evidence", "download_url", "availability_note"}
    if set(frame.columns) != required or frame.edition.tolist() != list(EDITIONS):
        fail("Release register must identify the sixteen author-confirmed WEO editions, in order.")
    for row in frame.to_dict("records"):
        if iso(row["available_from"], "register availability") <= iso(row["publication_date"], "register publication"):
            fail(f"Availability does not follow author publication date: {row['edition']}")
        if any(not row[k].strip() for k in required):
            fail(f"Missing register evidence: {row['edition']}")
    return frame.to_dict("records")


def decode_weo(content):
    if content.startswith((b"\xff\xfe", b"\xfe\xff")):
        encoding = "utf-16"
    elif content.startswith(b"\xef\xbb\xbf"):
        encoding = "utf-8-sig"
    elif b"\x00" in content[:256]:
        # The ASCII TSV header identifies LE unambiguously, including no-BOM files.
        if not content.startswith("WEO Country Code\t".encode("utf-16-le")):
            fail("Unrecognized NUL-containing WEO encoding; no byte removal.")
        encoding = "utf-16-le"
    else:
        encoding = "latin-1"
    try:
        text = content.decode(encoding)
    except UnicodeError as exc:
        raise PreparationError(f"Invalid WEO {encoding} encoding") from exc
    if "\x00" in text:
        fail("Decoded WEO text still contains NUL; no repair.")
    return text, encoding


def read_weo(path, release):
    text, encoding = decode_weo(Path(path).read_bytes())
    reader = csv.reader(io.StringIO(text), delimiter="\t", strict=True)
    header = next(reader)
    required = {"WEO Country Code", "ISO", "WEO Subject Code", "Country", "Subject Descriptor", "Units", "Scale", "Estimates Start After"}
    if not required <= set(header) or len(header) != len(set(header)):
        fail(f"Missing/duplicate WEO headers: {path}")
    years = [int(h) for h in header if re.fullmatch(r"[0-9]{4}", h)]
    if not years or years != list(range(min(years), max(years) + 1)):
        fail(f"WEO year columns not a complete increasing sequence: {path}")
    candidates, footer_count, blank_count, data_count = {}, 0, 0, 0
    expected_footer = f"International Monetary Fund, World Economic Outlook Database, {'September' if release['edition'].endswith('-09') else 'October'} {release['edition'][:4]}"
    for row in reader:
        if not row or all(not cell.strip() for cell in row):
            blank_count += 1
            continue
        if row[0].startswith("International Monetary Fund, World Economic Outlook Database,"):
            if row[0].strip() != expected_footer or any(cell.strip() for cell in row[1:]):
                fail(f"WEO footer contradicts release identity: {path}")
            footer_count += 1
            continue
        if row[0].startswith("Note: Non-zero values") and all(not cell.strip() for cell in row[1:]):
            footer_count += 1
            continue
        if len(row) != len(header):
            fail(f"WEO width mismatch: {path}, line {reader.line_num}")
        record = dict(zip(header, row)); data_count += 1
        if record["ISO"] not in COUNTRY_ASSETS or record["WEO Subject Code"] != "NGDPD":
            continue
        country = record["ISO"]
        if country in candidates:
            fail(f"Duplicate G7 NGDPD row: {release['edition']}, {country}")
        candidates[country] = (record, reader.line_num)
    if set(candidates) != set(COUNTRY_ASSETS):
        fail(f"Missing G7 NGDPD rows in {release['edition']}: {sorted(set(COUNTRY_ASSETS) - candidates.keys())}")
    rows, provenance, cutoffs = [], [], {}
    for country in sorted(candidates):
        record, line = candidates[country]
        if (record["Units"] != "U.S. dollars" or record["Scale"] != "Billions"
                or record["Subject Descriptor"] != "Gross domestic product, current prices"):
            fail(f"NGDPD unit/descriptor mismatch: {release['edition']}, {country}")
        cutoff = record["Estimates Start After"].strip()
        if not re.fullmatch(r"[0-9]{4}", cutoff) or int(cutoff) not in years:
            fail(f"Invalid Estimates Start After: {release['edition']}, {country}, {cutoff!r}")
        cutoffs[country] = int(cutoff)
        for year in years:
            if year > int(cutoff):
                continue
            value = number(record[str(year)].strip(), f"{release['edition']} {country} {year}", positive=True, grouped=True)
            row = {"period": str(year), "country": country, "indicator": "NGDPD", "value": value,
                   "unit": "USD_billions", "available_from": release["available_from"]}
            rows.append(row)
            provenance.append({**row, "edition": release["edition"], "publication_date": release["publication_date"],
                               "estimates_start_after": int(cutoff), "raw_value": record[str(year)],
                               "source_row": line, "source_column": str(year), "encoding": encoding,
                               "publication_evidence": release["publication_evidence"],
                               "download_url": release["download_url"]})
    return rows, provenance, {"edition": release["edition"], "encoding": encoding, "data_rows": data_count,
                              "footer_rows": footer_count, "blank_rows": blank_count,
                              "historical_cutoffs": cutoffs, "retained_g7_versions": len(rows),
                              "excluded_estimate_cells": sum(sum(y > c for y in years) for c in cutoffs.values())}


def g7_decisions(versions, decision_dates):
    """Independent as-of control, not a portfolio/strategy calculation."""
    rows = []
    for index, decision in enumerate(decision_dates):
        iso(decision, "G7 decision")
        eligible = [r for r in versions if r["available_from"] <= decision]
        common = set.intersection(*[{r["period"] for r in eligible if r["country"] == c} for c in sorted(COUNTRY_ASSETS)])
        if not common:
            fail(f"No common historical G7 year available at {decision}")
        period = max(common)
        selected = [max((r for r in eligible if r["country"] == c and r["period"] == period),
                        key=lambda r: r["available_from"]) for c in sorted(COUNTRY_ASSETS)]
        total = math.fsum(r["value"] for r in selected)
        weights = [r["value"] / total for r in selected]
        if any(not math.isfinite(w) or w <= 0 for w in weights) or not math.isclose(math.fsum(weights), 1, abs_tol=1e-12):
            fail(f"Invalid G7 weight control at {decision}")
        for record, weight in zip(selected, weights):
            rows.append({"decision_date": decision, "decision_type": "initial" if index == 0 else "annual_rebalance",
                         "selected_period": period, "country": record["country"],
                         "asset_id": COUNTRY_ASSETS[record["country"]], "value": record["value"],
                         "unit": record["unit"], "edition": record["edition"],
                         "available_from": record["available_from"], "target_weight": weight,
                         "g7_gdp_sum": total, "source_row": record["source_row"],
                         "source_file": record["source_file"], "source_sha256": record["source_sha256"]})
    return pd.DataFrame(rows)


def engine_validate(output):
    """Only public data validators/aligners; no simulation, SMA or strategy run."""
    import maturarbeit_engine
    from maturarbeit_engine.data.normalize import read_csv_snapshot, align_performance, align_risk_free
    from maturarbeit_engine.data.validate import validate_assets, validate_market, validate_risk_free, validate_macro
    from maturarbeit_engine.data.macro import select_gdp_targets
    from maturarbeit_engine.engine.context import check_period_logic
    if maturarbeit_engine.__version__ != "1.0.0":
        fail("Input validation requires the frozen Engine 1.0.0.")
    load = lambda name: read_csv_snapshot(output / name, name)[0]
    assets = validate_assets(load("assets.csv"))
    summaries = {}
    for name, settings in STUDIES.items():
        required = sorted(ASSETS[s][0] for s in settings["symbols"])
        market = validate_market(load(f"{name}_market.csv"), assets, required, "USD")
        performance, quality = align_performance(market, required, settings["start"], settings["end"])
        expected = pd.date_range(settings["start"], settings["end"], freq="ME")
        if len(performance) != settings["count"] or not performance.index.equals(expected):
            fail(f"Engine calendar/count mismatch: {name}")
        if check_period_logic(performance.index, "ME", 12) != (True, "available"):
            fail(f"Engine ME/12 contract mismatch: {name}")
        rf, _ = align_risk_free(validate_risk_free(load(f"rf_{name}.csv")), RF_METHOD, performance.index)
        if len(rf) != settings["count"] - 1:
            fail(f"Engine RF period count mismatch: {name}")
        basis = market.loc[(market.asset_id == ("WORLD_EQ" if name == "main" else "US_EQ"))
                           & (market.date <= pd.Timestamp(settings["start"]))]
        if len(basis) != 12 or len(basis.loc[basis.date < pd.Timestamp(settings["start"])]) != 11:
            fail(f"Twelve-month signal basis including initial valuation missing: {name}")
        summaries[name] = {"market_rows": len(market), "valuations": len(performance), "return_periods": len(rf),
                           "start": settings["start"], "end": settings["end"], "currency": "USD", "frequency": "ME",
                           "periods_per_year": 12, "signal_months_through_initial_valuation": 12,
                           "signal_months_strictly_before_initial_valuation": 11,
                           "removed_non_common_dates": {a: r["removed_non_common_dates"] for a, r in quality["series"].items()}}
    macro = validate_macro(load("macro_g7.csv")); checks = load("g7_decision_check.csv")
    params = {"country_assets": COUNTRY_ASSETS, "indicator": "NGDPD", "unit": "USD_billions"}
    for d, group in checks.groupby("decision_date", sort=True):
        weights, proof = select_gdp_targets(macro, params, pd.Timestamp(d), group.iloc[0].decision_type)
        if group.selected_period.unique().tolist() != [proof["selected_period"]]:
            fail(f"G7 control differs from frozen Engine at {d}")
        for row in group.itertuples():
            if not math.isclose(float(row.target_weight), float(weights[row.asset_id]), rel_tol=0, abs_tol=1e-12):
                fail(f"G7 weight differs from frozen Engine: {d}, {row.country}")
    return {"engine_version": maturarbeit_engine.__version__, "status": "passed", "studies": summaries,
            "macro_versions": len(macro), "g7_decisions": int(checks.decision_date.nunique()),
            "simulation_executed": False}


def verify_frozen_source(frozen, workspace, installed, relative):
    # Git's Windows checkout conversion changes CRLF only, not Python content.
    canonical = lambda content: content.replace(b"\r\n", b"\n")
    if canonical(workspace) != canonical(frozen) or canonical(installed) != canonical(frozen):
        fail(f"Frozen/source/installed Engine differs: {relative}")


def code_environment(register_path):
    import maturarbeit_engine
    root = Path(__file__).resolve().parents[2]
    result = subprocess.run(["git", "-c", f"safe.directory={root.as_posix()}", "rev-parse", "engine-v1.0^{commit}"],
                            cwd=root, capture_output=True, text=True, check=True)
    if result.stdout.strip() != ENGINE_COMMIT:
        fail("Engine tag does not point to the author-approved commit.")
    branch = subprocess.check_output(["git", "-c", f"safe.directory={root.as_posix()}", "branch", "--show-current"], cwd=root).decode().strip()
    if branch != "study-v1":
        fail(f"Expected study-v1 branch, found {branch}")
    installed = Path(maturarbeit_engine.__file__).parent
    sources = {p.relative_to(installed).as_posix(): digest(p) for p in sorted(installed.rglob("*.py"))}
    frozen_sources = {}
    for path in sorted((root / "src").rglob("*.py")):
        relative = path.relative_to(root / "src").as_posix()
        frozen = subprocess.check_output(["git", "-c", f"safe.directory={root.as_posix()}", "show", f"engine-v1.0:src/{relative}"], cwd=root)
        verify_frozen_source(frozen, path.read_bytes(), (installed / relative).read_bytes(), relative)
        frozen_sources[relative] = sha256(frozen).hexdigest()
    if set(sources) != set(frozen_sources):
        fail("Installed Engine Python file inventory differs from the frozen source.")
    files = {"prepare_data.py": digest(__file__), "weo_release_register.csv": digest(register_path)}
    return {"adapter_version": SCRIPT_VERSION, "preparation_files": files,
            "engine_version": maturarbeit_engine.__version__, "engine_tag": "engine-v1.0", "engine_commit": ENGINE_COMMIT,
            "engine_python_sha256": sources, "engine_git_blob_sha256": frozen_sources,
            "engine_comparison": "Exact Python bytes after Git CRLF-to-LF checkout normalization only; runtime hashes retain actual bytes.",
            "python": sys.version, "platform": platform.platform(),
            "packages": {p: metadata.version(p) for p in ["numpy", "pandas", "maturarbeit-engine", "python-dateutil", "tzdata"]}}


def write_frame(path, frame):
    if frame.empty or frame.isna().any().any():
        fail(f"Output has missing/empty required data: {path.name}")
    for column in frame.select_dtypes(include=np.number):
        if not np.isfinite(frame[column].to_numpy()).all():
            fail(f"Nonfinite output: {path.name}, {column}")
    frame.to_csv(path, index=False, encoding="utf-8", lineterminator="\n", float_format="%.17g")


def write_json(path, content):
    path.write_text(json.dumps(content, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False) + "\n",
                    encoding="utf-8", newline="\n")


def prepare(raw_dir, imf_dir, output_dir, register_path=None):
    raw_dir, imf_dir, output_dir = [Path(p).resolve() for p in [raw_dir, imf_dir, output_dir]]
    if output_dir.exists():
        fail(f"Output already exists; choose a new candidate directory, no overwrite: {output_dir}")
    if any(output_dir.is_relative_to(p) or p.is_relative_to(output_dir) for p in [raw_dir, imf_dir]):
        fail("Output must be separate from the immutable raw directories.")
    register_path = Path(register_path or Path(__file__).with_name("weo_release_register.csv")).resolve()
    before = raw_inventory(raw_dir, imf_dir)
    requests = verify_acquisition(raw_dir)
    environment = code_environment(register_path)
    releases = read_register(register_path)
    if {p.name for p in imf_dir.iterdir() if p.is_dir()} != set(EDITIONS):
        fail("IMF directory does not contain exactly the sixteen requested editions.")
    monthly, asset_rows, raw_market_report = {}, [], {}
    for symbol, (asset, country) in ASSETS.items():
        path = raw_dir / "yahoo" / f"{symbol}.csv"
        frame = read_csv(path); meta = strict_json(path.with_name(f"{symbol}_metadata.json"))
        if (meta.get("symbol") != symbol or meta.get("currency") != "USD" or meta.get("instrumentType") != "ETF"
                or meta.get("exchangeTimezoneName") != "America/New_York"
                or meta.get("exchangeName") not in {"PCX", "NGM", "NMS", "NYQ"}):
            fail(f"USD/US-listed ETF metadata mismatch: {symbol}")
        coverage = requests[symbol]["coverage"]
        if (coverage["rows"] != len(frame) or coverage["columns"] != list(frame.columns)
                or coverage["first_date"] != frame.date.iloc[0] or coverage["last_date"] != frame.date.iloc[-1]):
            fail(f"Yahoo coverage metadata differs from file: {symbol}")
        start = "2002-07-01" if symbol == "IEF" else "2002-01-01" if symbol == "VTI" else "2009-01-01"
        if frame.date.iloc[0] < start or frame.date.iloc[-1] > "2025-12-31":
            fail(f"Unexpected Yahoo raw interval: {symbol}")
        monthly[symbol] = monthly_observations(frame, symbol, start, "2025-12-31")
        asset_rows.append({"asset_id": asset, "name": meta.get("longName", meta.get("shortName", "")),
                           "asset_class": "ETF", "country": country, "currency": "USD",
                           "provider": "Yahoo Finance via yfinance", "provider_symbol": symbol})
        raw_market_report[symbol] = {"daily_rows": len(frame), "monthly_rows": len(monthly[symbol]),
                                    "first_source_date": frame.date.iloc[0], "last_source_date": frame.date.iloc[-1],
                                    "currency": "USD", "exchange": meta["exchangeName"],
                                    "required_numeric_missing": 0, "source_url": requests[symbol]["source_page"]}
    shared_trade_dates(monthly, tuple(ASSETS), "2009-01-31", "2025-12-31")
    quotes, fred_report = read_fred(raw_dir / "fred/DGS3MO.csv")
    market_outputs, observations, rf_outputs, rf_provenance = {}, [], {}, []
    for study, settings in STUDIES.items():
        parts = []
        for symbol in settings["symbols"]:
            source = monthly[symbol].loc[monthly[symbol].date >= settings["history_start"]].copy()
            asset = ASSETS[symbol][0]
            source_hash = digest(raw_dir / "yahoo" / f"{symbol}.csv")
            parts.append(source[["date", "performance_value"]].assign(asset_id=asset)[["date", "asset_id", "performance_value"]])
            for row in source.to_dict("records"):
                observations.append({"study": study, "asset_id": asset, "symbol": symbol, **row,
                                     "source_file": f"yahoo/{symbol}.csv", "source_sha256": source_hash,
                                     "role": "history_before_initial_valuation" if row["date"] < settings["start"] else "performance_valuation",
                                     "label_semantics": "calendar_month_end_label_not_exchange_observation"})
        market_outputs[study] = pd.concat(parts).sort_values(["date", "asset_id"], kind="stable")
        trade_dates = shared_trade_dates(monthly, settings["symbols"], settings["start"], settings["end"])
        rf_outputs[study], proof = risk_free_periods(quotes, trade_dates, study)
        source_hash = digest(raw_dir / "fred/DGS3MO.csv")
        rf_provenance += [{**r, "source_file": "fred/DGS3MO.csv", "source_sha256": source_hash,
                           "source_url": requests["DGS3MO"]["url"]} for r in proof]
    macro, macro_proof, weo_report = [], [], []
    for release in releases:
        folder = imf_dir / release["edition"]
        note = (folder / "download_note.txt").read_text(encoding="utf-8-sig")
        note_fields = dict(line.split(": ", 1) for line in note.splitlines() if ": " in line)
        expected_name = f"weo{'sep' if release['edition'].endswith('-09') else 'oct'}{release['edition'][:4]}all.xls"
        if (note_fields.get("Originaldateiname") != expected_name or note_fields.get("Downloadseite") != release["download_url"]
                or note_fields.get("Ausgabe") != f"WEO {'September' if release['edition'].endswith('-09') else 'October'} {release['edition'][:4]}"
                or note_fields.get("Downloadoption") != "Tab Delimited Values / By Countries"
                or {p.name for p in folder.iterdir()} != {expected_name, "download_note.txt"}):
            fail(f"Download note/files contradict WEO edition: {release['edition']}")
        datetime.fromisoformat(note_fields["Downloadzeitpunkt"])
        path = folder / expected_name
        rows, proof, report = read_weo(path, release)
        macro += rows
        source_hash = digest(path)
        note_hash = digest(folder / "download_note.txt")
        macro_proof += [{**r, "source_file": f"{release['edition']}/{path.name}", "source_sha256": source_hash,
                         "download_note_sha256": note_hash} for r in proof]
        weo_report.append(report)
    keys = [(r["period"], r["country"], r["available_from"]) for r in macro]
    if len(keys) != len(set(keys)):
        fail("Duplicate normalized macro version keys.")
    decisions = g7_decisions(macro_proof, [f"{year}-12-31" for year in range(2009, 2025)])
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=f".{output_dir.name}-candidate-", dir=output_dir.parent))
    frames = {"assets.csv": pd.DataFrame(asset_rows).sort_values("asset_id"),
              "main_market.csv": market_outputs["main"], "us_market.csv": market_outputs["us"],
              "rf_main.csv": rf_outputs["main"], "rf_us.csv": rf_outputs["us"],
              "macro_g7.csv": pd.DataFrame(macro).sort_values(["country", "period", "available_from"]),
              "observation_provenance.csv": pd.DataFrame(observations).sort_values(["study", "date", "asset_id"]),
              "risk_free_provenance.csv": pd.DataFrame(rf_provenance).sort_values(["study", "period_start"]),
              "macro_provenance.csv": pd.DataFrame(macro_proof).sort_values(["country", "period", "available_from"]),
              "g7_decision_check.csv": decisions}
    try:
        for name, frame in frames.items():
            write_frame(stage / name, frame)
        validation = engine_validate(stage)
        report = {"status": STATUS, "backtest_executed": False, "engine_validation": validation,
                  "markets": raw_market_report, "risk_free": {"method": RF_METHOD, **fred_report,
                  "max_selected_quote_age_days": max(r["quote_age_calendar_days"] for r in rf_provenance)},
                  "imf_editions": weo_report, "g7_reference_years": decisions.groupby("decision_date").selected_period.first().to_dict(),
                  "file_row_counts": {name: len(frame) for name, frame in frames.items()},
                  "raw_files_byte_identical": True, "monthly_trade_dates_agree": True,
                  "signal_history_semantics": "12 calendar months through initial December valuation; 11 strictly before it; no warm-up returns",
                  "limitations": ["USD quotation does not imply economic FX hedging.",
                  "Adj Close is today's archived provider-adjusted series, not an independently reconstructed total-return portfolio.",
                  "Monthly labels are not actual exchange observation dates; see observation provenance.",
                  "No external exchange calendar used; daily completeness beyond observed dates is not proved.",
                  "DGS3MO conversion is an author-confirmed simple ACT/365 approximation, not a measured bill holding return.",
                  "Publication dates are author-confirmed in the task; download notes establish edition identity, not the date of these exact bytes.",
                  "No WEO 2025 edition: the last nonterminal annual decision is 2024-12-31; no terminal trade/decision in 2025.",
                  "No scientific approval, final study freeze, final run configs, or strategy results."]}
        write_json(stage / "normalization_report.json", report)
        if raw_inventory(raw_dir, imf_dir) != before:
            fail("Raw input bytes/inventory changed during normalization; candidate not published.")
        if digest(__file__) != environment["preparation_files"]["prepare_data.py"] or digest(register_path) != environment["preparation_files"]["weo_release_register.csv"]:
            fail("Preparation script/register changed during normalization.")
        manifest = {"status": STATUS, "backtest_executed": False, "raw_roots": {"acquisition": str(raw_dir), "imf": str(imf_dir)},
                    "raw_files": before, "code_environment": environment,
                    "method_evidence": "documentation/ai-usage/prompts/2026-10-10-study-v1-data-adapter.md, author instructions",
                    "outputs": [{"path": p.name, "sha256": digest(p), "bytes": p.stat().st_size} for p in sorted(stage.iterdir())],
                    "manifest_self_hash": "not included; no circular hash", "reproducibility": "No timestamp, random run ID or output path in content; new candidate directory required."}
        write_json(stage / "processed_manifest.json", manifest)
        if output_dir.exists():
            fail(f"Output appeared during preparation; candidate preserved: {output_dir}")
        os.rename(stage, output_dir)
    except Exception as exc:
        raise PreparationError(f"Candidate not published; diagnostic files preserved at {stage}: {exc}") from exc
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw-dir", type=Path, required=True, help="Explicit author-selected ETF/FRED snapshot")
    parser.add_argument("--imf-dir", type=Path, required=True, help="Explicit directory containing sixteen WEO editions")
    parser.add_argument("--output-dir", type=Path, required=True, help="New local candidate directory; existing paths refused")
    args = parser.parse_args(argv)
    try:
        report = prepare(args.raw_dir, args.imf_dir, args.output_dir)
    except (ValueError, OSError, KeyError, csv.Error, UnicodeError, subprocess.SubprocessError) as exc:
        print(f"STOPP: {exc}", file=sys.stderr)
        return 1
    print(json.dumps({"status": report["status"], "output_dir": str(args.output_dir.resolve()),
                      "studies": report["engine_validation"]["studies"], "backtest_executed": False}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
