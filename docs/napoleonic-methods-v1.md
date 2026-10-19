# Napoleonic methods checkpoint v1

Status: primary-verified design, 2026-10-18. The owner authorized this checkpoint and the
workflow changes after the project assessment, and kept the no-subagents policy for calibration.
The exact messages are in `data/napoleonic/methods-v1/owner-decision.json`.

This design is committed before running its synthetic experiments. It admits no feature,
fits no historical outcome, and changes no frozen frame, dossier, ledger or rating run.
Its outputs are a feasibility report, evaluation partitions, a worked campaign specification,
reproducible research screens and an unscored calibration sample. The checkpoint ends there;
it does not start another historical deep dive or a rating run.

## 1. What campaign contribution would mean

The unit is a command appointment over a specified operational window, not a battle or a
printed commander appearance. Let Y be a vector of observed campaign results: achievement
of objectives documented before the decisions being assessed, elapsed time, resources used,
and useful force preserved. Keep these components separate; no utility weights or scalar
"campaign wins" are supplied by this design.

The intended contrast is the expected difference in Y between retaining the incumbent and
replacing that person at t0 with a draw from an explicitly documented eligible appointment
pool, under the same authority and inherited state. The pool must be fixed from information
available at t0, including rank, availability, jurisdiction and political constraints, before
looking at results. An average fitted commander is not that pool. Other commanders' reactions,
subordinates and subsequent force concentration may change under replacement.

For each appointment the record must specify:

- t0, its evidence or clearly labelled analytical convention, and the command scope being replaced;
- t1 and an endpoint rule fixed without looking at whether the commander succeeded;
- the eligible replacement pool, its inclusion rules and missingness;
- assigned objectives and inherited resources/information, with their population and timing;
- subsequent decisions, resource changes, withdrawals and opportunities that led to no battle;
- an outcome vector, source alternatives, and an account of which elements were observed;
- a causal diagram and a separate identification argument, including assignment and interference.

The diagram is: inherited conditions and appointment constraints -> appointment and results;
appointment -> decisions -> concentration/supply/posture -> results. At battle onset those
same conditions may be inherited. A campaign analysis must not adjust away all preparation
as though it preceded appointment. A battle residual is never added to the campaign vector.

### Worked specification: the 1805 group

The worked record is `data/napoleonic/methods-v1/campaign-pilot.json`. It uses only registered
passages already inspected for the 1805 group. That source group combines German, Italian,
Tyrolean and other operations; it is a research/evaluation group, not automatically one
appointment or one coherent objective. The pilot tests the proposed French command in the
German operations. It records the evidenced local directives and overlapping command roles,
and leaves campaign-onset t0, t1, inherited totals, replacement eligibility and campaign-result
components null where the inspected material does not establish them. An engagement's date
does not supply the campaign replacement date. An order to take a place does not prove that
the campaign achieved its prior objective.

This is a completed measurement-feasibility example with an explicit not-estimable result,
not a historical contribution estimate. It identifies the precise missing inputs that a
later bounded campaign study would need; no follow-up fetching is part of this checkpoint.

## 2. Schedule audit without fitting recorded outcomes

Use all 325 cohort IDs and the frozen war/year groups. To put printed commanders on side A
or B, the importer necessarily reads Bodart's winner/loser orientation and `french_side`.
It then discards that orientation. The analysis reads neither recorded outcomes nor printed
strengths/losses and supplies no real y to a fit. Historical facts and the frame have already
been seen; this is not human or model blinding to history.

Use conservative printed-label keys: Unicode case folding and punctuation/spacing
normalization only. Do not strip titles, merge aliases, split joint commands into credited
people, or infer identities by reputation. Missing and joint/complex labels remain visible.
The audit reports literal-label counts, opponent components, cross-group recurrence, held-out
availability and exact exclusions. These are provisional schedule diagnostics, not resolved
commander identities or responsibility assignments. A second view uses only rows with two
unambiguous printed labels; its denominator is explicit.

The campaign pilot records a few source-backed role/formation observations. It does not
equate a corps with an army or assert continuity from a repeated formation name. Without a
verified cross-engagement army registry, actual commander-versus-army rank and crossover
identification are **not assessed**. The report must retain this result even if the opponent
graph is connected.

## 3. Synthetic recovery experiments

The exact seed, repetitions and parameters are frozen in `methods-v1/protocol.json`.
Run 100 full-sample recoveries and 20 validation repetitions per scenario on the usable
printed-label schedule. This is a reduced logistic diagnostic of the additive commander
family: intercept, a synthetic force covariate and signed commander terms with fixed
normal prior SD 0.6. It does not estimate tau or reproduce every view of Civil War run 4.
The sparse solver must agree with that run's solver on small constructed data before release.

Five data-generating scenarios are fixed before execution:

1. Null: no commander or army effects, correctly observed synthetic force.
2. Commander: independent commander SD 0.6, with a group shock SD 0.35.
3. Stable army alias: no commander effect; each label permanently carries a hypothetical army
   effect SD 0.8, with group shocks. The army and commander columns are identical. No amount
   of opponent connectivity can separate those columns from these observations alone.
4. Switching armies: commander SD 0.6 and hypothetical army SD 0.8, assigned to eight pools
   per side with assignments rotating by group. Also fit the version observing those synthetic
   army labels. These invented assignments are sensitivity scenarios, never historical inputs.
5. Source bias: no commander or army effects; the observed synthetic force covariate has a
   persistent label-associated measurement bias SD 0.4. Outcomes use the unbiased force.

