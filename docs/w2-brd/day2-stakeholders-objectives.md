# W2 Day 2 — Stakeholders and Objectives — AI for Indian Satellites

**Week:** W2 Day 2 | **Hat:** Business Analyst | **Date:** 2026-09-08 | **Owner:** Omprakash Suthar (OPBSUTHAR) | **Track:** AI for Indian Satellites
**Focus:** Stakeholders and Objectives — Who Are Your Stakeholders? → Stakeholder Analysis With AI → Objectives That Actually Mean Something → Day 2 Recap

> Notice board rule: Stay inside scheduled program steps; links already provided. After finishing Day 2 steps, click **Complete All Steps** to mark attendance. Delayed attendance may be noted. Keep It Human — make useful things easier to understand.

## 1. Purpose
Answer two BRD spine questions with precision before defining requirements: who experiences the need, and what does success mean in observable terms. Capture stakeholder map and business objectives so they trace directly to `docs/brd/brd-v0.2.md:5` and `:2`.

## 2. Scope
- In: Day 2 scheduled content — stakeholders/objectives intro, stakeholder identification, AI-assisted stakeholder analysis, meaningful objectives, recap. Mapping to BRD §5 and §2.
- Out: Requirements authoring details (Days 3–4), technical design, model selection. No new use case outside flood mapping chosen in v0.2.

## 3. Key Outputs
- This Day 2 note — `docs/w2-brd/day2-stakeholders-objectives.md`
- Updated BRD traces — `docs/brd/brd-v0.2.md:5` (stakeholders refined), `:2` (objectives made testable), `:10` (KPIs)
- Update to `docs/progress-log.md` and `AGENTS.md` §3 (not yet, next turn)

## 4. Today's 5 Scheduled Steps

### 4.1 Focus — Stakeholders and Objectives
- **Why together:** Problem without owner has no priority. Objective without audience has no proof. W2 Welcome defines BRD success as answering need, who, success, boundaries — Day 1 covered need, Day 2 covers who + success.
- **Keep It Human reminder:** Complicated language hides weak thinking. A district analyst must understand your BRD in one reading. Short sentences, active voice, named owners.
- **Deliverable tie:** BRD §5 names who. BRD §2/§10 proves you served them. If §5 is vague, W6 SCRP and W7 LAAP inherit that vagueness.

### 4.2 Who Are Your Stakeholders? (Identification)
- **Primary (direct beneficiary, must-win):** District disaster analyst in KSDMA / ASDMA — decides evacuations and relief routing. Uses Bhuvan/MOSDAC tiles daily during monsoon. Success window <3 hours. This is BRD Deliverable BRD1 user.
- **Provider / authority (must-satisfy):** ISRO NRSC (Bhuvan) and SAC (MOSDAC) — data provenance, catalog access, dissemination policy. IN-SPACe — private/academic use framework. Without them, data claim is invalid.
- **Consumer of BRD (must-support):** W3 RLD, W4 VQRD, W5 PRD owners — they derive research, quality, and product decisions from your stakeholder map. Vague here → vague downstream.
- **Institutional anchor (should-include):** Christ University faculty research — Long-Range Connection links academic rigor to space-AI application.
- **Governance (must-comply):** Agnirva / Framewirk — weekly artefacts, Clear Beats Fancy, 30 activities (6/day), attendance rule (Complete Step after form, then Complete All Steps).
- **Audience handoff (could-serve in W2, must-flag):** Farmers, urban planners, citizens — served indirectly via analyst’s maps; detailed outreach deferred to W6 SCRP after BRD is stable.
- **Anti-pattern to avoid:** Listing “ISRO, farmers, government, public” without role/need/priority. BRD `brd-v0.2.md:5` already uses table with Role | Need | Priority — keep that precision.

### 4.3 Stakeholder Analysis With AI (How AI Helps, Where Human Judges)
- **What AI does well here (per Step 5):**
  - Draft stakeholder long-list from your problem statement and Indian satellite context (e.g., expand KSDMA → district admin, IMD, state remote sensing centre).
  - Propose influence/interest placement and suggest missing voices (e.g., ground validation team).
  - Check consistency — flag that “citizen” is marked Must while BRD scope says W2 is district-only.
