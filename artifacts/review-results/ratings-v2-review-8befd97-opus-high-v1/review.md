# Separate review: commander residual ratings run 2 (cohort v2), code change and results (`8befd97`)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. I ran as a
  fresh-context subagent. The author's conversation was not an input.
- **Date:** 2026-09-25.
- **Commits:** the prepared commit is `8befd972c30fba5c9e2da1c283dd31182a450cd8` and the previous
  commit is `6fe077c`. The bundle commit and worktree HEAD are
  `3e965cb89633f7a8a3fdb42e10e57d3118c56133`. `git diff 8befd97 3e965cb` touches only this bundle's
  `assignment.md` and `inputs.json`. Both authorizations name `code_commit`/`ledger_commit` values;
  the rating authorization names `cef8f3f`. `git diff cef8f3f 8befd97 -- generalship Makefile tests`
  changes only one stdout label in `generalship/cli.py` (the `estimate-evaluate` `outputs` list). No
  artifact depends on it.
- **Assignment:** `assignment.md` sha256 `17a06353cee220c396c667a454d10768014701a356f82f3a08dcc25416c0d4bc`.
- **Input manifest:** `inputs.json` sha256 `7753ee08245c889eed576a696515bdb1f5c19915af5960d5d5d22c2f823579d5`.
- **Hash check:** I checked all 29 bound paths against the manifest value, `git show 8befd97:<path>`
  and the worktree file. All 29 matched, with no mismatch.
- **Required reading that the manifest does not bind** (hashes at HEAD):
  - `docs/commander-ratings.md` `0ab4b7d5…04bb`;
  - `docs/strength-estimates.md` `795212ad…4ba3`;
  - `docs/ledgers-v2.md` `9076d96b…c2ee`;
  - `data/pilot/cohort-v2.json` `614f6c9b…6f9`, which run 2 uses; the manifest binds the v1
    `cohort.json` instead;
  - `docs/research/commander-ratings-v1.md` `5b37d95a…d6e`;
  - the run-1 review `3603b49e…a961`;
  - `generalship/estimates_v2.py` `368c5052…c943a`, `command.py` `58ffe17e…6954`, `baseline.py`
    `731d9ad9…2179` and `estimates.py` `af540a92…a32f`;
  - the three v2 ledgers, which match both authorizations: `7855d4d3…2deed8`, `495cef30…da06ac`
    and `91fc2526…5e3768`;
  - the v1 outputs `commander-ratings.json` `18bfa5f2…4aba` and `estimate-evaluation.json`
    `d02fa45c…9886`.

## Scope actually inspected

- **Read in full:**
  - `AGENTS.md`;
  - `docs/commander-ratings.md`, with §§3–8 checked against the code;
  - `docs/strength-estimates.md` §6;
  - `docs/ledgers-v2.md`;
  - both v2 authorization records;
  - `generalship/ratings.py`;
  - `generalship/estimate_eval.py`;
  - the changed parts of `generalship/dataset.py` and `cli.py`, plus the `Makefile` diff;
  - both v2 Markdown reports;
  - the v2 memo;
  - the verdict section of the run-1 memo;
  - the corrections and advisories sections of the run-1 review.
- **Read in part:**
  - the checkers `estimates_v2.check` and `command.check`, for how they bind the cohort;
  - `baseline.fit_logistic` and `baseline.scores`;
  - `estimates.nested_sets`.
- **JSON inspected by script:** the headline fields, the held-out predictions, the views, the
  per-commander entries and the common rows.
- **Not re-reviewed:** the coding of the v2 ledgers, as the assignment requires. I did no
  research, used no network, spawned no agents and wrote no primary files.
- **`make check`:** run offline. It reported 143 tests OK and exit 0. `git status` was unchanged
  before and after.
- **In-memory reproduction:** I ran `evaluate_estimates(root, v)` and `rate(root, v)` for v = 1
  and 2 at HEAD. I serialised the results as `write_json` does, into a temp directory outside the
  repository. All eight outputs are byte-identical to the committed files:
  - `estimate-evaluation{,-v2}.{json,md}`;
  - `commander-ratings{,-v2}.{json,md}`.
