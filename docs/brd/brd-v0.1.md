# Business Requirements Document (BRD) — AI for Indian Satellites — v0.1 Draft

**Project:** AI for Indian Satellites — Earth Observation Pipeline (candidate: flood mapping / crop monitoring — to be finalized Day 2) | **Hat:** W2 Business Analyst | **Date:** 2026-09-05 | **Version:** v0.1 draft | **Owner:** Omprakash Suthar (OPBSUTHAR) — Christ University, Bangalore

## 1. Purpose
Document business needs for an AI solution that makes Indian satellite data more useful, scalable, and intelligent. This BRD defines why and what before how. Scope: one Earth observation use case evaluated through the Business Analyst lens.

## 2. Scope
- In scope:
  - Problem statement for one Indian satellite AI use case
  - Stakeholders and their needs
  - Business requirements prioritized by MoSCoW
  - Success metrics and constraints (data, compute, latency, cost)
  - Assumptions, dependencies, references
- Out of scope:
  - Technical design and model architecture (deferred to RLD/PRD)
  - Pipeline implementation and deployment
  - Topics outside Week 2 scheduled steps

## 3. Problem Statement (Draft — refine Day 2)
- Current state: ISRO provides rich Earth observation data via Bhuvan and MOSDAC (Cartosat, Resourcesat, RISAT, INSAT-3D/3DR, Oceansat). Use is limited by manual analysis, latency, and fragmented access.
- Pain points:
  - Delayed insights for time-sensitive events (e.g., floods, crop stress)
  - High manual effort to interpret imagery across large geographies
  - Stakeholder-specific needs (agriculture, disaster management, urban planning) not mapped to requirements
- Opportunity: An AI-assisted pipeline can reduce time-to-insight, improve coverage, and scale analysis while keeping humans in the loop. Framewirk micro-movements structure this as weekly tangible outputs.
- Evidence needed: Cite Bhuvan catalog coverage, MOSDAC latency, IN-SPACe private participation notes (to be added in §8 with access dates).

> Day 1 action: Pick one use case by end of Day 2. Recommendation: flood mapping (near-real-time value, INSAT + SAR data) or crop health monitoring (seasonal value, Resourcesat data). Record decision rationale here.

## 4. Stakeholders (Draft)
| Stakeholder | Role | Need | Priority |
|-------------|------|------|----------|
| ISRO / NRSC (Bhuvan), SAC (MOSDAC) | Data provider | Reliable, documented access to Indian satellite imagery and products | Must |
| IN-SPACe | Regulator / enabler | Framework for private and academic use of space data | Must |
| Farmers / Agriculture Dept / State disaster cells (end users) | Beneficiary | Timely, accurate, actionable insights in local context | Must |
| Christ University — Faculty Research | Institutional anchor | Link academic research to space-AI application; Long-Range Connection continuity | Should |
| Agnirva / Framewirk program | Delivery governance | Weekly artifacts (BRD), Clear Beats Fancy standard, micro-movement cadence | Must |
| Development team (next hats: RLD, VQRD, PRD) | Consumer of BRD | Clear, testable requirements to derive research and product decisions | Must |

## 5. Requirements (MoSCoW) — Draft (expand Day 2–3)
| ID | Requirement | Priority | Source |
|----|-------------|----------|--------|
| BR-01 | BRD defines one use case with problem, stakeholders, and metrics before design | Must | W2 Day 1 — BRD Concept Review |
| BR-02 | Requirements are testable and traceable to stakeholders | Must | BA role definition |
| BR-03 | Data sources limited to Indian satellite ecosystem (Bhuvan, MOSDAC) with citation and access date | Must | Track Focus |
| BR-04 | Success metrics include time-to-insight and coverage in addition to accuracy | Must | AI for Indian Satellites lens |
| BR-05 | Constraints (compute, latency, cost, data access tier) are documented explicitly | Must | W2 directive §5 |
| BR-06 | BRD versioned v0.1 → v0.5 → v1.0 via docs/brd/ | Should | Artifact standards (AGENTS.md §4.3) |
| BR-07 | AI augmentation noted as supporting BA judgment, not replacing it (ethics/bias note) | Should | How AI is Changing BA Role |
| BR-08 | Localization/accessibility considerations flagged for handoff to LAAP (W7) | Could | 6-hat framework |

## 6. Success Metrics & Constraints (Draft)
- Metrics:
  - Completeness: all 8 BRD sections filled with Clear Beats Fancy style
  - Traceability: each Must requirement links to a stakeholder and a metric
  - Citation: ≥3 authoritative sources (ISRO/Bhuvan/MOSDAC/IN-SPACe) with URL + access date
  - Review: v0.1 → v0.5 feedback incorporated; v1.0 approved by self-review against template
- Constraints:
  - Data access: Bhuvan open tiers vs. restricted products; MOSDAC dissemination policy
  - Compute: student-tier resources; note what is feasible vs. deferred
  - Latency: define target per use case (e.g., flood: hours; crop: days/weeks)
  - Time: BRD must complete within Week 2 cadence; do not expand scope beyond scheduled steps

## 7. Assumptions & Dependencies
- Assumes program links for Day 1 steps are completed in order via provided platform links.
- Depends on W1 orientation artifacts (AGENTS.md, progress log, Long-Range Connection note) as inputs.
- Depends on form submission being counted as contribution; button clicks alone are insufficient per Important notice.

## 8. References (to be completed with access dates)
- ISRO Bhuvan — https://bhuvan.nrsc.gov.in (accessed 2026-09-05)
- MOSDAC — https://www.mosdac.gov.in (accessed 2026-09-05)
- IN-SPACe — https://www.inspace.gov.in (accessed 2026-09-05)
- Christ University Research — https://christuniversity.in/research (accessed 2026-09-05)
- Framewirk / Agnirva internship notice board — Week 2 Day 1 (accessed 2026-09-05)

---
*Status: v0.1 draft initialized Day 1. Next: finalize use case, expand §5 MoSCoW to 10–12 items, quantify §6 metrics, and complete citations. Then paste this content into the program Deliverable form, submit, then click Complete Step → Complete All Steps for attendance.*
