# Step 6 — BRD Concept Review

**Week:** W2 Day 1 Step 6 | **Hat:** Business Analyst | **Date:** 2026-09-05 | **Owner:** Omprakash Suthar (OPBSUTHAR)

> Source: Agnirva Internship Program, Week 2 Day 1 Step 6 — "BRD Concept Review" (accessed 2026-09-05). Concept check, not graded examination. Captured per Documentation First.

## 1. Purpose
Confirm absorption of four core ideas from Day 1 before applying them to BRD build.

## 2. Scope
- In: Purpose of review, 5 MCQs, what each covers (§01), why review exists (§02), how to use result.
- Out: BRD content authoring (next steps after review).

## 3. Key Outputs
- This Step 6 capture — `docs/w2-brd/step6-brd-concept-review.md`
- Check result noted in `docs/progress-log.md` (attempt count not tracked externally; logic check is internal)
- Reference link back to Steps 1–5 readings

## 4. Review Design (from program)

> This is a concept review, not a graded examination. Its purpose is to confirm that you have absorbed the four core ideas covered in Day 1 before applying the ideas that build your actual BRD. The review contains **five multiple-choice questions** drawn from the readings on the Business Analyst role, the structure of the BRD, the cost of skipping the requirements phase, and the AI-augmented BA workflow. Each question has one correct answer. You may attempt the check as many times as you need. Use the questions to check whether core ideas are clear.

- 5 MCQs, one correct answer each, unlimited attempts
- Covers logic, not memorisation

## 5. What This Review Covers (§01)

Five questions cover following ground (none require memorisation, all require reading logic):

| # | Area | Concept tested | Source file |
|---|------|----------------|-------------|
| 01 | What a BA is | Professional definition, lifecycle position, distinction BA vs PM | `docs/w2-brd/step3-what-is-a-business-analyst.md:4` + `:5` |
| 02 | What a BRD contains | Eleven standardised sections of BRD and what each is for | `docs/w2-brd/week2-welcome-business-analyst.md:7` + `docs/brd/brd-v0.2.md:1` |
| 03 | What a BRD is not | Distinction between BRD, Product Requirements Document (PRD), Functional Requirements Specification (FRS) | `docs/w2-brd/week2-welcome-business-analyst.md:6` (pipeline) + `docs/w2-brd/step3-what-is-a-business-analyst.md:6` |
| 04 | What goes wrong without a BRD | Three failure patterns when requirements phase skipped: divergent mental models, repeated scope decisions, undefined success | `docs/w2-brd/week2-welcome-business-analyst.md:5` + `docs/w2-brd/step3-what-is-a-business-analyst.md:6` (exponential cost) |
| 05 | How AI fits into BA role | What Agnirva Internship Assistant / Perplexity / NotebookLM / Gemini now do well, and what remains human BA responsibility | `docs/w2-brd/step5-how-ai-changing-ba-role.md:5` + `:6` |

## 6. Why This Review Exists (§02)

One of six concept reviews across program (one per role week). Exists because artifact activities after review require you to **apply** concepts rather than recognise them.

- Student who understands review → has conceptual ground for real BRD for real project
- Student who does not yet pass → benefits from re-reading relevant article before applying ideas

If idea feels unclear, revisit relevant reading and strengthen notes before applying concepts. Prototype stubs (`src/pipeline/bhuvan_fetch.py:1`) not relevant to review — review tests concepts, not implementation.

## 7. Expected Answers (logic, not memorised keys)

- BA = translates org intent → structured definition of what must be achieved, for whom, within constraints; first in, produces BRD before PM/design/engineering
- BRD = 11 sections: Executive Summary, Objectives, Problem Statement, Scope, Stakeholders, Requirements (MoSCoW), Assumptions, Constraints & Dependencies, Risks, Success Metrics, References & Glossary
- BRD vs PRD vs FRS: BRD defines business need (why/what); PRD defines product (how need becomes features); FRS defines functional spec (detailed behavior) — do not conflate
- Without BRD: divergent mental models surface late → scope re-decided informally → success undefined (no observable KPIs) — cost compounds
- AI in BA: AI accelerates drafts (stakeholder maps, risks, testable requirements, source discovery, consistency) → human owns scope, gap detection, sign-off, org reality; workflow = collaborator not author, judge every line

Use this section to self-check before marking Step 6 complete in portal. Retry until 5/5 logic is clear.

## 8. Method
- Captured Step 6 verbatim. Did not add external MCQs. Provided logic synthesis for self-check.
- Applied Clear Beats Fancy: tables, short sentences.

## 9. References
- Agnirva Internship Program, Week 2 Day 1 Step 6 — BRD Concept Review (accessed 2026-09-05)
- Steps 1–5 — `docs/w2-brd/week2-welcome-business-analyst.md`, `docs/w2-brd/step2-domain-project-ba-lens.md`, `docs/w2-brd/step3-what-is-a-business-analyst.md`, `docs/w2-brd/step4-ai-indian-satellites-ba-lens.md`, `docs/w2-brd/step5-how-ai-changing-ba-role.md`
- `docs/brd/brd-v0.2.md` — 11-section reference

---
*Next: Step 7 — Week 2 Deliverable: Build Your BRD (assemble My First Analysis Note).*
