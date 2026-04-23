# 308-Jamie-Ct-3b d-house — Technical Journal

**Owner:** Ethan Kunz
**Created:** 2026-04-23
**Last Updated:** 2026-04-23
**Total Sessions:** 1
**Total Development Time:** ~0.1 hours
**Current Phase:** Initial Setup

---

### 2026-04-23 (Thursday) — Project Scaffolding
**Phase:** Initial Setup
**Duration:** ~5 minutes
**Collaborators:** Ethan Kunz + Claude Code (Project Template Generator)

#### Work Completed

**1. Project Scaffolded**
   - Generated directory structure via Project Template Generator
   - Domain: Web Application
   - All mandatory files created (README.md, CLAUDE.md, GEMINI.md)

#### Key Technical Decisions

1. **Domain selection:** Web Application — chosen based on project requirements

#### Files Modified

- All files created from templates
- Summary: Initial scaffolding

#### Next Steps
1. Fill in project-specific content in README.md and CLAUDE.md
2. Begin implementation

---

### 2026-04-23 (Thursday) — Initial Data Population
**Phase:** Active Setup
**Duration:** ~30 minutes
**Collaborators:** Ethan Kunz + Claude (Cowork)

#### Work Completed

**1. Archive Documents Read**
   - Lease_308_Jamie_CT_Lease_and_Amendments_2025_signed.pdf — confirmed Geers as current tenant, $1,865/mo, lease May 2025–May 2026
   - 308 Jamie Ct Longview -Appraisal-2023.pdf — confirmed property specs: 1,735 sqft, 3/2, slab, brick, 14,584 sqft lot, $237K appraised Mar 2023
   - HVAC_Replace_Agreement_308Jamie_Kunz.pdf — Comfort King 3-ton, $12,141, July 2024, A/C Contractors TACLB4214C
   - Schedule-of-Real-Estate-Owned.pdf — mortgage balance $138,226, PITI $1,240.45, estimated value $250K as of Dec 2025
   - Lease_308_Jamie_CT_Lease_and_Amendments_2024.pdf — confirmed 2024 rent $1,750 base (+3.1%)

**2. config.yaml Populated**
   - All property specs, tenant info, lease history, financials, maintenance, warranties, contacts, and document index
   - Derived 2023 base rent ~$1,697 from 3.1% increase reference; flagged as estimate
   - $40/mo pet fee confirmed ($1,865 total = $1,825 base + $40 pet)

**3. CLAUDE.md Updated**
   - Replaced skeleton with full property context, AI operating rules, financial summary, key dates

**4. dashboard.html Built**
   - 5-tab dashboard: Overview, Financials, Lease & Tenant, Maintenance, Documents
   - Navy/gold/coral theme matching Kunz Finance design language
   - Active alerts for lease renewal (May 2026) and HVAC labor warranty (Jul 2026)

**5. STATUS.md Updated**

#### Key Technical Decisions

1. **Rent = $1,865 total** (not $1,825 base alone) — pet fee confirmed from lease doc comparison
2. **PITI = $1,240.45** — includes escrowed tax ($306.17) and insurance ($228.25); not just P&I
3. **config.yaml as single source of truth** — all values derived from or linked to archive docs

#### Data Gaps Noted (for future sessions)

- 2020 and 2022 original tenant details unknown (lease docs exist but text extraction was partial)
- 2018 appraisal value not extracted
- Maintenance costs for 2023 plumbing/garage work unknown
- Mortgage servicer phone number not confirmed

#### Files Modified

- config/config.yaml (populated from skeleton)
- CLAUDE.md (replaced skeleton)
- dashboard.html (replaced blank template)
- docs/active/STATUS.md (updated)
- docs/active/TECHNICAL_JOURNAL.md (this entry)

#### Next Steps
1. Define GEMINI.md domain mandates
2. Capture 2020/2022 lease details when needed
3. Update config with mortgage statement on next statement receipt

---

### 2026-04-23 (Thursday) — Document Organization & Data Reconciliation
**Phase:** Active — Records Consolidation
**Duration:** ~20 minutes
**Collaborators:** Ethan Kunz + Claude Code

#### Work Completed

**1. Stale PITI Corrected**
   - CLAUDE.md Financial Summary table: $1,240.45 → $1,328.67/mo (verified via USAA + 1098)
   - Rules #3, #9, #11 updated to match verified figures
   - Net to owner corrected: ~$424 → ~$336/mo; annual ~$5,094 → ~$4,032

**2. Tenant History Gap Filled**
   - Avail payment history CSV (`2026-04-23-received-payments-report.csv`) confirmed: first tenant was **Brittin Stevens**, not "Unknown"
   - Rent history: $1,300/mo (Jul 2020–May 2022) → $1,365/mo (May 2022–May 2023, +5.0%)
   - Updated in config.yaml, CLAUDE.md, SUMMARY.md, dashboard.html across all 3 history tables

**3. 4th-Term Lease Draft Loaded**
   - Draft at $1,920/mo ($1,880 base + $40 pet fee, +2.9% from current $1,865)
   - CPI-based methodology documented in §3 of draft
   - Flagged as `draft_unsigned` in config.yaml; added to all history tables with DRAFT badge
   - Status escalated to CRITICAL in STATUS.md — must sign before May 1, 2026

**4. File Organization**
   - `lease_308_jamie_ct_4th_term_2026_draft.md` → `docs/Archive/Reference/Leases/2026/`
   - `308-Jamie-Claude-Research-April2026.md` → `docs/Archive/Reference/General/`
   - `2026-04-23-received-payments-report.csv` → `docs/Archive/Reference/General/`
   - `docs/Archive/Reference/taxes/` (2018–2025) — already in correct location; added to config.yaml index

**5. Config & Dashboard Updated**
   - config.yaml: documents index updated with all new files; tax_archive section added
   - dashboard.html: overview + lease tab alerts upgraded to danger; rent/lease history tables updated

#### Key Findings

1. **GCAD sqft discrepancy** — Research report flags 1,666 sqft per GCAD vs. 1,735 sqft on appraisal. May affect future assessed value. Not urgent.
2. **Taxes 2024 1040-X** — Still overdue. $1,711 owed. Target was Feb 2026.
3. **4th-term lease is time-critical** — 8 days until May 1 expiry.

#### Files Modified

- CLAUDE.md (PITI, balance, rules #3/#9/#11, key dates)
- config/config.yaml (tenant history, 4th-term draft entry, documents index, tax_archive section)
- SUMMARY.md (cash flow note, lease history table, action items)
- dashboard.html (alerts, rent history, lease history, clause gap path)
- docs/active/STATUS.md (completion 60%→75%, blockers, active items, milestones)
- docs/active/TECHNICAL_JOURNAL.md (this entry)
- File moves: 3 documents reorganized to proper subdirectories

#### Next Steps
1. Sign 4th-term lease before May 1, 2026 (add missing clauses first)
2. Contact Meridian re: 2024 1040-X and 2025 return
3. Define GEMINI.md domain mandates
