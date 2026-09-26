# Commander ratings run 3 (grade E, all battles): separate review of code and results

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. I ran as a new subagent with fresh context, and the author's conversation was not an input.
- **Date:** 2026-09-25.
- **Commits:**
  - Prepared: `e1e07849e7ba1649b8e21250f983150e78d5256f`.
  - Previous: `3979161405b99cfc5da3e57b71c5d7e418953c39`.
  - Bundle (worktree HEAD): `991f4e5333b64c499eb617de42c26246065a8e88`. It adds only `assignment.md` and `inputs.json`.
  - Code: `generalship/`, `tests/`, the design and the grade E output are unchanged between `82901a9` and `e1e0784`, which run 3 cites.
- **Assignment:** `assignment.md`, sha256 `d3763d494969e70d787b877a8c26246e32eb85a21fc8816c5977dd52e7f4edd2`.
- **Input manifest:** `inputs.json`, sha256 `d605c8d0eca5522a20a043a54a16de9b52adbdfe9e68f090880896273938c16d`. Both match the hashes in the dispatch.
- **Outcome: corrections required** (R1–R5). All five are wording changes to the memo `docs/research/commander-ratings-v3.md`. I found no divergence in the code or results that changes a number or the verdict. Advisories A1–A10 are listed separately.

This AI review is a separate analysis. It is not human historical adjudication, feature admission or authorization of any fit.

## Input verification

- **Manifest paths.** All 21 paths in `inputs.json` match their sha256 at `git show e1e0784:<path>`, and the worktree copies are byte-identical. There is no mismatch.
- **Files the manifest does not bind.** The assignment names further files that `inputs.json` does not bind (see A10). I hashed them at the worktree HEAD. They are unchanged since `82901a9`.

| Path | sha256 |
|---|---|
| `docs/strength-imputation.md` | `15bdb6a2d9db1329ff1ed42a21d175b152cfa845f09eabe8078a617e4f2ed635` |
| `docs/commander-ratings.md` | `0ab4b7d541baf4f8e642634f316628f9cb372d68dcdbbc047a305f5a1fb704bb` |
| `data/command/rating-authorization-v3.json` | `690e2b3e264e9c5a594e1f1f4e7f1e65b064a3cfeecea121a745b08be2d8fd17` |
| `generalship/imputation.py` | `d3275c226f4a874c4c1c16d6a372cc89a5f765cf1fe4b8eaaab92e66577f99a7` |
| `generalship/ratings_v3.py` | `3a5b4396c2849d6f8908525925a7da5e4e30de4aacc22b19ac8f2e991756801f` |
| `tests/test_imputation.py` | `2fc55c1c740aaa5f0ce4a9569fbc0e7111b666b44bed8eb36b2b629ba34b9867` |
| `artifacts/strength-imputation-v1.json` | `f798faf37763d42f445773031bb613c0739618b1e3a50f46d58d810b98ad1caa` |
| design review `review.md` (imputation-design-2779bb6) | `b5aa284bcab581c7b40c81f145bf3f43996c9bc6ce72a7b333675a29b03351d3` |

The bindings in the run output and in the authorization record also check out:

- The authorization record's hashes for the design, imputation output, both ledgers, registry and campaigns all equal the `bindings` in `commander-ratings-v3.json`.
- The design and imputation hashes above match those bindings. The quoted owner response ("You're good to run it") is in the record.
- `admits_feature` and `changes_baseline` are both `false`.

## Scope actually inspected

**Read in full:**
- `AGENTS.md`
- `docs/strength-imputation.md`
- `generalship/imputation.py`
- `generalship/ratings_v3.py`
- `tests/test_imputation.py`
- `docs/research/commander-ratings-v3.md`
- `artifacts/commander-ratings-v3.md`
- `data/command/rating-authorization-v3.json`
- `docs/commander-ratings.md` §§3–8

