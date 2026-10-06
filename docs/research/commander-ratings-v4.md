# Commander residual ratings v4: context comparator, estimated τ and leakage handling

Run on 2026-10-06 under the pre-registered [run-4 design](../commander-ratings-v4.md). This is an
exploratory diagnostic, not a ranking of record, a measure of skill or a causal estimate. The
baseline is unchanged.

**Status: primary-verified.** No separate review was run, under the owner's policy of 2026-10-06.

## Authorization and pre-registration

- **The owner's approval.** The owner approved the plan: "Sounds good, go ahead and fix all 8"
  ([record](../../data/command/rating-authorization-v4.json)).
- **What the record binds:**
  - the design;
  - the grade E output;
  - the v3 strength ledger;
  - the v2 command ledger and registry;
  - the CWSAC battle and campaign tables;
  - all 17 package modules the run imports.
- **Pre-registration.** The design, code and authorization were committed and pushed in `570395c`
  before the run computed any held-out result. Before that, the code was tested on synthetic data
  and smoke-tested with shuffled outcomes.
- **Bindings.** The run's own record of its bindings matches the authorization exactly.
- **The run.** `make commander-ratings-v4` writes `artifacts/commander-ratings-v4.{json,md}`. It took
  28 minutes on 15 processes, under Python 3.14.7 (CPython, macOS).
  - In that environment the floating-point results reproduce bit for bit.
  - On other platforms and Python versions the last bits can differ.

## Rows

- **Battles.** There are 301 battles in 108 campaigns.
  - 120 have a modelled (grade E) side.
- **Post-start sides.** 17 rows had a post-start side in the ledger.
  - In 15 of them that side is now modelled.
  - In the other 2 it keeps a pre-start estimate: VA111 US at grade A, WV010 US at grade C.
- **Joint-command sides.** 18 rows have a joint-command side, which gets no commander term.
- **Effective denominator.** 236 of 301 held-out rows had a commander seen in another campaign.

## The verdict: no improvement under the pre-registered rule

The pre-registered comparison is the commander model (context terms, with τ estimated in each
training fold) minus the context model. Its held-out log loss, by weighting:

| Weighting | Difference | 95th percentile (the rule) | 95% interval |
| --- | ---: | ---: | ---: |
| Battle-weighted | −0.0174 | −0.0054 | −0.0320 to −0.0030 |
| Campaign-weighted | −0.0086 | +0.0092 | −0.0289 to +0.0130 |

- **The rule.** It requires the campaign bootstrap's 95th percentile to be below zero under both
  weightings. Under the battle weighting it is. Under the campaign weighting it is not: 21% of the
  resamples favour the context model.
- **The verdict is therefore no improvement.** The report gives no ordered ranking, and every
  estimate is labelled `no_heldout_signal`. The report's wording, "no detectable predictive signal",
  is the design's: "detectable" means detectable under the both-weightings rule. The battle-weighted
  difference alone clears its bound.
- **Run 3's rule.** Both point differences are below zero. Under run 3's rule (point estimates only),
  this would have been reported as an improvement (`point_lower_both`).

## Where the difference comes from (descriptive)

All rows below are held-out log-loss differences, with campaign-bootstrap 95% intervals.

| Comparison | Battle-weighted | Campaign-weighted |
| --- | ---: | ---: |
| Run 3 as recorded: commander − strength only (v2 ledger) | −0.0121 (−0.0241 to −0.0005) | −0.0065 (−0.0226 to +0.0102) |
| Bridge: run 3's configuration on the v3 ledger | −0.0134 (−0.0252 to −0.0017) | −0.0073 (−0.0233 to +0.0096) |
| Run 4's rows, leakage handled, no context (τ = 0.5) − strength only | −0.0118 (−0.0232 to −0.0005) | −0.0049 (−0.0203 to +0.0114) |
| Context only − strength only | +0.0111 (−0.0082 to +0.0325) | +0.0093 (−0.0127 to +0.0312) |
| Commander + context (τ-hat) − strength only | −0.0063 (−0.0272 to +0.0161) | +0.0007 (−0.0245 to +0.0263) |
| **The verdict:** commander + context (τ-hat) − context | −0.0174 (−0.0320 to −0.0030) | −0.0086 (−0.0289 to +0.0130) |

1. **Ledger v3 left run 3's result about where it was.** The bridge reproduces run 3's
   configuration on the new ledger and gives slightly larger gains.
2. **Leakage handling reduced the gain a little.** The reduction is mostly campaign-weighted: from
   −0.0073 to −0.0049.
3. **The context comparator was weaker than intended.** Its held-out log loss was higher than force
   size alone, by 0.0111 and 0.0093.
   - Out of sample, the 19 theater, period and theater-by-period terms (prior SD 0.5) added noise
     rather than signal.
   - Beating the context model is therefore a lower bar than beating strength only. With context
     terms in both, the commander model does not beat strength only (−0.0063 and +0.0007).
   - This was not known before the run. Any change to the comparator, such as a tighter context
     prior, would have to be fixed before the next run's data are seen. It cannot rescue this run.
