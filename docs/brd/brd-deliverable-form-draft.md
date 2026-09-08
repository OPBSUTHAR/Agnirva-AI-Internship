# BRD Portfolio Document — Deliverable Draft (Form-Ready, Meets Minimums)

**Week:** W2 Day 1 Step 7 | **Hat:** Business Analyst | **Track:** AI for Indian Satellites | **Date:** 2026-09-05 | **Owner:** Omprakash Suthar (OPBSUTHAR) — Christ University, Bangalore | **Version:** Deliverable draft — single source of truth (consolidated 2026-09-08, meets all minimums)
**Purpose:** Copy-ready paragraphs for official BRD manual submission form (BRD 1–8). BRD 1/2/3/5/6/8 now meet 80/90/120 minimums; BRD 4 needs + BRD 7 measures kept in structured form as requested, each within 40–60w guidance.

> Note: Consolidated to one draft after duplicate cleanup. Previous `brd-deliverable-form-short.md` removed. BRD4 and BRD7 retain structured fields (module/need/reference and what/why/good) per your last request.

---

## Student Record — Fill With Your Agnirva Identity

- Application ID / Student ID: [your Agnirva ID]
- Email used for Agnirva: [your registered email]
- First name: Omprakash | Last name: Suthar | College: Christ University, Bangalore | State: Karnataka
- Branch / discipline: [your branch, e.g., Computer Science / AI] | Internship track: **AI for Indian Satellites**

---

BRD 1 Primary User (98w — meets 80 minimum)
Primary user is district disaster analyst in Karnataka State Disaster Management Authority and Assam SDMA during monsoon, responsible for daily flood extent assessment. They monitor 500 to 2000 square kilometers using ISRO Resourcesat-2 and 2A LISS-3 optical and RISAT-1A SAR data accessed via Bhuvan and MOSDAC, coordinate field response teams, and brief senior officials in English while field inputs are in Kannada or Assamese. Their core task is to produce a validated district flood extent map within three hours of satellite overpass to decide evacuations, relief routing and dam advisories, because delays directly risk lives and district budgets.

BRD 2 Problem (98w — meets 90 minimum)
Today analysts manually interpret optical and SAR imagery from Bhuvan and MOSDAC, digitizing flood boundaries tile by tile. The process is slow, interpreter-dependent and lacks traceable lineage, so maps take six to twelve hours and cannot be repeated daily across 1000 plus square kilometers. During monsoon this delay risks late evacuations and misallocated relief. Without visible source citations and validated accuracy, senior officials do not trust outputs and revert to ground reports alone. The problem is therefore not lack of satellites, but lack of fast, source-backed, observable mapping that fits the three-hour operational decision window at district scale.

BRD 3 Insight (95w — meets 90 minimum)
Week 2 manual taught the Business Analyst lens: four questions need, who, success and boundaries must come before technology, otherwise teams build off-target systems and pay exponential rework. The 11-section BRD enforces that discipline. Step 5 showed AI drafts stakeholder maps and requirements quickly, but cannot replace scope decisions, missing-need detection or sign-off. Bhuvan and MOSDAC are authoritative for Indian EO data including Resourcesat, RISAT and INSAT-3D, IMD for weather, India Stack for specification discipline. This BRD ties every requirement and metric to a named source with access date and separates fact, interpretation and judgment.

## BRD 4 — Version 1 Requirements (Three Must-Haves)

### Requirement 1
- **Module / capability name:** Source-Backed Flood Extent Map (Bhuvan/MOSDAC lineage viewer)
- **User need it solves (52w):** The analyst needs a same-day flood map with visible source lineage, not a black box. This module ingests one Bhuvan/MOSDAC product per run, produces a district polygon with tile ID, sensor and acquisition time, so the analyst can validate and brief within three hours without manual digitization. Without lineage, officials reject it.
- **Reference or source inspiration:** ISRO Bhuvan (NRSC) and MOSDAC (SAC) — RISAT-1A SAR, Resourcesat LISS-3 (accessed 2026-09-05) — https://bhuvan.nrsc.gov.in / https://www.mosdac.gov.in

### Requirement 2
- **Module / capability name:** Observable Decision Metric Dashboard (Time-to-Insight, Coverage, Accuracy)
- **User need it solves (42w):** The analyst needs observable success, not vague better AI. This dashboard records time from overpass to map, area covered and IoU accuracy against hand-digitized samples, so the analyst can report 2.5 hours, 1200 km2, IoU 0.68 for sign-off and compare districts consistently.
- **Reference or source inspiration:** Agnirva track instruction — 11-section BRD Success Metrics and Step 2 BA lens (Q3 observable outcome); IIBA BABOK guidance on testable requirements

