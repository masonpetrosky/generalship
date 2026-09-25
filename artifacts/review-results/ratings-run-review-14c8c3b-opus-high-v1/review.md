# Separate review: commander residual ratings, model code and first run (`14c8c3b`)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This was a fresh-context
  subagent. The author's conversation was not an input.
- **Date:** 2026-09-25.
- **Commits:** prepared `14c8c3bfe3ce4e9c9de36a24b7f937ccb36c998f`, previous
  `28072824d7f1801db2a252e5617976d3c67e7eb9`. The bundle commit and worktree HEAD are
  `497eb12a8b6f52d4a69762d0b57e29b62df5722f`. The authorization's `code_commit` is `0bdc480`.
  `git diff 0bdc480 14c8c3b -- generalship tests` is empty, so the run used the authorized code.
- **Assignment:** `assignment.md` sha256 `11e5efe3503e12a1f1af2d7cc761b71dda9a3dbcbad59761f3b2a18292553382`.
- **Input manifest:** `inputs.json` sha256 `b338fd5abf5b46f039987c3b202da58e477d0c3648bb60ea43f658bb47cd64e7`.
- **Hash check:** I checked all 26 bound paths three ways: the manifest value, `git show 14c8c3b:<path>`
  and the worktree file. All 26 matched, with no mismatch.
- **Other files read** (hashes at `14c8c3b`, identical in the worktree):
  - `docs/commander-ratings.md` `0ab4b7d541baf4f8e642634f316628f9cb372d68dcdbbc047a305f5a1fb704bb`;
  - `generalship/baseline.py` `731d9ad96dc85ca8f69bd7689e7ec64d9a1917b1a4b9d45c9c55b37348d42179`;
  - `artifacts/estimate-evaluation.json` `d02fa45ce7b876940393deb104725fc856ffbc11fb8929f564beb43a94a59886`;
  - `data/estimates/side-strength-v1.json` `0656b03c…fde89`, `data/command/responsibility-v1.json`
    `0e3f1443…cdd67e` and `data/command/commanders-v1.json` `2b3bbef5…0706b1`. These match the
    authorization record.

  The assignment requires reading the design and `baseline.py`, but the manifest does not bind
  them. I did not re-review the two ledgers' coding.

## Scope actually inspected

- **Read in full:**
  - `AGENTS.md`;
  - `docs/commander-ratings.md`, all sections, with §§3–8 checked line by line against the code;
  - `data/command/rating-authorization-v1.json`;
  - `generalship/ratings.py` (all 448 lines) and `generalship/baseline.py`;
  - `tests/test_ratings.py`;
  - `artifacts/commander-ratings.md`;
  - `docs/research/commander-ratings-v1.md`;
  - the `2807282..14c8c3b` diffs of `Makefile`, `generalship/cli.py`, `artifacts/receipt.json` and
    `docs/roadmap.md`.
- **Inspected in part:**
  - `artifacts/commander-ratings.json`: the held-out block, the temporal block, the view metadata,
    all per-commander fields of the nine ranked commanders and the outcome-only views for all
    commanders;
  - the ledgers' structure and every side that has candidates, a successor, a superior or grade D;
  - the ledgers' nesting records;
  - `nested_sets` in `generalship/estimates.py`.
- **Commands run:**
  - `make check`, offline: 133 tests passed, and `generalship check` exited 0.
  - I re-ran `rate()` in memory without writing. `json.dumps(...)` of the result is byte-identical
    to `artifacts/commander-ratings.json`, and `report_text` is byte-identical to
    `artifacts/commander-ratings.md`.
  - I ran no `make reproduce`, `make commander-ratings`, build or packet command. `git status` was
    clean after each run.
- **Independent recomputation.** I wrote my own standard-library implementation outside the
  repository, at `/tmp`. It builds the rows directly from the two ledgers and `artifacts/battles.json`.
  It fits the model with a pure Newton method and a Gauss–Jordan inverse, without line search or
  Cholesky. Results:
  - **Rows:** 37 rows in 19 campaigns, with the same IDs as the evaluation's `set3_ABC` rows.
  - **Held-out log loss, battle-weighted:** 0.6635597 for the commander model against 0.6639213
    for strength only.
  - **Held-out log loss, campaign-weighted:** 0.6279897 against 0.6161456.
  - **Verdict:** `improved = False`. The commander model does better in 8 of 19 campaigns, and 21
    rows are effective.
  - **Predictions:** the stored per-row predictions agree within 2e-15 (commander model) and 2e-13
    (strength only).
  - **Consistency with the evaluation:** the strength-only predictions are identical (difference
    0.0) to the `diagnostic_union_score` values in `estimate-evaluation.json` `set3_ABC`, which
    §7 uses for the raw residuals.
  - **Full fit:** α, β and all 52 θ agree within 2e-15. The Laplace SDs agree within 4e-9 (see
    advisory A4).
  - **Temporal split:** 19 training rows and 18 test rows. Log loss is 0.66017 against 0.66963,
    matching the stored values.
  - **Rank intervals:** my own Cholesky, a different seed and a different quantile convention
    reproduce every stored 80% and 95% rank interval and median for the nine ranked commanders.

