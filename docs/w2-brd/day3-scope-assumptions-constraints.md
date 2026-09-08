# W2 Day 3 — Scope, Assumptions, and Constraints — AI for Indian Satellites

**Week:** W2 Day 3 | **Hat:** Business Analyst | **Date:** 2026-09-08 | **Owner:** Omprakash Suthar (OPBSUTHAR) | **Track:** AI for Indian Satellites
**Focus:** Scope, Assumptions, and Constraints — The Art of Scope: Why Saying No is a BA's Superpower → The Cost of Skipping the BRD → Assumptions and Risks: Planning for What Could Go Wrong → Day 3 Recap

> Notice board rule: Stay inside scheduled program steps; links already provided. After finishing Day 3 steps, click **Complete All Steps** to mark attendance. Delayed attendance may be noted. You Are Building Range — each week gives you a new professional lens; let the role change how you see the same project.

## 1. Purpose
Protect Day 2 work (stakeholders §5 + objectives §2) by drawing hard boundaries. Define what V1 includes, explicitly excludes, assumes true, and must operate within — so scope does not quietly grow beyond deliverable and project finishes on time. Maps directly to `docs/brd/brd-v0.2.md:4` (Scope), `:7` (Assumptions), `:8` (Constraints), `:9` (Risks).

## 2. Scope
- In: Day 3 scheduled content — scope/assumptions/constraints intro, art of saying no, cost of skipping BRD, assumptions & risks, recap. Mapping to BRD §4, §7, §8, §9. MT13–MT18 (6 activities).
- Out: Requirements deep-dive details already set in §6 trace, technical design/modeling (W3/W5), deployment/localization (W6/W7). No new use case outside flood extent pipeline.

## 3. Key Outputs
- This Day 3 note — `docs/w2-brd/day3-scope-assumptions-constraints.md`
- Updated BRD traces — `docs/brd/brd-v0.2.md:4` (In/Out hardened), `:7` (assumptions explicit), `:8` (constraints), `:9` (risks with mitigations)
- Update to `docs/progress-log.md` and `AGENTS.md` §3

## 4. Today's 5 Scheduled Steps

### 4.1 Focus — Scope, Assumptions, and Constraints (Step 1 of Day 3)
- **Why now:** Day 2 anchored who + what success looks like. Without boundaries, every downstream artefact (W3 SWOT, W5 PRD, W6 SCRP, W7 LAAP) inherits scope creep and never finishes. Scope is the discipline that protects human + outcome layers.
- **What you build today:** BRD §4 (In/Out), §7 (Assumptions — what you assume true and must validate), §8 (Constraints & Dependencies — hard limits: data access, compute, latency, time), §9 (Risks & Mitigations — what could go wrong if assumptions fail).
- **Range note:** You Are Building Range — BA lens this week is "define before build." Same project (AI for Indian Satellites flood extent) looks different through BA vs product vs research lens. Let role change your questions.
- **Work sequence:** Article on saying no → article on cost of skipping BRD → guide on assumptions/risks → six artifact activities MT13–MT18 that harden §4/§7/§8/§9 → Day 3 Recap.

### 4.2 The Art of Scope: Why Saying No is a BA's Superpower
- Placeholder for Step 2 article — to be filled when user provides Step 2 content. Expected themes: out-of-scope list as explicit promise, why "no" protects "yes," protecting 30-activity / 5-day cadence.
- Current BRD §4 already lists Out of scope: real-time rescue routing, multi-state expansion, model training/deployment, Kannada/Assamese alerts (W7). This will be hardened with rationale per activity MT13.

### 4.3 The Cost of Skipping the BRD
- Placeholder for Step 3 article — to be filled when user provides Step 3 content. Expected themes: exponential cost of late fixes, failure patterns when need not defined precisely, why W2 BRD is spine for W3–W7.
- Already traced in BRD §7 assumption: "BA holds problem space open; cost of late fix grows exponentially" (`docs/w2-brd/step3-what-is-a-business-analyst.md:5`) and §9 risk: "AI draft left unjudged."

### 4.4 Assumptions and Risks: Planning for What Could Go Wrong
- Placeholder for Step 4 guide — to be filled when user provides Step 4 content. Expected: assumption → risk → mitigation mapping, validation plan for each assumption (catalog access, latency, availability).
- Current BRD §7 lists 6 assumptions (links in order, one use case sufficient, form submission counts, etc.) and §9 has 5 risks with mitigations. MT14–MT17 will make each assumption testable and each mitigation owned.

### 4.5 Day 3 Recap — What Must Be True Before Leaving Day 3 (MT18)
- [ ] Scope in `brd-v0.2.md:4` has explicit In and Out lists — Out is not implied absence but stated commitment.
- [ ] Assumptions in `brd-v0.2.md:7` are numbered, falsifiable, with validation step and owner.
- [ ] Constraints in `brd-v0.2.md:8` name hard limits (Bhuvan/MOSDAC tiers, student compute, latency hours vs days, 5 days / 30 activities).
- [ ] Risks in `brd-v0.2.md:9` map directly from assumptions, each with impact + mitigation + owner — no orphan risks.
- [ ] In portal: completed Day 3 steps via provided links, then **Complete All Steps** — attendance rule per notice board.

## 5. Method
- Stayed inside Day 3 scheduled steps only; no extra program content.
- Applied Clear Beats Fancy and Documentation First (AGENTS.md §4.1–4.2).
- Linked outputs to 11-section BRD structure (`docs/w2-brd/week2-welcome-business-analyst.md:7`).

## 6. References
- Agnirva Notice Board — Week 2 Day 3 Focus: Scope, Assumptions, and Constraints (accessed 2026-09-08)
- `docs/w2-brd/week2-welcome-business-analyst.md` — 11 sections, pipeline Need→Synthesis
- `docs/brd/brd-v0.2.md:4`, `:7`, `:8`, `:9` — scope, assumptions, constraints, risks
- `docs/w2-brd/day2-stakeholders-objectives.md` — Day 2 anchors (§5 + §2) that Day 3 protects

---
*Next: Fill Steps 2–4 verbatim when provided, then execute MT13–MT18 to harden §4/§7/§8/§9 → v0.5. Day 4 turns to Requirements & Success Metrics.*
