# Offline admission validator, implementation v1

The validator implements the proposal and manifest checks in the
[reviewed design](feature-admission.md). It never installs feature inputs or fits
an enriched model. Astra `xhigh` implementation review and the
[focused follow-up](../artifacts/review-results/admission-implementation-1264e21-followup-v1/primary-assessment.md)
are accepted after fixing duplicate observation reuse, omitted compatible joint
assignments and ISO date ordering. The full 82-test suite passes. The original
design and its 13 worked examples remain immutable review artifacts; this
implementation prepares a distinct census of all 40 Shiloh troop observations.

## Run and inspect

```sh
python3 -m generalship admission-check
python3 -m generalship admission-check --details
python3 -m generalship admission-check path/to/proposal-or-release.json
make check
make reproduce
```

`admission-check` is read-only and prints a summary; `--details` prints every
decision, source observation, reason, scenario and coverage row. Invalid schema,
binding, scenario or release checks exit nonzero. A structurally valid research
proposal with blocked/excluded observations exits zero: unresolved evidence is a
research result, not a software failure. `make check` includes the default
proposal. `make reproduce` writes [admission-check.json](../artifacts/admission-check.json)
and the normal report/receipt. The baseline still consumes only its existing
CWSAC import, and its numerical artifacts remain unchanged.

Normal commands never accept test-only inputs and have no test-override flag.
The Python test harness explicitly enables synthetic fixtures to exercise a
positive reviewed-manifest path. Those fixtures are generated in temporary
directories, plainly labeled invented, and contain no historical approval.

## Checked-in research proposal

[shiloh-opening-v1.json](../data/admission/shiloh-opening-v1.json) binds
[the frozen evidence snapshot](../data/admission/snapshots/pilot-evidence-aac2ed2-v1.json)
and an exact copy of the accepted design. The snapshot copies the cohort, all
127 frame rows, all three dossiers and the complete 53-entry registry from the
pre-implementation state `aac2ed229b3fb8a4d0db4cb8a0a332548ede39b1`. Every registry
entry binds its metadata and original raw bytes; the raw evidence is reused,
not rewritten. Later changes to a working dossier or registry do not change
this snapshot. A new evidence version requires a new snapshot/proposal.

Each of the 40 candidates references one existing quantity by ID and its explicit
side/entity mapping. All new semantic mappings remain `unknown`, with null
membership sets and no invented evidence. Mechanical exclusions follow only
structured source basis (`reported_engaged` / `reported_reinforcements`), a
post-outcome claim phase, or a state date demonstrably after the proposed April 6
boundary. A same-day date is not an invented clock order. The exact contact,
area, availability definition and target memberships remain null. Comparisons
parse calendar dates, including ISO week/basic forms accepted in older dossiers;
the original source period strings remain in the diagnostic output.

The resulting counts are **18 blocked, 22 excluded, zero eligible candidates,
zero complete rows and zero promoted rows**. The ledger retains **127 engagements
and 36 campaign groups**, three available dossiers, and one engagement with
prepared candidates. Antietam and Champion Hill have no typed troop candidates;
the other 124 engagements have no dossier. Unprepared fields remain visible as
empty candidate lists, not numerical zero strength. The default scenario selects
nothing and retains both sides of every frame row.

These statuses are about proposed opening use, not the historical truth or value
of an observation. This pass neither resolves source disputes nor admits the
draft dossier. It does not replace the earlier 13 purposive design cases with a
claim of 40 independent historical reviews.

## Implemented object format

The stdlib implementation in [admission.py](../generalship/admission.py) validates
exact required keys, supported enums, types, IDs and references. Unknown fields,
duplicate JSON keys/IDs, nonfinite JSON numbers and missing bindings fail closed.
File hashes use exact bytes; embedded objects use sorted-key compact UTF-8 JSON
with `ensure_ascii=False` and `allow_nan=False`.

| Object | Implemented fields and rules |
| --- | --- |
| Proposal | `schema_version=1`, `kind=admission_proposal`, boolean `test_only`, profile, bound snapshot, boundaries, candidates and explicit scenarios. No embedded approval flag. |
| Snapshot | Bound cohort/frame, complete registry/source bindings and dossiers. Production v1 requires the original frozen cohort hash. Frame campaigns/outcomes/grain and baseline eligibility must agree with bound CWSAC source rows. Validation uses these snapshots, not the current registry/cohort. |
| Profile | Exact contract hash; supported use/target/field/unit; population and boundary rules; preserve-bounds/no-imputation policy; all-applicable joint alternatives without weights; no outcome/score selection. The evaluation plan records the research cutoff, whole-campaign holdouts, common-row versus expanded coverage and no fitting. |
| Boundary | Battle/profile IDs; date; contact, area and availability definitions; membership atoms for each side; citations and rationale. Null required mappings block candidates. A date alone never completes a boundary. |
| Candidate | ID, battle, side, formation entity, boundary ID, root node and dependency nodes. The side must match the dossier entity. |
| Node | ID, kind, reference, dependency IDs and semantic mapping. Leaves reference a quantity or a null/outcome claim. Operators are identity, sum and subtraction. Arbitrary formulas, authored numeric overrides and outcome-as-feature values are unsupported. |
| Mapping | Time relation, population compatibility, derivation class, membership atoms or null, rationale, exact citations and source-choice labels. Resolved mappings need citations; their historical entailment still needs evidence-use review. |
| Scenario | ID, rationale and exactly one US/Confederate candidate-or-null assignment for every frame engagement. No weights or score-based selector. |
| Release audit | Bound proposal, hashes of the three executing validator/provenance modules, bound review and primary reconciliation, expected preview-row and proposal-coverage hashes. It verifies content without installing it. |

