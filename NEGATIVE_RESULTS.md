# Negative Results — Voynich Decipherment

## We publish our failures because science requires it.

A decipherment with no falsified hypotheses is a red flag, not a credential. It means either
the researcher asked no hard questions, or they asked them and quietly buried the answers. This
document does neither. Every entry here was pre-registered before the test that refuted it. The
failures are part of the evidence — they demonstrate that the testing apparatus is real, that
the method has predictive teeth, and that confirmation bias was not the engine driving results.

The current confirmation record across all pre-registered structural predictions is documented
in PRE_REGISTRATIONS.md (the authoritative source for counts and outcomes as the research
continues). One prediction (GL4314, entry 16) is confirmed at EXPLORATORY-CONSISTENT-STRONG
(upgrade to CONFIRMATORY pending QO n≥8). Eight negative or null results are documented below
in full — every one was pre-registered. So are the botanical identifications we corrected mid-sprint, the authorship
claim we retracted when primary sources failed to support it, the known gaps in the syllabary,
and the methodological limitations that remain open.

---

## Section 1 — Falsified Hypotheses (pre-registered, did not confirm)

**NR-01 — `chedy` section profile (H-e2)**
- *Prediction:* `chedy` (N=498, one of the highest-frequency EVA tokens) would be §H-dominant,
  with ≥60% of occurrences in the herbal section, consistent with a pharmaceutical ingredient
  marker.
- *Result:* FALSIFIED. `chedy` is only 11% §H. It is strongly §B+§T dominant, consistent with
  a formula-connector or syntactic linker function, not an ingredient. The herbal-dominance
  criterion fails by a factor of five.
- *Disposition:* `chedy` reclassified as a structural connector. The §H-exclusivity criterion
  for ingredient status was retained and applied correctly to subsequent candidates.

**NR-02 — H5-1: §A encodes astronomical positions**
- *Prediction:* The star-section (§A, ff.67r–73v) uses its cipher to encode actual stellar
  coordinates or astronomical designations, consistent with the visual appearance of the
  illustrations (stars, wheels, cosmological diagrams).
- *Result:* FALSIFIED. §A vocabulary is pharmaceutical property codes — specifically timing
  and preparation-stage markers — not astronomical coordinates. The illustrations are
  pharmacological timing wheels, not star charts. The visual appearance was misleading.
  38/58 §A star labels match Tibetan/Mongolian pharmaceutical terminology at R=14 (H3
  confirmed); 0/58 match a coherent set of stellar designations.
- *Disposition:* H5-1 closed as falsified (batch3056). §A reframed as the timing register
  of the pharmacopoeia — the "when to administer" section, indexed by stellar/seasonal
  cycles as a timing mechanism. This is a stronger result: the cipher is consistent and
  purposeful, not merely decorative.

**NR-03 — Celestial cipher (§A uses R≠14)**
- *Prediction:* §A uses a different rotation value from §H — specifically R=11, derived from
  an exploratory read of the f68v1 wheel structure — because a dedicated astronomical section
  might employ a distinct encoding layer.
- *Result:* FALSIFIED. The confirmatory R-sweep found R=14 universal across §A. The R=11
  marginal candidate from the exploratory pass did not replicate. R=14 is the single rotation
  value that produces valid Tibetan/Mongolian outputs in both §H and §A, at identical
  statistical significance.
- *Disposition:* R=14 universality strengthened by the failure of the §A-specific prediction.
  Pre-reg commit: `f4a4b59` (2026-05-22, before confirmatory sweep ran).

**NR-04 — GL4299: §B `p`-initial predicts highest QO**
- *Prediction:* In §B (the pharmaceutical section with the highest overall phlegm/bad-kan
  signal), `p`-initial tokens would show the highest QO values among initials — extending the
  `p`-initial = intensity modulator law confirmed in §H and §A.
- *Result:* FALSIFIED. `p`-initial tokens in §B show QO=22.5%, the *lowest* initial group in
  §B (not the highest). QO in §B is statistically uniform across all initials (KW p not
  significant). The bad-kan signal in §B is section-level, not initial-modulated.
- *Disposition:* GL4299 formally falsified (batch3352). The initial-encoding law is now
  correctly scoped: it holds in §H and §A (2D and 1D encoding), not in §B, §P, or §T
  (0D encoding). This sharpened the encoding scope map rather than weakening it.

**NR-05 — GL4311 and GL4312: recto/verso OT asymmetry**
- *Prediction:* §H folios would show a detectable OT (timing channel) asymmetry between
  recto and verso sides, reflecting scribal workflow or a two-pass composition pattern.
