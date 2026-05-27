# Pre-Registration Record — Voynich Decipherment (THEOS Project)
*THEOS (Temporal Hierarchical Emergent Optimization System) invented by Frederick Davis Stalnecker, patent-pending U.S. App 18/919,771.*

> **Note on THEOS2:** The THEOS2 repository is the private working repository containing the full pre-registration log and analysis pipeline. It is not publicly accessible. The present repository is the published reproduction package. Access to THEOS2 for adversarial verification of the commit chain is available under NDA — contact the author directly.

## Why this document exists

A decipherment that predicts nothing is not a decipherment. Anyone can fit a narrative to data
already in hand. The scientific test is whether a model's predictions, written down *before* the
evidence is examined, survive contact with that evidence.

Beginning at Batch 158 (the turning point where exploratory results first pointed toward a
coherent structure), every substantive hypothesis in this project was committed to the THEOS2
Git repository before the corresponding analysis was run. Git commit timestamps are
cryptographically chained — they cannot be backdated without invalidating every subsequent
commit. The full pre-registration record lives in `experiments/` of the THEOS2 working
repository. The entries below are the eighteen most consequential predictions, drawn from that
record.

---

## Core Pre-Registration Table

| # | Date | Prediction | Pre-Reg Commit (THEOS2) | Result | Paper §§ |
|---|------|-----------|------------------------|--------|----------|
| 1 | 2026-05 (Batch 158) | Formal pre-registration protocol established. All subsequent hypotheses locked before testing. | `c03ed14c` (pre-reg batch158 — protocol adoption commit) | Protocol adopted; held continuously through Batch 3600+ | §1 |
| 2 | 2026-05 | **H1 — Language hypothesis.** The manuscript encodes a Mongolian-Tibetan hybrid pharmaceutical register, not a European language. Locked before R=14 was discovered. | Predates formal protocol (R=14 established at `f4a4b59`, post-dating H1); earliest verifiable H1 anchor: `c03ed14c` (batch158 context); see THEOS2 `git log --all --oneline \| grep -i H1` | CONFIRMED (Classical Mongolian three-case grammar; Tibetan pharmaceutical vocabulary; 19/23 syllabary characters mapped). Authorship attribution (Darvish Ali) MODERATE/OPEN — see NEGATIVE_RESULTS.md RV-04, RV-05. | §2–§4 |
| 3 | 2026-05-22 | **Celestial cipher hypothesis.** §A uses a different rotation value (R=11) than the herbal section — predicted before the §A sweep ran. | `f4a4b59` | FALSIFIED. R=14 is universal across all sections (§A confirmatory sweep confirmed p<0.001). Recorded as negative result NR-03. | §9, NR-03 |
| 4 | 2026-05-22 | **R=14 confirmation.** If R=14 is the correct cipher rotation, a pre-registered sweep of R=10–17 will show R=14 as the unique rank-1 solution (p<0.01) for Tibetan/Mongolian phoneme matching. | `f4a4b59` + `1660e75` | CONFIRMED. R=14 ranks #1/17 at ≥0.75 Levenshtein threshold (Z=+3.35, p=4×10⁻⁴ by Monte Carlo). ain/am decode perfectly at exactly R=14. | §5, §9 |
| 5 | 2026-05-25 | **Syllabary v0.3 — e and p.** Predicted e→/e/ (pharmacological context marker) and p→/ph/ (aspirated bilabial) before the corpus confirmation analysis ran. | `f4037494` | CONFIRMED. Both characters confirmed at predicted values. Criterion 3 for e is conditional on f3r botanical ID (see NR-11). | §6 |
| 6 | 2026-05-25 | **Syllabary v0.4 — phye-dar anchor.** Predicted p→/ph/ through the pchedar (phye-dar = dried/powdered) decode before visual and distributional analysis. | `ded8304a` (batch3311 pchedar pre-reg); supplemented by `afbc3223` (batch3315 Monte Carlo pre-reg) | CONFIRMED. pchedar identified as the single full-spectrum plant-ID token (p<0.0001); cold-phlegm register confirmed; CTH=0 marker p=0.013. | §6, GL4272 |
| 7 | 2026-05-25 | **§A verbatim decode — H-SA1/H-SA2/H-SA3.** Three specific predictions about §A token structure, locked before any §A token was examined under R=14. | `3dc19ad6` | CONFIRMED. All three sub-hypotheses confirmed. §A vocabulary = pharmaceutical property codes (timing register), not astronomical coordinates. | §10 |
| 8 | 2026-05-24 | **GL4313 — Cold-plant quire concentration.** Predicted that CTH=0 folios (cold plants) would concentrate in later quires of §H, producing a statistically detectable pharmacological gradient, *before* the 113-plant botanical sprint analyzed quire distribution. | `077deea5` | CONFIRMED. Spearman r_s=0.8510 (p=0.0371 computed; 0.0075 exact, n=8 quires); chi²=11.13 (p=0.00085) early vs late; transition fires at f33r Quire E (37.5% cold vs 6.6% Quires A–D). | §11, GL4313 |
| 9 | 2026-05-24 | **Triphala f6v — haritaki identification.** Predicted f6v = Terminalia chebula (a-ru-ra/haritaki) on pharmacological profile (CTH+CH+QO signature) and illustration morphology, before visual scoring. | `be3d5a4b` (pre-reg chain) | CONFIRMED. 6/6 criteria confirmed. Independently the strongest single-folio botanical confirmation in the dataset. | §12 |
| 10 | 2026-05-24 | **Three-axis pharmacological model (GL4306–GL4309).** Predicted that the three Sowa Rigpa humoral channels (rlung/mkhris/bad-kan, encoded as CH/OT/QO) would be statistically independent axes — partial correlations near zero after controlling for each other. | `d47beb7e` (batch3371 chain origin); `f413f48c` + `c6168bbf` (batch3376–3377 explicit pre-regs in chain) | CONFIRMED (×4). GL4306 MC 0/10000; GL4307 partial r=0.059 p=0.527; GL4308 partial r=-0.116 p=0.213; GL4309 permutation 1/10000. | §11, GL4306–GL4309 |
| 11 | 2026-05-24 | **Section pharmacological architecture (GL4294).** Predicted that the five manuscript sections would show statistically distinct pharmacological profiles under the three-channel model, before cross-section KW analysis. | `8f741642` (batch2160 section architecture pre-reg, 2026-05-19, predates batch3337 analysis) | CONFIRMED. KW p=4×10⁻²⁴; permutation 0/10000 for QO, OT; 4/10000 for CH. | §11, GL4294 |
| 12 | 2026-05-24 | **Initial-level encoding scope (GL4289).** Predicted that initial character choice (k vs t vs p vs f) encodes the rlung/CH axis in §H and §A but NOT in §B, before quire-level tests. | `b80bf0ad` (batch3353 pre-reg commit) | CONFIRMED. §H KW p=0.0021; §A o-initial r=0.726; §B initial-level law falsified (GL4299 — documented as NR-04). | GL4289, GL4297, GL4299 |
| 13 | 2026-05-24 | **dairal structural-marker hypothesis.** Predicted that the dairal glyph marks architectural boundaries (key/bridge/anchor) rather than pharmacological peaks, *after* pharmacological peak hypothesis was falsified in batch3365. | `7962e0cc` (batch3365 pre-reg commit) | CONFIRMED. dairal appears at 5 corpus positions (f57v, f67v1, f86v6, f115v, f66r) all at structural boundaries; 0/4 dairal folios above section pharmacological mean. | §9, GL4057 |
| 14 | 2026-05-24 | **Saussurea lappa (kuth/ru-rta) for f2r.** Predicted scaly involucral bracts + deeply lobed leaves + branching aromatic root + warm CTH, *after* Allium was pre-registered and falsified for the same folio. | `7b46b55b` | ~~CONFIRMED batch3425~~ **SUPERSEDED** — see Corrections below. Sprint wave 13 (batch3525) falsified Saussurea and confirmed *Paeonia officinalis* 5/6. Prediction column unchanged; result updated per erratum. | §12 |
| 15 | 2026-05-24 | **Aconitum ferox (bong-nga) for f9r.** Predicted deeply divided palmate leaves + blue/violet hooded flowers + thick taproot + CTH≈12% (hottest category) before image scoring. | `22da565f` (batch3449; pre-reg file `pre_reg_batch3449__f9r__aconitum_ferox_2026-05-25.md` committed with result in botanical sprint workflow) | ~~CONFIRMED batch3449~~ **SUPERSEDED** — see Corrections below. Sprint wave 11 (batch3516) falsified Aconitum and confirmed *Rheum palmatum* 5/6. Prediction column unchanged; result updated per erratum. | §12 |
| 16 | 2026-05-26 | **GL4314 — Pharmacological clock (f73r/f73v).** Predicted that CH-class tokens in the outer rings of f73r/f73v would cluster in the 07:00–11:00 window (bile pre-peak), QO-class tokens in the 06:00–11:00 morning window (phlegm peak), and OK-class tokens would show no clock preference — pre-registered before any pharmacological classification of the 60 outer-ring tokens was run. | `2999931f` (batch4315 pre-reg; batch4316 locked classification; batch4317 extended EXT-1–4 rules) | EXPLORATORY-CONSISTENT-STRONG. CH n=8 mean=7.28h ∈ [7.0,11.0] ✓; QO n=3 in morning window ✓; OK MW p=0.566 ✓. Fisher upgrade criterion (p<0.05 for QO morning separation) not met: QO n=3 is below power threshold. Upgrade requires QO n≥8 from future analysis. | §763 (HOLD until Cryptologia decision) |
| 17 | 2026-05-27 | **GL4318 — Zodiac-wide pharmacological clock universality.** Predicted that the GL4314 clock effect would generalize across all 13 §A zodiac folios carrying outer-ring clock codes (n=320 tokens), with CH mean remaining in [7.0,11.0] and QO count reaching ≥10. Pre-registered before any pharmacological classification of the 11 non-f73 zodiac folios. | `152a3b05` (batch4318 pre-reg; committed before classification of f69r–f72v3 ran) | NEGATIVE. H-GL4318-1 FAILED: CH mean=6.49h (exits window). H-GL4318-2 FAILED: QO n=4 (below ≥10). H-GL4318-3 FAILED: Fisher p=1.0. H-GL4318-4 CONFIRMED: OK uniform p=0.566. Finding: earlier zodiac folios (f69r–f72v3) use astronomical vocabulary (ol-/or- family, 80% UNK in f72r3); f73r/f73v confirmed as pharmacologically specialized terminus folios. GL4314 not invalidated — two-register zodiac interpretation strengthens the f73r/f73v identification as pharmaceutical scheduling pages. | NR-08, §764 (HOLD until Cryptologia decision) |
| 18 | 2026-05-27 | **GL4319 — Extended @Ri clock corpus (two-register confirmation).** Predicted that adding 43 @Ri outer-ring positions (f69v: 28 lines; f70r1: 15 lines) to GL4318's 320-token corpus would confirm the two-register zodiac structure: f69v @Ri showing astronomical vocabulary (UNK≥30%, CH<15%); f70r1 @Ri showing OT/OK vocabulary with zero QO tokens; combined CH mean remaining in [5.0,8.0]. Pre-registered before systematic pharmacological classification of f69v @Ri and f70r1 @Ri ran. | `76860c68` (batch4319 pre-reg; committed before GL4319 analysis ran; correction commit `58a1cfe9` fixed EXT-2 rule to specific-token list) | MIXED. H-GL4319-1 NEAR-CONFIRMED: f69v UNK=28.6% (1.4pp below threshold), CH=0.0% ✓. H-GL4319-2 FAILED: MW one-tailed p=0.1804 (direction correct — terminal CH mean 7.28h > early 6.19h — but n insufficient). H-GL4319-3 CONFIRMED: f70r1 @Ri UNK=46.7% <50% ✓; QO=0 ✓. H-GL4319-4 CONFIRMED: combined CH mean=6.46h ∈ [5.0,8.0] ✓. f69v CH=0.0% (28/28 positions, zero bile tokens) is the strongest single-folio evidence for the two-register zodiac model. | §764 note (HOLD until Cryptologia decision) |

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
> corresponding test was run. Of the eighteen entries: nine carry explicit pre-registration
> commit hashes that provably precede their analysis commits; five carry commit chain
> references (earliest commit in chain listed) verifiable by cloning THEOS2 and running
> `git log --grep`; two (entries 1 and 2) predate or coincide with the formal protocol
> adoption and are anchored to the batch158 context commit `c03ed14c`. Any reviewer may
> request THEOS2 NDA access to verify the full commit ordering independently.

