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
> Verbatim from board: "A project without a scope statement is a project that grows. A project that grows beyond what can be delivered is a project that fails. Day 3 introduces the single most underappreciated discipline: defining what the project will not do. Yesterday you defined who serves and what outcomes you commit to. Today you draw the boundary line. Inside is what you will deliver. Outside is everything else someone might reasonably expect, but which this project explicitly excludes. Without that boundary, every conversation becomes a negotiation about adding something new."

- **What you build today:** Three of eleven BRD sections. **Scope (§4)** names what is in scope and what is explicitly out of scope. **Assumptions (§7)** catalogs what you treat as true without formal verification. **Constraints (§8)** names hard limits: time, resources, access, policy, and others. These together protect from quiet expansion, hidden risks, and being judged later against criteria never agreed. Most skipped in first BRDs; absence causes most expensive downstream mistakes.
- **Work sequence:** Three short articles → six artifact activities MT13–MT18 that build Scope, Assumptions, Constraints in `docs/brd/brd-v0.2.md` → Day 3 Recap.
- **Range note:** You Are Building Range — each week gives new professional lens; let role change how you see same flood extent project.

### 4.2 The Art of Scope: Why Saying No is a BA's Superpower (Step 2 Article)
> Definition: "Scope is formal statement of what project will and will not deliver. Defines boundary between committed work and valuable-but-excluded work. Highest-leverage BA activity — every later build/test/ship decision references scope. Senior BAs recognised by ability to write defensible scope and protect under pressure (constant stakeholder additions each sound reasonable alone, together expand beyond timeline/resources)."

**01 — Two Halves of Scope Statement (junior misses second half):**
- **In-scope half** — deliverables, audiences, formats, conditions will produce. Climate example: "single district monsoon explainer for Krishna district AP, English+Telugu, PDF+web, June–Oct 2026, citing IMD + Ministry of Earth Sciences public sources."
- **Out-of-scope half** — reasonably expected but explicitly excluded. Same project: "will not cover districts beyond Krishna, will not provide real-time weather updates, will not include pest forecasts, will not produce printed booklet, will not translate beyond English/Telugu within Week 2."
Both matter: In tells what building, Out tells what not — only way to prevent low-level addition pressure during execution.

Operational checklist (6 items):
01 Deliverables in scope (named output + format + quantity) 02 Audiences in scope (named segment) 03 Geographies/timeframes in scope (where + period) 04 Deliverables explicitly out of scope (closely related outputs will not produce) 05 Audiences explicitly out of scope (adjacent segments not served) 06 Future work explicitly deferred (valuable but later phase)

Quote: "Hardest part is not deciding what to include. It is writing down, in advance, what you will refuse to add later when good ideas appear and team is enthusiastic."

**02 — Why "No" Is Superpower (Infosys/TCS/Wipro practice):**
Senior BAs advance because they hold scope under pressure — not obstructive, understand cost of unmanaged expansion. Every addition has 3 downstream costs: consumes time budgeted for original, introduces unanalysed dependencies, alters deliverable-objective relationship (attention diverted). Weak BA accepts to keep happiness short-term. Strong BA names trade-off explicitly: add X → remove Y OR extend timeline Z days OR lower quality threshold. Decision is project's, visibility is BA's. For Week 2 internship: "ten explainers" + stakeholder suggests video → BA surfaces trade-off: video means nine explainers OR longer timeline OR lower quality.

**03 — How to Write Scope That Holds (3 properties):**
- **Specific enough to operationalise** — not "educational content" but "ten 800-word explainers covering ten named ISRO missions"; not "for students" but "for grade 9 CBSE + state-board."
- **Paired with explicit out-of-scope list** — defensive work; when request arrives, point to list and ask trade-offs for moving into scope.
- **Agreed and signed off** — scope in head doesn't exist; scope in BRD formally reviewed/approved can be defended because agreed upfront.

AI help: Agnirva Internship Assistant reviews draft scope for typically missed items; Perplexity confirms named audiences/geographies/deliverables accurately; NotebookLM summarises planning docs into In/Out lists — judgment where line falls is yours.

Holds test: imagine request at week 6, open scope statement — would this be clearly out of scope as written? If yes, scope holds. If negotiation/interpretation needed, needs another pass.

Applied to this project (`docs/brd/brd-v0.2.md:4` already lists Out: real-time rescue routing, multi-state, model training/deployment, Kannada/Assamese alerts (W7) — now hardened to 6-item checklist + specific flood In: "1 district flood extent polygon per overpass, PDF+GeoJSON, Bhuvan/MOSDAC lineage, 3h window, June–Sept monsoon 2026" vs Out as above). MT13 maps to this §4.2.

### 4.3 The Cost of Skipping the BRD (Step 3 Article)
> Lead: "Cost is not abstract — documented measurable pattern across PMI Pulse of the Profession reports for two decades: projects with clearly defined requirements significantly more likely on time, within budget, stakeholder satisfied. Patterns observed including at TCS, Infosys, Wipro, HCL, Tech Mahindra where discipline refined because cost so well understood."

**01 — Three Failure Patterns (in order, each leads to next):**
- **Divergent mental models** — designer imagines one audience, content lead another, quality reviewer applies never-agreed criteria. Outputs don't fit because starting assumptions never explicit. Compounds weekly; by visibility, significant effort needs correction/discard.
- **Repeated scope decisions** — without agreed signed-off scope, "should this topic be covered? is audience in scope? does quality standard apply?" Each decision informal, inconsistent, unrecorded; different people at different times → project grows unexpectedly / contradicts itself.
- **Undefined success** — if success never formally defined, at end no basis to evaluate achieved. Teams produce technically sound outputs that don't address original need because need never formally stated. Delivered but unanswerable whether succeeded.

