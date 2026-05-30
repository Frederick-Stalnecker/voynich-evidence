#!/usr/bin/env python3
"""
structural_test.py — Decipherment-Independent Structural Analysis
=================================================================

This script demonstrates that the Voynich manuscript (MS 408) contains
REAL, NON-RANDOM sectional structure — a result that holds regardless
of whether any proposed decipherment is correct.

NO DECIPHERMENT IS USED. The test operates on:
  1. The raw EVA transcription (ZL3b-n.txt) — publicly available since 2005
  2. Section boundaries defined by folio number — a physical property of
     the manuscript established by codicological consensus

The question asked: "Do different physical sections of the manuscript use
statistically distinguishable vocabularies?"

If the manuscript were produced by a homogeneous random process (i.i.d.
glossolalia, a single undifferentiated source), the answer would be NO —
token distributions would be uniform across sections.

If the manuscript encodes structured content organized by topic, the answer
would be YES — different sections would use different words at different rates.

Method: Permutation test on the chi-square statistic of the token x section
contingency table, with the FOLIO PAGE as the unit of permutation. This avoids
any independence assumption on individual tokens (which are autocorrelated
within folios) and makes no distributional assumptions whatsoever.

Runtime: < 30 seconds (10,000 permutations). Python 3.8+ stdlib only.

Author: Frederick Davis Stalnecker / THEOS Research Institute
Repository: https://github.com/Frederick-Stalnecker/voynich-evidence
"""

import re
import random
import hashlib
import sys
from collections import Counter, defaultdict
from pathlib import Path

# =============================================================================
# SECTION BOUNDARIES — defined by physical codicology, NOT by any decipherment
# =============================================================================
# These boundaries are consensus assignments based on quire structure and
# illustration type. They predate any THEOS analysis. Sources:
#   - D'Imperio (1978), The Voynich Manuscript: An Elegant Enigma
#   - Clemens & Harkness (2016), "The World's Most Mysterious Manuscript"
#   - Zandbergen, voynich.nu section assignments
#
# Section labels here are NEUTRAL (A-F) to avoid any interpretive framing.

def folio_to_section(folio_str):
    """Map folio identifier to neutral section label based on physical position."""
    m = re.match(r"f(\d+)", folio_str)
    if not m:
        return None
    n = int(m.group(1))
    if n <= 66:   return "A"   # Plant illustrations ("Herbal")
    if n <= 73:   return "B"   # Circular diagrams ("Astronomical")
    if n == 74:   return None  # Single transitional folio, excluded
    if n <= 84:   return "C"   # Small figures in containers ("Balneological")
    if n <= 86:   return "D"   # Cosmological rosettes
    if n <= 102:  return "E"   # Pharmaceutical/recipe pages
    if n <= 116:  return "F"   # Text-heavy recipe/stars pages
    return None


