# Separate review: command-responsibility ledger v2, batch 4 of 8

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This is a separate
  subagent started with fresh context. The author's conversation was not an input.
- **Date:** 2026-09-25
- **Prepared commit reviewed:** `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`, against `96110cf`.
- **Bundle commit / worktree HEAD:** `af6f34be843773a78551daeac61ce69df93448df`. Between the
  prepared commit and HEAD, only the eight review-bundle files (`v2cmd-b1`…`b4` `assignment.md` and
  `inputs.json`) changed, so every primary artifact I read is identical to the prepared commit.
- **Assignment:** `assignment.md` sha256 `12010631e686241fa0f941572cddd3922a65c5472c505af58f2ddb75a01e6fe3` (matches).
- **Input manifest:** `inputs.json` sha256 `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0` (matches).
- **Input hashes:** I checked all 25 bound paths against `git show 11d4bc3…:<path>`. All 25 match, and
  each working-tree copy is byte-identical. There were no mismatches.
- **Files read that the manifest does not bind:** the assignment names these, but `inputs.json` does
  not list them. I read them at HEAD, where they are unchanged from the prepared commit:
  - `docs/ledgers-v2.md` (the addendum): `a7e05ddf…49eb1`. This equals the ledger's `addendum` binding.
  - `docs/commander-ratings.md`: `0ab4b7d5…04bb`. This equals the `design` binding.
  - `docs/research/command-responsibility-v1.md`: `208b796a…d0dd`.
  - `generalship/command.py`: `58ffe17e…6954`.
  - `data/pilot/cohort-v2.json`: `614f6c9b…66f9`. This equals the `cohort` binding.

  The manifest binds `docs/research/ledgers-v2.md`, the extraction record. I read that too.
- **Checks run offline:**
  - `make check`: exit 0, 143 tests OK.
  - `python3 -m generalship command-check --ledger data/command/responsibility-v2.json`: 305
    engagements and 610 sides; grades A 512 / B 21 / C 68 / D 9; 401 registry commanders; nesting
    4 nested / 2 unresolved / 10 not nested; `rated: false`.

  I ran no build, packet or evaluation commands. I made no network calls and spawned no agents. The
  only file I wrote is this one.

## Scope actually inspected

I inspected all 27 assigned engagements, both sides of each:

AL002, OK005, MS012, MS013, FL005, GA006, VA125, LA017, LA018, LA019, LA020, LA021, LA022, LA023,
KY010, TN030, AR012, AR013, AR014, AR015, AR016, NC012, VA049, VA110, VA111, VA064 and AR017.

For each side I did the following:

- **Ledger entry.** I read the whole entry: choice, rule, grade, labels, candidates, successor,
  superior, echelon, citations and rationale.
- **Frozen CWSAC data.** I read the frozen description and every CWSAC commander row, including the
  rank and navy fields.
- **Dossier.** I read the bound dossier's `responsibility` claim and its boundary note. All 27
  dossier hashes match their bindings. For VA125, AL002, OK005 and LA020 I also read the open
  questions.
- **Cited passages.** I read each cited passage in its source section, with surrounding context,
  using the pinned raw text. I did not rely only on the quote strings. The source families were:
  - OR selections: Dodge, Phillips/Thayer, Sherman, Polk, Forrest (Okolona and West Tennessee),
    W. Sooy Smith, Seymour, Finegan, Thomas, Johnston, Pollard, Kilpatrick, Taylor, Hicks, Leaming,
    Price, Wessells, McCausland, Crook, Hunter, Vaughn, Early, Mower and Greene;
  - Irwin, Britton (Indian Territory and Camden), Humphreys, and Pond (Crook–Averell and Lynchburg).
- **Rechecked items.** I checked each registry entry these engagements use: the passage-only entries
  Roddey, W. A. Phillips, Cooke, Pollard, Fox, Emory, Franklin, McCausland and Vaughn; the
  Frederick Steele passage merge; the Chalmers ID; and the Jones ID. I recomputed the
  contained-interval pairs with the checker's own `contained_pairs`.

