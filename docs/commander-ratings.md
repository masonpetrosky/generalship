# Commander residual ratings, design v1 (proposed)

**Status: proposed; revised after a separate design review.** On 2026-09-25 the owner asked
"Are we ready to rank the generals in the American civil war, or is there still work to be
done?". Later the same day they were asked three design questions: who gets credit, what unit
is scored, and how a rating is computed. They answered: "Okay, yeah I'm fine with whatever you
recommend." The [decision record](../data/command/owner-decision-2026-09-25.json) keeps the
questions and replies verbatim. The choices below are the author's recommendations, which the
owner delegated; they are not the owner's own words. The same reply also confirms the
evaluation's option (a) ([confirmation](../data/estimates/evaluation-authorization-v1-confirmation.json)).

This text applies the required corrections R1–R9 of the separate
[design review](../artifacts/review-results/ratings-design-0de28bd-opus-high-v1/review.md) of
`0de28bd`, with advisories A1–A7 adopted.

The design has two parts:

1. A **command-responsibility ledger**, which names one responsible commander for each side of
   each engagement, as a graded best estimate.
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
- **Force size is partly conditioned on.** The force-ratio slope β has a Normal(0, 1) prior. On
  the 37 primary rows, the data carry roughly as much information about β as the prior does, so
  β is shrunk towards zero and part of the force-ratio effect remains in the residual.
  - A commander who wins by concentrating superior numbers gets little, though not necessarily
    zero, credit for that concentration, because the force ratio may be a commander-created
    advantage (a mediator).
  - The outcome-only views (§6) show the other side of that choice. Neither view is the true
    measure.
- **Relative to one's own side.** Ratings compare a commander with the other commanders on the
  same side (§4, side offset).
- **Scope.** The pilot covers the 1862–1863 Eastern and Western campaigns only. No result is a
  Civil War ranking: careers are cut off at both ends (§8).

## 2. Command-responsibility ledger

**Target.** For each of the 91 decisive, non-aggregate engagements and each side, name:

> the officer who held command of that side's engaged forces, as the field commander directing
> the operation, when the record's fighting began (the **responsible commander**).

- ***Command*** means command authority over the engaged forces. The officer need not have been
  on the part of the field where fighting began. A departmental or national superior who was not
  directing this operation in the field is excluded.
- ***When the fighting began*** means the side's first combat within the frozen interval, which
  matches the methodology's replacement "at the start of the engagement". Frozen intervals are
  dates. A change of command on the start date before the first combat is therefore not a command
  change under rule 4: the officer in command at first combat is used.
- **Superior directing.** An inspected passage may show a superior other than the listed
  commander directing the operation from within the theater. MS001 is an example: the NPS
  description has Grant ordering Ord "to await the sound of fighting between Rosecrans and Price".
  In that case the listing still decides under rules 2–3. The side is labelled
  `superior_directing`, naming that officer, and §6 adds a view that uses the superior instead.

**Evidence.** Only registered sources may be used:

- the dossier's `responsibility` claims and their cited passages;
- other passages in registered sources that the dossier already cites;
- the frozen CWSAC commander listing (`cwsac_commanders.csv`), which names commanders and ranks
  without saying who held overall command.

Model recollection is never a source. When no inspected passage settles a question, the ledger
records it as unresolved.

**Rules.** They are applied in the order 5, 3, 2, 6. Rule 4 is then applied to the result, and
rule 7 across records.

1. **One commander per side.** Credit is never split among listed commanders. A battle never
   counts more than once per side.
2. **A single listed commander.** Use that commander unless an inspected passage contradicts the
   listing.
   - A passage contradicts the listing only if it names a different officer as commanding the
     side's engaged forces when the fighting began.
   - A passage showing a superior directing, or a subordinate leading part of the force, is not
     a contradiction. It is recorded as `superior_directing` or as subordinate context. MS006 is
     an example: Greene shows McClernand directing three divisions while CWSAC lists Grant.
3. **Several listed commanders in one service.**
   - (a) Use the one an inspected passage shows in command of the side's engaged forces when the
     fighting began.
   - (b) Otherwise, if one listed officer outranks every other by listed rank, use that officer and
     label the side `responsibility_unresolved`.
   - (c) If the highest listed ranks tie (for example, TN003 on both sides, VA102 US and GA003 CS),
     there is no rank fallback. The side is grade D, labelled `responsibility_unresolved`, with the
     tied candidates recorded.
