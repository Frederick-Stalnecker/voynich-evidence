# Structural Independence Test

**This test uses no decipherment.** It demonstrates a single, robust empirical fact: the Voynich manuscript's text is not homogeneous — it partitions into physically distinct sections with statistically distinguishable vocabulary distributions. The section boundaries are defined by codicological consensus (folio number and illustration type), not by any proposed reading. The statistical method is a folio-level permutation test (10,000 shuffles of folio-to-section labels), which makes no distributional assumptions and is immune to the within-folio token autocorrelation that invalidates parametric tests on this corpus. In 10,000 random reassignments, none produces vocabulary differentiation as strong as the manuscript's actual structure (empirical p < 10⁻⁴). This result holds whether or not any decipherment of the manuscript is correct: it establishes that the underlying text has real structure to be explained.

## Run it

```bash
python3 structural_test.py
```

## What you need

- Python 3.8+ (stdlib only — no external dependencies)
- `ZL3b-n.txt` (included, or download from https://www.voynich.nu/data/ZL3b-n.txt)

## Runtime

Under 30 seconds (10,000 permutations). Deterministic seed for reproducibility.

## What it proves — and what it does not

The test establishes that the manuscript's sections have genuinely distinct vocabularies. This is incompatible with a homogeneous random process (i.i.d. glossolalia, a single undifferentiated source). It does **not** by itself distinguish meaningful structured text from a sectionally-structured generative process (e.g., different Cardan grilles per section). That distinction requires the further model-dependent evidence presented in the full paper.

---

*Frederick Davis Stalnecker / THEOS Research Institute*
*Repository: https://github.com/Frederick-Stalnecker/voynich-evidence*
