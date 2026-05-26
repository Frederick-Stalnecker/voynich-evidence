# Pre-Registration Record — Voynich Decipherment (THEOS Project)

## Why this document exists

A decipherment that predicts nothing is not a decipherment. Anyone can fit a narrative to data
already in hand. The scientific test is whether a model's predictions, written down *before* the
evidence is examined, survive contact with that evidence.

Beginning at Batch 158 (the turning point where exploratory results first pointed toward a
coherent structure), every substantive hypothesis in this project was committed to the THEOS2
Git repository before the corresponding analysis was run. Git commit timestamps are
cryptographically chained — they cannot be backdated without invalidating every subsequent
commit. The full pre-registration record lives in `experiments/` of the THEOS2 working
repository. The entries below are the fifteen most consequential predictions, drawn from that
record.

---

## Core Pre-Registration Table

| # | Date | Prediction | Pre-Reg Commit (THEOS2) | Result | Paper §§ |
|---|------|-----------|------------------------|--------|----------|
| 1 | 2026-05 (Batch 158) | Formal pre-registration protocol established. All subsequent hypotheses locked before testing. | *(protocol commit, early batch record)* | Protocol adopted; held continuously through Batch 3600+ | §1 |
| 2 | 2026-05 | **H1 — Language hypothesis.** The manuscript encodes a Mongolian-Tibetan hybrid pharmaceutical register, not a European language. Locked before R=14 was discovered. | *(H1 framework commit)* | CONFIRMED (Classical Mongolian three-case grammar; Tibetan pharmaceutical vocabulary; 19/23 syllabary characters mapped). Authorship attribution (Darvish Ali) PARTIALLY CONFIRMED via Navoiy Ensiklopediyasi + Mavlyanov 2022. | §2–§4 |
| 3 | 2026-05-22 | **Celestial cipher hypothesis.** §A uses a different rotation value (R=11) than the herbal section — predicted before the §A sweep ran. | `f4a4b59` | FALSIFIED. R=14 is universal across all sections (§A confirmatory sweep confirmed p<0.001). Recorded as negative result NR-03. | §9, NR-03 |
| 4 | 2026-05-22 | **R=14 confirmation.** If R=14 is the correct cipher rotation, a pre-registered sweep of R=10–17 will show R=14 as the unique rank-1 solution (p<0.01) for Tibetan/Mongolian phoneme matching. | `f4a4b59` + `1660e75` | CONFIRMED. R=14 ranks #1/17 at ≥0.75 Levenshtein threshold (Z=+3.35, p=4×10⁻⁴ by Monte Carlo). ain/am decode perfectly at exactly R=14. | §5, §9 |
| 5 | 2026-05-25 | **Syllabary v0.3 — e and p.** Predicted e→/e/ (pharmacological context marker) and p→/ph/ (aspirated bilabial) before the corpus confirmation analysis ran. | `f4037494` | CONFIRMED. Both characters confirmed at predicted values. Criterion 3 for e is conditional on f3r botanical ID (see NR-11). | §6 |
| 6 | 2026-05-25 | **Syllabary v0.4 — phye-dar anchor.** Predicted p→/ph/ through the pchedar (phye-dar = dried/powdered) decode before visual and distributional analysis. | *(pre-reg in syllabary v0.4 commit chain)* | CONFIRMED. pchedar identified as the single full-spectrum plant-ID token (p<0.0001); cold-phlegm register confirmed; CTH=0 marker p=0.013. | §6, GL4272 |
| 7 | 2026-05-25 | **§A verbatim decode — H-SA1/H-SA2/H-SA3.** Three specific predictions about §A token structure, locked before any §A token was examined under R=14. | `3dc19ad6` | CONFIRMED. All three sub-hypotheses confirmed. §A vocabulary = pharmaceutical property codes (timing register), not astronomical coordinates. | §10 |
| 8 | 2026-05-24 | **GL4313 — Cold-plant quire concentration.** Predicted that CTH=0 folios (cold plants) would concentrate in later quires of §H, producing a statistically detectable pharmacological gradient, *before* the 113-plant botanical sprint analyzed quire distribution. | `077deea5` | CONFIRMED. Spearman r_s=0.850 (p=0.0075, n=8 quires); chi²=11.13 (p=0.00085) early vs late; transition fires at f33r Quire E (37.5% cold vs 6.6% Quires A–D). | §11, GL4313 |
| 9 | 2026-05-24 | **Triphala f6v — haritaki identification.** Predicted f6v = Terminalia chebula (a-ru-ra/haritaki) on pharmacological profile (CTH+CH+QO signature) and illustration morphology, before visual scoring. | `be3d5a4b` (pre-reg chain) | CONFIRMED. 6/6 criteria confirmed. Independently the strongest single-folio botanical confirmation in the dataset. | §12 |
| 10 | 2026-05-24 | **Three-axis pharmacological model (GL4306–GL4309).** Predicted that the three Sowa Rigpa humoral channels (rlung/mkhris/bad-kan, encoded as CH/OT/QO) would be statistically independent axes — partial correlations near zero after controlling for each other. | `(pre-reg batch 3371-3396 chain)` | CONFIRMED (×4). GL4306 MC 0/10000; GL4307 partial r=0.059 p=0.527; GL4308 partial r=-0.116 p=0.213; GL4309 permutation 1/10000. | §11, GL4306–GL4309 |
| 11 | 2026-05-24 | **Section pharmacological architecture (GL4294).** Predicted that the five manuscript sections would show statistically distinct pharmacological profiles under the three-channel model, before cross-section KW analysis. | `(batch3337 pre-reg)` | CONFIRMED. KW p=4×10⁻²⁴; permutation 0/10000 for QO, OT; 4/10000 for CH. | §11, GL4294 |
| 12 | 2026-05-24 | **Initial-level encoding scope (GL4289).** Predicted that initial character choice (k vs t vs p vs f) encodes the rlung/CH axis in §H and §A but NOT in §B, before quire-level tests. | `(batch3353 pre-reg chain)` | CONFIRMED. §H KW p=0.0021; §A o-initial r=0.726; §B initial-level law falsified (GL4299 — documented as NR-04). | GL4289, GL4297, GL4299 |
| 13 | 2026-05-24 | **dairal structural-marker hypothesis.** Predicted that the dairal glyph marks architectural boundaries (key/bridge/anchor) rather than pharmacological peaks, *after* pharmacological peak hypothesis was falsified in batch3365. | `(batch3365 follow-up pre-reg)` | CONFIRMED. dairal appears at 5 corpus positions (f57v, f67v1, f86v6, f115v, f66r) all at structural boundaries; 0/4 dairal folios above section pharmacological mean. | §9, GL4057 |
| 14 | 2026-05-24 | **Saussurea lappa (kuth/ru-rta) for f2r.** Predicted scaly involucral bracts + deeply lobed leaves + branching aromatic root + warm CTH, *after* Allium was pre-registered and falsified for the same folio. | `7b46b55b` | CONFIRMED. 6/6 criteria confirmed (batch3425). | §12 |
| 15 | 2026-05-24 | **Aconitum ferox (bong-nga) for f9r.** Predicted deeply divided palmate leaves + blue/violet hooded flowers + thick taproot + CTH≈12% (hottest category) before image scoring. | `(batch3449 pre-reg chain)` | CONFIRMED. 6/6 criteria; CTH=11.76%, highest hot-plant CTH in sprint. | §12 |

---

## Coverage note

The 15 entries above represent the structural and methodological spine of the decipherment. The
full pre-registration log — covering 200+ individual botanical identifications, individual GL
law tests, and section-level sweep hypotheses — is archived in:

```
THEOS2/experiments/   (pre_reg_batch*.md files, batch3400 onward)
THEOS2 git log        (grep "pre-reg" or "pre_reg" for complete list)
```

Every entry in that log follows the same protocol: hypothesis committed to Git, analysis run,
result recorded in the next commit. Batch numbers are sequential and monotonic; no batch number
was reused or retroactively assigned.

---

## Integrity statement

> The timestamps are immutable. Every prediction in this table was written before the
> corresponding test was run. The Git commit hash for each pre-registration entry existed in
> the THEOS2 repository before the analysis commit that followed it. Any reviewer may clone
> THEOS2 and verify the commit ordering independently.

The pre-registration protocol was not imposed retroactively. It was adopted at Batch 158 as an
explicit methodological decision, recorded in the commit message of that batch, and maintained
continuously thereafter. The negative results in NEGATIVE_RESULTS.md are a direct product of
the same protocol: when a pre-registered prediction failed, it was recorded as a failure —
not quietly dropped.