## 1. Plan fidelity (§§3–7)

**Confirmed as implemented:**

- **Primary rows (§3):** both sides of the strength ledger graded A–C, no `post_start_information`
  label, rounded `point` strengths (`round10`), and oriented with a Union win as 1.
- **Model and priors (§4):** α and β have N(0, 1) priors and τ = 0.5. Each θ enters with its side's
  sign. A grade D side (commander_id `null`: AR006 US, TN002 CS, TN004 US) gets no term but keeps
  its row.
- **Fit (§4):** Newton's method on all parameters with a Cholesky solve and the baseline's
  Newton-decrement stop at 1e-12. The gradient is `prec·w + Σ(p−y)v`, the Hessian is
  `diag(prec) + Σ p(1−p) v vᵀ`, and the line search is Armijo.
- **`use_force=False`:** β is pinned by a precision of 1e12 and x is omitted from the design. β's
  gradient is therefore identically 0 and β stays at 0. The β row and column of the Hessian are
  decoupled, so the θ covariance is unaffected. This is correct.
- **Laplace approximation (§4):** the covariance is the inverse Hessian. The rank-interval draws
  take the Cholesky factor of the ranked commanders' joint sub-covariance, with 1e-12 jitter. They
  use the joint draws for ranks within each side, with rank 1 for the highest θ. There are 20,000
  draws with seed 20260925. The quantiles are `floor(p·n)` order statistics at 0.1/0.9 and
  0.025/0.975.
- **Rank set (§4):** commanders with at least 2 modelled battles in the view's rows.
- **Posterior/prior SD ratio:** reported against τ = 0.5.
- **Connectivity (§4):** union-find over commander–opponent edges on the modelled rows. The
  component ID is its minimum commander ID. `not_connected` is set when no other ranked commander
  of the same side is in the component.
- **Held-out test (§5):** leave-one-campaign-out on the primary rows at τ = 0.5 with the primary
  attribution.
  - The strength-only model is `fit_logistic` with ridge 1, which matches the N(0, 1) priors.
  - An unseen commander gets θ = 0.
  - Improvement requires a strictly lower log loss under both the battle and the campaign
    weighting.
  - The effective rows are those with a commander seen in training, and they are named.
  - Brier and campaign counts are reported outside the verdict.
- **Temporal split (§5):** trained on 1862 and tested on 1863. It is descriptive, with
  `verdict: null`.
- **Views (§6):** each is refitted.
  - τ = 0.25 and τ = 1.0, and α's SD set to 3.
  - Grades A–B only.
  - Superior directing: the ledger sets `superior` exactly on the sides labelled
    `superior_directing`.
  - Command changes (i), excluded (30 rows), and (ii), the successor credited.
  - The four strength endpoints.
  - 15 alternative-candidate refits, one per candidate and per primary-row side with candidates.
    Each changes only that side, and for grade D (AR006 US) both candidates count.
  - Outcome-only (i) on 37 rows. Outcome-only (ii) on 89 rows: 91 less VA033 and VA034, both
    `nested` in VA032. The only `nesting_unresolved` pair (VA033⊃VA034) has both records already
    dropped, so no with/without variant is needed.
  - The labels `includes_force_size_advantage` and `expanded_rows` are applied as designed.
- **`view_sensitive` and `unranked_in_view` (§6):** computed over the robustness views only.
  Outcome-only views are excluded as designed. The opposite-sign test uses the view's 80% interval
  against the primary mode, and the rank test uses disjoint 80% rank intervals.
- **Raw residual (§7):** Σ(outcome − p), oriented to the commander's side, with p from the A–C
  evaluation's held-out `diagnostic_union_score`.
- **Gate (§7):** the run requires the authorization kind, the path and hash of both ledgers and
  the registry, `admits_feature: false` and `changes_baseline: false`, and a `reviewed…` status
  on both ledgers. It replays both checkers. Nothing is written to `baseline.json`.
