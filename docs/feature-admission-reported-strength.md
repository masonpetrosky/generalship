# Reported side-strength profile, design v1 (proposed)

**Status: a proposal awaiting separate review.** It does not amend, relax or replace
the [feature-admission contract](feature-admission.md) or its
`opening_available_combatants_v1` profile. Nothing here is implemented. It does not
authorize model inputs, an enriched fit or a commander score. Implementation, source
research and any release are later steps, each with its own review.

On 2026-09-25 the owner chose to add this coarser second-tier profile. Under the strict
opening profile, first-pass evidence cannot yield rows at a feasible research depth.

## 1. Why a second tier

- **The frozen pilot is mostly unusable as it stands.** It has 127 engagements.
  - 91 have a decisive recorded result and are not aggregate operations.
  - Only 23 of those have numeric strengths for both sides (the current baseline).
  - 63 have none, and 5 have one side only.
  - 36 inconclusive or aggregate records can never be rows for this target.
- **The first passes don't supply opening strengths.** They leave opening personnel
  unknown in 113 of 127 dossiers.
- **Even Shiloh doesn't.** After repeated boundary research it has zero eligible
  opening candidates.

The existing baseline already uses a coarser measure: CWSAC's whole-engagement
`source_reported_forces_engaged`. This profile formalizes that **measure class** so
enriched values can be added under review. It is not a new or better measure of opening
strength.

## 2. Profile definition

