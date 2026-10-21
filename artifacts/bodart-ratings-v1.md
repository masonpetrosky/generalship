# Bodart: broader provisional command-label ratings

**542 field engagements · 669 command labels · 72 ordered labels.** A first exploratory ranking from our own source table and model. Primary-verified; printed labels are not resolved historical identities.

[Download estimates](bodart-ratings-v1.csv) · [Saved run, folds and sensitivities](bodart-ratings-v1.json) · [Every inclusion/exclusion](../data/bodart/ratings-v1/cohort.json) · [Fixed design](../docs/bodart-ratings-v1.md) · [Source table](bodart-bulk-v1.csv)

## Does command information help held-out prediction?

Each calendar decade is excluded from training in turn. Lower scores are better. This is a development diagnostic, not a final or forward test; campaigns can cross decade boundaries.

| Model | Battle log loss | Equal-decade log loss | Battle Brier | Equal-decade Brier |
| --- | ---: | ---: | ---: | ---: |
| Equal odds | 0.693147 | 0.693147 | 0.250000 | 0.250000 |
| Force only | 0.663196 | 0.719430 | 0.234880 | 0.261950 |
| Force + command labels | 0.638346 | 0.701488 | 0.223695 | 0.253022 |

Command-label minus force-only log loss: **-0.024850 per battle**, **-0.017942 per decade**. These point differences do not establish correct skill rankings or isolate AI’s benefit. No uncertainty-adjusted claim of predictive superiority is made.

Held-out label availability: both previously seen 39/542, one seen 183/542, neither seen 320/542. Unseen labels receive prior mean zero, not an invented career rating.

## Provisional orders

Orders compare only labels within the same connected opponent component and require three included engagements. θ is the shrunk conditional log-odds association. The 95% intervals are approximate marginal Laplace intervals conditional on this model and its inputs; they do not include OCR, identity, source, army or campaign uncertainty. Adjacent orders with overlapping intervals should not be read as settled differences. No cross-component or causal wins-above-replacement ranking is supplied.

### Opponent component 1