- **Independent recomputation:** I wrote my own code, with no `generalship` imports. It uses
  Gauss–Jordan Newton, not the code's Cholesky routine. It rebuilds the primary rows from the
  ledgers and the raw CSV (126 rows, 66 campaigns), then recomputes:
  - leave-one-campaign-out for both models;
  - the effective denominator;
  - the temporal split;
  - the full fit with Laplace SDs.

## 1. Parameterization

- **Run 2 binds and refuses correctly.**
  - `rate(root, 2)` calls `authorize` first. It requires the authorization's
    `strength_ledger`, `command_ledger` and `registry` paths and hashes to equal the files named in
    `RUNS[2]`. It then replays `check_estimates_v2` and `check_command` on the v2 ledgers, before
    any row is built.
  - In memory, swapping any one of the three v1 files into `RUNS[2]` was refused with
    "Authorization names a different …". Pairing the v1 authorization with the v2 files was also
    refused.
  - `estimate_eval.authorize` refuses a v2 authorization paired with the v1 ledger.
- **The cohort is bound, but only indirectly.** Neither authorization names the cohort hash.
  Both authorized ledgers bind `data/pilot/cohort-v2.json` at `614f6c9b…`, and both checkers
  replay that binding before the run. The run output records the same hash, so the binding holds
  through the ledgers (A2).
- **Run 1 is unchanged.** Every v1 artifact reproduces byte for byte.
- **`build_dataset(root, 'data/pilot/cohort-v2.json')` builds the right frame.** It gives:
  - 384 records in 119 campaigns;
  - outcomes Union 196, Confederate 123 and Inconclusive 65;
  - 55 `baseline_eligible` records.

  All 119 campaigns are complete; I found no campaign with a battle missing from the cohort. The
  v1 call still gives 127 records, 23 of them eligible.
- **Nothing v1-specific remains on the run-2 path, with one exception.** View names, the
  `dropped_as_nested_in_outcome_only_all` key, the years, the evaluation path and the output names
  are all parameterized. The exception is the estimate evaluation's common-row definition and its
  report sentence (R1).

## 2. Plan fidelity for run 2

- **Primary rows.** 126 rows, those where both strength sides are A–C and neither side is
  post-start. This matches the A–C set of `estimate-evaluation-v2.json` exactly: the same 126 IDs.
  Three primary rows have a grade-D US command side (AR006, TN032 and VA083). Each has
  `commander_id` null, so it gets no θ, as §2 requires.
- **Held-out verdict.** Leave-one-campaign-out on the primary rows, with τ = 0.5, primary
  attribution and both weightings. An unseen commander gets θ = 0.
  - The effective denominator counts rows where either side's commander is in the training fit.
    That is §5's "θ estimated from another campaign".
- **§6 views: 71 in all.**
  - 68 robustness views: τ 0.25 and 1.0, `alpha_sd_3`, `grades_ab`, `superior_directing`, the two
    command-change views, the four endpoints, and 57 alternative-candidate refits. My own count of
    candidates other than the primary choice, over primary sides, is also 57.
  - Every side with `superior` set carries `superior_directing`, and every labelled side has a
    superior.
  - 3 outcome-only views:
    - `outcome_only_primary`, 126 rows;
    - `outcome_only_all`, 301 rows, which are the 305 in-scope engagements less GA012, LA009, VA033
      and VA034, dropped as nested under rule 7;
    - `outcome_only_all_without_TN035`, 300 rows. TN035 is the only unresolved contained record
      that is not already dropped; VA033–VA034 is unresolved, but both are dropped as nested.
- **Labels.** `view_sensitive` is computed over the 68 robustness views only. No commander is
  flagged. `unranked_in_view` is set for 15 of the 40 ranked commanders.
- **Raw residuals.** They use the A–C `diagnostic_union_score` from `estimate-evaluation-v2.json`,
  whose ledger hash is `7855d4d3…`. My recomputation of every `raw_residual_sum` matches to within
  2e-16. No out-of-model battle lacks a reason.
