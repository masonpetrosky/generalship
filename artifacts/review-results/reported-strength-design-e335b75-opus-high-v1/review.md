# Separate design review: `reported_side_strength_v1` (design v1, proposed)

## Record

| Field | Value |
| --- | --- |
| Reviewer | Claude agent, fresh-context subagent (not a fork of the author's conversation) |
| Model / effort | `claude-opus-5-5` (Claude Opus 5.5), reasoning effort `high` |
| Date | 2026-09-25 |
| Prepared commit reviewed | `e335b751e354bd2581eec5770b0fba7e200f6c0e` |
| Previous commit | `ff494b976d0d2dd124ad2c6b50304e016f3002f1` |
| Bundle commit (worktree HEAD) | `efeefb98374f470db0b59f70dd8d47a9992d2640` (adds only `assignment.md` and `inputs.json` over `e335b75`) |
| `assignment.md` sha256 | `c7158069206ddc8e8e623dac004bc9900eb2e1e3f0ccc61df8ef027e3bc02b6b` (verified) |
| `inputs.json` sha256 | `f92b3c690e499f6501518cd7c0b61e245b6f4a45dd77e67d5a2793143814451a` (verified) |
| Input hashes | All 19 paths in `inputs.json` match `git show e335b75:<path>` and the worktree bytes. **No mismatch.** |
| Outcome | **Corrections required** (R1–R9); advisories A1–A6 |

The assignment also required files that `inputs.json` does not bind. I read them at
`e335b75`, and none differs at the bundle HEAD. Their hashes:

- `docs/feature-admission.md` `b858b7a27f3617408779c928ea545da814b31229ff2c40caf64927773f320c99`. This equals `CONTRACT_SHA256` in `admission.py`, so the contract text is unchanged.
- `docs/admission-validator.md` `3aa7c1dfe192b13e10399030bd1f627ed73f9cec21382d9ed0a5e3eed0620e6c`
- `generalship/admission.py` `55927091b8f7fa4e6a1eaef8a3b57d54de341aff01dfc666eda678a360941993`
- `generalship/baseline.py` `f69156139eeb674e7a720a798bb235ddbec295944f048d83a68ba1593f53ceee`
- `generalship/evidence.py` `cf52c44b86956201cb6fa8c1a9c3cec85047ada71366f656330c551b536dee69`

This is an AI design review. It is a separate analysis, not human historical
adjudication, feature admission, approval of any candidate or proof of source
independence. It changes no evidence, no model input and no other file.

## Scope actually inspected

- **Read in full:**
  - `docs/feature-admission-reported-strength.md`
  - the `ff494b9..e335b75` diff (README, roadmap and design only)
  - `docs/feature-admission.md` (contract design v1)
  - `docs/admission-validator.md`
  - `generalship/baseline.py`
  - AGENTS.md
- **Read in part:**
  - `generalship/admission.py`: header, constants, `_snapshot`, `_mapping`, `_profile`, `_boundary`, `_status`, `_candidate` and `_scenarios`. I did not trace `validate_proposal`, `_coverage` or `audit_release` in detail.
  - `generalship/evidence.py`: the quantity validation and `QUANTITY_BASES`.
  - `docs/evidence-contract.md`: the quantities section.
  - README "Research direction".
  - Roadmap lines 1–30 and 366–400.
  - Methodology lines 1–80.
- **Searched only:**
  - `data/sources.json`, `docs/sources.md` and `data/evidence/` for Livermore / *Numbers and Losses*. There were no matches outside the design.
- **Recomputed from data:**
  - `artifacts/battles.json`, `data/pilot/cohort.json`, `data/raw/cwsac_battles.csv` and `data/raw/cwsac_forces.csv`.
  - `artifacts/baseline.json` metrics.
  - All 127 current `data/evidence/*.json` dossiers: claim IDs and statuses, schema versions and quantities. History files are excluded.
- **Not inspected:**
  - `generalship/cli.py`, `tests/test_evidence.py`, `artifacts/admission-check.json`, `data/admission/shiloh-opening-v{1,2}.json`, `data/raw/cwsac_commanders.csv`, the rest of `docs/sources.md` and the rest of `docs/methodology.md`. These are hash-verified only.
  - Any source passage. This design cites no historical passage, and I did no new research.
- **`make check`:** run offline. 82 tests passed (`OK`), and `generalship check` exited 0 with `artifacts_written: false`, admission statuses 18 blocked / 22 excluded and 0 promoted rows. The worktree was unchanged afterwards. I ran no build or packet command.

## Verified facts (question 6)

| Claim in design/roadmap | Recomputed | Result |
| --- | --- | --- |
| 127 engagements | 127 in `battles.json`, equal to cohort IDs; 36 campaign groups | ✔ |
| 91 decisive, non-aggregate | 91 (`result != Inconclusive`, `operation != 1`) | ✔ |
| 36 inconclusive or aggregate | 35 inconclusive + 1 aggregate operation, no overlap | ✔ |
| 23 with both numeric strengths | 23, both `battles.json` and CSV `strength_min/max` | ✔ |
| 5 one side, 63 none | 5 and 63 (sum 91) | ✔ |
| Roadmap "68 decisive engagements lacking a complete numeric pair" | 63 + 5 = 68 | ✔ |
| 23-engagement, 13-group reference, Brier 0.2768816348133779 vs 0.25 | `baseline.json`: n 23, 13 campaigns, ridge 1.0, battle-weighted Brier 0.2768816348133779, equal odds 0.25 | ✔ |
| 113 dossiers carry `opening-personnel-unknown` with status `unknown` | 113 exactly, all `unknown`. See A1 on the design's wording. | ✔ (wording) |
| "First-pass dossiers are schema v1 without typed quantities" | 126 are schema v1 with no quantities; Shiloh (TN003) is schema v3 and the only dossier with quantities | ✔ |
| Contract/opening profile unchanged | `docs/feature-admission.md` is not in the diff, and its hash equals `CONTRACT_SHA256` | ✔ |

Several frozen values bear on the findings:

- **Shiloh (TN003).** The frozen US figure is described as "Army of the Tennessee and Army of the Ohio (65,085)". The design's statement of reinforcement leakage is therefore concrete in the frozen inputs, not hypothetical.
- **Unit-list descriptions.** Five of the 23 frozen rows describe a side by named formations rather than an army. These are the basis for R3:
  - TN006 US "Detachments from four Union units (approx. 900)"
  - MS001 US "2nd Division and cavalry division, Army of the Mississippi…" and CS "1st Division, Army of the West (approx. 3,200)"
  - TN012 US "Detachments of two regiments…"
  - TN014 US "2nd Brigade, 5th Division, XIV Army Corps…"
  - TN022 US "3rd Cavalry Brigade (850)"

## Assessment by question

1. **Relationship to the contract.** The design leaves the contract text and the opening profile untouched, and §9 forbids relaxing the opening profile. It does not declare how contract §1 and §4 apply to a use that is not "retrospective pre-engagement prediction". Its §3.5 rule that "an unknown source derivation is allowed" contradicts §4's "Unknown derivation that may depend on outcome blocks admission until resolved". The design also states that it does "not … relax" the contract. That is a silent reinterpretation (R1). The reuse of §3, §5 and §6 is otherwise coherent.
2. **Measure and leakage.** The stated weakness is accurate but incomplete. Four gaps remain:
   - post-engagement returns;
   - figures for part of a multi-day interval;
   - an engagement-match exception ("an interval it states contains it with the same force") that is not separated from the campaign-total exclusion;
   - availability that may depend on the outcome.

   None of these is stated (R2). "Stated wherever results appear" is not carried into the §6 plan (R6).
3. **Applicability gates.** The statuses that are assigned follow §6: known incompatibility is `excluded` and unresolved applicability is `blocked`. Two ambiguities remain:
   - Whole-side scope for tabulated unit-list entries is ambiguous. It decides whether five frozen rows are applicable (R3).
   - An unresolved source role and a secondary figure with no basis have no status (R4).
4. **Rows, bases and scenarios.** The two orderings are not a complete fixed rule:
   - They do not rank two compiled families (CWSAC and Livermore) against each other.
   - They do not define cross-source or cross-role same-basis pairs.
   - They leave "basis class" and the composition of the `mixed_basis` scenario undefined.
   - "Adding scenarios where a third alternative exists" would be decided after extraction.

   An observation that forms only mixed-basis pairs in an engagement that also has a same-basis pair would appear in no scenario. The validator would flag this as `compatible_candidate_missing_joint_assignment` (R5).
5. **Evaluation plan.** The plan is not locked:
   - No rule is given for one-sided bounds or for the midpoint.
   - It does not say which rows train each model in the common-row comparison.
   - It reports "all complete tier-2 rows" rather than contract §7's "newly covered rows separately".
   - It sets no minimum-evaluability rule.
   - It omits campaign-weighted metrics.

   Comparing an expanded-coverage Brier against the 23-row baseline, or comparing scenarios with different row sets, would invite a misleading improvement claim (R6).
6. **Counts.** All verified. The 113 figure is a lower bound on unknown opening personnel, not the complement of 14 known dossiers (A1).
7. **Implementability.** §8 omits several constraints in the current object model. Each would force a later validator or schema change, so it should be named now (R7):
   - `CONTRACT_SHA256` and the use are pinned in `_profile`.
   - Candidates can reference only dossier quantities, not CSV rows.
   - `derivation: participation/unknown` excludes or blocks.
   - `estimation_status: unknown` blocks.
   - Membership atoms are required.
   - Schema v3 cannot represent one-sided bounds.
   - `_scenarios` hard-codes `profile_id` and does not check basis.
   - The review scope has seven parts, not eight.
   - No evaluation route exists.
8. **Research authorization.** The follow-up is bounded and tied to an admission decision, as the methodology's deeper-follow-up rule requires. There are three problems:
   - Livermore is described as "pinned as OCR" but is not in the registry.
   - Extracting only for the 68 would make the common-row comparison degenerate, because under `compiled_first` it would compare CWSAC with CWSAC.
   - The yield statement is an unverified expectation (R8).

   The roadmap's top "Current priority" heading still names the superseded coverage priority, which conflicts with the README (R9).

## Required corrections

### R1. Declare the relationship to contract §§1 and 4

**Evidence.**
- Contract §1: "The first supported profile is **retrospective pre-engagement prediction**".
- Contract §4: "Unknown derivation that may depend on outcome blocks admission until resolved", and "actual later arrivals/participation … are excluded as opening predictors".
- Design lines 3–5: "It does not amend, relax or replace the feature-admission contract".
- Design §3.5: "An unknown source derivation is allowed but labelled `derivation_unknown`."
- `admission.py` `_profile` accepts only `use == 'retrospective_pre_engagement_prediction'`.

**Replace design lines 3–5** ("**Status: a proposal awaiting separate review.** It does not amend, relax or replace … `opening_available_combatants_v1` profile.") with:

> **Status: a proposal awaiting separate review.** It does not change the text or hash of
> the [feature-admission contract](feature-admission.md) or its
> `opening_available_combatants_v1` profile. It adds a second, separately reviewed use under
> that contract's §§3, 5 and 6. Its departures from §4, which is written for pre-engagement
> prediction, are declared in §2 and apply to this profile only.

**Insert at the end of §2**, after the "must never be" list:

> **Relationship to contract §4 (this profile only).**
>
> - Every candidate records §4's five time distinctions unchanged. These are the state
>   interval, the document date and its role, publication and access dates, receipt
>   (null), and this profile's engagement interval and research cutoff.
> - Participation and arrivals *within* the engagement interval are accepted under the
>   declared partial-leakage label. They are never relabelled as opening data.
> - Excluded unchanged, with transitive dependency checks:
>   - casualties;
>   - survivors;
>   - post-engagement returns (§3.2);
>   - outcome narratives and outcome claims;
>   - loss-based reconstructions (§3.5).
> - §4's rule that an unknown derivation that may depend on the outcome blocks admission
>   is replaced here by the `derivation_unknown` label. This is a declared tier-2
>   relaxation: an undisclosed loss-based reconstruction cannot be ruled out for such a
>   figure. Results report, per scenario, how many rows rest on `derivation_unknown`
>   observations.
> - §4's outcome-, reputation- and score-blind selection rules apply unchanged.

### R2. Close the engagement-match and state-time leakage routes

**Evidence.**
- Design §3.2 admits "an interval it states contains it with the same force" but excludes "the campaign as a whole", without separating the two.
- Nothing in the design addresses returns dated after contact began, or figures for one day of a multi-day record.
- Contract §4: "Post-boundary casualties, survivors, … and outcome narratives are excluded".
- The Shiloh frozen US figure combines an army that arrived later ("Army of the Ohio (65,085)").
- Design §7 concedes that coverage will concentrate in "major battles". Availability is therefore not independent of the engagement.

**Replace design §3 item 2** with:

> 2. **Engagement match and state time.**
>    - The source ties the figure to this engagement: the side's force engaged in it, or a
>      return or estimate that the source states describes the force brought to it.
>    - A figure for another action or for the campaign as a whole is `excluded:
>      other_engagement`.
>    - A figure whose link to this engagement is uncertain is `blocked:
>      engagement_link_unknown`. This includes a return with an unstated muster date and a
>      return that the source does not tie to this engagement.
>    - A return or estimate whose state date falls after the frozen record's start date is
>      `excluded: post_engagement_state`. It describes the force after contact began, and a
>      later document date alone does not trigger this. The exception is a return the source
>      states describes the force at an earlier date; that earlier date is then its state
>      date.
>    - A figure the source limits to part of a multi-day engagement interval (one day or
>      phase) is `excluded: partial_interval`. When that is unclear, it is `blocked:
>      interval_unresolved`.

**Append to the "Known weakness" paragraph in §2:**

> Which engagements obtain figures may itself depend on the outcome, on size and on fame,
> because sides and compilers chose what to report. Results are conditional on source
> availability and do not represent the 91 decisive engagements.

### R3. Fix whole-side scope for tabulated unit-list entries

**Evidence.**
- Design §3.1 excludes "A named part (a brigade, …)" unless "a source … states that part was the side's entire force present".
- Design §4 simultaneously treats all 23 frozen CWSAC pairs as "one compiled-source candidate among others".
- Five of those rows name brigades, divisions or detachments (listed above). The rule as written could exclude them or admit them depending on the reviewer.

**Replace design §3 item 1** with:

> 1. **Whole-side scope.** The source presents the figure as the strength of that side's
>    whole force for this engagement, on its stated basis. Any of these qualifies:
>    - an army or command;
>    - "all troops engaged";
>    - a side-level table entry whose basis is the side's forces engaged, such as a CWSAC
>      forces row, even when it names the formations composing that force.
>
>    A figure that the source, or another cited passage, presents as one part of that
>    side's force is `excluded: partial_scope`. Examples are a brigade, an assault column,
>    one wing or the infantry alone. When the cited passages do not settle whether a named
>    formation was the side's whole force on that basis, the figure is `blocked:
>    scope_unresolved`. A side-level engaged entry satisfies scope on the engaged basis
>    only. It does not establish the side's present or effective strength.

### R4. Assign statuses to unresolved source roles and basis-less secondary figures

**Evidence.** Design §3.3 lists two admissible roles and one exclusion. It gives no status
for:
- a compiler who relays rather than adopts a figure;
- a compiled figure that visibly reproduces an opponent's estimate;
- a secondary total with no stated basis.

Contract §6 requires `blocked` when "disputed applicability [is] unresolved".

**Replace the paragraph after the role list in §3 item 3** ("An opponent's estimate, … never corrected.") with:

> An opponent's estimate, prisoner or citizen hearsay, and "said to be" figures relayed
> without the author's endorsement are `excluded: adversary_or_hearsay_estimate` in v1.
> - A compiled figure whose cited basis is visibly one side's report or an opponent's
>   estimate takes that underlying role.
> - A secondary total with neither a stated nor a table-level basis is `blocked:
>   basis_unknown`.
> - When the cited passages do not settle the role, the figure is `blocked:
>   source_role_unresolved`. An example is whether a compiler adopts or only relays a
>   figure.
>
> Own-side reports also carry a known bias. The role is recorded, never corrected.

### R5. Make pairing and scenario generation a complete rule fixed before extraction

**Evidence.**
- Design §4 is incomplete:
  - "a same-source compiled pair if present" does not order two compiled families;
  - "basis class" is undefined;
  - cross-source same-basis pairs are undefined;
  - the composition of `mixed_basis` is undefined;
  - "adding scenarios where a third alternative exists" is a choice made after extraction.
- Contract §5: "Every applicable alternative must appear … one observation per engagement", "do not form arbitrary Cartesian products".
- `admission.py` `_scenarios` flags any applicable candidate that has a compatible opposite but no joint assignment.

**Replace the "Basis pairing" and "Scenarios" bullets of §4** with:

> - **Basis pairing.** Each side's basis is the typed `basis` of its quantity. It is read
>   from the cited passage or the table's stated definition; a shared source does not
>   establish it. A same-basis pair has identical basis values. Every other pair is a
>   mixed-basis pair, including one with an unknown basis on either side.
> - **Candidate pairs.** An engagement's candidate pairs are every combination of one
>   applicable US and one applicable Confederate observation that no declared compatibility
>   constraint rules out (contract §5). A pair may combine sources and roles. It records
>   both source IDs, roles and bases.
> - **Pair ranking.** Fixed now, before any values are extracted or scored.
>   - Pair classes are: (a) both sides from one compiled source; (b) both sides' own
>     reports; (c) any other combination.
>   - Within a class, pairs are ordered by source ID, then quantity ID, in ascending
>     code-point order.
>   - Order A is (a), (b), (c). Order B is (b), (a), (c).
> - **Scenarios.** Each scenario is a full dataset with at most one pair per engagement,
>   no averaging and no weights. Engagements without a pair keep null sides. The declared
>   scenarios are exactly:
>   - `compiled_first`: each engagement's first same-basis pair under order A;
>   - `reports_first`: its first same-basis pair under order B;
>   - `alternate_k`, for k = 2 up to the largest number of same-basis pairs in any
>     engagement: its k-th same-basis pair under order A, or its `compiled_first` pair
>     when it has fewer;
>   - `mixed_basis_k`, for k = 1 up to the largest number of mixed-basis pairs in any
>     engagement: for each engagement with a mixed-basis pair, its k-th mixed-basis pair
>     under order A, or its first when it has fewer; every other engagement takes its
>     `compiled_first` pair.
>
>   The validator checks that the declared scenarios equal those this rule generates.
>   Every applicable pair therefore appears in at least one scenario. All scenarios are
>   reported with their own row counts. None is selected by score, outcome or reputation.
>   Results from scenarios with different row sets are never compared as improvements.

### R6. Lock the evaluation plan and carry the leakage label into it

**Evidence.**
- `baseline.py` `feature` uses `(low+high)/2` and requires finite positive values.
- `evaluate` needs at least 6 rows, at least 3 campaigns and both outcome classes, and reports battle- and campaign-weighted metrics.
- Contract §7: "report newly covered rows separately"; "Declare training-row differences"; "No enriched evaluation is authorized by this design".
- Design §2's uncertainty row leaves open whether the midpoint applies. The design has no rule for "over" or "nearly".

**Replace the §2 table's "Uncertainty" value** with:

> Preserve bounds; no imputation or weights. The only point value is §6's midpoint, used only in a locked evaluation. One-sided bounds form no scored row.

**Replace §6** with:

> ## 6. Evaluation plan, locked before any fitting
>
> This plan authorizes no fit. A fit needs a verified tier-2 release manifest and an
> explicit, recorded owner authorization (contract §7).
>
> - **Model.** `strength-logistic-v1` unchanged:
>   - ridge 1.0 logistic regression on (US − Confederate)/(US + Confederate);
>   - leave-one-campaign-out over the campaigns present in the row set;
>   - equal odds and the Laplace-smoothed, training-only prior as comparators.
>
>   No new predictors.
> - **Bounds.** A side's value is (lower + upper)/2, as in the baseline, with the
>   baseline's four-endpoint sensitivity reported. An observation with a one-sided printed
>   bound has no finite pair of bounds. It forms no scored row in v1 and stays in the ledger
>   as `blocked: one_sided_bound`.
> - **Evaluability.** A row set needs at least 6 rows from 3 campaigns, with both outcome
>   classes. A set below this is reported as not evaluable, with its counts.
> - **Reported separately for every scenario:**
>   1. **Common rows.** These are engagements with both a frozen baseline row and a tier-2
>      row. In each fold, both models are fit only on common training rows and scored on
>      the same held-out rows.
>   2. **Newly covered rows.** Tier-2 rows without a frozen baseline row, against equal
>      odds and the prior.
>   3. **All tier-2 rows.** Against equal odds and the prior, labelled as a population
>      different from the 23-row baseline.
>
>   Each report gives:
>   - battle- and campaign-weighted Brier and log loss;
>   - row and campaign counts;
>   - the number of rows resting on `derivation_unknown`, mixed-basis or own-report
>     observations.
> - **Labels.** Every result carries `partial_outcome_leakage` and
>   `conditional_on_source_availability`, together with the §2 statement. Predictions are
>   named as diagnostics, never win probabilities.
> - **Reference.** Retain the 23-engagement, 13-group baseline:
>   - battle-weighted Brier 0.2768816348133779 against 0.25 for equal odds;
>   - campaign-weighted Brier 0.2765271817053925 against 0.25.
>
>   Also retain the 127-engagement, 36-group coverage ledger. Never claim improvement by
>   comparing different populations or scenarios.

### R7. Complete the implementation notes

**Evidence** (all from `admission.py` and `evidence.py` at `e335b75`):
- `_profile` requires `contract.sha256 == CONTRACT_SHA256` and `use == 'retrospective_pre_engagement_prediction'`.
- Candidate leaves must be dossier `quantity` or `claim` nodes. There is no CSV leaf.
- In `_candidate`:
  - `derivation` of `participation` or `post_state` gives `excluded`, and `unknown` gives `blocked`;
  - basis `reported_engaged` gives `excluded`;
  - `estimation_status == 'unknown'` gives `blocked: estimation_provenance_unknown`;
  - `members is None` gives `blocked`;
  - a null boundary contact, area or availability gives `boundary_unresolved`.
- `_scenarios` writes `'profile_id': PROFILE` and carries no basis.
- `SCOPE` has seven names.
- Schema v3 quantities require finite `lower`/`upper` with `reported_exact`, `approximate` or `range`.

**Replace §8** with:

> ## 8. Implementation notes, for a later reviewed change
>
> The current validator accepts only the opening profile. Contract design v1 needs no text
> change if the following items are implemented as a separate, versioned profile path.
> `shiloh-opening-v1.json` and `-v2.json` must still validate unchanged.
>
> - **Profile binding.** The tier-2 profile binds the contract hash and this design's
>   accepted hash, with use `retrospective_whole_engagement_strength_diagnostic`.
> - **Boundary.** An engagement-interval boundary (frozen record ID, start and end dates)
>   replaces the contact, area and availability fields. It has one whole-side membership
>   atom per side.
> - **Mappings and codes.** A new proposal schema version adds `source_role` and the §3
>   codes:
>   `partial_scope`, `scope_unresolved`, `other_engagement`, `engagement_link_unknown`,
>   `post_engagement_state`, `partial_interval`, `interval_unresolved`,
>   `adversary_or_hearsay_estimate`, `source_role_unresolved`, `basis_unknown`,
>   `unreadable_value`, `derived_from_losses`, `derivation_unknown`, `one_sided_bound`.
> - **Profile-specific gate changes.** Under this profile only:
>   - `reported_engaged` and the `participation` derivation are applicable;
>   - `derivation: unknown` gives the `derivation_unknown` label;
>   - `estimation_status: unknown` is retained and labelled.
>
>   Neither of the last two is blocked.
> - **Frozen CSV figures.** These need either typed schema v3 quantities citing the CWSAC
>   row, or a separately reviewed CSV row/column leaf kind (contract §3). Candidates cannot
>   reference them otherwise.
> - **One-sided bounds.** Schema v3 cannot type a one-sided printed bound without inventing
>   an endpoint. Until a reviewed schema change, such a figure stays a prose claim and is
>   `blocked: one_sided_bound`.
> - **Rows and scenarios.** Rows carry the profile ID and both bases. The validator checks
>   the declared scenarios against the §4 generation rule.
> - **Review scope.** The release audit needs a profile-specific scope set covering §5's
>   eight items.
> - **Dossiers.** 126 of 127 first-pass dossiers are schema v1 without typed quantities.
>   Candidates need schema v3 quantities, added as versioned dossier revisions with
>   archived predecessors, and a new immutable evidence snapshot.
> - **Evaluation route.** No loader consumes rows. The §6 evaluation needs a separately
>   reviewed, non-installing evaluation command.
>
> If implementation shows that contract text must change, that is a contract revision
> with its own review.

### R8. Correct the research authorization

**Evidence.**
- There are no Livermore or *Numbers and Losses* entries in `data/sources.json`, `docs/sources.md` or `data/evidence/` at `e335b75`.
- If extraction is limited to the 68 engagements, the 23 common rows keep only first-pass and CWSAC figures. Under `compiled_first`, R6's common-row report would then compare CWSAC with CWSAC.
- The claim that compiled tables "mainly cover major battles" is not checked against any repository source.
- Methodology requires deeper follow-up to state "which admission or methodological decision it could change … and where the investigation stops".

**Replace §7** with:

> ## 7. Research authorized after this design is accepted
>
> This is bounded deeper work. It serves the tier-2 admission decision and follows the
> owner's 2026-09-25 decision. It is not boundary research, and it stops at the limits
> below.
>
> - Reuse first-pass citations already in the dossiers.
> - Add **one** compiled source family covering many engagements.
>   - The candidate is Livermore, *Numbers and Losses in the Civil War in America* (1901).
>   - It is not yet in the registry. Pin it with locators and hashes, as OCR, before
>     extraction.
>   - Extract it for all 91 decisive non-aggregate engagements, including the 23 with
>     frozen pairs, so that extraction does not depend on baseline status.
> - Add at most one further family for an engagement that still lacks an applicable figure
>   for each side.
>
> Each of the 91 engagements ends with either candidate figures for both sides or an
> explicit null with its reason. Inconclusive and aggregate records stay in the ledger but
> are never rows. Dependence between this compiled family and NPS/CWSAC is recorded as
> unknown unless evidenced, and their agreement is not corroboration.
>
> The yield is not known in advance. Compiled tables may favour larger actions, so many
> small cavalry and garrison actions may stay null. Report the actual yield per campaign,
> including zero.

### R9. Make the roadmap's current-priority heading match the owner decision

**Evidence.**
- AGENTS.md: "Read the current priority in `docs/roadmap.md`".
- Roadmap line 3 still reads "## Current priority — coverage before further depth". The new decision appears only at line 381, as "**Next priority**".
- README line 76 says "**Current priority: a reviewed second-tier strength profile.**"

**Replace roadmap line 3** with the following, keeping the existing "Owner direction, 2026-09-20" paragraph after it:

> ## Current priority — reviewed second-tier strength profile
>
> Owner decision, 2026-09-25: first-pass coverage is complete. The next step is separate
> review of the [reported side-strength design](feature-admission-reported-strength.md);
> see **Next priority** below. The coverage-first direction that follows still bounds any
> further research depth.

## Advisories (not required)

- **A1. Precise dossier count** (design §1 and roadmap line 382).
  - 113 dossiers carry `opening-personnel-unknown` with status `unknown`.
  - 11 more record opening or matched populations as `unknown` under other IDs:
    - `opening-populations-unknown`: MD001, MS016, NC002–NC006, TN001, TN002;
    - `matched-opening-strengths-unknown`: KY005, KY006.
  - MD003 and MS009 have no explicit unknown-opening claim.
  - Shiloh has zero eligible candidates.

  Suggested design §1 text: "Opening personnel is recorded as unknown in at least 124 of
  127 dossiers: 113 under `opening-personnel-unknown` and 11 under other claim IDs."
- **A2. "Same class".** The roadmap calls the measure "of the same class as the baseline's
  CWSAC forces-engaged figures". The profile also admits `present_for_duty`,
  `reported_present` and `reported_effective`, which are administrative or pre-contact
  bases. Consider "a coarser, reported whole-side measure that includes the baseline's
  forces-engaged class".
- **A3. Sums and reinforcements.** State whether §3.5's "same basis and time" forbids our
  own sum of an initial force and a later-arriving force. It should, so our own arithmetic
  does not increase leakage beyond what sources print.
- **A4. Output naming.** `baseline.py` emits `p_union_win`. Any tier-2 output should use a
  diagnostic name, consistent with §2's "never labelled … win probability".
- **A5. Ranking by source ID.** R5 orders pairs within a class by source ID. That order is
  arbitrary but outcome-blind. If the primary prefers another pre-extraction tiebreak,
  such as the frozen CWSAC pair first, it must be fixed before extraction and recorded.
- **A6. Scenario count.** Under R5, an engagement with many applicable observations (for
  example Shiloh's typed quantities) can produce many `alternate_k` scenarios. Declared
  compatibility constraints may reduce this, but only when fixed before extraction.

## Findings list

Required: R1, R2, R3, R4, R5, R6, R7, R8, R9. Advisory: A1, A2, A3, A4, A5, A6.
