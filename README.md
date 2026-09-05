# Agnirva AI Internship — NEAT 5.0 — AI for Indian Satellites

![Status](https://img.shields.io/badge/Week-1%20Completed-green)
![Week 2](https://img.shields.io/badge/Week%202-Business%20Analyst%20(BRD)-blue)
![Track](https://img.shields.io/badge/Track-AI%20for%20Indian%20Satellites-orange)
![Standard](https://img.shields.io/badge/Writing-Clear%20Beats%20Fancy-lightgrey)

**Owner:** Omprakash Suthar ([OPBSUTHAR](https://github.com/OPBSUTHAR)) | **Institution:** Christ University, Bangalore | **Powered by:** Framewirk (micro-movement structure)

> Satellite imagery analysis · Earth observation pipelines · Autonomous systems — making Indian satellite systems & applications more useful, scalable, and intelligent.

---

## Quick Links
- Agent instructions: [`AGENTS.md`](./AGENTS.md)
- Progress log (source of truth): [`docs/progress-log.md`](./docs/progress-log.md)
- Weekly report W1→W2: [`docs/weekly-status-reports/w1-status-report.md`](./docs/weekly-status-reports/w1-status-report.md)
- W2 Welcome (11-sec, 30 activities): [`docs/w2-brd/week2-welcome-business-analyst.md`](./docs/w2-brd/week2-welcome-business-analyst.md)
- W2 Day 1 BA Lens: [`docs/w2-brd/day1-business-analyst-lens.md`](./docs/w2-brd/day1-business-analyst-lens.md)
- BRD v0.2 draft (11 sections): [`docs/brd/brd-v0.2.md`](./docs/brd/brd-v0.2.md) | history: [`brd-v0.1.md`](./docs/brd/brd-v0.1.md)
- Prototype stub: [`src/README.md`](./src/README.md) + [`docs/w2-brd/prototype-note.md`](./docs/w2-brd/prototype-note.md)
- Faculty connection: [`docs/w1-orientation/long-range-connection.md`](./docs/w1-orientation/long-range-connection.md)
- Templates: [`docs/templates/`](./docs/templates/)

## Progress

| Week | Hat Role | Artifact | Status |
|------|----------|----------|--------|
| W1 | Orientation (Days 1–5) | Orientation + Long-Range Connection | ✅ Completed |
| W2 | Business Analyst | BRD — Business Requirements Document | 🟡 Day 1 Completed (v0.1 draft) |
| W3 | Research Analyst | RLD — Research Landscape Document | ⏳ Planned |
| W4 | Quality Analyst | VQRD — Validation & Quality Requirements | ⏳ Planned |
| W5 | Product Analyst | PRD — Product Requirements Document | ⏳ Planned |
| W6 | Stakeholder Communication Associate | SCRP — Communication & Reporting Plan | ⏳ Planned |
| W7 | Localization & Accessibility Strategist | LAAP — Localization & Accessibility Plan | ⏳ Planned |

Update rule: No progress is real until logged in [`docs/progress-log.md`](./docs/progress-log.md) and [`AGENTS.md`](./AGENTS.md) §3.

## 6-Hat Framework
Framewirk micro-movements → tangible output each movement. Writing standard: **Clear Beats Fancy** — concise, direct, factual, no fluff.

```
W1 Orientation → W2 BRD → W3 RLD → W4 VQRD → W5 PRD → W6 SCRP → W7 LAAP
```

## Repo Structure
```
.
├── AGENTS.md                          # Agent instruction file (must-read)
├── opencode.json                      # OpenCode config (points to AGENTS.md)
├── README.md
├── src/                               # Minimal prototype stub (W2 optional, out-of-scope)
│   └── pipeline/{bhuvan_fetch.py,eo_pipeline_stub.py}
├── docs/
│   ├── progress-log.md                # Single source of truth
│   ├── w1-orientation/long-range-connection.md
│   ├── weekly-status-reports/w1-status-report.md
│   ├── templates/{brd.template.md, weekly-status-report.template.md}
│   ├── brd/{brd-v0.1.md (8-sec history), brd-v0.2.md (11-sec)}
│   ├── w2-brd/{week2-welcome-business-analyst.md, day1-business-analyst-lens.md, prototype-note.md}
│   ├── rld/                           # W3 Research Analyst
│   └── ...
```

## Current Directive — Week 2 (Business Analyst) — Day 1 Done (11 sections + prototype)
1. ✅ Day 1 Step 1 — Week 2 Welcome captured → `docs/w2-brd/week2-welcome-business-analyst.md:1` (11-sec BRD, 30 activities 6/day, Need→Synthesis, My First Analysis Note)
2. ✅ Day 1 Lens — 7 steps: Welcome + Domain BA Lens + What is BA + AI for Indian Satellites BA Lens + How AI Changes BA + BRD Review + Deliverable → `docs/w2-brd/day1-business-analyst-lens.md:1`
3. ✅ BRD upgraded: v0.1 (8-sec history) → v0.2 (11-sec) → `docs/brd/brd-v0.2.md:1` | v0.1 kept for audit
4. ✅ Prototype path: BRD + minimal stub → `src/pipeline/bhuvan_fetch.py:1`, `src/pipeline/eo_pipeline_stub.py:1` (verified runnable, stdlib only) + `src/README.md:1`
5. ⏳ Day 2–3 — Finalize use case (flood vs crop), expand MoSCoW to 10–12 items, quantify §10 KPIs → v0.5
6. ⏳ Day 5 — Final assembly → My First Analysis Note (v1.0) — feeds W3 RLD, W5 PRD, W7 LAAP

> Attendance: Fill Deliverable form content and submit before clicking Complete Step. Then click **Complete All Steps**. Button only ≠ contribution.

## References
- ISRO Bhuvan — https://bhuvan.nrsc.gov.in (accessed 2026-09-05)
- MOSDAC — https://www.mosdac.gov.in (accessed 2026-09-05)
- IN-SPACe — https://www.inspace.gov.in (accessed 2026-09-05)
- Christ University Research — https://christuniversity.in/research (accessed 2026-09-05)

---
*Last updated: 2026-09-05 | W2 D1 done, BRD v0.1 drafted | Maintained by Muse Spark agent*
