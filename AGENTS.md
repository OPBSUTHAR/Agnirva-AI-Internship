# AGENTS.md — Agnirva AI Internship (NEAT 5.0) — AI for Indian Satellites

> **Owner:** Omprakash Suthar (OPBSUTHAR) | Christ University, Bangalore research link
> **Purpose:** Persistent agent instruction file. Every AI assistant working in this repo MUST read and follow this file.

---

## 1. Program Identity

- **Program:** Agnirva AI Internship Program (NEAT 5.0)
- **Track:** AI for Indian Satellites
- **Powered by:** Framewirk (micro-movement structure → tangible outputs each movement)
- **Track Focus:** Satellite imagery analysis, Earth observation pipelines, autonomous systems — making Indian satellite systems & applications more useful, scalable, and intelligent.
- **Writing Standard:** **Clear Beats Fancy** — concise, direct, factual, no fluff. All deliverables must pass this.
- **Institutional Anchor:** Christ University, Bangalore — Faculty Research: Long-Range Connection task links institutional research to space-AI technology.

## 2. 6-Hat Professional Framework

Rotates Week 2 → Week 7. Each hat produces a specific artifact:

| Week | Hat Role | Artifact | Code |
|------|----------|----------|------|
| W2 | Business Analyst | Business Requirements Document | BRD |
| W3 | Research Analyst | Research Landscape Document | RLD |
| W4 | Quality Analyst | Validation & Quality Requirements Document | VQRD |
| W5 | Product Analyst | Product Requirements Document | PRD |
| W6 | Stakeholder Communication Associate | Stakeholder Communication & Reporting Plan | SCRP |
| W7 | Localization & Accessibility Strategist | Localization & Accessibility Action Plan | LAAP |

Week 1 was Orientation (Days 1–5).

## 3. Progress Ledger (Source of Truth)

- **Week 1 — Orientation (Days 1–5): COMPLETED**
  - Orientation module finished
  - Faculty Research: Long-Range Connection task completed (Christ University × space-AI)
  - Roadmap, 6-hat methodology, and Clear Beats Fancy internalized
  - Weekly Status Report prepared for W1→W2 transition

- **Active Status (as of 2026-09-08):** **Week 2 — Business Analyst (BRD) — Day 3 COMPLETED (Scope, Assumptions, Constraints)**
  - Day 3 completed 2026-09-08: All 6 steps via `docs/w2-brd/day3-scope-assumptions-constraints.md:1` — Focus (scope statement grows→fails, In/Out boundary), Art of Scope (In/Out halves, Krishna example, 6-item checklist, 3 costs, holds test TCS/Infosys/Wipro), Cost of Skipping BRD (PMI Pulse, 3 failures divergent models/repeated scope/undefined success, 10x–100x compounding, what BRD prevents), Assumptions & Risks (7 bets across 5 categories, Risk Register Prob/Impact/Mitigation, assumption↔risk inverses, weekly review), Recap (5 of 11 sections finish, defensible scope for W4/W5/W6, Day 4 heart: Requirements & Risk Register). BRD `docs/brd/brd-v0.2.md:4`, `:7`, `:8`, `:9` hardened accordingly.
  - Day 2 completed 2026-09-08: All 6 steps via `docs/w2-brd/day2-stakeholders-objectives.md:1` — Focus (MT7-12, Keep It Human), Who Are Stakeholders (BABOK 4 cats 01-04 + 3 hidden groups, naming discipline), Analysis With AI (4 does-well, 3 cannot, 4-step workflow), Objectives That Mean Something (SMART TCS/Infosys/Wipro/Cognizant, 3 failures, handover test, O1-O5 SMART), Recap (anchored §5+§2 → W3/W5/W6/W7, Day 3 preview). BRD `docs/brd/brd-v0.2.md:2` and `:5` hardened accordingly.
  - Previous Day 2 active preserved below —

- **Completed (as of 2026-09-08):** **Week 2 — Business Analyst (BRD) — Day 2 COMPLETED (Stakeholders & Objectives)**
  - Day 2 captured: `docs/w2-brd/day2-stakeholders-objectives.md:1` — 5 steps (Focus, Who Are Stakeholders, Analysis With AI, Objectives That Mean Something, Recap), Keep It Human, stakeholder table refined, AI draft→judge workflow, 4 testable objectives (3h / 1000km² / IoU 0.65).
  - BRD deliverable consolidated 2026-09-08: `docs/brd/brd-deliverable-form-draft.md:1` now meets minimums (BRD1 98w/80, BRD2 98w/90, BRD3 95w/90, BRD5 106w/80, BRD6 120w/80, BRD8 123w/120) with BRD4/BRD7 structured per form; duplicate `brd-deliverable-form-short.md` removed.
  - Previous Day 1 status preserved below —

