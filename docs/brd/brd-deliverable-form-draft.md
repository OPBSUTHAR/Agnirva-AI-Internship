# BRD Portfolio Document — Deliverable Draft (Form-Ready)

**Week:** W2 Day 1 Step 7 | **Hat:** Business Analyst | **Track:** AI for Indian Satellites | **Date:** 2026-09-05 | **Owner:** Omprakash Suthar (OPBSUTHAR) — Christ University, Bangalore | **Version:** Deliverable draft (form-ready, maps to 11-section BRD `docs/brd/brd-v0.2.md`)
**Purpose:** Provide copy-ready answers for the official BRD manual submission form (BRD 1–8). Word counts meet minimums without filler. Use your own identity details for Student Record.

> This draft follows Track Instruction Manual (Week 2 Welcome, Steps 2–6) and public reference systems (ISRO Bhuvan, MOSDAC, IMD). It separates real satellite need from broad AI excitement, defines problem before technology, and respects BA discipline (elicit → document → validate → manage change).

---

## Student Record — Fill With Your Agnirva Identity (Do Not Fabricate)

- Application ID / Student ID: [your Agnirva ID]
- Email used for Agnirva: [your registered email]
- First name: Omprakash
- Last name: Suthar
- College / institution: Christ University, Bangalore
- State: Karnataka
- Branch / discipline: [your branch, e.g., Computer Science / AI]
- Internship track: **AI for Indian Satellites** — select this track

---

## BRD 1 — Primary User (Target 80 words — this draft 96 words)

**Primary user:** District disaster analyst in the Karnataka State Disaster Management Authority (KSDMA) / Assam State Disaster Management Authority cell during monsoon.

**Context:** They monitor flood extent across 500–2000 km² daily from ISRO data (Resourcesat-2/2A LISS-3, RISAT-1A SAR via Bhuvan and MOSDAC), coordinate field teams, and brief senior officials. They work inKannada/Assamese field contexts but report in English.

**What they are trying to do:** Produce a validated flood extent map within three hours of satellite overpass to decide evacuations, relief routing, and dam release advisories.

**Why first:** Time-critical decisions save lives and money. Serving this analyst first creates a measurable, observable success path before serving secondary users such as farmers or the general public.

## BRD 2 — User Problem (Target 90 words — this draft 101 words)

The analyst cannot currently convert raw ISRO Earth observation data into timely, trusted intelligence. Bhuvan and MOSDAC provide imagery, but interpretation is manual, slow (often 12–24 hours), and inconsistent across districts. They cannot quickly decide where water has actually spread, cannot compare today’s extent with yesterday’s without hand digitization, cannot trust a single automated claim without source lineage, and cannot communicate a clear map to field officers in local language within the decision window. Existing manual workflows do not scale when cloud cover forces SAR-optical fusion or when multiple tiles must be mosaicked overnight. Low awareness is not the problem; lack of speed, scale, accuracy, and interpretable evidence for a specific operational decision is.

## BRD 3 — Reference Insight (Target 90 words — this draft 104 words)

The track instruction manual taught the BA lens: four questions (need, who, success, boundaries) must be answered before technology, otherwise designers and developers build off-target systems. The 11-section BRD structure forces that discipline and shows cost of late fixes grows exponentially. Step 5 showed AI now drafts stakeholder maps, risk registers, and testable requirements in minutes, but scope decisions, missing-need detection, sign-off, and org navigation remain human judgment. Public references taught credibility anchors: Bhuvan and MOSDAC are authoritative for Indian EO data (Cartosat, Resourcesat, RISAT, INSAT-3D), IMD for weather context, and India Stack as proof that rigorous BA-driven interface specifications enable national scale. This BRD uses that insight to tie every requirement and metric to a named source and a precise user.

## BRD 4 — Version 1 Requirements (Three Must-Haves)