- **Connectivity.** The components and `not_connected` labels follow §4. 15 of the 40 ranked
  commanders are `not_connected`.
- **Ordering.** With `improved: true`, the report orders each side by median rank, with ties
  broken by θ mode, and drops "(alphabetical)". The ordering key is never shown (R6).
- **Temporal split.** It trains on 1861–1863 (79 rows) and tests on 1864–1865 (47 rows).
  - It stores `verdict: null` and is labelled "no verdict" in the report.
  - The design fixed only a v1 split, 1862→1863. The v2 years are an author's choice, recorded in
    the `RUNS` comment at `cef8f3f`, which was committed before the run commit `e9b813d`. Commit
    order is the only evidence of when the years were chosen.
  - The choice is reasonable: a calendar break at the start of 1864, both classes in training and
    a 63/37 split. It is not the only defensible choice.
  - The rows are the same as the leave-one-campaign-out rows, so the split is not independent
    evidence.
  - The memo calls it "points the same way" in the verdict list, which reads as support (R5).
- **Estimate evaluation, strength-estimates §6: deviation.** §6 defines common rows as rows with
  "both a frozen baseline row and an estimate row", from "the frozen 23-engagement, 13-group
  baseline".
  - The code uses `baseline_eligible` from whatever cohort it is given. On cohort v2 that gives
    46, 48 and 50 common rows, of which only 18, 20 and 21 are in `artifacts/baseline.json`.
  - The report still says every common row has "a frozen baseline row" (R1).

## 3. Numerical check (independent)

| Quantity | Stored | Mine |
| --- | --- | --- |
| Log loss, battle-weighted, commander / strength | 0.65398077 / 0.66327516 | 0.65398077 / 0.66327516 |
| Log loss, campaign-weighted, commander / strength | 0.67950500 / 0.68437291 | 0.67950500 / 0.68437291 |
| Improved (both weightings) | true | true |
| Campaigns better: commander / strength / tie | 39 / 27 / 0 | 39 / 27 / 0 |
| Effective denominator | 87 of 126 | 87 |
| Temporal split: n, then commander / strength log loss | 79/47, 0.659166 / 0.666646 | same |
| α, β | 0.366525, 1.120763 | same |

- The largest per-row prediction difference is 1.9e-15. The largest θ-mode or SD difference over
  all 166 modelled commanders is 5e-16.
- **Sample θ values and 80% intervals.** Mine match the report at two decimals:
  - Forrest: +0.498, −0.042 to +1.038, SD ratio 0.843;
  - Hood: −0.392, −0.969 to +0.185;
  - Sheridan: +0.200, −0.404 to +0.804;
  - Gillmore: −0.293, −0.901 to +0.315.
- **Rank intervals.** These come from the reproduced run, not from my own draws. The 80% rank
  intervals overlap for every pair on each side:
  - Confederate: the smallest upper bound is 11 (Forrest) and the largest lower bound is 8 (Hood);
  - US: the smallest upper bound is 17 and the largest lower bound is 6.
- **Margins.** 0.0093 battle-weighted and 0.0049 campaign-weighted. **The margins and the
  reported log losses are correct.**

## 4. Results and wording

- **Correct as stated.** I checked every number in both v2 Markdown reports against the JSON, and
  the following memo numbers are correct:
  - the strength table and the Brier comparisons;
  - 17 and 13 post-start rows;
  - the log losses, the margins and 39/27;
  - 87/126 against 21/37 in run 1;
  - 40 ranked commanders (21 US, 19 Confederate);
  - the SD ratios, 0.84 for Forrest and 0.86–0.96 for the rest;
  - no 80% or 95% interval excludes zero, among all 166 modelled commanders;
  - the top and bottom modes and records;
  - the rank-interval ranges;
  - 15 of 40 `not_connected`;
  - Lee 19 attributed and 7 modelled, Grant 11 and 5;
  - 301 rows, with Forrest, Beauregard and Grant above zero in `outcome_only_all`.
