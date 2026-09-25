# Command-responsibility ledger v2, batch 2 of 8: separate review

**Outcome: corrections required.** Required findings: R1–R4. Advisories: A1–A9.

## Record

| Item | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), `high` reasoning effort, separate subagent with fresh context (evidence-reviewer role) |
| Date | 2026-09-25 |
| Prepared commit reviewed | `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372` |
| Previous commit | `96110cf` (`96110cfad1ea80f4b0462947d9f9b5a98a4e71f5`) |
| Worktree / bundle commit | `1c6e0eba9c23ee03475d2055d99012a832dd1bb8`. Relative to `11d4bc3` it adds only the batch 1 and batch 2 review-assignment bundles. |
| Assignment | `assignment.md`, sha256 `87fa8d01e50d0f2de524e6f13c2287861c9c505aebb8d89cc7a6e77634f3cc5a` (verified) |
| Input manifest | `inputs.json`, sha256 `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0` (verified) |
| Bound inputs | All 25 paths match their `inputs.json` hashes at `git show 11d4bc3:<path>` and in the worktree. No mismatch. Key files: `responsibility-v2.json` `1271ea87…753a`; `commanders-v2.json` `cdf72348…267c`. |
| Read but not bound in `inputs.json` | The assignment names these files, but `inputs.json` does not bind them. Hashes are from the worktree, where they are unchanged since `11d4bc3`. `docs/ledgers-v2.md` `a7e05ddf…9eb1` and `docs/commander-ratings.md` `0ab4b7d5…04bb` both match the ledger's own bindings. `docs/research/command-responsibility-v1.md` `208b796a…dd0d`. `generalship/command.py` `58ffe17e…6954`. The assignment refers to the addendum as `docs/ledgers-v2.md`, but `inputs.json` binds the extraction memo `docs/research/ledgers-v2.md`. I read both. |
| Dossiers | All 25 assigned `data/evidence/<ID>.json` files match their ledger bindings. |
| Checks run (offline) | `make check`: 143 tests, OK, exit 0. `python3 -m generalship command-check --ledger data/command/responsibility-v2.json`: exit 0 (305 engagements, 610 sides, A 512 / B 21 / C 68 / D 9, 401 commanders, nesting 4 / 2 / 10). I ran no build, packet or evaluation command. I modified no primary artifact. |

**Scope actually inspected.** I checked all 50 sides of the 25 assigned engagements: NM001, NM002, AR001, GA001, LA001, LA002, SC002, SC003, AR002, FL002, AR003, LA003, LA004, MO013, MO014, MO015, MO016, OK004, MO017, TX001, TX002, FL003, LA005, AR004 and AR005.

- **Ledger and listings.** For each side I read:
  - the full ledger entry;
  - the frozen CWSAC listing rows and battle description;
  - the dossier's `responsibility` claim and open questions.
- **Source sections read in full or at length:**
  - Sibley, 4 May 1862;
  - Canby, 1 March 1862;
  - both Slough reports;
  - Gillmore, October 1865 (the fort-and-project and investment sections);
  - Mahan (the squadron and forts sections);
  - Lovell, 22 May 1862;
  - Jones, Secessionville;
  - Parker, Simmon's Bluff;
  - Britton (Independence, Lone Jack and Prairie Grove);
  - Salomon's and Cooper's Newtonia reports;
  - Cooper, 25 October 1862;
  - Blunt, 22 October 1862.
- **Context read around individual cited quotes:** Curtis, Van Dorn, Hindman (Cache River), Hovey, Irwin (Baton Rouge), Mouton, Brannan and Hopkins.
- **Registry.** I checked the entries these engagements use: 7 passage-only names, the Schofield passage merge and the Butler listing merge.
- **Nesting.** No recorded or computed contained-interval pair involves an assigned engagement. The checker requires the recorded pairs to equal the computed ones, and none of the 16 recorded pairs is from this batch.
- **Out of scope.** I did not re-inspect the other passages of each dossier or other sections of these sources. I did not review the 91 carried-forward v1 entries or the strength ledger.

This is an AI review. It is a separate analysis, not historical adjudication, independent corroboration, feature admission or authorization of any fit.

## Required corrections

### R1: SC002 US, `superior_directing: Hunter` rests on a misdated passage

The ledger labels Hunter as the superior directing the 16 June assault. It cites Jones: Hunter "agreed to defer his departure for Hilton Head to await the result of the demonstration on Secessionville".

In Jones, that passage concerns the movement planned for the morning of the 11th. The same section continues:

