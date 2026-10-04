"""Publish complete runs atomically, preserving input and code fingerprints."""
from datetime import datetime, timezone
from hashlib import sha256
from importlib.metadata import version
from pathlib import Path
from tempfile import TemporaryDirectory
from uuid import uuid4
import json
import subprocess
import sys
import pandas as pd
from .. import __version__
from ..engine.result import validate_results
from ..analysis.metrics import validate_run_metrics


def file_sha256(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, content):
    Path(path).write_text(json.dumps(content, indent=2, sort_keys=True, ensure_ascii=False,
                                    allow_nan=False) + "\n", encoding="utf-8")


def code_provenance():
    source = Path(__file__).resolve().parents[1]
    root = source.parent
    hashes = {p.relative_to(source).as_posix(): file_sha256(p) for p in sorted(source.rglob("*.py"))}
    for name in ["pyproject.toml", "requirements.lock"]:
        if (root / name).is_file():
            hashes["../" + name] = file_sha256(root / name)
    git = {"commit": None, "dirty": None, "status": "unavailable"}
    if (root / ".git").exists():
        try:
            base = ["git", "-c", "safe.directory=" + root.as_posix(), "-C", str(root)]
            commit = subprocess.run(base + ["rev-parse", "HEAD"], capture_output=True, text=True,
                                    check=True, timeout=10).stdout.strip()
            dirty = subprocess.run(base + ["status", "--porcelain", "--untracked-files=normal"],
                                   capture_output=True, text=True, check=True, timeout=10).stdout
            git = {"commit": commit, "dirty": bool(dirty.strip()), "status": "available"}
        except (OSError, subprocess.SubprocessError):
            pass
    return {"git": git, "files": hashes,
            "sha256": sha256(json.dumps(hashes, sort_keys=True).encode("utf-8")).hexdigest()}


def export_run(context, result, summary, metric_status):
    # Detect edits after reading: every recorded hash must describe the consumed file.
    for info in context.input_files:
        if file_sha256(info["path"]) != info["sha256"]:
            raise ValueError(f"Input changed during run: {info['kind']}")
    results = validate_results(context, result, require_complete=True)
    validate_run_metrics(results, context, summary, metric_status)
    root = context.config.output_dir.resolve()
    root.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    run_id = context.config.run_name + "-" + uuid4().hex
    destination = root / run_id
    with TemporaryDirectory(prefix=".pending-", dir=root) as temporary:
        stage = Path(temporary).resolve()
        if not stage.is_relative_to(root):
            raise ValueError("Staging directory escaped output root.")
        pd.concat([r.portfolio_history for r in results], ignore_index=True).sort_values(
            ["strategy", "date"], kind="stable").to_csv(stage / "portfolio_history.csv", index=False,
                                       date_format="%Y-%m-%d", float_format="%.17g", na_rep="",
                                       lineterminator="\n", encoding="utf-8")
        summary.to_csv(stage / "summary.csv", index=False, float_format="%.17g", na_rep="",
                       lineterminator="\n", encoding="utf-8")
        quality = dict(context.data_quality)
        for r in results:
            if r.macro_decisions is not None:
                quality["macro"] = {**quality["macro"], "decisions": list(r.macro_decisions)}
        write_json(stage / "data_quality.json", quality)
        names = ["portfolio_history.csv", "summary.csv", "data_quality.json"]
        for attribute in ["weights_history", "trades", "signals"]:
            tables = [getattr(r, attribute) for r in results if getattr(r, attribute) is not None]
            if tables:
                name = attribute + ".csv"
                pd.concat(tables, ignore_index=True).sort_values(["strategy", "date", "asset_id"], kind="stable").to_csv(
                    stage / name, index=False, date_format="%Y-%m-%d", float_format="%.17g",
                    na_rep="", lineterminator="\n", encoding="utf-8")
                names.append(name)
        manifest = {
            "engine_version": __version__, "schema_version": context.config.schema_version,
            "run_id": run_id, "run_name": context.config.run_name,
            "timestamp_utc": now.isoformat(), "config": context.config.resolved(),
            "requested_period": context.data_quality["requested_period"],
            "effective_period": context.data_quality["effective_period"],
            "base_currency": context.config.base_currency,
            "periods_per_year": context.config.periods_per_year,
            "input_files": list(context.input_files), "code": code_provenance(),
            "python_version": sys.version, "packages": {p: version(p) for p in ["numpy", "pandas"]},
            "metric_status": metric_status,
            "executed_strategies": [r.strategy for r in results],
            "metric_status_by_strategy": ({results[0].strategy: metric_status} if len(results) == 1 else metric_status),
            "results": [{"path": name, "sha256": file_sha256(stage / name)}
                        for name in names],
        }
        write_json(stage / "run_manifest.json", manifest)
        # UUID directory names avoid collisions; never replace an existing successful run.
        if destination.exists():
            raise FileExistsError(destination)
        stage.rename(destination)
    return destination, manifest