**Read in part:**
- **`generalship/ratings.py`:** the `fit` signature, `predict`, `components`, `summarize`, `attribution`, `attach` and `primary_rows`.
- **`generalship/baseline.py`:** `scores`.
- **`generalship/estimates.py`:** the constants, `conditions`, `class_of`, `round10` and `printed_value`.
- **Build files:** the `Makefile` and a grep of `generalship/cli.py`.
- **The design review:** its headings, R1–R8, A1–A4 and `correction.json`.
- **`artifacts/commander-ratings-v3.json`:**
  - the model, heldout, temporal and view summaries;
  - every commander's summary fields;
  - `views.median_imputation` for every commander.

The 180 robustness views were not inspected one by one.

**Hash-verified but not read:** `README.md`, `docs/methodology.md`, `docs/evidence-contract.md` and `docs/sources.md`, plus the raw CSVs and the admission, cohort and baseline files. For `docs/roadmap.md` I only grepped the Native American records line.

**Computed in memory** (no artifact written; the worktree stayed clean):

1. **`imputation.build(root, verify=False)`** equals the stored `artifacts/strength-imputation-v1.json` exactly, bindings included. I also checked the grade E sides:
   - `low ≤ point ≤ high` on all 262 sides;
   - no bound is violated;
   - the 102 set-aside directional inputs have these reasons: 52 opponent/hearsay, 29 applicability unresolved, 20 post-start and 1 multiple adjustments.
2. **Verdict recomputed from the stored `heldout_test.predictions` (301 rows):**
   - Battle-weighted log loss: 0.647586 (commander) against 0.659688 (strength only), a difference of −0.012102.
   - Campaign-weighted, over 108 campaigns: 0.658583 against 0.665062, a difference of −0.006479.
   - Strictly lower under both weightings, so `improved = True`.
   - Campaigns better: commander 61, strength only 47, ties 0.
   - Effective denominator: 243 distinct rows.
   - All of these equal the stored values.
3. **Two leave-one-campaign-out folds recomputed for all 20 imputations:** Streight's Raid (1 row) and Franklin–Nashville (8 rows). I rebuilt the rows with `base_rows` and `imputations(rows)` (seed 20260926), then refitted both models on each fold's training rows. The averaged per-row probabilities equal the stored ones exactly (difference 0.0) for both models on all 9 rows.
4. **Further refits:**
   - `median_imputation` refit: every commander's θ equals the stored view value (max |Δ| = 0.0), and β = 0.8646.
   - Primary pooled θ, as the mean of 20 modes: max |Δ| from the stored value is 0.0. Pooled β is 0.62936, equal to the stored value. Per-imputation β ranges from 0.437 to 0.875.
5. **Row counts:**
   - 301 rows;
   - nested records dropped: GA012, LA009, VA033, VA034;
   - unresolved: TN035;
   - 162 rows with a modelled side and 17 with a post-start side;
   - y = 1 on 184 rows and 0 on 117. The frame's results are only `Union` and `Confederate`.
6. **Per-commander claims in the memo:**
   - 94 ranked (52 US, 42 Confederate);
   - only Forrest's 80% interval excludes 0, and no 95% interval does;
   - SD ratios among the ranked run from 0.729 to 0.964;
   - no `view_sensitive`;
   - 19 `not_connected`;
   - 93 of 94 rank-80% intervals span at least half their side's list.
7. **Descriptive split of the stored predictions by row label:** see A4.

**`make check`:** run offline, exit 0. All 151 tests passed and `generalship check` passed (`artifacts_written: false`).

**Not done:**
- I did not rerun the 75-minute run.
- I did not recompute the Laplace or rank draws, the intervals, the temporal split, the Monte Carlo halves or the 180 robustness and other views. The Monte Carlo halves need per-imputation held-out probabilities, which the JSON does not keep.
- No network, research or agents were used.

## 1. Design fidelity

**`imputation.py` against design §2: faithful.** Each item below was checked against the code:

- **Training rows:** sides graded A–C with a point and no `post_start_information`, 348 − 20 = 328.
- **Response:** the log of the point.
- **Joint-command sides:** coded `unknown` in training and in imputation, with `joint_command_echelon_unknown` on the grade E sides (15).
- **Merges:** levels with fewer than 5 rows merge into `unknown`, with the merges recorded. Reference levels are `unknown`, US, 1863 and Eastern.
- **Ridge:** unpenalized intercept, λ = 1.
- **σ:** √(RSS/n)·√(n/(n−p)), with p = 12 including the intercept.
- **Leave-one-out calibration:** each row is refitted without itself and scored against N(μ₋ᵢ, σ₋ᵢ²). c = 0.7805, and k = 1.08 is the first point on the 0.01 grid reaching 0.80. k is never below 1.
- **Other reported statistics:** the leave-one-out median absolute log error overall and by echelon, and the leave-one-campaign-out coverage at k (0.7957).
- **Bound eligibility:** a directional bound qualifies if it is class A or B after removing the `BOUND` codes, with no point-basis condition.
- **Bound values and conflicts:** each bound takes its printed midpoint. L is the maximum lower bound and U the minimum upper bound. If L > U, neither is applied and the side gets `bound_conflict` (2 sides: KY005 US, VA022 US).
- **Truncation:** `bound_dominates` applies when the truncated mass is below 1e-12, with the side placed at the nearer bound. No side has it in v1.
- **Point and range:** median, 10th and 90th percentiles, rounded to 10 (halves up, floor 10).
- **Labels:** as declared.

There are two small differences from the design's text, neither with any effect on the values (A1, A2).

**`ratings_v3.py` against §§3–7: faithful.**

- **Rows and nesting (§3):** 301 rows. The contained records of `nested` pairs are dropped, and TN035 is the only unresolved contained record left.
- **Draws (§5):**
  - one `random.Random(20260926)` stream, taken in the order imputation, then battle ID, then US before Confederate;
  - each draw is the inverse CDF on the standardized truncation limits;
  - the same 20 imputed sets are reused in the held-out test and the primary.
- **Pooled estimates:**
  - θ is the mean of the modes;
  - 1,000 draws per imputation (20,000 in all) for the 80% and 95% intervals;
  - 1,000 joint Laplace draws per imputation for the within-side ranks.
- **Held-out test:**
  - both models are fitted per fold and imputation;
  - each held-out probability is averaged over the 20 imputations, and log loss is scored on those averages;
  - improvement requires strictly lower log loss under both weightings;
  - the effective denominator is reported;
  - the Monte Carlo check uses imputations 1–10 and 11–20;
  - the temporal split trains on 1861–63 and tests on 1864–65.
- **Views (§6):**
  - The robustness list is: τ 0.25 and 1.0, α sd 3, grades A–B, superior, command-changed excluded and successor, the four endpoints and 169 alternative-candidate refits (180 in all).
  - `view_sensitive` and `unranked_in_view` are computed against `median_imputation`, following commander-ratings §6.
  - The other views do not set `view_sensitive`.
  - `strength_graded_only` reproduces run 2 (max |Δθ| = 0.0, 126 rows).
- **Raw residual:** the outcome minus the averaged held-out strength-only p, oriented to the commander's side.
- **Gate:** the run refuses to start unless the six hashes match and the authorization admits no feature and leaves the baseline unchanged. It also requires the stored imputation to reproduce.

I found no divergence that changes a number or the verdict.

## 2. Reproduction

Reproduction checks out: see items 1–5 under "Computed in memory". The stored verdict, campaign counts, effective denominator and the recomputed folds, median view and pooled modes all match exactly.

## 3. Results and wording

Every number in the memo and the report that I checked matches the JSON:

- **Grade E:** 262 sides, 328 training rows, k 1.08, 0.78/0.80/0.80 coverage, median error 0.67 (e^0.67 ≈ 1.95), 70/11/63/15/15 labels.
- **Rows and verdict:** 301/108/162/17 rows; log losses 0.6476/0.6597/0.6586/0.6651; differences 0.0121/0.0065.
- **Descriptive checks:** Monte Carlo values; 61 of 108 campaigns; 243 of 301 rows; temporal split 0.6530/0.6606.
- **Commanders:** 94 (52/42); Forrest, Beauregard, Jackson, Hood, Wheeler, Taylor, Lee, Grant, Warren, Farragut, McNeil, Hancock, Gillmore, Butler and Sherman as quoted; SD ratios 0.73–0.96; rank intervals 1–19 of 42 and 2–27 of 52; 19 `not_connected`; no `view_sensitive`.
- **Force coefficient:** 0.63 in run 3 against 1.12 in run 2.

