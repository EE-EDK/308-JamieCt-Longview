# 308-Jamie-Ct-3b d-house — Technical Journal

**Owner:** Ethan Kunz
**Created:** 2026-04-23
**Last Updated:** 2026-04-24
**Total Sessions:** 4
**Total Development Time:** ~4.5 hours
**Current Phase:** Active — Lease Viewer Live, API Deployed, Jared Acknowledged

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

---

### 2026-04-23 (Thursday) — Media Gitignore & Repo Cleanup
**Phase:** Active — Repo Hygiene
**Duration:** ~10 minutes
**Collaborators:** Ethan Kunz + Claude Code

#### Work Completed

**1. Media Files Excluded from Git**
   - `.gitignore` extended with patterns for all video/image extensions: `mp4, mov, avi, mkv, wmv, jpg, jpeg, png, gif, bmp, webp, xhtml`
   - 48 files untracked from git index: 16 property walkthrough videos + 32 property photos
   - All files remain on disk — removed from repo only
   - Committed and pushed as `15b9038`

**2. Git History Note**
   - Binary data for those 48 files still exists in earlier commits (`aed5e46 initial`)
   - If repo size becomes a concern, `git filter-repo` can purge them from history

#### Files Modified
- `.gitignore` (media patterns added)

#### Next Steps
1. Sign 4th-term lease before May 1, 2026 (add missing clauses — see Clause Gap Analysis)
2. Contact Meridian: 2024 Form 1040-X (~$1,711 owed, overdue) + 2025 return
3. Define GEMINI.md domain mandates
4. Optional: `git filter-repo` to purge media blobs from history if repo size is a concern

---

### 2026-04-23 (Thursday) — 2025 Tax Return Actuals + Lease v2
**Phase:** Active — Tax Reconciliation
**Duration:** ~1 hour
**Collaborators:** Ethan Kunz + Claude Code

#### Work Completed

**1. 2025 Tax Return Read (Meridian — filed 2026-02-04)**
   - Full Schedule E actuals extracted from PDF
   - Return filed by Kathryn R. Griffin, Meridian Tax & Accounting
   - Federal refund $5,665 | KS $275 | MO $281 | Total refund $6,221
   - Net rental income as filed: $1,393 (vs. $3,668 projected in Dec 2025 plan)
   - QBI deduction: $279 (Form 8995)

**2. config.yaml — 2025 Schedule E Actuals Applied**
   - 2025 return entry changed from "Projected" → "FILED 2026-02-04"
   - Deduction breakdown updated with actuals:
     - Repairs: $340 → $3,064 (flagged as +$2,724 discrepancy)
     - Property taxes: $3,674 → $3,628
     - Mortgage interest: $3,800 → $3,805
     - Depreciation: $5,768 → $7,433
     - Auto/travel: $0 → $68 (new line item)
     - Water heater DMSH $2,391 removed → absorbed into depreciation
     - Total: $18,712 → $20,762
   - Net income: $3,668 → $1,393; refunds and QBI added

**3. Depreciation Classifications Recorded (per Meridian filing)**
   - HVAC: 27.5yr SL MM, $441 yr1
   - Driveway: 10yr 200DB, $18,500 basis, $1,850 yr1
   - Water heater: 7yr 200DB, $342 yr1

**4. Lease v2 Created**
   - `docs/Archive/Reference/Leases/2026/lease_308_jamie_ct_4th_term_2026_v2.md`
   - Expanded from 20 → 33 sections
   - 13 missing clauses added: Jointly & Severally Liable, Mechanic's Liens, Subordination, Severability, Landlord's Contractual Lien (TX Property Code Ch. 54), Vacation Rental/STR Prohibition, Fair Housing, Attorney's Fees, Landlord Liability Limitation, Move-In Checklist, Disturbances/Quiet Hours, Remedies Cumulative, Binding Effect
   - 5 existing sections strengthened: deposit return timeline, renters insurance proof, holdover penalty, abandoned property, smoke/CO detector compliance
   - Revision block at top itemizes all changes from v1

**5. All Supporting Files Updated**
   - config.yaml: tax actuals, depreciation classifications, lease v2 in documents index
   - SUMMARY.md: Tax Status section rewritten with filed actuals; action items updated
   - STATUS.md: completion 75% → 80%; active items updated; milestones added
   - TECHNICAL_JOURNAL.md: this entry

#### Key Findings

1. **Net rental income $1,393** (gross $22,155 − deductions $20,762). Refund $6,221 total.
2. **2026 projected depreciation $9,157** — all four assets now in service and depreciating.

#### Files Modified

