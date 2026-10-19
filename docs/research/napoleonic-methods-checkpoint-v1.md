# Napoleonic methods checkpoint: results and handoff

Completed 2026-10-18. Primary-verified; no separate review. The owner kept the single-session
policy and requested calibration preparation only. No second-opinion prompt was produced as
part of the implementation.

The design and code were committed and pushed in `18262defc140e2796df677bb6639f73a7b06ea6d`
before the synthetic job ran. All 17 result bindings match that commit. The
[execution receipt](../../data/napoleonic/methods-v1/execution.json) binds the complete result
and saved run log. Parameters and scenarios were not changed after seeing their results.

## What the checkpoint established

The [worked 1805 specification](../../data/napoleonic/methods-v1/campaign-pilot.json) is not
estimable from its inspected passages. It records local directives and overlapping authority,
but cannot supply campaign-onset boundaries, eligible alternatives, inherited resource totals,
the contemporary information set or a complete objective/outcome vector. These remain null.
The study group is also not automatically one coherent command appointment. This is a
measurement gap, not a reason to invent an average replacement commander or add battle wins
into a campaign score.

The frozen 325-entry schedule yields 375 conservative printed-label keys, 75 recurring and
42 occurring in more than one group. Missing or joint/complex labels exclude 28 entries from
simulation, leaving **297 entries and 357 labels**. All excluded entries remain in the cohort
denominator. Only 41 of 325 entries have both labels represented in another group. Titles and
aliases have deliberately not been merged. These figures cannot be read as counts of actual
people or as a verdict that the historically resolved schedule is disconnected.

There is no verified cross-engagement army registry in this checkpoint: **0 of 650 side slots**
has an admitted historical army identity. The pilot's authority observations are not army
continuity. Actual commander–army identification is therefore not assessed.

## Synthetic findings, including unsuccessful cases

The [generated report](../../artifacts/napoleonic-methods-v1.md) and
[full result](../../artifacts/napoleonic-methods-v1.json) retain all five scenarios, each with
100 recovery repetitions and 20 validation repetitions. These are invented outcomes, forces
and army assignments on a provisional label schedule. The fixed-tau diagnostic is a reduced
member of the existing logistic family, not the complete run-4 selection procedure.

| Scenario | True commander SD | Mean recovery correlation | Mean commander-minus-force log loss, battle weighted, leave-war-year-out |
| --- | ---: | ---: | ---: |
| Null | 0 | undefined | +0.0059 |
| Commander effect | 0.6 | 0.2954 | −0.0055 |
| Stable army effect only | 0 | undefined | −0.0136 |
| Commander plus switching armies | 0.6 | 0.2504 | −0.0012 |
| Biased force measurement | 0 | undefined | +0.0083 |

- **Predictive improvement does not distinguish army advantage from commander contribution.**
  In the stable-army case the model improves even though every true commander effect is zero.
  Permanent army and commander columns are identical. Supplying both columns changes the
  prior-driven allocation, not their structural identifiability.
- **Known commander differences were weakly recovered on this schedule.** Mean centered RMSE
  is 0.5711 for true SD 0.6, correlation 0.2954 and slope 0.0884. Shrinkage, sparse observations,
  conservative alias splitting and prior-dependent component/side offsets matter. This is
  not evidence that historical commanders lacked differences or that the final resolved
  registry will behave the same way.
- **Adding army terms is not an automatic remedy.** In the invented switching case, observing
  the synthetic army labels moves commander RMSE only from 0.5846 to 0.5811. Its forward-time
  commander-minus-force difference is +0.0015 battle weighted and +0.0070 by equal frozen group.
- **The source-bias case did not produce a helpful commander term.** Its held-out loss is
  worse than force only under all three validation strategies. This failed case is retained;
  it is not evidence that source bias is harmless under other measurement processes.

Validation denominators need care. War-year and whole-war validation both score 297 rows in
16 frozen war/year groups; the latter fits seven whole-war holdouts, while the equal-group
score still weights the frozen war/year groups equally. Forward-time validation scores
107 rows in five frozen groups. Its test population differs, so strategy scores are not a
paired competition on identical rows. The JSON's repetition ranges are not historical
confidence intervals. No scenario supplies a causal validation or historical ranking.

## Changes now in use

- Evaluation partitions are fixed at 273 development entries through 1813 and 52 reserved
  final entries of 1814–1815, in three intact final groups. Historical events have already
  been seen; the reservation is for future numerical model selection. The design requires
  within-training-fold selection for reported development performance, simple comparators,
  broader-war/temporal sensitivities, and restrained interpretation of the three-group final.
- Brief v3 makes each new first pass record per-side strength population/time and authority,
  unresolved army continuity, any additional sources checked, the decision a single targeted
  follow-up could change, and an explicit stopping reason. Existing drafts retain their old
  contracts. Do not treat every open question as another research assignment.
- Compact packets retain entry text and source/draft paths and hashes. `--battle-id` loads a
  single draft; `--full` explicitly restores the full view. The 1806 packet fell from 5,217,415
  to 224,233 bytes, about 95.7%, without deleting the source archive or dossier content.
- The reproducible screen retains 75 digit triage flags and one legacy four-root family flag.
  Its matching logic cannot adjudicate arithmetic, elliptical numbers or source independence.
  The bounded inspection and partial source dependence are documented in the research log.
  These warnings are not an estimated historical error rate and are not silently cleared.
- Calibration is a frozen, **unscored 47-task sample**, including all 15 unknowns and an
  eight-passage translation subsample. The separate public key makes blinding procedural.
  No reviewer or judgments exist. A later calibration requires a new versioned judgment
  record; it must not overwrite the generated blank sample.

## Stop and next step

This checkpoint is complete. It does not authorize a historical rating fit or feature
admission. Preserve the frozen inputs and code, the unhelpful results and the pilot's nulls.

The next research group remains `fourth-coalition 1807` (19 entries), using the new brief.
Use its command-scope field to retain source-backed identities and aliases where encountered,
and keep unestablished army continuity explicit. Resolve a responsibility/identity ledger and
the army/appointment design before any historical rating run; adding more printed labels is
not that resolution. A campaign contribution study additionally needs a separately bounded
appointment/objective investigation, including opportunities that produced no listed battle.
