"""
eo_pipeline_stub.py — EO pipeline proof-of-concept stub (W2 optional).

Stages mirrored for BRD traceability:
  ingest (bhuvan_fetch.py) → preprocess → inference (dummy) → metrics → report

This file stays minimal on purpose: W2 is BRD week. Real model and
evaluation move to W3 RLD / W4 VQRD / W5 PRD. The stub exists so the BRD's
Problem (§3), Requirements (§6), and Success Metrics (§10) have a runnable
anchor without violating W2 scope.

Run:
  python src/pipeline/eo_pipeline_stub.py --input data/raw --output data/processed
"""

import argparse
import json
from pathlib import Path


def preprocess_stub(input_dir: Path) -> dict:
    manifest = input_dir / "manifest_stub.json"
    if not manifest.exists():
        return {"status": "no_input", "hint": "Run bhuvan_fetch.py first to create data/raw/manifest_stub.json"}
    data = json.loads(manifest.read_text())
    return {"status": "preprocessed", "tiles": data.get("mock_tiles", 0), "crs": data.get("crs", "EPSG:4326")}


def inference_stub(preprocessed: dict) -> dict:
    # Dummy inference — returns fixed metrics so BRD §10 can be demonstrated
    return {
        "model": "dummy_unet_stub",
        "iou_mock": 0.0,
        "note": "Replace with real segmentation in W5. BRD requires metric to be accuracy + time-to-insight + coverage.",
        "preprocessed": preprocessed,
    }


def metrics_stub(inference: dict) -> dict:
    # Aligns to BRD §10 Success Metrics
    return {
        "accuracy_iou": inference["iou_mock"],
        "time_to_insight_hours_mock": 2.5,
        "coverage_km2_mock": 1200,
        "cost_inr_mock": 0,
        "completeness_check": "BRD §10 requires all 11 sections filled — see docs/brd/brd-v0.2.md",
    }


def main():
    parser = argparse.ArgumentParser(description="EO pipeline stub — BRD proof-of-concept")
    parser.add_argument("--input", default="data/raw", help="Input dir with manifest_stub.json")
    parser.add_argument("--output", default="data/processed", help="Output dir")
    args = parser.parse_args()

    inp = Path(args.input)
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    pre = preprocess_stub(inp)
    inf = inference_stub(pre)
    met = metrics_stub(inf)

    report = {"preprocess": pre, "inference": inf, "metrics": met}
    report_path = out / "report_stub.json"
    report_path.write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))
    print(f"[stub] Wrote report to {report_path}")


if __name__ == "__main__":
    main()
