"""Focused offline adapter tests; no real strategy run and no engine changes."""
import csv
import io
import json
import math
from pathlib import Path
import socket
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd
from scripts.study_v1 import prepare_data as adapter

ROOT = Path(__file__).resolve().parents[2]


def yahoo_frame(dates, values=None):
    return pd.DataFrame({"date": dates,
                         "source_timestamp": [d + "T00:00:00-05:00" for d in dates],
                         "Close": [200.] * len(dates),
                         "Adj Close": values or [100.] * len(dates),
                         "Dividends": [5.] * len(dates), "Stock Splits": [2.] * len(dates)})


def weo_fixture(path, cutoff=2021, encoding="latin-1", missing=False, duplicate=False, unit="U.S. dollars"):
    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer, delimiter="\t", lineterminator="\n")
    header = ["WEO Country Code", "ISO", "WEO Subject Code", "Country", "Subject Descriptor", "Units", "Scale",
              "2020", "2021", "2022", "Estimates Start After"]
    writer.writerow(header)
    for i, country in enumerate(sorted(adapter.COUNTRY_ASSETS)):
        row = [str(i), country, "NGDPD", "Synthetic é", "Gross domestic product, current prices", unit, "Billions",
               "2,758.87" if country == "GBR" else "1,000.5", "n/a" if missing else "1,100", "9,999", cutoff]
        writer.writerow(row)
        if duplicate and country == "GBR":
            writer.writerow(row)
    writer.writerow([])
    writer.writerow(["International Monetary Fund, World Economic Outlook Database, October 2022"])
    path.write_bytes(buffer.getvalue().encode(encoding))


