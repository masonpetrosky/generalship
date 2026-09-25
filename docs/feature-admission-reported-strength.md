# Reported side-strength profile, design v1 (proposed)

**Status: a proposal awaiting separate review.** It does not change the text or hash of
the [feature-admission contract](feature-admission.md) or its
`opening_available_combatants_v1` profile. It adds a second, separately reviewed use under
that contract's §§3, 5 and 6. Its departures from §4, which is written for pre-engagement
prediction, are declared in §2 and apply to this profile only.

Nothing here is implemented. It does not authorize model inputs, an enriched fit or a
commander score. Implementation, source research and any release are later steps, each
with its own review.

**Revision.** This text incorporates the required corrections R1–R9 and advisories A1–A4
and A6 from the first separate
[design review](../artifacts/review-results/reported-strength-design-e335b75-opus-high-v1/review.md)
of prepared commit `e335b75`. A5 keeps the source-ID tiebreak; see §4. A focused
follow-up review checks the corrections.

On 2026-09-25 the owner chose to add this coarser second-tier profile. Under the strict
opening profile, first-pass evidence cannot yield rows at a feasible research depth.

## 1. Why a second tier

- **The frozen pilot is mostly unusable as it stands.** It has 127 engagements.
  - 91 have a decisive recorded result and are not aggregate operations.
  - Only 23 of those have numeric strengths for both sides (the current baseline).
  - 63 have none, and 5 have one side only.
  - 36 inconclusive or aggregate records can never be rows for this target.
- **The first passes don't supply opening strengths.** Opening personnel is recorded as
  unknown in at least 124 of 127 dossiers: 113 under `opening-personnel-unknown` and 11
  under other claim IDs.
- **Even Shiloh doesn't.** After repeated boundary research it has zero eligible
  opening candidates.

The existing baseline already uses a coarser measure: CWSAC's whole-engagement
`source_reported_forces_engaged`. This profile defines a coarser, reported whole-side
measure that **includes** the baseline's forces-engaged class, so that enriched values can
be added under review. It is not a new or better measure of opening strength.

## 2. Profile definition