4. **Command change within the interval.** Examples are death, wounding, relief, or a superior
   arriving and taking command after the first combat. Use the commander at first combat, and
   label the side `command_changed`, naming the successor.
5. **Several listed commanders in different services** (the CWSAC `navy` field differs, for
   example TN001 and AR006).
   - If an inspected passage shows one officer in overall command of both forces, use that officer.
   - Otherwise, use the listed commander of the force that an inspected passage or the frozen
     description shows compelling the result (for example, surrender "to the fleet" at TN001), and
     label the side `joint_command`.
   - If neither is shown, the side is grade D, labelled `joint_command`, with the candidates
     recorded.
6. **Nobody identifiable.** If no commander can be named, the side is grade D.
7. **Nested records.**
   - The checker lists every same-campaign pair among the 91 whose frozen interval lies inside
     the other's.
   - For each pair, the ledger records one outcome:
     - `nested`, if an inspected passage or the frozen description shows that the containing
       record's fighting or force scope includes the contained record (for example, VA032's
       description narrates the Sedgwick operations and Salem Church, VA033);
     - `not_nested`, with a reason;
     - `nesting_unresolved`.
   - No view gives one commander both records of a `nested` pair: the containing record is used,
     and the contained one is listed as nested.
   - For `nesting_unresolved` pairs, every view that contains both records is reported with and
     without the contained record.

A grade D side contributes no commander term to the model. Its row still counts through α
and β.

**Grades.**

| Grade | Condition |
| --- | --- |
| A | Rule 2 or 3(a): an inspected passage states that the officer commanded the side's engaged forces when the fighting began, and nothing inspected contradicts it. |
| B | Rule 2 with no passage stating the command, and nothing inspected contradicting the single listing. |
| C | Rule 3(b) or rule 5 decided the choice, or inspected sources disagree about who commanded. |
| D | Rule 3(c), rule 5 with nothing shown, or rule 6. |

Labels such as `command_changed` and `superior_directing` do not change the grade. Each side also
records the responsible commander's **echelon** (army, wing or corps, division, brigade, or
detachment and post) as the passages or the listing show it, or `unknown`.

**Identity registry.** `data/command/commanders-v1.json` gives each commander:

- a stable ID;
- their side;
- every CWSAC name string mapped to them.

Identical `fullname` strings on the same side are presumed to be one person unless a passage or a
listing field shows otherwise. Other merges need a passage or the listing's own fields.
Unresolved cases stay separate and are labelled.

**Ledger and checker.** `data/command/responsibility-v1.json` records, for each side:

- the commander ID and echelon;
- the grade and labels;
- the other candidates and the successor, if any;
- the citations (source ID, locator, exact quote);
- a rationale.

It also records the nesting outcome of each contained-interval pair. An offline checker verifies:

- coverage of all 91 engagements × 2 sides;
- that every quote occurs in its source;
- that every ID resolves in the registry;
- that every CWSAC listing for the engagement is accounted for (used, a candidate, or recorded
  with a reason);
- that grades follow from the recorded rule;
- that every contained-interval pair has a nesting outcome.

**Review.** A separate Opus review checks the ledger in campaign batches, as for the strength
ledger.

## 3. Rows

**Primary rows.** These are the 37 rows of the reviewed strength ledger in which both sides are
grade A–C and neither side has a `post_start_information` label: the same rows as the
[evaluation](research/estimate-evaluation-v1.md)'s A–C set. Each row:

- is oriented once, with a Union win as the positive outcome;
- uses each side's rounded point strength.

**Coverage report.** Every commander is reported with:

- every battle attributed to them among the 91;
- how many of those are in the model;
- why the others are out (strength grade D, post-start, nested, or unattributed).

Sparse evidence must not quietly become an average rating (roadmap Milestone 2).

## 4. Model

For battle *i*, with force ratio x_i = (US − CS)/(US + CS):

```
logit P(Union win) = α + β·x_i + θ[US commander of i] − θ[Confederate commander of i]
θ_k ~ Normal(0, τ²), independently for each commander k
α, β ~ Normal(0, 1)   (the baseline's ridge 1.0)
```

- **Pooling.** τ is fixed at **0.5** on the log-odds scale, before any fit. It is a declared
  convention, not an estimate, and there is no hyperparameter search.
  - A commander effect of one prior standard deviation (0.5) moves an even battle to about 62%.
  - A difference θ_US − θ_CS of one prior standard deviation (about 0.71) moves it to about 67%.
  - Every θ is pulled towards zero, most strongly for commanders with few battles.
