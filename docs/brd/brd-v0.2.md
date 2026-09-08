# Business Requirements Document (BRD) — AI for Indian Satellites — v0.2 Draft (11 Sections)

**Project:** AI for Indian Satellites — Earth Observation Pipeline (candidate: flood mapping / crop monitoring — to be finalized Day 2) | **Hat:** W2 Business Analyst (Role Focus 1 of 6) | **Date:** 2026-09-05 | **Version:** v0.2 draft (11-section alignment) | **Owner:** Omprakash Suthar (OPBSUTHAR) — Christ University, Bangalore | **Friday Ship:** My First Analysis Note

> Previous version kept for history: `docs/brd/brd-v0.1.md` (8 sections). This version aligns to program-stated **eleven standard sections** from Week 2 Welcome. Days 1–4 build section by section; Day 5 final assembly.

## 1. Executive Summary
- Business need: Make Indian satellite data (ISRO Bhuvan, MOSDAC) more useful, scalable, and intelligent via an AI-assisted Earth observation pipeline.
- Approach: Business Analyst defines what exactly is the need and how we know it is addressed — before any design or build. This BRD is the foundation for W3–W7 (Landscape → Quality → Product → Audience → Language).
- Scope this week: One domain use case (flood mapping or crop monitoring to be finalized Day 2). Produce 30 artifact activities (6/day Mon–Fri), assembled Friday as My First Analysis Note.
- Success: Complete 11 sections, traceable requirements, cited sources, reviewed v0.2 → v0.5 → v1.0.

## 2. Business Objectives — 5 Testable Outcomes (Day 2 fill: MT7–MT12)
> Day 2 Step 1: Translate problem statement into 3–5 measurable, testable outcomes. Each must state what will be achieved, for whom, and how it is verified. Vague improvement language fails.

- O1 — Time-to-insight: Deliver validated district flood extent map within 3 hours of overpass, with tile lineage (Bhuvan/MOSDAC tile ID, acquisition time, sensor) attached. Verified by timestamp diff per tile.
- O2 — Coverage: Map ≥1000 km² per run from 2–3 tiles without hand digitization, CRS EPSG:4326 consistent. Verified by mosaic area calculation.
- O3 — Accuracy: Achieve IoU ≥0.65 against 10% hand-digitized validation sample, every polygon cites source URL + access date. Verified by sample comparison.
- O4 — Scope discipline: Keep V1 to one state / one monsoon window; log assumptions and out-of-scope items so later hats do not inherit creep. Verified by §4/§8 trace.
- O5 — Traceability: Every Must requirement links to a stakeholder in §5 and a metric in §10, with citations in §11. Verified by trace matrix review before v0.5.

## 3. Problem Statement
- Current state: ISRO provides rich Earth observation data via Bhuvan and MOSDAC (Cartosat, Resourcesat, RISAT, INSAT-3D/3DR, Oceansat). Use is limited by manual analysis, latency, and fragmented access.
- Pain points:
  - Delayed insights for time-sensitive events (floods, crop stress)
  - High manual effort to interpret imagery across large geographies
  - Stakeholder-specific needs (agriculture, disaster management, urban planning) not mapped to requirements
- Opportunity: AI-assisted pipeline reduces time-to-insight, improves coverage, scales analysis with humans in the loop. Framewirk micro-movements structure this as weekly tangible outputs.
- Evidence needed: Cite Bhuvan catalog coverage, MOSDAC latency, IN-SPACe private participation notes (to be added in §11 with access dates).
- Day 1 action: Pick one use case by end of Day 2. Recommendation: flood mapping (near-real-time value, INSAT + SAR data) or crop health monitoring (seasonal value, Resourcesat data). Record decision rationale here.
- BA lens trace: This section answers BA Q1 "What is the underlying need?" (gap behind request) — not solution phrasing. See `docs/w2-brd/step2-domain-project-ba-lens.md:4`.
- Step 4 satellite lens: Separate real need from broad AI excitement — need = where satellite workflow needs better speed/accuracy/scale/interpretation for a real user. See `docs/w2-brd/step4-ai-indian-satellites-ba-lens.md:4`. Must connect AI capability → real decision.

## 4. Scope
- In scope:
  - Problem statement for one Indian satellite AI use case
  - Stakeholders, objectives, scope, assumptions, risks, success metrics (the 7 items named in Welcome §01)
  - Business requirements prioritized by MoSCoW and traceable to stakeholders
  - References and glossary with citations (URL + access date)
