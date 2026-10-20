# Napoleonic strength and command ledgers: design v1

Status: primary-verified design and worked examples, 2026-10-19. The owner accepted
a bounded ledger design using existing development-cohort dossiers. This is a
measurement contract, not a ledger release or authorization for a historical fit.

## 1. Scope and stopping rule

The [scope record](../data/napoleonic/ledger-design-v1/scope.json) fixes the smallest
complete development-cohort group, breaking ties by earliest start year and then
group key. This selects `third-coalition 1806`: Campo Tenese, Maida, Gaëta and
Amantea, four entries and eight sides. The full Amantea interval extends into 1807;
its frozen group and interval remain intact. Selection uses group membership and
size, not outcomes, names or numerical availability. Historical facts have already
been seen; this is not historical blinding or a representative yield sample.

Use only the four existing dossiers and registered sources. Index every strength
and responsibility claim, and demonstrate the contract with bounded excerpts,
explicit unknowns, alternatives and arithmetic checks. The examples are not an
exhaustive atomic transcription of those claims. Unextracted material remains in
the unchanged dossiers. Stop after these four entries, passage inspection and
offline validation. No new fetching, deeper campaign research, calibration scoring,
synthetic experiment, model fit or feature admission is included.

The unchanged evaluation reservation remains **273 development entries in 13 groups**
and **52 final entries in three groups**. This design uses only the selected
development group. The final set supplies no ledger-design cases or numerical
model-selection feedback.

## 2. Separate objects and identities

| Object | Grain and required content |
| --- | --- |
| Strength observation | One source-specific quantity for an explicit battle, side, population and state referent. Retain printed wording, bounds, units, basis, precision, derivation, source role and uncertainty. |
| Command observation | One source's assertion of a person's role, authority scope and time. Preserve local, superior, subordinate, siege, garrison and negotiation roles separately. |
| Side record | Exactly one per frozen battle and side A/B, including null selections, unresolved boundary, army identity and command responsibility. |
| Discrepancy | A named set of observations and their relationship: differing value, scope, phase, authority, identity or unresolved dependence. An apparent numerical disagreement need not compare the same population. |
| Transformation proposal | Explicit input IDs, arithmetic and population/time/overlap mappings; a correct sum is not an applicable strength estimate. |
| Verification decision | Exact input and proposal hashes, passages checked, mapping dispositions, remaining findings and actual verifier role. |
| Future release | Versioned profile, complete cohort coverage, applicable scenarios, verified decisions, transform/code hashes and emitted-row hashes. No release is created here. |

Side A remains France and its allies under the frozen frame; side B is their
opponent. Do not orient a second row by the winner. Multiple commanders, sources,
scenarios and command changes never create additional engagement weight.

A printed name is a label observation. Worked command records leave
`resolved_person_id` null. A future person registry must retain literal aliases,
source-backed merges and unresolved matches. Rank, title similarity and a repeated
surname alone do not resolve identity. Local responsibility is a further mapping:
neither a printed commander nor the most senior officer automatically controls
the target force at the chosen boundary.

An army/formation mention is likewise not a verified cross-engagement army ID.
The side records leave `army_id` null. A future registry needs appointment and
formation continuity evidence, reorganization/split/merge rules, time intervals
and explicit unknowns. Repeated commander or corps names do not identify an army.
Commander-versus-army identification remains unassessed by this design.

## 3. Strength observations

`examples.json` contains worked observations; its source snapshot preserves complete
metadata entries, raw hashes, parents and facsimiles. Every used citation copies an
exact dossier citation and binds its claim. Source document dates come from the
snapshot's section map, including mapped nulls. Publication year, historical state,
document preparation and command receipt are distinct; unknown receipt stays null.

Amounts use one of `point`, `approximate`, `range`, `lower_bound`, `upper_bound` or
`unknown`, with nullable lower/upper endpoints and explicit endpoint inclusion.
An approximate printed number is retained as that number with its qualifier; it
does not acquire an invented error band. A one-sided bound keeps its missing end.
`unknown` has no endpoints. Printed integers do not imply exact historical accuracy.