- **Commander sides.** A commander always fights for one side, so each θ enters with that side's
  sign.
- **Side offset.** The likelihood cannot separate α from a common shift of one side's θs. The
  priors give nearly all of a side-wide difference to α, so each side's commanders are
  effectively centred on zero, and α absorbs any real difference between the two sides' average
  commanders. Ranks are therefore computed **within each side**. A combined list, if shown at all,
  is labelled `cross_side_prior_anchored`.
- **Connectivity.** The report gives the connected components of the commander–opponent graph on
  the modelled rows, and each commander's component.
  - Within a component, the data inform differences between θs. Between components, only α, β
    and the prior do.
  - A ranked commander who shares a component with no other ranked commander of the same side is
    labelled `not_connected`.
- **Fit.** The posterior mode is found by Newton's method on all parameters, using the standard
  library only (a Cholesky solve), with the baseline's Newton-decrement stopping rule. The
  objective is strictly convex, so the mode is unique.
- **Uncertainty.** A Laplace approximation (the inverse Hessian at the mode) gives an approximate
  posterior. Its mean equals the mode.
  - Each θ gets central 80% and 95% intervals.
  - Rank intervals come from 20,000 draws of the approximation with a fixed seed.
  - These are approximate model-based intervals. They leave out attribution, strength and source
    uncertainty, which the sensitivity views cover (§6).
  - A unit test compares the Laplace interval with brute-force quadrature for one θ on a
    synthetic case.
- **Rank set.** Within each side, ranks are computed among commanders with at least 2 modelled
  battles, with central 80% and 95% rank intervals.
- **Prior dominance.** Commanders with fewer than 2 modelled battles get no rank position. They
  are listed separately, with their estimate and interval. Every commander's output also gives
  the ratio of posterior to prior standard deviation. With τ = 0.5, near even odds, that ratio is
  about 0.94 for 2 battles and 0.87 for 5, so ratings from a handful of battles are still mostly
  prior.

## 5. Held-out test

Before anything is ranked, the design asks whether commander identity carries any predictive
signal.

- **Method.** Leave-one-campaign-out, on the primary rows. The commander model is compared with
  the strength-only model on the same rows and folds. A commander unseen in training gets θ = 0.
- **Verdict configuration.** The verdict uses τ = 0.5, the primary attribution and the 37 primary
  rows only. No sensitivity view is used to reverse or support it.
- **Verdict metric.** The verdict is held-out log loss, weighted by battle and by campaign. Brier
  score and a count of the campaigns where each model does better are also reported, but are not
  part of the verdict.
- **Effective denominator.** The report counts the held-out rows in which at least one side's
  commander has a θ estimated from another campaign, and names those commanders. Other held-out
  rows can differ from the strength-only model only through α and β. Commanders whose modelled
  battles all fall in one campaign never affect a held-out prediction.
- **Reading an improvement.** An improvement is reported with its size and effective denominator.
  It is read only as "held-out log loss was lower on these rows". There is no threshold and no
  significance test. It is not evidence of a persistent commander effect, and it is not proof of
  skill, because commanders are tied to armies, theaters and opponents (§8).
- **If there is no improvement** under both weightings:
  - the report states that commander identity adds no detectable predictive signal in these
    data;
  - the Markdown report gives no ordered ranking;
  - the JSON keeps θ, the intervals and the rank intervals, each labelled `no_heldout_signal`.
- **Temporal split.** A split trained on 1862 and predicting 1863 is reported descriptively
  beside the leave-one-campaign-out test, without a verdict.

## 6. Sensitivity views

Each view refits the model and reports its ratings beside the primary ones.

**Robustness views:**

- **Pooling strength.** τ = 0.25 and τ = 1.0.
- **Side offset.** α's prior standard deviation set to 3. This shows how much of each side's
  results moves between α and the θs.
- **Attribution grades.** Only sides whose attribution is grade A or B; other sides get no
  commander term.
- **Alternative candidates.** Each `responsibility_unresolved` or `joint_command` side is
  assigned to its other recorded candidate.
- **Superior directing.** Sides labelled `superior_directing` use the named superior.
- **Command changes.**
  - (i) Rows labelled `command_changed` excluded.
  - (ii) The successor credited instead.
- **Strength endpoints.** The four endpoint refits (US low or high × Confederate low or high), as
  in the evaluation.