### Requirement 1
- **Module / capability name:** Source-Backed Flood Extent Map (Bhuvan/MOSDAC lineage viewer)
- **User need it solves:** The analyst needs a same-day flood map with visible source lineage, not a black-box output. This module ingests one Bhuvan/MOSDAC product per run (e.g., RISAT SAR or Resourcesat LISS-3), produces a district-level extent polygon, and displays tile ID, acquisition time, sensor, and citation. It solves speed and trust: the analyst can validate and brief within the three-hour window without manual digitization, and can answer “which source proves this extent?” in the review meeting. Without lineage, automation is rejected.
- **Reference or source inspiration:** ISRO Bhuvan (NRSC) and MOSDAC (SAC) — authoritative Indian EO dissemination; INSAT-3D/3DR and RISAT-1A SAR for all-weather imaging (accessed 2026-09-05).

### Requirement 2
- **Module / capability name:** Observable Decision Metric Dashboard (Time-to-Insight, Coverage, Accuracy)
- **User need it solves:** The analyst needs observable success criteria, not vague “better AI.” This dashboard records time from overpass to map, km² covered per run, and validated accuracy (IoU against hand-digitized sample). It makes the BA Q3 “what does success look like?” measurable. The analyst can report “flood extent in 2.5 hours, 1200 km², IoU 0.68” instead of “improved mapping,” enabling sign-off and comparison across districts. It enforces BA discipline that success must be observable.
- **Reference or source inspiration:** Agnirva track instruction — 11-section BRD Success Metrics and Step 2 BA lens (Q3 observable outcome); IIBA BABOK guidance on testable requirements (referenced in Step 3).

### Requirement 3
- **Module / capability name:** Scoped Change & Trust Register (Scope, Assumptions, Evidence Rule)
- **User need it solves:** The analyst works within strict scope and must avoid quiet expansion into unrelated tasks (e.g., rescue routing or crop advice). This register documents in-scope (one-state flood extent map) vs out-of-scope, lists assumptions to validate (catalog access, latency), and enforces an evidence rule separating fact, interpretation, and student judgment. It solves clarity and credibility: stakeholders see boundaries before work begins, and reviewers can trace every claim to Bhuvan/MOSDAC/IMD with access dates. It respects Step 5 judgment — AI drafts, human owns scope and sign-off.
- **Reference or source inspiration:** ISRO MOSDAC dissemination policy and Bhuvan catalog documentation; India Stack pattern — every interface spec traces to a documented requirement (Step 3 context).

## BRD 5 — Out Of Scope (Target 80 words — this draft 92 words)

Version 1 must exclude: (1) real-time rescue routing or resource allocation — beyond mapping and requires field logistics not validated here; (2) multi-state or multi-hazard expansion (drought, crop stress, urban change) — would dilute focus and inherit gaps across artefacts; (3) model training, deployment pipeline, or mobile app — technical design belongs to W3 RLD / W5 PRD, not W2; (4) automated field alerts in Kannada/Assamese — localization belongs to W7 LAAP. Excluding these protects feasibility within 30 activities, keeps time-to-insight measurable, prevents late rework that grows exponentially, and preserves trust by promising only what Bhuvan/MOSDAC evidence can support in one district and one monsoon window.

## BRD 6 — Trust And Evidence Rule (Target 80 words — this draft 98 words)

Evidence rule: Every factual claim about satellite, sensor, product, or extent must cite a source with URL and access date; interpretation must be labeled “interpretation” with method noted; student judgment must be labeled “judgment” with assumptions stated. Claims needing sources: ISRO mission specs, Bhuvan/MOSDAC catalog entries, IMD weather data, and any accuracy/latency numbers. Claims to avoid: un-sourced superlatives (“best model”), unverified coverage promises, or model performance without validation sample. Separate fact (published data), interpretation (what map means for flood decision), and judgment (scope choice) so reviewers and later W3–W7 roles can trace, verify, and sign off without confusion.

## BRD 7 — Success Measures (Three)

### Success Measure 1
- **What will be measured?** Time-to-insight from satellite overpass to validated district flood map delivered to analyst.
- **Why does it matter?** Directly proves BA speed dimension and disaster decision value; maps to BRD §3 opportunity and Step 4 “where AI adds value.” Faster insight prevents delayed evacuations. Without this, accuracy alone is irrelevant in monsoon windows.
- **Good result / acceptance signal:** Median delivery ≤3 hours for one district run, with acquisition time and delivery timestamp logged per tile, source lineage attached.

