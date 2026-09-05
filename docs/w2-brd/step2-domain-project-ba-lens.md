# Step 2 — Your Domain Project Through the Business Analyst Lens

**Week:** W2 Day 1 Step 2 | **Hat:** Business Analyst | **Date:** 2026-09-05 | **Owner:** Omprakash Suthar (OPBSUTHAR) | **Track:** AI for Indian Satellites (AI / Space within DCAPSS)

> Source: Agnirva Internship Program, Week 2 — "Your Domain Project Through the Business Analyst Lens" (accessed 2026-09-05). Captured per Documentation First.

## 1. Purpose
Convert the assigned project idea into a precise, structured statement of need before any creative or technical work. Not generating ideas, styles, stacks, or formats — asking with discipline what is requested, for whom, what it must achieve, where boundaries lie.

## 2. Scope
- In: BA lens definition, 4-question spine, application to domain track, why BA comes first in Agnirva pipeline.
- Out: Solution thinking (held for W5 Product Analyst), visual/tech choices, implementation.

## 3. Key Outputs
- This Step 2 capture — `docs/w2-brd/step2-domain-project-ba-lens.md`
- Updated traceability in `docs/brd/brd-v0.2.md` §3–§10 to the 4 questions
- Link to prototype stub remains optional (`src/README.md`)

## 4. What the BA Lens Looks For (01)

**Clarity before action.** Designer asks "what should this look like?" Developer asks "what should this do?" BA asks four prior questions that must be answered before either:

| # | BA Question | Meaning | BRD Section |
|---|-------------|---------|-------------|
| 01 | What is the underlying need? | Not the phrasing, but the actual gap / problem / opportunity behind the request | §3 Problem Statement |
| 02 | Who experiences that need? | Specific people, orgs, or communities affected, named with precision | §5 Stakeholders & Personas |
| 03 | What does success look like? | Specific, observable outcome that tells everyone the need is addressed | §10 Success Metrics (KPIs) |
| 04 | What is in scope, and what is not? | Defensible boundary that prevents quiet expansion into unrelated work | §4 Scope (In/Out) + §8 Constraints |

These four are the spine of every BRD. Until answered, no other professional decision can be made well.

> The BA lens does not produce the solution. It produces the conditions under which a good solution becomes possible.

**Cost of skipping:** Designer without these answers produces something attractive but off-target. Developer produces something functional but unused. BA prevents that waste at the only point where prevention is cheap.

## 5. Applying the Lens to Your Project This Week (02)

Your project sits inside one of six DCAPSS tracks. Content domain changes; discipline does not. Five working days answer the four questions above, expanded into **eleven standard BRD sections**, assembled into a structured document.

Track examples from program (BA lens applied the same way):

| Track | BA Lens Asks |
|-------|--------------|
| Design | Who is visual content for, what understanding must it produce, which existing assets fall short? |
| Climate | Which district/audience the climate guide serves, what decisions it must support, what data from IMD / ISRO is credible? |
| **AI (your track)** | Which space/science topic the AI explainer must clarify, which audience misconception it must correct? For **AI for Indian Satellites**: which EO problem (e.g., flood mapping, crop health) and which Indian satellite source (Bhuvan cart, MOSDAC) is authoritative? |
| Product Management | Which segment of space economy the catalog covers, what decisions reader must make? |
| Space | Which mission / microgravity concept must be made accessible, to whom? |
| Software | Which mission / developer audience the catalog serves, what gap in current docs it fills? |

**Your track — AI for Indian Satellites — specific BA framing:**
- Need: Turn ISRO EO data (Cartosat, Resourcesat, RISAT, INSAT-3D/3DR via Bhuvan/MOSDAC) into timely, scalable, intelligent insight for a defined beneficiary (farmers, disaster cells, urban planners).
- Who: Name precision required — not "users" but "Karnataka State Disaster Management cell needing <3hr flood extent" or "smallholder farmers in Punjab needing weekly crop stress alert."
- Success: Observable outcome — e.g., time-to-insight <4h, coverage 1000 km², IoU >0.65 on validation set — not vague "better accuracy."
- Boundaries: One use case only; no model building in W2; no multi-state rollout.

**Common mistake:** Jumping to solution thinking — "we should build X" / "article should look like Y" — before need is fully described. BA lens deliberately holds that instinct back. Solution thinking is Product Analyst's job in Week 5, not this week.

## 6. Why the BA Lens Comes First (03)

Agnirva pipeline: `Need (W2) → Landscape (W3) → Quality (W4) → Product (W5) → Audience (W6) → Language (W7) → Synthesis (W8)`

BA produces first link. Every subsequent role depends on precision here:

- Vague problem statement → W3 SWOT studies vague landscape
- Loosely defined stakeholders → W6 engagement plan reaches loosely defined people
- Undefined scope → W5 PRD designs a product that grows in unintended directions
- Cost of imprecision in W2 compounds through every week

This is why BA is engaged first in any professional project, any industry, any country. ISRO does not begin a mission without mission requirements. TCS, Infosys, Wipro, HCL — every serious technology services firm operating from India runs same discipline at same lifecycle point.

**AI tools** (Agnirva Internship Assistant, Perplexity, NotebookLM, Gemini) accelerate drafting but do not replace BA responsibility for final answer.

> This week, you are clearing the ground for your project. Use the BA lens deliberately. The work you do here will outlast the week.

## 7. Translation to Your BRD (AI for Indian Satellites)

To keep W2 compliant per Welcome (11 sections, 30 activities), map the 4 BA questions to BRD v0.2 now:

- Q1 Need → Fill `docs/brd/brd-v0.2.md:3` with underlying EO gap (not request phrasing). Add evidence lines for Bhuvan/MOSDAC.
- Q2 Who → Expand `brd-v0.2.md:5` with 2–3 precise personas (e.g., disaster analyst, agronomist, faculty researcher) — name org, decision they make, data they trust.
- Q3 Success → Quantify `brd-v0.2.md:10` with observable KPIs (time-to-insight hours, coverage km², IoU threshold, cost).
- Q4 Boundaries → Harden `brd-v0.2.md:4` + `brd-v0.2.md:8` with in/out list that protects against quiet expansion (e.g., "no multi-sensor fusion in W2; no deployment pipeline").

Prototype stubs (`src/pipeline/bhuvan_fetch.py:1`, `src/pipeline/eo_pipeline_stub.py:1`) stay as out-of-scope validation aid — they do not answer the 4 questions, they only demonstrate that answers are implementable later.

## 8. Method
- Captured Step 2 verbatim concepts. Did not add external tracks or solution proposals.
- Applied Clear Beats Fancy: bullets, table, active voice.

## 9. References
- Agnirva Internship Program, Week 2 Day 1 Step 2 — Your Domain Project Through the Business Analyst Lens (accessed 2026-09-05)
- Week 2 Welcome: Business Analyst — 11 sections, 30 activities, pipeline Need→Synthesis (accessed 2026-09-05, `docs/w2-brd/week2-welcome-business-analyst.md`)
- ISRO / Bhuvan / MOSDAC / IMD — credible sources for Climate/AI tracks (to be cited with access dates in `docs/brd/brd-v0.2.md:11`)

---
*Next: Fill the 4 questions directly into BRD v0.2 §3–§5, §10, §4 — one section per micro-movement (6 activities/day).*