- **No-signal presentation (§5):** the Markdown gives no ordering: the tables are alphabetical,
  with the required statement. In the JSON, every modelled commander carries `no_heldout_signal`.

**Divergences:** F6 (§3 coverage reasons) and F5 (§6 outcome-only differences). Both are below.

## 2. Numerical correctness

- The fit, the Laplace covariance, the rank draws and the held-out verdict are correct. My
  independent recomputation, described above, matches them to floating-point error.
- `artifacts/commander-ratings.json` and `.md` reproduce byte-for-byte.
- **The headline verdict is confirmed:** there is no improvement. The commander model is 0.00036
  lower under the battle weighting and 0.01184 higher under the campaign weighting.

## 3. Results and wording

I checked every number in `artifacts/commander-ratings.md`, including the table values, the rank
intervals, the labels, the counts and the log losses. All are correct.

In the memo, these are correct: the log-loss table, 8/11 campaigns, 21/37 effective rows, the
temporal 0.660/0.670 on 19/18 rows, the nine θ modes, W–L records and 95% intervals, the SD ratio
range (0.898–0.955, stated as 0.90–0.95), 7 of 9 `not_connected`, 37/52/9, and Lee's 4 of 9 out.
For Lee, the out-of-model battles are VA017 (post-start, Confederate side) and VA021, VA026 and
VA033 (grade D on both sides).

The negative verdict is stated in the words the design requires. The errors and wording problems
are below.

## Required corrections

**F1. Memo rank-interval sentence is wrong for Jackson.**

- **Location:** `docs/research/commander-ratings-v1.md`, lines 68–69.
- **Evidence:** the JSON and the Markdown report give Jackson `rank_80` = [1, 4]. The memo says
  the Confederates are "1–5 or 2–5 of 5". Every 95% rank interval is the full list.
- **Replace:**
  > - **Rank intervals span almost the whole list:** 1–4 of 4 for the Union and 1–5 or 2–5 of 5 for
  >   the Confederates.
- **with:**
  > - **Rank intervals span almost the whole list.** The 80% rank intervals are 1–4 of 4 for every
  >   Union commander. Of the five Confederates, they are 1–5 for Bragg, Ewell and Lee, 2–5 for Morgan
  >   and 1–4 for Jackson. Every 95% rank interval is the whole list (1–4 or 1–5).

**F2. The battle-weighted difference is misstated and characterised without a threshold.**

- **Location:** memo, lines 35–36.
- **Evidence:** the difference is 0.6639213 − 0.6635597 = 0.00036, which is 0.0004 at four
  decimals, not 0.0003. Design §5 sets no threshold, so "negligible" is an unanchored judgment.
  The size of the campaign-weighted gap is not given.
- **Replace:**
  > - The battle-weighted difference is negligible (0.0003), and the campaign-weighted score is
  >   worse.
- **with:**
  > - Under the battle weighting, the commander model's log loss was 0.0004 lower (0.66356 against
  >   0.66392). Under the campaign weighting, it was 0.0118 higher (0.62799 against 0.61615). The
  >   rule required a strictly lower value under both, so this is no improvement.

**F3. The memo overstates that single-campaign commanders "never affect a held-out prediction".**

- **Location:** memo, lines 38–40.
- **Evidence:** design §5 says such a commander's own θ is never used, "though their rows still
  inform α, β and their opponents' θs in other folds". A concrete case is Jackson's five modelled
  battles, which are all in Jackson's Valley Campaign. When the Gettysburg Campaign is held out,
  Jackson's VA102 row trains Milroy's θ. Milroy's θ is then used for the effective row VA107.
- **Replace:**
  > Commanders whose battles all fall in one campaign, such as Jackson in the Valley,
  >   never affect a held-out prediction.
