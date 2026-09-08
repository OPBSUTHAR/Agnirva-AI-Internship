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

### 4.1 Focus — Stakeholders and Objectives (Step 1 of Day 2)
> Verbatim from board: "A project that does not know who it serves cannot succeed. A project that cannot state what success looks like cannot ready. Day 2 addresses both gaps directly. You spent Day 1 defining title, overview, problem statement. Today you build human and outcome layers: who is on receiving end, and what specific, observable outcomes must you produce for them?"

- **What you build today:** Two of eleven BRD sections. **Stakeholders (§5)** catalogs every person/group with interest, what each cares about, what each needs. **Objectives (§2)** translates problem statement into 3–5 measurable, testable outcomes.
- **Quality signal:** Generic list ("users", "partners") = not examined. Named groups with one line on what they need = real BA work. Same for objectives: vague verbs vs testable statements reveal clarity.
- **Work sequence:** Read two articles → AI guide on stakeholder analysis → six artifact activities MT7–MT12 that fill §5 and §2 in `docs/brd/brd-v0.2.md`.
- **Keep It Human reminder:** District analyst must understand your BRD in one reading. Short sentences, active voice, named owners.

### 4.2 Who Are Your Stakeholders? (Step 2 Article — BABOK 4 Categories)
> Definition from article: stakeholder is any person/group/org affected by project, holds influence, or has legitimate interest. BA identifies every stakeholder before design, documents what each cares about, ensures design accounts for them. Missed stakeholders surface later at worst time, at higher cost. Identification ≠ management (management is W6 Community Operations Associate). Article cites BABOK Guide — IIBA.

**01 — The 4 Standard Categories (tick your draft against these; empty category = revisit):**
- **01 Sponsors & decision-makers** — authorise/fund/cancel. For Agnirva: Agnirva program team + partner institutions. Maps to Agnirva governance + Christ University anchor in `brd-v0.2.md:5`.
- **02 End users & beneficiaries** — consume/benefit from output. For track: district disaster analyst (KSDMA/ASDMA) — primary user BRD1; for Climate track would be district farmers, for Design track school students by age band. This is the Must-win.
- **03 Subject matter experts & contributors** — knowledge informs/review validates. For AI for Indian Satellites: ISRO NRSC/SAC scientists, IMD experts, IIT faculty, senior Agnirva alumni — provide Bhuvan/MOSDAC provenance.
- **04 Adjacent & affected parties** — affected without direct use. For space education guide: other platforms, Ministry of Education, regional language communities (localisation). For flood EO: downstream districts, NDRF, insurers, Kannada/Assamese language citizens.

Quote from article: “A project's hidden stakeholders are the ones who become visible only when something goes wrong. The Business Analyst's job is to find them first.”

**02 — 3 Groups Most Often Missed in First BRDs (≈50% miss rate):**
- **Operational handler** — owns output after project ends. For Agnirva: editorial & publishing team (needs file format, metadata, citation conventions, accessibility tags). Missing → delivery problem not finished product.
- **Regulatory/policy stakeholder** — shapes what can be said/how. For education: Ministry of Education / NCERT; for public data: Digital Personal Data Protection Act 2023 compliance; for EO: MOSDAC dissemination policy, Bhuvan access tier, IN-SPACe framework.
- **Negative stakeholder** — inconvenienced/displaced by success. Example: new free flood map displaces paid intermediary; new guide displaces paid publisher. BA must acknowledge, not pretend.

**03 — For Agnirva Domain Project (minimum 6 named groups, naming discipline):**
Must include at least: 1) Agnirva program team (sponsor 01), 2) target audience segment — not “everyone” but “district disaster analyst in Karnataka/Assam during monsoon” (beneficiary 02), 3) SMEs whose knowledge cited (03 — ISRO/SAC/IMD), 4) Agnirva editorial/publishing operation (operational handler), 5) partner institutions/communities (Christ University, State Remote Sensing Centre), 6) affected parties specific to domain (NDRF, adjacent districts, localisation communities).

Naming test from article: “Students” is not a stakeholder; “Class 9 students in Hindi-medium government schools in Bihar” is. For your track: not “farmers” but “smallholders in Punjab needing weekly crop stress alert from Resourcesat LISS-3 via Bhuvan.” Check each entry: “If this group disappeared, would objectives still be met?” If yes, remove; if no, keep.

AI acceleration per article: Perplexity finds named institutions/segments, Agnirva Internship Assistant flags generic entries, NotebookLM summarises collected audience material — judgment which groups belong is yours.

Current `brd-v0.2.md:5` updated to tag each row with 01–04 category and to include the three hidden groups (operational handler, regulatory, negative) to pass the 4-category tick test.

