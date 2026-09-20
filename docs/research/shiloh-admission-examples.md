# Shiloh feature-admission design examples

These cases exercise the proposed [contract](../feature-admission.md), not an
admission engine. The [structured examples](../../design/feature-admission-v1/shiloh-examples.json)
bind the exact contract bytes, dossier, registry, cohort and baseline. They
retain claim/quantity/event IDs and 115 citation occurrences with exact quotes,
locators, raw SHA-256 and complete source-entry metadata hashes. The evidence
snapshot is commit `e92eefd5dad99e019fd2f905a2fd9b46053db47f`.

The proposed opening target is April 6 before first hostile contact. Its precise
contact definition, spatial scope and availability mapping remain unresolved;
neither tactical nor campaign replacement time has been established. Each case
also identifies its own population, time or use restriction. Solving a boundary
alone would not make these observations usable.

## Worked cases

Expected statuses below are design judgments about the proposed uses, not
computed validator decisions. A case may reference several observations to
illustrate a disputed or invalid transformation. The observations themselves
remain unchanged in the draft dossier.

| ID | Proposed use / evidence | Expected disposition and reason |
| --- | --- | --- |
| S01 | Use NPS 65,085 US / 44,968 CS as opening strength | Excluded: whole-engagement population includes later participation. |
| S02 | Turn the 44,895 paper return, including Wallace's 7,564, into an opening total | Blocked: paper strength, omissions, mixed dates and boundary mapping need review; subtraction does not solve them. |
| S03 | Treat p.112 summary, detail and facsimile as corroborating 5,463 | Blocked for opening use; they represent one return, not independent votes. |
| S04 | Treat Confederate 40,335 / 38,773 as an opening range or scenario pair | Blocked: composition, muster timing and Monday-arrival accounting are unresolved. |
| S05 | Use after-battle 29,636 / 32,212 or reverse them with casualties | Excluded: post-boundary state and derivation. |
| S06 | Use Reed's 7,545 with its estimated 735 component as an opening total | Excluded: mixed-phase reconstruction; adding the component also double counts. The separate 735 observation remains a candidate requiring population/time review. |
| S07 | Average or choose McCook's 7,553 / 7,552 | Excluded for April 6 opening: April 7 participation; preserve the printed discrepancy. |
| S08 | Use Ohio's 17,918 and component/April 30 return values | Excluded: later participation, mixed-date derivation and nested populations. |
| S09 | Substitute Nelson/Grose 600, about 400, 380 or 4,541 for an exact crossing count | Excluded for opening use: differing contingents and later phases; exact Sunday crossed strength remains null. |
| S10 | Convert Ammen/Crittenden dates into opening availability or completed readiness | Excluded: reinforcement events and unsupported readiness completion; keep report, diary, arrival and debarkation distinct. |
| S11 | Turn unknown logistics into a supply/readiness feature | Excluded: no supported numerical profile; null evidence remains visible, never zero or normal. |
| S12 | Attribute fortification/command changes as causal commander credit | Excluded: causal profile unsupported; authority, receipt and effective transfer unresolved. |
| S13 | Use the recorded Union victory as a predictor | Excluded: target leakage; preserve it in a separate outcome channel. |

For example, the p.112 abstract's citation is
`or-union-return-april4-5:p112`; its finer Sixth Division transcription is
`or-union-return-detail-v3:p112` and its image is `or-union-return-scan`.
The metadata revision changes dependence information without creating a new
historical witness. The structured file binds all three entries and raw hashes.

Reed's `reed-1909-ohio-strength-v1:p100` prints McCook's 7,553;
`:p102` prints 7,552 and the 17,918 recap. The `:p111-note-j` passage explains the
mixed March 20, March 31 and April 30 reconstruction and quotes Buell's estimate.
Their inclusion here preserves the discrepancy; neither is selected as truth.

Crittenden's `or-crittenden-reinforcements-v1:p355` reports about 21:00 arrival,
then debarkation as soon as practicable, and positioning about 05:00 the next
morning. Ammen's `or-ammen-crossing-v2:p328-report` belongs to his April 10 report;
`:p330-diary` and `:p333-diary` have null document-composition dates. The structured
references preserve those nulls rather than borrowing the report date.

## Coverage and limits

There are **13 cases**, referencing **26/62 claims, 27/40 quantities and 8/26
events**. The 115 quote occurrences resolve to 29 distinct source/locator pairs;
21 source entries are bound including linked facsimiles. Quote membership and
hash checks establish reference integrity, not entailment or historical truth.
This design pass does not claim new image-transcription review. The original
bounded source review still leaves 35/65 cited source-section pairs text/CSV-only.

There are **zero admitted features and zero emitted rows**. The frozen frame
remains 127 engagements / 36 campaign groups; the baseline remains 23 eligible
engagements / 13 groups with Brier 0.2768816348133779 versus equal odds 0.25.
The examples are purposive design checks, not an accuracy sample. They cannot
establish source reliability, a canonical opening strength or command effects.

Positive admission behavior is specified using explicitly synthetic fixtures in
the contract's implementation acceptance matrix. No historical positive example
or reviewer approval has been fabricated to make the design appear complete.
