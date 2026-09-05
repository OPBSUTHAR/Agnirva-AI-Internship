"""
notebooks/eo_exploration_stub.py — Lightweight exploration note (replaces .ipynb for portability).

Purpose: Give reviewers a one-file view of what the EO prototype would explore
without requiring heavy data or GPU. Converts to notebook by renaming.

Steps:
  1. Inspect mock Bhuvan manifest (data/raw/manifest_stub.json)
  2. Visualize tile coverage (stub — prints bbox)
  3. Note risks and next experiments for W3 RLD

Run:
  python notebooks/eo_exploration_stub.py
"""

import json
from pathlib import Path

manifest = Path("data/raw/manifest_stub.json")
if not manifest.exists():
    print("[stub] No manifest yet. Run: python src/pipeline/bhuvan_fetch.py")
    print("[stub] Then: python src/pipeline/eo_pipeline_stub.py")
else:
    data = json.loads(manifest.read_text())
    print("=== Mock Bhuvan Manifest ===")
    print(json.dumps(data, indent=2))
    print("\n[todo W3] Validate real Bhuvan catalog coverage for chosen use case")
    print("[todo W3] List 3 papers for RLD that justify model choice")
    print("[todo W4] Define VQRD quality gates for IoU, latency, coverage")