51 ordered labels out of 178 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | napoleon i | 1805–1813 | 20 (19) | 20 | +1.968 (+0.845, +3.090) | 1 / 1 |
| 2 | bonaparte | 1796–1800 | 18 (17) | 18 | +1.712 (+0.557, +2.867) | 2 / 2 |
| 3 | gf suworow | 1773–1799 | 5 (5) | 4 | +1.223 (-0.237, +2.683) | 4 / 3 |
| 4 | gouvion st cyr | 1799–1812 | 9 (8) | 9 | +1.066 (-0.227, +2.360) | 3 / 7 |
| 5 | gf wittgenstein | 1812–1813 | 7 (5) | 7 | +1.004 (-0.299, +2.307) | 6 / 5 |
| 6 | moreau | 1796–1800 | 16 (12) | 16 | +0.966 (-0.102, +2.034) | 5 / 6 |
| 7 | erzhz karl von österreich | 1796–1799 | 5 (4) | 5 | +0.965 (-0.457, +2.388) | 7 / 4 |
| 8 | sir wellesley | 1808–1809 | 4 (4) | 4 | +0.794 (-0.776, +2.363) | 9 / 9 |
| 9 | fh v melas | 1799–1799 | 4 (4) | 4 | +0.788 (-0.816, +2.392) | 10 / 8 |
| 10 | lannes | 1800–1806 | 3 (3) | 3 | +0.764 (-0.850, +2.378) | 8 / 10 |
| 11 | richepanse | 1800–1800 | 4 (4) | 4 | +0.726 (-0.867, +2.319) | 11 / 11 |
| 12 | erzhz karl v österreich | 1796–1809 | 14 (7) | 14 | +0.604 (-0.491, +1.700) | 17 / 12 |
| 13 | ney | 1799–1812 | 8 (6) | 8 | +0.471 (-0.827, +1.769) | 12 / 22 |
| 14 | baron melas | 1800–1800 | 4 (3) | 4 | +0.471 (-1.048, +1.990) | 20 / 13 |
| 15 | gf wurmser | 1793–1796 | 7 (4) | 7 | +0.460 (-0.916, +1.836) | 19 / 14 |
| 16 | victor | 1797–1812 | 6 (4) | 6 | +0.441 (-0.930, +1.812) | 14 / 16 |
| 17 | baron beaulieu | 1793–1796 | 4 (2) | 4 | +0.437 (-1.131, +2.006) | 21 / 15 |
| 18 | pz v coburg | 1793–1793 | 4 (3) | 4 | +0.413 (-1.089, +1.916) | 15 / 19 |
| 19 | fürst schwarzenberg | 1805–1813 | 4 (3) | 4 | +0.380 (-1.170, +1.929) | 22 / 18 |
| 20 | fh v elsnitz | 1799–1800 | 3 (2) | 3 | +0.323 (-1.225, +1.871) | 23 / 26 |
| 21 | soult | 1799–1813 | 13 (7) | 13 | +0.317 (-0.749, +1.383) | 16 / 24 |
| 22 | lecourbe | 1799–1800 | 8 (5) | 8 | +0.299 (-0.944, +1.541) | 18 / 25 |
| 23 | macdonald | 1794–1813 | 5 (3) | 5 | +0.285 (-1.145, +1.714) | 25 / 20 |
| 24 | lefebvre | 1796–1809 | 5 (3) | 5 | +0.259 (-1.185, +1.702) | 24 / 27 |
| 25 | erzhz johann v österreich | 1800–1809 | 6 (3) | 6 | +0.230 (-1.170, +1.630) | 28 / 17 |
| 26 | jourdan | 1793–1799 | 8 (4) | 8 | +0.215 (-1.027, +1.458) | 29 / 21 |
| 27 | desaix | 1796–1798 | 3 (2) | 3 | +0.212 (-1.348, +1.773) | 26 / 31 |
| 28 | suchet | 1800–1813 | 11 (7) | 11 | +0.198 (-1.003, +1.399) | 13 / 42 |
| 29 | erzhz ferdinand v österreich | 1805–1809 | 3 (2) | 3 | +0.194 (-1.382, +1.770) | 27 / 37 |
| 30 | fh v hiller | 1809–1809 | 3 (1) | 3 | +0.134 (-1.516, +1.785) | 33 / 23 |
| 31 | colli | 1793–1796 | 3 (1) | 3 | +0.127 (-1.472, +1.726) | 30 / 28 |
| 32 | barclay de tolly | 1807–1813 | 4 (2) | 4 | +0.082 (-1.465, +1.630) | 31 / 34 |
| 33 | fh v bennigsen | 1807–1807 | 3 (1) | 3 | +0.063 (-1.587, +1.713) | 41 / 32 |
| 34 | fh v kray | 1794–1800 | 9 (4) | 9 | +0.030 (-1.183, +1.243) | 37 / 39 |
| 35 | masséna | 1794–1811 | 23 (12) | 23 | +0.019 (-0.881, +0.919) | 34 / 35 |
| 36 | baron davidovich | 1796–1796 | 3 (1) | 3 | +0.018 (-1.665, +1.702) | 39 / 36 |
| 37 | gf sztarray | 1796–1800 | 4 (1) | 4 | +0.009 (-1.528, +1.547) | 42 / 29 |
| 38 | vizekönig pz eugen beauharnais | 1809–1813 | 6 (3) | 6 | +0.007 (-1.400, +1.415) | 35 / 30 |
| 39 | championnet | 1798–1799 | 3 (1) | 3 | -0.002 (-1.620, +1.616) | 36 / 38 |
| 40 | pz v koburg | 1794–1794 | 4 (2) | 4 | -0.008 (-1.484, +1.469) | 32 / 40 |
| 41 | grenier | 1799–1799 | 3 (1) | 3 | -0.056 (-1.709, +1.597) | 40 / 41 |
| 42 | gf latour | 1794–1796 | 4 (1) | 4 | -0.072 (-1.596, +1.452) | 43 / 33 |
| 43 | dumouriez | 1792–1793 | 4 (2) | 4 | -0.080 (-1.599, +1.440) | 38 / 44 |
| 44 | oudinot | 1799–1813 | 5 (2) | 5 | -0.176 (-1.587, +1.234) | 44 / 43 |
| 45 | schérer | 1795–1799 | 3 (1) | 3 | -0.258 (-1.806, +1.291) | 45 / 45 |
| 46 | fürst bagration | 1799–1812 | 4 (1) | 4 | -0.352 (-1.902, +1.199) | 46 / 47 |
| 47 | fh v hotze | 1799–1799 | 6 (2) | 6 | -0.374 (-1.716, +0.969) | 47 / 46 |
| 48 | gf clerfayt | 1794–1795 | 7 (2) | 7 | -0.561 (-1.888, +0.766) | 48 / 49 |
| 49 | pichegru | 1794–1795 | 8 (3) | 8 | -0.573 (-1.872, +0.725) | 49 / 48 |
| 50 | fh v ott | 1800–1800 | 3 (0) | 3 | -0.879 (-2.454, +0.697) | 50 / 51 |
| 51 | blake | 1808–1811 | 8 (1) | 8 | -0.948 (-2.305, +0.409) | 51 / 50 |
### Opponent component 2