### Requirement 3
- **Module / capability name:** Scoped Change & Trust Register (Scope, Assumptions, Evidence Rule)
- **User need it solves (42w):** The analyst works within strict boundaries and needs scope discipline. This register documents in-scope single-state flood mapping versus out-of-scope items, lists assumptions and enforces an evidence rule separating fact, interpretation and judgment, so stakeholders see limits upfront and reviewers trace every claim.
- **Reference or source inspiration:** ISRO MOSDAC dissemination policy and Bhuvan catalog documentation; India Stack pattern — every interface traces to documented requirement (Step 3 context)

BRD 5 Out of Scope (106w — meets 80 minimum)
Version 1 explicitly excludes four areas to protect feasibility within thirty activities and one state focus. One, real-time rescue routing or resource allocation, which requires field logistics beyond mapping. Two, multi-state or multi-hazard expansion into drought, crop stress or urban change, which would dilute validation and inherit gaps across artefacts. Three, model training pipelines, deployment infrastructure or mobile apps, which belong to research and product hats, not the business requirements hat. Four, automated Kannada and Assamese field alerts, which belong to Week 7 localization and accessibility work. These deferrals keep time-to-insight measurable, prevent exponential late rework and keep promises aligned to available Bhuvan and MOSDAC evidence.

BRD 6 Trust Rule (120w — meets 80 minimum)
Evidence rule: every factual claim about satellite, sensor, product, coverage or processing latency must cite a source with URL and access date; every interpretation must be labeled interpretation with method noted; every student judgment about scope or priority must be labeled judgment with assumptions stated. Claims that require citations include ISRO mission specifications, Bhuvan and MOSDAC catalog entries, IMD weather inputs and any accuracy or latency numbers. Prohibited are unsourced superlatives such as best model, unverified promises of national coverage and model performance without a hand-digitized validation sample. This separation of fact, interpretation and judgment lets reviewers and later W3 to W7 owners trace, verify and sign off without confusion, while enforcing human ownership of scope as Step 5 requires.

## BRD 7 — Success Measures

### Success Measure 1 (46w combined)
- **What will be measured?** Time-to-insight from satellite overpass to validated district flood map delivered.
- **Why does it matter?** Proves speed value for evacuation decisions; without fast insight, accuracy is irrelevant in monsoon windows and BA opportunity is unmet.
- **Good result / acceptance signal:** Median delivery within three hours, with acquisition and delivery timestamps logged per tile and lineage attached.

### Success Measure 2 (46w combined)
- **What will be measured?** Coverage and consistency of flood mapping across standard area per run.
- **Why does it matter?** Proves scale; manual digitization cannot repeatably cover 1000 plus km2 daily, and tests one-state repeatability.
- **Good result / acceptance signal:** At least 1000 km2 per run from 2-3 tiles mosaicked without hand digitization, CRS consistent and reproducible across two overpasses.

### Success Measure 3 (42w combined)
- **What will be measured?** Accuracy and source-aware credibility of extent polygons.
- **Why does it matter?** Proves trust; without validated accuracy and citations, officials reject automation and human judgment is unproven.
- **Good result / acceptance signal:** IoU at least 0.65 against 10 percent hand-digitized sample, every polygon cites Bhuvan/MOSDAC URL plus date, fact versus interpretation labeled.

BRD 8 Summary (123w — meets 120 minimum)
This BRD serves district disaster analysts in Karnataka and Assam who must deliver a validated flood extent map within three hours of an ISRO overpass for evacuation decisions. Manual Bhuvan and MOSDAC interpretation is too slow, not repeatably scalable across 1000 plus square kilometers and not traceable for official use. Version 1 delivers a source-backed flood map with lineage, a metric dashboard for time, coverage and IoU, and a trust register fixing boundaries and evidence rules. Out-of-scope logistics, multi-hazard expansion, model deployment and localization are deferred to later hats. Trust requires URL plus date citations and labeled fact versus interpretation, with human sign-off. Success is median three-hour delivery over 1000 square kilometers at IoU 0.65 with lineage, providing foundation for W3 to W7.

---

## References

- ISRO Bhuvan — https://bhuvan.nrsc.gov.in (accessed 2026-09-05)
- MOSDAC — https://www.mosdac.gov.in (accessed 2026-09-05)
- IMD — https://mausam.imd.gov.in (accessed 2026-09-05)
- Agnirva Week 2 Welcome + Steps 2–6 — `docs/w2-brd/` | IIBA BABOK, India Stack (Step 3 context)

*Maps to 11-section BRD: BRD1→§5, BRD2→§3, BRD3→§11, BRD4→§6, BRD5→§4/§8, BRD6→§9/§11, BRD7→§10, BRD8→§1/§2.*
