# Prototype Note — W2 BRD + Minimal Prototype Path

**Date:** 2026-09-05 | **Decision:** BRD + minimal prototype (per user choice) | **Scope:** W2 deliverable remains BRD only; prototype is optional validation aid

## 1. Purpose
Explain why a minimal runnable stub exists alongside the BRD without breaking Week 2 scope.

## 2. Scope
- In: Stub implementation that traces to BRD §3, §6, §8, §10
- Out: Real model training, evaluation, deployment (W3–W5), heavy data

## 3. What was built
- `src/pipeline/bhuvan_fetch.py` — mock Bhuvan catalog fetch
- `src/pipeline/eo_pipeline_stub.py` — full pipeline stub with metrics
- `notebooks/eo_exploration_stub.py` — exploration note
- `src/README.md` — scope and traceability

All files are stdlib-only and write mock JSON to `data/` so they run without credentials.

## 4. How this stays W2-compliant
- BRD §4 Scope explicitly marks pipeline implementation as out of scope.
- Prototype is labelled proof-of-concept in code comments and docs.
- Program Deliverable form receives BRD text (`docs/brd/brd-v0.2.md`), not prototype code.
- Audit trail: `docs/progress-log.md` logs this as optional, not required.

## 5. Next
- W2 Day 2–4: Complete BRD §6–§11, keep prototype unchanged.
- W3 RLD: Replace stubs with real literature-backed approach.
- W5 PRD: Replace dummy inference with real model.

---
*Teams that get the BRD right make every later artefact coherent (Week 2 Welcome). Prototype does not replace that.*
