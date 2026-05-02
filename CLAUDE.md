# CLAUDE.md — 308 Jamie Court, Longview TX
# Rental Property Management

**Owner:** Ethan D. Kunz
**Last Updated:** 2026-04-23
**Status:** Active — Occupied

---

## What This Is

Property management documentation for 308 Jamie Court, Longview TX 75605 — a single-family rental property owned by Ethan Kunz. Contains lease history, financial facts, maintenance records, and AI operating rules. All canonical values live in `config/config.yaml`.

---

## Property Quick Facts

| Field | Value |
|---|---|
| Address | 308 Jamie Court, Longview, TX 75605-8003 |
| County | Gregg County |
| Legal | LT 6 BLK 8 RAMBLING CREEK #1 |
| APN | 619372022 |
| Type | Single Family Residential |
| Size | 1,735 sqft above grade |
| Lot | 14,584 sqft (105' × 138.9') |
| Bed/Bath | 3 bed / 2 bath |
| Stories | 1 |
| Year Built | ~1980 |
| Foundation | Slab |
| Exterior | Brick |
| HVAC | Comfort King 3-ton heat pump (replaced July 2024) |
| Garage | Attached 2-car |
| School District | Longview ISD |
| Flood Zone | Zone X (no hazard) |
| Zoning | None (outside city limits) |

---

## Current Tenant

| Field | Value |
|---|---|
| Tenants | Jared Geers & Kayla Geers |
| Jared email | jgeers08@gmail.com |
| Kayla email | geerskayla0413@gmail.com |
| Jared phone | 573-424-7776 |
| Kayla phone | 903-746-9903 |
| In since | May 2023 (Year 4 tenancy) |
| Pets | Yes (pet amendment May 2023) |
| Additional occupant | Daughter (amendment May 2023) |

---

## Current Lease

| Field | Value |
|---|---|
| Year | 4 (3rd amendment) |
| Term | May 1, 2025 – May 1, 2026 |
| Base Rent | $1,825/mo |
| Pet Fee | $40/mo |
| **Total Monthly** | **$1,865/mo** |
| Platform | Avail.co |
| Signed | March 29, 2025 |

**Renewal due:** May 1, 2026. Begin renewal discussion by March 2026.

---

## Financial Summary

| Item | Monthly | Annual |
|---|---|---|
| Gross Rent | $1,865 | $22,380 |
| **PITI Total** | **$1,328.67** | **$15,944** |
| Operating Reserve | $200.00 | $2,400 |
| **Net Operating (after PITI)** | **~$536** | **~$6,432** |
| **Net to Owner (after reserve)** | **~$336** | **~$4,032** |

PITI breakdown: P&I $634.15 + Escrow $694.52 (includes shortage repayment; will normalize once shortage repaid). Verified via USAA statement 07/03/2025 + loanDepot 1098.

**Mortgage:** loanDepot.com, LLC — 2.75% fixed
**Balance (Dec 2025):** $136,310.98 (per 1098)
**Purchase price (May 2020):** $155,337
**Appraised value (Mar 2023):** $237,000
**Estimated value (Dec 2025):** $250,000

**Schedule E:** Annual depreciation ~$4,739 (residential 27.5yr straight-line, improvements basis ~$130,337).

---

## Maintenance History

| Date | Item | Cost | Status |
|---|---|---|---|
| Summer 2023 | Plumbing cleared | Unknown | Done |
| Summer 2023 | Garage door spring/track | Unknown | Done |
| July 8, 2024 | HVAC full replacement | $12,141 | Done |

**Active warranties:**
- HVAC: Comfort King 3-ton heat pump — 10yr parts (expires 2034-07-08), 2yr labor (expires **2026-07-08 ← coming soon**). Contractor: A/C Contractors, 903-759-4250.

---

## Repository Structure

