# Napoleonic operational command units and authority: specification v1

Primary-verified design, 2026-10-20. The owner accepted the
[feasibility checkpoint's recommendation](research/napoleonic-measurement-feasibility-v1.md)
to define the command unit and authority rules using six existing cases. This
specification ends with those cases. It installs no registry, admission profile,
model input or historical run.

## 1. Unit decision and scope

**The campaign comparison unit is a person's command appointment over an
explicit operational authority and force scope during a specified window.**
The operational force is an organizational command, not the sum of everybody
mentioned in an engagement. Its identity, the appointment holder, and the people
locally available at an event are separate objects.

The organizational level belongs to the unit definition: an institutional army,
corps, division, brigade, siege command, garrison or temporary task force must
retain its declared level and mandate. A superior institutional command can
contain a local force without being identical to it. Future army context means
an evidenced persistent operational command **at the level declared for that
analysis**. A comparison must use one declared level or explicitly model the
different levels; it must not put a corps and its parent army into one undifferentiated
army-effect category. No historical army IDs or cross-entry links are selected here.

The authority being replaced is part of the contrast. Replacing a local field
commander while retaining the superior is different from replacing the superior
and allowing subordinate assignments to change. Both may be research questions;
their observations and contribution estimates cannot be interchanged or added.

The six worked cases are the four Naples entries plus Castalla and July
Salamanca from the completed 1812 group. They are **six design cases**, not a new
six-entry research cohort or a complete reinspection of either campaign. The
parent measurement denominator remains **12 entries / 24 sides**. The frozen first
cohort remains 325 entries: 273 development entries in 13 groups, and 52 reserved-final
entries in three groups. No final-reservation dossier supplies a design case.

## 2. Separate records

These are requirements for a future versioned mapping format. They are not fields
installed in the existing immutable JSON files. A local record key identifies an
observation or hypothesis; it does not assert a resolved person or persistent army.
Every mapping retains its input record IDs, exact byte hashes, source/passages,
interpretation, competing alternatives, decision basis and actual primary verifier.

| Object | Required meaning and fields |
| --- | --- |
| Source mention | Local key, literal actor/formation label, source ID and passage locator, source-specific time, reported role/scope and uncertainty. Preserve an unknown label, date or scope explicitly. |
| Operational entity hypothesis | Local key, proposed organizational level, authority jurisdiction/mandate, reported names, time scope, evidence and unresolved alternatives. A persistent `unit_id` stays null until a source-backed identity mapping is justified. Record source wording separately from an analyst's proposed classification. |
| Entity relationship | Two local/entity references, relation kind, level, time scope, evidence, alternatives and use-specific disposition. Distinguish containment, administrative membership, operational attachment, detachment, succession and identity. |
| Authority observation | Actor reference and nullable global person ID; target force reference and nullable global unit ID; authority kind; task/jurisdiction; time support; evidence and competing roles. A reported role need not have a complete appointment interval. |
| Authority-use query | The requested authority kind, force scope, area, boundary/window and intended use; relevant observations; dispositions of competing scopes; unresolved items; use-specific result. A force-total/actor co-report is an input, not a responsibility decision. |
| Campaign appointment candidate | Holder, force/authority scope, reported tenure evidence, analytical comparison window and its basis, inherited state, prior objectives, replacement eligibility, information, outcome-vector coverage and identification gaps. Unknowns stay null with reasons. Do not confuse an analytically chosen window with the historically reported start/end of tenure. |

Authority kinds distinguish superior operational direction, immediate local troop
direction, garrison government, reserve/sector direction, administrative authority
and delegated task authority. Preserve the source's title and an `unknown` or
disputed classification when necessary. A compiler's commander label is a mention
with unestablished authority scope; rank is not an authority-selection rule.

One actor can hold several roles; one force can have superior, local and
administrative authorities at the same time. This compatibility is not proof of
joint tactical control. Reported joint control requires its own evidence. Keep
competing assertions, compatible different scopes and genuine identity disputes
separate rather than forcing all of them into a single commander field.

## 3. Identity and continuity rules

**U1 — Evidence and levels.** Compare the same declared organizational level,
jurisdiction and periods. Retain affirmative evidence for a proposed continuity
or distinction and dispose of material contradictions. Matching names, recurring
commanders, similar troop totals, a corps numeral or a shared source campaign are
leads, not a mapping. Missing continuity is not proof of distinct armies.

**U2 — Containment is not identity.** An army, its corps and a detachment are
different scopes even when the source explicitly relates them. Time-bound
operational attachment is distinct from permanent administrative membership.
A detachment can remain administratively within a parent while serving another
operational task. Membership alone supplies neither a complete local population
nor the authority of every superior over that population at a chosen event.

**U3 — Changes require a relation, not automatic relabelling.** Apply these
conventions before selecting data or seeing numerical model feedback:

| Change or proposed link | Treatment |
| --- | --- |
| New holder of the same evidenced command | Preserve the operational entity if continuity is supported; create a separate holder/authority episode. A new commander alone neither proves nor disproves force continuity. |
| Same holder, another force or jurisdiction | Keep distinct scope records. Resolve entity identity from the force/mandate evidence, not the holder. |
| Troop rotation, reinforcement or concentration | Record composition changes. Neither freeze the personnel population nor create a new entity merely because its count changes. Positive organizational continuity is still required for a cross-time link. |
| Detachment or temporary attachment | Record parent and task relationships with their time/scope limits. Do not replace either with an equality edge. Arrival and local availability need separate evidence. |
| Reorganization or renaming | Preserve identity only where evidence supports continuation at the declared level; retain contrary evidence and uncertainty. The same numeral or a new title alone settles neither direction. |
| Split | Record the split and branches. Retain a continuing parent only with evidence of that continuation; newly constituted branches have their own entity hypotheses. Do not assert every branch is the same parent or infer a split merely from several troop mentions. |
| Merger or absorption | Distinguish a newly constituted command from an evidenced continuing recipient. Record incoming entities and transition evidence; do not infer identity by pooling their headcounts. |
| Unresolved transition | Keep local handles and an unresolved relationship. Separate handles are not an assertion that the historical entities differ. Missing links never become a default national/campaign/commander army ID. |

Identity is not established by transitive traversal through a containment,
attachment or delegation edge. Even supported identity links can only be composed
where their levels, time scopes and alternatives are compatible. A containment
hierarchy must not contain a cycle at the same epoch and relationship type;
different administrative and operational relations are not one undifferentiated tree.

This defines how a later registry would make and qualify decisions. The six
cases below do not establish historical split/merger lineages or empirically
validate the full continuity policy. No registry is installed by these rules.

## 4. Authority and time rules

**U4 — Select the question before a role.** A boundary-level tactical query asks
who exercised the specified local authority over the target force at that
boundary. A campaign query asks which operational authority is being replaced
over its window, including preparation and subordinate appointments. Council
policy, a visit, an investment task, government and negotiating powers can each
be retained without becoming the same authority. Delegation conveys the stated
task only. Do not select the most senior or most familiar name by default.

**U5 — Time is source-qualified support.** Retain the printed event/date label,
ordering, precision, anchor and unknown bounds. Publication, document date,
reported event, effective assumption of authority and receipt of information are
distinct. A day, approximate clock or successor's later act does not establish
an exact transfer instant. A single observation does not prove continuous tenure
before or after it. Missing ends are unknown, not infinite intervals.

A point query may be supported by an unambiguous source-relative ordering over
the relevant force; it does not require every tenure date or a synchronized
clock. A window query requires evidence or explicitly labelled design assumptions
appropriate to coverage throughout that window. A full lifetime biography is
unnecessary. If an effective transfer is uncertain, retain the possible holders
and their conditions instead of inventing an overlap, gap or fractional share.
Documented tenure, study-window boundaries and uncertainty are separate fields.
An analytical boundary convention cannot turn an unknown historical transfer
into a fact or silently replace the strict first-hostile-contact target.

**U6 — Person reference is a separate mapping.** A source-local co-reference can
support retaining the same actor within its episode without installing a global
person ID. Cross-source/entry identity requires an explicit evidence-use decision
with literal aliases, conflicting matches and scope retained; a complete biography
is not universally required. Recurrent surnames, title similarity and transliteration
are insufficient alone. Cross-entry commander pooling still needs those identity
decisions. Authority never establishes army identity by itself.

**U7 — Force availability is a separate mapping.** Authority over a wider force,
an order to join, later participation or membership in an institution does not
establish who was physically available locally at contact. Keep quantity,
category, assignment, area and state-time mappings separate. No battalion-to-person
conversion, implied gun crew, summed later columns or selection by source prestige
is supplied here. Existing population alternatives and explicit unknowns remain.

**U8 — Outcomes do not choose the mapping.** Fix the scope, continuity policy,
comparison window and source-use rules before numerical outcome fitting. Do not
change an entity/appointment boundary merely because a battle was won, a commander
was wounded later, or a preferred force ratio results. A subsequent change of
authority is evidence to record, not permission to manufacture an exact boundary.
Do not end a campaign appointment at achievement/failure of its objective unless
an endpoint convention was fixed without selecting on that realized result.

Changing strategy, concentrating troops or achieving an objective does not by
itself constitute a new organizational command. Those can be consequences of
the appointment. Record a materially changed authority jurisdiction or a new
mandate with its basis; do not cut away commander-created advantages by repeatedly
resetting the inherited state.

## 5. Evidence required depends on use

These are separate query results, not a cumulative confidence score. For each
use, return supported scope plus explicit unresolved items; `not_established`
does not mean the role or entity did not exist. A structural check is not proof
of entailment, independent corroboration or historical truth.

| Requested use | Sufficient record requirements at this stage | Additional requirements for a later use |
| --- | --- | --- |
| Retain a source-reported role | Exact source/passages and hashes; literal actor; reported authority/task scope; time support and unknowns. | No complete troop count, global registry or entire tenure is required merely to retain it. |
| Retain a local actor association | Explicit source-local context linking the role or person references, with alternatives visible. | A global identity merge, continuous appointment and first-contact authority do not follow automatically. |
| Map an entity relationship | Declared level/kind/time, affirmative relationship evidence, relevant alternatives and a qualified disposition under U1–U3. | Containment or organizational continuity does not supply personnel persistence. Unknown parent/continuity leaves the related army-context use unresolved. |
| Establish local boundary responsibility | The requested actor/authority scope is evidenced over the same target force/area at the boundary, with competing scopes disposed of or joint/unknown control retained. | Global identity is needed for cross-entry person pooling. Complete opening force/person use additionally needs both sides' common boundary and population mappings under the existing target. No existing selection is promoted by this specification. |
| Specify a campaign appointment comparison | Evidenced authority and force scope; t0/t1 or declared analytical window conventions; inherited state/information, prior objectives, eligible replacements and observed/missing outcome-vector components. | Non-battle opportunities, assignment, interference and identification must be addressed. An average fitted commander is not a replacement pool. |
| Admit features or estimate a result | A separate implemented, primary-verified release over exact mappings/versions, complete coverage/exclusion accounting and a complete run design. | Historical fitting still requires exact owner code/input authorization. Commander-versus-army separation and a causal interpretation need their own identification arguments; no predictive gain establishes them. |

Here a qualified local responsibility finding remains distinct from filling the
old ledger's `selected_person_id`. Its resolved-person and other selection gates
remain in force. A future profile using local handles would need its own explicit
version and implementation; this specification does not relax an installed gate.

One engagement retains one outcome weight. Multiple roles, phases, aliases,
scenarios or appointments do not create extra battle rows or equal shares of
credit. Overlapping superior/local appointments remain related observations,
not independent campaign successes. A future analysis must define how its target
handles joint authority or leave scalar attribution unavailable. A campaign
outcome vector is never a sum of battle residuals. The
[methods design](napoleonic-methods-v1.md#1-what-campaign-contribution-would-mean)
continues to govern mediators, replacements and evaluation.

## 6. Six worked cases

These apply U1–U8 to **existing assertions** rather than resolve history again.
A = [Naples authority mappings](../data/napoleonic/authority-v1/mappings.json);
B = [boundary records](../data/napoleonic/boundaries-v1/records.json);
P = [1812 measurement records](../data/napoleonic/peninsula-1812-measurement-v1/records.json).
Array IDs below are stable record locators. Referenced passages retain source
IDs, sections, quotes, raw/metadata/facsimile hashes and English interpretations.
The primary read the cited frozen passages and reconciliations for this design;
this is not a renewed page-image inspection or independent historical review.

### C1. Campo Tenese: council policy and local direction

**Inputs:** A reconciliation `campo-policy-and-local-direction`, organization
context `three-corps-and-detachments`; passages `p006`, `p028`, `p027`, `p040`
(Koch pp.173, 175, 174, 169); B scenario `ct-approach`.

**Rule result (U2, U4–U7):** retain the Joseph/Masséna council context, Reynier's
local orders and Damas's opposing-force role with their reported scopes. The
existing record places the local charge order during the developing action;
it does not synchronize every actor or component to earliest approach contact.
Council presence supplies no equality between superior and local authority.
The army/corps context in A's `organization_context` is a relationship report,
not a resolved army ID for either local force.

**Use still unresolved:** complete first-contact population and boundary-level
responsibility, persistent unit identity and campaign appointment. The concrete
missing mapping is authority over the same local components at the contact
boundary, not another title or a presumption that the council's senior member
commanded every local act.

### C2. Maida: expedition, preparation and field authority

**Inputs:** A reconciliation `maida-expedition-and-field`, local identity link
`stuart-within-bunbury`; passages `p009`, `p031`, `p032` (Bunbury pp.235, 240;
Koch p.190); B scenario `m-field`.

**Rule result (U1, U4–U7):** retain Bunbury's Sir John Stuart expedition and
preparatory orders as the supported source-local actor association already
recorded. Retain Koch's Stewart/Reynier field dispositions separately. An
expedition decision is not a complete local first-shot authority/population
mapping; the date alternatives and Stuart/Stewart hypothesis remain open.
Changing a role's phase does not prove either a change or continuity of army.

**Use still unresolved:** cross-source identity and common-time field-force
mapping. The bounded need is a compatible identity/force/time relationship,
not a full biography or automatic acceptance of all expedition personnel as
the local force. The source-local association remains useful without a global ID.

### C3. Gaëta: troop command, superior direction and delegation

**Inputs:** A reconciliation `gaeta-command-and-delegation`, organization context
`capitulation-staff-office`; passages `p010`, `p033`, `p034`, `p035`, `p036`
(Koch pp.196, 223, 229, 422); B scenarios `g-initial`, `g-july`.

**Rule result (U2–U6):** retain Lacour's brigade/negotiation role, Gardanne's
troop-command appointment, the superior visit/direction context and the later
capitulation's principal/delegate roles. The appointment and visit do not prove
an exclusive transfer. Franceschi's delegated negotiating powers and staff office
do not identify the entire siege force with his parent corps or make him its
commander. The document's dated evening is an event/document locator, not a
tenure start. The existing implicit marshal referent remains qualified.

**Use still unresolved:** a boundary-level force/person mapping and persistent
siege/parent entity relationship. Later explicit authority can support a role
at that document's context while leaving initial rifle-contact authority unknown.
The necessary query is authority over a specified force/window, not whether
only one name may appear in the whole siege.

### C4. Amantea: broader authority, investment and later columns

**Inputs:** A reconciliation `amantea-broader-and-local`, passages `p039`, `p019`,
`p020`, `p022` (Koch pp.281–282); B scenarios `a-investment`, `a-colletta` and
membership cases `a-a-huard`, `a-a-verdier`, `a-a-reynier`.

**Rule result (U2–U5, U7):** retain the reported broader command devolution to
Reynier, Huard's local investment task and the later columns/operations. The
scopes can coexist without an exclusive, clocked handover. A later departure
does not put the intact column at the earlier investment marker, and common
superior direction neither proves unchanged personnel nor licenses a sum.
The investment marker remains a non-contact scenario.

**Use still unresolved:** first-contact population/authority and entity continuity.
The concrete population need is concurrent local membership at an applicable
boundary; the organizational need is evidence of how each task force relates
to the persistent command. Colletta's undated assault alignment remains as
qualified in the older boundary records; no alternative clock is installed here.

### C5. Castalla: reserve, sector task and later support

**Inputs:** P observations `B432a-A-a02`, `B432a-A-a03`, `B432a-A-a04`,
`B432a-A-a05`; passages `p035`, `p036`, `p051`, `p052` (Toreno p.124;
Suchet pp.254–255); P's `B432a` entry and both side records.

**Rule result (U2–U5, U7):** retain Harispe's reserve scope, Mesclop's Ibi task,
Delort's advance/local counterattack scopes, the support order and later
approach as different asserted roles/events. The support order is not an arrival
record. Harispe's reported reserve role does not settle initial local authority;
a Delort local task also does not settle whole-entry authority or erase a superior.
Operational attachment and immediate location require separate mappings.

**Use still unresolved:** joint local boundary, complete categories/headcounts,
effective authority and persistent entity identity. The needed evidence would
place specified components and the relevant control at the same contact; it
would not convert all Ibi, Alcoy and Castalla forces into one local population.

### C6. July Salamanca: subordinate task and reported succession

**Inputs:** P observations `B432b-A-a02` through `B432b-A-a05`,
`B432b-B-a02`; passages `p039`, `p040`, `p041`, `p053`, `p054`, `p055`
(Marmont pp.235, 240; Oman p.436); P's `B432b` entry and both side records.

**Rule result (U3–U8):** retain Marmont's orders, Bonnet's earlier subordinate
task, reported Bonnet–Clausel succession, and Wellington's later attack-initiation
task with their own source-relative times. Bonnet's task and later succession
are different authority episodes. Succession alone does not create a new army,
prove its cross-entry continuity or supply exact transfer clocks. Oman's later
attack context is not synchronized to Marmont's wound or the first hostile act.

**Use still unresolved:** authority at a chosen common opening boundary,
continuous scope for a campaign window, and global person/unit mappings. A later
wound does not retroactively disqualify a well-supported earlier point role;
it also cannot make one printed name responsible for the entire outcome. Any
later model must declare its point/window contrast and deal with the succession
without dividing the recorded battle into extra weighted wins or losses.

## 7. Verification, versioning and stopping decision

The case checks preserve six useful sets of scoped role observations. **Zero new
global person IDs, persistent unit/army links, selected opening mappings,
admitted features or model rows are created.** This is the scope of this design,
not an estimate that none could ever be established. Earlier side records and
their blockers remain unchanged. The cases neither score historical commanders
nor test the statistical identification of commander and army effects.

A future mapping release must be immutable and bind the exact specification,
parent records, source snapshots, relationship decisions, unresolved cases and
code. A changed identity, force level or time interpretation needs a new version
and explicit migration. Do not repair a frozen record in place, convert an
unknown into a default ID, or reuse its old verification for a different use.
Implement and test the release contract before it can admit model inputs.

The primary checked each cited passage/reconciliation and the six rule results,
including the unsupported implications each case must leave unresolved. The
existing offline suite replays provenance and earlier contracts; it does not
implement or automatically validate this new specification. Validation and byte
preservation results are recorded in the
[research log](research-log.md#operational-command-unit-and-authority-specification-v1-2026-10-20).
No new code or test framework is needed for this specification-only deliverable.
All 356 existing tests, `make check` and `make reproduce` passed. Reproduction
preserved all 8,008 protected pre-existing tracked files byte for byte, including
the prior receipt. All eight input hashes and local document/heading links passed.

The following exact file hashes bind the record base and prior measurement/
methods rules. A/P passages retain the individual source IDs, locators and
raw/metadata/image hashes; their established checkers replay those bindings.

| Input | SHA-256 |
| --- | --- |
| `data/napoleonic/authority-v1/mappings.json` | `eb40cf4628603c46c3d3a4ad686b1112ea24e0507602f69e1571376114f9ebb7` |
| `data/napoleonic/boundaries-v1/records.json` | `a3227d0f7c71dcdb594202cb524f6d59b2ef8377bd9c7b8dfb2bf3e63797b278` |
| `data/napoleonic/peninsula-1812-measurement-v1/records.json` | `20623489a5f9b20cfcbf6b91cbab3bc5ce765ed0045b8f7487f4a783e0e8d514` |
| `docs/napoleonic-ledgers-v1.md` | `79641ce66734fd8084df0bdfb6533cec143404db58687d648af85b4c0eafb442` |
| `docs/napoleonic-methods-v1.md` | `fa87d34496e52e4f0a71f7ac7869ce396fdf2410da3cd902f158be7ad25ad8be` |
| `docs/research/napoleonic-measurement-feasibility-v1.md` | `59f2732d4d70457974d541e3b6ef34d0f9252911905917358709226deef856f7` |
| `data/napoleonic/methods-v1/evaluation.json` | `eae74dfcda9e5b14653882ae6a5ff03e79b8d6dfc76b291463d4792ce4fcd927` |
| `data/napoleonic/methods-v1/campaign-pilot.json` | `b0f24a4c21d02a3dcf623d16b8928d2f0bb8cb0c654823a125aa06f9d8ea6ffa` |

Stop after this specification and the six cases. Wider strict-opening extraction
remains paused. A useful next source task is the already identified
[1805 German-operations pilot](../data/napoleonic/methods-v1/campaign-pilot.json):
a bounded check of its pre-operation appointment/mandate and prior objectives
in the existing orders, before adding troop totals or outcome observations.
That would address its missing authority/window mapping, using the existing
source-family/follow-up ceiling and retaining nulls if it cannot be established.
It is a recommendation, not a source task executed or queued by this design.

No source fetch, historical extraction expansion, separate review, subagent,
second-opinion prompt, calibration score, synthetic job or historical fit ran.
The existing strict opening target, full cohorts, prepared packets and numerical
results retain their prior status. Campaign contribution remains distinct from
tactical effects and predictive residuals.