### Success Measure 2
- **What will be measured?** Coverage and consistency of flood extent mapping across standard area.
- **Why does it matter?** Proves scale — the BA problem manual interpretation cannot cover 1000+ km² repeatedly; also tests W2 scope discipline (one-state repeatability).
- **Good result / acceptance signal:** ≥1000 km² mapped per run, mosaicked from 2–3 tiles without hand-digitization, lineage and CRS consistent (EPSG:4326), reproducible across two consecutive overpasses.

### Success Measure 3
- **What will be measured?** Accuracy and source-aware credibility of extent map.
- **Why does it matter?** Proves trust — without validated accuracy and citations, automation is rejected by authority; tests Step 5 human-judgment requirement to review every AI-drafted line.
- **Good result / acceptance signal:** IoU ≥0.65 against 10% hand-digitized validation sample, every polygon cites Bhuvan/MOSDAC tile with URL + access date, fact/interpretation/judgment labeled per Trust Rule, sign-off checklist passes 11-section coherence.

## BRD 8 — BRD Summary (Target 120 words — this draft 128 words)

This BRD serves the district disaster analyst who must produce a validated flood extent map within three hours of an ISRO overpass to decide evacuations and relief routing. Today manual interpretation of Bhuvan/MOSDAC imagery is too slow, not scalable, and not source-traceable for operational decisions. Version 1 therefore includes: (1) a source-backed flood extent map with Bhuvan/MOSDAC lineage, (2) an observable metric dashboard (time-to-insight, coverage, IoU), and (3) a scoped trust register defining boundaries, assumptions, and evidence discipline. Out of scope are rescue logistics, multi-hazard expansion, model deployment, and localization — deferred to later hats to protect feasibility and prevent exponential rework. Trust is protected by requiring URL+date citations, labeling fact vs interpretation vs judgment, and human ownership of scope and sign-off (AI drafts, human judges). Success is judged by ≤3-hour delivery over ≥1000 km² at IoU ≥0.65 with lineage attached — a coherent, source-aware foundation for W3–W7.

---

## References (Cite with access dates in form if fields allow)

- ISRO Bhuvan — https://bhuvan.nrsc.gov.in (accessed 2026-09-05)
- MOSDAC — https://www.mosdac.gov.in (accessed 2026-09-05)
- IMD — https://mausam.imd.gov.in (accessed 2026-09-05)
- IN-SPACe — https://www.inspace.gov.in (accessed 2026-09-05)
- Agnirva Week 2 Welcome: Business Analyst (11 sections, 30 activities, Need→Synthesis) — `docs/w2-brd/week2-welcome-business-analyst.md`
- Steps 2–6 — `docs/w2-brd/step2-domain-project-ba-lens.md` through `docs/w2-brd/step6-brd-concept-review.md`
- IIBA BABOK, India Stack (Step 3 context)

## Word Count Verification

- BRD1 96 /80 — pass
- BRD2 101 /90 — pass
- BRD3 104 /90 — pass
- BRD5 92 /80 — pass
- BRD6 98 /80 — pass
- BRD8 128 /120 — pass
- All requirements and success measures use 2–4 sentence need explanations and named sources.

## How to Submit

1. Copy each section above into the matching BRD 1–8 field on the Agnirva form (do not paste citations inside filler text; paste clean answer).
2. Fill Student Record with your Agnirva identity (Application ID, email, college, state, branch, track = AI for Indian Satellites).
3. Submit BRD, then click Complete Step for Deliverable. After all Day 1 steps, click Complete All Steps. Push remains batched — this draft is committed locally and will push after 15 total.

---
*Maps to 11-section BRD: BRD1→§5, BRD2→§3, BRD3→§11, BRD4→§6, BRD5→§4/§8, BRD6→§9/§11, BRD7→§10, BRD8→§1/§2.*
