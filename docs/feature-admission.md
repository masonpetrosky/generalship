# Feature-admission contract, design v1

This is a specification for a future admission layer, not an implemented API or
permission to change model inputs. The current baseline continues to read its
pinned CWSAC tables. The [worked Shiloh cases](research/shiloh-admission-examples.md)
emit no features. Design review and historical evidence-use review are separate:
accepting this contract does not approve the examples for modeling.

## 1. Supported use and explicit non-goals

The first supported profile is **retrospective pre-engagement prediction** of the
recorded decisive Union outcome, within the frozen source frame. It reconstructs
earlier conditions using later research. It is not a forecast made with only
information available to a historical commander. Its predictions and residuals
are diagnostics, not command effects, general win probabilities, or WAR.

A profile MUST declare its target, observation unit, feature definitions,
population, spatial scope, boundary, transformations, uncertainty policy,
selection rules and evaluation plan before fitting or examining comparative
scores. Each engagement contributes once; mirrored sides, multiple commanders,
and scenario alternatives are not extra observations. Dossier entity `CS` maps to
dataset side `Confederate`; `US` maps to `US`. Entity membership requires an
explicit ID mapping, not name matching.

Historical information-set forecasts, battle replacement effects and campaign
contribution are unsupported in v1. They require separately reviewed contracts,
including knowledge/receipt evidence or replacement population, authority,
counterfactual intervention and causal identification as appropriate. No battle
residual may be allocated automatically to listed commanders or added to a
campaign score. A commander's earlier preparations may be predictive conditions
and also mediators of campaign contribution; including them in prediction does
not identify that total causal effect.

## 2. Proposed first feature profile

`opening_available_combatants_v1` is a proposed profile, still requiring
engagement-specific evidence-use review. Its unit is people assigned to combat
units, including officers, infantry, artillery crews and cavalry, physically
available in the defined engagement area immediately before first hostile
contact. It excludes detached units outside that area, subsequent arrivals and
people known to be absent, hospitalized or in noncombatant duties. It counts
people, not guns or formations. It makes no latent morale or readiness score.

Before any admission, an engagement boundary record MUST define which contact
starts the engagement (including picket contact), the area and treatment of
outposts, detached formations and transports, and the operational meaning of
"available." Evidence must establish membership at that boundary; later actual
participation is not its definition. The same boundary and population rules apply
to both sides. A reviewed relative ordering may suffice where a clock time is
unknown, but only if every included/excluded observation is unambiguously placed
on the relevant side of that boundary. Uncertain order crossing the boundary
blocks the affected observation. Do not invent precision or equate arrival,
landing, formation and engagement.

The Shiloh examples propose an April 6 pre-contact target but leave the exact
contact definition, area and availability mapping unresolved. They do not set a
tactical or campaign replacement boundary. No canonical Shiloh opening total is
established here. This proposed opening profile must not silently relabel the
existing baseline's whole-engagement `source_reported_forces_engaged` values.

## 3. Admission objects and immutable bindings

The future implementation MUST keep these distinct objects:

| Object | Required contents |
| --- | --- |
| Profile | Version/ID; contract hash; target and unit; scope and boundary rules; coding and scenario policies; evaluation-plan hash. |
| Evidence snapshot | Dossier path, revision and byte hash; complete registry snapshot path/hash; exact source IDs, raw paths/hashes and complete source-entry metadata hashes; evidence commit or content-addressed snapshot. |
| Candidate | Stable ID; battle/side/entity mapping; claim, quantity and event IDs; exact citation/section or CSV row/column; proposed value or null; source precision and estimation classification; temporal and population mappings; dependencies and reasons. |
| Boundary record | Battle and profile IDs; event definition, spatial scope, available-population definition, interval/ordering and precision; supporting citations; unresolved alternatives; review scope. |
| Decision | Candidate hash; every gate result and reason; reviewer artifacts and primary disposition; status, alternatives and exclusions. |
| Release manifest | All object hashes; decisions; scenarios; cohort and evaluation plan; complete coverage ledger; transform implementation hash; exact emitted rows/hash. |

Hashes of files use SHA-256 of exact bytes. Hashes of embedded metadata use
sorted-key compact UTF-8 JSON with `ensure_ascii=False`, `allow_nan=False`, matching
`source_metadata_digest`. Exact source IDs alone are insufficient: corrected
metadata can share the same raw file. Preserve the full bound snapshots for
replay. Never resolve a released manifest against "latest" or overwrite an older
manifest. Adding an unrelated source to a later registry does not alter an old
release; replay uses its own snapshot. A changed referenced observation,
metadata entry, boundary, transform, scenario, review disposition or profile
requires a new candidate/release and review of its changed scope.