- **Errors and wording problems** are the corrections below:
  - "71 views" (R3);
  - the scope of "largest moves" (R4);
  - the verdict reading (R2);
  - the temporal framing (R5).

## Required corrections

**R1. Common rows in the v2 estimate evaluation do not follow strength-estimates §6.**

- **Evidence:** in `artifacts/estimate-evaluation-v2.json`, the set3 common rows number 50, of
  which 21 are in `artifacts/baseline.json` (set1 18/46, set2 20/48). §6 limits common rows to
  frozen baseline rows. The report sentence at `generalship/estimate_eval.py:264` is therefore
  false for run 2.
- **Change:** in `generalship/estimate_eval.py`, `evaluate_estimates`, insert after
  `records, _ = build_dataset(root, run['cohort'])`:
  ```python
      if version != 1:  # strength design §6: common rows are rows of the frozen 23-engagement baseline
          frozen_ids = {r['battle_id'] for r in build_dataset(root)[0] if r['baseline_eligible']}
          records = [{**r, 'baseline_eligible': r['baseline_eligible'] and r['battle_id'] in frozen_ids}
                     for r in records]
  ```
  Then regenerate with `make commander-ratings-v2`.
- **Checked in memory.** I patched only this step and wrote nothing. The result:
  - The A, AB and ABC primary predictions, the metrics and every sensitivity refit are unchanged.
  - Common rows become 18, 20 and 21, identical by construction for 16, 18 and 18. Their Brier
    scores equal run 1's exactly.
  - New rows become 43, 60 and 105. Their strength-model Brier scores are 0.2496/0.2480,
    0.2530/0.2683 and 0.2327/0.2416.
  - The ratings would change only in `raw_residual_input.sha256`.
- **Alternative, if the author prefers to keep the 50-row comparison:** record it as a documented
  deviation. Replace the report sentence for run 2 with: "Common rows are rows of this cohort that
  pass the frozen baseline's eligibility rule and have an estimate row; only 18/20/21 of them are
  rows of the frozen 23-engagement baseline (strength design §6 deviation)."

**R2. The memo reads the positive verdict more strongly than §5 allows.**

- **Evidence:** §5 says an improvement "is read only as 'held-out log loss was lower on these
  rows'".
- **Change 1:** in `docs/research/commander-ratings-v2.md`, lines 50–52, replace
  > By the design's rule, commander identity adds a held-out predictive signal on these rows, so the Markdown report orders commanders by median rank.

  with
  > By the design's rule this is an improvement, read only as: held-out log loss was lower on these rows. The Markdown report therefore orders commanders by median rank.
- **Change 2:** at lines 91–93, replace
  > **More coverage changed the answer.** On the 1862–63 pilot (37 rows) commander identity added no held-out signal; on the full war (126 rows, 87 with a commander seen elsewhere) it adds a small one under both weightings. The test was fixed before either run.

  with
  > **The verdict changed with the wider frame.** On the 1862–63 pilot (37 rows) the commander model's held-out log loss was not lower under both weightings; on the full war (126 rows, 87 with a commander seen elsewhere) it was lower under both, by 0.0093 and 0.0049. The rows, campaigns and years all differ between the runs, so this does not show which change moved it. The rule was fixed before either run.

**R3. `view_sensitive` count.**

- **Evidence:** §6 and the code compute `view_sensitive` over robustness views only. There are 68;
  the 3 outcome-only views do not set it.
- **Change:** at line 79, replace "across the 71 views" with "across the 68 robustness views (the
  three outcome-only views do not set it, design §6)".

**R4. Outcome-only scope qualifiers.**

- **Evidence:** among all modelled commanders, James H. Wilson moves −0.34, more than Sherman's
  −0.30. Grant and Sherman are the largest moves only among the 40 ranked commanders. The frame
  has 317 decisive, non-aggregate engagements, and 305 are in scope. There is also an
  `outcome_only_all_without_TN035` view.
