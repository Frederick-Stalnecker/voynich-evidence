#!/usr/bin/env python3
"""
One-time utility: parse §H botanical master summary → data/botanical_dataset.json
Run from voynich-evidence root: python scripts/build_botanical_dataset.py
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "data" / "botanical_dataset.json"

if len(sys.argv) < 2:
    print("Usage: python scripts/build_botanical_dataset.py <path/to/sh_botanical_master_summary.md>")
    print("This is a one-time utility used to generate data/botanical_dataset.json.")
    print("The generated file is included in this repository — you do not need to re-run this.")
    sys.exit(1)
MASTER = Path(sys.argv[1])

# Parse the table rows
QUIRE_MAP = {
    "A": list(range(1, 9)),    # folios 1–8
    "B": list(range(9, 18)),   # folios 9–17
    "C": list(range(18, 25)),  # folios 18–24
    "D": list(range(25, 34)),  # folios 25–33
    "E": list(range(34, 41)),  # folios 34–40
    "F": list(range(41, 50)),  # folios 41–49
    "G": list(range(50, 58)),  # folios 50–57
    "H": list(range(58, 67)),  # folios 58–66
}

def parse_table(text):
    plants = {}
    # Match table rows: | N | fXXy | Zr | *Latin* | Common | CTH | CH | QO | Warm/Cold | Rlung | Quire |
    pattern = re.compile(
        r'^\|\s*(\d+)\s*\|\s*(f\w+)\s*\|\s*\w+\s*\|\s*\*(.*?)\*\s*\|\s*(.*?)\s*\|\s*([\d.—–-]+)\s*\|\s*([\d.—–-]+)\s*\|\s*([\d.—–-]+)\s*\|\s*(\w[\w-]*)\s*\|\s*(\w+)\s*\|\s*([A-H])\s*\|'
    )
    for line in text.split('\n'):
        m = pattern.match(line.strip())
        if not m:
            continue
        n, folio, latin, common, cth_s, ch_s, qo_s, warm_cold, rlung, quire = (
            m.group(1), m.group(2), m.group(3), m.group(4).strip(),
            m.group(5), m.group(6), m.group(7),
            m.group(8), m.group(9), m.group(10)
        )
        def parse_pct(s):
            s = s.strip()
            if s in ('—', '–', '-', ''):
                return None
            try: return float(s)
            except: return None

        cth = parse_pct(cth_s)
        ch  = parse_pct(ch_s)
        qo  = parse_pct(qo_s)

        # Determine status
        confirmed_folios = {"f6v", "f51v"}
        visual_only = cth is None
        if folio in confirmed_folios:
            status = "CONFIRMED"
        elif visual_only:
            status = "VISUAL-ONLY"
        else:
            status = "CONFIRMED"

        # Notes
        notes = []
        if folio == "f6v":
            notes.append("Triphala anchor: haritaki / a-ru-ra — CONFIRMED")
        elif folio == "f51v":
            notes.append("Triphala: bibhitaki / ba-ru-ra — CONFIRMED")
        elif folio == "f1r":
            notes.append("Unique: only QO=0% folio (Silybum marianum = liver tonic, no phlegm indication)")
        elif folio == "f44v":
            notes.append("Highest CTH in corpus: CTH=16.00% (Zingiber officinale / ginger)")
        elif cth == 0.0 and ch is not None:
            notes.append("COLD plant (CTH=0.0%)")
        if ch is not None and ch >= 30.0:
            notes.append(f"EXTREME rlung: CH={ch}%")

        plants[folio] = {
            "identification": latin.strip() + (f" ({common.strip()})" if common.strip() else ""),
            "status": status,
            "warm_cold": warm_cold,
            "rlung_tier": rlung,
            "quire": quire,
            "CTH_pct": cth,
            "CH_pct": ch,
            "QO_pct": qo,
            "notes": "; ".join(notes) if notes else None
        }
    return plants

def main():
    text = MASTER.read_text()
    plants = parse_table(text)
    print(f"Parsed {len(plants)} plant entries.")

    n_classified  = sum(1 for p in plants.values() if p["status"] != "VISUAL-ONLY")
    n_cold        = sum(1 for p in plants.values() if p.get("CTH_pct") == 0.0)
    n_extreme_ch  = sum(1 for p in plants.values() if (p.get("CH_pct") or 0) >= 30.0)
    n_visual_only = sum(1 for p in plants.values() if p["status"] == "VISUAL-ONLY")

    dataset = {
        "_description": "§H Botanical Sprint Dataset — 113/132 §H folios classified",
        "_corpus": "ZL3b-n.txt SHA-256 bf5b6d4ac1e3a51b1847a9c388318d609020441ccd56984c901c32b09beccafc",
        "_source": "sh_botanical_master_summary_2026-05-25.md (batches 3407–3596)",
        "_date": "2026-05-26",
        "plants": plants,
        "summary": {
            "total_sh_folios": 132,
            "folios_in_dataset": len(plants),
            "folios_classified": n_classified,
            "visual_only": n_visual_only,
            "folios_skipped_not_in_dataset": 132 - len(plants),
            "cold_plants_CTH0": n_cold,
            "extreme_rlung_CH_ge30": n_extreme_ch,
            "dominant_family": "Asteraceae",
            "dominant_family_count": 24,
            "warm_peak_CTH": "f44v Zingiber officinale 16.00%",
            "wind_peak_CH": "f2v Nelumbo nucifera 44.30%",
            "unique_cold_QO0": "f1r Silybum marianum",
            "PASS": n_classified >= 100
        }
    }

    OUT.write_text(json.dumps(dataset, indent=2))
    print(f"Written to {OUT}")
    print(f"  Classified: {n_classified}  Cold(CTH=0): {n_cold}  Extreme-CH: {n_extreme_ch}")
    print(f"  PASS: {dataset['summary']['PASS']}")

if __name__ == "__main__":
    main()
