# Command-responsibility ledger v2, separate review, batch 1 of 8

**Outcome: corrections required (R1, R2).** Advisories: A1–A11.

This is an AI review: a separate analysis of extraction against the registered passages. It is
not historical adjudication, independent corroboration, feature admission or authorization of any
fit or rating run.

## Reviewer and inputs

| Item | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`, separate subagent started with fresh context for this assignment. The harness did not give the reviewer a task ID. |
| Date | 2026-09-25 |
| Prepared commit reviewed | `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372` (against `96110cf`) |
| Bundle commit / worktree HEAD | `1b6b83012d485fe9170b9aa5807da9a0b1509884`. `git diff 11d4bc3 HEAD` touches only this bundle's `assignment.md` and `inputs.json`. |
| `assignment.md` sha256 | `c553426f1096c48b7241681b6b84e331f371b4520fefd518d2fb3b5a848f5ed8` (matches) |
| `inputs.json` sha256 (input manifest) | `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0` (matches) |
| 25 bound inputs | All 25 match `inputs.json`, both at `git show 11d4bc3:<path>` and in the worktree. No mismatch. |

Key bound hashes (full):

- `data/command/responsibility-v2.json` `1271ea87f72a3c57d88a99ccf2fc2d6f36e03730570ab20dbdfaea9a5546753a`
- `data/command/commanders-v2.json` `cdf72348c809256c80fd77a03b3afc8371bcfa96e1c0e89fc7113ffb9ebe267c`
- `data/raw/cwsac_battles.csv` `952b5d08402a7b77a42de709a87cd96540e460dd6fd4911d30574b5ad3585f1f`
- `data/raw/cwsac_commanders.csv` `6c587c2987171764f362513f31eaf7c713b888b806419291c494623ea41800c7`
- `docs/research/ledgers-v2.md` `e9986d9b9728ed08a099fa8f821395e8993c8284292ca67eb7fd52087aa85030`

**Binding observation (not a mismatch).** The assignment tells the reviewer to read the addendum
`docs/ledgers-v2.md`, the design `docs/commander-ratings.md`, the v1 memo and
`generalship/command.py`. `inputs.json` does not bind these four files. Instead it binds
`docs/research/ledgers-v2.md`, which is the extraction record, not the addendum. I read the
worktree copies, which are identical to the prepared commit, and recorded their hashes:

| File | sha256 |
| --- | --- |
| `docs/ledgers-v2.md` | `a7e05ddfc072c493f8f9152064e444e4b285e070a7dfcdbd279e80fc4aa49eb1` (equals the ledger's `bindings.addendum`) |
| `docs/commander-ratings.md` | `0ab4b7d541baf4f8e642634f316628f9cb372d68dcdbbc047a305f5a1fb704bb` (equals `bindings.design`) |
| `docs/research/command-responsibility-v1.md` | `208b796a3f60ffc869a6686a12241a4356b4e94655128fb84bc88433dc33d0dd` |
| `generalship/command.py` | `58ffe17ebc42cc3d2ec5950e55d56a243caf662460df86059c845ade62ef6954` |

Future bundles should bind these files.

## Commands run (offline)

- `make check`: 143 tests passed (`OK`) and exit status 0. The embedded command check reports
  A 512, B 21, C 68, D 9, and nesting 4 nested / 10 not nested / 2 unresolved.
- `python3 -m generalship command-check --ledger data/command/responsibility-v2.json`: exit 0,
  305 engagements, 610 sides, the same grades, 401 registry commanders, `rated: false`.
- I ran no build, packet or evaluation commands and modified no primary artifact.

## Coverage actually inspected

- **Ledger and dossiers.** All 28 assigned engagements, both sides (56 sides): the ledger entry,
  the frozen CWSAC description and commander rows, the dossier `command-roles` claims, and every
  registry entry these sides use, including merges and passage-only entries. For all 28 I also
  read the dossier source lists and open questions.
- **Source sections read in full:**
  - Morris (Philippi); Rust and Reynolds (Cheat Mountain);
  - Pierce and Magruder (Big Bethel);
  - Snead's Booneville and Carthage sections;
  - Atchison and Scott (Blue Mills); Lane (Dry Wood) and Britton's Dry Wood section;
  - Plummer (Fredericktown); T. J. Jackson and Patterson (Hoke's Run); Zagonyi (Springfield);
  - Stringham and Martin (Hatteras);
  - Schoepf (Camp Wildcat); Torrence and Turner (Roan's Tan Yard).
- **Read in part or through keyword passages:**
  - Nicolay (Sumter, and Manassas/Blackburn's Ford/Bull Run);
  - Snead's Wilson's Creek sections; Britton's Lexington, Springfield and Mount Zion passages;
  - Beauregard (Blackburn's Ford); Pegram; Stone (Ball's Bluff); Ord (Dranesville); Pillow (Belmont);
  - Williams (Ivy Mountain) and Nelson; Anderson and Brown (Santa Rosa Island);
  - Stuart (Dranesville); Zollicoffer; Rosecrans; Floyd and Wise (Kanawha).
- **Presence check only, context not read:** the passages from Grant (Belmont), Price
  (Lexington), Prentiss (Mount Zion), Lyon (Boonville), Sigel (Carthage), Sturgis (Wilson's
  Creek), McDowell (Bull Run), Thompson (Fredericktown), Evans (Ball's Bluff), Anderson
  (Sumter, OR I) and the NPS pages beyond the frozen description.
- **Nesting.** The one contained-interval pair that involves this batch, MO006/MO003, compared
  with the reviewed nesting precedents in the same ledger.
- **Out of scope:** the strength ledger, other batches and the 91 carried-forward v1 entries. I
  opened MO006's strength entry only to understand the nesting pair. I did no new research and
  opened no new source family.

## Summary by engagement

"OK" means the choice, rule, grade, labels, candidates and echelon follow from the inspected
passages under design §2 and the addendum.

| Engagement | US | Confederate | Notes |
| --- | --- | --- | --- |
| SC001 | OK | OK | |
| WV001 | OK (Kelley, 2 C; Dumont successor; Morris superior and candidate) | OK | A7 |
| WV003 | OK (McClellan, 3a A; alternative recorded) | OK | |
| WV004 | OK | OK | A7 |
| WV006 | OK | OK | |
| WV005 | OK | OK (Lee, 3a A) | |
| VA003 | OK | OK | A5 |
| MO001 | OK | OK | A8 |
| MO002 | OK | OK | |
| MO004 | OK | OK | |
| MO005 | OK | OK (3b C) | A3 |
| MO006 | OK | OK | nesting: A10 |
| MO003 | OK | OK (grade A is thin) | A2 |
| MO007 | OK | OK | |
| MO008 | OK | OK | |
| WV002 | OK | OK | |
| VA004 | OK | OK | A6 |
| VA005 | OK | OK | |
| NC001 | **R1** | OK | A1 |
| KY001 | OK | OK | |
| KY002 | OK | OK | A9 |
| KY003 | OK | OK | |
| FL001 | OK | OK | |
| VA006 | OK | OK | |
| VA007 | OK | OK | A11 |
| MO009 | OK | **R2** | |
| MO010 | OK | OK | A4 |
| MO011 | OK (2 C, Hubbard candidate) | OK | |

## Required corrections

### R1: NC001 US, citation missing for the premise that decides the choice

The rationale chooses Stringham under rule 2's third bullet because he "commanded the force
engaged when the fighting began". None of the side's citations states that Stringham commanded
the squadron:

- "At 10 o'clock the Wabash and Cumberland opened tire on Fort Clark" names ships, not a commander;
- "Major-General Butler took passage in this ship" is about Butler;
- the NPS and Martin quotes name Butler and Stringham jointly.

The registry's passage citation for Stringham (NPS, "Flag-Officer Silas Stringham") also does
not state his command. The stating passage exists in a source the dossier already cites, in the
same section as dossier `command-roles` citation 4. I verified that it resolves.

- **Change.** Add to `engagements[NC001].sides.US.citations`:

  ```json
  {"source_id": "orn6-stringham-hatteras-selections-v1", "section": "stringham-1861-08-30", "locator": "p.120 (OCR page markers; not checked against print)", "quote": "Articles of capitulation between Flag-Officer Stringham, commanding the Atlantic Block¬ ading Squadron, and Benjamin F. Butler, U. S. Army, commanding", "battle_id": "NC001"}
  ```

- **Rationale.** After "(Stringham's journal)", add: "The articles of capitulation style
  Stringham 'commanding the Atlantic Blockading Squadron' and Butler 'commanding'."
- The grade (C), candidates and labels are unchanged by R1. On the label, see A1.

### R2: MO009 Confederate, successor and superior identity asserted on surname alone

Pillow's report names "Major-General Polk":

- "Under instructions delivered in person by Major-General Polk";
- "The pursuit was continued under the immediate command and direc tion of Major-General Polk".

The ledger maps this officer to `cs-polk`, the v1 passage-only entry for KY009. That entry's only
evidence is Cist's "The enemy's troops engaged in the battle were under the immediate command of
General Polk." No listing field or inspected passage ties the Belmont "Major-General Polk" to
KY009's "General Polk" or to the MS012 listing "Leonidas Polk". Reusing an existing ID for a new
passage name is a merge. The addendum requires a merge to rest on listing fields or a passage,
and the extraction record says "Surname-only matches stay separate (Polk, …)". The rationale's
"a merge … is proposed in the report" also refers to a document that is not bound.

- **Change 1.** Add to `data/command/commanders-v2.json`:

  ```json
  {"id": "cs-polk-mo009", "name": "Polk", "side": "Confederate", "cwsac_names": [], "passage_citation": {"dossier": {"claim_id": "reported-force-scope", "citation_index": 5}, "source_id": "or3-pillow-belmont-selections-v1", "quote": "Under instructions delivered in person by Major-General Polk", "battle_id": "MO009"}}
  ```

- **Change 2.** In `engagements[MO009].sides.Confederate`, set `successor` to `"cs-polk-mo009"`
  and `superior` to `"cs-polk-mo009"`.
- **Change 3.** Replace the rationale's last sentence ("Polk uses the v1 passage-only entry
  'cs-polk' (KY009), taken as the same Major General Polk; a merge with the listing 'Leonidas
  Polk' (MS012) is proposed in the report.") with: "Polk is a passage-only entry for this record
  ('Major-General Polk' in Pillow's report). No inspected passage or listing field identifies him
  with KY009's passage-only 'General Polk' or the MS012 listing 'Leonidas Polk', so he stays
  separate under the addendum's surname-only rule."
- **Alternative.** If the primary finds a passage in an already-cited registered source that
  gives the full name or matching initials, record that as a `passage_merges` entry on the
  listed commander instead.
- Pillow's choice, grade A, `command_changed` and `superior_directing` are otherwise supported.

## Advisories (no change required)

**A1. NC001 US, the `joint_command` label under rule 2.** The design defines `joint_command` only
under rule 5, where several listed commanders are in different services. Here only Butler is
listed. This is the only non-rule-5 use of the label in the v1 and v2 ledgers. The passages do
show joint command: NPS says "led by" both, Martin names both, and both signed the articles. So
the label is descriptive, but the primary should record it as a design interpretation.

The choice of Stringham is defensible. Both sources put the squadron's fire before the 11.30
landing: Stringham at 10 o'clock, Martin "between 8 and 9 o'clock". That clock difference could
be noted. The alternative keeps the listed Butler as commander of the expedition. It is also grade
C, and the rationale records it.

**A2. MO003 Confederate, grade A.** Grade A rests on two phrases: the frozen description's "his
force crossed the Missouri River", and Atchison's own ambiguous "The men of our command". Against
them, the compilers footnote "No record of his official status", and Atchison's report shows him
delivering Price's orders to columns under Saunders, Wilfley, Patton and Childs. The rationale
keeps these doubts visible. A stricter reading of "states that the officer commanded" would not
give A. Grade B would need listing-only citations, so the alternative is to read the description
as the stating passage, which is what the ledger does. Leave it at A only if the primary accepts
"his force" as a statement of command.

**A3. MO005 Confederate (3b, C).** The rationale says no passage shows who directed the fight. It
could add the compiler footnote in Lane's selection (dossier `casualty-records` citation 3, same
section): "From a return of casualties in the Eighth Division Missouri State Guard, Brig. Gen.
J. S. Rains cornmandiDg, it appears that the Confederate loss in this action was 4 killed and 16
wounded." It supports Britton in placing the engaged force in Rains's division. Price's presence
at the head of the army, rule 3(b), and grade C are unaffected.

**A4. MO010 Confederate, timing scope.** The Britton quote "Colonel Dorsey threw for- ward a
superior force to attack him" describes the December 27 skirmish with Captain Howland near
Hallsville. That is outside the frozen interval (1861-12-28). The command at first combat on the
28th rests on the frozen description ("Dorsey's Rebels"). Suggested rationale wording: "Britton
puts the force under Dorsey on December 27 (Howland's skirmish, outside the interval)."
Grade A still follows from the description.

**A5. VA003 US, citation support.** "I rode back, ordered them to cease firing" concerns the
night friendly-fire at New Market Bridge, not "the attack and retreat". Add "Shortly after I
directed all the forces to retire." (dossier `command-roles` citation 7). A passage showing
Pierce ordering the attack dispositions could also be added from the same section, for example
"I directed Colonel Townsend, with his regiment, to advance".

**A6. VA004 US.** The rationale relies on Nicolay, but the side cites only the listing and the
description. Add dossier `command-roles` citations 5 and 6: Tyler "heeded his instructions";
"Upon hearing the cannonade, McDowell had immediately ordered all the divisions forward to
Centreville". Then the Tyler reading and the absence of McDowell from the ford are cited.

**A7. Stale references to "the report".**

- **WV004 Confederate.** The rationale says "'John Floyd' and v1 'John B. Floyd' are proposed as
  one person (report)". The registry has already merged them on listing fields (`merge_basis`
  present), so say "merged on the listing fields".
- **WV001 US.** "the listing 'Benjamin F. Kelley' exists at MD008 (merge proposed in the report)"
  should go. MD008 is Inconclusive and outside the ledger, and the registry has no "Benjamin F.
  Kelley" entry.

**A8. MO001 Confederate, superior identity.** The superior "the Governor" is mapped to the
listing "Clairborne Jackson" (MO002). The supporting passage is the MO001 frozen description,
"Claiborne Jackson, the pro-Southern Governor of Missouri", which I verified resolves. Add it to
`superior_citations` so the identity rests on a cited passage.

**A9. KY002 US.** The stating evidence is thin: the description's "his men" and Schoepf's
"our men, under the immediate command of Colonels Coburn and Wolford". Consider adding
Schoepf's "I can hold my position with my present force against an equal or superior number"
(dossier `stated-aims` citation 2). The echelon `brigade` describes only the reinforcement
Schoepf brought; the description puts the combined force at about 7,000. `unknown` may be more
exact.

**A10. MO006/MO003 nesting (`not_nested`).** The reason itself records that the force scopes
partly overlap. Two reviewed precedents in this ledger treat such partial overlap as
`not_nested`: VA026/VA025, and WV010/MD002. The outcome is therefore consistent. The reason could
add Atchison's "I delivered your orders to the above commands to hasten to this point
(Lexington) with as much dispatch as possible." (MO003 dossier `stated-aims` citation 0).

Across batches, LA010/LA009 is `nested` on force scope alone, while partial overlap gives
`not_nested`. The primary may want one stated rule for this, but that is outside this batch.

**A11. VA007 US.** Ord reported to McCall and "He was so kind as to direct me to continue". That
supports reading McCall's arrival as a superior taking command (rule 4), and it equally supports
reading it as superior direction without relief. The pair of labels is defensible. The grade is
unaffected.

## Checked and found sound (selected)

- **Army commander chosen over the subordinate who led the fight.** WV003 US (McClellan over
  Rosecrans), VA004 both sides (McDowell over Tyler; Beauregard over Longstreet), VA006 US (Stone
  over Baker), MO004 Confederate (McCulloch over the senior-listed Price, by Snead's account of the
  turnover) and VA005 Confederate (Johnston "as ranking officer assumed command") all follow design
  §2's "command authority, not location" and the MS006 example. Each rationale records the
  alternative reading.
- **Choices away from the listing.** WV001 US (Kelley) and MO007 US (Plummer; Carlin "reported to
  me in person for orders") read their passages correctly.
- **Successors and first combat.** The following labels are supported:
  - MO004 US: Sturgis ("The command devolved upon Major Sturgis");
  - NC001 Confederate: Barron ("consented to take charge", evening of the 28th, after first
    combat);
  - WV001 US: Dumont ("by the fall of Colonel Kelley, had command");
  - MO009 Confederate: Polk takes command of the pursuit (the identity question is R2).
- **Superiors.** These are orders for the specific operation and are labelled:
  - Butler at VA003 ("the original design of General Butler");
  - Sweeny at MO002;
  - Grant at MO007;
  - Sturgis at MO003;
  - Zollicoffer at KY001;
  - Thomas at KY002;
  - Fremont at MO008;
  - Pope at MO011.

  These are departmental or unnamed and are correctly left unlabelled:
  - Fremont at MO006;
  - "headquarters Saint Louis" at MO009;
  - Halleck at MO010;
  - Johnston's adjutant at WV002;
  - "the general commanding" at FL001;
  - Lee "during the month" at WV004.
- **Registry merges.** These merges on listing fields fit the addendum rule:
  - "John Floyd" / "John B. Floyd";
  - "Benjamin Butler" / "Benjamin Franklin Butler";
  - "Richard Anderson" / "Richard H. Anderson";
  - "Gideon Pillow" / "Gideon J. Pillow";
  - "D.H. Hill" / "D. H. Hill".

  Each has the same side and surname, and the given names differ only by an omitted middle
  name or initial, as in the addendum's Wright example. "S. D. STURGIS" matches the listing's
  initials. The passage-only entries used here (Kelley, Dumont, Sweeny, Stringham, Barron,
  McCall, Hubbard) each carry a resolving citation and are not merged. The listing's "James
  Zagonyi" and "James Frazier" differ from the description's "Charles" and "Julian"; the
  rationales note this and assert no further identity.
- **Nesting.** MO006/MO003 is the only contained-interval pair involving this batch. The checker
  confirms that exactly one outcome is recorded.

## Unresolved items (kept visible, not corrections)

- **WV001.** When Kelley's and Dumont's columns joined; Morris says they were fifteen minutes
  apart.
- **MO003.** Atchison's official status.
- **MO011.** Whether Turner's "he attacked" covers the whole column.
- **MO008.** White's role before the charge.
- **VA004.** Whether McDowell intended the Blackburn's Ford attack.
- **NC001.** The clock of the first naval fire.

These rest on interested or retrospective accounts, which are single families per side as the
dossiers record, and inspected sources do not settle them.
