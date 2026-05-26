# Voynich Manuscript Decipherment — Evidence Repository

This repository contains the reproducible statistical evidence for the claim that the Voynich Manuscript (Beinecke MS 408, Yale University) encodes a pharmaceutical text in a hybrid Classical Mongolian / Tibetan Sowa Rigpa register, encrypted by a rotational substitution cipher calibrated at R=14.

**Published paper:** Stalnecker, F.D. (2026). *Cryptologia*, submission ID 264889452, decision pending.

---

## Reproduce in One Command

```bash
git clone [this-repo]
cd voynich-evidence

# Place the corpus file in data/
curl -o data/ZL3b-n.txt https://www.voynich.nu/data/ZL3b-n.txt

# Run the full pipeline (~5 minutes)
./reproduce.sh
```

Open `REPRODUCTION_REPORT.md` when it finishes.

**Expected runtime:** 3–8 minutes on a standard laptop.  
**Dependencies:** Python 3.8+, standard library only (no pip install required).  
**Corpus SHA-256:** See `CORPUS_HASH.txt`.

---

## What This Repository Proves

Five independent statistical results, each pre-registered before testing:

| Claim | Test | Result |
|-------|------|--------|
| R=14 is the cipher calibration parameter | Rotation sweep + permutation test | p < 10⁻¹² |
| Syllabary: 19/23 characters T1-confirmed | Anchor chain analysis | No alternative reading works |
| Pharmaceutical vocabulary section-consistent | Chi-square, section distribution | shor §H=68.5%; qol §B=76.6% |
| §H organized as pharmacological gradient | Spearman r_s=0.850 | p=0.0075 (8 quires) |
| Three-humor section architecture | Kruskal-Wallis | p=4×10⁻²⁴ |

These results are independent: the gradient holds whether or not the cipher is correct; the vocabulary section distributions hold whether or not the pharmaceutical interpretation is correct; the cipher sweep holds whether or not the language identification is correct.

---

## Glossary

| Term | Meaning |
|------|---------|
| EVA | Extended Voynich Alphabet — the standard transliteration of Voynich characters |
| R=14 | Rotation value (cipher calibration parameter) for the f57v volvelle wheel |
| §H, §A, §B, §C, §P, §T | Manuscript sections: Herbal, Astronomical, Phlegm, Cosmological, Pharmaceutical, Clinical Text |
| CTH | Warmth-class token percentage — pharmacological warmth classification metric |
| CH | Wind-humor (rlung) token percentage |
| QO | Phlegm-humor (bad-kan) token percentage |
| Sowa Rigpa | Traditional Tibetan medicine system (source of the pharmaceutical vocabulary) |
| ZL3b-n.txt | Zandbergen-Landini EVA corpus, the standard Voynich transcription |

---

## Claim-to-Script Map

| Paper claim | Reproducing script |
|-------------|-------------------|
| R=14 cipher, p<10⁻¹² (§4) | `scripts/1_cipher.py` |
| Syllabary 19/23 T1-confirmed (§5) | `scripts/2_syllabary.py` |
| 11 vocabulary items + section distributions (§6) | `scripts/3_vocabulary.py` |
| 113-plant botanical classification (§7) | `scripts/4_botanical.py` *(dataset pending)* |
| GL4313 pharmacological gradient (§8) | `scripts/5_gradient.py` |
| Full report with pass/fail per claim | `scripts/verify_report.py` |

---

## How to Challenge Specific Claims

**To test R=14 against every other rotation value:**
```bash
python scripts/1_cipher.py
# results/cipher.json contains match rates for R=0 through R=22
```

**To test the syllabary's "no alternative reading" criterion:**
```bash
python scripts/2_syllabary.py
# Each anchor shows what happens when you substitute every other phoneme for the unconstrained character
```

**To rerun the GL4313 gradient with your own quire-level data:**
Edit the `QUIRE_DATA` table in `scripts/5_gradient.py` and rerun.

**To use a different transcription of the corpus:**
Replace `data/ZL3b-n.txt` with your transcription. Note that token counts will differ; the PASS criteria in `verify_report.py` are tolerance-based, not exact-match.

---

## Pre-Registration

All hypotheses were registered in a Git repository before testing. Timestamps are cryptographically chained and immutable. See `PRE_REGISTRATIONS.md` for the full index with commit hashes.

---

## Negative Results

We publish every pre-registered hypothesis that failed. See `NEGATIVE_RESULTS.md`. This is not a weakness — it is the evidence that the method is scientific rather than curve-fitting.

---

## Known Limitations

- 5 of 23 phonological units remain unmapped (j, u, v, x, z — together <3% of corpus characters)
- `scripts/4_botanical.py` requires the full 113-plant dataset, not yet released in this repository
- The three-column decoded folio pages (f67r1, f70r2, f68v3, f70r1) are available in the companion `ASTROMEDICA-Book` repository

---

## Citation

```bibtex
@article{stalnecker2026voynich,
  author  = {Stalnecker, Frederick Davis},
  title   = {[Title per Cryptologia publication]},
  journal = {Cryptologia},
  year    = {2026},
  note    = {Submission ID 264889452}
}
```

---

## Contact

Technical questions (reproduction, methodology): guestent@gmail.com  
Media and general inquiries: guestent@gmail.com

*Repository maintained by Frederick Davis Stalnecker. Research conducted with THEOS (Temporal Hierarchical Emergent Optimization System).*
