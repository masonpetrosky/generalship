# Napoleonic measurement feasibility checkpoint v1

Primary-verified assessment of existing records, 2026-10-20. The owner accepted
the checkpoint after the two completed measurement groups. The assessment covers
**12 entries / 24 sides** and ends with a research-allocation recommendation.
It does not extend either group's historical research.

**Recommendation: pause wider strict-opening extraction. Define the operational
command unit and boundary-specific authority rules before another measurement
batch.** The existing records contain useful partial measurements, but none
establishes a complete joint opening mapping. More troop totals alone would leave
the common authority/entity problem unresolved. This is a recommendation about
the next task, not a change to the opening target or an approved historical run.

## Scope and what the result means

The strict target remains combat-unit personnel, including officers and artillery
crews, physically available in a defined local area immediately before first
hostile contact, including relevant outposts. Both sides need the same boundary
and population rule. A force/person association additionally needs evidenced
authority over that population at that boundary. See
[ledger design v1, sections 4–5](../napoleonic-ledgers-v1.md#4-opening-population-applicability).

The four Naples entries are the smallest complete development group. The eight
1812 Peninsular entries were selected by a bounded existing-page comparison.
Neither selection is representative. Their **12/273 development entries in two
of 13 groups** cannot estimate corpus-wide admission yield, historical error rate
or the cost of resolving another group. The **52 reserved-final entries in three
groups** supply no cases or numerical selection feedback here; the reservation
remains numerical, not historical blinding.

This is a synthesis of the primary-verified packages below. It inspects their
observations, scenarios, membership cases, authority reconciliations, side
blockers and checker rules. It adopts no new historical passage and does not
claim renewed facsimile inspection. The linked records retain the exact source
IDs, locators, quotations, interpretations and raw/metadata/image hashes.

| Package | Denominator and retained evidence | Established mapping limit |
| --- | --- | --- |
| Naples ledger, boundary and authority packages | Four entries / eight sides; 43 strength observations; 28 original command appearances plus two capitulation examples; 30 membership cases. Strength observations include components, non-personnel units and unknowns. | All eight joint opening mappings unresolved. Four source-local **person co-references** are supported; all 12 enumerated same-side inter-entry army-continuity pairs are `not_established`. |
| Peninsula 1812 combined measurement | Eight entries / 16 sides; 39 strength observations: 32 numerical and seven explicit unknowns; 43 authority appearances. | All 16 joint opening mappings unresolved. Six source-local **troop-total/role co-reports**, on six sides in six entries; none supplies both sides of an entry. No army-continuity pair inventory was performed here. |
| Combined assessment | 12 entries / 24 sides, retaining both sides of every entry. | Zero complete joint opening mappings established in these packages; zero admitted or emitted model rows. |

The strength-observation granularities differ between packages. The four person
co-references and six troop-total/role co-reports also measure different
relationships. Neither set is pooled into a yield or quality score.

**Zero emitted rows is partly imposed by the contracts.** In particular,
[`napoleonic_measurement.check`](../../generalship/napoleonic_measurement.py)
requires blocked side records and null boundary/strength/person/army selections;
its report fixes complete opening pairs and emitted rows to zero. The Naples
designs also prohibit promotion. Those output counts cannot serve as an empirical
test that opening reconstruction is impossible. The feasibility finding rests on
the substantive unresolved mappings documented below, rather than on null fields
or the success of a checker.

## What is reusable, and what would change applicability

| Requirement | Existing-record finding | Needed before the relevant next use |
| --- | --- | --- |
| Joint contact boundary and local area | Both packages record unresolved boundary/area membership for every entry. Source-relative encounters and later siege phases are already distinguished. | A definition fixed before selection, plus evidence locating the counted components on both sides. Qualitative ordering can suffice; an exact clock is not a universal requirement. Choosing an unopposed investment or later main assault would change the target. |
| Complete combat-unit population | Every side retains a substantive population gap: missing local headcount, partial categories, wider formations, mixed civilian/sick tables, later presence or unresolved persistence. | A usable source-specific quantity or documented component construction with compatible categories, locality and state. An original dated return is helpful evidence, not a universal documentary prerequisite. Correct arithmetic and a precise printed integer are insufficient. |
| Authority at the boundary | Local orders, garrison government, superior direction and delegation are useful observations. Their force scopes and times are not reconciled into one boundary-level responsibility mapping. | Specify which authority is being measured and resolve relevant competing scopes at that boundary. A complete lifetime biography, whole-siege tenure or exact later handover is not automatically required to record a local opening role. Campaign appointments have additional interval requirements. |
| Person and operational-entity identity | Global person/army selections remain deliberately null. Naples has unresolved cross-source identity hypotheses and no established inter-entry army links; the 1812 package has local associations rather than a global registry. | Define the entity level and evidence rules for aliases, containment, detachments, continuity, splits and merges before historical linking. Resolve only links needed for the intended analysis. Registry absence is not evidence that a reported troop count or local role is false. |
| Admission and estimation | These are non-promoting measurement packages. No historical outcome fit has run. | Separate profile/admission and run decisions. A local observation can be retained without a global registry; distinguishing commander from army effects needs a defended entity/identification design. A valid measurement still does not identify a causal effect. |

The seven explicit 1812 headcount unknowns occur on **seven distinct sides in
seven of eight entries**: `B430a-B`, `B430b-B`, `B430c-A`, `B431b-B`, `B432a-A`,
`B432b-A` and `B441a-B`. Their observation IDs are, respectively,
`B430a-B-s02`, `B430b-B-s02`, `B430c-A-s02`, `B431b-B-s02`, `B432a-A-s02`,
`B432b-A-s03` and `B441a-B-s04`. These are unknown **matched own-side local
counts in this evidence scope**, not claims that no source anywhere contains a
number, or that Bodart has no number. Badajoz, the remaining entry, still has
mixed-population and infantry-only alternatives. Merely relaxing the clock would
therefore leave consequential population work throughout this group.

## All twelve entries, including both sides

Side A is France and its allies; B is the opponent. The cells summarize existing
mapping records, not new historical adjudications. The record locators use the
stable array IDs or `battle_id`/`side` filters defined below. Every row also retains
unselected global person and army mappings; that shared design/registry issue is
not repeated as though each row supplied an independent historical failure.

| Naples entry | Boundary/area issue already recorded | A: reusable evidence and population/authority gap | B: reusable evidence and population/authority gap | Record locators |
| --- | --- | --- | --- | --- |
| `B370c` Campo Tenese | Earlier approach displacement is distinct from the main attack; following components' positions are unresolved. | Local reconnaissance and Reynier's orders; broader corps/concentration totals do not supply the complete local roster. Policy council and local direction have different scopes. | Local reconnaissance horse and main-position defenders; complete common-time population unresolved. Damas's source-local name link does not establish the joint opening mapping. | L: `B370c`; B: `ct-approach`, `ct-a-*`, `ct-b-*`; A: `campo-policy-and-local-direction`, `damas-within-koch`. |
| `B370d` Maida | Source-relative artillery exchange; date alternatives and final column/reserve location remain unresolved. | Infantry/cavalry components and local direction; artillery personnel and common-time completeness missing. Wider command and actual participation are different populations. | Marching rank and file and local orders; officers/all-arms coverage, reserves and later presence are unresolved. Distant tower guards are conditionally outside the local field area. | L: `B370d`; B: `m-field`, `m-a-*`, `m-b-*`; A: `maida-expedition-and-field`, `stuart-within-bunbury`. |
| `B371a` Gaëta | Initial rifle encounter has unresolved date/interval link; July battery opening is a later phase. | Before-place troops, detached bodies and mixed posts cannot all be summed as local opening personnel. Troop command, superior direction and delegated negotiation are separate. | Garrison estimates and later government/capitulation roles; initial population and succession/identity remain unresolved. Later prisoners are a different basis. | L: `B371a`; B: `g-initial`, `g-july`, `g-a-*`, `g-b-*`; A: `gaeta-command-and-delegation`, `gaeta-governor-succession`. |
| `B379c` Amantea | Investment is a non-contact marker; formal attack and Colletta's undated initial assault are separate unresolved scenarios. | Huard's investing component and later departing columns; concurrency/completeness unresolved. Broader command and local/column leadership need not be exclusive. | Regulars, insurgents and governed inhabitants; no complete assigned-combatant count. Whole-town population cannot substitute for defenders; Mirabelli's cross-source match remains a hypothesis. | L: `B379c`; B: `a-investment`, `a-formal`, `a-colletta`, `a-a-*`, `a-b-*`; A: `amantea-broader-and-local`, `mirabelli-cross-source`. |

For every Peninsula row, P's `entries[battle_id]` contains the boundary/area
findings, and its two `side_records[battle_id, side=A|B]` contain the specific
blockers and evidence IDs. The co-report IDs below identify the reusable local
associations; they do not identify opening candidates.

| Peninsula 1812 entry | Boundary/area issue already recorded | A: reusable evidence and population/authority gap | B: reusable evidence and population/authority gap | P co-report, if indexed |
| --- | --- | --- | --- | --- |
| `B430a` Ciudad Rodrigo | Preliminary redoubt operation and planned approach do not establish a joint first-contact state. | Mixed garrison table and reported governor; category coverage and persistence to contact unresolved. Diagnostic subtraction is not selection. | Wider source force and planned approach; matched own-side local headcount and local/subordinate authority unestablished. | None indexed. |
| `B430b` Altafulla | Approach force on the 22nd is not proven unchanged and available at contact on the 24th. | Mathieu's relief force/role are co-reported; full opening membership and effective scope unresolved. | Local headcount unknown; Eróles/Lacy battle-day scopes disputed. Later orders do not settle them. | `altafulla-mathieu` (A). |
| `B430c` Peñíscola | Approach/rejected terms and later bombardment are different markers; naval/land scope unresolved. | Siege battalions and Severoli's establishment; no matched own-side local people count. Organizational units are not people. | Garrison total and governor co-reported; category/time match and García Navarro/Pareia-Navarro identity unresolved. | `peniscola-garcia` (B). |
| `B431a` Badajoz | Earlier table and unopposed investment do not establish first hostile contact. | Mixed garrison table and retrospective siege figure; combatant classification/state and opening governor authority unresolved. | Beresford's investing bayonets co-reported; infantry-only and wider army totals cannot supply the same local all-arms force. Superior/local roles differ. | `badajoz-beresford` (B). |
| `B431b` Salamanca, June forts | Three forts and local investment are distinct from the wider field army; no joint first-fire mapping. | Garrison alternatives and Duchemin role; categories, common state and authority interval unresolved. | Clinton's investing division and Wellington's superior arrangements; no local people count or settled boundary-level responsibility. | `salamanque-duchemin` (A). |
| `B432a` Castalla | Ibi/Castalla sectors, reserve, support orders and later joining forces cannot be backdated into one opening force. | Local headcount unknown; Harispe, Delort and Mesclop have different reported tasks and phases. | Distributed versus advancing totals; Odonell/O-Donell labels and force role retained without a global merge or complete sector mapping. | `castalla-odonnell` (B). |
| `B432b` Salamanca, July field battle | Early dispositions, wound/succession and later attack narrative are distinct source-relative events. | Compiler components and Oman's reconstruction; matched own-side opening count and combatant/train/time scope unresolved. Marmont/Bonnet/Clausel succession is not one whole-entry commander. | National officer/men table and later attack task; complete common-time population and earliest-contact authority mapping unresolved. | None indexed. |
| `B441a` Burgos | Town occupation/detachment precedes frozen start; no complete first-contact mapping. | Castle garrison and Dubreton role co-reported; categories and contact-state correspondence unresolved. | Wider strategic availability differs from local besiegers; local headcount and subordinate scope unestablished. | `burgos-dubreton` (A). |

**Locator key:** L = [ledger examples](../../data/napoleonic/ledger-design-v1/examples.json),
filter `strength_records` by `battle_id`; B =
[boundary records](../../data/napoleonic/boundaries-v1/records.json), `scenarios`
and `membership_cases` by stable `id` (an asterisk means that ID prefix); A =
[authority mappings](../../data/napoleonic/authority-v1/mappings.json),
`reconciliations`/`identity_links` by `id`; P =
[combined measurement records](../../data/napoleonic/peninsula-1812-measurement-v1/records.json).
P's `observations` and `co_reports` supply the exact quantities and actor labels;
its `passages` preserve their citation/claim origins. B/A similarly link event and
role IDs to their adopted passages and immutable source snapshots.

Two examples illustrate why these are substantive mapping questions. P's `p048`
retains Oman's explicit unopposed-investment context (`oman-1914-t5-ocr-v1`,
printed p. 228); the previous pass did not equate it with first contact. A's
`p033` retains Gardanne's troop-command appointment alongside Masséna's visit
(`koch-massena-t5-p223-figures-v1`, section `p223`); its reconciliation did not
invent an exclusive handover. Their exact quoted passages and raw/image hashes
remain in the linked records. This checkpoint adds no claim about uninspected
original returns or pages beyond those prior packages.