class AdapterTests(unittest.TestCase):
    def setUp(self):
        temp_root = (ROOT / ".venv/study_v1_adapter_check/test-temp").resolve()
        if not temp_root.is_relative_to(ROOT):
            raise AssertionError("Test temporary directory must stay inside the workspace")
        temp_root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temp_root)
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)
        def denied(*args, **kwargs):
            raise AssertionError("Network forbidden in adapter test")
        for target in ["socket.create_connection", "socket.getaddrinfo", "socket.socket.connect", "socket.socket.connect_ex", "urllib.request.urlopen"]:
            guard = patch(target, side_effect=denied)
            guard.start(); self.addCleanup(guard.stop)

    def release(self):
        return next(r for r in adapter.read_register(ROOT / "scripts/study_v1/weo_release_register.csv") if r["edition"] == "2022-10")

    def test_monthly_last_observed_adj_close_without_double_adjustment(self):
        frame = yahoo_frame(["2010-01-04", "2010-01-29", "2010-02-26"], [90., 101., 110.])
        monthly = adapter.monthly_observations(frame, "VT", "2010-01-01", "2010-02-28")
        self.assertEqual(monthly.date.tolist(), ["2010-01-31", "2010-02-28"])
        self.assertEqual(monthly.source_trade_date.tolist(), ["2010-01-29", "2010-02-26"])
        self.assertEqual(monthly.performance_value.tolist(), [101., 110.])
        self.assertEqual(monthly.source_row.tolist(), [3, 4])
        self.assertEqual(monthly.source_timestamp.iloc[0], "2010-01-29T00:00:00-05:00")

    def test_missing_month_not_shortened(self):
        with self.assertRaisesRegex(adapter.PreparationError, "Missing months.*2010-02"):
            adapter.monthly_observations(yahoo_frame(["2010-01-29", "2010-03-31"]), "VT", "2010-01-01", "2010-03-31")

    def test_invalid_last_value_not_replaced_by_earlier_valid_value(self):
        for value in ["", "NaN", "Infinity", "0", "-1"]:
            with self.subTest(value=value), self.assertRaises(adapter.PreparationError):
                adapter.monthly_observations(yahoo_frame(["2010-01-28", "2010-01-29"], [100, value]), "VT", "2010-01-01", "2010-01-31")

    def test_duplicate_or_unordered_daily_dates(self):
        for dates in [["2010-01-29", "2010-01-29"], ["2010-01-29", "2010-01-28"]]:
            with self.subTest(dates=dates), self.assertRaisesRegex(adapter.PreparationError, "Duplicate/unordered"):
                adapter.monthly_observations(yahoo_frame(dates), "VT", "2010-01-01", "2010-01-31")

    def test_source_timestamp_date_must_match(self):
        frame = yahoo_frame(["2010-01-29"])
        frame.loc[0, "source_timestamp"] = "2010-01-28T00:00:00-05:00"
        with self.assertRaises(adapter.PreparationError):
            adapter.monthly_observations(frame, "VT", "2010-01-01", "2010-01-31")

    def test_different_last_trade_days_are_reported(self):
        a = adapter.monthly_observations(yahoo_frame(["2010-01-29"]), "VT", "2010-01-01", "2010-01-31")
        b = adapter.monthly_observations(yahoo_frame(["2010-01-28"]), "IEF", "2010-01-01", "2010-01-31")
        with self.assertRaisesRegex(adapter.PreparationError, "Different last.*2010-01-31.*2010-01-29.*2010-01-28"):
            adapter.shared_trade_dates({"VT": a, "IEF": b}, ["VT", "IEF"], "2010-01-31", "2010-01-31")

    def test_missing_required_asset_month_fails(self):
        frame = pd.DataFrame({"date": ["2010-01-31"], "source_trade_date": ["2010-01-29"]})
        with self.assertRaisesRegex(adapter.PreparationError, "Missing/duplicate month-end"):
            adapter.shared_trade_dates({"VT": frame}, ["VT"], "2010-01-31", "2010-02-28")

    def test_rf_strict_lag_percent_to_decimal_and_actual_calendar_days(self):
        quotes = [{"quote_date": "2020-01-29", "annual_rate_percent": 5., "raw_quote": "5", "source_row": 2},
                  {"quote_date": "2020-01-30", "annual_rate_percent": 99., "raw_quote": "99", "source_row": 3},
                  {"quote_date": "2020-02-28", "annual_rate_percent": 88., "raw_quote": "88", "source_row": 4}]
        dates = {"2020-01-31": "2020-01-30", "2020-02-29": "2020-02-28"}
        result, provenance = adapter.risk_free_periods(quotes, dates, "main")
        self.assertEqual(result.period_start.tolist(), ["2020-01-31"])
        self.assertEqual(result.period_end.tolist(), ["2020-02-29"])
        self.assertAlmostEqual(result.period_return.iloc[0], .05 * 29 / 365)
        self.assertEqual(provenance[0]["quote_date"], "2020-01-29")
        self.assertEqual(provenance[0]["calendar_days"], 29)
        self.assertEqual(provenance[0]["quote_age_calendar_days"], 1)

    def test_rf_missing_daily_quotes_are_skipped_not_zero(self):
        path = self.root / "fred.csv"
        path.write_text("observation_date,DGS3MO\n2010-01-27,4\n2010-01-28,.\n2010-01-29,\n", encoding="utf-8")
        quotes, report = adapter.read_fred(path)
        result, proof = adapter.risk_free_periods(quotes, {"2010-01-31": "2010-01-29", "2010-02-28": "2010-02-26"}, "main")
        self.assertEqual(report["missing_daily_quotes"], 2)
        self.assertEqual(proof[0]["quote_date"], "2010-01-27")
        self.assertAlmostEqual(result.period_return.iloc[0], .04 * 28 / 365)

    def test_rf_seven_days_allowed_eight_days_rejected(self):
        dates = {"2010-01-31": "2010-01-29", "2010-02-28": "2010-02-26"}
        for quote, fails in [("2010-01-22", False), ("2010-01-21", True)]:
            quotes = [{"quote_date": quote, "annual_rate_percent": 1.}]
            if fails:
                with self.assertRaisesRegex(adapter.PreparationError, "older than seven days"):
                    adapter.risk_free_periods(quotes, dates, "main")
            else:
                self.assertEqual(adapter.risk_free_periods(quotes, dates, "main")[1][0]["quote_age_calendar_days"], 7)

    def test_rf_no_prior_quote_rejected(self):
        with self.assertRaisesRegex(adapter.PreparationError, "No strictly earlier"):
            adapter.risk_free_periods([{"quote_date": "2010-01-29", "annual_rate_percent": 1.}],
                                     {"2010-01-31": "2010-01-29", "2010-02-28": "2010-02-26"}, "main")

    def test_rf_negative_rate_not_floored_and_nonfinite_rejected(self):
        dates = {"2010-01-31": "2010-01-29", "2010-02-28": "2010-02-26"}
        result, _ = adapter.risk_free_periods([{"quote_date": "2010-01-28", "annual_rate_percent": -.1}], dates, "main")
        self.assertAlmostEqual(result.period_return.iloc[0], -.001 * 28 / 365)
        for value in ["NaN", "Infinity", "bad"]:
            with self.subTest(value=value), self.assertRaises(adapter.PreparationError):
                adapter.risk_free_periods([{"quote_date": "2010-01-28", "annual_rate_percent": value}], dates, "main")

    def test_fred_duplicate_dates_fail(self):
        path = self.root / "fred.csv"
        path.write_text("observation_date,DGS3MO\n2010-01-28,1\n2010-01-28,2\n", encoding="utf-8")
        with self.assertRaisesRegex(adapter.PreparationError, "duplicate or unordered"):
            adapter.read_fred(path)

    def test_latin1_and_utf16_le_without_bom_same_historical_values(self):
        results = []
        for encoding in ["latin-1", "utf-16-le"]:
            path = self.root / (encoding + ".xls")
            weo_fixture(path, encoding=encoding)
            rows, proof, report = adapter.read_weo(path, self.release())
            self.assertEqual(report["encoding"], encoding)
            self.assertEqual(len(rows), 14)
            self.assertEqual({r["period"] for r in rows}, {"2020", "2021"})
            self.assertNotIn("2022", {r["period"] for r in rows})
            self.assertEqual(report["footer_rows"], 1)
            results.append(rows)
        self.assertEqual(results[0], results[1])

    def test_utf16_nul_bytes_not_removed_or_misread_as_latin1(self):
        path = self.root / "weo.xls"
        weo_fixture(path, encoding="utf-16-le")
        original = path.read_bytes()
        self.assertIn(b"\x00", original)
        rows, _, _ = adapter.read_weo(path, self.release())
        self.assertEqual(path.read_bytes(), original)
        self.assertEqual(next(r["value"] for r in rows if r["country"] == "GBR" and r["period"] == "2020"), 2758.87)

    def test_imf_historical_missing_value_or_wrong_units_rejected(self):
        for params in [{"missing": True}, {"unit": "National currency"}]:
            path = self.root / "weo.xls"; weo_fixture(path, **params)
            with self.subTest(params=params), self.assertRaises(adapter.PreparationError):
                adapter.read_weo(path, self.release())

    def test_duplicate_g7_indicator_rejected(self):
        path = self.root / "weo.xls"; weo_fixture(path, duplicate=True)
        with self.assertRaisesRegex(adapter.PreparationError, "Duplicate G7 NGDPD"):
            adapter.read_weo(path, self.release())

    def test_wrong_weo_footer_identity_rejected(self):
        path = self.root / "weo.xls"; weo_fixture(path)
        path.write_bytes(path.read_bytes().replace(b"October 2022", b"October 2023"))
        with self.assertRaisesRegex(adapter.PreparationError, "footer contradicts"):
            adapter.read_weo(path, self.release())

    def test_register_author_dates_and_2012_exception(self):
        rows = adapter.read_register(ROOT / "scripts/study_v1/weo_release_register.csv")
        self.assertEqual(len(rows), 16)
        special = next(r for r in rows if r["edition"] == "2012-10")
        self.assertEqual(special["publication_date"], "2012-10-08")
        self.assertEqual(special["available_from"], "2012-10-10")
        self.assertIn("October 9", special["availability_note"])

    def test_true_2022_raw_regression_and_engine_cross_check(self):
        path = ROOT / "data/study_v1/raw/imf/2022-10/weooct2022all.xls"
        if not path.exists():
            self.skipTest("The explicitly selected local WEO 2022 file is absent")
        before = path.read_bytes()
        rows, proof, report = adapter.read_weo(path, self.release())
        self.assertEqual(report["historical_cutoffs"]["GBR"], 2020)
        self.assertEqual({v for k, v in report["historical_cutoffs"].items() if k != "GBR"}, {2021})
        self.assertEqual(next(r["value"] for r in rows if r["country"] == "GBR" and r["period"] == "2020"), 2758.87)
        versions = [{**r, "source_file": path.name, "source_sha256": adapter.digest(path)} for r in proof]
        checks = adapter.g7_decisions(versions, ["2022-12-31"])
        self.assertEqual(checks.selected_period.unique().tolist(), ["2020"])
        self.assertEqual(checks.edition.unique().tolist(), ["2022-10"])
        self.assertAlmostEqual(checks.target_weight.sum(), 1.)
        from maturarbeit_engine.data.validate import validate_macro
        from maturarbeit_engine.data.macro import select_gdp_targets
        targets, decision = select_gdp_targets(validate_macro(pd.DataFrame(rows)),
                                               {"country_assets": adapter.COUNTRY_ASSETS, "indicator": "NGDPD", "unit": "USD_billions"},
                                               pd.Timestamp("2022-12-31"), "annual_rebalance")
        self.assertEqual(decision["selected_period"], "2020")
        self.assertAlmostEqual(sum(targets), 1.)
        self.assertEqual(path.read_bytes(), before)

    def test_g7_latest_revision_no_lookahead_and_dynamic_common_year(self):
        versions = []
        for edition, available, max_year, base in [("2021-10", "2021-10-13", 2020, 10), ("2022-10", "2022-10-12", 2021, 20)]:
            for country in sorted(adapter.COUNTRY_ASSETS):
                for year in range(2020, max_year + 1):
                    if edition == "2022-10" and country == "GBR" and year == 2021:
                        continue
                    versions.append({"country": country, "period": str(year), "value": float(base), "unit": "USD_billions",
                                     "edition": edition, "available_from": available, "source_row": 2, "source_file": "synthetic", "source_sha256": "synthetic"})
        earlier = adapter.g7_decisions(versions, ["2022-10-11"])
        self.assertEqual(earlier.edition.unique().tolist(), ["2021-10"])
        latest = adapter.g7_decisions(versions, ["2022-12-31"])
        self.assertEqual(latest.selected_period.unique().tolist(), ["2020"])
        self.assertEqual(latest.edition.unique().tolist(), ["2022-10"])
        self.assertEqual(latest.value.tolist(), [20.] * 7)
        versions.append({**versions[-1], "country": "GBR", "period": "2021"})
        self.assertEqual(adapter.g7_decisions(versions, ["2022-12-31"]).selected_period.unique().tolist(), ["2021"])

    def test_g7_missing_country_never_removed_from_denominator(self):
        with self.assertRaisesRegex(adapter.PreparationError, "No common historical"):
            adapter.g7_decisions([], ["2022-12-31"])

    def test_country_asset_mapping(self):
        self.assertEqual(adapter.ASSETS["VT"], ("WORLD_EQ", "GLOBAL"))
        self.assertEqual(adapter.COUNTRY_ASSETS, {"USA": "US_EQ", "CAN": "CA_EQ", "JPN": "JP_EQ", "GBR": "GB_EQ",
                                                 "DEU": "DE_EQ", "FRA": "FR_EQ", "ITA": "IT_EQ"})

    def test_frozen_source_allows_only_git_line_endings(self):
        adapter.verify_frozen_source(b"value = 1\n", b"value = 1\r\n", b"value = 1\r\n", "example.py")
        for workspace, installed in [(b"value = 2\n", b"value = 1\n"),
                                     (b"value = 1\n", b"value = 2\r\n")]:
            with self.subTest(workspace=workspace, installed=installed), self.assertRaisesRegex(adapter.PreparationError, "Engine differs"):
                adapter.verify_frozen_source(b"value = 1\n", workspace, installed, "example.py")

    def test_strict_csv_width_nul_and_duplicate_headers(self):
        for content in [b"a,b\n1,2,3\n", b"a,a\n1,2\n", b"a,b\n1,2\x00x\n"]:
            path = self.root / "invalid.csv"; path.write_bytes(content)
            with self.subTest(content=content), self.assertRaises(adapter.PreparationError):
                adapter.read_csv(path)

    def test_unsafe_output_or_existing_output_refused(self):
        output = self.root / "existing"; output.mkdir()
        (output / "keep.txt").write_bytes(b"preserve")
        with self.assertRaisesRegex(adapter.PreparationError, "Output already exists"):
            adapter.prepare(self.root / "absent", self.root / "absent2", output)
        self.assertEqual((output / "keep.txt").read_bytes(), b"preserve")
        raw = self.root / "raw"; raw.mkdir()
        with self.assertRaisesRegex(adapter.PreparationError, "separate from"):
            adapter.prepare(raw, self.root / "imf", raw / "output")

    def test_explicit_missing_raw_no_fallback(self):
        with self.assertRaisesRegex(adapter.PreparationError, "Explicit raw directory missing; no fallback"):
            adapter.prepare(self.root / "not-there", self.root / "other", self.root / "new-output")
        self.assertFalse((self.root / "new-output").exists())

    def test_nonfinite_or_missing_output_refused(self):
        for value in [math.nan, math.inf]:
            with self.subTest(value=value), self.assertRaises(adapter.PreparationError):
                adapter.write_frame(self.root / "out.csv", pd.DataFrame({"value": [value]}))

    def synthetic_archive(self):
        raw = self.root / adapter.SNAPSHOT_NAME; raw.mkdir()
        (raw / "yahoo").mkdir(); (raw / "fred").mkdir()
        releases = adapter.read_register(ROOT / "scripts/study_v1/weo_release_register.csv")
        imf = self.root / "imf"; imf.mkdir()
        requests = []
        for symbol, (asset, _) in adapter.ASSETS.items():
            start = "2002-07-01" if symbol == "IEF" else "2002-01-01" if symbol == "VTI" else "2009-01-01"
            dates = pd.date_range(start, "2025-12-31", freq="BME").strftime("%Y-%m-%d").tolist()
            frame = yahoo_frame(dates)
            frame.to_csv(raw / "yahoo" / (symbol + ".csv"), index=False)
            adapter.write_json(raw / "yahoo" / (symbol + "_metadata.json"),
                               {"symbol": symbol, "currency": "USD", "instrumentType": "ETF", "exchangeTimezoneName": "America/New_York",
                                "exchangeName": "PCX", "longName": "Synthetic " + symbol})
            requests.append({"symbol": symbol, "proposed_asset_id": asset, "parameters": {
                "start": "2002-01-01" if symbol in {"VTI", "IEF"} else "2009-01-01", "end": "2026-01-01", "interval": "1d",
                "auto_adjust": False, "back_adjust": False, "repair": False, "keepna": True, "actions": True},
                             "coverage": {"rows": len(frame), "columns": list(frame.columns), "first_date": dates[0], "last_date": dates[-1]},
                             "source_page": "synthetic"})
        quotes = pd.date_range("2002-01-01", "2025-12-31", freq="BME") - pd.Timedelta(days=1)
        pd.DataFrame({"observation_date": quotes.strftime("%Y-%m-%d"), "DGS3MO": [5] * len(quotes)}).to_csv(raw / "fred/DGS3MO.csv", index=False)
        requests.append({"series_id": "DGS3MO", "provider": "FRED", "url": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS3MO"})
        files = [{"path": p.relative_to(raw).as_posix(), "bytes": p.stat().st_size, "sha256": adapter.digest(p)} for p in sorted(raw.rglob("*")) if p.is_file()]
        adapter.write_json(raw / "acquisition_manifest.json", {"status": "ACQUIRED_PENDING_DATA_REVIEW", "backtest_executed": False, "requests": requests, "files": files})
        for release in releases:
            folder = imf / release["edition"]; folder.mkdir()
            month = "September" if release["edition"].endswith("-09") else "October"
            year = int(release["edition"][:4]); name = f"weo{'sep' if month == 'September' else 'oct'}{year}all.xls"
            header = ["WEO Country Code", "ISO", "WEO Subject Code", "Country", "Subject Descriptor", "Units", "Scale"]
            header += [str(y) for y in range(2008, 2024)] + ["Estimates Start After"]
            buf = io.StringIO(); writer = csv.writer(buf, delimiter="\t", lineterminator="\n"); writer.writerow(header)
            for country in adapter.COUNTRY_ASSETS:
                writer.writerow(["1", country, "NGDPD", "Synthetic", "Gross domestic product, current prices", "U.S. dollars", "Billions"]
                                + ["1,000" for _ in range(2008, 2024)] + [year - 1])
            writer.writerow([f"International Monetary Fund, World Economic Outlook Database, {month} {year}"])
            (folder / name).write_bytes(buf.getvalue().encode("utf-16-le" if year in {2020, 2024} else "latin-1"))
            (folder / "download_note.txt").write_text(f"Ausgabe: WEO {month} {year}\nDownloadseite: {release['download_url']}\nDownloadzeitpunkt: 2026-10-09T12:00:00+02:00\nOriginaldateiname: {name}\nDownloadoption: Tab Delimited Values / By Countries\n", encoding="utf-8")
        return raw, imf

    def test_full_normalization_reproducible_hashes_raw_unchanged_and_us_own_history(self):
        raw, imf = self.synthetic_archive()
        before = adapter.raw_inventory(raw, imf)
        first, second = self.root / "first", self.root / "second"
        # Any attempt to execute a strategy through the runner is a test failure.
        with patch("maturarbeit_engine.engine.simulation.run_simulation", side_effect=AssertionError("No backtest allowed")):
            report = adapter.prepare(raw, imf, first)
            adapter.prepare(raw, imf, second)
        self.assertEqual(report["status"], adapter.STATUS)
        self.assertFalse(report["backtest_executed"])
        self.assertEqual(report["engine_validation"]["studies"]["main"]["valuations"], 193)
        self.assertEqual(report["engine_validation"]["studies"]["us"]["return_periods"], 276)
        self.assertEqual(adapter.raw_inventory(raw, imf), before)
        self.assertEqual({p.name for p in first.iterdir()}, {p.name for p in second.iterdir()})
        self.assertEqual(len(list(first.iterdir())), 12)
        for path in first.iterdir():
            self.assertEqual(path.read_bytes(), (second / path.name).read_bytes(), path.name)
        manifest = adapter.strict_json(first / "processed_manifest.json")
        for item in manifest["outputs"]:
            self.assertEqual(adapter.digest(first / item["path"]), item["sha256"])
        us = adapter.read_csv(first / "us_market.csv")
        self.assertEqual(us.loc[us.asset_id == "US_EQ"].date.iloc[0], "2002-01-31")
        self.assertEqual(us.loc[us.asset_id == "US_TREASURY_7_10"].date.iloc[0], "2002-07-31")
        self.assertEqual(len(us), 570)
        self.assertEqual(len(adapter.read_csv(first / "main_market.csv")), 1836)
        self.assertEqual(len(adapter.read_csv(first / "rf_main.csv")), 192)
        self.assertEqual(len(adapter.read_csv(first / "rf_us.csv")), 276)
        with self.assertRaisesRegex(adapter.PreparationError, "Output already exists"):
            adapter.prepare(raw, imf, first)

    def test_acquisition_tamper_detected(self):
        raw, imf = self.synthetic_archive()
        with (raw / "yahoo/VT.csv").open("ab") as stream:
            stream.write(b"modified")
        with self.assertRaisesRegex(adapter.PreparationError, "Acquisition SHA/size mismatch"):
            adapter.prepare(raw, imf, self.root / "output")
        self.assertFalse((self.root / "output").exists())


if __name__ == "__main__":
    unittest.main()
