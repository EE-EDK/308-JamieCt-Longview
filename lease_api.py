"""
308 Jamie Court — Lease API
Serves tenant-facing lease data from config.yaml and records acknowledgments.
Port 8084 — reverse-proxied via Caddy at /lease-api/*
"""

import json
from datetime import datetime, timezone
from pathlib import Path

import yaml
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

BASE_DIR = Path(__file__).parent
CONFIG_FILE = BASE_DIR / "config" / "config.yaml"
ACK_FILE = BASE_DIR / "data" / "acknowledgments.json"

ALLOWED_ORIGINS = [
    "https://ee-edk.github.io",
    "https://edk7c.github.io",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app = FastAPI(title="308 Jamie Ct — Lease API", root_path="/lease-api")


class PrivateNetworkMiddleware(BaseHTTPMiddleware):
    """Handle Chrome Private Network Access preflights."""

    async def dispatch(self, request: Request, call_next):
        origin = request.headers.get("origin", "")
        if (
            request.method == "OPTIONS"
            and request.headers.get("access-control-request-private-network")
            and origin in ALLOWED_ORIGINS
        ):
            return Response(
                status_code=200,
                headers={
                    "Access-Control-Allow-Origin": origin,
                    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Private-Network": "true",
                    "Access-Control-Max-Age": "600",
                },
            )
        return await call_next(request)


app.add_middleware(PrivateNetworkMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)


def _load_config() -> dict:
    with open(CONFIG_FILE) as f:
        return yaml.safe_load(f)


def _load_acks() -> list:
    if ACK_FILE.exists():
        with open(ACK_FILE) as f:
            return json.load(f)
    return []


def _save_ack(entry: dict) -> None:
    acks = _load_acks()
    acks.append(entry)
    ACK_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(ACK_FILE, "w") as f:
        json.dump(acks, f, indent=2)


# ── Models ────────────────────────────────────────────────────────────────────

class AcknowledgeRequest(BaseModel):
    tenant1_name: str
    tenant2_name: str
    confirmed: bool


# ── Endpoints ─────────────────────────────────────────────────────────────────

@app.get("/data")
def get_lease_data():
    """Return tenant-facing lease data for the 4th-term (2026) lease."""
    cfg = _load_config()
    tenant = cfg["tenant"]
    lease_2026 = next(
        (h for h in cfg["lease"]["history"] if h["year"] == 2026), {}
    )

    return {
        "tenant1": tenant["primary"],
        "tenant2": tenant["secondary"],
        "property_address": (
            f"{cfg['property']['address']}, "
            f"{cfg['property']['city']}, {cfg['property']['state']} "
            f"{cfg['property']['zip']}"
        ),
        "landlord": cfg["project"]["owner"],
        "lease_start": "May 1, 2026",
        "lease_end": "May 1, 2027",
        "base_rent": f"${lease_2026.get('rent_base', 1880):,.0f}",
        "pet_fee": f"${lease_2026.get('pet_fee', 40):,.0f}",
        "total_monthly": f"${lease_2026.get('rent_total_monthly', 1920):,.0f}",
        "security_deposit": "$1,500",
        "late_fee": "$175 per two weeks",
        "lease_term": "Year 4 — 4th Term",
        "platform": cfg["project"]["lease_platform"],
    }


@app.post("/acknowledge")
def post_acknowledge(body: AcknowledgeRequest):
    """Record tenant acknowledgment of the 4th-term lease."""
    if not body.confirmed:
        raise HTTPException(status_code=400, detail="confirmed must be true")

    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "tenant1_name": body.tenant1_name.strip(),
        "tenant2_name": body.tenant2_name.strip(),
        "confirmed": True,
        "lease_term": "4th Term — May 1, 2026",
    }
    _save_ack(entry)
    return {"status": "recorded", "timestamp": entry["timestamp"]}


@app.get("/status")
def get_status():
    """Return all recorded acknowledgments. Owner-facing — Tailscale-only access."""
    acks = _load_acks()
    return {
        "total_acknowledgments": len(acks),
        "acknowledgments": acks,
    }


@app.get("/health")
def health():
    return {"status": "ok"}