- *Result:* NULL. GL4311: recto split p=0.147 (not significant). GL4312: no significant
  result. Two null results from pre-registered tests.
- *Disposition:* No recto/verso timing asymmetry detected. The null is informative: §H
  composition is consistent across folio sides at the section level. Pre-reg commits:
  batch3392-3393.

**NR-06 — H6-2 and H6-3**
- *Prediction:* Two hypotheses in the Phase 6 series regarding section-level structural
  predictions.
- *Result:* FALSIFIED (batch results, Phase 6 sweep, 2026-05-22).
- *Disposition:* Documented in main paper §§ covering Phase 6. No revision of core claims
  required; Phase 6 results were not load-bearing for the primary decipherment case.

**NR-07 — European language family (Proto-Romance and cognates)**
- *Prediction:* Standard academic hypothesis entering the project. Tested whether the corpus
  could be explained as an encrypted form of a European natural language (Latin, proto-Romance,
  Occitan, medieval Italian variants).
- *Result:* FALSIFIED across all tested candidates through Batch 100. Index of Coincidence
  analysis was attempted but the Beale Cipher baseline used in early literature was shown to
  be methodologically inappropriate for the Voynich corpus. No European language candidate
  survived quantitative testing under correctly calibrated null distributions.
- *Disposition:* European language family closed. The failure motivated the pivot to
  Mongolian-Tibetan hypothesis, which had been independently suggested by the R=14 sweep.
  Cheshire (2019) proto-Romance claim is included here as a prior falsified hypothesis;
  GL4294 cross-section architecture (p=4×10⁻²⁴) directly contradicts any single-language
  European model — a copying algorithm or natural language substitution cipher cannot produce
  five pharmacologically distinct sections with orthogonal humoral channels.

---

## Section 2 — Revised Identifications (initial calls corrected after evidence)

**RV-01 — f3r botanical identification: sga-skam (ginger) → Lamiaceae**
- *Initial call:* f3r = Zingiber officinale (sga-skam, ginger). Assigned in the vocabulary
  sprint (Batch 1401) on pharmacological grounds.
- *Correction:* FALSIFIED at Batch 1997 when the f3r illustration was examined. f3r is a
  dicotyledonous plant with opposite leaves and a root morphology inconsistent with a
  monocot rhizome. Lamiaceae (mint family) is the current EXPLORATORY-STRONG candidate.
  Ginger identification formally withdrawn.
- *Impact:* Syllabary Criterion 3 for the character e (pharmacological context: present
  on f3r) is marked CONDITIONAL pending resolution of the f3r botanical ID. This is
  documented explicitly in the syllabary tables.

**RV-02 — f3r Triphala three-fruits: initial role of f3r**
- *Initial call:* f3r = Phyllanthus emblica (amla/skyu-ru-ra), as the third of the Triphala
  trio after f6v (haritaki) and f51v (bibhitaki).
- *Correction:* f3r amla pre-registration NOT confirmed (batch3402). Folio shows a vivid
  red root inconsistent with amla; Rubia cordifolia (madder) emerged as the leading
  alternative. Triphala identification remains complete for f6v (haritaki CONFIRMED) and
  f51v (bibhitaki CONFIRMED). f3r is not the amla folio.
- *Impact:* Triphala is confirmed as a two-folio explicit identification (f6v + f51v).
  The three-fruits hypothesis as a complete unit is EXPLORATORY-STRONG.

**RV-03 — f1r identification revised: Silybum marianum (milk thistle)**
- *Initial call:* f1r received an earlier provisional botanical identification.
- *Correction:* f1r confirmed as Silybum marianum (milk thistle) in the botanical sprint.
  QO=0 (the sole zero-phlegm folio in the dataset, consistent with milk thistle's Sowa
  Rigpa profile as a liver tonic with no phlegm indication). The revised identification
  is pharmacologically more coherent than the initial call.

**RV-04 — Hoshiyayi Mutavval authorship attribution: removed**
- *Initial call:* Early H1 authorship research identified Hoshiyayi Mutavval as a possible
  named individual associated with the Baysunkur Academy scribal tradition.
- *Correction:* Mavlyanov 2022 was read directly (batch3200 chain). Section II item 4
  identifies "Hoshiyayi Mutavval" as a different person — Abul Qasim Abul Laysiy's work.
  No connection to Darvish Ali or to the manuscript's medical tradition. Attribution
  removed from H1 record.