- config/config.yaml (2025 Schedule E actuals, depreciation corrections, lease v2 in index)
- SUMMARY.md (Tax Status section, maintenance table, action items)
- docs/active/STATUS.md (completion, active items, milestones, recent changes)
- docs/active/TECHNICAL_JOURNAL.md (this entry)
- docs/Archive/Reference/Leases/2026/lease_308_jamie_ct_4th_term_2026_v2.md (created)

#### Next Steps
1. Sign 4th-term lease v2 before May 1, 2026
2. File 2024 Form 1040-X (~$1,711 owed, overdue)
3. Define GEMINI.md domain mandates

---

### 2026-04-24 (Friday) — Lease Viewer + API Deployment
**Phase:** Active — Lease Viewer & Backend Live
**Duration:** ~2 hours
**Collaborators:** Ethan Kunz + Claude Code

#### Work Completed

**1. index.html — 4th-Term Lease Viewer (GitHub Pages)**
   - Built full "Notarial Modernism" lease viewer: Cormorant Garamond + EB Garamond + DM Sans, navy/ivory/teal/amber palette
   - 33 lease sections with visual NEW (teal, §21–§33) and UPDATED (amber, §4/§10/§13/§16/§17) treatments
   - "What Changed" banner (expanded by default): rent comparison table, 5 updated + 13 new clause lists
   - Key terms bar: $1,920 total, $1,880 base, $40 pet, $1,500 deposit, May 1 2026 start, $175 late fee
   - Scroll progress bar, sticky TOC with IntersectionObserver scroll-spy, print CSS for clean legal output
   - Acknowledgment form: POST to /lease-api/acknowledge with success state
   - Dynamic API fetch with 5s timeout + hardcoded fallback if API unreachable
   - Deployed to GitHub Pages: https://ee-edk.github.io/308-JamieCt-Longview/

**2. lease_api.py — FastAPI Backend (Port 8084)**
   - GET /lease-api/data — serves tenant-facing data from config.yaml (no financial/mortgage data exposed)
   - POST /lease-api/acknowledge — records acknowledgment to data/acknowledgments.json (gitignored)
   - GET /lease-api/status — acknowledgment log (owner-facing)
   - GET /lease-api/health — uptime check
   - CORS configured for ee-edk.github.io + Chrome Private Network Access preflight middleware
   - Deployed as `lease-308-api` systemd service, enabled + running

**3. Caddy Route Added (Self-Host)**
   - `/lease-api/*` → reverse_proxy 127.0.0.1:8084 added to Caddyfile
   - Validated, deployed, reloaded — public access via Tailscale Funnel confirmed

**4. Tenant Data Updates**
   - Kayla Geers new phone 903-746-9903 added to config.yaml (phone_jared/phone_kayla split)
   - Jared's acknowledgment recorded Apr 24 at 9:07 PM CT (text confirmation from landlord)
   - CLAUDE.md, dashboard.html updated: Kayla phone, ack status, lease viewer link

#### Key Technical Decisions

1. **API security boundary:** Only tenant-facing data (names, rent, dates) served publicly — PITI, mortgage balance, NOI, escrow stay config-only
2. **Acknowledgments gitignored:** data/ is excluded from repo per PII rules; JSON lives server-side only
3. **Fallback data hardcoded in JS:** API fetch uses AbortSignal.timeout(5000); Geers info pre-populated so page works even if API is down

#### Files Modified
- `index.html` (created) — GitHub Pages lease viewer
- `lease_api.py` (created) — FastAPI backend
- `config/config.yaml` — phone_kayla added, last_updated bumped to 2026-04-24, version 1.2.0
- `CLAUDE.md` — Kayla phone added to quick-facts + operating rule #6
- `dashboard.html` — Kayla phone, last updated date, alert banners, lease history badge
- `docs/active/TECHNICAL_JOURNAL.md` — this entry
- `docs/active/STATUS.md` — milestones updated
- Self-Host: `caddy/Caddyfile` — /lease-api/* route added

#### Commits Pushed
- `0bb6feb` feat: add 4th-term lease viewer (index.html) for GitHub Pages
- `3f71a52` feat: add lease-308-api FastAPI backend (port 8084)
- `f2e8d3e` feat(data): reconcile lease terms, maintenance history, and landlord info from source docs
- `2e1273f` chore: add Kayla Geers new phone (903-746-9903), split phone_jared/phone_kayla fields
- `1ee4709` docs: add Kayla phone 903-746-9903, update dashboard with Jared ack + lease viewer link
- Self-Host `11d3d6f` feat: add /lease-api/* route to Caddyfile → port 8084

#### Next Steps
1. Get formal Avail signature from Jared + Kayla before May 1, 2026
2. File 2024 Form 1040-X (~$1,711 owed, overdue)
3. HVAC labor warranty expiry — monitor (Jul 8, 2026)
