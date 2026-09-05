# Step 3 — What is a Business Analyst?

**Week:** W2 Day 1 Step 3 | **Hat:** Business Analyst | **Date:** 2026-09-05 | **Owner:** Omprakash Suthar (OPBSUTHAR) | **Track:** AI for Indian Satellites

> Source: Agnirva Internship Program, Week 2 — "What is a Business Analyst?" (accessed 2026-09-05). Captured per Documentation First.

## 1. Purpose
Define the Business Analyst role — what it does, where it sits in a project, and why you operate as BA in Week 2.

## 2. Scope
- In: BA definition, 4 core activities, lifecycle position, BA vs PM vs designer/engineer, Indian context (IIBA/BABOK, India Stack), implication for W2.
- Out: Solution design, product specification, tech architecture (downstream roles).

## 3. Key Outputs
- This Step 3 capture — `docs/w2-brd/step3-what-is-a-business-analyst.md`
- Trace added to `docs/brd/brd-v0.2.md` §6/§7/§11 for BA method
- Progress logged for Step 3 completion

## 4. Definition (from program)

A Business Analyst is the professional responsible for translating an organisation's intent into a clear, structured definition of what a project must achieve, for whom, and within what constraints. The BA sits between the people who want something done and the people who will do it, and produces the documentation that ensures both groups work toward the same outcome.

The role exists because organisations rarely fail for lack of effort or talent. They fail because requesters and makers held different mental pictures of success, and differences surfaced only after significant time and money were spent. The BA makes mental pictures explicit, written down, and agreed upon before execution.

## 5. What a BA Actually Does — 4 Core Activities (§01)

| # | Activity | What it means | BRD Link |
|---|----------|---------------|----------|
| 01 | **Elicits requirements** | Structured conversations with stakeholders to surface real needs, separating needs from assumptions, preferences, untested ideas | BRD §5 Stakeholders (elicitation source) + §6 Requirements |
| 02 | **Documents the need** | Captures elicited info in structured written format any future reader can understand without being present | BRD 11 sections (`docs/brd/brd-v0.2.md:1`) |
| 03 | **Validates with stakeholders** | Returns documentation to stakeholders for review and formal sign-off; written record must match intent | BRD review cycle v0.2 → v0.5 → v1.0 + §7 Assumptions to be validated |
| 04 | **Manages change** | When new information affects definition, manages formal change to documentation rather than letting project drift informally | BRD versioning + §9 Risks / change control |

**Not a project manager:** PM delivers on time, on budget, to scope. BA defines what scope means. Without BA definition, PM has nothing to manage against.

**Not a designer / engineer / content creator / developer:** BA does not produce solution. BA produces the brief from which solution is built. Most common mistake: jumping to solution thinking before problem is fully defined. Disciplined BA holds problem space open until definition is precise, even when stakeholders are eager to talk solutions.

> The BA is not the person who answers the questions. The BA is the person who knows which questions must be asked, in which order, of which people, and refuses to let the project move forward until those questions have answers everyone agrees on.

## 6. Where the BA Sits in a Professional Project (§02)

BA engaged at very beginning, often before formal approval. One of first roles to start and first to deliver.

Lifecycle:
```
Organisation identifies need/opportunity
  → BA investigates, asks questions, documents findings → BRD
  → BRD reviewed and signed off by stakeholders
  → Only then downstream roles begin: designers, product managers, engineers, content teams
    Each uses BRD as primary reference
```

This sequencing exists because cost of changing direction grows exponentially:

- Misunderstanding caught in BRD phase → costs a single conversation
- Caught after design → costs days of rework
- Caught after development → can cost months and large sums

BA work done well prevents compounding costs by surfacing misunderstanding when cheapest to fix.

## 7. The BA in the Indian Context (§03)

- India employs more BAs than any other country. Role is foundational to IT services model.
- Firms: **Tata Consultancy Services, Infosys, Wipro, HCL Technologies, Tech Mahindra, Cognizant** — maintain large BA practices to translate client requirements across countries/sectors/cultures into precise engineering work.
- Standards: **International Institute of Business Analysis (IIBA)** publishes **BABOK Guide** (body of knowledge). Indian BAs hold IIBA certs: **ECBA, CCBA, CBAP** (by experience depth).
- Beyond IT services: product companies, fintech, healthtech, edtech, government digital. **India Stack** (UPI, Aadhaar auth, DigiLocker) was built on rigorous business analysis — every interface spec traces to a documented requirement.
- AI shift: Tools — Agnirva Internship Assistant, Perplexity, Gemini, NotebookLM — have reshaped junior BA throughput (stakeholder map from afternoon to minutes, risk register in one session). Judgment work (deciding what answer actually is) remains human; drafting has shifted.

For internship students, understanding BA early matters:
1. BA mindset (define problem before solution) is transferable to every other role (W3–W7).
2. BA is highly accessible entry-level role in India with clear progression: senior analyst → lead analyst → product management.

You are operating as BA this week on your domain project, using same five questions, same structured documentation, same sign-off discipline as a junior BA at Infosys/Wipro on first client engagement. Difference vs senior BA is experience, not method. Certification follows years of repeated practice. Practice begins this week.

## 8. What This Means for Your Week 2 (§04)

- You are the BA on your domain project doing real BA work this week.
- Artefact: **Business Requirements Document** — your first piece of professional analytical work. Will not be perfect on first attempt. Must be honest, structured, and ready for review — foundation for six weeks.
- BA mindset learned this week quietly improves every artefact W3–W7. Once you learn to define before you build, you will find it difficult to stop.

For **AI for Indian Satellites** this means: elicit from ISRO/Bhuvan/MOSDAC docs + end-user needs (disaster cell / farmer), document per 11 sections, validate assumptions, manage scope — do not jump to model or pipeline. Prototype stubs (`src/pipeline/bhuvan_fetch.py:1`) stay as out-of-scope validation aid only.

## 9. Method
- Captured Step 3 verbatim concepts. Did not add external steps.
- Applied Clear Beats Fancy: bullets, table, lifecycle diagram.

## 10. References
- Agnirva Internship Program, Week 2 Day 1 Step 3 — What is a Business Analyst? (accessed 2026-09-05)
- International Institute of Business Analysis (IIBA) — BABOK Guide (referenced in program)
- India Stack — UPI / Aadhaar / DigiLocker as BA-driven specifications (program context)
- Agnirva Week 2 Welcome + Step 2 BA Lens — `docs/w2-brd/week2-welcome-business-analyst.md`, `docs/w2-brd/step2-domain-project-ba-lens.md`

---
*Next: Step 4 — AI for Indian Satellites Through the Business Analyst Lens (domain application).*