The profile/contract review MUST name exact hashes. Candidate evidence-use review
MUST bind the candidate, profile, source snapshot and boundary hashes and state
which mappings, passages, transformations and alternatives it checked. Preserve
the actual response, task identity, model/effort if AI, date, findings and primary
reconciliation. A source transcription review alone does not approve a feature's
temporal or population mapping. A dossier's `supported` claim or `reviewed` status
does not approve every candidate. Draft dossiers may supply candidates, but only
a separate reviewed admission manifest may supply new model rows. Field-scoped
review may approve a bounded candidate without pretending the whole dossier is
resolved. There is no automatic human-review requirement in this design; actual
separate review follows repository policy and any specifically stated evidence
requirement. Separate AI analysis is not independent historical evidence.

Avoid circular approval hashes: a content-addressed decision proposal binds all
candidate inputs and proposed rows; the reviewer reviews that proposal. A final
manifest references the proposal hash, actual review, primary dispositions and
emitted-row hash. It may only package unchanged approved content. Any substantive
correction produces a new proposal and bounded follow-up review; no approval
record claims to hash the file containing itself.

## 4. Time, scope and leakage gates

Every candidate MUST distinguish:

1. The historical state/event interval being measured and its precision.
2. The document's preparation/report/forwarding date, with its role specified.
3. Publication and research access dates (null when unknown).
4. Any evidenced command receipt/knowledge time (null when unknown).
5. The profile's state boundary and the evaluation's research snapshot cutoff.

A post-battle report may describe a pre-battle return. Its later document date
alone neither excludes nor admits that return. Review must support its earlier
referent, population and derivation. A date in a heading, a date forwarded, and
the muster date need not be the same. Mixed-document section dates take
precedence, including mapped nulls; never borrow a neighboring report's date.
Issue date does not establish receipt, and reported death does not establish
effective transfer of command. Retrospective reconstruction may leave historical
knowledge unknown because it makes no information-set forecast claim.

Post-boundary casualties, survivors, fatigue caused by combat, actual later
arrivals/participation and outcome narratives are excluded as opening predictors.
Reconstructing opening force as survivors plus casualties is also excluded in
v1. Dependency checks MUST be transitive: relabeling a post-event input, hiding it
in a sum or replacing its date with a return heading cannot remove leakage.
Unknown derivation that may depend on outcome blocks admission until resolved.
Pre-boundary plans or expectations require their own measured variable and
profile; do not replace them with what later happened.

The target label has a separate, bound outcome channel. Candidate selection,
feature coding, source preference, scenario weights and boundary definitions
MUST NOT use whether a choice better matches recorded outcomes, commander
reputation or held-out scores. Outcome-blinded extraction can be documented, but
AI historical knowledge remains a limitation; do not claim blinding proves
absence of hindsight. Record deviations from the locked plan and evaluate them
as exploratory until a new evaluation is specified.

## 5. Quantities, overlap and disputed alternatives

Preserve `lower`, `upper`, unit, basis, period, scope, printed precision,
`estimation_status`, estimation note and citations. Printed integers are not
proof of measurement accuracy. Explicit estimation is not itself disqualifying;
its target applicability and any uncertainty treatment still require review.
Source bounds are not probability intervals. V1 has no default midpoint,
confidence weight or imputation rule for enriched inputs; these must be part of
the reviewed profile. The existing baseline's midpoint rule is unchanged.

Null stays null. Missing supplies, morale or readiness must not become zero,
"normal," a synthetic score or a proxy based on fame. A partial army total is not
a whole-army estimate. Missingness flags may appear in the coverage ledger;
using them as predictors requires a separate reviewed feature definition.

Every numeric transform MUST declare an acyclic dependency graph, formula,
units, time compatibility, membership sets and overlap relations. Sums require
evidence that components are disjoint, cover the stated target and share the
required time/population. Subtraction requires an evidenced nested subset with
the same basis and boundary. Unknown overlap blocks the transform. A sum of
units present at different phases is not a simultaneous available total.
Recorded counts may stay in evidence even when no valid transform exists.

Registry aliases, transcript/scan pairs and reproduced returns are one
underlying document for corroboration purposes. Record same-document,
derivative, shared-input, independent-authorship or unknown relationships with
evidence. Different `independence_group` strings do not prove independence;
independent authors can reuse the same return. Do not count citations as votes.

Preserve conflicting printed values separately with discrepancy IDs and the
reason their relationship is unresolved. Do not silently correct, average or
select the convenient value. Alternatives may enter **scenarios only after each
is individually applicable to the same target**. Wrong-scope/post-boundary data
cannot be rescued by calling it a scenario. A still-disputed but applicable
pair can be reviewed as coherent alternatives without declaring either true.

Scenarios are mutually exclusive joint assignments across affected variables,
sources and engagements. Declare compatibility constraints, shared-source
dependence and required exclusions; do not form arbitrary Cartesian products
of incompatible totals and components. Each scenario is a separate full dataset
and refit/evaluation, with one observation per engagement. Report all declared
scenarios and their coverage. Do not choose the best-scoring scenario. No default
probability weights or pooling across scenarios; any future averaging rule must
have independently justified weights fixed before evaluation. Endpoint-only
prediction variation is not a refitted sensitivity analysis.

## 6. State machine and release gate

Gate order is binding/schema integrity, supported profile, temporal applicability,
population and overlap, derivation/uncertainty, evidence-use review, and release
integrity. Record all evaluated reasons, not just the first failure.