| Field | Value |
| --- | --- |
| ID | `reported_side_strength_v1` (tier 2) |
| Use | `retrospective_whole_engagement_strength_diagnostic` |
| Target | `recorded_decisive_union_outcome` (the baseline's outcome channel) |
| Field and unit | `reported_side_strength`, people |
| Interval | The frozen record's engagement interval |
| Uncertainty | Preserve bounds; no imputation, midpoint or weights beyond the existing baseline's midpoint rule, which applies only in a later locked evaluation |

**Population.** The whole force of one side that a source reports as engaged, present,
effective or present for duty *for this engagement*. The quantity basis is retained
exactly (`reported_engaged`, `reported_effective`, `reported_present`,
`present_for_duty`).

**Known weakness, stated wherever results appear.** An engaged or whole-engagement
total can reflect how the battle developed. Reinforcements get committed, and some units
never reach action. The measure therefore carries partial outcome leakage, which the
opening profile forbids.

Tier-2 results are diagnostics. They must never be:

- labelled opening strength, win probability or command effect;
- pooled or averaged with tier-1 rows;
- allocated to listed commanders.

## 3. Candidate applicability

An observation is technically applicable only when **all** of these hold. Each failure
keeps the observation in the evidence and ledger with its reason.

1. **Whole-side scope.** The source presents the figure as the strength of that side's
   force in this engagement: the army, command or all troops engaged. A named part (a
   brigade, an assault column, one wing, the infantry alone) is `excluded:
   partial_scope`. The exception is a source that states that part was the side's
   entire force present.
2. **Engagement match.** The source ties the figure to this engagement, or to an
   interval it states contains it with the same force. Figures for another action, the
   campaign as a whole, or an unlinked return date are `excluded: other_engagement`
   when known and `blocked: engagement_link_unknown` when uncertain.
3. **Source role.** Admissible roles:
   - the side's own report or return;
   - a compiled or secondary total with a stated or table-level basis (for example,
     the NPS/CWSAC tables or a numbers-and-losses compilation).

   An opponent's estimate, prisoner or citizen hearsay, and "said to be" figures relayed
   without the author's endorsement are `excluded: adversary_or_hearsay_estimate` in v1.
   Own-side reports also carry a known bias. The role is recorded, never corrected.
4. **Printed value.**
   - Bounds are preserved: "about", "over", "nearly" and ranges are recorded as printed,
     with the estimation status.
   - OCR readings are reported, not silently corrected.
   - Unreadable figures are `blocked: unreadable_value`.
5. **Derivation.**
   - Our own arithmetic follows contract §5: disjoint whole components with the same
     basis and time for sums, nested sets for subtraction. Otherwise the transform is
     `blocked` or `excluded`.
   - Opening or engaged strength reconstructed from losses, survivors or casualties, by
     us or visibly by the source, is `excluded: derived_from_losses`.
   - An unknown source derivation is allowed but labelled `derivation_unknown`.

## 4. Rows, bases and alternatives

- **Both sides are required.** A row needs one applicable candidate per side for the same
  engagement. One side alone leaves the row incomplete, and it stays in the denominator.
- **Basis pairing.**
  - A row's two sides must share a basis class, as they do in a same-source compiled
    pair.
  - Mixed-basis pairs (for example, own-report `reported_effective` against compiled
    `reported_engaged`) may appear only in the declared `mixed_basis` scenario. They are
    reported separately.
- **Scenarios.** They follow contract §5, with one observation per engagement per
  scenario and no averaging or weights. Two orderings are fixed **now, before any
  values are extracted or scored**:
  - `compiled_first`: a same-source compiled pair if present, else an own-report pair;
  - `reports_first`: the reverse.

  Every applicable alternative must appear in at least one declared scenario, adding
  scenarios where a third alternative exists. All scenarios are reported; none is
  selected by score, outcome or reputation.
- **Frozen values.** The frozen CWSAC figures for the 23 existing rows stay the
  baseline's inputs. In this profile they are one compiled-source candidate among
  others, in the NPS/CWSAC family.

## 5. Review and release

Contract §§3 and 6 apply unchanged:

- immutable evidence snapshots and candidates bound by hash;
- gate order and statuses (`invalid`, `excluded`, `blocked`, `eligible_candidate`,
  `admitted`);
- a separate evidence-use review of an exact proposal;
- primary reconciliation and a release manifest.

`admitted` is release-scoped. Zero rows is a valid result.

The evidence-use review scope for this profile is: whole-side scope, engagement match,
source role, printed value and bounds, derivation, source dependence, basis pairing and
scenarios. A dossier's `supported` status, or its first-pass review, approves no
candidate.

## 6. Evaluation plan, locked before any fitting

- Keep the existing model: the baseline's regularized logistic regression on relative
  strength. No new predictors.
- Whole-campaign holdouts, with train-only equal-odds and prior comparators.
- Report separately:
  1. **Common rows.** On engagements with both a frozen baseline row and a tier-2 row,
     frozen against tier-2 values with the same folds.
  2. **Expanded coverage.** All complete tier-2 rows against equal odds and the prior.
  3. **Each scenario.** No best-scenario selection.
- Retain the 23-engagement, 13-group reference (Brier 0.2768816348133779 against 0.25).
  Never claim improvement by comparing different populations.

## 7. Research authorized after this design is accepted

One targeted strength follow-up per engagement for the decisive records lacking a
complete numeric pair:

- reuse first-pass citations already in the dossiers;
- add **one** compiled source family covering many engagements (the candidate is
  Livermore, *Numbers and Losses in the Civil War in America*, 1901, pinned as OCR);
- add at most one further family for an engagement with no both-side figure.

This is a bounded extraction pass, not boundary research. The record for each
engagement is either candidate figures for both sides or an explicit null with its
reason.

The expected yield is limited. Compiled tables mainly cover major battles, so many
small cavalry and garrison actions will stay null. Inconclusive and aggregate records
stay in the ledger but are never rows.

## 8. Implementation notes, for a later reviewed change

- **Validator.** `admission.py` must accept this profile separately from
  `opening_available_combatants_v1`:
  - an engagement-interval boundary object instead of a contact boundary;
  - a `source_role` field in candidate mappings;
  - basis handling in which `reported_engaged` is applicable here but still excluded
    under the opening profile.
- **Dossiers.** First-pass dossiers are schema v1 without typed quantities. Candidates
  need schema v3 quantities, added as versioned dossier revisions with archived
  predecessors, and a new immutable evidence snapshot.

## 9. Non-goals

- No opening-strength claims.
- No commander scores or residual allocation.
- No campaign contribution.
- No relaxing of the opening profile.
- No imputation of missing sides.
- No outcome- or reputation-based choice among sources.
