# Methodology, version 0.1

## Research question and units

How much better or worse did a command perform than a well-specified comparison
under the opportunities available at a particular replacement time?

Three outputs must remain distinct:

1. **Predictive battle residual:** recorded outcome minus a fitted conditional
   expectation. This includes omitted conditions, luck, measurement error, and
   possible command skill. Version 0.1 implements only this diagnostic.
2. **Battle execution effect:** a counterfactual comparison replacing a commander
   at the start of the engagement, under an explicit command scope and information set.
3. **Campaign contribution:** a counterfactual replacement at campaign onset,
   covering preparation, supply, concentration, decisions to fight or withdraw,
   and achievement of assigned objectives. This is the intended principal measure.

The term “replacement” requires a defined eligible commander population. An
average fitted prediction is not a replacement-level general. Until that definition
and identification strategy exist, the project does not label results WAR.

Each imported record is one source-listed engagement or operation, not one
commander appearance. Commander lists are many-to-one descriptive metadata.
Multiple listed commanders do not multiply a battle's statistical weight and are
not automatically assigned equal shares of credit. Name strings are not yet a
resolved identity registry. Campaigns and strategic objectives will require their
own records; sums of battle residuals are not campaign outcomes.

## Frozen pilot and selection

The source frame is Arnold's CWSAC battle compilation at commit
`3a6020dbfcbcfc650a268b10a9f155588472432b` (384 records).

Select campaigns in the source's **Eastern** or **Western** theater with at least
one engagement starting in **1862 or 1863**, then retain all source-listed
engagements in those campaigns, including any extending outside those years.
Freeze the resulting IDs before model fitting: **127 engagements, 36 campaigns**.
These are complete groups within this source, not exhaustive historical campaigns.
Selection uses no outcome, commander reputation, or strength-availability filter.

The frame already favors recorded principal engagements. It cannot measure all
command opportunities, avoided battles, quiet logistics successes, or documentation
bias. Restricting geography and time improves comparability but does not remove
those biases. The 127 records are a research cohort, not 127 research-complete dossiers.

## Research depth and coverage

Build comparable first-pass dossiers across the frozen cohort before pursuing
fine-grained historical resolution in individual battles. The first pass uses
the existing seven dimensions: strength, terrain, logistics, information,
objectives, responsibility and outcome. Each receives inspected-source claims
or an explicit unknown; a source gap is a valid research result.

Inspect up to three source families per battle, reusing campaign-level sources
where relevant. Make at most one targeted follow-up for the most consequential
gap, then record the unresolved issue and move on. This default effort ceiling
does not require finding three sources, justify unsupported claims, or establish
source independence. Preserve locators, hashes, alternative estimates and
population/time distinctions. Check every passage actually cited. Missing or
inaccessible evidence remains missing after the effort ceiling is reached.

Review first-pass work by complete source campaign. Record source families and
dimensions covered, deferred questions, and actual review scope; distinguish
draft presence from completed first-pass work, separate review and feature
admission. Correct extraction errors without requiring reviewers to resolve
every historical dispute. Do not automatically create a new packet for each
open question. Deeper follow-up should specify which admission or methodological
decision it could change, why existing evidence is insufficient and where the
investigation stops, or respond to an explicit owner request.

Shiloh is the detailed evidence-contract case, not the minimum required depth
for the other 126 engagements. Its remaining source-lineage investigations are
parked under the [current roadmap](roadmap.md). This changes research allocation,
not the cohort, evidence standards, model inputs or admission requirements.

## Eligibility and missingness

The binary baseline admits a row only when it has exactly US and Confederate
forces, a decisive recorded result, positive numerical strength bounds for both
sides, and engagement rather than aggregate-operation grain. Eligibility is not
historical adjudication. Imported rows remain `imported_unreviewed`.

- Unknown strength stays null. A regiment, corps, or army name is not a headcount.
- Zero reported strength is held for review, never used as a small army.
- Inconclusive is preserved as a category, not silently mapped to 0.5.
- Lower/upper bounds are source ranges, not statistical confidence intervals.
- Post-battle casualties, survivors, narrative outcome language, and preservation
  significance are not predictors.
- Commander lists, known reputations, and draft dossier prose are not predictors.

The resulting **23 eligible engagements in 13 campaign groups** are a strongly
selected complete-case subset. Every excluded row remains in the denominator and
queue. The model estimates a recorded Union victory conditional on being a decisive,
numerically documented engagement in this frame; it does not estimate the chance
of victory for every possible engagement. Future missing-data models must justify
their selection assumptions and retain a comparable evaluation population.

## Implemented statistical baseline

Orient each battle once with Union as the positive class:

```
x = (Union strength - Confederate strength) / (Union strength + Confederate strength)
p(Union victory) = sigmoid(intercept + slope * x)
Union residual = recorded Union victory (0 or 1) - p
Confederate residual = -Union residual
```