**Outcome-only views.** Both have no force-ratio term (β = 0) and are labelled
`includes_force_size_advantage`:

- (i) on the 37 primary rows, which isolates the effect of dropping the force term;
- (ii) on all 91 decisive engagements with attribution, after rule 7. This also changes the rows,
  and is labelled `expanded_rows`.

These views credit force concentration, and also every other advantage the commander did not
create.

**`view_sensitive`.** A commander with at least 2 modelled battles is flagged if, in any
robustness view:

- their 80% interval lies entirely on the opposite side of zero from their primary posterior
  mode; or
- their 80% rank interval does not overlap their primary 80% rank interval.

The outcome-only views estimate a different quantity. They are reported beside the primary
ratings with their differences, and they do not set `view_sensitive`.

## 7. Outputs and records

`artifacts/commander-ratings.json` and `.md` give, per commander:

- battles attributed and battles modelled, with wins and losses in the model;
- the sum over modelled battles of the outcome minus p, oriented to the commander's side. Here p
  is the held-out `diagnostic_union_score` of the A–C strength-only fit in
  `artifacts/estimate-evaluation.json`;
- the posterior mode θ (the mean of the Laplace approximation), the ratio of posterior to prior
  standard deviation, the 80% and 95% intervals, and the within-side rank interval;
- the echelon and component, the attribution grade mix, labels, and results in every view.

The outputs also include a research memo interpreting the results against the §5 test.

**Gate.** The command `commander-ratings` refuses to run unless:

- the responsibility ledger's review is reconciled; and
- an owner authorization record names the hashes of both ledgers, as for the evaluation.

Its outputs never enter `artifacts/baseline.json`.

**Reviews.** A separate Opus review covers this design, then the responsibility ledger in campaign
batches, then the model code and results.

## 8. Limits and non-goals

- **Not causal.** The rating is not command skill. Commanders are not randomly assigned to armies,
  theaters, opponents or odds.
- **Side-relative.** The Union intercept α absorbs nearly all of any side-wide difference,
  including any real difference between the two sides' average commanders. Ratings are relative to
  one's own side. Within-side differences still absorb army, theater and opponent differences.
- **Few battles, weak connections.** Fewer than a dozen commanders are expected to have two or more
  modelled battles: a provisional listing-based attribution gives 8, and the ledger will give the
  count. Many are not connected through shared opponents. Most ratings will sit near zero with
  wide intervals, and that is the correct result.
- **Selection.** Which battles have usable strengths may depend on the outcome, size and fame.
  Every result carries `whole_engagement_leakage` and `conditional_on_source_availability`.
- **Attribution is not blind.** The ledger's extractor and reviewers are AI systems that may know
  outcomes and reputations. Rules 2–5 are mechanical where possible. Judging a contradiction
  (rule 2), choosing a passage (rule 3(a)) and applying rule 5 are still judgments. The grade A–B
  view is the structural check, not proof.
- **Mixed echelons.** The target names army commanders in some rows and corps, brigade or
  detachment commanders in others, all pooled with one τ. For example, VA016 lists Fitz John
  Porter against Lee. The ledger records each echelon, and the report gives it.
- **Not Milestone 3.** There is no causal graph, no army, opponent or campaign effect, no locked
  final test set and no temporal verdict. This exploratory diagnostic does not meet Milestone 3's
  acceptance.
- **Truncated careers.** The pilot covers only 127 of the 384 source-listed engagements
  (1862–1863, Eastern and Western). The Overland, Atlanta and other 1864–65 campaigns, the
  Trans-Mississippi and 1861 are absent. A Civil War ranking needs the full frame researched to the
  same standard first. That is an owner decision about scope (§9).
- **No reputation check.** A familiar-looking list is not evidence of correctness, and an
  unfamiliar one is not evidence of error.
- **Also excluded.** There is no battle and campaign double counting, no double counting of nested
  records (rule 7), no cross-era comparison and no imputation of commanders.

## 9. Next decisions after this pilot

- **Extend the cohort to the full war.** That is 257 more engagements, researched in campaign
  batches to the first-pass standard, with strength and responsibility ledgers.
- **Campaign contribution** (methodology output 3). This needs coded campaign objectives, and is
  a separate design.
- **Methods for sparser eras.** The owner expects far thinner evidence for earlier wars. The graded
  best estimates, grade-D handling and pooling here are meant to degrade gracefully to that case:
  with less evidence, ratings move towards zero, with wider intervals.