- "This contemplated movement for the morning of the nth was, how- ever, deferred";
- "…eral Hunter left the field of operations on the even- ing of the nth, leaving General Benham In com- mand, with the Instructions already quoted".

Those instructions were that "you will make no attempt to advance on Charleston or attack Fort Johnson until largely reinforced". The description also says the assault was made "contrary to Hunter's orders".

So Hunter was a departmental superior who had left the field, and the assault went against his orders. The design excludes such a superior ("A departmental or national superior who was not directing this operation in the field is excluded"). The v1 convention also limits the label to a superior "ordering or directing this operation, not merely holding departmental command". The same passage directly supports Benham's grade A.

Exact change (SC002, US; the commander `us-henry-benham`, grade A and rule 2 are unchanged):

- `labels`: `[]`
- `superior`: `null`
- `superior_citations`: `[]`
- `citations`: add
  - `{"dossier": {"claim_id": "command-roles", "citation_index": 2}, "source_id": "jones-secessionville-selections-v1", "quote": "Hunter left the field of operations on the even- ing of the nth, leaving General Benham In com- mand, with the Instructions already quoted.", "battle_id": "SC002"}`
  - `{"source_id": "arnold-cwsac-battles", "row_key": {"battle": "SC002"}, "column": "description", "quote": "contrary to Hunter's orders", "battle_id": "SC002"}`
- `rationale`: "A cited passage states the command: Wright's and Stevens's divisions were under Benham's immediate direction, and Benham overruled objections and ordered the assault. Jones says Hunter 'left the field of operations on the evening of the 11th, leaving General Benham in command', with written instructions to make no attempt on Charleston or Fort Johnson until reinforced, and the description says the assault was 'contrary to Hunter's orders'. Hunter's assent and deferred departure in Jones concern the movement planned for the 11th, which was deferred. Hunter was not directing this operation and is not labelled. Hunter relieved Benham after the battle; no change of command within the one-day interval is shown."

I verified that both new quotes occur in their sources.

### R2: MO015 Confederate, rule 3(a) cannot choose Cockrell on the ledger's own first-combat reading

The ledger's US side treats Foster's night attack of 15 August as the first combat. Its Confederate rationale also accepts that this attack is "the side's first combat in the frozen interval". The engaged Confederate force at that combat was "1,600 Rebels under Col. J.T. Coffee" (description).

Britton says Coffee's force "up to this time, was acting independently of the Confederate officers". He also puts "Colonel Cockrell, with the main rebel force" in camp "about three miles northwest of town".

Rule 3(a) takes the listed officer whom a passage shows "in command of the side's engaged forces when the fighting began". No listed officer (Cockrell, Thompson or Hays) is shown in that position. Cockrell's grade C under "3a" therefore does not follow from the rule. The two sides of the same record also use different first combats.

This batch's AR003 handles an unlisted, passage-named commander by reading rule 3(a) with rule 2's third bullet (grade C). The v1 ledger chose the first-combat commander at KY007, TN005 and TN017. Consistent with those precedents, the change is as follows.

Exact change (MO015, Confederate):

- `commander_id`: `cs-j-t-coffee` (an existing passage-only registry entry, citing the description)
- `grade`: `C`
- `rule`: `3a`
- `echelon`: `unknown`
- `labels`: `["responsibility_unresolved", "command_changed"]`
- `candidates`: `["cs-jeremiah-vard-cockrell", "cs-g-w-thompson", "cs-upton-hays"]`
- `successor`: `cs-jeremiah-vard-cockrell`
- `superior`: `null`
- `citations`: keep all the current citations. Add
  - `{"dossier": {"claim_id": "command-roles", "citation_index": 8}, "source_id": "britton-border-1-boston-mountains-selections-v1", "quote": "was reinforced by twelve hundred men under Colonel Coffey", "battle_id": "MO015"}`
- `rationale`: "Cockrell, Thompson and Hays (all Colonel). The side's first combat in the frozen interval was Foster's night attack of August 15 on the camp of '1,600 Rebels under Col. J.T. Coffee' (description); Britton says Coffee, commanding Missouri State Guard troops, 'up to this time, was acting independently of the Confederate officers', with Cockrell's main force three miles away. No listed officer is shown in command of the engaged force at that combat; the passages name one other officer, Coffee, so he is used (rule 3(a) read with rule 2's third bullet, as at AR003; grade C). On the 16th Foster and Britton have Cockrell commanding the Confederates in the fight, and Coffee's men rejoined about 11 a.m. (rule 4: command_changed, successor Cockrell). Thompson and Hays commanded regiments under Cockrell (Britton). Alternative reading: if Coffee's independent force is not taken as the side's engaged force at the first combat, no listed officer is shown in command then, and the tied colonels give rule 3(c), grade D."

