# Business Requirements Document (BRD) — AI for Indian Satellites — v0.2 Draft (11 Sections)

**Project:** AI for Indian Satellites — Earth Observation Pipeline (candidate: flood mapping / crop monitoring — to be finalized Day 2) | **Hat:** W2 Business Analyst (Role Focus 1 of 6) | **Date:** 2026-09-05 | **Version:** v0.2 draft (11-section alignment) | **Owner:** Omprakash Suthar (OPBSUTHAR) — Christ University, Bangalore | **Friday Ship:** My First Analysis Note

> Previous version kept for history: `docs/brd/brd-v0.1.md` (8 sections). This version aligns to program-stated **eleven standard sections** from Week 2 Welcome. Days 1–4 build section by section; Day 5 final assembly.

## 1. Executive Summary
- Business need: Make Indian satellite data (ISRO Bhuvan, MOSDAC) more useful, scalable, and intelligent via an AI-assisted Earth observation pipeline.
- Approach: Business Analyst defines what exactly is the need and how we know it is addressed — before any design or build. This BRD is the foundation for W3–W7 (Landscape → Quality → Product → Audience → Language).
- Scope this week: One domain use case (flood mapping or crop monitoring to be finalized Day 2). Produce 30 artifact activities (6/day Mon–Fri), assembled Friday as My First Analysis Note.
- Success: Complete 11 sections, traceable requirements, cited sources, reviewed v0.2 → v0.5 → v1.0.

## 2. Business Objectives
- O1: Define the need precisely enough that the team aligns on what to build (avoid need-definition failure — the top cause of project failure per W2 Welcome).
- O2: Map objectives to measurable outcomes (time-to-insight, coverage, cost, accuracy) rather than vague improvement claims.
- O3: Establish scope, assumptions, risks, and constraints so later weeks (RLD, VQRD, PRD, SCRP, LAAP) have a coherent reference.
- O4: Keep work inside Week 2 scheduled steps; produce one professional artefact per day rhythm without scope creep.

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

## 5. Stakeholders & Personas
| Stakeholder | Role | Need | Priority |
|-------------|------|------|----------|
| ISRO / NRSC (Bhuvan), SAC (MOSDAC) | Data provider | Reliable, documented access to Indian satellite imagery and products | Must |
| IN-SPACe | Regulator / enabler | Framework for private and academic use of space data | Must |
| Farmers / Agriculture Dept / State disaster cells (end users) | Beneficiary | Timely, accurate, actionable insights in local context | Must |
| Christ University — Faculty Research | Institutional anchor | Link academic research to space-AI application; Long-Range Connection continuity | Should |
| Agnirva / Framewirk program | Delivery governance | Weekly artefacts (BRD), Clear Beats Fancy standard, micro-movement cadence | Must |
| Development team (next hats: RLD, VQRD, PRD) | Consumer of BRD | Clear, testable requirements to derive research and product decisions | Must |
| Citizen / public audience (W6–W7 handoff) | Audience | Accessible, localized insight delivery | Could |
- BA lens trace: This section answers BA Q2 "Who experiences that need?" (precision-named persons/orgs) — see `docs/w2-brd/step2-domain-project-ba-lens.md:4`.

## 6. Requirements (MoSCoW) — Draft (expand Day 2–3 to 10–12 items)
| ID | Requirement | Priority | Source | Traces to |
|----|-------------|----------|--------|-----------|
| BR-01 | BRD defines one use case with problem, stakeholders, and metrics before design | Must | W2 Day 1 — BRD Concept Review | §3, §5, §10 |
| BR-02 | Requirements are testable and traceable to stakeholders | Must | BA role definition | §5 |
| BR-03 | Data sources limited to Indian satellite ecosystem (Bhuvan, MOSDAC) with citation and access date | Must | Track Focus | §11 |
| BR-04 | Success metrics include time-to-insight and coverage in addition to accuracy | Must | AI for Indian Satellites lens | §10 |
| BR-05 | Constraints (compute, latency, cost, data access tier) are documented explicitly | Must | W2 directive | §8 |
| BR-06 | BRD versioned v0.1 → v0.2 → v0.5 → v1.0 via docs/brd/ | Should | Artifact standards (AGENTS.md §4.3) | — |
| BR-07 | AI augmentation noted as supporting BA judgment, not replacing it (ethics/bias note) | Should | How AI is Changing BA Role | §7, §9 |
| BR-08 | Localization/accessibility considerations flagged for handoff to LAAP (W7) | Could | 6-hat framework | §5 |

## 7. Assumptions
- Program links for Day 1 steps are completed in order via provided platform links; no external steps are added.
- W1 orientation artifacts (AGENTS.md, progress log, Long-Range Connection note) are available as inputs.
- Form submission counts as contribution; button clicks alone are insufficient per Important notice.
- One use case is sufficient for BRD depth; breadth is deferred to later weeks.

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
| Scope creep — adding implementation/code in W2 | BRD never finishes; later artefacts inherit gaps | Enforce out-of-scope §4; defer build to W5 | BA |
| Need definition too vague | Team misalignment (top failure cause per Welcome) | Use 11-section traceability; each Must maps to metric in §10 | BA |
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
- Framewirk — micro-movement structure (orientation)
- Glossary:
  - BRD — Business Requirements Document (this artefact, W2)
  - RLD — Research Landscape Document (W3), VQRD — Validation & Quality Requirements (W4), PRD — Product Requirements (W5), SCRP — Stakeholder Communication & Reporting Plan (W6), LAAP — Localization & Accessibility Action Plan (W7)
  - MoSCoW — Must / Should / Could / Won't prioritization

---
*Status: v0.2 draft aligned to 11 sections (Welcome). Next: finalize use case and expand §6 to 10–12 requirements, quantify §10 metrics, complete §11 citations. Then paste into program Deliverable form, submit, then Complete Step → Complete All Steps for attendance. Content from v0.1 preserved above; v0.1 kept as history.*
