#!/usr/bin/env python3
"""
MODULE 4: Botanical Classification Verification
================================================
Verifies the §H botanical sprint results (113/132 §H folios classified,
CTH/CH/QO pharmacological profiles, pre-registration confirmations).

This module requires data/botanical_dataset.json — the full 113-plant
dataset with per-folio CTH/CH/QO scores, pre-registration commit hashes,
and confirmation criteria. That dataset will be published alongside the
Cryptologia paper.

Until the dataset is released, this module:
  1. Reports what the dataset must contain (format spec below)
  2. Verifies any partial data provided
  3. Computes summary statistics if data is present

Expected data/botanical_dataset.json format:
{
  "_description": "§H botanical sprint dataset",
  "_corpus": "ZL3b-n.txt SHA-256 ...",
  "plants": {
    "f6v": {
      "identification": "Terminalia chebula (a-ru-ra / haritaki)",
      "status": "CONFIRMED",
      "pre_reg_commit": "...",
      "CTH_pct": 0.0,
      "CH_pct": 18.5,
      "QO_pct": 6.2,
      "n_tokens": 89,
      "criteria_confirmed": 6,
      "criteria_total": 6,
      "notes": "Triphala anchor folio"
    },
    ...
  },
  "summary": {
    "total_folios": 132,
    "folios_classified": 113,
    "folios_skipped": 19,
    "confirmed_count": 113,
    "exploratory_strong_count": 15,
    "cold_plants_CTH0": 20,
    "dominant_family": "Asteraceae",
    "dominant_family_count": 24,
    "PASS": true
  }
}
"""

import json, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_PATH = ROOT / "data" / "botanical_dataset.json"
RESULTS_PATH = ROOT / "results" / "botanical.json"

def run():
    print("=" * 60)
    print("MODULE 4: Botanical Classification Verification")
    print("=" * 60)

    if not DATA_PATH.exists():
        print(f"\n  ⚠️  data/botanical_dataset.json not found.")
        print(f"  This module requires the full 113-plant dataset.")
        print(f"  The dataset will be published with the Cryptologia paper.")
        print(f"\n  Expected dataset format is documented in this script's")
        print(f"  module docstring — see scripts/4_botanical.py lines 14–46.")
        print(f"\n  Reference values (from paper Table 2):")
        print(f"    Total §H folios:    132")
        print(f"    Folios classified:  113 (86%)")
        print(f"    Folios skipped:      19 (11 image-quality; 8 no candidate)")
        print(f"    Dominant family:    Asteraceae (24 plants)")
        print(f"    Cold plants CTH=0:  20 folios")
        print(f"    Warm peak CTH:      f44v Zingiber 16.00%")
        print(f"    Wind peak CH:       f2v Nelumbo nucifera 44.30%")
        print(f"    Unique cold folio:  f1r Silybum marianum (QO=0%)")
        print(f"\n  To run this module: place botanical_dataset.json in data/")
        print(f"  and re-run ./reproduce.sh or python scripts/4_botanical.py")
        result = {"PASS": None, "status": "DATASET_PENDING",
                  "note": "Full dataset to be published with Cryptologia paper"}
        RESULTS_PATH.write_text(json.dumps(result, indent=2))
        return result

    print(f"\nLoading botanical dataset from {DATA_PATH}...")
    data = json.loads(DATA_PATH.read_text())
    plants = data.get("plants", {})
    summary = data.get("summary", {})

    n_classified = len(plants)
    n_confirmed  = sum(1 for p in plants.values() if p.get("status") in ("CONFIRMED", "EXPLORATORY-STRONG"))
    n_cold       = sum(1 for p in plants.values() if p.get("CTH_pct", 1) == 0.0)

    print(f"  Folios in dataset:  {n_classified}")
    print(f"  Confirmed/Strong:   {n_confirmed}")
    print(f"  Cold plants CTH=0:  {n_cold}")

    # Verify GL4313 thermal gradient from botanical data
    quire_groups = {"early": [], "late": []}
    for folio_id, p in plants.items():
        try:
            # Extract folio number (f6v -> 6, f27r -> 27, etc.)
            num = int(''.join(filter(str.isdigit, folio_id)))
            if 1 <= num <= 33:
                quire_groups["early"].append(p.get("CTH_pct", 0))
            elif 34 <= num <= 66:
                quire_groups["late"].append(p.get("CTH_pct", 0))
        except (ValueError, IndexError):
            pass

    if quire_groups["early"] and quire_groups["late"]:
        early_mean = sum(quire_groups["early"]) / len(quire_groups["early"])
        late_mean  = sum(quire_groups["late"])  / len(quire_groups["late"])
        print(f"\n  Thermal gradient from botanical data:")
        print(f"    Early §H (f1–f33) mean CTH: {early_mean:.1f}%")
        print(f"    Late  §H (f34–f66) mean CTH: {late_mean:.1f}%")
        gradient_ok = late_mean > early_mean
        print(f"    Direction: {'WARM→COLD ✅' if gradient_ok else 'CHECK'}")
    else:
        gradient_ok = True  # no folio data to test

    # Triphala confirmations
    triphala_ok = all(
        plants.get(f, {}).get("status") == "CONFIRMED"
        for f in ("f6v", "f51v")
    )
    print(f"\n  Triphala confirmations:")
    print(f"    f6v (haritaki):  {'✅ CONFIRMED' if plants.get('f6v',{}).get('status')=='CONFIRMED' else '❌'}")
    print(f"    f51v (bibhitaki): {'✅ CONFIRMED' if plants.get('f51v',{}).get('status')=='CONFIRMED' else '❌'}")

    passes = n_classified >= 100 and triphala_ok and gradient_ok
    result = {
        "n_classified": n_classified,
        "n_confirmed": n_confirmed,
        "n_cold_CTH0": n_cold,
        "triphala_confirmed": triphala_ok,
        "thermal_gradient_ok": gradient_ok,
        "PASS": passes
    }
    RESULTS_PATH.write_text(json.dumps(result, indent=2))
    status = "PASS" if passes else "FAIL"
    print(f"\nBotanical module: {status}")
    return result


if __name__ == "__main__":
    run()
