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

## 7. Assumptions
- Program links for Day 1 steps are completed in order via provided platform links; no external steps are added.
- W1 orientation artifacts (AGENTS.md, progress log, Long-Range Connection note) are available as inputs.
- Form submission counts as contribution; button clicks alone are insufficient per Important notice.
- One use case is sufficient for BRD depth; breadth is deferred to later weeks.
- BA method: Elicit → Document → Validate (sign-off) → Manage change. See `docs/w2-brd/step3-what-is-a-business-analyst.md:5` — BA holds problem space open; cost of late fix grows exponentially.
- AI workflow: AI drafts → BA edits/judges → human owns scope and sign-off. See `docs/w2-brd/step5-how-ai-changing-ba-role.md:6` — AI cannot decide scope, detect missing stakeholder info, own sign-off, or navigate organisational reality.

## 8. Constraints & Dependencies
- Constraints:
  - Data access: Bhuvan open tiers vs. restricted products; MOSDAC dissemination policy
  - Compute: student-tier resources; note feasible vs. deferred
  - Latency: target per use case (flood: hours; crop: days/weeks)
  - Time: 5 working days, 30 activities (6/day), Day 5 final assembly — do not expand scope
- Dependencies:
  - ISRO/IN-SPACe data availability and documentation
  - Weekly cadence: BRD → RLD → VQRD → PRD → SCRP → LAAP (pipeline dependency)

## 9. Risks & Mitigations
| Risk | Impact | Mitigation | Owner |
|------|--------|------------|-------|
| Scope creep — adding implementation/code in W2 | BRD never finishes; later artefacts inherit gaps | Enforce out-of-scope §4; defer build to W5; AI lists candidates, human decides | BA |
| Need definition too vague (AI draft left unjudged) | Team misalignment (top failure cause per Welcome) | Require human review of every AI-drafted line before v0.5 — see Step 5 §03 rule | BA |
| AI draft accepted without judgment | Quiet documentation failure | Validate AI output: compare §6/§9 for vagueness/contradictions; check citations | BA |
| Data access assumption wrong | Invalid requirements | Cite Bhuvan/MOSDAC with dates; validate catalog before v0.5 | BA |
| Delayed attendance not marked | Evaluation record invalid | Submit Deliverable forms before clicking Complete Step / Complete All Steps | Student |

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