- **with:**
  > A commander whose modelled battles all fall in one campaign, such as Jackson (all five in
  >   Jackson's Valley Campaign), never has his own θ used in a held-out prediction. His rows still
  >   inform α, β and his opponents' θs in other folds. For example, Jackson's VA102 row informs
  >   Milroy's θ, which is used when VA107 (Gettysburg Campaign) is held out.

**F4. The `view_sensitive` bullet understates `unranked_in_view`.**

- **Location:** memo, lines 73–75.
- **Evidence:** in the JSON, three of the nine commanders fell out of the rank set in six
  robustness refits in total, so the rank-overlap test could not run there. The memo's "none
  produced a non-overlapping rank interval" omits this. Design §6 requires the label and the
  view's name.
- **Replace** the bullet beginning "**No commander is `view_sensitive`.**" **with:**
  > - **No commander is `view_sensitive`.** In the robustness views where they were ranked, no
  >   80% interval moved to the other side of zero, and no 80% rank interval failed to overlap the
  >   primary one. Three commanders were `unranked_in_view` in six refits, where their rank could not
  >   be tested:
  >   - Milroy in `command_changed_excluded`, `command_changed_successor` and
  >     `alternative_VA102_US_us-robert-schenck`;
  >   - Bragg in `command_changed_excluded` and `alternative_GA004_Confederate_cs-james-longstreet`;
  >   - Ewell in `superior_directing`.
  >
  >   That reflects how wide the intervals are, not how robust the estimates are.

**F5. The outcome-only views are not reported with their differences (§6), and the memo is silent
about them.**

- **Evidence:**
  - Design §6 says the outcome-only views "are reported beside the primary ratings with their
    differences". The code (`rate`, `views` per commander) stores each view's ratings but no
    differences. The Markdown report and the memo do not mention these views.
  - The JSON shows that Jackson's outcome-only view (ii) 80% interval is +0.0166 to +1.1135. It is
    the only interval of any commander in that view to exclude zero. A reader should see it with
    its caveats.
- **Correction:** insert this bullet in the memo after the F4 bullet:
  > - **Outcome-only views.** These have no force term, are labelled `includes_force_size_advantage`,
  >   estimate a different quantity and do not set `view_sensitive`.
  >   - **View (i), 37 primary rows:** the nine modes move by at most 0.03.
  >   - **View (ii), 89 rows:** these are the 91 engagements less VA033 and VA034, which are dropped
  >     as nested in VA032. The largest moves are Grant (+0.17 to +0.46), Burnside (−0.02 to +0.24)
  >     and Jackson (+0.39 to +0.57). Jackson's 80% interval there (+0.02 to +1.11) is the only
  >     interval of any commander in that view to exclude zero.
  >   - That view credits force concentration and every other advantage the commander did not
  >     create, and it has no held-out test. It is not a finding about Jackson.

  The largest view (i) move is Jackson's +0.034, which is why the bullet says "at most 0.03". The
  advisory A2 code change would make the differences explicit in the JSON.

**F6. The §3 coverage report omits why battles are out of the model and which are dropped as nested.**

- **Evidence:**
  - Design §3 requires, for every commander, "why the others are out (strength grade D, post-start,
    or unattributed), and which are dropped as nested in outcome-only view (ii)".
  - `rate()` gives only `out_of_model` battle IDs. `dropped_as_nested` exists only at view level.
  - **Consequence:** the reasons, such as the memo's hand-written Lee explanation, cannot be traced
    to the artifact. I verified that explanation separately.
- **Correction:** in `generalship/ratings.py`, `rate()`, immediately after
  `in_model = {r['battle_id'] for r in primary}`, insert:
  ```python
      strength_by = {e['battle_id']: {s: e['sides'][s]['estimate'] for s in SIDES} for e in strength['engagements']}

      def out_reasons(b):
          est = strength_by[b]
          reasons = []
          if any(est[s]['grade'] == 'D' for s in SIDES):
              reasons.append('strength_grade_D')
          if any('post_start_information' in est[s]['labels'] for s in SIDES):
              reasons.append('post_start_information')
          return reasons
  ```
  In the `out[c] = {...}` dict, immediately after the `'out_of_model': ...,` line, insert:
  ```python
                    'out_of_model_reasons': {b: out_reasons(b) for b, _, _ in attributed[c] if b not in in_model},
                    'dropped_as_nested_in_outcome_only_91': sorted(b for b, _, _ in attributed[c] if b in dropped),
  ```
- **Checks on the correction:**
  - I checked this logic offline against the stored artifact. Every out-of-model battle of every
    commander gets at least one reason.
  - The reasons for the nine ranked commanders are:
    - Lee: VA017 post-start; VA021, VA026 and VA033 grade D.
    - Grant: MS008 grade D; MS011, TN002 and TN024 post-start.
    - Jackson: VA022 grade D; WV010 grade D and post-start.
    - Burnside: NC003, TN020 and TN023 grade D.
    - Bragg: TN024 post-start.
    - Morgan: TN008 grade D.
  - Battles with an `unattributed` (grade D, `null`) command side are never in any commander's
    `attributed` list, so that reason cannot arise per commander.
  - The change does not alter any fit, verdict or number.
- **Regeneration:** regenerating `artifacts/commander-ratings.json` requires the gated
  `commander-ratings` command. That is for the primary agent to do under the existing
  authorization, which binds the ledgers, not the code.

