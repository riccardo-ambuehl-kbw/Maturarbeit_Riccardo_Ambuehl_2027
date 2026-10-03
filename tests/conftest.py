"""Synthetic inputs and a network guard for every test."""
import json
import socket
import urllib.request
import pandas as pd
import pytest


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def blocked(*args, **kwargs):
        raise AssertionError("Network access is forbidden in a backtest test.")
    for name in ["connect", "connect_ex"]:
        monkeypatch.setattr(socket.socket, name, blocked)
    monkeypatch.setattr(socket, "create_connection", blocked)
    monkeypatch.setattr(socket, "getaddrinfo", blocked)
    monkeypatch.setattr(urllib.request, "urlopen", blocked)


@pytest.fixture
def case(tmp_path):
    market = pd.DataFrame({"date": ["2020-01-31", "2020-02-29", "2020-03-31"],
                           "asset_id": ["SYNTH_A"] * 3, "performance_value": [100., 110., 99.]})
    assets = pd.DataFrame([{"asset_id": "SYNTH_A", "name": "Artificial index", "asset_class": "synthetic",
                            "country": "SYNTHETIC", "currency": "CHF", "provider": "synthetic",
                            "provider_symbol": "ARTIFICIAL"}])
    rf = pd.DataFrame({"period_start": ["2020-01-31", "2020-02-29"],
                       "period_end": ["2020-02-29", "2020-03-31"],
                       "series_id": ["SYNTH_RF"] * 2, "period_return": [.001, .002]})
    raw = {"schema_version": "1.0", "run_name": "synthetic_test",
           "period": {"start": "2020-01-01", "end": "2020-03-31"},
           "start_capital": 100, "base_currency": "CHF", "periods_per_year": 12,
           "period_frequency": "ME", "data": {"market": "market.csv", "assets": "assets.csv",
                       "risk_free": {"path": "rf.csv", "series_id": "SYNTH_RF"}},
           "strategies": {"buy_hold": {"enabled": True, "asset": "SYNTH_A"}},
           "output_dir": "runs"}
    def save():
        market.to_csv(tmp_path / "market.csv", index=False)
        assets.to_csv(tmp_path / "assets.csv", index=False)
        rf.to_csv(tmp_path / "rf.csv", index=False)
        (tmp_path / "config.json").write_text(json.dumps(raw, allow_nan=False), encoding="utf-8")
        return tmp_path / "config.json"
    save()
    return {"root": tmp_path, "market": market, "assets": assets, "rf": rf, "raw": raw, "save": save}
