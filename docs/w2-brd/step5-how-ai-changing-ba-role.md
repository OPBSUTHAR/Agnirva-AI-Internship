# Step 5 — How AI is Changing the Business Analyst Role

**Week:** W2 Day 1 Step 5 | **Hat:** Business Analyst | **Date:** 2026-09-05 | **Owner:** Omprakash Suthar (OPBSUTHAR)

> Source: Agnirva Internship Program, Week 2 Day 1 Step 5 — "How AI is Changing the Business Analyst Role" (accessed 2026-09-05). Captured per Documentation First.

## 1. Purpose
Explain how BA role in 2026 differs structurally from 2020 — same 11 BRD sections, same 5 questions, same discipline (define problem before solution), but AI has shifted how BA spends the working day. Clarify what AI accelerates and what it cannot replace.

## 2. Scope
- In: What AI now does well in BA work (§01), what AI cannot replace (§02), recommended Agnirva workflow this week (§03).
- Out: Tool comparisons, model selection, BRD content itself.

## 3. Key Outputs
- This Step 5 capture — `docs/w2-brd/step5-how-ai-changing-ba-role.md`
- Trace added to `docs/brd/brd-v0.2.md` §7/§9 for judgment vs draft distinction
- Progress logged

## 4. Core Premise

> The BA role in 2026 looks structurally different from 2020. The eleven sections of a BRD are the same. The five questions are the same. The discipline of defining the problem before defining the solution is unchanged. What has changed is how the BA spends the working day, because a large portion of manual labour that once took up that day is now done by AI in seconds.

Implication: BA who can use AI well outperforms BA who cannot; BA who relies on AI without judgment produces documentation that quietly fails.

## 5. What AI Now Does Well in BA Work (§01)

Former hours → well-formed prompt + minutes of review. Agnirva Internship Assistant + Perplexity/Gemini/NotebookLM assist with:

| BA task | What AI does | Your action |
|---------|--------------|-------------|
| Stakeholder mapping drafts | Generates first-pass list of likely stakeholder groups, interests, questions each would want answered | Edit for your domain; add precision (names, orgs) |
| Risk register first drafts | Surfaces common risks for project type | Refine with project-specific risks AI cannot know |
| Requirement formulation | Converts loose statement ("article should be useful") → testable requirement ("must include three named ISRO missions") | Verify testability |
| Source discovery | Perplexity finds current sources faster than manual search, with citations to verify | Verify citations; cite with access dates |
| Document structure & consistency | Compares BRD sections for contradictions, missing fields, vague language | Fix flagged vagueness |

Common pattern: AI accelerates **draft** stage. Produces starting point far faster than blank page. Starting point rarely final answer, but shifts economics: you move from authoring → editing, generating → judging.

## 6. What AI Cannot Replace in the BA Role (§02)

| Cannot do | Why |
|-----------|-----|
| **Decide what is in scope** | Scope is political/strategic decision — trade-offs between stakeholders, time vs quality, this project vs later. Right answer depends on unwritten conversations. AI can list candidates for in/out columns; human BA decides which goes where. |
| **Identify what is missing from stakeholder conversation** | What stakeholder leaves unsaid often matters more than what they say. Trained BA notices gap, asks follow-up. AI sees only prompt. |
| **Own the sign-off** | BRD is contract between BA and stakeholders. Sign-off is human "yes, this is what we agreed." AI drafts; accountability is human. |
| **Navigate organisational reality** | Which stakeholder to consult first, which constraints are real vs negotiable, which requirements are policy vs preference — local knowledge no general model can learn. |

## 7. How Agnirva Interns Use AI This Week (§03)

Recommended workflow — AI as collaborator, not author:

- **Agnirva Internship Assistant** → project-specific guidance (knows BRD structure, 11 sections, expected standards). Ask it to review draft sections; flag vague/generic/missing.
- **Perplexity** → sourcing domain facts (ISRO mission numbers, audience demographics, comparable content).
- **NotebookLM** → when you have stack of source PDFs/articles to summarise into structured findings you can cite.
- **Gemini** → general-purpose drafting assistant to translate rough thought → formal requirement language.

Non-negotiable rule: Every section of your BRD must be reviewed by you, in your own judgment, before final document. AI produces starting material. You produce the BRD.

> The students this internship recognises at the end will be those who used AI deliberately and read every line they kept.

## 8. Application to Your BRD (AI for Indian Satellites)

- Allowed: Use AI to draft stakeholder map (`docs/brd/brd-v0.2.md:5`), risk register (`:9`), testable requirements (`:6`), source discovery for §11.
- Not allowed to delegate: Scope decisions (`:4`/`:8`), gap detection in stakeholder needs, sign-off, constraint negotiability — these remain your judgment.
- Prototype stubs (`src/pipeline/bhuvan_fetch.py:1`) illustrate acceleration pattern: AI drafted pipeline skeleton in minutes; you validated scope boundary (out-of-scope in W2) and citation discipline.

## 9. Method
- Captured Step 5 verbatim concepts. Preserved two halves (does well vs cannot replace) and workflow table.
- Applied Clear Beats Fancy: tables, short sentences.

## 10. References
- Agnirva Internship Program, Week 2 Day 1 Step 5 — How AI is Changing the Business Analyst Role (accessed 2026-09-05)
- Steps 1–4 — `docs/w2-brd/week2-welcome-business-analyst.md`, `docs/w2-brd/step2-domain-project-ba-lens.md`, `docs/w2-brd/step3-what-is-a-business-analyst.md`, `docs/w2-brd/step4-ai-indian-satellites-ba-lens.md`
- Tools referenced: Agnirva Internship Assistant, Perplexity, Gemini, NotebookLM

---
*Next: Step 6 — BRD Concept Review (11 sections + 5 questions → document structure).*
