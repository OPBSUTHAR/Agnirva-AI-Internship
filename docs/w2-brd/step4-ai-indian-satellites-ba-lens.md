# Step 4 — AI for Indian Satellites Through the Business Analyst Lens

**Week:** W2 Day 1 Step 4 | **Hat:** Business Analyst | **Artifact:** BRD | **Date:** 2026-09-05 | **Owner:** Omprakash Suthar (OPBSUTHAR) | **Track:** AI for Indian Satellites

> Source: Agnirva Internship Program, Week 2 Day 1 Step 4 — "AI for Indian Satellites Through the Business Analyst Lens" (accessed 2026-09-05). Captured per Documentation First.

## 1. Purpose
Define AI for Indian Satellites as a Business Analyst problem — separate real project need from broad AI excitement. Focus on problem before technology.

## 2. Scope
- In: Why specificity matters for satellite AI, role lens (speed/accuracy/scale/interpretation), artifact focus (5 BRD clarifications), framing guidance.
- Out: Technology stack choice, model selection, implementation (deferred).

## 3. Key Outputs
- This Step 4 capture — `docs/w2-brd/step4-ai-indian-satellites-ba-lens.md`
- Trace updates to `docs/brd/brd-v0.2.md` §3–§6/§10 for satellite-specific need
- Progress logged

## 4. Core Message (Why This Matters)

> AI can support satellite imagery, anomaly detection, mission planning, data analysis, agriculture, climate, and infrastructure monitoring. That range is powerful, but it can also become vague. A BRD helps identify the specific need this project is addressing.

Without specificity, AI for satellites becomes a buzzword list. BA discipline forces precision.

## 5. Role Lens — Business Analyst on Satellite AI

> As a Business Analyst, focus on the problem before the technology. Ask where satellite workflows may need better speed, accuracy, scale, or interpretation, and who benefits from that improvement. The strongest framing will connect AI capability to a real user or institutional need.

BA questions for AI for Indian Satellites:

| Improvement dimension | BA asks | Example |
|-----------------------|---------|---------|
| Speed | Where does latency cost decisions? | Flood extent <3h vs. 24h manual interpretation |
| Accuracy | Where do errors cost lives / money? | Crop stress false negatives reduce yield response |
| Scale | Where can humans not cover area? | Resourcesat scenes across 1000+ km² weekly |
| Interpretation | Where is data not yet intelligence? | Raw LISS-3 DN → actionable crop health map for farmer in Punjabi |

Strongest framing ties AI capability directly to a user/institutional decision, not to tech showcase.

## 6. Artifact Focus — What Your BRD Must Clarify

Program lists 5 clarifications (transcribed verbatim, truncated tail preserved):

1. **the satellite or space-data problem being addressed**
2. **the users or stakeholders who need better intelligence**
3. **where AI may add value**
4. **what is within project scope**
5. **what outcomes would signal success** *(text truncated as "signa l access" in source; interpreted as signal success)*

Mapping to 11-section BRD:

| Program ask | BRD section | Current file |
|-------------|-------------|--------------|
| satellite / space-data problem | §3 Problem Statement | `docs/brd/brd-v0.2.md:3` |
| users / stakeholders needing intelligence | §5 Stakeholders & Personas | `docs/brd/brd-v0.2.md:5` |
| where AI may add value | §6 Requirements (BR-04, BR-07) + §3 Opportunity | `docs/brd/brd-v0.2.md:6` |
| within project scope | §4 Scope + §8 Constraints | `docs/brd/brd-v0.2.md:4` |
| outcomes that signal success | §10 Success Metrics (KPIs) | `docs/brd/brd-v0.2.md:10` |

## 7. Applying to Your Project (AI for Indian Satellites — EO Pipeline)

Choose **one** problem to keep BRD testable (per Step 2 Q4 boundary). Two candidates that satisfy Step 4 lens:

| Candidate | Satellite data | Problem wording (BA) | User who benefits | AI value | Scope boundary |
|-----------|----------------|----------------------|-------------------|----------|----------------|
| Flood mapping | INSAT-3D/3DR + RISAT SAR via MOSDAC/Bhuvan | Delay in manual flood extent mapping after monsoon events | Karnataka State Disaster Management cell | Speed: SAR + optical fusion for extent in hours; Scale: district-wide automation | One state, monsoon season, extent map only (no rescue routing) |
| Crop health monitoring | Resourcesat-2/2A LISS-3/4 via Bhuvan | Weekly crop stress not visible until yield loss | Smallholder farmers + Agriculture Dept | Interpretation: NDVI time-series classification; Accuracy: reduce false negatives | One crop (e.g., wheat), one district, weekly alert (no input recommendation) |

Both connect AI capability → real decision. Recommendation: finalize by Day 2 and record rationale in `docs/brd/brd-v0.2.md:3`.

## 8. Anti-Pattern to Avoid

- Vague framing: "We will use AI for satellites to improve data." Fails BA test (no who, no observable success).
- Technology-first: "We will build a CNN on ISRO data." BA asks: for whom, why, how will you know it helped?
- Scope creep: covering flood + crop + urban change + climate in one BRD — violates 11-section coherence and 30-activity cadence.

Prototype stubs (`src/pipeline/bhuvan_fetch.py:1`, `src/pipeline/eo_pipeline_stub.py:1`) demonstrate where AI may add value (stub metrics) without claiming delivery — consistent with BA problem-before-technology rule.

## 9. Method
- Captured Step 4 verbatim. Did not select technology. Preserved 5-point artifact focus.
- Applied Clear Beats Fancy: tables, short sentences.

## 10. References
- Agnirva Internship Program, Week 2 Day 1 Step 4 — AI for Indian Satellites Through the Business Analyst Lens (accessed 2026-09-05)
- Steps 1–3 — `docs/w2-brd/week2-welcome-business-analyst.md`, `docs/w2-brd/step2-domain-project-ba-lens.md`, `docs/w2-brd/step3-what-is-a-business-analyst.md`
- ISRO Bhuvan / MOSDAC catalog documentation (to be cited with access dates in `docs/brd/brd-v0.2.md:11`)

---
*Next: Step 5 — How AI is Changing the Business Analyst Role (AI-augmented BA work).*