Membership atoms denote the smallest explicitly mapped disjoint contingents
needed for a transformation; they are not fabricated individual-person IDs.
Authored mappings must establish what each atom means in the cited source and
at the boundary. The validator can check set relations, not prove the historical
partition. Root membership must cover the boundary's full side population.

Dependencies are acyclic and all nodes must be reachable. Every dependency is
checked even if a parent carries clean labels: a later survivor or participation
leaf still excludes the root. Sums require disjoint member sets and subtraction
requires nesting. Bounds propagate through interval arithmetic; no midpoint or
probability interval is invented. Negative subtraction bounds and nonpositive
strength block use. Source precision and estimation classifications remain in
the decision's original quantity record.
There is exactly one observation leaf per quantity/claim reference within a
candidate. Reuse that graph node when a calculation needs it again, such as
`(A+B)-B`; creating another leaf cannot assign the same observation conflicting
membership labels and count it twice.

Source representations retain source IDs, raw and metadata hashes, dependence
labels and a same-document key. Explicit transcript/facsimile links share a key;
raw-identical metadata aliases also share a key. An unlinked derivative may still
depend on another document: the validator does not infer independence from a
different key or group string. Citations never act as votes or quantity weights.

Scenarios must include every technically applicable candidate somewhere. Shared
source-choice labels must agree within a joint scenario; incompatible choices
or inapplicable candidates suppress that scenario's previews and fail a release
audit. On outcome/grain-eligible engagements, every applicable candidate with a
compatible opposite-side candidate at the same boundary must appear in at least
one coherent joint assignment. Splitting compatible sides into separate partial
scenarios does not satisfy this rule. An absent/inapplicable opposite side does
not force a fabricated row, and no full Cartesian expansion is required.
Scenario rows remain separate, while the coverage denominator counts
distinct engagements. No refitting is performed; the output supplies separately
identified preview datasets for a future separately authorized evaluation.

## Review and manifest checks

Without a review, a technically usable candidate is `eligible_candidate`.
Known incompatible use is `excluded`; unresolved applicability is `blocked`;
malformed bindings/schema are `invalid`, in that precedence order. Evaluated
reasons remain visible when a later check finds an invalid condition. An invalid
candidate remains in the frame ledger when its battle and side can be identified;
unplaceable objects invalidate the whole proposal.

A release audit requires a separate review object with kind
`separate_evidence_use_review`, actual response-file binding, reviewer identity,
kind, model/effort for AI, date, verdict, findings, and the complete seven-part
scope (profile, boundary, time, population, derivation, dependence, scenarios).
The machine scope names are `profile`, `boundary`, `temporal`, `population`,
`derivation`, `source_dependence`, `scenarios`. The review must bind the exact
proposal, snapshot, profile, boundaries and every candidate hash. A separately
bound primary reconciliation identifies a different actor and binds that review
and proposal. Source-transcription-only reviews and unresolved findings do not
pass. Substantive corrections require a new proposal and clean follow-up review;
v1 does not silently close findings with an author-written status flag.

The manifest binds the full **proposal-stage** coverage ledger and preview rows;
its review/reconciliation bindings record the later approval stage. The returned
audit labels that coverage stage explicitly and reports release-scoped candidate
statuses separately. A verified manifest can expose `audited_rows_by_scenario`
and `admitted` candidate statuses **within that audit only**. It always reports
`emitted_rows=[]` and `promoted_rows=0`. No model loader, installation command or
release discovery mechanism consumes these rows. No real historical release or
evidence-use approval is supplied in this repository.

Hashes and typed review fields are not signatures. The validator cannot prove
reviewer identity, sincerity, source independence, or that passages support an
authored mapping. The primary agent/owner still must inspect the actual separate
review; automated success does not establish historical truth.

## Validation and remaining work

The synthetic suite exercises the positive audited-manifest path, first-review
waiting, adverse and insufficient-scope reviews, mutated bindings/rows/coverage,
later reports of earlier states, null section dates, transitive post-event and
target leakage, unsupported causal/information-set profiles, overlap/nesting,
cycles, missing values/sides, source aliases, joint alternatives, source cutoffs,
cohort integrity, replay against later registry changes, and common versus new
coverage. Existing baseline/evidence/reproducibility tests remain in place.

Before historical admission, establish and review a usable opening boundary and
population mapping, resolve applicability or retain coherent alternatives, and
obtain actual evidence-use review of an immutable proposal. Continue evidence
work by complete campaign. A model-input installation route, enriched fit,
forecast-accuracy claim or causal interpretation remains outside this change.