Keep personnel, guns, horses, inhabitants and organizational units distinct.
`rank_and_file`, infantry, cavalry, garrison, wider-corps and actual-participation
figures are not interchangeable all-arms available-combatant totals. Do not add an
officer multiplier, assume an artillery crew size, multiply battalions by an
average establishment or convert a town's inhabitants into defenders.

Source roles include compiled accounts, own-side retrospective accounts,
retrospective histories, opponent estimates and hearsay. These
describe provenance, not quality weights.
Publication/scan/transcript copies in one source family are not independent votes.
Own-side reporting does not automatically outrank a compiled total. Unknown
underlying derivation remains unknown even when the author gives a precise integer.
An illustrative assumption remains labelled illustrative.

An observation can be retained while unusable for a particular profile. Selection
never uses the recorded winner, reputation, a desirable force ratio, fitted scores
or an attempt to make a commander look plausible. No median, average, preferred
source hierarchy, confidence weight or imputation is supplied by this design.

## 4. Opening-population applicability

The proposed Napoleonic opening target follows the population discipline in
[feature admission v1](feature-admission.md#2-proposed-first-feature-profile): people
assigned to combat units, including officers and artillery crews, physically
available in a defined area immediately before a specified first hostile contact.
This is a retrospective reconstruction, not a forecast from a commander's known
information. No Napoleonic admission profile is installed in the existing Civil War
validator by this design.

Each engagement first needs a versioned boundary defining contact, outposts,
investment/blockade versus bombardment, area, detached troops and availability,
supported by inspected evidence. Frozen start dates delimit source-listed records;
they do not establish first contact, campaign appointment time or a transfer clock.
A qualitative ordering may suffice if it unambiguously locates every component;
otherwise retain uncertainty. Never turn a day label into an invented clock time.
The same boundary and population rules apply to both sides.

The non-promoting design checker reports all applicable reasons:

1. Broken bindings, malformed amounts, missing sides, unknown references or a
   changed frozen selection are invalid and fail closed.
2. A known wrong unit/basis/population, actual-participation selection, illustrative
   number or post-event reconstruction is excluded from this opening profile.
3. Missing boundary, uncertain state/area membership, incomplete population,
   unknown derivation or an unclosed bound blocks applicability.
4. A constructed observation passing those technical gates may be labelled
   `eligible_candidate`; it still emits nothing and has no historical approval.

Exclusion takes precedence over blocking, with every reason retained. A later
publication can describe an earlier state; publication date alone supplies no
leakage verdict. Conversely, an early return heading cannot clean a quantity
derived from casualties, survivors or later participation. Future transformations
must audit dependencies transitively, including source-derived inputs. The worked
arithmetic proposals are direct sums only; they are **not** a general transform or
release engine. More complex dependency graphs require a later implementation.

All worked side boundaries remain null, so no side has an established opening
mapping. Do not classify every later phase by comparison with the frozen start date:
the contact definition itself may be unresolved. The checker validates the declared
mappings and provenance; matching a quotation cannot establish historical entailment.

## 5. Command responsibility and campaign contribution

A command record preserves the literal actor label, source-specific role, force
scope, state-time description, evidenced authority and uncertainty. Separate
on-site tactical direction, a superior's campaign directives, troop command,
garrison government, acting command and authority to negotiate a capitulation.
An acting governor at surrender does not become the opening governor. A subordinate
leading an investment does not automatically replace a superior for the whole siege.
Keep transfers and overlapping claims explicit, with null effective times when absent.

A future boundary-level responsibility selection requires a resolved person,
evidenced authority over the same population/area as the strength target and
placement at the same boundary. Every competing or overlapping assertion needs a
disposition. Rank or a frame's single-name listing is insufficient. Unresolved
joint control remains unresolved; do not distribute residuals among listed names.
This design selects no responsible person and assigns no commander effect.

Campaign contribution additionally requires appointment t0/t1, objectives,
eligible replacements, inherited resources/information and the identification
argument in [methods v1](napoleonic-methods-v1.md#1-what-campaign-contribution-would-mean).
Strength created by concentration, supply and preparation can be inherited at
battle onset and mediated by a campaign appointment. These are separate mappings,
not one phase label reused across estimands. Neither opening applicability nor a
predictive residual identifies a tactical or campaign effect. No battle/campaign
double counting or invented replacement pool is allowed.

## 6. Alternatives, arithmetic and coverage

Every side retains all worked alternatives and explicit null selections. A
discrepancy's resolution stays null here. A future scenario can select alternatives
only after each is individually applicable to the same target and source/phase
compatibility is declared. Wrong-scope observations remain evidence, not scenario
escape hatches. No arbitrary Cartesian products, citation voting, automatic source
weights or best-scoring scenario selection are allowed.

For a sum, document identical units/bases, disjoint membership, common state time
and complete target coverage. Correct arithmetic alone establishes none of those.
For example, separately dated marching columns need not have been simultaneously
available, and local siege troops plus detached posts need an explicit area rule.
Do not infer independence from different source IDs. Retain failing or blocked
proposals along with their arithmetic result and all applicability reasons.

The generated report distinguishes four engagements, eight side slots, individual
observations, source-family counts, indexed claims, unknown identities, candidate
applicability and zero emitted model rows. These are design-example denominators;
they do not estimate a corpus error rate or future admission yield. Full-cohort
expansion must retain all 325 entries and 650 sides, including missing/excluded
cases, and retain the 273/52 evaluation reservation and complete campaign groups.

## 7. Verification, versioning and release

The [worked bundle](../data/napoleonic/ledger-design-v1/examples.json) binds this
design, the scope, four exact dossier byte hashes and a frozen subset of complete
source metadata. Its checker reads that snapshot rather than latest registry
metadata. Unrelated future registry additions do not rewrite these examples.
Referenced raw files, source parent/facsimile relationships and dossier claims
still have to replay exactly. A referenced revision requires a new version and
explicit migration; never overwrite an older released record. The selected
dossiers and every pinned source remain unchanged in this work.

The source registry hash in the scope records the selection base; replay uses the
bound subset snapshot. Canonical embedded hashes use sorted-key compact UTF-8
JSON, `ensure_ascii=False`, `allow_nan=False`; file hashes use exact bytes. No
object claims to hash the file containing itself. `verification.json` binds final
design/example/code/test bytes and records the actual primary's checks; it is
neither an independent review nor a feature-admission approval.

Current owner policy requires primary verification, not a separate reviewer.
A future admission release needs its own primary evidence-use decision over the
exact population/time/authority mappings, distinct in scope from transcription
checks. Any separate review requires an explicit owner request. Existing frozen
Civil War admission contracts and review records remain as recorded; a future
Napoleonic admission implementation must version its profile and policy-aligned
verification gate rather than silently reuse that implementation's separate-review
requirements. No separate approval record is fabricated here.

Before a real release: finish and primary-verify the profile and mapping rules,
resolve or retain alternatives, implement immutable snapshot/decision/coverage
replay, and lock coherent scenarios and the exact transform. A historical fit
additionally needs a complete rating design and exact owner code/input run
authorization. This ledger-design acceptance supplies neither a release nor that
run authorization. Calibration remains prepared and unscored.

## 8. Offline checks and next decision

`python3 -m generalship napoleonic-ledger-design-check` verifies the worked bundle
without writing model inputs. `make reproduce` regenerates its JSON/Markdown
report, and `make check` runs contract tests plus the same checks. There are no
network or model calls. Constructed positive and adversarial tests are labelled
synthetic and never become historical verification records.

The worked result and precise remaining gates are in the
[generated report](../artifacts/napoleonic-ledger-design-v1.md). The next useful
measurement task is a bounded boundary/membership specification for these same
four entries and eight sides, using the pinned passages. It should stop with
explicit unresolved orderings where the evidence is insufficient, before expanding
extraction to the other development groups or fitting anything.