These values pass each checker rule I traced in `command.py`:

- rule `3a` with grade C and `responsibility_unresolved`;
- every listing is accounted for through the candidates;
- the commander is not his own candidate;
- the successor comes with `command_changed`.

The quote occurs in its source. If the primary rejects the AR003 reading, the only rule-consistent alternative is the rule 3(c) grade D stated at the end of the rationale. Cockrell under 3(a) is not.

### R3: GA001 US, the rationale misstates the checker

The rationale ends: "Note: 'Captain' is not in the declared army rank order, so the checker's rank step cannot run on this side; the choice does not rest on rank."

That is false for v2. `RANK_ORDER_V2` includes Captain, and the ledger's own `rank_order` declares it. `check()` calls `rank_level` for every multi-listing side, and it resolved Captain here.

Exact change (GA001, US, `rationale`): replace that final sentence with "The choice does not rest on rank: by listed rank Hunter (Major General) outranks Gillmore (Captain), and rule 3(b) would apply only if no passage decided the side." Nothing else changes.

Out of batch, for the primary to check: TN032 US carries a similar stale note ("'Lieutenant Commander' is not in the declared navy rank order"), but `RANK_ORDER_V2` declares Lieutenant Commander.

### R4: MO016, "Echelon not stated" is contradicted by the cited report sections

Both MO016 rationales say "Echelon not stated", and both sides record `unknown`. The cited sections say otherwise:

- Cooper's section (`cooper-1862-10-02-newtonia`) opens "Report of Col. Douglas H. Cooper , C. S. Army , commanding division . Headquarters Field Division";
- Salomon's section (`salomon-1862-10-01`) opens "Report of Brig. Gen. Frederick Salomon , TJ. S. Army , commanding division ." It also has him order "the forces here (First and Second Brig- ades of Kansas)". His letterhead, however, reads "Headquarters First Brigade, Army of Kansas".

Exact changes:

- **MO016 Confederate.**
  - `echelon`: `division`.
  - Add the citation `{"dossier": {"claim_id": "command-roles", "citation_index": 5}, "source_id": "or13-cooper-newtonia-old-fort-wayne-selections-v2", "quote": "Report of Col. Douglas H. Cooper , C. S. Army , commanding division . Headquarters Field Division", "battle_id": "MO016"}`.
  - In the rationale, replace "Echelon not stated." with "Echelon: the report heading and letterhead give 'commanding division' and 'Headquarters Field Division'."
- **MO016 US.**
  - `echelon`: `division`.
  - Add the citation `{"dossier": {"claim_id": "command-roles", "citation_index": 3}, "source_id": "or13-salomon-newtonia-selections-v1", "quote": "Report of Brig. Gen. Frederick Salomon , TJ. S. Army , commanding division .", "battle_id": "MO016"}`.
  - In the rationale, replace "Echelon not stated." with "Echelon: the report heading styles Salomon 'commanding division' and he ordered the First and Second Brigades of Kansas forward, though his letterhead reads 'Headquarters First Brigade, Army of Kansas'."
  - If the primary treats that conflict as unresolved, keeping `unknown` is acceptable, provided the rationale states the conflict instead of "not stated".

Both quotes occur in their sources.

## Advisories (no change required)

- **A1: `superior_directing` borderline cases.** The batch labels superiors who ordered the operation from a distance, which the v1 convention allows. Examples: Van Dorn (LA003), Hindman (AR003, AR004), Totten (MO015), Butler (LA005), Schofield (OK004). Comparable superiors are left unlabelled:
  - **Lovell at LA001 CS.** He placed the vessels under Mitchell, and by his own account "on the night of April 23 I went down m} self in a steamboat, to urge Captain Mitchell". That is within the interval and on the scene.
  - **Rains at MO016 CS.** Cooper marched "In conformity with orders from Brigadier-General Bains".
  - **Blunt at AR005 US.** Britton: Herron "re- ceived an order from General Blunt to send forward all of the cavalry that he could spare", and the first Union cavalry engaged were marching "to reinforce General Blunt". Blunt is already the successor there. NM001 labels Sibley as both successor and superior, so labelling Blunt the same way would be consistent.

  None of these is a clear error. The v1 memo asks that borderline cases be kept in the rationales. Lovell (LA001) and Blunt (AR005) are already discussed there. Rains (MO016) is not mentioned.