I did not re-review the 91 carried-forward v1 entries, the strength ledger, or other batches'
engagements, except to compare them as precedents (for example KY007, TN017, NC014, TX006 and
AR006).

**Nesting.** No contained-interval pair among the in-scope engagements involves any assigned
engagement. Of the 27, only MS012/MS013 and the Red River, Camden and Lynchburg records share
campaigns, and none of their intervals lies inside another's. No nesting outcome is therefore in
scope. The ledger records none, which is correct.

## Required corrections

There are two. Neither changes a commander choice, grade, label or identity. Each corrects a
rationale that the cited passages do not support, or that a passage the ledger missed contradicts.

### R1 — LA022 US: the rationale misattributes the forming of the line to Banks

- **Engagement, side, field:** LA022, US, `rationale`.
- **Problem:** The rationale says Irwin has Banks "forming line on the Mansura prairie". Irwin's
  passage is passive and names no one: "The infantry rapidly formed line of battle, Mower on the
  right, Kilby Smith next, Emory in the centre, Lawler on the left," (irwin-red-river-selections-v1,
  section `last-days`, p.345). The only passages that tie Banks to the force are the march order
  ("On the 13th of May Banks marched from Alex- andria on SImmesport,") and "Banks's losses were
  small,".
- **Replacement `rationale`:** "Irwin has Banks marching the army from Alexandria on May 13, Lawler
  leading the infantry column, Emory next and A. J. Smith's divisions in the rear, and at Mansura
  speaks of 'Banks's losses' (rule 2). Irwin says 'The infantry rapidly formed line of battle'
  without naming who ordered it. The division commanders are subordinate context."
- **Optional added citation**, supporting the corrected sentence:
  `{"source_id": "irwin-red-river-selections-v1", "dossier": {"claim_id": "reported-force-scope", "citation_index": 7}, "quote": "The infantry rapidly formed line of battle, Mower on the right, Kilby Smith next, Emory in the centre, Lawler on the left,", "battle_id": "LA022"}`.
  I checked that it resolves and that the quote occurs in the resolved passage.
- **Grade:** Grade A stays. The march-order passage states Banks's command of the column that
  fought on the 16th, and nothing inspected contradicts the listing.

### R2 — VA125 Confederate: a missed dating passage places Pollard alone in command at the side's first combat on March 2

- **Engagement, side, fields:** VA125, Confederate, `citations` (add one) and `rationale` (replace
  one sentence).
- **Problem:** The rationale leaves open that if Fox's "then took command" is read as before the
  first fire, "rule 2 would return the listed Hampton". The same March 7 Pollard report, in the same
  source and section the ledger already cites, dates an earlier combat on March 2 against the same
  detachment. Pollard was alone in command then, before McGruder or Fox joined:
  - "I overtook the enemy about 4 p. m. and attacked his rear, skirmishing with him for several miles."
    (or33-pollard-walkerton-selections-v1, section `pollard-1864-03-07`, p.208).
  - It is followed by "Was re-enforced by Captain McGruder…" and "I then sent for Cap- tain Fox…".

  Under design §2, the side's first combat within the frozen interval therefore has Pollard in
  command whichever way "then" is read. The Fox passage bears only on rule 4 (successor), not on the
  choice.
- **Add citation:**
  `{"source_id": "or33-pollard-walkerton-selections-v1", "dossier": {"claim_id": "reported-force-scope", "citation_index": 16}, "quote": "I overtook the enemy about 4 p. m. and attacked his rear, skirmishing with him for several miles.", "battle_id": "VA125"}`.
  I checked that it resolves and that the quote occurs in the resolved passage.
- **Replace this sentence:** "If 'then' is read as before the first fire, the contradicting passages
  name two officers and rule 2 would return the listed Hampton (still grade C)."
- **With:** "Pollard's March 7 report also has him overtaking the party about 4 p.m. and attacking
  its rear, skirmishing for several miles, before McGruder or Fox joined him. So Pollard commanded at
  the side's first combat on March 2 whichever way Fox's 'then took command' is read, and the Fox
  passage bears only on the successor. This rests on the dossier's reading of the record as the
  pursuit and ambush of Dahlgren's detachment; under the raid-wide reading (Hampton's attack on
  Kilpatrick), the listing would decide."
