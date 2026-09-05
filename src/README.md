# src — Minimal Prototype (W2 Optional, Not Deliverable)

This `src/` exists because you asked for **BRD + minimal prototype** rather than documentation only.

**Rule from Week 2 Welcome:** W2 artefact is strictly the **BRD (11 sections, 30 activities, My First Analysis Note)**. Implementation is **out of scope** and deferred to W3–W5. This prototype is therefore marked **optional proof-of-concept** — it makes the BRD tangible without violating W2 scope.

## What is here
- `pipeline/bhuvan_fetch.py` — stub for Bhuvan/MOSDAC catalog access (writes `data/raw/manifest_stub.json`)
- `pipeline/eo_pipeline_stub.py` — ingest → preprocess → dummy inference → metrics → report (`data/processed/report_stub.json`)
- `notebooks/eo_exploration_stub.py` — one-file exploration note

All stubs use stdlib only. No credentials, no heavy downloads, no GPU.

## How to run (optional)
```bash
python src/pipeline/bhuvan_fetch.py --product Resourcesat-2_LISS3 --bbox 77,12,78,13
python src/pipeline/eo_pipeline_stub.py --input data/raw --output data/processed
python notebooks/eo_exploration_stub.py
```

## Traceability to BRD
- Problem (§3) → flood/crop use case context
- Requirements (§6 BR-03) → Bhuvan/MOSDAC data source
- Constraints (§8) → latency/compute noted in stub comments
- Metrics (§10) → report_stub.json contains time-to-insight, coverage, IoU placeholders

## What not to do in W2
Do not expand this into a real model. Real architecture, training, and evaluation belong to **RLD (W3) / VQRD (W4) / PRD (W5)**. If you paste code into the program Deliverable form, paste the BRD text (`docs/brd/brd-v0.2.md`), not this stub.

---
*Status: Stub only. Keeps W2 compliant while giving you something runnable.*