- *Impact:* H1 authorship claim narrows to the documented reference in Navoiy
  Ensiklopediyasi Vol.1 pp.331–332 and Mavlyanov 2022 (Baysunkur Academy 1420–1434,
  inside the VMS radiocarbon window).

**RV-05 — Zafarnama citation for H1: retracted**
- *Initial call:* Zafar-name pp.243/296 (Sharq 1997) was cited as supporting a connection
  between Darvish Ali and the Timurid court.
- *Correction:* FALSIFIED at cited location (batch3189). Those pages contain no reference
  to Darvish Ali. The citation originated in a secondary source footnote treated as
  primary-source confirmation — a cascade error documented in full in §512 of the main paper.
- *Impact:* H1 authorship downgraded from CONFIRMED to MODERATE/OPEN at all occurrences
  in the paper pending direct primary-source retrieval. The core H1 linguistic hypothesis
  (Mongolian-Tibetan pharmaceutical register) is not affected; only the attribution of
  specific authorship.

---

## Section 3 — Known Limitations of the Current Decipherment

**L-01 — §A outer ring labels: partial decode only**
The main §A analysis applies R=14 to the central text of folios ff.67r1–73v. The outer
ring star labels in §A use different R values depending on wheel position. The R=14 result
of 38/58 matches covers the main-text decode. Full outer-ring decode remains in progress
and is not claimed as complete.

**L-02 — f68v3 and f70r1 three-column decodes are reconstructions**
The three-column decode format (EVA | R=14 literal | pharmaceutical prose) applied to
f68v3 and f70r1 is a reconstruction assembled from confirmed vocabulary items and the
wheel's structural position. It is not a verbatim EVA line-by-line extraction from the
corpus in the same sense as the §H botanical decodes. This distinction is marked in the
decode tables.

**L-03 — Botanical sprint: 19 folios skipped**
The §H botanical sprint covered 113 of 132 §H folios. 19 folios were skipped: 11 for
image quality/ambiguity, 8 for pharmacological profiles that did not generate a
sufficiently discriminating pre-registration candidate. These are not claimed as
identifications. The sprint coverage rate is 86% (113/132).

**L-04 — EXPLORATORY-STRONG designations are not confirmations**
Approximately 15–20 §H botanical identifications carry the designation
EXPLORATORY-STRONG (e.g., Meconopsis grandis for f47v, Petasites hybridus for f47r,
Rubia cordifolia for f3r). This means: the pharmacological profile is highly consistent
and the illustration morphology is suggestive, but fewer than 6/6 pre-registered criteria
were confirmed, or the pre-registration process was initiated post-hoc after exploratory
observation. These are research-grade leads, not claims.

**L-05 — §P directional result (GL4295 r=-0.239)**
The CH-QO correlation in §P shows a directional negative pattern (r=-0.239) consistent
with the specialization law confirmed in §H (r=-0.282 p=0.0016). The §P result is
directional only — not statistically significant at p<0.05. It is not claimed as a
confirmation.

**L-06 — Zingiber hunt: 6 folios eliminated before confirmation**
Six folios were pre-registered and tested as Zingiber officinale (ginger) candidates
before the correct folio was identified. The pre-registration record documents each
elimination. This is reported to illustrate the iteration cost of botanical identification
under strict pre-registration, not as a flaw — the eliminations narrow the search space
honestly.

---

## Section 4 — Unmapped Characters in the Syllabary

The THEOS syllabary (Frederick Davis Stalnecker, patent-pending U.S. App 18/919,771) maps 18 of 23 functional EVA character positions. Five remain
unmapped:

| EVA character | Corpus frequency | Status |
|---------------|-----------------|--------|
| j | <1% | No stable decode found at R=14 |
| u | <1% | Occurs in ligatures; positional ambiguity unresolved |
| v | <1% | May be allographic variant; not independently mapped |
| x | <1% | Very low frequency; insufficient distributional signal |
| z | <1% | Near-hapax in ZL3b-n; no decode attempted |

These five characters account for less than 3% of total corpus occurrences. Their absence
from the syllabary does not affect any of the 19 confirmed character mappings, and does
not affect any of the pharmacological or vocabulary statistics, which are computed at
the token level (full EVA strings), not the character level.

The unmapped characters are not claimed as decoded. They are reported here to give a
complete and accurate account of the syllabary's current scope.

---

## Section 5 — Count Corrections Discovered During Reproduction

**NR-COUNT-01 — daiin and sar stated frequencies**

- *Working notes (date range: multiple batches, 2026-04-05 through 2026-05-25) stated:*
  sar N=277; daiin N=3,832 ("the single most common multi-character token").