- **Unchanged:** the choice (`cs-pollard`), grade C, the labels `command_changed` and
  `responsibility_unresolved`, the successor `cs-fox`, and the candidates.

## Advisories (not required)

Each advisory is optional. None changes a grade or choice under the rules as written.

- **A1 — VA064 CS: the rationale overstates Pond.**
  - The rationale says "both name Breckinridge … for the defence when the fighting began on the 17th".
    Pond actually says Breckinridge "long before Hunter's arrival had placed his troops and Vaughan's
    behind the intrenchments". That concerns dispositions before the fight.
  - Pond also has "the 17th … brought to the city half of Early's corps", and "Early at that time
    threw two brigades of Bamseur's division into this redoubt" at the close of the evening attack.
  - The only passage naming Breckinridge as commanding at the point of first combat is Hunter's
    intelligence ("The best information to be obtained at this point … under the command of General
    Breck¬ inridge"). Hunter also credits the 18th to Breckinridge, which Early's own June 19 dispatch
    contradicts ("my lines … my command").
  - Suggestion: reword the rationale to say this. Also record the alternative: if Hunter's
    intelligence is not read as naming who commanded at first combat, rule 2 returns the listed
    Early at grade C, with Breckinridge as candidate and no `command_changed`.
- **A2 — LA021 US: record Franklin as an alternative.**
  - Irwin has Franklin reconnoitring at daylight on the 23rd, then "after maturing his plans" turning
    over his command to Emory. No inspected passage says whether firing began before the handover.
  - Taylor has contact from "about 2 p. m. on the 22d".
  - Suggestion: note in the rationale that if combat on the 23rd began during Franklin's
    reconnaissance, Franklin would be the choice (grade C), with `command_changed` naming Emory as
    successor.
  - Identity: Irwin's appendix names "Nineteenth Army Corps : Major - General William B. Franklin."
    (section `appendix-sabine-pleasant-hill-losses`). That passage could support a `passage_merges`
    entry identifying `us-franklin` with `us-william-b-franklin`. It affects only the `superior`
    field.
- **A3 — LA021 CS: a stronger passage and a better echelon for Bee.** Taylor's dispatch states "Bee
  was in posi- tion at Monett's Ferry with Major's, Bagby's, Debray's, and Terrell's brigades of
  cavalry" (section `taylor-1864-04-24-monetts-ferry`). This states the command over all the engaged
  Confederate brigades, including Major's division, and would strengthen grade A. It also makes the
  echelon `division` doubtful: Bee held two divisions' brigades. `unknown` or `detachment_or_post` is
  closer.
- **A4 — VA049 CS: the successor identity.**
  - McCausland's May 9 dispatch in the cited source is signed "JOHN McCAUSLAND, Colonel, Commanding."
    (section `mccausland-1864-05-09`). The extraction record's rule ("a cited passage gives … the full
    name") would allow a `passage_merges` entry identifying `cs-mccausland` with the listed
    `cs-john-mccausland` (MD008).
  - The rank differs: Colonel here, Brigadier General at MD008. Record that if the entries are
    merged.
  - Also, the Jones candidate is identified with the VA111 listing through Pond's "W. E. Jones". That
    basis appears only in the rationale; recording it as a `passage_merges` entry would make it
    auditable.
- **A5 — GA006 US: Palmer as the possible field commander.**
  - Thomas's report has "General Palmer notified me, from Ringgold," and refers to "General Palmer's
    command at Ringgold". It also has Cruft taking position "by instructions from General Palmer",
    and Palmer advancing on Tunnel Hill. No inspected passage places Thomas in the field.
  - Keeping Thomas is consistent with rule 2's second bullet, because no passage names Palmer over
    the whole engaged force.
  - Suggestion: add to the rationale that Palmer may have been the field commander.
- **A6 — AR017 US: the first skirmish was not shown under Mower.**
  - Mower "debarked with the Second and Third Brigades of this division," and had "no artil- lery in
    my command". The cavalry was "in advance and … skir- mishing" before Mower came up. So the first
    combat was by cavalry that the passages do not show under Mower.
  - This strengthens the A. J. Smith alternative that the rationale already records.
  - Suggestion: state it. If Greene's "Major-General Smith commanded" is read as a contradiction,
    rule 2 would give A. J. Smith at grade C.
- **A7 — TN030 CS: echelon.** Forrest says McCulloch's brigade (Chalmers's division) and Bell's
  brigade (Buford's division) were "both placed for the ex- pedition under the command of" Chalmers.
  `detachment_or_post` describes that force better than `division`.
- **A8 — AR015 CS: timing of Kirby Smith's command.** Britton has Kirby Smith, "having assumed
  command … in person", sending Fagan out. Price says Smith "had on April 26 assumed command of the
  Army of Arkansas in person", which is after Marks' Mills. Price also says Smith "reached the field
  of opera- tions" on April 19. Suggestion: note this timing disagreement beside the
  `superior_directing` label.

## Items checked and found sound

**AL002**
- CS: Roddey is used at grade C. The January 29 report is the only passage naming a different
  officer; the January 26 dispatches name the listed Hannon, who is kept as a candidate.
- US: "Captain Adam" is identified with the listed Emil Adams through NPS.

**OK005**
- US: Willette with `superior_directing` Phillips. This is consistent with the MS006 precedent.
- CS: Jumper at grade B. His regiment is placed in the fight, but no passage states his command of
  all the Confederates engaged.

**MS012, MS013, FL005, LA018, LA019, AR013, AR014, AR016, NC012, VA111**
- The rule-2 or rule-3(a) choices rest on passages that state the command.

**VA125 US**
- Dahlgren is chosen under rule 3(a), with Cooke as successor. "The colonel commanding (Dahlgren)
  was killed at the first fire"; Kilpatrick says the party was "then under command of … Cooke".

**LA017**
- US: A. J. Smith under rule 3(a) ("the command of the whole he gave to A. J. Smith").
- CS: Byrd at grade B, with `superior_directing` Taylor.

**LA020**
- US: grade D under the third case of rule 5. Irwin says "Kilby Smith and Porter responded", and the
  description credits the troops together with the gunboats. This follows the AR006 precedent.
- CS: Green, with `command_changed`. No successor is shown, and there is precedent for that.

**LA021 US and LA023**
- The Emory and Mower choices follow the passages. The contradiction of the listed Banks at LA021 is
  stated in both Irwin and the description.

**KY010 US**
- Hicks under the second case of rule 5, applied to the losing side's defence. This is consistent
  with the NC014 and TX006 US precedents, and the rationale states the grade-D alternative.

**TN030**
- US: Booth under rule 3(a), with Bradford as successor.
- CS: Chalmers is used because Forrest's own report names him in command before Forrest reached the
  field and "Assuming command". This follows the KY007 CS precedent.

**AR012**
- Price's order to Marmaduke was to Tate's Bluff, not this action, so leaving `superior` null is
  defensible.

**VA049**
- CS: Jenkins was placing troops "in person" and ordering the charges. McCausland "assumed command"
  when Jenkins was wounded.
- Pond's joint "Generals W. E. Jones and Jenkins" is kept as a source disagreement at grade C.

**VA110**
- US: Stahel's morning command of Moor's advance is subordinate context. Sigel "came up with the
  remainder of his small army" and formed the main line "under Sigel's per- sonal direction".

**Registry and identities across the batch**
- Every passage-only entry used in this batch has a citation that resolves.
- No identity is asserted without a listing field or a passage.
- Vaughn has no CWSAC listing, so the passage-only `cs-vaughn` is correct.

## Outcome

**Corrections required: R1 (LA022 US rationale) and R2 (VA125 Confederate citation and
rationale).** Advisories A1–A8 are optional.

This is an AI review within the scope above. It is not human historical adjudication, independent
corroboration of the sources, feature admission, or authorization of any fit or rating run.