```
real-estate/
├── .gitignore
├── README.md, CLAUDE.md, GEMINI.md, SUMMARY.md, LICENSE
├── config/
│   └── config.yaml                  ← SINGLE SOURCE OF TRUTH
├── dashboard.html                   ← property management dashboard (6-tab)
├── index.html                       ← interactive lease viewer (GitHub Pages)
├── lease_api.py                     ← FastAPI backend (port 8084)
├── output/                          ← generated lease documents (DOCX, PDF)
├── scripts/
│   ├── generate_lease_docs.py       ← markdown → DOCX/PDF generator
│   └── verify_project_state.py
├── data/
│   └── .gitignore                   ← runtime data (gitignored)
└── docs/
    ├── STATUS.md                    ← current blockers + milestones
    ├── TECHNICAL_JOURNAL.md         ← session log
    ├── general/                     ← appraisals, HVAC, plumbing, photos, research
    ├── leases/                      ← leases by year (2020–2026)
    │   └── 2026/                    ← 4th-term v2 source markdown
    └── taxes/                       ← tax returns by year (gitignored)
```

---

## AI Operating Rules

1. **Never invent property data.** Always read `config/config.yaml` for canonical values. Cite `last_updated` when quoting figures.
2. **Rent figure:** Total monthly rent is $1,865 ($1,825 base + $40 pet fee). Do not quote $1,825 alone as total rent.
3. **Mortgage total:** PITI is $1,328.67/mo (verified). Do NOT use P&I alone ($634.15) as the monthly expense figure. Escrow is $694.52 (includes shortage repayment).
4. **Lease renewal:** Current lease expires May 1, 2026. Flag this date when discussing forward planning.
5. **HVAC labor warranty expires July 8, 2026.** If any HVAC issue arises before then, flag warranty coverage.
6. **Tenant contacts:** Jared 573-424-7776 / jgeers08@gmail.com. Kayla: 903-746-9903 / geerskayla0413@gmail.com.
7. **Document references:** Cite path under `docs/` when referencing source docs (e.g., `docs/leases/`, `docs/general/`, `docs/taxes/`).
8. **Config updates:** Update `last_updated` in config.yaml after any value change. Do not store non-numeric metadata in numeric sections.
9. **Net operating income:** Gross ($1,865) − PITI ($1,328.67) = ~$536 gross operating income before reserve. Less $200 reserve = ~$336/mo net to owner.
10. **Depreciation:** Annual ~$4,739 for Schedule E. Estimated basis — verify against actual tax returns.
11. **Lease history:** Brittin Stevens was tenant from Jul 2020 through ~May 2023 across two lease terms — $1,300/mo initially, raised to $1,365/mo in Jun 2022. Confirmed via Avail payment history CSV (`docs/general/2026-04-23-received-payments-report.csv`). Geers started May 2023.
12. **Git security:** Do NOT commit financial statements, tax documents, or tenant PII to any public repo. `data/` is gitignored. Verify with `git ls-files` before any push.

---

## Testing (lease API)

- Install: `pip install -r requirements-dev.txt`
- Run: `python -m pytest test -q` from repo root, or `.\scripts\run_tests.ps1`
- Tests patch `CONFIG_FILE` / `ACK_FILE`; no production network calls

## Session Workflow

### At Session Start
1. Read this file
2. Read `docs/TECHNICAL_JOURNAL.md` (last ~100 lines)
3. Check `docs/STATUS.md` for current blockers
4. Read `config/config.yaml` for any values needed

### During the Session
- Track files changed, decisions made
- Verify config changes with a YAML lint check
- Never delete historical records — annotate as stale, additive only

### END SESSION
1. Run `python scripts/verify_project_state.py`
2. Append entry to `docs/TECHNICAL_JOURNAL.md`
3. Update `docs/STATUS.md`
4. Update `config/config.yaml` `last_updated` if values changed
5. Single descriptive commit

---

## Key Dates

| Date | Event |
|---|---|
| 2020-05-01 | Property purchased ($155,337) |
| 2023-05 | Geers tenancy began |
| 2024-07-08 | HVAC replaced ($12,141) |
| 2025-05-01 | Current lease term begins |
| **2026-05-01** | **4th-term lease draft ready ($1,920/mo) — must sign before this date** |
| 2026-07-08 | HVAC labor warranty expires |
| 2034-07-08 | HVAC parts warranty expires |

---

## What NOT to Do

- Do not commit secrets, financial docs, or tenant PII
- Do not quote P&I alone as the monthly mortgage cost — always use PITI ($1,240.45)
- Do not quote base rent alone as total — always use $1,865 (includes pet fee)
- Do not delete historical lease or maintenance records — annotate instead
- Do not duplicate values from config.yaml inline — reference config as source

---

**v1.0** | 2026-04-23
