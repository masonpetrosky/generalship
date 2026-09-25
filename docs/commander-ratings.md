# Commander residual ratings, design v1 (proposed)

**Status: proposed; awaiting separate design review.** On 2026-09-25 the owner asked for
the next step towards ranking generals and answered the design questions put to them:
"Okay, yeah I'm fine with whatever you recommend." The choices below are the author's
recommendations, recorded as such. The owner delegated them; they are not the owner's own
words.

The design has two parts:

1. A **command-responsibility ledger**, which names one responsible commander for each side
   of each engagement, as a graded best estimate.
2. A **partially pooled residual model**, which summarises how each commander's battles went
   relative to what force size predicts, with uncertainty.

It changes nothing in the frozen baseline, the [best-estimate ledger](strength-estimates.md),
the [admission contract](feature-admission.md) or the dossiers. Like the
[estimate-layer evaluation](research/estimate-evaluation-v1.md), it is an exploratory
diagnostic layer.

## 1. What is measured

The measure is the [methodology's](methodology.md#research-question-and-units) first output,
the **predictive battle residual**, attributed to a responsible commander and pooled across
their battles. It is called a **residual rating**.

- **Included.** A residual contains omitted conditions, luck, source error and possibly command
  skill. The rating cannot separate them.
- **Not measured.** The rating is not the battle execution effect or the campaign contribution
  (methodology outputs 2 and 3), and not a causal effect. It is not replacement-level value
  (WAR).
- **Force size is conditioned on.** A commander who wins by concentrating superior numbers
  gets no credit for that concentration, because the force ratio may be a commander-created
  advantage (a mediator). The outcome-only view (§6) shows the other side of that choice. Neither
  view is the true measure.
- **Scope.** The pilot covers the 1862–1863 Eastern and Western campaigns only. No result is a
  Civil War ranking: careers are cut off at both ends (§8).

## 2. Command-responsibility ledger

**Target.** For each of the 91 decisive, non-aggregate engagements and each side, name:

> the officer exercising overall command of that side's forces engaged in the frozen record,
> at the start of the record's interval (the **responsible commander**).

The start-of-interval anchor matches the methodology's replacement time for a battle.

**Evidence.** Only registered sources may be used:

- the dossier's `responsibility` claims and their cited passages;
- other passages in registered sources that the dossier already cites;
- the frozen CWSAC commander listing (`cwsac_commanders.csv`), which names commanders without
  saying who held overall command.

Model recollection is never a source. When no inspected passage settles a question, the
ledger records it as unresolved.

**Rules.**

1. **One commander per side.** Credit is never split equally among all listed commanders, and
   a battle never counts more than once per side.
2. **Listing alone.** If the side has exactly one CWSAC-listed commander and no inspected
   passage contradicts the listing, that commander is used.
3. **Several listed commanders.** Use the one an inspected passage shows directing the side's
   engaged force. If no passage settles it, use the senior listed officer by the listed rank,
   and label the side `responsibility_unresolved`.
4. **Command change within the interval** (death, wounding, relief, or a superior arriving and
   taking command). Use the commander at the start, and label the side `command_changed`,
   naming the successor.
5. **Joint or naval command.** If land and naval commanders shared the action with no overall
   commander shown, use the commander of the force whose action the frozen record describes,
   and label the side `joint_command`.
6. **Nobody identifiable.** If no commander can be named, the side is grade D and gets no
   commander term in the model.

**Grades.**

| Grade | Condition |
| --- | --- |
| A | An inspected passage states that the officer commanded the side's engaged force, and nothing inspected contradicts it. |
| B | Rule 2 applies: a single listing, uncontradicted, with no passage stating the command. |
| C | Rules 3–5 decided the choice, or inspected sources disagree. |
| D | No identifiable commander. |

**Identity registry.** `data/command/commanders-v1.json` gives each commander a stable ID, their
side and every CWSAC name string mapped to them. Identity comes only from registered listings
and cited passages. Two strings are merged only when a passage or the listing's own fields show
they are the same person; unresolved cases stay separate and are labelled.

**Ledger and checker.** `data/command/responsibility-v1.json` records for each side:

- the commander ID;
- the grade and labels;
- the successor, if any;
- the citations (source ID, locator, exact quote);
- a rationale.

An offline checker verifies:

- coverage of all 91 engagements × 2 sides;
- that every quote occurs in its source;
- that every ID resolves in the registry;
- that every CWSAC listing for the engagement is accounted for (used, or recorded with a
  reason);
- that grades follow from the recorded rule.

**Review.** A separate Opus review checks the ledger in campaign batches, as for the strength
ledger.

## 3. Rows

**Primary rows.** These are the 37 rows of the reviewed strength ledger in which both sides are
grade A–C, with no `post_start_information` label: the same rows as the
[evaluation](research/estimate-evaluation-v1.md)'s A–C set. Each row:

- is oriented once, with a Union win as the positive outcome;
- uses each side's rounded point strength.

**Coverage report.** Every commander is reported with:

- all battles attributed to them among the 91;
- how many of those are in the model;
- why the others are out (strength grade D, post-start, or unattributed).

Sparse evidence must not quietly become an average rating (roadmap Milestone 2).

## 4. Model

For battle *i*, with force ratio x_i = (US − CS)/(US + CS):

```
logit P(Union win) = α + β·x_i + θ[US commander of i] − θ[Confederate commander of i]
θ_k ~ Normal(0, τ²), independently for each commander k
α, β ~ Normal(0, 1)   (the baseline's ridge 1.0)
```

- **Pooling.** τ is fixed in advance at **0.5** on the log-odds scale, before any fit. One
  standard deviation of τ moves an even battle to about 62%. Every θ is pulled towards zero, most
  strongly for commanders with few battles. There is no hyperparameter search.
- **Commander sides.** A commander always fights for one side, so each θ enters with that
  side's sign. A side without a commander (grade D) contributes no term.
- **Fit.** The posterior mode is found by Newton's method on all parameters, using the standard
  library only (a Cholesky solve). A stopping rule based on the Newton decrement is used, as in
  the baseline.
- **Uncertainty.** A Laplace approximation (the inverse Hessian at the mode) gives an approximate
  posterior. The report gives 80% and 95% intervals for each θ. Rank intervals come from 20,000
  draws of that approximation with a fixed seed. These are approximate model-based intervals.
  They leave out attribution, strength and source uncertainty, which the sensitivity views cover
  (§6).

**Commanders with fewer than 2 battles in the model** get no rank position. They are listed
separately, with their estimate and interval, because their rating is almost entirely the
prior.

## 5. Held-out test

Before anything is ranked, the design asks whether commander identity carries any predictive
signal:

- **Method.** Leave-one-campaign-out, on the primary rows. Compare the commander model with the
  strength-only model on the same rows and folds. A commander unseen in training gets θ = 0.
- **Scores.** Brier and log loss, weighted by battle and by campaign. The report also counts the
  campaigns where each model does better.
- **Pre-stated reading.** Suppose the commander model does not reduce held-out log loss under
  both weightings. Then the report says that commander identity adds no detectable predictive
  signal in these data. The ratings are then presented only as descriptive, heavily pooled
  residual summaries.
  - No significance test is run.
  - An improvement is not proof of skill: commanders are tied to armies, theaters and opponents
    (§8).

## 6. Sensitivity views

Each view refits the model and reports its ratings beside the primary ones:

- **Pooling strength.** τ = 0.25 and τ = 1.0.
- **Attribution grades.** Only sides whose attribution is grade A or B; other sides get no
  commander term.
- **Command changes.** Rows labelled `command_changed` excluded.
- **Strength endpoints.** The four endpoint refits (US low or high × Confederate low or high), as
  in the evaluation.
- **Outcome-only view.** No force-ratio term (β = 0), on all 91 decisive engagements with
  attribution. This view credits force concentration, and also every other advantage the
  commander did not create. It is labelled `includes_force_size_advantage`.

A commander whose rank interval or sign changes across views is flagged `view_sensitive`.

## 7. Outputs and records

- `artifacts/commander-ratings.json` and `.md`. Per commander, they give:
  - battles attributed, battles modelled, and wins and losses in the model;
  - the sum of raw residuals, the posterior mean θ, the 80% and 95% intervals, and the rank
    interval;
  - the attribution grade mix, labels, and results in every view.
- A research memo that interprets the results against the §5 test.
- **Gate.** The command `commander-ratings` refuses to run unless:
  - the responsibility ledger's review is reconciled; and
  - an owner authorization record names the hashes of both ledgers, as for the evaluation.

  Its outputs never enter `artifacts/baseline.json`.
- **Reviews.** A separate Opus review covers this design, then the responsibility ledger in
  campaign batches, then the model code and results.

## 8. Limits and non-goals

- **Not causal.** The rating is not command skill. Commanders are not randomly assigned to
  armies, theaters, opponents or odds. The Union intercept α absorbs side-wide differences only
  partly. Army quality, subordinates and supply stay in the residual.
- **Few battles.** On the primary rows only about a dozen commanders have two or more battles.
  Most ratings will sit near zero with wide intervals, and that is the correct result.
- **Selection.** Which battles have usable strengths may depend on the outcome, size and fame.
  Every result carries `whole_engagement_leakage` and `conditional_on_source_availability`.
- **Truncated careers.** The pilot covers only 127 of the 384 source-listed engagements
  (1862–1863, Eastern and Western). The Overland, Atlanta and other 1864–65 campaigns, the
  Trans-Mississippi and 1861 are absent. A Civil War ranking needs the full frame researched to
  the same standard first. That is an owner decision about scope (§9).
- **No reputation check.** A familiar-looking list is not evidence of correctness, and an
  unfamiliar one is not evidence of error.
- **Also excluded.** There is no battle and campaign double counting, no cross-era comparison
  and no imputation of commanders.

## 9. Next decisions after this pilot

- **Extend the cohort to the full war.** That is 257 more engagements, researched in campaign
  batches to the first-pass standard, with strength and responsibility ledgers.
- **Campaign contribution** (methodology output 3). This needs coded campaign objectives, and is
  a separate design.
- **Methods for sparser eras.** The owner expects far thinner evidence for earlier wars. The
  graded best estimates, grade-D handling and pooling here are meant to degrade gracefully to
  that case: with less evidence, ratings move towards zero, with wider intervals.