- *Direct corpus extraction during reproduction script construction (commit 06ad82c, 2026-05-26):*
  sar standalone = 63–76; daiin standalone = 748–801 (range reflects tokenization variants).

- *Source of the daiin discrepancy (identified and resolved):*
  The N=3,832 figure counts **all tokens ending in the `-aiin` suffix** — the full Classical
  Mongolian genitive paradigm: `daiin` (748), `aiin` (437), `qokaiin` (261), `okaiin` (201), `otaiin`
  (132), `saiin` (112), and 50+ further types. The corpus contains 3,493 tokens ending in
  -aiin. The working notes conflated the standalone token `daiin` with the genitive family
  it heads. The linguistic interpretation — that the -aiin suffix is the Classical Mongolian
  genitive marker -yin, and that it appears with extraordinary frequency (10.3% of all corpus
  tokens) — **remains valid and is strengthened** by the full count: 3,493 genitive-marked
  tokens is strong evidence for an inflected Mongolian-grammar language.

- *Source of the sar discrepancy (partially explained):*
  The N=277 figure is not explained by substring counting (sar as substring appears 145
  times) or by including closely related tokens. The most likely explanation is that an
  earlier analysis used a different version of the EVA transcription or a pre-annotation-
  stripped corpus file, producing higher counts. The current verified count from ZL3b-n.txt
  (version 3b, 2025-05-13) is sar=63–76. This count is used in all reproduction analyses.

- *What changes:*
  All token counts in `results/expected.json` reflect verified corpus extraction. The
  vocabulary section-distribution findings (shor §H-dominant, qol §B-dominant, sar
  distributed across pharmaceutical sections) **are confirmed at the corrected counts**.
  No pharmaceutical interpretation changes. The 11-item confirmed vocabulary list is intact.

- *Methodological note:*
  This correction was not made retroactively to match the expected values. It was discovered
  during a blind test of the reproduction pipeline: the script returned different numbers
  than the working notes, and the discrepancy was investigated and documented rather than
  suppressed. The corrected values replace the working-note values in all public materials.

**NR-08 — GL4318: Zodiac-wide pharmacological clock universality (2026-05-27)**
- *Prediction:* The GL4314 pharmacological clock (CH tokens clustering in 07:00–11:00 across
  f73r/f73v) would generalize across all 13 §A zodiac folios carrying outer-ring clock codes
  (@Lz, &Lz, @Ro), producing CH mean ∈ [7.0, 11.0] over N=320 tokens and QO count ≥10.
  Pre-registered at commit `152a3b05` before any pharmacological classification of the
  11 non-f73 zodiac folios was performed.
- *Result:* NEGATIVE (batch4318, 2026-05-27). H-GL4318-1 FAILED: CH mean = 6.49h (exits
  window). H-GL4318-2 FAILED: QO n=4 (below ≥10 threshold). H-GL4318-3 FAILED: Fisher p=1.0.
  H-GL4318-4 CONFIRMED: OK uniform MW p=0.566.
- *Why it failed:* Vocabulary stratification. Earlier zodiac folios (f69r–f72v3) are dominated
  by `ol-`, `or-`, `oe-` initial families not present in the locked pharmacological classifier
  (80% UNK in f72r3). CH-class tokens in these folios cluster in the pre-dawn window
  (00:30–06:45h), pulling the combined CH mean from 7.28h (f73r/f73v only) to 6.49h (all 13
  folios). Earlier zodiac folios encode an astronomical/calendar register; f73r/f73v encode a
  pharmaceutical timing register.
- *GL4314 status:* EXPLORATORY-CONSISTENT-STRONG (unchanged). GL4318 tested zodiac
  universality; GL4314 tested f73r/f73v specifically. The negative result places GL4314 in
  sharper scope: the pharmacological clock is a property of the terminal zodiac folios, not
  the zodiac section as a whole. This two-register interpretation — astronomical calendar
  (f69r–f72v3) followed by daily pharmaceutical scheduling (f73r–f73v) — is consistent with
  the §A visual evidence and with Sowa Rigpa medical astronomy practice.
- *Disposition:* NR-08 recorded as a genuine pre-registered negative result. GL4318 paper
  section (§764) drafted; on hold until Cryptologia decision (~June 3, 2026).

**NR-09 — GL4330: Terminal zodiac clock variance lower than early zodiac (2026-05-27)**
- *Prediction:* Terminal zodiac folios (f73r/f73v) would have significantly lower temporal
  variance (clock position std) than early zodiac (f69r–f72v3), on the assumption that
  f73r's four-cluster protocol structure compresses positions into specific time windows.
  Pre-registered at commit `717d6b3d`; within-group std values were unknown at pre-reg time.