**02 — Why Costs Compound (10x–100x multiplier):**
Misunderstanding caught in BRD phase costs single conversation. Same caught after design costs days redesign; after development weeks rework; after launch can cost credibility entirely. PMBOK + BABOK summarise multiplier 10x–100x depending how late surfaces. Why senior BAs at Cognizant/Tech Mahindra spend so much time on BRD even on aggressive timelines — time invested recovered many times over by avoiding rework.

Quote: "A misunderstanding caught at requirements phase costs a conversation. Same misunderstanding caught after launch costs the project. BRD catches misunderstandings while still cheap."

**03 — What BRD Actually Prevents (maps to sections):**
- Prevents **divergent models** via Project Overview + Problem Statement + Stakeholders — same starting picture; when designer vs content lead disagree on audience, open BRD same definition → resolves or escalates, not hidden.
- Prevents **repeated scope decisions** via Scope §4 In/Out — when addition request arrives, BA can point and accept formally with trade-offs or refuse with clear reason; decision conscious not drift.
- Prevents **undefined success** via Objectives §2 + Success Metrics §10 — translate problem into testable criteria; at end team returns and asks yes/no/partial with evidence.

Agility note: Agnirva BRD includes all sections precisely because each prevents known failure. AI tools (Internship Assistant, Perplexity, Gemini, NotebookLM) make drafting faster than ever; discipline same as pre-AI: define precisely, write down In/Out, agree success upfront, refer throughout execution.

Close: "BRD is not deliverable to be finished and filed away. It is reference team returns to whenever decision must be made. BRD written, signed off, never opened again = wasted. BRD opened weekly to resolve disagreements = doing job."

Applied: `docs/brd/brd-v0.2.md` already holds problem space open per `docs/w2-brd/step3-what-is-a-business-analyst.md:5` (§7) and AI-without-judgment risk (§9) — Step 3 explains why those prevent compounding costs. MT15 maps here.

### 4.4 Assumptions and Risks: Planning for What Could Go Wrong (Step 4 Article)
> Lead: "Every project relies on assumptions, faces risks. Mature work names both explicitly so team knows what treated as true and what could change outcome. Assumptions §7 + Risk Register §9 are two of 11 standard sections, referred to most often during execution."
> Definition: **Assumption** = treated as true without formal verification ("assume target audience has reliable internet" — might be true, not checked; if false, decisions revisited). **Risk** = event that could happen and would change outcome if did ("risk partner doesn't approve citation format in time" — plan needed for both).

**01 — Writing Useful Assumptions (5–8 for W2, 3 properties: condition, what changes if false, testable):**
- Weak: "We assume project will be successful."
- Strong: "Assume Agnirva editorial team available Day 5 for BRD sign-off. If not, sign-off deferred to Monday, Week 3 starts against unsigned draft. Testable via calendar."
Strong names specific condition, specifies what changes if false (deferred sign-off, draft becomes working doc), testable (calendar confirms).

Categories (5):
01 Audience assumptions — what true about people served (know, device, language) 02 Source assumptions — what credible without further verification 03 Institutional assumptions — what expect from partners/program team, timeframe 04 Tool/resource assumptions — working conditions depends on (AI tools, time budget) 05 Timeline assumptions — availability of stakeholders/reviewers/own time

Quote: "Every assumption is a quiet bet. Naming bet doesn't change odds. It changes whether you notice when bet gone wrong."

**02 — Building Useful Risk Register (5–10 for W2, Infosys/TCS/Wipro standard format — 4 pieces per risk):**
For each risk: (1) what is risk plain language, (2) probability High/Med/Low, (3) impact High/Med/Low, (4) mitigation — action to reduce probability or impact. High/High = fully developed mitigation, may change plan before materialises; Low/Low = acknowledge/monitor; middle = BA judgment.

Common Agnirva categories: source risks (key reference unavailable/outdated), audience risks (definition different from assumed), quality risks (fails W4 VQRD review), localisation risks (W7 translator finds untranslatable terms), timeline risks (overruns week).

**03 — How Assumptions and Risks Work Together (related distinct):**
Every assumption wrong = risk materialised. Register often includes inverse of assumption. Example: Assumption "partner responds within 5 working days" → Risk "partner does not respond within 5 days. Prob: medium. Impact: medium. Mitigation: identify alternate review source by Day 3, secure backup commitment by Day 4." Together gives finished picture what uncertain + how managed. BRD without assumptions reads as knows everything; without register reads as no plan for what might go wrong.

AI help: Internship Assistant generates candidate risks for project type (refine with specific knowledge); Perplexity verifies assumptions vs public info (institution still operates, policy still applies); Gemini stress-tests language for specificity/testability. Judgment which assumptions/risks matter remains yours.

Close: "Risk register not write once and file. Read weekly: have any materialised? new emerged? assumptions confirmed/invalidated? Read weekly = doing job. Written and ignored = decoration."

Applied to this project: `docs/brd/brd-v0.2.md:7` currently 6 assumptions will be expanded to 7 covering audience/source/institutional/tool/timeline with testable conditions; `:9` 5 risks will be expanded to 7 with probability/impact/mitigation + assumption inverses, per MT14–MT17.

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
