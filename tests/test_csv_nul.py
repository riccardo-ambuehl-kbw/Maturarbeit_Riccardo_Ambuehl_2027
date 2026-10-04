"""Reject the original NEW-EB-01 inputs before pandas or publication."""
import csv
from hashlib import sha256
from io import StringIO
import json
import pandas as pd
import pytest
from maturarbeit_engine.data.normalize import read_csv_snapshot
from maturarbeit_engine.data.validate import DataValidationError
from maturarbeit_engine.engine.simulation import run_simulation


def write_csv(path, rows, *, quoted=False, bom=False):
    buffer = StringIO()
    csv.writer(buffer, lineterminator="\n",
               quoting=csv.QUOTE_ALL if quoted else csv.QUOTE_MINIMAL).writerows(rows)
    path.write_bytes(buffer.getvalue().encode("utf-8-sig" if bom else "utf-8"))


@pytest.fixture
def csv_case(tmp_path):
    tables = {
        "market": [["date", "asset_id", "performance_value"],
                   ["2020-01-31", "A", "100"], ["2020-01-31", "B", "100"],
                   ["2020-02-29", "A", "110"], ["2020-02-29", "B", "100"],
                   ["2020-03-31", "A", "99"], ["2020-03-31", "B", "110"]],
        "assets": [["asset_id", "name", "asset_class", "country", "currency", "provider", "provider_symbol"],
                   ["A", "Artificial A", "synthetic", "C_A", "CHF", "audit", "A"],
                   ["B", "Artificial B", "synthetic", "C_B", "CHF", "audit", "B"]],
        "risk_free": [["period_start", "period_end", "series_id", "period_return"],
                      ["2020-01-31", "2020-02-29", "RF", "0.001"],
                      ["2020-02-29", "2020-03-31", "RF", "0.002"]],
        "macro": [["period", "country", "indicator", "value", "unit", "available_from"],
                  ["2019", "C_A", "GDP", "60", "UNITS", "2020-01-01"],
                  ["2019", "C_B", "GDP", "40", "UNITS", "2020-01-01"]],
    }
    for kind, rows in tables.items():
        write_csv(tmp_path / f"{kind}.csv", rows)
    config = {
        "schema_version": "1.0", "run_name": "synthetic_csv_nul",
        "period": {"start": "2020-01-31", "end": "2020-03-31"},
        "start_capital": 100, "base_currency": "CHF", "periods_per_year": 12,
        "period_frequency": "ME",
        "data": {"market": "market.csv", "assets": "assets.csv", "macro": "macro.csv",
                 "risk_free": {"path": "risk_free.csv", "series_id": "RF"}},
        "strategies": {"country_weighting": {
            "enabled": True, "country_assets": {"C_A": "A", "C_B": "B"},
            "indicator": "GDP", "unit": "UNITS", "rebalance_frequency": "annual"}},
        "output_dir": "runs",
    }
    path = tmp_path / "config.json"
    path.write_text(json.dumps(config), encoding="utf-8")
    return tmp_path, path, tables


def assert_rejected_before_pandas_and_run(root, config, target, kind, monkeypatch):
    original = target.read_bytes()

    def pandas_must_not_receive_nul(*args, **kwargs):
        pytest.fail("NUL-containing input reached pandas.")

    with monkeypatch.context() as blocked:
        blocked.setattr("maturarbeit_engine.data.normalize.pd.read_csv", pandas_must_not_receive_nul)
        with pytest.raises(DataValidationError, match="CSV contains NUL byte") as error:
            read_csv_snapshot(target, kind)
        assert target.name in str(error.value)
    with pytest.raises(DataValidationError, match="CSV contains NUL byte"):
        run_simulation(config)
    assert target.read_bytes() == original, "Reject without repairing the input."
    assert not (root / "runs").exists(), "No invalid run or staging directory may be published."


@pytest.mark.parametrize("kind,column", [
    ("market", "performance_value"), ("assets", "currency"),
    ("risk_free", "period_return"), ("macro", "value")])
@pytest.mark.parametrize("quoted", [False, True], ids=["unquoted", "quoted"])
def test_nul_in_each_input_type_is_rejected_before_parsing_and_output(csv_case, monkeypatch, kind, column, quoted):
    root, config, tables = csv_case
    rows = tables[kind]
    rows[1][rows[0].index(column)] += "\x00INVALID"
    target = root / f"{kind}.csv"
    write_csv(target, rows, quoted=quoted)
    assert b"\x00" in target.read_bytes()
    assert_rejected_before_pandas_and_run(root, config, target, kind, monkeypatch)


def test_exact_1_nul_e2_audit_minimal_case_fails_without_output(tmp_path, monkeypatch):
    (tmp_path / "market.csv").write_bytes(
        b"date,asset_id,performance_value\n2020-01-31,A,1\x00e2\n2020-02-29,A,110\n")
    (tmp_path / "assets.csv").write_bytes(
        b"asset_id,name,asset_class,country,currency,provider,provider_symbol\n"
        b"A,Artificial,synthetic,C_A,CHF,audit,A\n")
    config = {
        "schema_version": "1.0", "run_name": "nul_minimal",
        "period": {"start": "2020-01-31", "end": "2020-02-29"},
        "start_capital": 100, "base_currency": "CHF", "periods_per_year": 12,
        "period_frequency": None, "data": {"market": "market.csv", "assets": "assets.csv"},
        "strategies": {"buy_hold": {"enabled": True, "asset": "A"}}, "output_dir": "runs",
    }
    path = tmp_path / "config.json"
    path.write_text(json.dumps(config), encoding="utf-8")
    assert_rejected_before_pandas_and_run(tmp_path, path, tmp_path / "market.csv", "market", monkeypatch)


@pytest.mark.parametrize("location", ["header", "unused_column"])
def test_nul_anywhere_in_utf8_bom_snapshot_rejects_whole_file(csv_case, monkeypatch, location):
    root, config, tables = csv_case
    rows = tables["market"]
    rows[0].append("note\x00suffix" if location == "header" else "note")
    for row in rows[1:]:
        row.append("retained text")
    if location == "unused_column":
        rows[-1][-1] += "\x00suffix"
    target = root / "market.csv"
    write_csv(target, rows, bom=True)
    assert target.read_bytes().startswith(b"\xef\xbb\xbf")
    assert_rejected_before_pandas_and_run(root, config, target, "market", monkeypatch)


@pytest.mark.parametrize("bom", [False, True], ids=["utf8", "utf8_bom"])
def test_valid_quotes_multiline_extra_columns_and_bom_remain_unchanged(csv_case, bom):
    root, config, tables = csv_case
    tables["assets"][1][1] = "Artificial, quoted name"
    tables["assets"][2][1] = "Artificial\nmultiline name"
    for kind, rows in tables.items():
        rows[0].append("named_extra")
        for row in rows[1:]:
            row.append("quoted, comma\nand newline")
        path = root / f"{kind}.csv"
        write_csv(path, rows, bom=bom)
        frame, info = read_csv_snapshot(path, kind)
        assert frame.index.equals(pd.RangeIndex(len(rows) - 1))
        assert frame.columns.tolist() == rows[0]
        assert frame.values.tolist() == rows[1:]
        assert info["sha256"] == sha256(path.read_bytes()).hexdigest()
    outcome = run_simulation(config)
    # No annual event occurs here: the original 60/40 holdings retain their units.
    expected = [100, 60 * 1.10 + 40, 60 * 0.99 + 40 * 1.10]
    assert outcome.result.portfolio_history.portfolio_value.tolist() == pytest.approx(expected)
    assert outcome.output_path.is_dir()