Strength uses the midpoint of each recorded interval. Fit logistic regression by
minimizing **sum of binary log losses + 0.5 × (intercept² + slope²)**. The penalty
is fixed in advance at 1. Both parameters are penalized, including the intercept;
this differs from many libraries' defaults. The intercept can capture side-specific
conditions and source imbalance. It is not a Union commander effect.

The two-parameter implementation uses Newton steps, backtracking, and a convergence
check. Tests verify score equations, side relabeling, single-class fitting, finite
probabilities, and holdout separation. No hyperparameter search is performed.

For each eligible campaign, fit on every other eligible campaign and predict its
held-out battles. This prevents battles or mirrored sides of the same campaign
from leaking into training. Fold membership is saved. The comparator probabilities
are 0.5 and a Laplace-smoothed Union win rate computed only from that fold's training
rows. Metrics are Brier score and log loss, both per battle and equally weighted
across eligible campaigns. No in-sample performance is presented as validation.

Campaign grouping does not eliminate recurrent commanders, related operations,
shared-source errors, or all chronological leakage. It is a first evaluation
design, not a claim of prospective prediction. The tiny sample has no calibrated
uncertainty estimate for comparative model performance yet. Predefine larger
evaluation groups and a final locked test set before feature experiments.

The endpoint sensitivity calculation varies only each held-out battle's two
strength ranges while retaining the fitted model. It is not a confidence/credible
interval and does not propagate uncertainty from training records. Later work
should refit across disputed input scenarios and cluster uncertainty by campaign.

## Identification and the next model

At campaign replacement time, a commander's preparation and force concentration
are potential mediators. Conditioning on them can remove the contribution we want
to measure. At battle replacement time, some of those same variables may be
inherited state. The labels must therefore be attached to an explicit boundary,
authority, and timeline, with uncertain classifications kept unresolved.

An enriched model should start with an explicit causal diagram and confounder/
mediator audit. Consider hierarchical commander, opponent, army, and campaign
effects with partial pooling. Check whether commander assignments and army context
can be distinguished at all; weakly connected schedules may not identify them.
No numerical causal claim follows merely from adding controls or fitting a
hierarchical model. Sensitivity to unmeasured confounding and assignment remains necessary.

Campaign success should be coded against pre-specified objectives, time, resources,
and preservation of useful force. Avoid subjective utility weights disguised as
facts. Model objectives with multiple outcomes or publish explicit sensitivity
scenarios. A battlefield withdrawal can achieve a campaign objective. Battle and
campaign scores must not be added as independent successes.

Cross-era comparisons are outside the pilot. Era-normalized distinction would not
establish who would win under identical conditions. Cumulative contributions,
performance per comparable opportunity, and evidence coverage should eventually
be displayed separately, with uncertainty and no precision unsupported by evidence.

## AI's role and validation

AI locates evidence, extracts claims, maps terminology, reconstructs decision
timelines, and identifies disagreements. It does not supply win probabilities or
authoritative hidden morale scores. Known historical outcomes can leak from model
training even when names are masked. Blinding is a diagnostic, not proof of no leakage.

Audit extraction accuracy separately from predictive quality: compare proposed
claims against passages and independent review; record disagreements, source
dependence, missing dimensions, and corrected claims. Matching a quote does not
prove it supports the claim, and a correct extraction can preserve an incorrect source.

Version 0.1 neither calls a model API nor trains on dossier text. The three draft
dossiers illustrate the evidence contract and cannot be treated as validated
enriched features. A separate fresh-context Astra `xhigh` review of the frozen
Shiloh dossier checked 62 claims, 40 quantities, 26 events and 26 supplied scan
selections; 35 of 65 cited source/section pairs remain text/CSV-only. Its
[actual response and primary assessment](research/shiloh-review-handoff.md#completed-ai-review)
retain historical disputes. The [four corrections](research/shiloh-review-corrections.md)
are implemented in a versioned draft with focused implementation review and
validator follow-up accepted. Antietam and Champion
Hill have no separate review. AI review is not human historical adjudication or
proof of source independence. Agreement with famous-generals lists is never an
acceptance criterion.

## Feature-admission design

The [v1 admission specification](feature-admission.md) defines a future
retrospective pre-engagement prediction profile and immutable evidence-use
review/release gates. This profile may use later reports to reconstruct an earlier
state; it does not claim to forecast from a historical commander's information
set. It excludes post-boundary state and participation, including indirect use
through transformations, and keeps unresolved scope and source alternatives
visible. The [offline validator](admission-validator.md) now implements proposal
and manifest checks without promoting model inputs or fitting enriched models.

The [13 Shiloh design cases](research/shiloh-admission-examples.md) cover selected
observations and emit no features. The proposed opening population and boundary
still need evidence-use review. Future evaluation must distinguish paired
common-row comparisons from expanded coverage and preserve complete campaign
holdouts. Tactical replacement and campaign contribution require separately
reviewed causal designs; contract acceptance does not establish either effect.