- **What AI cannot replace (human owns):**
  - Choosing Must vs Could — only you decide who must win in V1.
  - Detecting missing stakeholder info — AI won’t know you lack a Kannada field volunteer persona.
  - Owning sign-off — analyst’s acceptance criteria must be validated with human logic, not generated text.
- **Workflow to use:** Prompt AI with BRD §3 + §5 draft → ask for gaps, conflicts, and citation needs → edit every line → keep source links (Bhuvan/MOSDAC doc dates). AI = collaborator, not author. This mirrors `docs/w2-brd/step5-how-ai-changing-ba-role.md:6` workflow already traced in BRD §7/§9.

### 4.4 Objectives That Actually Mean Something (From Vague to Testable)
- **Bad objective:** “Improve flood mapping with AI.” Not testable. No owner. No time.
- **Good objectives for this BRD (trace to §2 and §10):**
  - O1 — Deliver validated district flood extent map within 3 hours of overpass, with tile lineage (Bhuvan/MOSDAC ID, time, sensor) attached.
  - O2 — Cover ≥1000 km² per run from 2–3 tiles without hand digitization, CRS EPSG:4326 consistent.
  - O3 — Achieve IoU ≥0.65 against 10% hand-digitized validation sample, with citations for every polygon.
  - O4 — Keep V1 scope to one state / one monsoon window; log assumptions and out-of-scope items to prevent creep.
- **Why this matters:** Objectives are the contract that turns stakeholder need into measurable success. W2 Welcome warns top failure is need never defined precisely enough — measurable objectives prevent that.
- **Test:** Each objective must link to a stakeholder in §5 and a KPI in §10, and must be writable as “What will be measured / Why it matters / Good result” (same form as BRD7).

### 4.5 Day 2 Recap — What Must Be True Before Leaving Day 2
- [ ] Stakeholder table in `brd-v0.2.md:5` names real orgs/roles, not generic groups, with Must/Should/Could set.
- [ ] Objectives in `brd-v0.2.md:2` are testable (hours, km², IoU), not adjectives.
- [ ] Used AI to draft/gap-check stakeholders, then human-judged every line per Step 5 rule.
- [ ] Updated `docs/progress-log.md`; ready to expand MoSCoW and scope on Days 3–4.
- [ ] In portal: completed Day 2 steps via provided links, then **Complete All Steps** — attendance rule per notice board.

## 5. Method
- Stayed inside Day 2 scheduled steps only; no extra program content.
- Applied Clear Beats Fancy: bullets, table in §5, sentences <20 words where possible.
- Linked outputs to BRD sections as required by 11-section structure (`docs/w2-brd/week2-welcome-business-analyst.md:7`).

## 6. References
- Agnirva Notice Board — Week 2 Day 2 Focus: Stakeholders and Objectives (accessed 2026-09-08)
- `docs/w2-brd/week2-welcome-business-analyst.md` — 11 sections, pipeline Need→Synthesis
- `docs/w2-brd/step2-domain-project-ba-lens.md` — 4-question spine (who = §5, success = §10)
- `docs/w2-brd/step5-how-ai-changing-ba-role.md` — AI drafts, human judges (applied in 4.3)
- `docs/brd/brd-v0.2.md:2`, `:5`, `:10` — objectives, stakeholders, KPIs
- ISRO Bhuvan — https://bhuvan.nrsc.gov.in (accessed 2026-09-05) | MOSDAC — https://www.mosdac.gov.in (accessed 2026-09-05) | IN-SPACe — https://www.inspace.gov.in (accessed 2026-09-05)

---
*Next: Day 3 — Requirements & Scope refinement (expand `brd-v0.2.md:6` to 10–12 MoSCoW items, harden `brd-v0.2.md:4` boundaries) then quantify KPIs → v0.5.*
