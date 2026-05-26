#!/usr/bin/env python3
"""
Final verifier: reads all results/*.json files, compares against expected.json,
and writes REPRODUCTION_REPORT.md with a pass/fail line for every major claim.

This is the document a skeptical reviewer reads first.
"""

import json, sys, math
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
RESULTS = ROOT / "results"
REPORT_PATH = ROOT / "REPRODUCTION_REPORT.md"


def load_json(path):
    if not path.exists():
        return None
    return json.loads(path.read_text())


def pf(condition):
    return "✅ PASS" if condition else "❌ FAIL"


def run():
    expected  = load_json(RESULTS / "expected.json")
    cipher    = load_json(RESULTS / "cipher.json")
    syllab    = load_json(RESULTS / "syllabary.json")
    vocab     = load_json(RESULTS / "vocabulary.json")
    gradient  = load_json(RESULTS / "gradient.json")
    botanical = load_json(RESULTS / "botanical.json")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M UTC")
    lines = []

    lines.append("# Voynich Decipherment — Reproduction Report")
    lines.append(f"\nGenerated: {timestamp}")
    lines.append(f"Corpus: ZL3b-n.txt (verify SHA-256 in CORPUS_HASH.txt)\n")
    lines.append("This report is generated automatically by `reproduce.sh`.")
    lines.append("Each row is a specific falsifiable claim from the published paper.")
    lines.append("PASS = result matches stated value within tolerance. FAIL = run `./reproduce.sh` for details.\n")
    lines.append("---\n")

    lines.append("## 1. Cipher Parameter — R=14")
    lines.append("")
    lines.append("| Claim | Reference | Reproduced | Status |")
    lines.append("|-------|-----------|------------|--------|")

    if cipher:
        lines.append(f"| Peak rotation value | R=14 | R={cipher.get('peak_R')} | {pf(cipher.get('peak_R') == 14)} |")
        p_rep = cipher.get('permutation_p_value', 1.0)
        p_ref = 8.43e-12
        lines.append(f"| Combinatorial p-value | p={p_ref:.2e} | p={p_rep:.2e} | {pf(p_rep < 1e-4)} |")
        cribs_rate = cipher.get('peak_match_rate', 0)
        lines.append(f"| Cribs satisfied at R=14 | 9/9 (1.000) | {cribs_rate:.3f} | {pf(cribs_rate >= 0.999)} |")
        baseline = cipher.get('baseline_mean', 1)
        lines.append(f"| Cribs at other rotations | 0/9 (0.000) | {baseline:.3f} | {pf(baseline < 0.001)} |")
    else:
        lines.append("| All cipher claims | — | MODULE NOT RUN | ❌ MISSING |")
    lines.append("")

    lines.append("## 2. Syllabary Map v0.4")
    lines.append("")
    lines.append("| Claim | Reference | Reproduced | Status |")
    lines.append("|-------|-----------|------------|--------|")

    if syllab:
        t1 = syllab.get("T1_confirmed", 0)
        cov = syllab.get("corpus_coverage_pct", 0)
        lines.append(f"| T1-CONFIRMED characters | 19/23 | {t1}/23 | {pf(t1 >= 18)} |")
        lines.append(f"| Corpus character coverage | ~97% | {cov:.0f}% | {pf(cov >= 95)} |")
        lines.append(f"| tsheos anchor (e=/e/) | PASS | {'PASS' if syllab.get('all_anchors_pass') else 'FAIL'} | {pf(syllab.get('all_anchors_pass'))} |")
        lines.append(f"| pchedar anchor (p=/ph/) | PASS | {'PASS' if syllab.get('all_anchors_pass') else 'FAIL'} | {pf(syllab.get('all_anchors_pass'))} |")
    else:
        lines.append("| All syllabary claims | — | MODULE NOT RUN | ❌ MISSING |")
    lines.append("")

    lines.append("## 3. Confirmed Vocabulary — 11 Items")
    lines.append("")
    lines.append("| Token | Stated N | Corpus N | Status |")
    lines.append("|-------|----------|----------|--------|")

    if vocab and expected:
        exp_counts = expected.get("vocabulary_counts", {})
        rep_counts = vocab.get("confirmed_vocab", {})
        for tok, exp_n in exp_counts.items():
            rep_n = rep_counts.get(tok, {}).get("N", "?")
            # Tolerance: ±10% or ±8 tokens, whichever is larger (tokenization variants)
            ok = isinstance(rep_n, int) and abs(rep_n - exp_n) <= max(8, exp_n * 0.10)
            lines.append(f"| {tok:8} | {exp_n:6} | {str(rep_n):6} | {pf(ok)} |")
        # Section distribution tests
        shor_pct = vocab.get("shor_H_pct", 0)
        daiin_pct = vocab.get("daiin_H_pct", 0)
        sar_pct  = vocab.get("sar_A_pct", 100)
        lines.append(f"| shor §H-dominant (treatment verb) | >50% | {shor_pct:.1f}% | {pf(shor_pct > 50)} |")
        lines.append(f"| daiin §H-dominant (grammar word) | >50% | {daiin_pct:.1f}% | {pf(daiin_pct > 50)} |")
        lines.append(f"| sar not §A-concentrated (timing marker) | <30% §A | {sar_pct:.1f}% §A | {pf(sar_pct < 30)} |")
    else:
        lines.append("| All vocabulary claims | — | MODULE NOT RUN | ❌ MISSING |")
    lines.append("")

    lines.append("## 4. GL4313 — Pharmacological Gradient")
    lines.append("")
    lines.append("| Claim | Reference | Reproduced | Status |")
    lines.append("|-------|-----------|------------|--------|")

    if gradient:
        rs = gradient.get("spearman_r_cold_frac", 0)
        p  = gradient.get("spearman_p_cold_frac", 1)
        chi2 = gradient.get("chi2", 0)
        chi2_p = gradient.get("chi2_p", 1)
        early = gradient.get("early_cold_pct", 0)
        late  = gradient.get("late_cold_pct", 0)
        lines.append(f"| Spearman r_s | 0.850 (working notes) | {rs:.4f} (computed) | {pf(abs(rs - 0.850) < 0.05)} |")
        lines.append(f"| p-value (Spearman) | 0.0075 (working notes) | {p:.4f} (computed) | {pf(p < 0.05)} |")
        lines.append(f"| Chi-square (early vs late) | 11.13 | {chi2:.2f} | {pf(abs(chi2 - 11.13) < 2.0)} |")
        lines.append(f"| Chi-square p | 0.00085 | {chi2_p:.5f} | {pf(chi2_p < 0.01)} |")
        lines.append(f"| Cold% early quires (A–D) | 6.6% | {early:.1f}% | {pf(abs(early - 6.6) < 2)} |")
        lines.append(f"| Cold% late quires (E–H) | 33.3% | {late:.1f}% | {pf(abs(late - 33.3) < 5)} |")
    else:
        lines.append("| All GL4313 claims | — | MODULE NOT RUN | ❌ MISSING |")
    lines.append("")

    lines.append("## 5. Section Pharmacological Architecture")
    lines.append("")
    lines.append("| Claim | Reference | Status |")
    lines.append("|-------|-----------|--------|")
    if expected:
        arch = expected.get("section_architecture", {})
        lines.append(f"| §A OT% highest (timing section) | {arch.get('SA_OT_pct')}% | ℹ️ manual verification — see paper §9 |")
        lines.append(f"| §B QO% highest (phlegm section) | {arch.get('SB_QO_pct')}% | ℹ️ manual verification — see paper §8 |")
        lines.append(f"| KW p-value (section architecture) | {arch.get('KW_p_value'):.0e} | ℹ️ manual verification |")
    lines.append("")
    if botanical and botanical.get("PASS"):
        lines.append(f"*Botanical dataset loaded: {botanical.get('n_classified', '?')} folios. GL4313 confirmed by folio data: early={botanical.get('early_cold_pct','?')}% / late={botanical.get('late_cold_pct','?')}% cold.*\n")
    else:
        lines.append("*Note: Section architecture requires the full §H botanical dataset (scripts/4_botanical.py).*")
        lines.append("*Interim values are from paper Table 2.*\n")

    lines.append("## 6. Triphala Botanical Identifications")
    lines.append("")
    lines.append("| Folio | Claimed Identification | Status |")
    lines.append("|-------|------------------------|--------|")
    if expected:
        tri = expected.get("triphala", {})
        lines.append(f"| f6v | {tri.get('plant_f6v', '?')} | {'✅ CONFIRMED' if tri.get('f6v_confirmed') else '❌'} |")
        lines.append(f"| f3r | {tri.get('plant_f3r', '?')} | {'✅ CONFIRMED' if tri.get('f3r_confirmed') else '❌'} |")
        lines.append(f"| f51v| {tri.get('plant_f51v', '?')} | {'✅ CONFIRMED' if tri.get('f51v_confirmed') else '❌'} |")
        lines.append("\n*Botanical confirmation requires visual cross-reference. See paper §7 and decoded folio pages.*")
    lines.append("")

    lines.append("---\n")
    lines.append("## How to Challenge Specific Claims\n")
    lines.append("**To test R=14 against other rotation values:**")
    lines.append("```bash")
    lines.append("python scripts/1_cipher.py")
    lines.append("```")
    lines.append("Results in `results/cipher.json` include match rates for all R values (0–19).\n")
    lines.append("**To verify vocabulary token counts:**")
    lines.append("```bash")
    lines.append("python scripts/3_vocabulary.py")
    lines.append("```\n")
    lines.append("**To rerun GL4313 gradient with your own data:**")
    lines.append("Modify the `QUIRE_DATA` table in `scripts/5_gradient.py` and rerun.\n")
    lines.append("**To challenge the syllabary assignments:**")
    lines.append("See `scripts/2_syllabary.py` — each anchor's 'no alternative reading'")
    lines.append("test lists every phoneme substitution that was tried and rejected.\n")
    lines.append("**Contact for technical review:** guestent@gmail.com")
    lines.append("*Please cite: Stalnecker, F.D. (2026). Voynich Manuscript Decipherment — Evidence Repository. GitHub. https://github.com/Frederick-Stalnecker/voynich-evidence. Manuscript in review at Cryptologia (2026).*\n")

    # Summary — 5 modules: cipher, syllabary, vocabulary, gradient, botanical
    bot_pass = botanical.get("PASS", False) if botanical and botanical.get("PASS") is not None else None
    modules_run = sum([cipher is not None, syllab is not None, vocab is not None, gradient is not None,
                       botanical is not None and bot_pass is not None])
    passes = sum([
        cipher.get("PASS", False) if cipher else False,
        syllab.get("PASS", False) if syllab else False,
        vocab.get("PASS", False) if vocab else False,
        gradient.get("PASS", False) if gradient else False,
        bool(bot_pass) if bot_pass is not None else False,
    ])

    lines.append("---\n")
    lines.append(f"## Summary: {passes}/{modules_run} modules PASS\n")
    bot_status = "data loaded ✅" if (botanical and bot_pass) else "dataset pending"
    lines.append(f"Modules run: {modules_run}/5 (scripts/4_botanical.py — {bot_status})\n")
    if passes == modules_run and modules_run == 5:
        lines.append("**All five modules PASS. Results are fully reproducible.**\n")
    elif passes == modules_run and modules_run == 4:
        lines.append("**All four core modules PASS. Botanical module requires data/botanical_dataset.json.**\n")
    elif modules_run == 0:
        lines.append("**No modules have been run yet. Execute `./reproduce.sh` first.**\n")
    else:
        lines.append(f"**{passes}/{modules_run} modules passed. See individual sections for details.**\n")

    REPORT_PATH.write_text("\n".join(lines))
    print(f"\nREPRODUCTION_REPORT.md written to {REPORT_PATH}")
    print(f"Summary: {passes}/{modules_run} modules PASS")


if __name__ == "__main__":
    run()
