from pathlib import Path

import pytest
import yaml


@pytest.fixture()
def minimal_cfg(tmp_path: Path) -> Path:
    cfg = {
        "project": {"owner": "Owner O.", "lease_platform": "Avail.co"},
        "property": {
            "address": "308 Jamie Court",
            "city": "Longview",
            "state": "TX",
            "zip": "75605",
        },
        "tenant": {"primary": "A", "secondary": "B"},
        "lease": {
            "history": [
                {
                    "year": 2026,
                    "rent_base": 1880,
                    "pet_fee": 40,
                    "rent_total_monthly": 1920,
                }
            ]
        },
    }
    p = tmp_path / "config.yaml"
    p.write_text(yaml.safe_dump(cfg), encoding="utf-8")
    return p


@pytest.fixture()
def client(minimal_cfg: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    import lease_api

    monkeypatch.setattr(lease_api, "CONFIG_FILE", minimal_cfg)
    ack = tmp_path / "ack.json"
    monkeypatch.setattr(lease_api, "ACK_FILE", ack)
    from fastapi.testclient import TestClient

    return TestClient(lease_api.app)