Generate true force from Uniform(-0.5, 0.5) and use coefficient 1.0. No historical personnel
figures enter this experiment. Independent random streams give each scenario/repetition its
own draws. Report all scenarios, successful or not; do not tune parameters after execution.

Report centered commander RMSE, recovery slope/correlation where true spread is nonzero,
and estimated commander spread under the null/army/bias cases. Report summaries over
repetitions, not a single favorable run. Report held-out log-loss differences against force
only and a training-only smoothed prior, under battle and equal-group weighting. Compare
leave-war-year-out, leave-entire-war-out and forward-time tests, with their distinct row
denominators. There is no historical ranking, causal test or pass/fail skill verdict.
Successful simulated recovery establishes behavior only under the supplied assumptions.

## 4. Evaluation decisions fixed before a Napoleonic outcome fit

`methods-v1/evaluation.json` binds exact IDs, groups and input hashes. No group is removed
from the cohort or silently split.

- **Development:** 1805–1813, all 273 entries in 13 groups. Main development evaluation leaves
  one frozen group out. Declare the candidate set and selection algorithm before the first
  development outcome fit. Any selection used for reported outer-fold performance must occur
  within that fold's training rows. Scores reused to choose a candidate are exploratory;
  their bootstrap does not become a fresh confirmatory test. Select the final locked candidate
  using development rows only.
- **Final evaluation reserved now:** all 52 entries of 1814–1815 in three complete groups.
  No fitting or model selection on their historical outcomes before the final predictions
  and exact code/input authorization are locked. Frame transcription and historical familiarity
  already exposed these events; "reserved" means unused for numerical model selection from
  this checkpoint, not historically blind or inaccessible to the author.
- **Dependence sensitivities:** leave entire wars out on development rows, and forward-time
  development (train through 1812, predict 1813). Report the changed prediction target and
  denominators. These coarser views preserve the frame and the original groups.
- **Comparators:** force only, context without commanders, training-only Laplace-smoothed
  prior and equal odds. Fix context terms and priors before any development outcome fit.
- **Development predictive rule:** the commander candidate must lower held-out log loss
  relative to every comparator, with the campaign-bootstrap one-sided 95% bound below zero
  under both weightings. Publish every comparison, calibration and concentration result.
  A weak context comparator cannot substitute for beating the simpler benchmarks.
- **Final report:** evaluate the one locked candidate once, against every comparator under
  both weightings. Three groups provide little replication. Report per-group results and
  sensitivity, and do not manufacture a decisive significance claim from a three-cluster
  bootstrap. A predictive success is not a causal validation or a ranking of skill.

The reserved final set is a deliberately limited future check, not a replacement for
development diagnostics. A revision after seeing its scores must label them reused rather
than untouched. A full rating design, resolved ledgers, priors/context profile and exact
owner authorization are still required before any historical outcome is fitted. This
checkpoint does not authorize that future run. No predictive gate by itself establishes
or is a universal prerequisite for a causal effect; the causal estimand has its own design.

## 5. Research throughput and quality

Brief v3 turns "researched fully" into a field checklist and stopping rule. Future passes
record source-specific strength population/time, scope of command, missing army continuity,
the decisive dispute, and the decision a follow-up could change. Existing evidence remains
immutable. A first pass can end with unknowns and alternatives. It need not resolve every
subordinate's movement or reproduce the whole source narrative.

Packets default to a compact group index: entry text, frame fields, draft paths/hashes and
only relevant source references. A per-entry command loads a selected draft; `--full` is an
explicit compatibility view. The source archive remains complete. Packet length is a
navigation measure, not evidence quality.

The research screen retains executable checks for source-family ceilings, locator sections,
and digit provenance. Numeric matches are triage: an unrelated matching number does not
establish support; spelled-out quantities, arithmetic, OCR and interpretation still require
inspection. Historical warnings are retained, not silently rewritten or treated as new
failures. The screen is reproducible and its findings feed primary verification.

Calibration uses a frozen stratified sample: eight strength, eight responsibility, eight
posture/fortification and eight other known claims, plus every explicit unknown in the 49
checkpoint drafts. Draw with seed 20261018 from sorted (battle ID, claim ID). Add an
eight-citation translation subsample drawn from the known sample. Store dossier and source
hashes, opaque sample IDs and blank judgments; exclude author rationale and translations
from the first reading view. Known claims are assessed against their passages; unknowns
require a bounded search of already inspected source sections. The latter cannot prove a
whole literature is silent. Publish stratum denominators; never report an unweighted pooled
error rate as representative of the corpus.

No reviewer is launched. The owner explicitly kept the single-session policy and requested
preparation only. The sample is unscored, not an independent review or an error-rate estimate.
Any later calibration writes a separate, versioned judgment record bound to the sample IDs;
it does not fill or overwrite the generated blank sample or public key.
There is no second-opinion prompt workflow.

## 6. Reproduction and limits

`make napoleonic-methods` explicitly runs the synthetic job. Tests use only small constructed
cases; tests and `make reproduce` do not run the experiment. The stored result binds the
design, protocol, frame, cohort, pilot, source snapshots and executed code. `make reproduce`
regenerates the report from the stored result and the research/evaluation/calibration
artifacts offline. `make check` verifies their bindings, partitions and contracts.

The checkpoint is primary-verified. It cannot establish historical truth, the adequacy of
Bodart's selected frame, cross-engagement army continuity or causal identification. Failed
recovery, poor held-out results and missing pilot fields remain reportable results.

Methodological reference: Gelman et al., [Bayesian Workflow, section 4.1](https://arxiv.org/html/2011.01808v1#S4.SS1),
on recovery experiments with known parameters and the limits of a single simulation.