2 ordered labels out of 9 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | bern | 1849–1849 | 3 (1) | 0 | -0.154 (-1.737, +1.430) | 1 / 1 |
| 2 | görgey | 1849–1849 | 4 (1) | 0 | -0.450 (-1.947, +1.047) | 2 / 2 |
### Opponent component 3

3 ordered labels out of 8 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | sir abercrombie | 1799–1801 | 4 (4) | 4 | +0.865 (-0.707, +2.436) | 1 / 1 |
| 2 | brune | 1799–1799 | 4 (2) | 4 | +0.184 (-1.327, +1.695) | 3 / 2 |
| 3 | hz v york | 1793–1799 | 5 (3) | 5 | +0.177 (-1.270, +1.624) | 2 / 3 |
### Opponent component 4

1 ordered labels out of 7 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | davoust | 1805–1812 | 7 (6) | 7 | +0.763 (-0.606, +2.132) | 1 / 1 |
### Opponent component 5

2 ordered labels out of 7 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | j b hood | 1864–1864 | 3 (1) | 0 | -0.159 (-1.749, +1.431) | 1 / 1 |
| 2 | j johnston | 1864–1866 | 4 (1) | 0 | -0.189 (-1.730, +1.351) | 2 / 2 |
### Opponent component 6

1 ordered labels out of 6 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | friedrich ii | 1742–1760 | 5 (4) | 0 | +0.801 (-0.640, +2.243) | 1 / 1 |
### Opponent component 7

2 ordered labels out of 5 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | don ricardos | 1793–1793 | 4 (3) | 4 | +0.496 (-1.002, +1.995) | 1 / 1 |
| 2 | b g daoust | 1793–1793 | 3 (1) | 3 | -0.277 (-1.860, +1.305) | 2 / 2 |
### Opponent component 9

1 ordered labels out of 5 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | g garibaldi | 1860–1867 | 4 (2) | 0 | -0.005 (-1.475, +1.466) | 1 / 1 |
### Opponent component 10

1 ordered labels out of 5 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | gf tilly | 1622–1632 | 3 (1) | 0 | -0.165 (-1.736, +1.407) | 1 / 1 |
### Opponent component 12

1 ordered labels out of 4 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | mqs de la roche jacquelin | 1793–1793 | 4 (3) | 4 | +0.174 (-1.360, +1.709) | 1 / 1 |
### Opponent component 13

1 ordered labels out of 4 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | kosciuszko | 1792–1794 | 3 (2) | 3 | +0.309 (-1.255, +1.872) | 1 / 1 |
### Opponent component 14

