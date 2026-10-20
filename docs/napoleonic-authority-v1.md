# Naples person, authority and army-continuity mapping v1

Primary-verified measurement work, 2026-10-19. The owner accepted the next bounded
step after [opening-boundary v1](napoleonic-boundaries-v1.md): the same four
development entries/eight sides, with existing pinned evidence only. This does
not admit features, select a responsible person or fit a historical outcome.

## What is being mapped

Keep three relationships separate:

1. **Person reference:** which literal labels a source uses for an actor. A
   source-local co-reference can join a full name and shortened label in one
   continuous episode, or a document's named principal and signature. It does
   not supply a project-wide person ID or establish another author's identity.
2. **Authority:** what that actor is reported to control, at which event or
   phase. Orders, troop command, superior direction, visits, garrison government
   and a delegate's negotiating powers have different scopes. Neither rank nor
   a compiler's single-name entry resolves the opening commander.
3. **Army continuity:** whether an operational entity continues across entries,
   at a fixed organizational level, through composition and command changes.
   A recurring commander, corps numeral, national label, shared campaign or
   similar troop total does not prove it. A corps, field division, siege force
   and wider army must not be silently interchanged.

The mappings index all 28 immutable command-role observations from
[ledger design v1](napoleonic-ledgers-v1.md). Two additional examples use the
already pinned Gaëta capitulation: Masséna's explicit siege-corps command and
Franceschi's delegated negotiating powers. These are 30 role appearances, not
30 distinct people, exhaustive command extraction or a usable command ledger.
Appearance IDs are bookkeeping handles, not resolved person IDs.

Each appearance retains its original label, force scope and source-specific time,
with the reported authority category, relevant boundary scenario and concrete
remaining gap. Missing appointment starts, ends and effective transfer times stay
null. A known appointment day or a dated capitulation is retained as reported
text, without inventing an intraday clock or backdating authority to first contact.

All eight side mappings retain null selected boundary, strength, person and army.
The same boundary and population rules apply to both sides. Even a supported
authority claim cannot resolve the missing complete opening force population.

## Source findings

### Campo Tenese

Koch p.173 separates the council presided over by Joseph, attended by Masséna,
from Reynier's operational task and Roger de Damas's left-corps command. His
pp.174–175 describe Reynier's local movement and orders, and Damas's position.
The fuller and shorter Damas labels are linked within that continuous Koch
episode. This is a source-local co-reference, not an automatic match to all
printed Damas references or an approved command selection.

The council's wider directive is not the same authority scope as local tactical
direction. Exact component membership at the earliest local approach contact
remains unresolved. The cavalry commander called Franceschi on p.176 is not
automatically identified with the Franceschi who signs Gaëta's capitulation as
a staff officer and delegate on p.422.

### Maida

Bunbury pp.235 and 240 use Sir John Stuart for the expedition decision and
reconnaissance/posting orders in the same episode. That source-local link is
supported. Bodart's Sir J. Stuart and Koch's Stewart remain explicit cross-source
identity hypotheses; they are not silently normalized. Koch pp.189–190 reports
Reynier assembling/directing his division and Stewart's field dispositions.
The existing 4/5 July date alternatives are retained.

An expedition decision, an order before the march and a local field order have
different temporal and force scopes. None supplies a complete boundary-matched
opening force/commander pair. Repeated Reynier labels at Campo Tenese, Maida and
Amantea alone do not prove either a global person match or army continuity.

### Gaëta

Koch p.196 describes Lacour's brigade/negotiations and the prince de Hesse's
garrison government. His p.223 reports Gardanne taking command of the siege
troops on the 17th, in the May context; the following day Masséna visits with the
troop commander and the artillery/engineer commanders. A superior's visit does
not establish Gardanne's dismissal or an exclusive handover. Page 229 describes
reports from Gardanne and the marshal's later headquarters at Castellone; no
exact transfer time follows.

The translated capitulation on p.422 names Masséna as commander of the siege
corps, Franceschi as his fully empowered delegate, and François Hotz as commander
of the place and acting governor, with representatives empowered by him. The
document is dated **18 July 1806, 11 in the evening**. The principal/signature
links for Masséna and Hotz are supported within this document. Its date is a
document/event locator, not either person's appointment start or transfer time.
Delegated negotiation is not proof that Franceschi commanded the whole siege.
The source states that it is translated from the Italian; no original is supplied.

