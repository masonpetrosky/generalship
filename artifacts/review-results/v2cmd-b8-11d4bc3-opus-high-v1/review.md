# Command-responsibility ledger v2, batch 8 of 8: separate review

**Outcome: corrections required** (R1–R5). Advisories A1–A9 are listed separately.

## Record

| Field | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`, fresh-context subagent |
| Date | 2026-09-25 |
| Assignment | `artifacts/review-results/v2cmd-b8-11d4bc3-opus-high-v1/assignment.md`, sha256 `6531ce435488228d86d4b510a241e32003a0669f4ee5944e8e24a7ade97bed08` (verified) |
| Input manifest | `inputs.json`, sha256 `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0` (verified) |
| Prepared commit reviewed | `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`, against `96110cf` (`96110cfad1ea80f4b0462947d9f9b5a98a4e71f5`) |
| Worktree HEAD | `ca6f0dc619a28f22be71edf9cc3a392997cbe0d0` (bundle commit); `git diff 11d4bc3 ca6f0dc` touches only the eight review-bundle directories |

**Input hashes.** All 25 paths in `inputs.json` match their recorded sha256, both as
`git show 11d4bc3:<path>` and in the worktree. There are no mismatches. Key hashes: ledger
`data/command/responsibility-v2.json` `1271ea87…753a`; registry `data/command/commanders-v2.json`
`cdf72348…e267c`.

**Files the assignment names that `inputs.json` does not bind.** I hashed these in the worktree;
none differs between `11d4bc3` and HEAD:

- `docs/commander-ratings.md`: `0ab4b7d541baf4f8e642634f316628f9cb372d68dcdbbc047a305f5a1fb704bb`. This equals the ledger's `design` binding.
- `docs/ledgers-v2.md`: `a7e05ddfc072c493f8f9152064e444e4b285e070a7dfcdbd279e80fc4aa49eb1`. This equals the ledger's `addendum` binding.
- `docs/research/command-responsibility-v1.md`: `208b796a3f60ffc869a6686a12241a4356b4e94655128fb84bc88433dc33d0dd`.
- `generalship/command.py`: `58ffe17ebc42cc3d2ec5950e55d56a243caf662460df86059c845ade62ef6954`.

The assignment calls the addendum `docs/ledgers-v2.md`, but `inputs.json` binds the extraction
record `docs/research/ledgers-v2.md`. I read both.

**Checks run (offline).**

- `make check`: 143 tests OK, exit 0.
- `python3 -m generalship command-check --ledger data/command/responsibility-v2.json`: exit 0.
  It reports 305 engagements and 610 sides, grades A 512 / B 21 / C 68 / D 9, 401 registry
  commanders, and nesting outcomes nested 4 / not_nested 10 / nesting_unresolved 2.

I ran no build, packet or evaluation command.

## Scope actually inspected

- **Engagements.** All 30 assigned engagements, both sides (60 sides): GA025, GA026, SC010,
  GA027, GA028, NC014, VA081, VA082, NC015, NC016, SC011, NC017, NC020, VA123, FL006, AL005,
  AL006, VA085–VA090, VA092–VA094, VA096, VA097, AL007 and TX005.
- **Each side's entry.** I read the whole ledger entry, the frozen CWSAC description and every
  CWSAC commander row for the battle.
- **Citations.** I resolved every non-listing citation and superior citation, through the
  bound dossier claim and the source section, and read the surrounding passage (±350–600
  characters) to check timing, attribution and scope.
- **Full sections and dossier claims read** (where a choice, grade or label turned on them):
  - GA025: G. W. Smith's report and his November 19 letter.
  - SC010: Hatch's report, the opening of the November 30 narrative.
  - NC014: Whiting's narrative for December 24–27.
  - VA088: Humphreys, "five-forks" section.
  - VA093: every mention of Sheridan in Humphreys's Sailor's Creek section.
  - VA123: Pond's Waynesboro section.
  - The dossier `command-roles` (or equivalent) claims and open questions for GA025, SC010,
    NC016, NC017, VA088, VA123, FL006, SC011 and TX005.
- **Registry.** I checked every registry entry these engagements use that is passage-only,
  merged or passage-merged: `cs-g-w-smith`, `cs-robert-preston`, `cs-william-lamb`,
  `cs-d-h-maury`, `cs-cook`, `us-charles-r-woods`, `us-e-f-catterson`, `us-david-branson`,
  `cs-richard-h-anderson`, `us-alfred-h-terry`, `us-benjamin-franklin-butler`,
  `cs-william-j-hardee` and `us-john-m-schofield`.
- **Nesting.** No contained-interval pair involves an assigned engagement. The other cohort
  records in these campaigns (NC018, NC019, VA091, VA095, VA124) are Inconclusive and out of
  scope. AL005 and AL006 overlap, but neither interval contains the other. The checker's
  complete-pair test passes.
- **Not done.** I did not read every other claim of the 30 dossiers or every full source
  section. The 91 v1 entries and the other batches are out of scope. I used no network, did no
  new research, opened no new source family and ran no agents.

## Required corrections

### R1: GA025 Confederate, `rationale` (a timing and scope misreading)

The rationale cites G. W. Smith's statement that Wheeler gave no direct orders to the infantry
and artillery as evidence "against that choice" at Griswoldville. The quote comes from Smith's
letter dated "Macon, November 19, 1864" (section `smith-1864-11-19`). The letter concerns the
earlier move from Forsyth to Macon: "General Wheeler was the senior officer on this theater of
operations, and without giving direct orders to the infantry and artillery, strongly advised, so
soon as he developed the strength of the enemy, that I should move to Macon at once."

The action took place on November 22. The letter says nothing about the command at Griswoldville.

**Unchanged:** the choice (Wheeler), the rule (3(b)), the grade (C) and the labels. The citation
may stay.

**Replacement for the sentence beginning "Against that choice:"**

> Against that choice: Woods says the first combat was with part of Wheeler's cavalry and that two of his brigades stood in reserve during the militia's assaults. The assaulting militia were G. W. Smith's command. His report says the collision occurred 'Notwithstanding my order to avoid an engagement at that place and time' and that the troops were withdrawn to Macon by his order. Smith was in Macon, however, and does not name who led them on the field. Smith's November 19 letter, written three days before the action, says Wheeler, 'the senior officer on this theater of operations', gave no direct orders to the infantry and artillery when he advised the move to Macon. That concerns the earlier movement, not the command at Griswoldville.

The rest of the rationale is unchanged.

### R2: GA028 Confederate, `grade` A → B (identity asserted across conflicting initials)

- **Listing:** "George A. Anderson", Major.
- **Passage (Cox, `cox-savannah-selections-v2`):** "son was about two hundred men under command of Major G. W. Anderson."
- **Ledger:** grade A, on the ground that "rank and post agree".

The middle initials conflict (W against A). The addendum admits a passage name only on "matching
initials or the full name", and the ledger keeps initial conflicts separate ("James B. Fagan"
and "James F. Fagan"). Where initials differed, it rested identity on another passage (LA009,
"identity rests on the description"). No listing field or passage identifies G. W. Anderson with
George A. Anderson. The Cox passage therefore does not state the listed officer's command.

It does not establish a different officer either. So the listing stands and is not contradicted:
rule 2, grade B. This matches GA002, the same listed officer, where the compiler's "[G. W.]"
conflict is graded B.

**Exact changes:**

- `grade`: `"B"`. `rule` stays `"2"`, `commander_id` stays `cs-george-a-anderson`, and `labels` stay `[]`.
- `citations`: keep only the listing citation (`arnold-cwsac-commanders`, GA028/Confederate/"George A. Anderson", `rank`, "Major"). The checker requires grade B to cite only the listing.
- `rationale`:

> Rule 2, grade B. Cox puts the garrison of about two hundred men 'under command of Major G. W. Anderson'. His initials (G. W.) conflict with the listing's George A. Anderson. No listing field or passage identifies the two, and the ledger keeps conflicting initials separate (as with James B./James F. Fagan), so the passage is not taken as stating the listed officer's command. It establishes no different officer either, so the listing stands uncontradicted (as at GA002).

### R3: FL006 Confederate, `grade` A → B (joint naming does not state the command at first combat)

The only non-listing citation is Newton's April 6 report: "The rebel force altogether was over
2,000 men with at least five light 12-pounders, commanded by Generals Jones and Miller."

The passage names two generals jointly. It refers to the force "altogether", after the
reinforcements Newton says arrived about noon. It does not say who commanded when the fighting
began before dawn. The rationale concedes this ("The passage does not say which of the two
commanded when the fighting began"). The grade table's A condition, a passage stating that the
officer commanded the side's engaged forces when the fighting began, is therefore not met.

The passage does not name another officer to the exclusion of Jones, so the listing is not
contradicted (rule 2).

**Exact changes:**

- `grade`: `"B"`. The rule, commander, labels and echelon (`unknown`) are unchanged.
- `citations`: keep only the listing citation (`arnold-cwsac-commanders`, FL006/Confederate/"Sam Jones", `rank`, "Major General").
- `rationale`:

> Rule 2, grade B. Newton, the opposing commander, writing a month later, says the Confederate force 'altogether' was 'commanded by Generals Jones and Miller'. The passage names two officers jointly for the whole force, including the reinforcements he says arrived about noon. It does not say who commanded when the fighting began before dawn, and no Confederate report was inspected. It names no officer to the exclusion of the listed Jones, so the listing stands uncontradicted.

### R4: VA088 Confederate, `grade` A → C, `labels` and `rationale` (a missed dating passage)

The rationale says "No inspected passage places Pickett at the moment the attack began." That
is wrong for an inspected passage. The ledger already cites the Humphreys "five-forks" section
(dossier `reported-force-scope`, citation index 6), and that section says:

- "When the battle began General Pickett and General Fitz Lee were on the north side of Hatcher’s Run."
- "General Pickett was all this time, and until near the close of the action, on the north side of Hatcher’s Run"
- "There was no Confederate commander on the field"

It also says that on arriving Pickett "ordered up Mayo’s brigade" and "he directed General Corse
to form a line".

No other officer is named in command, so the listed Pickett is kept. The inspected sources do
disagree about whether anyone directed the side's engaged forces when the fighting began. The
reviewed v1 ledger grades the equivalent statements C:

- TN006 US: Cist says no one was in command;
- MS010 CS: Greene says there "seemed to be no one in command".

The design's statement that the officer "need not have been on the part of the field where
fighting began" keeps Pickett as the choice. It does not make the absence statement
uncontradicting.

**Exact changes:**

- `grade`: `"C"`, `rule`: `"2"`.
- `labels`: `["responsibility_unresolved", "superior_directing"]`. The superior stays `cs-robert-e-lee`, and `candidates` stay `[]`.
- `citations`: add two entries, each `{"dossier": {"claim_id": "reported-force-scope", "citation_index": 6}, "source_id": "humphreys-appomattox-selections-v1", "battle_id": "VA088"}`, with the quotes:
  - `"When the battle began General Pickett and General Fitz Lee were on the north side of Hatcher’s Run."`
  - `"There was no Confederate commander on the field"`

  I checked both as occurring exactly once in the resolved section.
- `rationale`:

> Rule 2. The description has Lee order Pickett, with his division and three cavalry divisions, to hold Five Forks (superior_directing: Lee). Humphreys says that when the battle began Pickett and Fitz Lee were north of Hatcher's Run, out of hearing of the firing, and that Pickett stayed there 'until near the close of the action'. He adds that 'There was no Confederate commander on the field'. On reaching his troops, Pickett ordered up Mayo's brigade and directed Corse's new line. No passage names another officer in command, so the listing is kept. The inspected sources disagree, however, about whether anyone directed the side's engaged forces when the fighting began: grade C, responsibility_unresolved, as v1 TN006 US and MS010 CS.

### R5: VA093 Confederate, add `command_changed` (the responsible commander was captured within the action)

Ewell's report: "I surrendered myself and staff to a cavalry officer … telling him he was
surrounded, General Anderson’s attack had failed, I had surrendered … though I gave no orders,
being a prisoner. Before the messenger reached him General Lee had been captured".

So G. W. C. Lee's troops were still engaged after Ewell's surrender. Humphreys also has the II
Corps' contest with Gordon's corps run on to "just before dark". Rule 4 applies to a command
change within the interval (death, wounding, relief). The ledger applies it where no successor
is named, as at LA020 CS ("Green was killed during the attack (rule 4: command_changed); no
inspected passage names who then commanded, so no successor is recorded"). The current rationale
withholds the label only because no successor is named.

**Exact changes:**

- `labels`: `["command_changed", "responsibility_unresolved"]`. `successor` stays `null`.
- `rationale`: replace the last sentence with:

> Ewell surrendered during the action ('I surrendered myself and staff … though I gave no orders, being a prisoner'), while G. W. C. Lee's troops and Gordon's corps were still engaged (rule 4: command_changed). No inspected passage names a successor for the side, so none is recorded (as LA020 CS).

## Advisories (not required)

- **A1: consistency of `superior_directing` for orders given before the operation.**
  - The label is applied at:
    - GA026 US: Sherman's November 23 instructions at Milledgeville to move toward Millen.
    - VA123 US: Pond, "Grant began to desire the repetition of the attempt". Grant's letters of February 8 and 20 were written from outside the Valley and put suggestions ("I think you will have no difficulty").
  - It is withheld at:
    - GA025 CS: Hardee's order, "that is the movement, not the fight".
    - VA114 (another batch): Grant's and Halleck's telegrams, as "national superiors outside the field".
  - v1's standard is "a named superior ordering or directing this operation, not merely holding departmental command".
  - GA027, where orders that day said to "engage Wheeler wherever we find him", clearly qualifies.
  - The primary should settle one reading for GA026 and VA123. My view is that VA123 is the weakest case.
- **A2: SC010 Confederate.** Smith says he based "the directions of the whole operation for the
  day" on the district officers' information, and dates "the battle" from after his
  dispositions. The rationale records this alternative reading, and grade A on the earlier
  skirmishing is defensible. Hatch's report adds an earlier November 30 combat that the
  rationale could cite: the howitzers and four companies of the 54th Massachusetts "were
  attacked, and repulsed a body of the enemy from the direction of Bee’s Creek battery". Its
  Confederate commander is not named.
- **A3: registry `cs-g-w-smith` (SC010 successor).** It reuses the v1 passage-only entry from
  NC009 ("G. W. SMITH"), identified on matching initials and surname only. Consider recording the
  SC010 basis, the report heading in `or44-gw-smith-selections-v1` section `smith-report`
  ("Report of Maj. Gen. Gnstavus Smithy … First I>ivisio7iy Georgia Militia", OCR as printed).
- **A4: GA025 Confederate candidates.** Consider recording `cs-g-w-smith` as an unlisted
  candidate. The militia were his command, as his report states, though he was absent.
- **A5: VA093 Confederate candidates.** Consider recording `cs-richard-h-anderson` as an
  unlisted candidate. Ewell describes a co-equal arrangement with Anderson.
- **A6: NC016 Confederate.** Bragg's report dates his arrival on the 21st, not his departure.
  That he was absent when the fighting began on February 12 is inferred from the description's
  "under Maj. Gen. Robert Hoke". Grade C and `responsibility_unresolved` already carry this
  uncertainty.
- **A7: NC014 US.** Rule 5's "force … compelling the result" is applied to the losing side
  through Butler's decision not to assault. The rule 5 third case (grade D) is the alternative
  reading. Grade C is defensible and the rationale states the basis.
- **A8: SC011 US.** Grade A rests on Blair's heading ("commanding Seventeenth Army Corps") and
  orders given in the passive voice. This is acceptable under ledger practice, but it is at the
  weak end of A.
- **A9: GA002 Confederate (out of scope).** It uses the same `cs-george-a-anderson` with the same
  G. W./George A. conflict and says "identity is not in doubt". If R2 is accepted, the primary
  may align that wording.

## Engagements with no finding

The following entries are consistent with the rules, and their quotes support their rationales:

GA026 (subject to A1), GA027, SC010 (A2), NC014, VA081, VA082, NC015, NC016 (A6), SC011 (A8),
NC017, NC020, VA123 (A1), AL005, AL006, VA085, VA086, VA087, VA089, VA090, VA092, VA094, VA096,
VA097, AL007 and TX005, together with the US sides of GA025, GA028, FL006, VA088 and VA093.

Specific checks:

- **Choices overturning the listing (rule 2, third bullet), all grade C with the listed officer as candidate:** NC014 CS (Lamb), VA082 CS (Preston), NC016 CS (Hoke), NC017 US (Cox) and TX005 US (Branson).
- **Rank fallbacks:** GA025 CS and VA093 CS at 3(b).
- **Grade C at 3(a) by timing ambiguity:** VA090 CS.
- **Joint command:** NC014 US and NC015 US under rule 5.
- **Registry merges used:** Terry, Butler, Hardee and R. H. Anderson meet the listing-field or initials basis.
- **Separations kept:** William Lamb and Charles Lamb, and the surname-only `cs-cook`, stay separate.

This is an AI review, a separate analysis within the scope stated above. It is not human
historical adjudication, independent corroboration, feature admission or authorization of any
fit.