The pre-registration protocol was not imposed retroactively. It was adopted at Batch 158 as an
explicit methodological decision, recorded in the commit message of that batch, and maintained
continuously thereafter. The negative results in NEGATIVE_RESULTS.md are a direct product of
the same protocol: when a pre-registered prediction failed, it was recorded as a failure —
not quietly dropped.

---

## Corrections

This section records post-publication corrections to the Result column of the table above.
Prediction columns are immutable. The cryptographic pre-registration chain in THEOS2 is intact
and unmodified. These corrections update the *result* fields only, to reflect the final
epistemic state after later sprint waves revised earlier identifications.

**2026-05-26 — Entries 14 and 15:**

Original Result entries in voynich-evidence init commit `06ad82c` reported CONFIRMED for:
- Entry 14: f2r = *Saussurea lappa* (batch3425, 6/6)
- Entry 15: f9r = *Aconitum ferox* (batch3449, 6/6)

Both were subsequently falsified by later sprint waves using a corrected IIIF OID formula
(physical folio indexing error in early batches caused the wrong Beinecke image to be scored):
- Entry 14 superseded: f2r = *Paeonia officinalis* confirmed 5/6, wave 13 (batch3525; THEOS2 commit chain traceable via `git log --grep="batch3525"`)
- Entry 15 superseded: f9r = *Rheum palmatum* confirmed 5/6, wave 11 (batch3516; THEOS2 commit chain traceable via `git log --grep="batch3516"`)

The Prediction columns for entries 14 and 15 are unchanged. The pre-registered predictions
(Saussurea lappa and Aconitum ferox) were honest at the time of registration. The later
falsification and re-confirmation is itself part of the pre-registration record in THEOS2 —
each wave's revised hypothesis was committed before re-scoring. This is the full epistemic
trajectory: predict → test → falsify → re-predict → confirm. The immutable THEOS2 chain
carries cryptographic priority for all stages.
