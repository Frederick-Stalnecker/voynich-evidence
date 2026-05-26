#!/usr/bin/env bash
# =============================================================================
# reproduce.sh — Voynich Decipherment Evidence: One-Command Reproduction
#
# Usage:
#   ./reproduce.sh
#
# What this does:
#   Verifies your corpus file matches the reference hash, runs four statistical
#   modules against the ZL3b-n.txt Voynich EVA corpus, and writes
#   REPRODUCTION_REPORT.md summarizing which claims pass and which fail.
#
# Expected runtime: 3–8 minutes on a standard laptop (permutation test N=10,000)
# Python version: 3.8+
# External dependencies: none (uses only stdlib)
#
# The corpus (ZL3b-n.txt) must be placed in data/ before running.
# Download from: https://www.voynich.nu/data/ZL3b-n.txt
# Expected SHA-256: bf5b6d4ac1e3a51b1847a9c388318d609020441ccd56984c901c32b09beccafc
# =============================================================================

set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

PYTHON="${PYTHON:-python3}"
CORPUS="data/ZL3b-n.txt"
EXPECTED_HASH="bf5b6d4ac1e3a51b1847a9c388318d609020441ccd56984c901c32b09beccafc"

echo "============================================================"
echo "  Voynich Decipherment — Reproduction Pipeline"
echo "  https://github.com/Frederick-Stalnecker/voynich-evidence"
echo "  Estimated runtime: 3–8 minutes"
echo "============================================================"
echo ""

# -- Step 0: Verify corpus --
echo "[0/5] Verifying corpus..."
if [ ! -f "$CORPUS" ]; then
    echo "ERROR: Corpus not found at $CORPUS"
    echo ""
    echo "Download the ZL3b-n.txt Voynich EVA corpus:"
    echo "  curl -o data/ZL3b-n.txt https://www.voynich.nu/data/ZL3b-n.txt"
    echo ""
    echo "Expected SHA-256: $EXPECTED_HASH"
    exit 1
fi

# Compute hash (macOS uses shasum, Linux uses sha256sum)
if command -v sha256sum &>/dev/null; then
    ACTUAL_HASH=$(sha256sum "$CORPUS" | awk '{print $1}')
else
    ACTUAL_HASH=$(shasum -a 256 "$CORPUS" | awk '{print $1}')
fi

if [ "$ACTUAL_HASH" = "$EXPECTED_HASH" ]; then
    echo "  ✅ Corpus hash verified: $ACTUAL_HASH"
else
    echo "  ⚠️  Corpus hash MISMATCH"
    echo "     Expected: $EXPECTED_HASH"
    echo "     Actual:   $ACTUAL_HASH"
    echo ""
    echo "  You are using a different version of the ZL transcription."
    echo "  Token counts may differ from stated values."
    echo "  Continuing — results will note the discrepancy."
fi
echo ""

# -- Step 1: Cipher --
echo "[1/5] Cipher parameter (R=14) sweep and permutation test..."
echo "      (This step runs 10,000 permutations — ~2 minutes)"
$PYTHON scripts/1_cipher.py
echo ""

# -- Step 2: Syllabary --
echo "[2/5] Syllabary map v0.4 anchor verification..."
$PYTHON scripts/2_syllabary.py
echo ""

# -- Step 3: Vocabulary --
echo "[3/5] Confirmed vocabulary token counts and section distributions..."
$PYTHON scripts/3_vocabulary.py
echo ""

# -- Step 4: Botanical (if data available) --
if [ -f "data/botanical_dataset.json" ]; then
    echo "[4/5] Botanical dataset analysis (113 plants, CTH/CH/QO)..."
    $PYTHON scripts/4_botanical.py
    echo ""
else
    echo "[4/5] Botanical dataset (scripts/4_botanical.py) — SKIPPED"
    echo "      data/botanical_dataset.json not present."
    echo "      This module requires the 113-plant dataset from the full paper."
    echo ""
fi

# -- Step 5: Gradient --
echo "[5/5] GL4313 pharmacological gradient (Spearman correlation)..."
$PYTHON scripts/5_gradient.py
echo ""

# -- Final report --
echo "[✓] Generating REPRODUCTION_REPORT.md..."
$PYTHON scripts/verify_report.py
echo ""
echo "============================================================"
echo "  DONE. Open REPRODUCTION_REPORT.md to review results."
echo "============================================================"