- **Completed (as of 2026-09-05):** **Week 2 — Business Analyst (BRD) — Day 1 COMPLETED (11-section alignment)**
  - Day 1 completed: W2 Welcome Step 1 (Business Analyst is first role, 11-section BRD, 30 activities 6/day, pipeline Need→Synthesis, My First Analysis Note), plus Day 1 lens 7-step capture. Upgrades: `docs/brd/brd-v0.1.md` (8-sec history) → `docs/brd/brd-v0.2.md` (11-sec per Welcome: Executive Summary→References&Glossary)
  - Prototype path chosen: **BRD + minimal prototype** — stubs `src/pipeline/bhuvan_fetch.py:1`, `src/pipeline/eo_pipeline_stub.py:1` (stdlib-only, verified runnable) + `src/README.md:1` + `docs/w2-brd/prototype-note.md:1`. Marked optional/ out-of-scope; deliverable form still receives BRD text only.
  - Step 2 captured: `docs/w2-brd/step2-domain-project-ba-lens.md:1` — 4-question spine (need/who/success/scope), clarity before action, tracks DCAPSS, why BA first (ISRO/TCS/Infosys discipline). BRD v0.2 trace updated (`docs/brd/brd-v0.2.md:3`, `:4`, `:5`, `:10`).
  - Step 3 captured: `docs/w2-brd/step3-what-is-a-business-analyst.md:1` — BA definition, 4 core activities (elicit/document/validate/manage change), lifecycle position (cost grows exponentially if late), Indian context (IIBA/BABOK, India Stack, TCS/Infosys/Wipro/HCL). BRD traces added to §7 and §11.
  - Step 4 captured: `docs/w2-brd/step4-ai-indian-satellites-ba-lens.md:1` — separates real need from AI excitement, problem before tech, speed/accuracy/scale/interpretation mapping, 5 BRD clarifications (problem/users/AI value/scope/outcomes). BRD traces to `docs/brd/brd-v0.2.md:3` and BR-04/BR-05.
  - Step 5 captured: `docs/w2-brd/step5-how-ai-changing-ba-role.md:1` — AI does well (stakeholder drafts, risk register, requirement formulation, source discovery, consistency checks) vs cannot replace (scope decision, missing gap detection, sign-off ownership, org reality). Workflow: AI collaborator not author, human judges every line. BRD traces to §7 (AI workflow), §9 (AI-without-judgment risk), BR-07/BR-08.
  - Step 6 captured: `docs/w2-brd/step6-brd-concept-review.md:1` — 5 MCQs (BA definition, BRD 11 sections, BRD vs PRD/FRS, failure without BRD, AI fit), why review exists (apply not recognise).
  - Step 7 Deliverable drafted: `docs/brd/brd-deliverable-form-draft.md:1` — 8-section BRD form (BRD 1 Primary User 96w, BRD2 Problem 101w, BRD3 Insight 104w, BRD4 three reqs with Bhuvan/MOSDAC/BABOK sources, BRD5 Out-of-Scope 92w, BRD6 Trust Rule 98w, BRD7 three success measures, BRD8 Summary 128w) + Student Record placeholders. Ready to paste into official manual submission form.
  - Info note: `docs/w2-brd/info-365futures-support.md:1` — 365Futures bundle optional, does not replace attendance/evaluation.
  - Attendance note: Completed forms for Deliverable steps, then clicked Complete All Steps; delayed attendance may be noted per program board
  - Next: Day 2–3 — finalize use case (flood vs crop), expand MoSCoW to 10–12 items, quantify §10 KPIs → BRD v0.5

Update this table on every turn. No progress is real until documented in `/docs/progress-log.md`.

## 4. Agent Operating Instructions (MUST FOLLOW)

### 4.1 Documentation First
1. **Never work without documenting.** Each micro-movement must create/update a file under `docs/`.
2. Maintain `docs/progress-log.md` as the single source of truth. Append date, hat, movement, output, next step.
3. Keep `docs/weekly-status-reports/` current. Template: `docs/templates/weekly-status-report.template.md`.
4. After any file change, verify via `read` or `bash`.

### 4.2 Clear Beats Fancy
- Sentences < 20 words where possible. Active voice. Bullets over paragraphs.
- No jargon without definition. No superlatives. Facts + evidence + references.
- Every doc starts with: Purpose → Scope → Key Outputs → Method → References.

### 4.3 Artifact Standards
- Each hat artifact lives in `docs/<hat-code>/` (e.g., `docs/brd/`, `docs/rld/`).
- Use provided templates in `docs/templates/`.
- Version every artifact: `v0.1 draft → v0.5 review → v1.0 final`.
- Cite sources: ISRO, IN-SPACe, Bhuvan, MOSDAC, papers — with URL + date accessed.

### 4.4 Repo Hygiene
- Do NOT create files outside the allowed structure without asking.
- Keep `README.md` synced with progress (badges, status table, quick links).
- Commit messages: `docs(w2-brd): <movement> — <output>` or `feat(brd): ...` style.
- This repo will be pushed to `https://github.com/OPBSUTHAR/<repo-name>` — keep it public-ready.
- **Push cadence (user rule): Batch pushes every 8 commits.** Commit locally after each micro-movement, but `git push` only after 8 commits accumulate (or on explicit user request). Track count via `git log origin/main..HEAD --oneline | wc -l`.

### 4.5 Interaction Rules
- Ask clarifying questions with the `question` tool when scope is ambiguous.
- Use `todowrite` for any multi-step work (3+ steps).
- Prefer `read`/`edit`/`write` over bash for file ops.
- When generating deliverables, also update `AGENTS.md` progress ledger and `docs/progress-log.md`.

## 5. Current Directive (Week 2)

**Role:** Business Analyst
**Goal:** Produce BRD for an AI-for-Indian-Satellites use case (e.g., Earth observation pipeline / satellite imagery analysis).
**Next micro-movements:**
1. Define problem statement & stakeholders
2. Elicit & prioritize requirements (MoSCoW)
3. Define success metrics & constraints (ISRO data, compute, latency)
4. Draft BRD v0.1 → review → v1.0

## 6. How to Update This File

- When a week/hat completes, move it from Active to Completed, increment version, and log in `docs/progress-log.md`.
- When a new track/focus is assigned, update §1 and §5.
- Do not delete history — append.

---
*Last updated: 2026-09-08 | Status: W2 D3 done — scope/assumptions/constraints, 20 ahead (push at 8, pushing now)*