2 ordered labels out of 4 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | gf radetzky | 1848–1848 | 3 (3) | 0 | +0.774 (-0.880, +2.428) | 1 / 1 |
| 2 | könig carlo alberto von sardinien | 1848–1848 | 3 (1) | 0 | -0.404 (-2.018, +1.210) | 2 / 2 |
### Opponent component 15

1 ordered labels out of 4 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | hoche | 1793–1797 | 3 (2) | 3 | +0.143 (-1.433, +1.719) | 1 / 1 |
### Opponent component 17

1 ordered labels out of 4 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | könig karl xii | 1701–1708 | 3 (3) | 1 | +0.980 (-0.622, +2.582) | 1 / 1 |
### Opponent component 24

1 ordered labels out of 3 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | rosecrans | 1862–1863 | 3 (2) | 0 | +0.163 (-1.451, +1.777) | 1 / 1 |
### Opponent component 29

1 ordered labels out of 3 estimated labels.

| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | gf lambert | 1812–1812 | 3 (3) | 3 | +0.649 (-1.008, +2.306) | 1 / 1 |

## Coverage and fixed sensitivities

The parent table has 1682 entries; 542 enter this experiment and 1140 do not. All 52 reserved-final entries are excluded before numerical use. Exclusion reasons overlap:

| Reason | Entries |
| --- | ---: |
| command_label_span_over_60_years | 4 |
| indecisive | 14 |
| loser:ambiguous_personnel_flags | 533 |
| loser:joint_or_complex_command_label | 149 |
| loser:missing_command_label | 231 |
| loser:missing_positive_personnel | 529 |
| naval | 121 |
| no_combat | 10 |
| outside_single_field_engagement_types | 678 |
| reserved_final | 52 |
| unknown_year | 70 |
| winner:ambiguous_personnel_flags | 428 |
| winner:joint_or_complex_command_label | 198 |
| winner:missing_command_label | 155 |
| winner:missing_positive_personnel | 425 |

Included source status:

| Status | Entries |
| --- | ---: |
| existing_image_checked_transcription | 346 |
| ocr_candidate_not_image_verified | 188 |
| ocr_candidate_with_checked_fields | 8 |

There are 204 disconnected opponent components; 597 labels have fewer than three appearances and receive no order. Rank removal normalizes titles, not biographical aliases or every spelling error. Bonaparte and Napoleon I can remain separate; homonyms can remain. No label is verified by reputation.

Unchecked OCR years can place a record in the wrong evaluation decade. Embedded rank text is excluded conservatively, including some valid single names with nationality prefixes. Only the listed fields of sampled images were checked; other OCR readings remain candidates.

The prior columns use fixed θ prior SD 0.5 / 2 on the same rows (primary SD 1). They are sensitivity orders, not confidence bounds. The personnel-checked subset has **354/542 engagements**, **351 labels** and **61 ordered labels**. It is a different cohort, not an equal-coverage accuracy comparison; scoped personnel checks do not verify the OCR command names. Full subset estimates remain in the saved JSON.

## What was fitted and verified

`logit(p_A) = beta * log(personnel_A/personnel_B) + theta_A - theta_B`, with labels sorted before assigning the outcome. No intercept, no winner-first orientation, no imported ratings. Gaussian priors: beta SD 2, theta SD 1. Estimated beta = 0.843318; maximum penalized gradient = 3.2e-12. A force coefficient is an association in a selected historical compilation; force advantages may be commander-created mediators. Army quality, appointment selection and source bias can drive apparent command effects.

Protocol/code/cohort were committed before fitting at `ea022c1517aeea317f39a548fe1355d8b3201581`. The saved run binds their SHA-256 hashes. Verification checks every fold membership and saved prediction, selection denominator, penalized gradient, marginal inverse-Hessian solve and reported metric without refitting historical outcomes. Toy tests check the numerical methods. The source table retains quoted passages, locators, raw readings and source/image hashes. No original frozen model or final evaluation set changes.

`python3 -m generalship.bodart_ratings --write` regenerates this page and CSV from the saved run. The default verifies them. `make reproduce` does not run the historical fitting job.