- Out of scope:
  - Technical design, model architecture, and pipeline implementation (deferred to RLD/W3 and PRD/W5) — solution thinking held for W5 Product Analyst
  - Deployment and localization execution (W6–W7)
  - Topics outside Week 2 scheduled steps and the 30 artifact activities
- BA lens trace: This section answers BA Q4 "What is in scope, and what is not?" (defensible boundary) — see `docs/w2-brd/step2-domain-project-ba-lens.md:4`. Hold solution instinct.

## 5. Stakeholders & Personas — Catalog with Interest and Need (Day 2 fill: MT7–MT12, Step 2 BABOK)
> Day 2 Steps 1–2: Catalog every person/group with interest, what each cares about, and what each needs. Generic groups signal imprecise work; named groups with one-line need signal real work. Must cover 4 BABOK categories (IIBA) and 3 commonly missed groups. Maps to BRD §5 in Welcome 11-section structure.

| Stakeholder | BABOK Category | Role | Cares About (Interest) | Needs From This Work | Priority |
|-------------|----------------|------|------------------------|----------------------|----------|
| District disaster analyst — KSDMA / ASDMA (primary user, BRD1) | 02 End user/beneficiary | Decides evacuation & relief routing | Lives saved in <3h window, defensible map for briefing | Validated flood extent polygon with Bhuvan/MOSDAC lineage (tile ID, time, sensor) | Must |
| ISRO NRSC (Bhuvan) / SAC (MOSDAC) | 03 SME/contributor + 04 Adjacent | Data provider & provenance | Correct citation, proper use of open vs restricted tiers | Documentation of source tier, catalog link, access date per tile | Must |
| IN-SPACe | 04 Adjacent / regulatory | Regulator / enabler | Compliant private/academic use of space data | Framework reference showing V1 stays within permitted use | Must |
| IMD (weather context) | 03 SME/contributor | Adjacent data provider | Rainfall context for flood interpretation | Cited IMD input where used, not conflated with EO extent | Should |
| Christ University — Faculty Research | 01 Sponsor/decision-maker | Institutional anchor | Research linkage Long-Range Connection | Traceable BRD that connects academic rigor to space-AI application | Should |
| Agnirva / Framewirk program | 01 Sponsor/decision-maker | Delivery governance | Weekly artefacts, Clear Beats Fancy, micro-movement cadence | BRD v0.2 with 11 sections, 6 activities/day, attendance via Complete All Steps | Must |
| Agnirva Editorial & Publishing operation | Hidden — operational handler (§02) | Owner post-project | File format, metadata, citation conventions, accessibility tags | BRD anticipates handoff format, not just content | Must |
| MOSDAC/Bhuvan policy + DPDP Act 2023 | Hidden — regulatory (§02) | Policy constraint | What can be published/how | Out-of-scope note and evidence rule in §9/§11 compliance | Must |
| Paid map/intermediary providers | Hidden — negative stakeholder (§02) | Displaced by free validated map | Acknowledged, not pretended away; engagement deferred to W6 | Could |
| Downstream hats — RLD / VQRD / PRD owners | 01 Sponsor + 03 SME | Consumer of BRD | Clear, testable requirements to derive next artefacts | Requirements table (MoSCoW) with stakeholder + metric trace | Must |
| Citizen / regional language communities | 04 Adjacent/affected | Audience (W6–W7 handoff) | Accessible, localized insight (Kannada/Assamese) | Flag for SCRP/LAAP handoff, not built in V1 | Could |
- Day 2 trace: Generic "users/partners" replaced by named groups above. Each row now answers interest + need + priority — test of precise examination per Step 1 article. Four BABOK categories ticked (01–04 all represented); three hidden groups added per Step 2 §02 — see `docs/w2-brd/day2-stakeholders-objectives.md:4.2`.
- BA lens trace: This section answers BA Q2 "Who experiences that need?" (precision-named persons/orgs) — see `docs/w2-brd/step2-domain-project-ba-lens.md:4`.