Colletta p.30 calls the acting successor Storz after the prince's wound. Neither
the Hotz/Storz correspondence nor the cross-source Hesse/Philippsthal/Philipstadt
identities are settled here. Preserve the literal alternatives and unknown
effective times. The later capitulation roles cannot be assigned to the initial
rifle encounter or March construction merely because they concern the same siege.

### Amantea

Koch pp.281–282 separates the marshal's dispositions, the statement that command
devolved by right on Reynier, Huard leading the investment on the 18th, Verdier's
later departing column, and Reynier directing siege operations. The broader
command statement and local investment leadership can coexist. Neither the
marshal's departure nor the order of these sentences supplies an exclusive,
effective transfer clock over the complete local force.

Mirabelli's garrison authority is reported by Koch p.280 and Colletta pp.31–32,
but complete population membership and continuous authority at a defined first
contact remain unestablished. Cross-source Mirabelli and Verdier references stay
identity hypotheses. Retain boundary v1's qualification: Colletta's initial dawn
assault is undated, a later night assault is explicitly in December, and his
return follows December. Do not align these automatically to Koch's earlier attempt.

## Organization and continuity

Koch p.169 explicitly describes an army reorganized into three corps, the 1st
under the marshal with troops detached for Gaëta's blockade, and the 2nd under
Reynier for Calabria. Page 187 distinguishes the 1st corps' occupation and
blockade demands. The Gaëta capitulation gives Franceschi a staff office in the
1st corps of the French army in Naples. These are source-reported organization
and office relationships. They do not make every siege troop a member of that
corps or turn a staff title into a persistent army identifier.

The eight local force handles preserve the scope differences without becoming
army IDs. All **12 same-side inter-engagement pairs** (six per side) receive an
explicit continuity disposition. All remain `not_established`: the inspected
passages do not establish a fixed army-entity level, complete lineage through
reorganizations, or the necessary transfer/continuity evidence. This is absence
of an established mapping, not proof that every pair involves different armies.

The army definition must be defended before a future registry is installed:
wider institutional command and local troop lineage can yield different
identification problems. No choice between them is made to improve a model fit.

## Records and verification

[Mappings](../data/napoleonic/authority-v1/mappings.json) hold exact passages,
English interpretations, raw/metadata/image hashes, all role appearances,
identity hypotheses, organizational context, force handles, pair dispositions
and the eight side-level blockers. They reuse the two immutable source snapshots
already bound by earlier work. A small supplement freezes additional **existing**
metadata; no raw file, source registration or dossier changes. Source families
remain within the original three-family ceiling per entry.

The standalone offline standard-library checker replays both parent contracts,
requires exact role/side/pair accounting and retained unknowns, and rejects
cross-source or cross-entry links labelled source-local, invented appointments,
automatic person/army selections and emitted model rows. Structural validity is
not proof of entailment, historical truth, source independence or model identification.
The [primary record](../data/napoleonic/authority-v1/verification.json) binds the
actual sources, mappings, design and checker/tests; this is not separate review.

`make check` includes the new checker; `make reproduce` regenerates its report.
`python3 -m generalship.napoleonic_authority` checks without writing; `--write`
regenerates only the new [report](../artifacts/napoleonic-authority-v1.md).
Earlier code, records, reports, prepared dossier packet and model inputs retain
their bytes. The legacy general receipt includes the new module/data; this
standalone checker verifies its own report. Calibration remains 47 prepared,
unscored tasks; the 273/52 development/final reservation and prior results remain.

## Stopping decision

Stop this four-entry measurement pilot here. Authority and organization evidence
are now explicit, but all eight complete opening force/person/army mappings are
still blocked and no complete candidate engagement is emitted. More local detail
without a specific admission decision would exceed this task's purpose.

The next useful action is a mechanical blocker inventory across the 273
development entries, grouped by complete campaign, to identify reusable evidence
and choose the next bounded measurement batch. It should report what is present
and what needs inspection, without claiming semantic reconciliation, opening the
52-entry final reservation for model selection, or restarting historical deep dives.
