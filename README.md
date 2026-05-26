# Voynich Manuscript Decipherment — Evidence Repository

This repository contains the reproducible statistical evidence for the claim that the Voynich Manuscript (Beinecke MS 408, Yale University) encodes a pharmaceutical text in a hybrid Classical Mongolian / Tibetan Sowa Rigpa register, encrypted by a rotational substitution cipher calibrated at R=14.

Manuscript under review at *Cryptologia* (2026). arXiv preprint forthcoming.

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

> **Note on `results/cipher.json`:** The repository ships with a pre-seeded reference state so that `REPRODUCTION_REPORT.md` shows all four modules. Running `./reproduce.sh` overwrites it with independently computed values from your corpus copy. If you want to verify the cipher claim from scratch without any pre-seeded state, delete `results/cipher.json` before running.

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
| 113-plant botanical classification (§7) | `scripts/4_botanical.py` |
| GL4313 pharmacological gradient (§8) | `scripts/5_gradient.py` |
| Full report with pass/fail per claim | `scripts/verify_report.py` |

*Note: Two pre-registered species identifications (f2r, f9r) were superseded by later sprint waves. See [PRE_REGISTRATIONS.md § Corrections](PRE_REGISTRATIONS.md#corrections) for the full erratum.*

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

## Tokenization Methodology

All token counts in this repository use the following pipeline:

1. Lines containing `<!` (IVTFF metadata) are excluded.
2. Text is extracted via regex `>\s+(.*)` after the folio-position marker.
3. Annotations are stripped: `<...>`, `{...}`, `[...]` patterns removed.
4. Text is split on `[.,\s;!?%-]+` — dots, commas, spaces, and standard punctuation.
5. Tokens must match `^[a-z]+$` (lowercase alpha only; no digits, no punctuation fragments).

This gives standalone token counts. Importantly, tokens like `odaiin` and `chodaiin` are
counted separately from `daiin` — they are distinct EVA words with the same suffix.

**Token count ranges by method:**

| Token | Standalone (this method) | Whitespace-split only | Substring |
|-------|--------------------------|----------------------|-----------|
| daiin | 748–751 | 853 | 1,430 |
| sar   | 63–76   | 79  | 145 |
| aiin  | 437–442 | 528 | 3,944 |
| shor  | 83–94   | 94  | 155 |

Working notes from the research phase cited daiin N=3,832 and sar N=277. Investigation
revealed: the daiin figure counted all tokens ending in the -aiin genitive suffix (3,493
tokens across the full paradigm). The sar figure's source is not fully explained; it may
reflect an earlier corpus version. Both discrepancies are documented in `NEGATIVE_RESULTS.md`
(Section 5). The section-distribution findings are confirmed at the corrected counts.

---

## Known Limitations

- 5 of 23 phonological units remain unmapped (j, u, v, x, z — together <3% of corpus characters)
- `scripts/4_botanical.py` requires `data/botanical_dataset.json` — included in this repository (113 confirmed plants, batch3597)
- Two early botanical identifications (f2r, f9r) were falsified by later sprint waves and re-confirmed with different species. See [Corrections](PRE_REGISTRATIONS.md#corrections) in PRE_REGISTRATIONS.md for the full erratum and the THEOS2 commit chain.
- The three-column decoded folio pages (f67r1, f70r2, f68v3, f70r1) are part of a forthcoming companion publication and are not included in this repository

---

## Citation

This work is currently under review at *Cryptologia*. Until publication, please cite as:

```bibtex
@misc{stalnecker2026voynich,
  author       = {Stalnecker, Frederick Davis},
  title        = {Voynich Manuscript Decipherment --- Evidence Repository},
  year         = {2026},
  howpublished = {GitHub repository},
  url          = {https://github.com/Frederick-Stalnecker/voynich-evidence},
  note         = {Manuscript in review at Cryptologia (2026). Citation will be updated upon publication.}
}
```

## Intellectual Property Notice

The research in this repository was conducted using THEOS (Temporal Hierarchical Emergent Optimization System), invented by Frederick Davis Stalnecker and the subject of U.S. Patent Application No. 18/919,771 (provisional No. 63/831,738). THEOS is the exclusive intellectual property of Frederick Davis Stalnecker and THEOS Research Institute.

The MIT license on the reproduction scripts in this repository applies only to those scripts. It does not grant any rights to THEOS. See `LICENSE` for the full scope statement.

---

## Contact

Technical questions (reproduction, methodology): guestent@gmail.com  
Media and general inquiries: guestent@gmail.com

*Repository maintained by Frederick Davis Stalnecker. Research conducted with THEOS (Temporal Hierarchical Emergent Optimization System), invented by Frederick Davis Stalnecker (patent-pending U.S. App 18/919,771).*