### 4.3 Stakeholder Analysis With AI (Step 3 Guide — W2 Day 2 Step 3)
> Verbatim lead: "One of the BA tasks that changed most in past 3 years. Half-day sticky-note workshop → 5-minute prompt with right tool. Used well, richer first draft than full pre-AI day. Used badly, generic plausible list that doesn't match context."

**01 — What AI Now Does Well (4 kinds, draft stage accelerated from authoring to editing):**
- **Candidate generation** — Perplexity/Gemini from project description produces first-pass list including categories you may miss (regulatory bodies, adjacent platforms).
- **Interest & concern summaries** — one-line draft per stakeholder of what group typically cares about → your refinement start point.
- **Power/influence mapping** — ranking by likely influence over success + interest in outcomes → quadrant map to review/adjust.
- **Gap detection** — Agnirva Internship Assistant compares your draft vs typical set for project type, flags missing groups.

Pattern: AI accelerates draft, rarely final answer, changes economics to editing.

**02 — What AI Cannot Replace (3 limits):**
- **Cannot identify actual stakeholders** — doesn't know your specific partners, communities reached, named individuals. Model suggests "regional language communities"; you must add "Telugu-speaking learners in Andhra Pradesh coastal districts."
- **Cannot judge relative weight** — doesn't know editorial team's citation format matters while hypothetical international agency doesn't. Weighting needs your context.
- **Cannot anticipate negative stakeholders in your specific situation** — requires local landscape knowledge. AI suggests categories; naming actual displaced group is your job.

**03 — Workflow Agnirva Interns Use for MT7–MT12:**
1. Paste Day 1 overview + problem statement + objectives into Agnirva Internship Assistant (or Perplexity). Ask for candidate list grouped by 4 categories from Step 2.
2. Review line by line: strike anything not specifically applicable; add anything specific tool missed (e.g., State Remote Sensing Centre, Kannada field volunteer).
3. For each surviving stakeholder, ask tool to draft one-line need statement → edit until specific enough to act on. Test: "needs accurate information" = not specific. "needs verifiable ISRO mission dates with cited sources for Grade 9 textbook alignment" = specific. For EO: "needs Bhuvan tile ID + time + sensor per polygon for <3h briefing" is specific.
4. Final verification pass with Perplexity: confirm each named institution/community exists, correctly named, still active (models hallucinate entities). 3-minute check prevents citation embarrassment in final BRD.

Applied to this project: candidate flood stakeholders (NDRF, KSDMA, NRSC, SAC, IMD, IN-SPACe) drafted via AI, then human-filtered to 11 rows in `docs/brd/brd-v0.2.md:5` with Interest+Need columns. AI = collaborator, not author — see `docs/w2-brd/step5-how-ai-changing-ba-role.md:6` workflow traced in BRD §7/§9.

### 4.4 Objectives That Actually Mean Something (Step 4 Article — SMART + Failure Modes)
> Definition from article: "Objective is measurable, observable outcome, written so two independent reviewers agree whether met. Converts problem into testable claims. Without testable objectives, project can be finished without anyone able to say whether it succeeded."

**Aspiration vs Objective:** "Improve student understanding of space science" = wish, not testable. "Publish ten 800-word explainers covering ten specified ISRO missions, each reviewed by SME and rated ≥4/5 by grade 9 sample" = commitment, testable.

**01 — SMART Format and Limits (taught at TCS, Infosys, Wipro, Cognizant for 3+ decades):**
- **S Specific** — names deliverable + audience + condition. Not "more content" but "ten explainers for grade 9 students."
- **M Measurable** — includes number/threshold/verifiable state. Not "high quality" but "rated 4+ by 80% reviewers."
- **A Achievable** — realistic for time/resources. Not "10,000 explainers" for 5-day week but "ten explainers."
- **R Relevant** — connects directly to problem + stakeholder need. Not tangential impressive goal.
- **T Time-bound** — specifies when. Not "eventually" but "by Friday Week 7."

Limit: SMART passes format while measuring wrong thing. Common failure is measuring outputs ("publish ten explainers") when stakeholders care about outcomes ("reach 5,000 grade 9 students who rate useful"). Quote: "A project objective that cannot be tested is a project objective that cannot fail. Projects that cannot fail also cannot succeed in any meaningful sense."

**02 — 3 Common Failure Modes in First-Draft BRDs:**
- **Activity disguised as outcome** — "Conduct research on Indian space missions" (activity) vs "Produce research-validated catalog of 25 missions with cited sources" (outcome). Fix: ask "what would I show to prove done?" Process = activity, artefact/state = outcome.
- **Immeasurable adjective** — "improved, enhanced, better, comprehensive, robust, engaging" without defined meaning. Fix: replace with number/threshold/comparison.
- **Unowned objective** — no specific stakeholder agreed they care; BA's preference imported. Fix: trace each objective back to stakeholder list entry.

