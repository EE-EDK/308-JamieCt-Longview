from pathlib import Path

import yaml


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_lease_data_shape(client):
    r = client.get("/data")
    assert r.status_code == 200
    j = r.json()
    assert j["tenant1"] == "A"
    assert "1,920" in j["total_monthly"]


def test_acknowledge_requires_confirmed(client):
    r = client.post(
        "/acknowledge",
        json={"tenant1_name": "A", "tenant2_name": "B", "confirmed": False},
    )
    assert r.status_code == 400


def test_acknowledge_writes_file(client, tmp_path):
    r = client.post(
        "/acknowledge",
        json={"tenant1_name": "A ", "tenant2_name": " B", "confirmed": True},
    )
    assert r.status_code == 200
    st = client.get("/status")
    assert st.json()["total_acknowledgments"] == 1


def test_config_yaml_loads():
    root = Path(__file__).resolve().parents[1]
    cfg_path = root / "config" / "config.yaml"
    assert cfg_path.is_file()
    data = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    assert "tenant" in data
    assert "lease" in data
    years = [h["year"] for h in data["lease"]["history"]]
    assert 2026 in years

