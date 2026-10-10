"""Read-only Study-v1 freeze verification; no download, simulation or run export.

Use the separately recorded manifest hash, never a hash inferred from the archive.
Config copies in configuration-records retain their original repository path base.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
import math
from pathlib import Path, PurePosixPath
import sys

import pandas as pd

if __package__:
    from . import prepare_data as adapter
else:
    import prepare_data as adapter

APPROVED = "948865ea3302ced267c9828b9a459ba03cd1c62971c070a818fd4c356c629c28"
FREEZE_ID = "study-freeze-v1"
STATUS = "FREEZE_CANDIDATE_READY_FOR_GIT_SEAL"
CONFIG_NAMES = ("H1", "K1", "Z1", "S1", "S2")
COUNTRIES = {"USA": "US_EQ", "CAN": "CA_EQ", "JPN": "JP_EQ", "GBR": "GB_EQ", "DEU": "DE_EQ", "FRA": "FR_EQ", "ITA": "IT_EQ"}


class FreezeError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise FreezeError(message)


def fingerprint(path):
    return {"bytes": path.stat().st_size, "sha256": sha256(path.read_bytes()).hexdigest()}


def regular_copy_file(path):
    require(path.is_file() and not path.is_symlink() and path.stat().st_nlink == 1,
            f"Missing file or linked file forbidden: {path}")
    for parent in path.parents:
        require(not parent.is_symlink() and not parent.is_junction(), f"Linked directory forbidden: {parent}")


def safe_member(root, member):
    require(isinstance(member, str) and bool(member) and "\\" not in member and ":" not in member,
            f"Unsafe archive member: {member!r}")
    parts = PurePosixPath(member)
    require(not parts.is_absolute() and ".." not in parts.parts and parts.as_posix() == member,
            f"Unsafe archive member: {member!r}")
    path = root / member
    require(path.resolve().is_relative_to(root.resolve()), f"Archive path escapes root: {member}")
    return path


def verify_records(root, records, unlisted=()):
    root = root.resolve()
    seen = set()
    for item in records:
        member = item["path"]
        require(member not in seen, f"Duplicate archive member: {member}")
        seen.add(member)
        path = safe_member(root, member)
        regular_copy_file(path)
        require(fingerprint(path) == {k: item[k] for k in ["bytes", "sha256"]}, f"Hash/size mismatch: {path}")
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file() or p.is_symlink()}
    require(actual == seen | set(unlisted), f"Archive inventory differs: missing={sorted(seen - actual)}, extra={sorted(actual - seen - set(unlisted))}")
    for folder in root.rglob("*"):
        require(not folder.is_symlink() and not folder.is_junction(), f"Linked archive entry forbidden: {folder}")


def verify_approved(project):
    processed = project / "data/study_v1/processed"
    manifest_path = processed / "processed_manifest.json"
    require(adapter.digest(manifest_path) == APPROVED, "STOPP: approved Processed manifest hash differs")
    manifest = adapter.strict_json(manifest_path)
    require(len(manifest["raw_files"]) == 54 and len(manifest["outputs"]) == 11, "Approved inventory counts differ")
    roots = {"acquisition": project / "data/study_v1/raw" / adapter.SNAPSHOT_NAME,
             "imf": project / "data/study_v1/raw/imf"}
    raw_records = []
    for kind, root in roots.items():
        require(Path(manifest["raw_roots"][kind]).resolve() == root.resolve(), f"Unexpected approved raw root: {kind}")
        records = [r for r in manifest["raw_files"] if r["root"] == kind]
        verify_records(root, records)
        raw_records += [(root / r["path"], f"raw/{root.name}/{r['path']}", "raw", r) for r in records]
    verify_records(processed, manifest["outputs"], [manifest_path.name])
    for name, value in manifest["code_environment"]["preparation_files"].items():
        require(adapter.digest(project / "scripts/study_v1" / name) == value, f"Approved preparation file differs: {name}")
    return manifest, raw_records


def copy_verified_file(source, destination, expected):
    """Exclusive new physical copy. Existing destinations are never overwritten."""
    regular_copy_file(source)
    require(fingerprint(source) == expected, f"Source hash/size differs: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    content = source.read_bytes()
    require({"bytes": len(content), "sha256": sha256(content).hexdigest()} == expected, f"Source changed before copy: {source}")
    with destination.open("xb") as output:
        output.write(content)
    regular_copy_file(destination)
    require(not source.samefile(destination) and fingerprint(destination) == expected, f"Physical copy mismatch: {destination}")
    require(fingerprint(source) == expected, f"Source changed during copy: {source}")


def expected_strategies(name):
    trend = lambda window, asset="WORLD_EQ": {"enabled": True, "asset": asset, "short_window": window,
        "long_window": 12, "signal_lag": 1, "signal_source": "performance_value"}
    country = {"enabled": True, "country_assets": COUNTRIES, "indicator": "NGDPD", "unit": "USD_billions", "rebalance_frequency": "annual"}
    rebalance = lambda weights: {"enabled": True, "target_weights": weights, "rebalance_frequency": "annual"}
    if name == "H1":
        return {"buy_hold": {"enabled": True, "asset": "WORLD_EQ"}, "rebalance": rebalance({"WORLD_EQ": .6, "US_TREASURY_7_10": .4}),
                "trend": trend(3), "country_weighting": country}
    if name == "K1":
        return {"rebalance": rebalance({asset: 1 / 7 for asset in COUNTRIES.values()}), "country_weighting": country}
    if name == "Z1":
        return {"buy_hold": {"enabled": True, "asset": "US_EQ"}, "rebalance": rebalance({"US_EQ": .6, "US_TREASURY_7_10": .4}), "trend": trend(3, "US_EQ")}
    return {"trend": trend(2 if name == "S1" else 6)}


def validate_config_contract(path, project, archive):
    from maturarbeit_engine.engine.config import load_config
    name = path.stem
    require(name in CONFIG_NAMES, f"Unexpected study config: {name}")
    config = load_config(path)
    raw = adapter.strict_json(path)
    start = "2002-12-31" if name == "Z1" else "2009-12-31"
    require(raw["period"] == {"start": start, "end": "2025-12-31"}, f"Author period differs: {name}")
    require(config.schema_version == "1.0" and config.run_name == name and config.start_capital == 100000
            and config.base_currency == "USD" and config.period_frequency == "ME" and config.periods_per_year == 12,
            f"Author constants differ: {name}")
    require(raw["strategies"] == expected_strategies(name), f"Author strategies/parameters differ: {name}")
    prefix = "us" if name == "Z1" else "main"
    expected = {"market": f"{prefix}_market.csv", "assets": "assets.csv", "risk_free": f"rf_{prefix}.csv"}
    if name in {"H1", "K1"}:
        expected["macro"] = "macro_g7.csv"
    require(set(raw["data"]) == set(expected), f"Unexpected data references: {name}")
    paths = {"market": config.market_path, "assets": config.assets_path, "risk_free": config.risk_free_path, "macro": config.macro_path}
    for kind, filename in expected.items():
        literal = raw["data"][kind]["path"] if kind == "risk_free" else raw["data"][kind]
        require(not Path(literal).is_absolute() and ":" not in literal, f"Config data path must be relative: {name}, {kind}")
        require(paths[kind] == (archive / "processed" / filename).resolve(), f"Config must read frozen copy: {name}, {kind}")
    require(config.risk_free_series == adapter.RF_METHOD, f"Risk-free series differs: {name}")
    require(config.output_dir == (project / "outputs/runs").resolve(), f"Output must be outputs/runs: {name}")
    return config


def validate_configs(project, archive):
    from maturarbeit_engine.engine.context import prepare_context
    from maturarbeit_engine.data.macro import select_gdp_targets
    summaries = {}
    for name in CONFIG_NAMES:
        path = project / "configs/study_v1" / f"{name}.json"
        config = validate_config_contract(path, project, archive)
        context = prepare_context(config)  # Data alignment and SMA validity only; no strategy.run.
        expected = pd.date_range(config.start, config.end, freq="ME")
        count = 277 if name == "Z1" else 193
        require(context.performance.index.equals(expected) and len(expected) == count, f"Valuation calendar differs: {name}")
        require(context.risk_free is not None and len(context.risk_free) == count - 1
                and context.risk_free.index.equals(expected[1:]), f"Risk-free periods differ: {name}")
        require(context.annualization_available and context.annualization_status == "available", f"ME/12 mismatch: {name}")
        summary = {"config_sha256": config.config_sha256, "start": config.start.isoformat(), "end": config.end.isoformat(),
                   "valuations": count, "risk_free_periods": count - 1, "currency": "USD", "frequency": "ME", "periods_per_year": 12,
                   "strategies": list(config.strategies()), "input_files": list(context.input_files), "simulation_executed": False}
        if config.trend_enabled:
            quality = context.data_quality["trend"]
            require(quality["used_warm_up_observations"] == 11 and quality["valid_start_signal"] is True,
                    f"SMA history/start validity differs: {name}")
            require(context.trend_signals is not None and len(context.trend_signals) == count and not context.trend_signals.isna().any().any(),
                    f"SMA validation incomplete: {name}")
            summary["trend_validation"] = quality
        if config.country_weighting_enabled:
            require(context.macro is not None and len(context.macro) == 4087, f"Macro versions differ: {name}")
            periods = {}
            for year in range(2009, 2025):
                decision = pd.Timestamp(f"{year}-12-31")
                weights, proof = select_gdp_targets(context.macro, config.country_params(), decision, "initial" if year == 2009 else "annual_rebalance")
                require(len(weights) == 7 and all(w > 0 for w in weights) and math.isclose(math.fsum(weights), 1, abs_tol=1e-12), f"Invalid G7 control: {name}, {year}")
                periods[str(year)] = proof["selected_period"]
                if year == 2022:
                    require(proof["selected_period"] == "2020", f"2022 reference year differs: {name}")
                    british = next(r for r in proof["countries"] if r["country"] == "GBR")
                    require(british["value"] == 2758.87 and british["available_from"] == "2022-10-12", f"2022 vintage differs: {name}")
            summary["g7_reference_years"] = periods
        summaries[name] = summary
    return {"status": "passed", "validation_kind": "static inputs, context/SMA validity and GDP controls only",
            "simulation_executed": False, "run_exported": False, "configs": summaries}


def verify_archive(archive, expected_manifest_sha256):
    archive = archive.resolve()
    path = archive / "freeze_manifest.json"
    regular_copy_file(path)
    require(adapter.digest(path) == expected_manifest_sha256, "Freeze manifest hash differs from separate seal evidence")
    manifest = adapter.strict_json(path)
    require(manifest["freeze_id"] == FREEZE_ID and manifest["status"] == STATUS and manifest["git_sealed"] is False
            and manifest["strategy_runs_executed"] is False, "Unexpected freeze state")
    require(manifest["approved_processed_manifest_sha256"] == APPROVED, "Approved manifest binding differs")
    require(manifest["engine"]["version"] == "1.0.0" and manifest["engine"]["tag"] == "engine-v1.0"
            and manifest["engine"]["commit"] == adapter.ENGINE_COMMIT, "Engine binding differs")
    verify_records(archive, manifest["files"], ["freeze_manifest.json"])
    processed = archive / "processed/processed_manifest.json"
    require(adapter.digest(processed) == APPROVED, "Frozen processed manifest differs")
    approved = adapter.strict_json(processed)
    verify_records(archive / "processed", approved["outputs"], [processed.name])
    require(len([r for r in manifest["files"] if r["category"] == "raw"]) == 54, "Archive must contain 54 raw files")
    configs = manifest["configurations"]
    require(set(configs) == set(CONFIG_NAMES), "Five configuration records required")
    for name, info in configs.items():
        require(adapter.digest(safe_member(archive, info["archive_path"])) == info["sha256"], f"Archived config differs: {name}")
    return manifest


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--manifest-sha256", required=True, help="Expected hash from the separate Git seal evidence")
    args = parser.parse_args(argv)
    project = Path(__file__).resolve().parents[2]
    try:
        archive = args.archive.resolve()
        require(archive == project / "data/study_v1/archive" / FREEZE_ID, "Unexpected Study-v1 archive path")
        manifest = verify_archive(archive, args.manifest_sha256)
        verify_approved(project)
        environment = adapter.code_environment(project / "scripts/study_v1/weo_release_register.csv")
        require(environment["engine_python_sha256"] == manifest["engine"]["python_sha256"], "Installed Engine hash differs")
        for name, info in manifest["configurations"].items():
            require(adapter.digest(project / info["repository_path"]) == info["sha256"], f"Repository config changed: {name}")
        validation = validate_configs(project, archive)
    except (ValueError, OSError, KeyError) as exc:
        print(f"STOPP: {exc}", file=sys.stderr)
        return 1
    print(json.dumps({"status": STATUS, "verification": validation["status"], "archive_files": len(manifest["files"]),
                      "manifest_sha256": args.manifest_sha256, "strategy_runs_executed": False}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