**F7. The memo and the roadmap assert that the bottleneck is coverage, "not method", and that more
data will make commanders distinguishable.**

- **Evidence:**
  - The run tested only whether commander identity improved held-out log loss. It did not test why
    it did not, or whether more coverage would change that.
  - Design §8 lists non-random assignment, side-relativity and army, theater and opponent
    confounding. More battles would not by themselves remove these, and a larger run can still
    find no signal.
- **Memo correction:** replace lines 84–90 (from "- **These data cannot tell commanders apart.**"
  through "…to be distinguishable.") with:
  > - **In these data, the model does not distinguish commanders.** Likely contributors are the
  >   37 battles, 52 commanders, only nine with two or more modelled battles, and weak connections
  >   through shared opponents. The run does not test which of these limits it, or which of the
  >   design's choices does (τ = 0.5, side-relative θ, the attribution rules).
  > - **More coverage is necessary but may not be sufficient.** A Civil War rating needs at least:
  >   - the other 257 source-listed engagements (1861, 1864–65 and the Trans-Mississippi);
  >   - more of the existing 91 engagements with usable strengths on both sides.
  >
  >   More battles per commander, across campaigns, would narrow the intervals and allow a sharper
  >   held-out test. They would not by themselves show that commanders differ. A positive result
  >   would still not be evidence of skill (design §§5, 8).
- **Roadmap correction:** in `docs/roadmap.md`, lines 33–34, replace
  "The bottleneck is coverage: a meaningful Civil War rating needs the other 257 source-listed
  engagements and more usable strengths." with:
  > More coverage is necessary but may not be sufficient: a Civil War rating needs at least the other
  > 257 source-listed engagements and more usable strengths, and a larger run may still find no
  > signal.

## Advisories (not required)

**A1. Ambiguous no-signal sentence in the Markdown report.**

- "No improvement under both weightings" can be read as "worse under both", but the commander
  model was 0.0004 lower under the battle weighting.
- Suggested change, in `report_text`, the `if not t['improved']` string: begin with "**No
  improvement under the both-weightings rule (lower held-out log loss was required under both;
  it was not lower under the campaign weighting):" followed by the existing text.
- The unit test asserts only "No ordered ranking is given", which still matches.

**A2. Content missing from the Markdown report.**

- The report omits the following, which the JSON or the memo carries:
  - the temporal split (§5, "beside" the test);
  - the names of the effective-row commanders (§5);
  - `unranked_in_view` (§6);
  - the outcome-only views and their differences (§6);
  - the 95% intervals, SD ratio, raw residual, echelon, component and grade mix (§7).
- `Campaigns better` is printed as a Python dict repr.
- Consider adding these, and storing `theta_mode_minus_primary` in each per-commander view entry.

**A3. The report's closing sentence is inaccurate for out-of-model commanders.**

- It says "those outside the model … their ratings are almost entirely the prior", but those
  commanders have no rating.
- Suggested replacement: "Commanders with one modelled battle are in the JSON with their estimate,
  which is almost entirely the prior. Commanders outside the model are listed there with coverage
  only."

**A4. The Laplace covariance is taken at the next-to-last iterate.**

- `fit` returns `chol_inverse(low)` from the Hessian computed before the final Newton step, so the
  SDs differ from the Hessian at the mode by at most 4e-9.
- This has no practical consequence. Recomputing the Hessian at the final `w` would make the code
  match §4 literally.

**A5. The raw-residual input is not bound.**

- `artifacts/estimate-evaluation.json` feeds `raw_residual_sum`, but neither the authorization nor
  this manifest binds it. Its hash is recorded above.
- Consider recording its hash in the run output.

**A6. The memo's sparser-eras claim is untested.**

- The memo says "For sparser eras, the same machinery gives the same honest answer". This is
  untested.
- Design §9 says the approach is "meant to degrade gracefully". Suggested wording: "is designed to
  give the same answer, or wider intervals, …".

**A7. Two required inputs are unbound.**

- `docs/commander-ratings.md` and `generalship/baseline.py` are required reading but not bound in
  `inputs.json`. Their hashes are recorded above.

## Outcome

**Corrections required:** F1, F2, F3, F4, F5, F6 and F7.

The code implements the locked plan, apart from the §3 coverage reasons (F6) and the §6
outcome-only differences (F5). The fit, the Laplace covariance, the rank intervals and the negative
held-out verdict are numerically correct and reproduce. The corrections are to the memo's numbers
and wording, one roadmap sentence, and the coverage fields.

This AI review is a separate analysis. It is not historical adjudication, independent
corroboration, feature admission or authorization of any fit.