| Status | Meaning and allowed next step |
| --- | --- |
| `invalid` | Malformed/missing binding, unresolved ID or hash mismatch. Correct or supply a new immutable proposal; emit nothing. |
| `excluded` | Known incompatible target, unsupported use or leakage. Preserve reason; a different profile is a new candidate, not a bypass. |
| `blocked` | Required timing/population/derivation evidence or review is missing, disputed applicability unresolved, or blocking finding open. Research/review may resolve a new proposal. |
| `eligible_candidate` | Technical and evidence applicability gates pass; review/release not yet complete. Emit nothing. |
| `admitted` | Exact proposal has separate evidence-use review and reconciled disposition, all applicable alternatives handled under the locked policy, all gates pass, and the release manifest verifies. Emit only the bound value/scenario. |

Implementations MUST represent review as a separate gate: an otherwise eligible
candidate awaiting its first review is `eligible_candidate`; an adverse review
with unresolved required corrections is `blocked`. If multiple failure classes
apply, `invalid` takes precedence, then `excluded`, then `blocked`; all reasons
remain visible. The status `admitted` is release-scoped, not a mutable flag in a
dossier. Zero admitted rows is a valid research result, never a trigger to relax
the contract. The examples' expected statuses are design judgments, not runtime
validator results or actual historical admission decisions.

## 7. Coverage, evaluation and replay

Every release retains all **127 engagements and 36 source campaign groups** in
its coverage ledger, including unsupported outcomes and aggregate operations.
Record per-field/side availability, reviewed mappings, accepted alternatives,
excluded/blocked reasons and complete eligible model rows separately. A reviewed
US side alone does not complete a force-contrast row; both sides need the same
profile and boundary. Distinguish source coverage, extraction review, feature
admission and forecast evaluation. Publish exact numerators and denominators;
do not count aliases, scenarios or commanders as additional engagements.

No enriched evaluation is authorized by this design. A future locked evaluation
must retain whole-campaign holdouts and train-only comparator fitting. Compare
the enriched and old models on the same common rows/folds for paired claims;
report newly covered rows separately against equal odds and training-only priors.
The old strength model may lack predictions on newly covered rows. Do not claim
its performance improved by comparing different complete-case populations.
Declare training-row differences and source-scenario refits. Retain the current
23-engagement/13-campaign baseline and its unimproved Brier result as a reference.

Replay MUST be offline and deterministic with the standard library. Missing
snapshots, changed raw bytes, invalid metadata, uncovered frame IDs, duplicate
rows, cycles and unreviewed content fail closed. No model calls, implicit network
fetches or automatic promotion are permitted in validation. Design examples
live outside model/evidence input paths and cannot be discovered as releases.

## 8. Required implementation acceptance cases (future work)

These are requirements for a later implementation, not tests claimed to exist.
Positive fixtures use explicitly synthetic populations and test-only review
stubs; never fabricate a real historical approval record. Production replay must
reject test-only fixtures and require real review artifacts plus reconciliation.

| Case | Required result |
| --- | --- |
| Complete synthetic same-boundary disjoint populations, reviewed proposal and valid release | One emitted row per engagement; deterministic exact replay. |
| Otherwise identical proposal awaiting first review | `eligible_candidate`; no row. |
| Adverse unresolved evidence-use finding | `blocked`; source transcription approval does not override it. |
| Later report with directly supported pre-boundary referent and clean derivation | May pass time gate; all other gates still required. |
| Later survivors, casualties or participation hidden through multiple transforms | `excluded`; transitive provenance identifies leakage. |
| Unknown pre/post ordering, muster date or derivation relevant to eligibility | `blocked`; no inferred timestamp. |
| Null section date beside dated report, or order issue without receipt | Null retained; no information-set forecast admitted. |
| Same raw bytes with changed metadata, omitted binding or changed proposal after approval | `invalid`; review cannot be reused for altered content. |
| Transcript, scan and metadata aliases | One underlying document; no extra vote or quantity. |
| Whole plus nested component, unknown overlap or mixed-phase sum | No double count; transform blocked or excluded as applicable. |
| Explicit estimate with exact printed integer | Estimation retained; applicability may pass independently of precision. |
| Conflicting applicable alternatives with locked coherent scenarios | Separate full refits/datasets; no averaging, extra battle weight or score-driven selection. |
| Wrong-population alternative disguised as scenario | `excluded`; no scenario escape hatch. |
| Unknown logistics or one missing side | Null retained; row incomplete and still in denominator. |
| Changed registry only outside an older bound snapshot | Old replay unchanged; no lookup against current registry. |
| Cohort omissions, mirrored duplicate, commander expansion or changed target mapping | Release fails; no silent cohort or target migration. |
| Enriched coverage differs from old baseline | Common-row comparison distinguished from expanded-coverage report. |

Implementation should first provide a non-promoting validator and coverage ledger
against this reviewed specification. Admission of actual Shiloh features requires
further evidence-use work and an explicit release; this document alone supplies
neither.