## 6. Requirements (MoSCoW) — Draft (expand Day 2–3 to 10–12 items)
| ID | Requirement | Priority | Source | Traces to |
|----|-------------|----------|--------|-----------|
| BR-01 | BRD defines one use case with problem, stakeholders, and metrics before design | Must | W2 Day 1 — BRD Concept Review | §3, §5, §10 |
| BR-02 | Requirements are testable and traceable to stakeholders | Must | BA role definition | §5 |
| BR-03 | Data sources limited to Indian satellite ecosystem (Bhuvan, MOSDAC) with citation and access date | Must | Track Focus | §11 |
| BR-04 | Success metrics include time-to-insight and coverage in addition to accuracy — must map to satellite workflow improvement (speed/accuracy/scale/interpretation) | Must | AI for Indian Satellites lens (Step 4) | §10 |
| BR-05 | Constraints (compute, latency, cost, data access tier) are documented explicitly — separates real need from broad AI excitement | Must | W2 directive + Step 4 | §8 |
| BR-06 | BRD versioned v0.1 → v0.2 → v0.5 → v1.0 via docs/brd/ | Should | Artifact standards (AGENTS.md §4.3) | — |
| BR-07 | AI accelerates draft (stakeholder maps, risk register, requirement formulation, source discovery, consistency checks) — human BA judges and signs off | Should | How AI is Changing BA Role (Step 5 §01 — draft vs judge) | §7, §9 |
| BR-08 | Scope, missing stakeholder gaps, sign-off ownership, organisational reality — human judgment only (AI cannot replace) | Must | How AI is Changing BA Role (Step 5 §02 — cannot replace) | §4, §5, §7 |
| BR-09 | Localization/accessibility considerations flagged for handoff to LAAP (W7) | Could | 6-hat framework | §5 |

## 7. Assumptions — 7 Testable Bets (Day 3 MT14–MT15, Step 4 categories)
> Each assumption names condition, what changes if false, and how verified (testable). Naming bet doesn't change odds — changes whether you notice when wrong. See `docs/w2-brd/day3-scope-assumptions-constraints.md:4.4`.

| # | Assumption (treated as true) | Category | If False, Then | Verification |
|---|------------------------------|----------|----------------|--------------|
| A1 | KSDMA/ASDMA analyst has reliable internet and desktop to view GeoJSON/PDF within 3h | Audience | Fallback to static PNG + SMS summary; W6 SCRP adds offline path | Confirm via Agnirva stakeholder note Day 2 — not yet formally verified |
| A2 | Bhuvan open tiers + MOSDAC RISAT/Resourcesat via https://bhuvan.nrsc.gov.in / https://www.mosdac.gov.in remain accessible for student use in 2026 monsoon | Source | Scope shrinks to single sensor or sample tiles; requirements BR-03/BR-04 revised | Check catalog access before v0.5 (Perplexity verification) |
| A3 | Agnirva program team and editorial available Day 5 for BRD sign-off | Institutional | Sign-off deferred to next Monday; Week 3 starts against unsigned draft | Editorial calendar — testable |
| A4 | One flood use case (district extent, one state) sufficient for BRD depth; breadth deferred | Resource | Must split into narrower slice or extend timeline — scope re-cut | Framewirk 30-activity budget (6/day) |
| A5 | Agnirva Internship Assistant / Perplexity / Gemini available for draft and gap-check | Tool/resource | Revert to manual stakeholder gap check; longer draft time | Tool availability check Day 3 |
| A6 | Time boxed to 5 working days / 30 activities (MT13–MT18 Day 3); no external steps added | Timeline | Must defer scope items to Could/Won't; re-plan MT | Weekly cadence tracker |
| A7 | Form submission counts as contribution; button clicks alone insufficient | Institutional | Attendance marked invalid if only clicked | Program Important notice |

- BA method: Elicit → Document → Validate → Manage change (`docs/w2-brd/step3-what-is-a-business-analyst.md:5`). AI workflow: AI drafts → BA judges → human owns scope/sign-off (`docs/w2-brd/step5-how-ai-changing-ba-role.md:6`).

## 8. Constraints & Dependencies
- Constraints:
  - Data access: Bhuvan open tiers vs. restricted products; MOSDAC dissemination policy
  - Compute: student-tier resources; note feasible vs. deferred
  - Latency: target per use case (flood: hours; crop: days/weeks)
  - Time: 5 working days, 30 activities (6/day), Day 5 final assembly — do not expand scope
- Dependencies:
  - ISRO/IN-SPACe data availability and documentation
  - Weekly cadence: BRD → RLD → VQRD → PRD → SCRP → LAAP (pipeline dependency)

## 9. Risks & Mitigations — Risk Register (7 risks, Prob/Impact, Mitigation, Owner) (Day 3 MT16–MT17)
> Format per Infosys/TCS/Wipro: Risk — Prob — Impact — Mitigation. Read weekly: materialised? new? assumptions confirmed? See `docs/w2-brd/day3-scope-assumptions-constraints.md:4.4`. Each risk inverses an assumption in §7 where noted.