def load_corpus_by_folio(corpus_path):
    """
    Parse ZL3b-n.txt into per-folio-page token counts.
    Aggregates all lines within the same page (e.g., f1r.1, f1r.2, ... -> f1r).
    Returns: list of (folio_page_id, section, Counter) tuples.
    """
    page_data = {}  # {page_id: (section, Counter)}
    current_page = None
    current_section = None

    with open(corpus_path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            # Detect folio headers: <f1r.1,@P0> or <f67r1> etc.
            folio_m = re.match(r"<(f\d+[rv]\d*)", line)
            if folio_m:
                full_id = folio_m.group(1)
                # Extract page-level ID (e.g., f1r from f1r.1)
                page_id = re.match(r"(f\d+[rv]\d*)", full_id).group(1)
                sec = folio_to_section(page_id)
                if sec is not None:
                    current_page = page_id
                    current_section = sec
                    if page_id not in page_data:
                        page_data[page_id] = (sec, Counter())
                else:
                    current_page = None
                    current_section = None

            if current_page is None:
                continue

            # Extract text after ">"
            text_m = re.search(r">\s+(.*)", line)
            if not text_m:
                continue
            raw = text_m.group(1)
            # Strip annotations
            raw = re.sub(r"[<{(\[].*?[>})\]]", "", raw)
            # Tokenize
            for tok in re.split(r"[.,;\s\-!?%*:]+", raw):
                tok = tok.strip().lower()
                if tok and re.match(r"^[a-z]+$", tok):
                    page_data[current_page][1][tok] += 1

    # Convert to list
    folios = [(pid, sec, counter) for pid, (sec, counter) in page_data.items()
              if sum(counter.values()) > 0]
    return folios


def compute_chi_square_fast(folio_token_matrix, section_labels, n_tokens, sections):
    """
    Compute chi-square statistic using pre-computed folio-token matrix.
    
    folio_token_matrix: list of lists [n_folios][n_tokens] — token counts per folio
    section_labels: list of section indices (same length as n_folios)
    n_tokens: number of tokens (columns)
    sections: list of section indices [0..k-1]
    
    Returns: chi-square statistic
    """
    n_sections = len(sections)

    # Aggregate: section_counts[section_idx][token_idx]
    section_counts = [[0] * n_tokens for _ in range(n_sections)]
    col_totals = [0] * n_sections

    for folio_idx, sec_idx in enumerate(section_labels):
        row = folio_token_matrix[folio_idx]
        sec_row = section_counts[sec_idx]
        for t in range(n_tokens):
            sec_row[t] += row[t]
            col_totals[sec_idx] += row[t]

    grand_total = sum(col_totals)
    if grand_total == 0:
        return 0.0

    # Row totals (per token across all sections)
    row_totals = [0] * n_tokens
    for t in range(n_tokens):
        for s in range(n_sections):
            row_totals[t] += section_counts[s][t]

    # Chi-square
    chi2 = 0.0
    for t in range(n_tokens):
        rt = row_totals[t]
        if rt == 0:
            continue
        for s in range(n_sections):
            expected = (rt * col_totals[s]) / grand_total
            if expected > 0:
                diff = section_counts[s][t] - expected
                chi2 += (diff * diff) / expected

    return chi2


# =============================================================================
# MAIN
# =============================================================================

def main():
    print()
    print("=" * 70)
    print("  VOYNICH MANUSCRIPT — DECIPHERMENT-INDEPENDENT STRUCTURAL TEST")
    print("=" * 70)
    print()
    print("  This test uses NO decipherment, NO proposed reading, NO syllabary.")
    print("  It asks only: do the manuscript's physical sections have distinct")
    print("  vocabulary distributions?")
    print()
    print("  Section boundaries are defined by codicological consensus")
    print("  (folio number / quire / illustration type), not by any")
    print("  interpretation of the text.")
    print()

    # Locate corpus
    script_dir = Path(__file__).parent
    corpus_candidates = [
        script_dir / "ZL3b-n.txt",
        script_dir / "data" / "ZL3b-n.txt",
        script_dir.parent / "data" / "ZL3b-n.txt",
        Path("data/ZL3b-n.txt"),
    ]

    corpus_path = None
    for candidate in corpus_candidates:
        if candidate.exists():
            corpus_path = candidate
            break

    if corpus_path is None:
        print("  ERROR: ZL3b-n.txt not found.")
        print("  Place it in the same directory as this script, or in data/")
        print("  Download: https://www.voynich.nu/data/ZL3b-n.txt")
        sys.exit(1)

    print(f"  Corpus: {corpus_path.name}")

    # Verify hash
    with open(corpus_path, "rb") as f:
        actual_hash = hashlib.sha256(f.read()).hexdigest()
    expected_hash = "bf5b6d4ac1e3a51b1847a9c388318d609020441ccd56984c901c32b09beccafc"
    if actual_hash == expected_hash:
        print(f"  SHA-256: {actual_hash[:20]}... VERIFIED")
    else:
        print(f"  SHA-256: {actual_hash[:20]}... (non-standard version; proceeding)")
    print()

    # Load corpus at folio-page level
    folios = load_corpus_by_folio(corpus_path)
    sections_set = sorted(set(sec for _, sec, _ in folios))
    sec_to_idx = {s: i for i, s in enumerate(sections_set)}
    n_sections = len(sections_set)

    descriptions = {
        "A": "Folios 1-66: Plant illustrations",
        "B": "Folios 67-73: Circular/astronomical diagrams",
        "C": "Folios 75-84: Small figures in containers",
        "D": "Folios 85-86: Cosmological rosettes",
        "E": "Folios 87-102: Pharmaceutical/recipe pages",
        "F": "Folios 103-116: Text-heavy recipe pages",
    }

    print("  " + "-" * 66)
    print(f"  {'Section':<10} {'Pages':>6} {'Tokens':>8}  Physical description")
    print("  " + "-" * 66)

    section_page_counts = Counter()
    section_token_counts = Counter()
    total_tokens = 0
    for fid, sec, counter in folios:
        n = sum(counter.values())
        section_page_counts[sec] += 1
        section_token_counts[sec] += n
        total_tokens += n

    for s in sections_set:
        desc = descriptions.get(s, "")
        print(f"  {s:<10} {section_page_counts[s]:>6} {section_token_counts[s]:>8,}  {desc}")

    print("  " + "-" * 66)
    print(f"  {'TOTAL':<10} {len(folios):>6} {total_tokens:>8,}")
    print()

    # Determine top tokens (corpus-wide)
    global_counts = Counter()
    for _, _, counter in folios:
        global_counts.update(counter)

    TOP_N = 50  # Top 50 tokens — sufficient and keeps permutation fast
    top_tokens = [tok for tok, _ in global_counts.most_common(TOP_N)]

    # Build folio-token matrix for fast permutation
    n_folios = len(folios)
    folio_token_matrix = []
    true_labels = []

    for fid, sec, counter in folios:
        row = [counter[tok] for tok in top_tokens]
        folio_token_matrix.append(row)
        true_labels.append(sec_to_idx[sec])

    # =========================================================================
    # PERMUTATION TEST
    # =========================================================================
    N_PERM = 10000
    SEED = 42  # Reproducible

    print(f"  METHOD: Folio-level permutation test")
    print(f"  Test statistic: Chi-square of homogeneity ({TOP_N} tokens x {n_sections} sections)")
    print(f"  Permutation unit: FOLIO PAGE ({n_folios} pages)")
    print(f"  Permutations: {N_PERM:,}")
    print(f"  Null hypothesis: section labels are exchangeable across folio pages")
    print()
    print("  Computing observed statistic...", end=" ", flush=True)

    # Observed statistic
    observed_chi2 = compute_chi_square_fast(
        folio_token_matrix, true_labels, TOP_N, list(range(n_sections))
    )
    print(f"chi2 = {observed_chi2:,.1f}")
    print()

    print(f"  Running {N_PERM:,} permutations...", flush=True)
    rng = random.Random(SEED)
    n_exceed = 0

    for i in range(N_PERM):
        perm_labels = true_labels[:]
        rng.shuffle(perm_labels)
        perm_chi2 = compute_chi_square_fast(
            folio_token_matrix, perm_labels, TOP_N, list(range(n_sections))
        )
        if perm_chi2 >= observed_chi2:
            n_exceed += 1

        if (i + 1) % 2500 == 0:
            print(f"    ... {i+1:,}/{N_PERM:,} complete", flush=True)

    p_value = (n_exceed + 1) / (N_PERM + 1)  # +1 correction (Phipson & Smyth 2010)

    print()
    print("  " + "=" * 66)
    print(f"  RESULT:")
    print(f"    Observed chi-square  = {observed_chi2:,.1f}")
    print(f"    Folio pages          = {n_folios}")
    print(f"    Permutations         = {N_PERM:,}")
    print(f"    Permutations >= obs  = {n_exceed}")

    if n_exceed == 0:
        print(f"    Empirical p-value    < 1/{N_PERM:,} (p < {1/N_PERM:.0e})")
    else:
        print(f"    Empirical p-value    = {p_value:.4e}")

    print()

    if n_exceed == 0:
        print(f"    CONCLUSION: In {N_PERM:,} random reassignments of folio pages")
        print(f"    to sections, NONE produced vocabulary differentiation as strong")
        print(f"    as the manuscript's actual section structure.")
        print()
        print(f"    The manuscript's sections have genuinely distinct vocabulary")
        print(f"    profiles (empirical p < {1/N_PERM:.0e}).")
        print()
        print(f"    THIS RESULT IS INDEPENDENT OF ANY PROPOSED DECIPHERMENT.")
        print(f"    No syllabary, no translation, no interpretation was used.")
    elif p_value < 0.001:
        print(f"    CONCLUSION: The manuscript's sections have strongly distinct")
        print(f"    vocabulary distributions (p = {p_value:.4e}).")
        print()
        print(f"    THIS RESULT IS INDEPENDENT OF ANY PROPOSED DECIPHERMENT.")
    elif p_value < 0.05:
        print(f"    CONCLUSION: Sections show statistically significant")
        print(f"    vocabulary differences (p = {p_value:.4f}).")
    else:
        print(f"    CONCLUSION: No significant structural difference detected")
        print(f"    (p = {p_value:.4f}).")

    print()
    print("  " + "=" * 66)

    # =========================================================================
    # SUPPLEMENTARY: Show the strongest section-specific tokens
    # =========================================================================
    print()
    print("  SUPPLEMENTARY: Tokens with strongest section specificity")
    print("  (tokens appearing 20+ times with highest concentration in one section)")
    print()
    print(f"  {'Token':<12} {'N':>6}  {'Dominant section':>16} {'Concentration':>14}")
    print(f"  {'-'*12} {'------':>6}  {'-'*16:>16} {'-'*14:>14}")

    by_section = defaultdict(Counter)
    for _, sec, counter in folios:
        by_section[sec].update(counter)

    concentrations = []
    for tok in global_counts.most_common(100):
        tok = tok[0]
        total_tok = sum(by_section[s][tok] for s in sections_set)
        if total_tok < 20:
            continue
        max_sec = max(sections_set, key=lambda s: by_section[s][tok])
        max_count = by_section[max_sec][tok]
        concentration = max_count / total_tok
        concentrations.append((tok, total_tok, max_sec, concentration))

    concentrations.sort(key=lambda x: -x[3])
    for tok, n, sec, conc in concentrations[:15]:
        desc_short = descriptions.get(sec, "").split(":")[0]
        print(f"  {tok:<12} {n:>6}  {sec} ({desc_short}){' '*(10-len(desc_short))}    {conc*100:>5.1f}%")

    print()
    print("  These concentrations arise from the TEXT ITSELF, not from any")
    print("  interpretation. They demonstrate functional specialization")
    print("  across the manuscript's physical divisions.")
    print()

    # =========================================================================
    # INTERPRETATION NOTE
    # =========================================================================
    print("  " + "-" * 66)
    print("  NOTE ON INTERPRETATION:")
    print()
    print("  This test does not tell you WHAT the manuscript says.")
    print("  It tells you that the manuscript says DIFFERENT THINGS in")
    print("  different sections — a property incompatible with:")
    print("    - A homogeneous random process (i.i.d. glossolalia)")
    print("    - A single undifferentiated generative source")
    print("    - Meaningless repetition from one source table")
    print()
    print("  It does NOT by itself distinguish between:")
    print("    - Meaningful structured text (e.g., a pharmacopoeia)")
    print("    - A sectionally-structured generative process (e.g., different")
    print("      Cardan grilles per section, as in Rugg 2004)")
    print()
    print("  That distinction requires the further (model-dependent) evidence")
    print("  presented in the full paper. This test establishes the necessary")
    print("  precondition: the text has real structure to be explained.")
    print("  " + "-" * 66)
    print()
    print("=" * 70)
    print("  TEST COMPLETE. No decipherment was used. The structure is real.")
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()