- **Change:** at lines 84–85, replace
  > On all 301 decisive rows (GA012, LA009, VA033 and VA034 dropped as nested), the largest moves are Grant (+0.40) and Sherman (−0.30);

  with
  > On the 301 in-scope decisive rows (the 305 two-sided engagements less GA012, LA009, VA033 and VA034, dropped as nested; a further view also drops TN035, whose nesting is unresolved), the largest moves among the 40 ranked commanders are Grant (+0.40) and Sherman (−0.30) (among all modelled commanders, James H. Wilson moves −0.34);

**R5. The temporal split is framed as support, and its years look pre-set.**

- **Change:** at lines 56–57, replace
  > The descriptive split (trained on 1861–1863, tested on 1864–1865; no verdict) points the same way: 0.6592 against 0.6666 on 47 test rows.

  with
  > The descriptive split carries no verdict and does not support the verdict (design §5). Its years, trained on 1861–1863 (79 rows) and tested on 1864–1865 (47 rows), are an author's run-2 choice, set in the code at `cef8f3f` before the run commit; the design fixed only the v1 1862→1863 split. There the commander model's log loss was 0.6592 against 0.6666 on the same rows as the held-out test.

**R6. The ordering key is not stated in the Markdown report.**

- **Evidence:** `report_text` sorts by `rank_median`, which the table does not show. Nothing in the
  report tells a reader how the list is ordered or cautions against reading it as a ranking.
- **Change:** in `generalship/ratings.py`, `report_text`, `else` branch (lines 482–483), replace
  the `lines += [...]` with:
  ```python
          lines += ['Held-out log loss was lower under both weightings on these rows. This is not evidence of a persistent '
                    'commander effect or of skill (design §5).', '',
                    'Within each side, commanders are listed by median within-side rank over the rank draws (ties by θ mode). '
                    'The order is a point summary under the design, not a finding that one commander did better than '
                    'another; read it with the 80% rank intervals.', '']
  ```
  This leaves v1 output unchanged (`improved` is false there). Then regenerate
  `commander-ratings-v2.md`.

## Advisories (not required)

- **A1.** The v2 evaluation report's "Frozen baseline reference (23 rows, 13 campaigns)" could
  add "cohort v1; not these rows", so that 0.2769 is not compared directly with the v2 set
  scores.
- **A2.** Two cross-checks in `rate()` would make implicit bindings explicit:
  - check that `evaluation['ledger']['sha256']` equals the run's strength-ledger hash (they match
    now: `7855d4d3…`);
  - check that `run['cohort']` equals both ledgers' `bindings.cohort.path`.

  Consider naming the cohort hash in future authorizations.
- **A3.** No unit test exercises `RUNS[2]` or the `build_dataset` branch that selects by battle
  ID. The refusal and frame checks above were run by hand, in memory only.
- **A4.** The comment in `dataset.py` that later frames are "complete by construction" is asserted
  but not checked by the code. It is true for cohort v2.
- **A5.** The memo's "overlap almost completely" understates the overlap. On each side, every
  pair's 80% rank intervals overlap.
- **A6.** The memo could note that the 39/27 campaign counts are not part of the verdict (§5).
- **A7.** "The code is at `cef8f3f`": the only later code change is a stdout label in `cli.py`.
  The outputs reproduce at `8befd97`.
- **A8.** The design still describes its scope in v1 terms, for example §1 Scope and §8 Truncated
  careers. A short note on run 2's full-war frame, perhaps in `docs/ledgers-v2.md`, would avoid
  confusion. §8's other limits still apply: selection, non-blind attribution, mixed echelons and
  that the rating is not causal.

## Outcome

**Corrections required: R1, R2, R3, R4, R5 and R6.**

- **Correct and reproducible:** the parameterization, the refusal gates, the v1 reproduction and
  the v2 numbers. The positive held-out verdict is numerically correct, and I recomputed it
  independently.
- **What the corrections fix:**
  - one plan deviation in the estimate evaluation's common rows, which does not affect the
    ratings or the verdict (R1);
  - wording in the memo that reads the small improvement more strongly than design §5 allows
    (R2–R5);
  - the report's undisclosed ordering key (R6).

This AI review is a separate analysis. It is not historical adjudication, independent
corroboration, feature admission or authorization of any fit.