**03 — What Good Agnirva Objectives Look Like (3–5, each passes measured + traced tests):**
- Climate track example: "Produce Telugu and English district-level monsoon explainer covering Krishna and Godavari basins, validated by ≥2 state agriculture sources and reviewed by ≥3 farming contacts."
- Design track example: "Publish six visual explainers on Chandrayaan-3 phases, each rated ≥4/5 by 25 grade 9 students, text editable in three Indian languages by Week 7."
- Discipline: name deliverable + audience + verification precisely.

**Applied to this BRD (§2 now 5 objectives, all SMART and owned):**
- O1 — Deliver validated district flood map within 3 hours of overpass, with tile lineage attached. Traces to KSDMA analyst (02), verified by timestamp diff.
- O2 — Cover ≥1000 km² per run from 2–3 tiles without hand digitization, CRS consistent. Traces to analyst + publishing handler, verified by area calc.
- O3 — IoU ≥0.65 vs 10% hand-digitized sample, every polygon cited. Traces to NRSC/SAC SMEs, verified by sample IoU.
- O4 — Keep V1 to one state / one monsoon window with assumptions logged. Traces to Framewirk governance, verified by §4/§8 trace.
- O5 — Traceability: every Must links to stakeholder + metric + citation. Traces to downstream hats (RLD/VQRD/PRD), verified by matrix review.

**AI help:** Agnirva Internship Assistant reviews drafts against SMART + 3 failure modes, returns edits list; Gemini translates loose ("should be useful for students") → testable ("must include ≥3 named ISRO missions with dates verified against ISRO archive"). Judgment which version commits remains yours. Handover test: give objective to outsider, ask "how would you check?" Clear test description = well written.

### 4.5 Day 2 Recap — What Must Be True Before Leaving Day 2 (MT12)
- [ ] Stakeholders in `brd-v0.2.md:5` now has Interest + Need columns (what each cares about + what each needs), not just Role/Need — passes Step 1 "examined precisely" test.
- [ ] Objectives in `brd-v0.2.md:2` are 5 testable statements (O1 3h, O2 1000km², O3 IoU 0.65, O4 scope, O5 traceability) — each verifiable, per Step 1 requirement.
- [ ] MT7–MT12 activities logged: MT7 stakeholder long-list, MT8 care/need one-liner, MT9 priority Must/Should/Could, MT10 objectives draft, MT11 testability check, MT12 trace to §10 KPIs.
- [ ] Used AI to draft/gap-check stakeholders, then human-judged every line per Step 5 rule.
- [ ] In portal: completed Day 2 steps via provided links, then **Complete All Steps** — attendance rule per notice board (delay may be noted).

## 5. Method
- Stayed inside Day 2 scheduled steps only; no extra program content.
- Applied Clear Beats Fancy: bullets, table in §5, sentences <20 words where possible.
- Linked outputs to BRD sections as required by 11-section structure (`docs/w2-brd/week2-welcome-business-analyst.md:7`).

## 6. References
- Agnirva Notice Board — Week 2 Day 2 Focus: Stakeholders and Objectives (accessed 2026-09-08)
- Agnirva Article — Who Are Your Stakeholders? — W2 Day 2 Step 2 (BABOK 4 categories, 3 missed groups, naming discipline) (accessed 2026-09-08)
- Agnirva Article — Objectives That Actually Mean Something — W2 Day 2 Step 4 (SMART, 3 failure modes, handover test) (accessed 2026-09-08)
- `docs/w2-brd/week2-welcome-business-analyst.md` — 11 sections, pipeline Need→Synthesis
- `docs/w2-brd/step2-domain-project-ba-lens.md` — 4-question spine (who = §5, success = §10)
- `docs/w2-brd/step5-how-ai-changing-ba-role.md` — AI drafts, human judges (applied in 4.3)
- `docs/brd/brd-v0.2.md:2`, `:5`, `:10` — objectives, stakeholders, KPIs
- IIBA BABOK Guide — stakeholder categories (01–04) (cited via article)
- ISRO Bhuvan — https://bhuvan.nrsc.gov.in (accessed 2026-09-05) | MOSDAC — https://www.mosdac.gov.in (accessed 2026-09-05) | IN-SPACe — https://www.inspace.gov.in (accessed 2026-09-05)

---
*Next: Day 3 — Requirements & Scope refinement (expand `brd-v0.2.md:6` to 10–12 MoSCoW items, harden `brd-v0.2.md:4` boundaries) then quantify KPIs → v0.5.*
