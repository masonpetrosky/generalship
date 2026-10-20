# Napoleonic temporal probability-correction test v1

Status: primary-verified preparation only. The owner accepted designing one fixed
development-only test after the [1813 diagnostic](research/napoleonic-forward-diagnostic-v1.md).
That acceptance does not authorize a historical fit. No run authorization is created here.

## Question and limits

Does one training-only additive correction improve the next source-year cohort's
predictions of Bodart's recorded winner? This tests a probability-calibration
alternative to the existing compiler-strength baseline. It estimates no commander,
tactical, appointment or campaign-contribution effect and admits no enriched feature.

The original development frame remains **273 entries / 13 complete source groups**.
All **52 final entries / three groups** retain their existing reservation. Neither
historical familiarity nor their presence in a hashed source makes them blind.
No reserved ID is used for fitting, calibration, selection or scoring.

All development outcomes were exposed in prior work. This protocol is fixed before
its own execution but is **exploratory**, motivated by an inspected 1813 result.
The 1813 scores cannot govern the continuation decision. This is statistical
probability correction, distinct from the prepared, unscored extraction-review sample.

## Fixed records and availability

Use the unchanged [prepared compiler dataset](../artifacts/napoleonic-benchmark-v1.json),
its four fixed populations and exact exclusions. Read only the whitelisted A/B
personnel totals as numerical predictors. A is France and its allies. Missing
extracts, ambiguous totals, notes and population/time uncertainty remain unchanged.
No figure is fetched, repaired, imputed or selected from a dossier.

For each frozen development group, derive completion as the maximum `end_date`
over **every member**, including rows excluded from a numerical population. Any
unknown end date makes that group unavailable for training. Do not move an entry
to another group or discard an inconvenient late-ending member.

For target cohort year Y, fix a cutoff of January 1 of Y. A training group must
have an earlier cohort year and a known completion strictly before that cutoff.
All members of a group occupy the same temporal role, subject only to the existing
population's numerical eligibility. Test groups are all original groups with
`start_year == Y`; every test exclusion remains in the denominator.

The base groups must additionally finish strictly before the earliest known start
of **every calibration member**. An unknown calibration start or an overlapping
base group makes the whole paired fold not estimable. Do not try another block
or silently remove a member. The prepared historical folds satisfy this guard.

Several cohorts end later than their start-year labels. For example the frozen
`peninsula 1810` group ends in 1812 (`B437b.end_date`); it is unavailable to training
before 1813. These locators identify existing encoded metadata, not a fresh
historical adjudication. The [generated plan](../artifacts/napoleonic-temporal-calibration-plan-v1.md)
publishes every group completion date and controlling entry locator.

Event completion is an explicit retrospective admissibility proxy. It does not
establish when a source was written, published or known to a commander. The
whole-entry force totals still lack an established opening-state clock/population,
so this is not a contemporary-information forecasting design.

## One fixed correction and five comparators

Among available groups, the calibration block is **all groups completing in the
latest nonempty completion calendar year**. The base block contains every earlier
available group. There is no search for a favorable window. When no newer complete
group becomes available, the block repeats; its age is reported, not concealed.

Require at least **ten eligible base rows and ten calibration rows** in a population.
This is a pragmatic support floor, not a validated precision guarantee. A deficient
fold remains not estimable with reasons; no fallback fits on its test labels.

1. Fit the existing ridge-1 force model on base rows only:
   `x = (A-B)/(A+B)` and `z = alpha + beta*x`. Both alpha and beta are penalized
   as in the original benchmark.
2. Freeze alpha and beta. On the disjoint calibration block, estimate one delta by
   minimizing `sum(log_loss(sigmoid(z_i + delta), y_i)) + delta²/2`.
3. Predict test rows with `sigmoid(alpha + beta*x + delta)`. Keep the base model
   frozen after estimating delta; do not refit it on calibration rows afterward.

The offset score equation is `delta + sum(sigmoid(z_i+delta)-y_i) = 0`; its derivative
is `1 + sum(p_i*(1-p_i)) > 0`. Bisection on `[-n, n]` finds its unique root, checked
to absolute score-equation tolerance `1e-9`. No label-dependent support filter,
penalty tuning, slope correction or alternate calibration method is proposed.
The penalty shrinks delta toward zero rather than forcing exact agreement with
the calibration block's observed win share. Within a fold, the correction retains
the base model's ordering; no ordering improvement is claimed.

Score these five fixed comparators on exactly the same test rows:

| Comparator | Fit or estimate uses |
| --- | --- |
| `same_base_force` | The identical base force model, with delta zero |
| `expanding_force` | A separate ridge-1 force model fitted on base plus calibration rows |
| `expanding_prior` | `(A wins + 1)/(n + 2)` over base plus calibration rows |
| `recent_prior` | The same Laplace prior over calibration rows only |
| `equal_odds` | Fixed probability 0.5 |

The expanding force comparator prevents success from being defined solely against
an older, smaller training fit. The recent prior checks whether force information
adds value beyond using only the calibration block's outcome frequency. Each
population refits its own models; their cross-population differences are not
causal effects of source qualifiers.

## Frozen folds, coverage and output

The annual inventory includes 1805–1813. The rules yield no scorable outer fold
in 1805–1807: 68 development entries, including 42 primary-eligible rows, remain
warmup. The main decision region is **1808–1812: 115/141 primary entries in five
annual folds and seven complete source groups**, with all 26 exclusions retained.

**1813 remains secondary and reused: 37/64 entries**, with all 27 exclusions.
Two eligible 1813 development entries end in 1814 (`B483a`, `B483c`); their IDs
remain development under the unchanged start-cohort reservation. This does not
reclassify or consume any of the 52 reserved-final IDs. The primary plan's 273-entry
denominator reconciles as 68 warmup + 141 main + 64 secondary.

The four populations remain primary (194 eligible), printed-indecisive exclusion
(194, a no-op), non-combat exclusion (193), and unqualified totals (163). The last
has **103/141 main and 30/64 secondary** eligible entries. Publish every population;
do not select the best sensitivity after execution. There are 24 scorable
population/year folds and 72 proposed parameter fits: two force fits and one
offset per fold. Preparation runs none.

Publish fold membership/support, deferred earlier groups, parameters/offset score
equations, all six probabilities, every paired case loss, and unscored IDs. Report
log loss (natural logarithms), Brier and the original five probability bins, under
battle and equal-source-campaign weighting. Show main and 1813 results separately,
all year/group scores, and concentration of absolute paired log-loss differences
using a denominator that retains gains and losses without cancelling them.

Five annual folds/seven source groups, repeated calibration blocks, overlapping
training sets, long operations and one compiler family provide limited replication.
No bootstrap confidence interval or significance claim is proposed. Source
selection, strength-dependent outcome coding and uncertain force populations remain
unresolved. An improved compiler-record score would not establish calibrated
historical probabilities or command skill.

## Fixed exploratory continuation rule

Only the **primary 1808–1812** scores determine the main comparison. Continue this
one correction for a later explicitly scoped design only if:

1. It has strictly lower log loss and nonhigher Brier than **each of the five
   comparators**, under both battle and equal-campaign weighting.
2. It lowers battle-weighted log loss against expanding force in at least three
   of the five decision years.
3. The unqualified-total sensitivity does not worsen either score against
   expanding force under either weighting.

Use absolute arithmetic tolerance `1e-12`: a strict improvement must exceed it;
non-worsening allows it. Missing required annual or aggregate scores means
**not assessable**, never passed. Publish every failed comparison and retain the
uncorrected alternative. The other fixed sensitivities are reported without
changing the rule. **Never inspect the 1813 scores inside the decision function.**

This is a pragmatic exploratory continuation rule, not a confirmatory test,
automatic promotion, feature admission or the separate methods-v1 commander-rating
gate. Passing does not authorize a final evaluation; failing does not trigger a
window search, another correction or wider historical research.

## Execution boundary and reproduction

The [proposal](../data/napoleonic/temporal-calibration-v1/run-proposal.json) binds
the exact design, protocol, source dataset, executing files and prepared outputs.
The historical runner requires a later owner authorization matching the proposal
SHA-256, exact command and scope, and actual owner reply **before reading outcome
labels or calling any fitter**. It refuses to overwrite its proposed result path.

The current owner reply authorizes this preparation only. No run authorization or
historical result is created. Tests fit constructed cases only. `make check` and
`make reproduce` invoke the metadata-only planner; they never invoke the historical
runner. Reproduction can restore missing/corrupt plan outputs but cannot silently
rebind a frozen proposal after an input or code change.

Preparation stops at the validated, executable proposal. Preserve all previous
versioned records, inputs, source bytes and numerical results. No new evidence
source, dossier, opening selection, commander identity, rating, second-opinion
prompt, separate reviewer or subagent is part of this task.