4. **The best held-out model** was the commander model without context terms. It was still not
   better than force size alone beyond campaign-resampling noise under the campaign weighting.
5. **Campaigns.** The commander model did better in 65 of 108 campaigns (exact sign test p = 0.043).
   - The battle-weighted gain survives resampling, but the campaign-weighted one does not. The gain
     therefore sits in campaigns with several battles.
6. **Concentration (stored predictions, no refit).**
   - Forrest's 12 rows carry 46% of the net gain.
   - Beauregard's 7 rows carry 19% and Grant's 10 rows 15%. A row counts for both of its commanders,
     so shares overlap.
   - Without Forrest's rows, the verdict difference is −0.0098 battle-weighted and −0.0054
     campaign-weighted. The battle-weighted 95th percentile is then −0.0004, only just below zero.
7. **Leakage rows (no refit).** Without the 34 rows that had a post-start side in the ledger or a
   joint-command side, the difference is −0.0159 and −0.0055. The campaign-weighted 95th percentile
   is +0.0143.
8. **Monte Carlo check.** Imputations 1–10 give −0.0179 and −0.0090; imputations 11–20 give −0.0168
   and −0.0082.
9. **Temporal split** (1861–1863 → 1864–1865, no verdict). The battle-weighted log losses are:

   | Model | Log loss |
   | --- | ---: |
   | Commander + context | 0.6321 |
   | Context only | 0.6457 |
   | Strength only | 0.6505 |

## Do commanders differ? (τ, descriptive)

**All rows.** The Laplace marginal likelihood peaks at **τ = 0.6**, with an approximate 95% profile
interval of 0.2 to 1.0. That interval excludes zero.

**Calibration.**

- Outcomes were simulated 100 times from the context model, a world with no commander differences.
- The largest evidence gain over the grid had median 0.00 and 95th percentile 0.89.
- 55 of the simulations put τ-hat at zero.
- The observed gain on the same imputations is 2.51, larger than in all 100 simulations
  (p = 0.010).

**Within folds and splits.**

- In the held-out folds, τ-hat was 0.6 in 106 of 108 and 0.5 in 2.
- On the 1861–1863 training years alone, τ-hat is again 0.6, but the interval (0 to 1.25) includes
  zero.

**Reading.** In sample, results differ by credited commander more than force size and the coarse
context explain, and more than chance would produce under the context model. This is consistent
with commander effects. It is equally consistent with army, subordinate, opponent or theater
effects that commander identity carries and four theaters and three periods do not. It did not
become a held-out improvement under both weightings.

## What the estimates look like (no ordered ranking)

**Who is rated.**

- 91 commanders have two or more modelled battles: 49 US and 42 Confederate.
- 11 others appear only for coverage:
  - 8 are credited only on joint-command sides;
  - 3 are credited only on nested records: Sedgwick, Augur and Powers.

**Estimates.** At τ = 0.6:

- Two 80% intervals exclude zero:
  - Forrest, +0.96 (12 battles, 9–3; 80% interval +0.38 to +1.54);
  - Beauregard, +0.64 (7 battles, 6–1; +0.01 to +1.27).
- Forrest's 95% interval also excludes zero.
- No other interval excludes zero.
- Posterior SDs are 0.69 to 0.95 of the prior's.

**Labels.**

- No commander is `view_sensitive`.
- 31 are `unranked_in_view` in at least one robustness view.
- 19 are `not_connected`.

The report lists commanders alphabetically, as the rule requires.

## What changed from run 3, and what did not

**Changed:**

- the comparator, which is now context, not force size alone;
- τ, which is now estimated, not fixed;
- the pre-start strength view;
- no commander term for rule-5 sides;
- the uncertainty rule;
- a war profile;
- compact output: 3.5 MB, against run 3's 40 MB.

**Unchanged:**

- the rating model's form, priors on α and β, and attribution rules;
- multiple imputation, with 20 imputations;
- the views, and their `view_sensitive` reading.

## What this means

- **The verdict.** The test fixed in advance did not find an improvement. The battle-weighted gain
  is robust to resampling campaigns; the campaign-weighted gain is not, and much of either rests on
  Forrest.
- **The in-sample evidence.** It says results vary with commander identity beyond force size and
  coarse context (τ about 0.6, calibrated p about 0.01). Commander identity still bundles the army,
  subordinates and opponents, so this is not evidence of skill.
- **The comparator.** It was weaker than force size alone, which is itself a finding about coarse
  theater and period terms on these rows.
- **The next war.** The rule, code and profile are now fixed and war-agnostic. A Napoleonic run, with
  commanders meeting repeatedly, can apply them unchanged, with any comparator change fixed before
  its data are seen.

## Limits

- Design §12 applies:
  - not causal;
  - coarse context;
  - Laplace and grid approximations;
  - selection;
  - not blind;
  - not a review.
- Concentration, leakage-row and subset figures reuse the held-out predictions. They show where
  the difference sits, not what a refit would give.
- Every result carries `whole_engagement_leakage`, `conditional_on_source_availability`,
  `not_causal`, `side_relative` and, where used, `modelled_strength`.
- The twelve records with a Native American belligerent remain outside the two-sided model.