| # | Risk (plain language) | Prob | Impact | Mitigation | Owner | Inverses |
|---|------------------------|------|--------|------------|-------|----------|
| R1 | BHUVAN/MOSDAC tier unavailable or policy changes (DPDP Act) — A2 fails | Med | High | Use sample tiles + alternate source (IMD) and revise BR-03; identify backup catalog by Day 3 | BA | A2 |
| R2 | Audience has no reliable internet / needs offline (A1 fails) | Med | Med | Provide PNG fallback + SMS path; log for W6 SCRP | BA | A1 |
| R3 | Editorial not available Day 5 for sign-off — A3 fails | Med | Med | Secure backup reviewer by Day 3; start Week 3 against unsigned draft with risk note | BA | A3 |
| R4 | Scope creep — implementation/code added in W2 (Day 3 focus failure) | High | High | Enforce §4 In/Out; defer build to W5; AI lists candidates, human decides; holds test | BA | A4/A6 |
| R5 | Need definition too vague / AI draft left unjudged | Med | High | Human review every AI-drafted line before v0.5; SMART + 3 failure-mode check (Step 4) | BA | A5 |
| R6 | Data/quality assumption wrong — artefact fails W4 VQRD review | Med | High | Cite Bhuvan/MOSDAC with dates; validate catalog + IoU method before v0.5 | BA | A2 |
| R7 | Delayed attendance not marked / timeline overruns — A6/A7 fails | Med | Med | Submit Deliverable forms before Complete Step; track MT13–MT18 daily; Complete All Steps only after all steps done | Student/BA | A6/A7 |

## 10. Success Metrics (KPIs)
- Completeness: all 11 sections filled with Clear Beats Fancy style (sentences <20 words, active voice, bullets)
- Traceability: each Must requirement links to a stakeholder (§5) and a metric in this section
- Citation: ≥3 authoritative sources (ISRO/Bhuvan/MOSDAC/IN-SPACe) with URL + access date in §11
- Cadence: 30 activities tracked (6/day Mon–Fri), Day 1–4 builds, Day 5 assembly → My First Analysis Note
- Review: v0.2 → v0.5 feedback incorporated; v1.0 passes 11-section checklist and self-review
- BA lens trace: This section answers BA Q3 "What does success look like?" (specific observable outcome) — see `docs/w2-brd/step2-domain-project-ba-lens.md:4`. Must be observable, not vague.

## 11. References & Glossary
- ISRO Bhuvan — https://bhuvan.nrsc.gov.in (accessed 2026-09-05)
- MOSDAC — https://www.mosdac.gov.in (accessed 2026-09-05)
- IN-SPACe — https://www.inspace.gov.in (accessed 2026-09-05)
- Christ University Research — https://christuniversity.in/research (accessed 2026-09-05)
- Agnirva AI Internship — Week 2 Welcome: Business Analyst — Week 2 Day 1 Step 1 (accessed 2026-09-05)
- Agnirva AI Internship — Your Domain Project Through the Business Analyst Lens — Week 2 Day 1 Step 2 (accessed 2026-09-05, `docs/w2-brd/step2-domain-project-ba-lens.md`)
- Agnirva AI Internship — What is a Business Analyst? — Week 2 Day 1 Step 3 (accessed 2026-09-05, `docs/w2-brd/step3-what-is-a-business-analyst.md`)
- Agnirva AI Internship — AI for Indian Satellites Through the Business Analyst Lens — Week 2 Day 1 Step 4 (accessed 2026-09-05, `docs/w2-brd/step4-ai-indian-satellites-ba-lens.md`)
- Agnirva AI Internship — How AI is Changing the Business Analyst Role — Week 2 Day 1 Step 5 (accessed 2026-09-05, `docs/w2-brd/step5-how-ai-changing-ba-role.md`)
- Framewirk — micro-movement structure (orientation)
- Glossary:
  - BRD — Business Requirements Document (this artefact, W2)
  - RLD — Research Landscape Document (W3), VQRD — Validation & Quality Requirements (W4), PRD — Product Requirements (W5), SCRP — Stakeholder Communication & Reporting Plan (W6), LAAP — Localization & Accessibility Action Plan (W7)
   - MoSCoW — Must / Should / Could / Won't prioritization
   - IIBA / BABOK — International Institute of Business Analysis / Business Analysis Body of Knowledge (see Step 3 §7)
   - India Stack — UPI / Aadhaar / DigiLocker as BA-driven specifications

---
*Status: v0.2 draft aligned to 11 sections (Welcome). Next: finalize use case and expand §6 to 10–12 requirements, quantify §10 metrics, complete §11 citations. Then paste into program Deliverable form, submit, then Complete Step → Complete All Steps for attendance. Content from v0.1 preserved above; v0.1 kept as history.*
