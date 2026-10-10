"""Focused physical-copy, input-path and freeze-integrity checks; no backtests."""
import json
import os
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

from scripts.study_v1 import verify_freeze as freeze

ROOT = Path(__file__).resolve().parents[2]


class FreezeTests(unittest.TestCase):
    def setUp(self):
        temp_root = (ROOT / ".venv/study_v1_freeze_check/test-temp").resolve()
        self.assertTrue(temp_root.is_relative_to(ROOT))
        temp_root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temp_root)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.archive = self.root / "data/study_v1/archive/study-freeze-v1"
        self.config_dir = self.root / "configs/study_v1"
        self.config_dir.mkdir(parents=True)
        for name in freeze.CONFIG_NAMES:
            shutil.copyfile(ROOT / "configs/study_v1" / f"{name}.json", self.config_dir / f"{name}.json")

    def change_config(self, name, edit):
        path = self.config_dir / f"{name}.json"
        raw = json.loads(path.read_text())
        edit(raw)
        path.write_text(json.dumps(raw), encoding="utf-8")
        return path

    def file(self, name="source.txt", content=b"original"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def test_physical_copy_is_independent_and_byte_equal(self):
        source = self.file()
        destination = self.root / "copy/target.txt"
        freeze.copy_verified_file(source, destination, freeze.fingerprint(source))
        self.assertEqual(source.read_bytes(), destination.read_bytes())
        self.assertFalse(source.samefile(destination))
        self.assertEqual(destination.stat().st_nlink, 1)
        destination.write_bytes(b"new data")
        self.assertEqual(source.read_bytes(), b"original")

    def test_existing_destination_never_overwritten(self):
        source, destination = self.file(), self.file("target.txt", b"preserved")
        with self.assertRaises(FileExistsError):
            freeze.copy_verified_file(source, destination, freeze.fingerprint(source))
        self.assertEqual(destination.read_bytes(), b"preserved")

    def test_changed_source_fails_before_copy(self):
        source = self.file()
        original = freeze.fingerprint(source)
        source.write_bytes(b"tampered")
        destination = self.root / "copy.txt"
        with self.assertRaisesRegex(freeze.FreezeError, "Source hash/size differs"):
            freeze.copy_verified_file(source, destination, original)
        self.assertFalse(destination.exists())

    def test_valid_complete_record_inventory(self):
        path = self.file("archive/file.txt")
        freeze.verify_records(path.parent, [{"path": path.name, **freeze.fingerprint(path)}])

    def test_same_length_archive_tamper_detected(self):
        path = self.file("archive/file.txt")
        record = {"path": path.name, **freeze.fingerprint(path)}
        path.write_bytes(b"tampered")
        with self.assertRaisesRegex(freeze.FreezeError, "Hash/size mismatch"):
            freeze.verify_records(path.parent, [record])

    def test_wrong_record_size_detected(self):
        path = self.file("archive/file.txt")
        record = {"path": path.name, **freeze.fingerprint(path), "bytes": 1}
        with self.assertRaisesRegex(freeze.FreezeError, "Hash/size mismatch"):
            freeze.verify_records(path.parent, [record])

    def test_unlisted_extra_file_detected(self):
        path = self.file("archive/file.txt")
        self.file("archive/extra.txt")
        with self.assertRaisesRegex(freeze.FreezeError, "inventory differs"):
            freeze.verify_records(path.parent, [{"path": path.name, **freeze.fingerprint(path)}])

    def test_missing_file_and_duplicate_record_rejected(self):
        path = self.file("archive/file.txt")
        record = {"path": path.name, **freeze.fingerprint(path)}
        with self.assertRaisesRegex(freeze.FreezeError, "Duplicate archive"):
            freeze.verify_records(path.parent, [record, record])
        with self.assertRaisesRegex(freeze.FreezeError, "Missing file"):
            freeze.verify_records(path.parent, [{**record, "path": "missing.txt"}])

    def test_unsafe_archive_members_rejected(self):
        for value in ["../escape", "/absolute", "C:/absolute", "folder\\file", "./file", "folder//file", ""]:
            with self.subTest(value=value), self.assertRaises(freeze.FreezeError):
                freeze.safe_member(self.root, value)

    def test_hardlinked_source_rejected(self):
        source = self.file()
        expected = freeze.fingerprint(source)
        linked_stat = list(source.stat())
        linked_stat[3] = 2  # st_nlink: inject OS metadata; the sandbox forbids creating hardlinks.
        with patch.object(Path, "stat", return_value=os.stat_result(linked_stat)), self.assertRaisesRegex(freeze.FreezeError, "linked file forbidden"):
            freeze.copy_verified_file(source, self.root / "copy.txt", expected)
        self.assertFalse((self.root / "copy.txt").exists())

    def test_symlink_guard_rejects_linked_file(self):
        source = self.file()
        with patch.object(Path, "is_symlink", return_value=True), self.assertRaisesRegex(freeze.FreezeError, "linked file forbidden"):
            freeze.regular_copy_file(source)

    def test_all_five_original_configs_resolve_to_archive(self):
        for name in freeze.CONFIG_NAMES:
            config = freeze.validate_config_contract(self.config_dir / f"{name}.json", self.root, self.archive)
            self.assertTrue(config.market_path.is_relative_to(self.archive))
            self.assertEqual(config.periods_per_year, 12)
        from maturarbeit_engine.engine.config import load_config
        k1 = load_config(self.config_dir / "K1.json")
        self.assertEqual(len(k1.target_weights), 7)
        self.assertTrue(all(weight == 1 / 7 for _, weight in k1.target_weights))
        self.assertFalse(k1.buy_hold_enabled or k1.trend_enabled)
        z1 = load_config(self.config_dir / "Z1.json")
        self.assertEqual(z1.start.isoformat(), "2002-12-31")
        self.assertFalse(z1.country_weighting_enabled)

    def test_working_processed_reference_rejected(self):
        path = self.change_config("H1", lambda r: r["data"].update(market="../../data/study_v1/processed/main_market.csv"))
        with self.assertRaisesRegex(freeze.FreezeError, "must read frozen copy"):
            freeze.validate_config_contract(path, self.root, self.archive)

    def test_absolute_data_reference_rejected(self):
        path = self.change_config("H1", lambda r: r["data"].update(market=str(self.archive / "processed/main_market.csv")))
        with self.assertRaisesRegex(freeze.FreezeError, "must be relative"):
            freeze.validate_config_contract(path, self.root, self.archive)

    def test_parameter_or_strategy_drift_rejected(self):
        path = self.change_config("S1", lambda r: r["strategies"]["trend"].update(short_window=3))
        with self.assertRaisesRegex(freeze.FreezeError, "Author strategies/parameters"):
            freeze.validate_config_contract(path, self.root, self.archive)
        path = self.change_config("K1", lambda r: r["strategies"].update(buy_hold={"enabled": True, "asset": "WORLD_EQ"}))
        with self.assertRaisesRegex(freeze.FreezeError, "Author strategies/parameters"):
            freeze.validate_config_contract(path, self.root, self.archive)

    def test_external_manifest_hash_is_required_binding(self):
        path = self.file("archive/freeze_manifest.json", b"{}"); original = freeze.fingerprint(path)
        with self.assertRaisesRegex(freeze.FreezeError, "separate seal evidence"):
            freeze.verify_archive(path.parent, "0" * 64)
        self.assertEqual(freeze.fingerprint(path), original)


if __name__ == "__main__":
    unittest.main()