## Research decision before further extraction

Continue preserving these local observations for the evidence explorer and future
compatible uses. A source-specific garrison/role association is useful even when
it cannot supply a strict opening pair. However, copying more such observations
into a ledger is not currently enough to justify scaling the strict target.
The Naples sequence has already separated quantities, boundaries/membership and
authority/continuity; the combined 1812 pass reaches the same classes of unresolved
mapping without that three-step sequence. This is qualitative workflow evidence,
not a measured cost comparison or a forecast of another campaign's yield.

**The next recommended deliverable is one operational-unit and authority
specification, bounded to the existing cases.** It should define:

1. The unit being compared: a command appointment over an operational force and
   window, with a separate containment relationship for army/corps/division/siege
   forces. A frozen source campaign group is an evaluation group, not an army ID
   or an appointment. State what persistence through detachments, splits,
   recombinations and changing commanders would mean before seeking links.
2. Which question each authority record can answer: local control at a specified
   contact, superior operational direction over an appointment, garrison
   government or delegated task. Keep unknown/joint authority possible. Require
   evidence appropriate to the question, rather than demanding complete tenure
   dates and a global identity merge before retaining any local fact.
3. A small set of required evidence transitions for future use, with an explicit
   unknown when the existing evidence cannot justify one. Work six already
   documented stress cases: Campo council/local direction, Maida expedition/field
   scope, Gaëta troop command/delegation, Amantea later columns, Castalla
   reserve/sector tasks and July Salamanca succession. These are examples of
   rule behavior, not new identity or continuity findings.

