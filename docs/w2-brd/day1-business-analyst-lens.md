# W2 Day 1 — Business Analyst Lens — AI for Indian Satellites

**Week:** W2 Day 1 | **Hat:** Business Analyst | **Date:** 2026-09-05 | **Owner:** Omprakash Suthar (OPBSUTHAR) | **Track:** AI for Indian Satellites

## 1. Purpose
Complete Week 2 Welcome and Day 1 scheduled steps through the Business Analyst lens. Build foundation for BRD deliverable.

## 2. Scope
- In: 7 scheduled program steps for Day 1 (listed in §4).
- Out: Full BRD draft (starts Day 1, completes through Week 2). No code/pipeline build yet.

## 3. Key Outputs
- This Day 1 note — `docs/w2-brd/day1-business-analyst-lens.md`
- BRD scaffold — `docs/brd/brd-v0.1.md` (initialized today, iterated through Week 2)
- Updated progress — `docs/progress-log.md`

## 4. Today's Scheduled Steps (Complete All 7 Before Clicking Complete All Steps)

> Rule from Notice Board: Stay inside scheduled program steps; links are already provided. After finishing all steps, click **Complete All Steps** to mark attendance. For any step prefixed **Deliverable**, fill the form content, submit it, then click Complete Step. Clicking without form submission may invalidate evaluation. Delayed attendance may be noted.

### 4.1 Week 2 Welcome: Business Analyst
- **Transition:** W1 Orientation (Days 1–5) → W2 Business Analyst.
- **Goal this week:** Produce Business Requirements Document (BRD) for one AI-for-Indian-Satellites use case.
- **Framewirk rhythm:** Micro-movements → tangible output each day. Today = conceptual lens + BRD start.
- **Success rule:** Clear Beats Fancy throughout. Active voice, bullets, evidence.

### 4.2 Your Domain Project Through the Business Analyst Lens
- **Project context:** AI for Indian Satellites.
- **BA lens question:** What business problem does satellite AI solve, for whom, with what constraints?
- **Focus from Track:** Satellite imagery analysis, Earth observation pipelines, autonomous systems.
- **Candidate use cases to evaluate for BRD (pick ONE in BRD §3):**
  - Crop health / yield estimation (Resourcesat / RISAT + Bhuvan)
  - Flood mapping and early warning (INSAT-3D/3DR + MOSDAC)
  - Urban land-use change detection (Cartosat series)
  - Deforestation / coastal monitoring
- **BA filter:** Prioritize by stakeholder need + data availability + feasibility. Document choice rationale.

### 4.3 What is a Business Analyst?
- **Role:** Bridge between stakeholders and solution. Elicits, analyzes, validates, documents requirements.
- **Core duties:**
  - Define problem and stakeholders
  - Elicit requirements (interviews, observation, docs)
  - Prioritize (MoSCoW: Must / Should / Could / Won't)
  - Define metrics and constraints
  - Prevent scope creep via traceability
- **Artifacts:** BRD (this week) → later feeds PRD, VQRD, backlog.
- **Mindset:** Ask why before what before how.

### 4.4 AI for Indian Satellites Through the Business Analyst Lens
- **Ecosystem to reference in BRD:**
  - ISRO satellites: Cartosat, Resourcesat, RISAT, INSAT-3D/3DR, Oceansat — via Bhuvan and MOSDAC.
  - IN-SPACe: private participation framework.
  - NITI Aayog / Ministries: agriculture, disaster management use cases.
- **BA questions for this domain:**
  - Which satellite data is open vs. restricted? (Bhuvan catalog, MOSDAC dissemination policy)
  - What latency is acceptable? (Near-real-time for floods vs. weekly for crop)
  - What compute/storage is realistic for a student/Business Analyst prototype vs. production?
  - What existing pipelines exist that AI should augment, not replace?
- **Value lens:** Useful, scalable, intelligent — measure each.

### 4.5 How AI is Changing the Business Analyst Role
- **Before AI:** Manual elicitation, static diagrams, slow validation.
- **With AI:**
  - Faster need discovery (synthesis of stakeholder notes, imagery metadata).
  - Automated traceability (requirement → metric → test).
  - Assisted prioritization and impact analysis.
  - BA remains accountable for judgment, ethics, and stakeholder alignment — AI augments, does not replace.
- **Implication for BRD:** Include AI-assisted workflows as requirements where they save time or improve accuracy. Also note risks: bias, hallucination, data drift.

### 4.6 BRD Concept Review
- **BRD purpose:** Single source of business truth before design/build. Answers why and what.
- **BRD vs PRD:** BRD = business needs and constraints. PRD = product features derived from BRD.
- **Structure (used in `docs/brd/brd-v0.1.md`):**
  1. Purpose → 2. Scope → 3. Problem Statement → 4. Stakeholders → 5. Requirements (MoSCoW) → 6. Success Metrics & Constraints → 7. Assumptions & Dependencies → 8. References
- **Versioning:** v0.1 draft (Day 1–2) → v0.5 review (mid-week) → v1.0 final (end of Week 2).
- **Quality bar:** Every requirement testable. Every claim cited (ISRO, IN-SPACe, Bhuvan, MOSDAC + date accessed).

### 4.7 Week 2 Deliverable: Build Your BRD — Action for Day 1
- **Deliverable type:** Form / submission step. Today you start it; you complete it through Week 2.
- **Day 1 actions:**
  1. Create scaffold `docs/brd/brd-v0.1.md` from template.
  2. Fill §1 Purpose, §2 Scope, §3 Problem Statement (draft), §4 Stakeholders (draft list) now.
  3. Copy same content into the program's Deliverable form, submit, then click Complete Step for that deliverable item.
  4. Click **Complete All Steps** only after all 7 steps show complete. Attendance delay is noted per Important notice.
- **What counts:** Form submission, not just button click. Skipping form may invalidate evaluation record.

## 5. Attendance & Deliverable Checklist — Do Today

- [ ] Completed all 7 steps via provided links (do not go outside scheduled steps)
- [ ] For Deliverable steps: filled form content and submitted, then clicked Complete Step
- [ ] Clicked **Complete All Steps** to mark attendance for Day 1
- [ ] Initialized `docs/brd/brd-v0.1.md` §1–§4 (draft)
- [ ] Pushed progress to GitHub repo (this file + BRD scaffold)

## 6. Method
- Followed notice board focus exactly. No extra program steps.
- Documented per Clear Beats Fancy and AGENTS.md §4.1.

## 7. References
- Agnirva AI Internship — Notice Board — Week 2 Day 1 (accessed 2026-09-05)
- Framewirk — micro-movement structure (program orientation)
- ISRO Bhuvan — https://bhuvan.nrsc.gov.in (accessed 2026-09-05)
- MOSDAC — https://www.mosdac.gov.in (accessed 2026-09-05)
- IN-SPACe — https://www.inspace.gov.in (accessed 2026-09-05)

---
*Next: Fill `docs/brd/brd-v0.1.md` §5–§8 (MoSCoW, metrics, constraints) on Day 2–3, then review to v0.5.*
