# Contributing — Adversarial Verification Welcome

This repository is a reproduction package, not a development project. There is nothing to contribute except verification and challenge.

## How to Challenge a Specific Claim

File an issue with:

1. **The claim being challenged** — cite the specific row in `REPRODUCTION_REPORT.md` or the hypothesis in `PRE_REGISTRATIONS.md`
2. **The test you ran** — exact command, exact corpus, exact script version
3. **The corpus hash** — SHA-256 of your `data/ZL3b-n.txt` (run `./reproduce.sh` to verify)
4. **The discrepant result** — your output vs. the stated reference value

A challenge that follows this format will receive a direct response. Vague challenges will not.

## If You Find a Genuine Error

Open an issue. If the error affects a published claim, it will be documented in `NEGATIVE_RESULTS.md` following the same protocol as all other corrections in that file.

## Reproducibility Reports

If you successfully reproduced the results on a different platform, OS, or Python version, a brief issue noting this is welcome — it builds the reproducibility record.

## Contact

For adversarial verification requiring access to the private THEOS2 working repository (full pre-registration log and analysis pipeline): contact the author directly. NDA required.
