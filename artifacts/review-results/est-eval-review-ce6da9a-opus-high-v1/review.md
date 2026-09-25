# Separate review: estimate-layer evaluation at `ce6da9a`

**Outcome: corrections required** (R1–R5; advisories A1–A9).

## Reviewer record

| Field | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`, fresh-context subagent |
| Date | 2026-09-25 |
| Worktree / bundle commit | `26584abfe5c723b9e79b8b7e71c0ab1c8c829d1c` |
| Prepared commit reviewed | `ce6da9a7a562778dd3ae81c82e3233809676ba65` |
| Previous commit | `4ba48a12b51a1a654710777c4ac475fde1ada938` |
| `assignment.md` SHA-256 | `e4b543a719be14a6ecb077ceb181692245d290fad8309afa786ef4b3e23d49be` (verified) |
| `inputs.json` SHA-256 | `1b57c62ea36ad94a02d04d83b9c196c597ccebb7f240538081f03bb901006441` (verified) |
| Input hashes | All 27 paths in `inputs.json` match both `git show ce6da9a:<path>` and the worktree files. No mismatch. |

This is a separate AI analysis. It is not historical adjudication, not feature admission and
not authorization of any fit.

## Scope actually inspected

- **Read in full:** `AGENTS.md`, `docs/strength-estimates.md` (all sections, §6 closely),
  `generalship/estimate_eval.py`, `generalship/baseline.py`, `tests/test_estimate_eval.py`,
  `docs/research/estimate-evaluation-v1.md`, `data/estimates/evaluation-authorization-v1.json`
  and `artifacts/estimate-evaluation.md`.
- **Read in part:** `generalship/estimates.py` lines 85–262 (§4 rules, `estimate_side`,
  `estimate_row`, `nested_sets`; not the checker). `docs/research/strength-estimates-ledger-v1.md`
  lines 1–200 (the summary, the extraction record and the first part of the per-engagement
  table). I read `artifacts/estimate-evaluation.json` through scripts, not line by line.
- **Diffs `4ba48a1..ce6da9a`:** `baseline.py`, `cli.py`, `Makefile`, `README.md`,
  `docs/roadmap.md`, `artifacts/receipt.json`.
- **Not re-reviewed:** the ledger's per-engagement coding (reviewed separately), `dataset.py`
  and the other inputs listed in `inputs.json` beyond their hashes.

**Computations (offline, in memory; no artifact was written):**

1. `make check`: exit 0; 120 tests OK; the CLI checks passed.
2. `evaluate(build_dataset(root))` serialized like `write_json` is **byte-identical** to the
   committed `artifacts/baseline.json`.
3. `evaluate_estimates(root)` is byte-identical to the committed
   `artifacts/estimate-evaluation.json`. Its `report_text` output is identical to
   `artifacts/estimate-evaluation.md`.
4. **Old and new optimizers compared.** I loaded `fit_logistic` from `git show
   4ba48a1:generalship/baseline.py` and ran it beside every one of the 570 `fit_logistic`
   calls in a full `evaluate_estimates` run.
   - The old code raised "did not converge" on 34 calls.
   - On the other 536 calls, the parameters differ by at most 5.1e-10; 488 are exactly equal.
   - On all 13 frozen-baseline folds, old and new give bit-identical intercepts and slopes.
5. **Regression fold.** On the fold in `tests/test_estimate_eval.py`, the old code raises. A
   trace shows the gradient stuck near 4e-9 to 1e-8, just above the 1e-9 tolerance, with
   `g·d` ≈ 2.7e-17 and Armijo accepting erratic small steps until iteration 100. The new
   result has gradient ≈ (4e-16, 1e-16). An independent 200,000-step gradient descent reaches
   the same point within 3.3e-16.
6. **Recomputed from the JSON predictions:**
   - A–C primary-fit Brier: 0.2932 on the 21 common rows and 0.1603 on the 16 new rows.
   - Largest difference between the estimate and frozen-refit `diagnostic_union_score` on
     common rows: 0.0049 (A), 0.0052 (A–B) and 0.0072 (A–C).
   - Common rows that are not identical by construction: MS001, TN003 and VA032 at A–C.
   - New rows at A–C: 14 of 16 are Union wins.
   - Grades of the rows with a `post_start_information` side (derived from the ledger).
   - Post-start exclusions in the rule 4, basis-order and median variants (each 0/0/6, as in
     the primary).

## 1. Plan fidelity (design §6)

The implementation matches §6 in every modelling respect:

- **Model.** `point_feature` uses `advantage(US point, CS point)` with the stored rounded
  points, and `fit_logistic` keeps its default ridge of 1.0.
- **Validation.** `loco` leaves out one campaign at a time, over the campaigns present in the
  rows passed to it.
- **Comparators.** Equal odds is 0.5. The prior is Laplace-smoothed from the training rows only.
- **Leakage.** `assemble` drops every row with a `post_start_information` side before any fit.
- **Row sets.** The three nested sets come from `nested_sets`.
- **Evaluability.** `evaluable` requires at least 6 rows, 3 campaigns and both outcomes.
- **Sensitivity refits:**
  - The four endpoint combinations are true refits: the training and held-out features both
    use the endpoints.
  - The four labels are excluded one at a time.
  - The rule 4 factor of 1, `ALT_BASIS_ORDER` (it equals the §6 order) and `upper_median` are
    true re-estimations through `estimate_side` and `estimate_row`, followed by a new
    `assemble`.
- **Common rows.** `common_comparison` fits both models inside the same leave-one-campaign-out
  folds, on the `baseline_eligible` rows of the set only. Identity by construction is tested
  on the exact, unrounded points against the frozen midpoints.
- **Newly covered rows.** They are scored from the primary fit against equal odds and the
  prior only.
- **Frozen reference.** The constants equal `artifacts/baseline.json`.
- **Naming.** Predictions are called `diagnostic_union_score` throughout.

One divergence from the §6 reporting list, and one mislabelled count:

- **Sensitivity results omit label counts and post-start counts (R5).** `summary()`
  (`estimate_eval.py` lines 167–172) drops `label_counts_sides` and `flags`, and no variant
  records its post-start count. §6 says "Each result gives … every §5 label count; the number
  of rows excluded as `post_start_information`."
  - I checked that the re-estimated variants exclude the same rows as the primary (set3: 6).
    The endpoint and label variants use subsets of the primary rows. The metrics are
    therefore unaffected; only the report is incomplete.
- **The "excluded" count is mislabelled (R1).** `rows_excluded_post_start_information` and the
  report's "Rows excluded as `post_start_information`: 7" count WV010. Its Confederate side is
  grade D, so it enters no row set anyway. Only 6 rows are excluded from any fit: the per-set
  lists give set1 0, set2 0 and set3 6. The ledger memo already states this correctly ("7 (6
  with both sides estimated, plus WV010 …)").

## 2. Gate

**What `authorize()` does** (`estimate_eval.py` lines 175–184):

- It refuses the fit unless the record's `kind` and `ledger_path` match.
- It refuses unless `ledger_sha256` equals the SHA-256 of the current ledger file.
- It refuses unless `option` is `a_exploratory_estimate_layer_diagnostic`.
- `evaluate_estimates` then replays the ledger with `check()` before any fit.
- The unit tests cover the hash mismatch and the rejection of option (b). This is an adequate
  mechanical gate.

**What the gate and the record do not establish:**

- **The owner's words are relayed.** The record holds the agent's transcription of a chat
  reply (`recorded_by`). Nothing in the repository can verify it.
- **The owner did not choose an option.** The question put to the owner named the ledger path
  and hash, and the reply ("go ahead and run") explicitly authorizes running that ledger. But
  the question never put option (a) against option (b), and it did not say "exploratory" or
  "outside the admission contract". The record's `option` and `option_text` are therefore the
  recording agent's reading.
  - That reading is reasonable: no option (b) admission profile exists, so a run could only
    be (a).
  - But the memo and the roadmap present option (a) as the owner's explicit choice. §6 says the
    authorization "must" take one of the options, so this should be visible (R4).
- **The review precondition is not checked by code.** The §6 requirement that the ledger's
  review be reconciled appears only in the documents (ledger memo "Status: reviewed and
  reconciled").
- **The output does not bind the authorization record.** It gives the record's path, date and
  option, not its SHA-256. `artifacts/receipt.json` does bind it (A5).

## 3. Optimizer change

**Soundness.** The objective has a ridge penalty, so its Hessian H ≽ ridge·I = I. Then
`g·d = gᵀH⁻¹g = λ²`, the squared Newton decrement, which is ≥ 0 and is 0 only when g = 0.

- λ² < 1e-12 implies |g| ≤ √(λ_max(H)·1e-12). With |x| ≤ 1, λ_max(H) ≤ 1 + n/2, so |g| is a few
  1e-6 at these row counts.
- A full Newton step from there lands within O(|d|²) of the unique minimizer.

**The minimizer is unchanged.** The objective, ridge and feature are unchanged; only the
stopping point moves.

- Empirically, the stopping point moves by at most 5.1e-10 where the old code converged.
- The frozen baseline is safe: all 13 baseline folds are bit-identical, and `baseline.json`
  reproduces byte for byte.

**The regression test is meaningful.** The old code raises on its exact input. Its asserted
literals match an independent gradient-descent optimum within 3.3e-16. But the literals came
from the new code itself, so a gradient-norm assertion would make the test self-standing (A9).

## 4. Results and wording

**Numbers checked.** Every number in the memo's table and prose, the README and the roadmap
matches the JSON:

- Brier scores, row and campaign counts, and the frozen reference.
- Log loss at A–C: 0.664, 0.693 and 0.693.
- Common rows 21, with 18 identical; 0.2947 against 0.2941.
- New rows 16: 0.1603, 0.1662 and 0.2500.
- Sensitivity range 0.212–0.263; endpoints 0.227–0.244; 0.263 on 27 rows and 0.256 on 30
  rows; NE on 1 and 5 rows.
- README 0.279 and 0.236; roadmap 21 and 37 rows.

The exception is the count of excluded rows (R1).

**Wording.** Two sentences understate a weakness or overstate agreement (R2, R3), and the
authorization option is misattributed (R4). Nothing claims commander effects, win
probabilities or accuracy of the estimates. The claim that no difference "is significant" has
no test behind it (A1).

## Required corrections

**R1: excluded-row count.** Seven rows carry a post-start side, but only six are excluded from
a fit.

- `docs/research/estimate-evaluation-v1.md` line 64. Replace
  > Seven rows are excluded as post-start: MS003, MS011, NC007, TN002, TN024, VA017 and WV010.

  with
  > Seven rows carry a `post_start_information` side: MS003, MS011, NC007, TN002, TN024, VA017 and WV010. Six of them would otherwise be A–C rows and are excluded from its fits (none from the A or A–B sets). WV010 enters no row set in any case, because its Confederate side is grade D.

- `generalship/estimate_eval.py` lines 231–232 (`report_text`). Replace
  ```python
  f"Rows excluded as `post_start_information`: {len(result['rows_excluded_post_start_information'])} "
  f"({', '.join(result['rows_excluded_post_start_information'])}).", '',
  ```
  with
  ```python
  f"Rows with a `post_start_information` side: {len(result['rows_excluded_post_start_information'])} "
  f"({', '.join(result['rows_excluded_post_start_information'])}); excluded from fits: "
  + ', '.join(f"{k} {len(v['excluded_post_start_information'])}" for k, v in result['row_sets'].items()) + '.', '',
  ```
  Then regenerate `artifacts/estimate-evaluation.md` under the existing authorization. The
  ledger hash is unchanged, so the gate still passes. The JSON key can stay; its members are
  correct as a list of labelled rows.

**R2: the source of the A–C gain.** Within the A–C fit, all of the battle-weighted gain over
equal odds comes from the new rows; the memo says "most". Recomputed from the JSON: 21 common
rows at 0.2932 and 16 new rows at 0.1603, against 0.2500. Memo lines 88–89. Replace
> Most of the gain is in newly covered rows, where the prior does almost as well.

with
> All of the battle-weighted gain over equal odds comes from the 16 newly covered rows (0.1603). On the 21 common rows, the same A–C fit scores 0.2932, worse than equal odds. On the new rows the prior does almost as well (0.1662), because 14 of the 16 are Union wins.

**R3: "the same predictions".** The predictions are not identical. Three common rows at A–C are
not identical by construction (MS001, TN003, VA032). The largest score difference is 0.0072,
and the Brier scores are 0.2947 against 0.2941. Memo lines 90–91. Replace
> On common rows the estimates and the frozen figures give the same predictions, as expected, since most are the same figures.

with
> On common rows the estimates and the frozen figures give nearly the same predictions (largest difference 0.007 at A–C; Brier 0.2947 against 0.2941), as expected: 18 of the 21 rows are the same figures before rounding.

**R4: option (a) is attributed to the owner.** The owner's reply authorizes the run and does not
choose between (a) and (b).

- Memo lines 14–15. Replace
  > It takes design §6 option (a): an exploratory diagnostic outside the admission contract.

  with
  > The question did not put design §6 options (a) and (b) to the owner. The record applies option (a), an exploratory diagnostic outside the admission contract, because no option (b) admission profile exists; that choice is the recording agent's reading of the reply, not the owner's words.

- `docs/roadmap.md` lines 18–19 (one sentence split across the line break). Replace
  > The owner authorized the locked evaluation (design §6, option (a)) for that ledger hash on 2026-09-25;

  with
  > The owner authorized running the locked evaluation (design §6) for that ledger hash on 2026-09-25; the authorization record applies option (a), the only option available without an admission profile;

**R5: sensitivity reporting.** Sensitivity results must carry the §5 label counts and the
post-start counts. In `generalship/estimate_eval.py`:

- Line 168. Replace
  ```python
  keep = ('evaluable', 'rows', 'campaigns', 'union_wins', 'grade_mix_sides', 'metrics')
  ```
  with
  ```python
  keep = ('evaluable', 'rows', 'campaigns', 'union_wins', 'grade_mix_sides', 'label_counts_sides', 'flags', 'metrics')
  ```
- In `sensitivity`, line 151. Keep the primary exclusions:
  ```python
  base_rows, base_excluded, _ = assemble(variant_estimates(ledger), records)
  ```
  Add `'excluded_post_start_information': len(base_excluded[k])` to each endpoint and label
  variant entry.
- Lines 162–163. Record each re-estimated variant's own exclusions:
  ```python
  rows, excluded, _ = assemble(variant_estimates(ledger, **params), records)
  out[name] = {k: {**summary(fit_set(rows[k])), 'excluded_post_start_information': len(excluded[k])} for k in SETS}
  ```
- Then regenerate both outputs.

The metrics will not change: I verified that the exclusions are 0/0/6 in every variant.

## Advisories

- **A1: significance.** No significance test was run. Memo line 92 and the limitation string at
  `estimate_eval.py` line 214 assert "no difference is significant". Suggested memo wording: "No
  significance test was run; at 21–37 rows none of these differences is presented as
  significant (design §6)."
- **A2: optimizer note.** The memo's "predicted decrease (about 1e-15)" does not match the
  regression fold, where `g·d` ≈ 2.7e-17. Also, `g·d` is the squared Newton decrement λ², and the
  quadratic model's predicted decrease is λ²/2. Suggested wording: "the squared Newton decrement
  `g·d` (2.7e-17 on the regression fold)". The old code failed on 34 of 570 fits.
- **A3: README summary.** "Army size alone predicts outcomes weakly" sits beside a grade-A result
  that is worse than equal odds. The sentence also pairs the battle-weighted 0.236 with a
  campaign-weighted clause about the prior; battle-weighted, the model beats the prior (0.2357
  against 0.2456). Consider: "army size alone is a weak predictor: worse than equal odds on
  grade-A rows (Brier 0.279 against 0.25); on A–C rows 0.236 battle-weighted, but no better
  than the training prior campaign-weighted (0.213 against 0.211)."
- **A4: log loss.** "Log loss follows the same pattern" does not hold in one cell. At A–C the
  campaign-weighted log loss is 0.616 for the strength model and 0.617 for the prior, while the
  campaign-weighted Brier favours the prior. The memo could state that the model and the prior
  are tied on campaign-weighted log loss.
- **A5: gate outputs.** Add the authorization record's SHA-256 to the JSON `authorization`
  block. Optionally, have the gate require `admits_feature` and `changes_baseline` to be false.
- **A6: frozen reference.** `FROZEN_REFERENCE` is hard-coded. A test comparing it with
  `artifacts/baseline.json` would catch drift.
- **A7: owner confirmation.** If the owner wants §6's "must" read strictly, a short explicit
  confirmation of option (a) could be recorded in a versioned `evaluation-authorization-v2.json`.
  This review does not require it.
- **A8: other results.** The common-row and newly-covered results carry no grade mix, label
  counts or flags. §6 arguably covers them under "each result".
- **A9: regression test.** Also assert that the gradient norm at the returned point is below
  1e-9, so the test does not rest only on literals produced by the new code.

## Finding IDs

Required: R1, R2, R3, R4, R5. Advisory: A1, A2, A3, A4, A5, A6, A7, A8, A9.
