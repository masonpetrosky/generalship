# Bodart provisional ratings v1: fixed experiment and admission

Prepared and primary-verified on 2026-10-21, before the first fit. The owner's
“Sounds good, go ahead” accepts the proposed broader provisional ranking from the
expanded Bodart table. This authorizes this explicit standalone experiment and its
fixed checks. It does not authorize changes to earlier frozen models or their final set.

## Input and target

Use only our `artifacts/bodart-bulk-v1.csv`, its metadata and source bindings. No
Arsht data, code, ranking target, or dossier-derived predictor is used. The target is
association with Bodart's recorded decisive winner, conditional on his force readings
and the opposing printed command label. It is not causal generalship, tactical effect,
campaign contribution, wins above replacement, or a historical victory probability.
Force size can itself reflect command decisions. Army quality and appointments remain
confounded with command labels.

This is a separate exploratory admission profile: the primary admits the bulk table's
year, printed event type, decisive outcome, paired positive personnel and normalized
single command labels for this descriptive experiment only. Raw strings, source IDs,
locators, SHA-256 hashes and image-check scope remain in the bound table. Existing
image-checked transcription and unchecked OCR remain distinguishable. No historical
identity or responsibility ledger is inferred. No enriched dossier feature is admitted.

## Rows and command units

Start with all 1,682 entries. Exclude the 52 reserved-final IDs before any numerical
use. Exclude naval, indecisive and no-combat entries, unknown years, and event types
other than exactly SCHLACHT, TREFFEN, GEFECHT or REITERGEFECHT. This excludes sieges,
capitulations and combined/aggregate descriptions rather than adding campaign outcomes
to battle wins. It does not resolve every possible overlap among source entries.

Require two positive personnel totals and two nonempty single command labels.
Exclude flagged malformed/ambiguous/multiple-state force readings unless the numerical
field was image-corrected. Reject joint labels, parentheses, Arabic digits, prose,
commas, semicolons, slashes and labels longer than 80 characters. Remove a fixed list
of leading military ranks only; normalize Unicode, case and punctuation. Preserve
nobility, geographic qualifiers and Roman numerals. No biographical alias merging:
Bonaparte/Napoleon and Wellesley/Wellington can remain different units. Exclude equal
opposing labels and any normalized unit spanning more than 60 years in otherwise
eligible records. Shorter-span homonyms and spelling fragmentation remain possible.
Reject embedded military ranks after leading-rank removal: this catches joint labels
without “und” and can conservatively omit valid names with nationality prefixes.

Every row has an inclusion decision and explicit exclusion reasons. Labels are source
strings, not verified people or an allocation of command credit to everybody present.
Order only units with at least three appearances, within their connected opponent
component. Other estimated units remain downloadable without a rank. Components have
no common historical scale merely because the prior supplies a numerical zero.

## Fixed model and uncertainty

Use our own symmetric regularized paired-comparison implementation. The general model
family is [Bradley and Terry (1952)](https://doi.org/10.1093/biomet/39.3-4.324).
For labels A and B sorted by normalized key (not by winner), define
`x = log(personnel_A / personnel_B)` and `y = 1` when A is Bodart's winner:

`logit(p_A) = beta*x + theta_A - theta_B`.

There is no intercept. Fixed independent zero-centred Gaussian priors have SD 2 for
beta and SD 1 for each theta. Estimate the strictly convex penalized likelihood with
Newton/conjugate-gradient optimization. Report the convergence residual. Do not choose
priors after viewing the historical fit. Theta is a shrunk log-odds association, not
a sum of wins. A zero estimate in sparse data does not mean mediocre ability.

For ordered labels, report marginal 95% Laplace intervals from inverse-Hessian solves.
These are approximate conditional intervals, not rank intervals. They omit source/OCR,
identity, selection, campaign dependence and model uncertainty, and do not justify
confident adjacent ranks. Fixed sensitivities use theta prior SD 0.5 and 2 on the same
rows, plus SD 1 on rows with both personnel fields image-checked. Report sensitivity
orders separately from confidence intervals and show the checked subset's denominator.
Personnel checks alone do not verify command labels or remove source bias.

## Fixed evaluation

Leave out each calendar decade (`10 * (year // 10)`) in turn. Fit on the other decades
and save one prediction per held-out row from (1) force plus command labels, (2) force
only with the same beta prior, and (3) equal odds. A label absent from training has
theta zero. Save fold memberships and coefficients so training exclusion and predictions
can be checked without refitting. Report log loss and Brier score both per battle and
with each decade weighted equally, plus cold-label coverage.

This is a development diagnostic, neither a forward forecast nor complete-campaign
holdout. Campaigns can cross decade boundaries, and army/source dependence remains.
No held-out predictive improvement establishes correct personal skill rankings or
isolates AI's benefit. The 1814–1815 final reservation is not scored, tuned on or fitted.

## Execution and stopping rule

Commit this protocol, prepared cohort, implementation and toy tests before the first
historical run. The saved run binds that Git commit, all input SHA-256s, this protocol,
the cohort and the implementation. Run once using the fixed specification; retain an
unimproved result. Fix genuine implementation errors transparently rather than tuning
the experiment. Primary verification checks selection, orientation, numerical gradients,
held-out predictions, interval solves, counts and rendered output. No separate reviewer
or second-opinion prompt is required or implied.

`python3 -m generalship.bodart_ratings --prepare` writes the deterministic cohort.
`python3 -m generalship.bodart_ratings --run` is the explicit historical job.
`--write` regenerates reports/downloads from the saved run; the default checks them.
Ordinary tests and `make reproduce` never fit historical outcomes. Stop after this
provisional report and its validations; additional dossiers are not a prerequisite.
