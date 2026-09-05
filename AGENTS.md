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

- **Active Status (as of 2026-09-05):** **Week 2 — Business Analyst (BRD) — Day 1 COMPLETED (11-section alignment)**
  - Day 1 completed: W2 Welcome Step 1 (Business Analyst is first role, 11-section BRD, 30 activities 6/day, pipeline Need→Synthesis, My First Analysis Note), plus Day 1 lens 7-step capture. Upgrades: `docs/brd/brd-v0.1.md` (8-sec history) → `docs/brd/brd-v0.2.md` (11-sec per Welcome: Executive Summary→References&Glossary)
  - Prototype path chosen: **BRD + minimal prototype** — stubs `src/pipeline/bhuvan_fetch.py:1`, `src/pipeline/eo_pipeline_stub.py:1` (stdlib-only, verified runnable) + `src/README.md:1` + `docs/w2-brd/prototype-note.md:1`. Marked optional/ out-of-scope; deliverable form still receives BRD text only.
  - Step 2 captured: `docs/w2-brd/step2-domain-project-ba-lens.md:1` — 4-question spine (need/who/success/scope), clarity before action, tracks DCAPSS, why BA first (ISRO/TCS/Infosys discipline). BRD v0.2 trace updated (`docs/brd/brd-v0.2.md:3`, `:4`, `:5`, `:10`).
  - Step 3 captured: `docs/w2-brd/step3-what-is-a-business-analyst.md:1` — BA definition, 4 core activities (elicit/document/validate/manage change), lifecycle position (cost grows exponentially if late), Indian context (IIBA/BABOK, India Stack, TCS/Infosys/Wipro/HCL). BRD traces added to §7 and §11.
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
- **Push cadence (user rule): Batch pushes every 15 commits.** Commit locally after each micro-movement, but `git push` only after 15 commits accumulate (or on explicit user request). Track count via `git log origin/main..HEAD --oneline | wc -l`.

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
*Last updated: 2026-09-05 | Updated by: Muse Spark agent | Status: W2 D1 done, BRD v0.2 + Step 3, push cadence = every 15 commits*