The problems are with interpretation, below.

## Required corrections

All five are in `docs/research/commander-ratings-v3.md`.

### R1: The force coefficient's attenuation is stated as a demonstrated mechanism across different row sets (lines 58–60)

**Problem.** The memo says "The pooled force coefficient is 0.63, against 1.12 in run 2. Noisy modelled strengths attenuate it, which leaves more of each result to be attributed to commanders or the prior."

The 1.12 comes from run 2's 126 rows. The 0.63 comes from 301 rows, so this comparison mixes a change of rows with imputation noise. The stored views separate the two effects:

| Fit | Rows | β |
|---|---:|---:|
| `strength_graded_only` (run 2's rows) | 126 | 1.12 |
| `median_imputation` | 301 | 0.86 |
| Multiple imputation, pooled | 301 | 0.63 |
| `wide_imputation` | 301 | 0.43 |

Moving from the grade E medians to draws, then to doubled SD, lowers β on the same rows. That is consistent with attenuation by imputation noise. The drop from 1.12 to 0.86 comes with a change of rows and is not isolated. That more of each result then goes to commanders is a plausible reading, but no view tests it. Stated as fact, it overclaims.

**Replace** lines 58–60 (from "- **The force term weakens.**" through "…not a finding about force size.") with:

> - **The force term weakens.** The pooled force coefficient is 0.63 on the 301 rows, against 1.12 on run 2's 126 rows (reproduced by `strength_graded_only`). On the same 301 rows it is 0.86 with grade E sides at their medians (`median_imputation`) and 0.43 when the imputation SD is doubled (`wide_imputation`), which is consistent with noisy modelled strengths attenuating it; the fall from 1.12 to 0.86 also changes the rows and is not isolated. A weaker force term may leave more of each result to commanders or the prior; no view tests this. This is a limit of the method, not a finding about force size.

### R2: The cross-run comparison of the improvement lacks its caveat (lines 64–66)

**Problem.** "…commander identity again lowers held-out log loss under both weightings, by more than on the 126 well-sourced battles."

The comparison itself is correct: run 2's stored differences are −0.0093 (battle-weighted) and −0.0049 (campaign-weighted), against −0.0121 and −0.0065 here. But the two runs differ in rows, in folds (108 against 66 campaigns) and in the size of the force term (R1). The design's reading rule (§5) allows only "held-out log loss was lower on these rows".

**Replace** lines 64–66 with:

> - **Filling the gaps did not remove the improvement.** On all battles, with the uncertainty of modelled strengths carried through, the commander model again had lower held-out log loss under both weightings (by 0.0121 and 0.0065, against 0.0093 and 0.0049 in run 2). The two runs differ in rows, folds and the size of the force term, so the sizes are not directly comparable, and neither is evidence of skill.

### R3: The Monte Carlo values are described as "the same" (line 38)

**Problem.** The stored values are −0.0122 and −0.0068 for imputations 1–10, against −0.0120 and −0.0062 for 11–20. They are close but not the same.

**Replace** "the difference is the same on imputations 1–10" with "the difference is similar on imputations 1–10".

### R4: Selection is not stated as a limit

**Problem.** Design §8 lists as a limit: "Which battles are well documented still depends on outcome, size and fame; grade E fills the gaps but cannot remove that selection." The memo's Limits carry only the flag name. The owner's decision was about filling gaps, so this limit should be explicit.

The stored `selection_descriptive` counts are:

| Sides | Won | Lost |
|---|---:|---:|
| Grade D | 134 | 128 |
| Graded | 171 | 177 |

**Insert** after line 76 (the "Grade E is a typical size…" bullet):

> - Grade E fills gaps but does not remove selection: which battles and sides are well documented still depends on outcome, size and fame (design §8). Descriptively, grade D sides won 134 and lost 128; graded sides won 171 and lost 177 (`selection_descriptive`).

### R5: `not_connected` is named but not explained (line 56)

**Problem.** The ordered US list places `not_connected` commanders high: Farragut third, Averell seventh. The memo does not say what the label means. Under commander-ratings §4, "Between components, only α, β and the prior" inform the differences, so these places do not come from shared opponents.

**Replace** "19 of the 94 are `not_connected`." with:

> 19 of the 94 are `not_connected`: they share no component with another ranked commander of their side, so their place relative to that side's other commanders rests on α, β and the prior, not on shared opponents (design §4).

## Advisories (not required)

- **A1: Flotilla training count.**
  - Design §2 says `flotilla` has 3 training rows. The output records 2, because one flotilla training side is `joint_command` and is coded `unknown`, as the design's own joint-command rule requires. By ledger echelon there are 3.
  - Both counts merge into `unknown`, so the fit is unaffected. The design is hash-bound, so note this in the memo's Grade E paragraph or a later design version rather than editing it.
- **A2: `applied_bounds` on conflict sides.** For KY005 US and VA022 US (`bound_conflict`), `applied_bounds` lists the conflicting inputs, although `lower_bound` and `upper_bound` are null and nothing was applied. The label makes this clear. A later version could list them separately, for example under `conflicting_bounds`.
- **A3: Report formatting.**
  - `report_text` renders the Monte Carlo keys as "imputations 1 10" and "imputations 11 20" (`k.replace('_', ' ')`).
  - Negative numbers use a hyphen where the memo uses a minus sign.
  - This is cosmetic. Fix it in code before the next regeneration and do not hand-edit the run artifact.
- **A4: Where the improvement occurs, descriptively.** This is my computation from the stored predictions, with row labels from `base_rows`. It is not an artifact field.

  | Rows | n | Commander | Strength only | Difference |
  |---|---:|---:|---:|---:|
  | With a modelled side | 162 | 0.6495 | 0.6581 | −0.0086 |
  | Run 2's graded rows | 126 | 0.6467 | 0.6619 | −0.0153 |
  | Other | 13 | 0.6324 | 0.6576 | −0.0252 |

  The improvement is not concentrated on modelled rows. The θs are still trained on all rows, and the strength-only comparator is itself attenuated, so this does not rule out commander terms absorbing mismeasured force. The memo could add a sentence saying so.
- **A5: `unranked_in_view`.** 34 of the 94 ranked commanders are unranked in at least one robustness view (14 in 1, 5 in 2, 11 in 3, 2 in 4, 2 in 5). The memo's "No commander is `view_sensitive`" could say this alongside.
- **A6: "Leads" and "trail".** With 80% rank intervals like 2–27 of 52, "Grant leads" or "Forrest … lead" reads as a finding. "Is listed first by median rank" matches the report's own caveat better.
- **A7: Test coverage.**
  - `tests/test_imputation.py` does not unit-test:
    - merges;
    - the calibration grid for k;
    - `bound_conflict` and `bound_dominates` handling (including the nearer-bound choice);
    - held-out averaging, or the Monte Carlo slices lining up with imputation order.
  - The refusal test passes the v2 authorization, which fails on its missing keys. It does not test a single mismatched hash.
  - The committed-imputation replay test does cover the whole grade E output.
- **A8: Draws for fixed sides.** In `imputations()`, `rng.random()` is consumed even for a side with a fixed (`bound_dominates`) value. No such side exists in v1, so nothing is affected. A later design should say whether fixed sides consume a draw.
- **A9: Endpoint views.** These use each grade E side's stored `low` and `high`, which are rounded to 10, rather than the unrounded 10th and 90th percentiles. The difference is negligible.
- **A10: Bundle manifest scope.**
  - `inputs.json` does not bind `generalship/imputation.py`, `generalship/ratings_v3.py`, `tests/test_imputation.py`, `artifacts/strength-imputation-v1.json`, `docs/strength-imputation.md`, `docs/commander-ratings.md` or `data/command/rating-authorization-v3.json`, although the assignment directs review of them. I hashed them myself (table above).
  - Future bundles should bind them.
  - The JSON also drops per-imputation held-out probabilities, so the Monte Carlo check cannot be recomputed without refitting.

The memo's status line ("separate review pending", line 7, and line 80) is for the primary to update after reconciling this review.

## Findings

- **Required:** R1, R2, R3, R4, R5.
- **Advisories:** A1–A10.