Stop after that specification and its six worked cases. Do not reopen historical
extraction, create a registry of assumed lineages or queue a new campaign merely
because fields remain null. Any later source task must name the particular
authority/entity or population mapping it could change and have its own bounded
scope. This recommendation preserves the stopped status of both measurement
groups; it does not authorize more historical research in them.

This order serves the project's campaign-contribution aim. The
[existing methods design](../napoleonic-methods-v1.md#1-what-campaign-contribution-would-mean)
already requires appointment boundaries, inherited state, prior objectives,
eligible replacements, non-battle opportunities and an identification argument.
Even perfect opening battle counts would not supply those. Do not silently use
commander-created concentration or preparation as inherited campaign controls,
or add battle residuals to campaign outcomes.

A broader source-reported engagement-strength diagnostic is a possible **different
target**, with population/phase alternatives and explicit exclusions. It could
answer descriptive or predictive questions; it would not establish campaign
contribution or commander-versus-army identification. This checkpoint does not
choose that track, relax the opening profile, select preferred figures, change
the 273/52 partition or authorize a fit. If the owner later chooses that product,
its target, admissible inputs and evaluation/run design must be fixed separately.

## Primary verification and reproducibility

This is a documentation-only assessment. No new extractor, scoring rule, admission
checker or test framework is introduced. Counts were recomputed from the linked
arrays, including the seven unknown-side IDs, six co-report sides, zero entries
with two indexed co-report sides and the 12 unresolved Naples continuity pairs.
The primary checked every table row against its cited existing records, including
the distinction between historical gaps and deliberately unselected fields.
Offline validation results are recorded in the
[research log](../research-log.md#measurement-feasibility-checkpoint-v1-2026-10-20).
All 356 tests, `make check` and `make reproduce` passed. Reproduction preserved
all 7,750 protected pre-existing data/artifact/code/test/protocol files, including
the prior receipt, byte for byte. All eight input hashes in this memo and its
local document/heading links were checked.

The exact assessment inputs below are SHA-256 file hashes. The package checkers
replay their prior source snapshots, passages, raw hashes and verification
bindings. Checksum replay verifies provenance and contract consistency; it cannot
prove historical entailment or the adequacy of the proposed estimand.

| Input | SHA-256 |
| --- | --- |
| `data/napoleonic/ledger-design-v1/examples.json` | `21b9059b4b6def3dfa032da0c514b9a34beaab13c47ee700907078270b6e840d` |
| `data/napoleonic/boundaries-v1/records.json` | `a3227d0f7c71dcdb594202cb524f6d59b2ef8377bd9c7b8dfb2bf3e63797b278` |
| `data/napoleonic/authority-v1/mappings.json` | `eb40cf4628603c46c3d3a4ad686b1112ea24e0507602f69e1571376114f9ebb7` |
| `data/napoleonic/peninsula-1812-measurement-v1/records.json` | `20623489a5f9b20cfcbf6b91cbab3bc5ce765ed0045b8f7487f4a783e0e8d514` |
| `data/napoleonic/methods-v1/evaluation.json` | `eae74dfcda9e5b14653882ae6a5ff03e79b8d6dfc76b291463d4792ce4fcd927` |
| `docs/napoleonic-ledgers-v1.md` | `79641ce66734fd8084df0bdfb6533cec143404db58687d648af85b4c0eafb442` |
| `docs/napoleonic-methods-v1.md` | `fa87d34496e52e4f0a71f7ac7869ce396fdf2410da3cd902f158be7ad25ad8be` |
| `generalship/napoleonic_measurement.py` | `dffa9f0cc79fa59adb212588e3d9c9cf10cea7be7248fa252d9757ccaf44aace` |

Earlier records, raw sources, dossiers, prepared packets and numerical results
retain their bytes. Calibration stays prepared/unscored. The assessment is
primary-verified; no subagent, separate review, second-opinion prompt, new source
fetch, synthetic job, feature admission or historical fit ran.