- **A2: LA001 US.** Grade A rests on the description and on Mahan's note that Porter commanded the flotilla. Mahan's same section, "The steam vessels of the flotilla were at once ordered by the flag-officer to Southwest Pass", states Farragut's authority over Porter's flotilla directly. I verified the quote. Consider citing it.
- **A3: MO014 CS.** Britton states Hughes's command and the change directly: "Colonel and acting Brigadier-Gen- … eral John T. Hughes" led a column, and "After Colonel Hughes was killed Colonel G. W. Thompson took command". This is stronger than the description alone. Consider citing it. Both quotes are verified in the `independence` section (the first spans a running head).
- **A4: OK004 CS candidates.** Cooper also wrote on 25 October that "Colonel Watie, who has command during my illness". He says he was ill "at the time of the attack, for some days previous and am now", and Blunt attacked "the rebel forces of Cooper and Stand Watie". The ledger reads the Watie line as describing the time of writing, which is reasonable given the postscript naming Buster "on the day of the battle". Still, one could read the line as covering the battle. Consider recording `cs-stand-watie` (a listed registry ID) as a candidate. The grade stays C.
- **A5: MO017 CS.** Wickersham's "General Green" is treated as the dispute with the listed Colton Greene. No passage identifies the two, so the rationale should say the identity is not established. The grade and candidates are unaffected.
- **A6: LA003 US.** Irwin says Dudley "seems to have commanded the troops actually engaged" after Williams fell, while the description names Cahill. Only Cahill can be credited in command-change view (ii). The dispute is recorded in the rationale; Dudley has no registry entry. On the Confederate side, the description's "his corps" and the report's "Breckinridge's Division" disagree. The ledger records `corps_or_wing` and notes the conflict. `unknown` would be the more conservative value.
- **A7: Registry `us-m-h-brawner`.** Its `passage_citation` ("Captain Brawner was then in command.") does not carry the initials. The name rests on the description ("Capt. M.H. Brawner"), and Britton has "Captain Milton Brawner". Consider citing the description as the registry passage. No merge is involved.
- **A8: LA001 and LA002.** The two engagements overlap in time (16–28 April and 25 April–1 May) in one campaign, and Farragut is credited in both. They are not a contained-interval pair, so rule 7 does not reach them. This is not a ledger error, but the rating views should note the overlap.
- **A9: Minor echelon choices.** FL002 US records `flotilla` for a single gunboat. `detachment_or_post` would also fit. Either is defensible.

## Checked and found supported

The choices, grades, labels and candidates of the following sides follow the rules and their passages, apart from the corrections and advisories above:

- **NM001.** Canby under rule 2 (Roberts as subordinate context). Green under 3(a) for the 20th; Sibley recorded as successor and superior.
- **NM002.** Chivington and Pyron under 3(a) for the 26th; Slough and Scurry as successors.
- **AR001.** Curtis and Van Dorn.
- **GA001.** Gillmore under 3(a), with Hunter present as superior (apart from R3). Olmstead.
- **LA001 CS.** Duncan under rule 5, second case.
- **LA002.** Farragut under rule 5, second case. Lovell.
- **SC002 CS.** Evans.
- **SC003.** Rhind. Parker, grade C, with McCullough as candidate.
- **AR002.** Fitch under rule 5, second case. Fry.
- **FL002.** Drake and Pearson.
- **AR003.** Hovey under 3(a). Rust, grade C, with Hindman as superior.
- **LA003.** Williams, with the command change to Cahill. Breckinridge.
- **LA004.** Farragut. Landry at grade B.
- **MO013.** McNeil and Porter.
- **MO014.** Buel. Hughes, with the command change to Thompson.
- **MO015 US.** Foster, with the command change to Brawner and Totten as superior.
- **MO016.** The choices (not the echelons; see R4).
- **OK004.** Blunt with Schofield as superior. Buster, grade C.
- **MO017.** Barstow. Burbridge, grade C.
- **TX001.** Crocker and Irvine.
- **TX002.** Renshaw. Cook under 3(a).
- **FL003.** Brannan and Hopkins.
- **LA005.** Weitzel with Butler as superior. Mouton.
- **AR004.** Blunt. Marmaduke with Hindman as superior.
- **AR005.** Herron under 3(a), with the command change to Blunt. Hindman.

Every quote I read in context supports the use the rationale makes of it, except the SC002 superior citations (R1).

Registry identities used by this batch are sound:

- **Passage-only names.** Each carries a passage: Parker, Rust, Coffee, Brawner (see A7), Cahill, Totten and Buster. "Rust" is kept separate from the listed `cs-albert-rust`, as the memo states.
- **Merges.** The Schofield passage merge (the full name in Blunt's address) and the Butler listing merge (same side, rank and surname; middle name omitted) have adequate bases.