| Field | Value |
| --- | --- |
| ID | `reported_side_strength_v1` (tier 2) |
| Use | `retrospective_whole_engagement_strength_diagnostic` |
| Target | `recorded_decisive_union_outcome` (the baseline's outcome channel) |
| Field and unit | `reported_side_strength`, people |
| Interval | The frozen record's engagement interval |
| Uncertainty | Preserve bounds; no imputation or weights. The only point value is §6's midpoint, used only in a locked evaluation. One-sided bounds form no scored row. |

**Population.** The whole force of one side that a source reports as engaged, present,
effective or present for duty *for this engagement*. The quantity basis is retained
exactly (`reported_engaged`, `reported_effective`, `reported_present`,
`present_for_duty`).

**Known weakness, stated wherever results appear.** An engaged or whole-engagement
total can reflect how the battle developed. Reinforcements get committed, and some units
never reach action. The measure therefore carries partial outcome leakage, which the
opening profile forbids. The frozen Shiloh US figure, for example, combines the Army of
the Ohio, which arrived during the engagement.

Which engagements obtain figures may itself depend on the outcome, on size and on fame,
because sides and compilers chose what to report. Results are conditional on source
availability and do not represent the 91 decisive engagements.

Tier-2 results are diagnostics. They must never be:

- labelled opening strength, win probability or command effect;
- pooled or averaged with tier-1 rows;
- allocated to listed commanders.

**Relationship to contract §4 (this profile only).**

- Every candidate records §4's five time distinctions unchanged. These are the state
  interval, the document date and its role, publication and access dates, receipt
  (null), and this profile's engagement interval and research cutoff.
- Participation and arrivals *within* the engagement interval are accepted under the
  declared partial-leakage label. They are never relabelled as opening data.
- Excluded unchanged, with transitive dependency checks:
  - casualties;
  - survivors;
  - post-engagement returns (§3 item 2);
  - outcome narratives and outcome claims;
  - loss-based reconstructions (§3 item 5).
- §4's rule that an unknown derivation that may depend on the outcome blocks admission is
  replaced here by the `derivation_unknown` label. This is a declared tier-2 relaxation:
  an undisclosed loss-based reconstruction cannot be ruled out for such a figure. Results
  report, per scenario, how many rows rest on `derivation_unknown` observations.
- §4's outcome-, reputation- and score-blind selection rules apply unchanged.

## 3. Candidate applicability

An observation is technically applicable only when **all** of these hold. Each failure
keeps the observation in the evidence and ledger with its reason.

1. **Whole-side scope.** The source presents the figure as the strength of that side's
   whole force for this engagement, on its stated basis. Any of these qualifies:
   - an army or command;
   - "all troops engaged";
   - a side-level table entry whose basis is the side's forces engaged, such as a CWSAC
     forces row, even when it names the formations composing that force.

   A figure that the source, or another cited passage, presents as one part of that
   side's force is `excluded: partial_scope`. Examples are a brigade, an assault column,
   one wing or the infantry alone. When the cited passages do not settle whether a named
   formation was the side's whole force on that basis, the figure is `blocked:
   scope_unresolved`. A side-level engaged entry satisfies scope on the engaged basis
   only. It does not establish the side's present or effective strength.
2. **Engagement match and state time.**
   - The source ties the figure to this engagement: the side's force engaged in it, or a
     return or estimate that the source states describes the force brought to it.
   - A figure for another action or for the campaign as a whole is `excluded:
     other_engagement`.
   - A figure whose link to this engagement is uncertain is `blocked:
     engagement_link_unknown`. This includes a return with an unstated muster date and a
     return that the source does not tie to this engagement.
   - A return or estimate whose state date falls after the frozen record's start date is
     `excluded: post_engagement_state`. It describes the force after contact began, and a
     later document date alone does not trigger this. The exception is a return the source
     states describes the force at an earlier date; that earlier date is then its state
     date.
   - A figure the source limits to part of a multi-day engagement interval (one day or
     phase) is `excluded: partial_interval`. When that is unclear, it is `blocked:
     interval_unresolved`.
3. **Source role.** Admissible roles:
   - the side's own report or return;
   - a compiled or secondary total with a stated or table-level basis (for example,
     the NPS/CWSAC tables or a numbers-and-losses compilation).

   An opponent's estimate, prisoner or citizen hearsay, and "said to be" figures relayed
   without the author's endorsement are `excluded: adversary_or_hearsay_estimate` in v1.
   - A compiled figure whose cited basis is visibly one side's report or an opponent's
     estimate takes that underlying role.
   - A secondary total with neither a stated nor a table-level basis is `blocked:
     basis_unknown`.
   - When the cited passages do not settle the role, the figure is `blocked:
     source_role_unresolved`. An example is whether a compiler adopts or only relays a
     figure.

   Own-side reports also carry a known bias. The role is recorded, never corrected.
4. **Printed value.**
   - Bounds are preserved: "about", "over", "nearly" and ranges are recorded as printed,
     with the estimation status.
   - OCR readings are reported, not silently corrected.
   - Unreadable figures are `blocked: unreadable_value`.
   - A one-sided printed bound ("over", "nearly", "at least") is `blocked:
     one_sided_bound` in v1 (§6, §8).
5. **Derivation.**
   - Our own arithmetic follows contract §5: disjoint whole components with the same
     basis and time for sums, nested sets for subtraction. Otherwise the transform is
     `blocked` or `excluded`.
   - "Same time" forbids our own sum of an initial force and a force that arrived later.
     Our arithmetic must not add leakage beyond what sources print.
   - Opening or engaged strength reconstructed from losses, survivors or casualties, by
     us or visibly by the source, is `excluded: derived_from_losses`.
   - An unknown source derivation is labelled `derivation_unknown`, under the declared
     relaxation in §2.

## 4. Rows, bases and alternatives

- **Both sides are required.** A row needs one applicable candidate per side for the same
  engagement. One side alone leaves the row incomplete, and it stays in the denominator.
- **Basis pairing.** Each side's basis is the typed `basis` of its quantity. It is read
  from the cited passage or the table's stated definition; a shared source does not
  establish it. A same-basis pair has identical basis values. Every other pair is a
  mixed-basis pair, including one with an unknown basis on either side.
- **Candidate pairs.** An engagement's candidate pairs are every combination of one
  applicable US and one applicable Confederate observation that no declared compatibility
  constraint rules out (contract §5). A pair may combine sources and roles. It records
  both source IDs, roles and bases. Compatibility constraints, if any, must be declared
  before extraction.
- **Pair ranking.** Fixed now, before any values are extracted or scored.
  - Pair classes are: (a) both sides from one compiled source; (b) both sides' own
    reports; (c) any other combination.
  - Within a class, pairs are ordered by source ID, then quantity ID, in ascending
    code-point order. This tiebreak is arbitrary but outcome-blind.
  - Order A is (a), (b), (c). Order B is (b), (a), (c).
- **Scenarios.** Each scenario is a full dataset with at most one pair per engagement,
  no averaging and no weights. Engagements without a pair keep null sides. The declared
  scenarios are exactly:
  - `compiled_first`: each engagement's first same-basis pair under order A;
  - `reports_first`: its first same-basis pair under order B;
  - `alternate_k`, for k = 2 up to the largest number of same-basis pairs in any
    engagement: its k-th same-basis pair under order A, or its `compiled_first` pair
    when it has fewer;
  - `mixed_basis_k`, for k = 1 up to the largest number of mixed-basis pairs in any
    engagement: for each engagement with a mixed-basis pair, its k-th mixed-basis pair
    under order A, or its first when it has fewer; every other engagement takes its
    `compiled_first` pair.

  The validator checks that the declared scenarios equal those this rule generates.
  Every applicable pair therefore appears in at least one scenario. An engagement with
  many applicable observations can generate many `alternate_k` scenarios; the count is
  reported, not trimmed after extraction. All scenarios are reported with their own row
  counts. None is selected by score, outcome or reputation. Results from scenarios with
  different row sets are never compared as improvements.
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

The evidence-use review scope for this profile is: whole-side scope, engagement match and
state time, source role, printed value and bounds, derivation, source dependence, basis
pairing and scenarios. A dossier's `supported` status, or its first-pass review, approves
no candidate.

## 6. Evaluation plan, locked before any fitting

This plan authorizes no fit. A fit needs a verified tier-2 release manifest and an
explicit, recorded owner authorization (contract §7).

- **Model.** `strength-logistic-v1` unchanged:
  - ridge 1.0 logistic regression on (US − Confederate)/(US + Confederate);
  - leave-one-campaign-out over the campaigns present in the row set;
  - equal odds and the Laplace-smoothed, training-only prior as comparators.

  No new predictors. Tier-2 predictions are named as diagnostics (for example,
  `diagnostic_union_score`), not `p_union_win`.
- **Bounds.** A side's value is (lower + upper)/2, as in the baseline, with the
  baseline's four-endpoint sensitivity reported. An observation with a one-sided printed
  bound has no finite pair of bounds. It forms no scored row in v1 and stays in the ledger
  as `blocked: one_sided_bound`.
- **Evaluability.** A row set needs at least 6 rows from 3 campaigns, with both outcome
  classes. A set below this is reported as not evaluable, with its counts.
- **Reported separately for every scenario:**
  1. **Common rows.** These are engagements with both a frozen baseline row and a tier-2
     row. In each fold, both models are fit only on common training rows and scored on
     the same held-out rows.
  2. **Newly covered rows.** Tier-2 rows without a frozen baseline row, against equal
     odds and the prior.
  3. **All tier-2 rows.** Against equal odds and the prior, labelled as a population
     different from the 23-row baseline.

  Each report gives:
  - battle- and campaign-weighted Brier and log loss;
  - row and campaign counts;
  - the number of rows resting on `derivation_unknown`, mixed-basis or own-report
    observations.
- **Labels.** Every result carries `partial_outcome_leakage` and
  `conditional_on_source_availability`, together with the §2 statement.
- **Reference.** Retain the 23-engagement, 13-group baseline:
  - battle-weighted Brier 0.2768816348133779 against 0.25 for equal odds;
  - campaign-weighted Brier 0.2765271817053925 against 0.25.

  Also retain the 127-engagement, 36-group coverage ledger. Never claim improvement by
  comparing different populations or scenarios.

## 7. Research authorized after this design is accepted

This is bounded deeper work. It serves the tier-2 admission decision and follows the
owner's 2026-09-25 decision. It is not boundary research, and it stops at the limits
below.

- Reuse first-pass citations already in the dossiers.
- Add **one** compiled source family covering many engagements.
  - The candidate is Livermore, *Numbers and Losses in the Civil War in America* (1901).
  - It is not yet in the registry. Pin it with locators and hashes, as OCR, before
    extraction.
  - Extract it for all 91 decisive non-aggregate engagements, including the 23 with
    frozen pairs, so that extraction does not depend on baseline status.
- Add at most one further family for an engagement that still lacks an applicable figure
  for each side.

Each of the 91 engagements ends with either candidate figures for both sides or an
explicit null with its reason. Inconclusive and aggregate records stay in the ledger but
are never rows. Dependence between this compiled family and NPS/CWSAC is recorded as
unknown unless evidenced, and their agreement is not corroboration.

The yield is not known in advance. Compiled tables may favour larger actions, so many
small cavalry and garrison actions may stay null. Report the actual yield per campaign,
including zero.

## 8. Implementation notes, for a later reviewed change

The current validator accepts only the opening profile. Contract design v1 needs no text
change if the following items are implemented as a separate, versioned profile path.
`shiloh-opening-v1.json` and `-v2.json` must still validate unchanged.

- **Profile binding.** The tier-2 profile binds the contract hash and this design's
  accepted hash, with use `retrospective_whole_engagement_strength_diagnostic`.
- **Boundary.** An engagement-interval boundary (frozen record ID, start and end dates)
  replaces the contact, area and availability fields. It has one whole-side membership
  atom per side.
- **Mappings and codes.** A new proposal schema version adds `source_role` and the §3
  codes:
  `partial_scope`, `scope_unresolved`, `other_engagement`, `engagement_link_unknown`,
  `post_engagement_state`, `partial_interval`, `interval_unresolved`,
  `adversary_or_hearsay_estimate`, `source_role_unresolved`, `basis_unknown`,
  `unreadable_value`, `derived_from_losses`, `derivation_unknown`, `one_sided_bound`.
- **Profile-specific gate changes.** Under this profile only:
  - `reported_engaged` and the `participation` derivation are applicable;
  - `derivation: unknown` gives the `derivation_unknown` label;
  - `estimation_status: unknown` is retained and labelled.

  Neither of the last two is blocked.
- **Frozen CSV figures.** These need either typed schema v3 quantities citing the CWSAC
  row, or a separately reviewed CSV row/column leaf kind (contract §3). Candidates cannot
  reference them otherwise.
- **One-sided bounds.** Schema v3 cannot type a one-sided printed bound without inventing
  an endpoint. Until a reviewed schema change, such a figure stays a prose claim and is
  `blocked: one_sided_bound`.
- **Rows and scenarios.** Rows carry the profile ID and both bases. The validator checks
  the declared scenarios against the §4 generation rule.
- **Review scope.** The release audit needs a profile-specific scope set covering §5's
  eight items.
- **Dossiers.** 126 of 127 first-pass dossiers are schema v1 without typed quantities.
  Candidates need schema v3 quantities, added as versioned dossier revisions with
  archived predecessors, and a new immutable evidence snapshot.
- **Evaluation route.** No loader consumes rows. The §6 evaluation needs a separately
  reviewed, non-installing evaluation command.

If implementation shows that contract text must change, that is a contract revision
with its own review.

## 9. Non-goals

- No opening-strength claims.
- No commander scores or residual allocation.
- No campaign contribution.
- No relaxing of the opening profile.
- No imputation of missing sides.
- No outcome- or reputation-based choice among sources.