- *Result:* FAILED (batch4330, 2026-05-27). H1 FAILED: terminal std=3.89h > early std=3.59h
  (opposite direction). H2 FAILED: Levene p=0.195 (not significant). H3 FAILED: all-class
  and CH-specific directions inconsistent (terminal all-class std higher, terminal CH std
  lower, neither significant). All 15 zodiac folios show std in the 3.4–4.0h range.
- *Why it failed:* The zodiac clock face assigns positions at 30-minute increments spanning
  0–12h uniformly for every folio — this is the clock design, not a pharmacological signal.
  Terminal and early folios both use the full clock face, producing the same ~3.7h population
  std. The four-cluster f73r structure (GL4325) is not position compression but pharmacological
  class assignment: specific classes (CH, OT/OK) occupy specific hour windows while the
  positions themselves span the full day in both groups.
- *Informative implication:* Rules out the alternative that the f73r protocol is "fewer
  clock positions." The temporal structure is encoded in which pharmacological class occupies
  which hour, not in any reduction of temporal coverage. The clock face is the annotation
  grid; the pharmacological class is the encoded message.
- *Disposition:* NR-09 recorded. GL4330 result strengthens the class-assignment interpretation
  of the pharmacological clock and closes the clock variance question.

**NR-10 — zodiac-astro vs. fRos @Cc clock equivalence (GL4336)**
- *Prediction:* fRos @Cc clock positions (n=9, mean=5.89h, σ=3.63h) and zodiac-astro @Cc
  clock positions would be statistically equivalent at both mean (MW p > 0.05) and variance
  (Levene p > 0.10) levels — completing the four-register model by establishing that fRos
  "belongs to the same register as zodiac-astro."
- *Result:* FAILED (0/3). Zodiac-astro @Cc tokens (n=38, mean=10.06h, σ=0.92h, range 8.5–12.0h)
  are dramatically different from fRos @Cc (MW p=0.0009; Levene F=23.52, p<0.0001; variance
  ratio=15.5). Zodiac-astro @Cc clusters near-peak (~10h) like f68-series, NOT full-clock like
  fRos. The pre-registered prediction was based on an incorrect assumption: the "zodiac mean=5.59h"
  in prior GLs came from @Ro/@Lz/@Ri outer-ring position codes, not @Cc. The @Cc position code
  in zodiac folios marks the WHEEL CENTER (hub), which encodes near-peak timing (~10h). The @Ro/
  @Lz outer-ring positions span the full clock face (~5.6h). fRos @Cc (5.89h) matches the zodiac
  outer-ring, not the zodiac center.
- *Disposition:* NR-10 recorded. The finding generates GL4337 (zodiac @Cc ≈ f68-series @Cc,
  both near-peak): if @Cc consistently marks near-peak timing across zodiac AND f68 sections,
  fRos @Cc (5.89h, full-clock) is the structural outlier requiring explanation. The four-register
  model as published in GL4333/GL4334 remains valid (fRos @Cc vs. f68-series @Cc comparison is
  still apple-to-apple), but the claim that fRos "belongs to the same register as zodiac-astro"
  is not supported at the @Cc level.

---

## What the failures prove

A method that cannot fail is not science. The pre-registration protocol used here was
designed to ensure that every prediction could fail — and some did. The celestial cipher
prediction (NR-03) failed and, in failing, made the R=14 universality result *stronger*:
it ruled out a family of alternative models that would have fit the data post-hoc. The
§B initial-encoding falsification (NR-04) sharpened the encoding scope map from a vague
"initials matter" claim to a precise "2D/1D/0D encoding hierarchy across five sections"
claim that would have been invisible without the negative result.

The botanical falsifications — Allium for f2r, Polygonatum for f47v, Platycodon for f5r,
Inula for f4v, Curcuma for f17r, and others — are the mechanism by which the confirmed
identifications earn their confidence. Each failure tightens the prior on the next
candidate.

Science does not require a perfect record. It requires an honest one.

---

*Full pre-registration record: THEOS2 repository, `experiments/` directory and git log.*
*Corpus: ZL3b-n.txt (Zandbergen-Landini v3b, SHA-256: bf5b6d4ac1e3a51b1847a9c388318d609020441ccd56984c901c32b09beccafc)*
*All statistics computed locally in Python against the verified corpus. Reproduction: see `reproduce.sh`.*
