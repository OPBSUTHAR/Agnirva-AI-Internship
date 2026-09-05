"""
bhuvan_fetch.py — Minimal prototype stub for W2 BRD validation (optional, not W2 deliverable).

Purpose: Demonstrate how Bhuvan/MOSDAC data would be accessed for the BRD use case
(flood mapping / crop monitoring). This stub is NOT the pipeline implementation;
full pipeline is deferred to W5 PRD. Keep it inside BRD scope as proof-of-concept.

Usage:
  python src/pipeline/bhuvan_fetch.py --help

References:
  - Bhuvan: https://bhuvan.nrsc.gov.in (accessed 2026-09-05)
  - MOSDAC: https://www.mosdac.gov.in (accessed 2026-09-05)
"""

import argparse
from pathlib import Path


def fetch_bhuvan_catalog_stub(product: str = "Resourcesat-2_LISS3", bbox: str = "77,12,78,13") -> dict:
    """
    Stub: In production, call Bhuvan API / download via NRSC.
    Here we return mock metadata so BRD reviewers can see the data contract
    without needing credentials or heavy downloads.
    """
    return {
        "product": product,
        "bbox": bbox,
        "mock_tiles": 3,
        "crs": "EPSG:4326",
        "note": "Stub — replace with actual Bhuvan/NRSC API call in W5. See BRD §8 Constraints.",
        "next_step": "Validate catalog access and cite URL+date in docs/brd/brd-v0.2.md §11",
    }


def main():
    parser = argparse.ArgumentParser(description="Bhuvan fetch stub — BRD proof-of-concept")
    parser.add_argument("--product", default="Resourcesat-2_LISS3", help="Bhuvan product name")
    parser.add_argument("--bbox", default="77,12,78,13", help="BBOX as lon_min,lat_min,lon_max,lat_max")
    parser.add_argument("--out", default="data/raw", help="Output directory (mock)")
    args = parser.parse_args()

    result = fetch_bhuvan_catalog_stub(args.product, args.bbox)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    # Write mock manifest so prototype looks tangible but stays lightweight
    manifest = out / "manifest_stub.json"
    import json
    manifest.write_text(json.dumps(result, indent=2))
    print(f"[stub] Would fetch {result['product']} for bbox {result['bbox']}")
    print(f"[stub] Wrote mock manifest to {manifest}")
    print(f"[stub] Note: {result['note']}")


if __name__ == "__main__":
    main()
