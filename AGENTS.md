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

- **Active Status (as of 2026-09-05):** **Week 2 — Business Analyst (BRD) — Day 1 COMPLETED**
  - Day 1 completed: W2 Welcome, Domain Project through BA Lens, What is a BA, AI for Indian Satellites BA Lens, How AI is Changing BA Role, BRD Concept Review, Deliverable: Build Your BRD (scaffold `docs/brd/brd-v0.1.md` v0.1 draft)
  - Attendance note: Completed forms for Deliverable steps, then clicked Complete All Steps; delayed attendance may be noted per program board
  - Next: Day 2–3 — finalize use case, expand MoSCoW, quantify metrics → BRD v0.5

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
*Last updated: 2026-09-05 | Updated by: Muse Spark agent | Status: W2 D1 done, BRD v0.1 drafted*
