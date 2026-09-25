# Command-responsibility ledger: separate review, batch 4 of 4

**Outcome: corrections required** (R1–R5). Advisories A1–A8 follow them.

## Reviewer record

| Field | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This is a separate subagent with fresh context; the author's conversation was not an input. |
| Date | 2026-09-25 |
| Prepared commit reviewed | `a9520c2d5628c25b49437f4f54bfc78268a85393` |
| Previous commit | `16a32116067912a1b5cb380097d75092a2a430b4` |
| Bundle commit (worktree HEAD) | `19176f6b2b85fdcfb68434733cc87f631ce6019f` |
| `assignment.md` sha256 | `e9e792f8533a9a5cc081b3f235f79cfbb95039d8b164e783bb0dee1df15b27b9` (verified) |
| `inputs.json` sha256 | `11f34d78cb94fd48165b789ec37c0e0ff8ad82f6acee3d1d7e90581f9b5e3a62` (verified) |
| Input hashes | All 24 paths in `inputs.json` were hashed from `git show a9520c2:<path>` and from the worktree. All match; there are no mismatches. Between `a9520c2` and `19176f6`, only the four review-bundle directories changed. |
| Dossier and source bindings | The 91 dossier hashes and the cited-source metadata and raw hashes bound in the ledger were replayed by `command-check`, and all pass. |

This is an AI review. It is not human historical adjudication, independent corroboration, feature admission or authorization of any fit. Where a source is interested or written after the event, I say so; agreement within one source family is not treated as corroboration.

## Checks run (offline)

- **`make check`:** exit 0. It ran 126 tests (`OK`), and the command check passed inside it.
- **`python3 -m generalship command-check`:** 91 engagements and 182 sides, graded A 149, B 15, C 15, D 3. The registry has 128 commanders. Nesting: 2 nested, 6 not nested, 1 unresolved. `rated: false`.
- **Corrections tested in memory.** R1–R5 were applied to an in-memory copy of the ledger and passed through `generalship.command.check(root, ledger=...)`. No file was written. The check passes with overall grades unchanged at A 149 / B 15 / C 15 / D 3, because R2 moves one side from B to A and R3 moves one from A to B.
- **Files changed:** none apart from this review. `git status` was clean before this file was written.

## Scope actually inspected

- **Documents read:** `AGENTS.md`; design `docs/commander-ratings.md` §1–2 in full (§3–9 not reviewed); the memo `docs/research/command-responsibility-v1.md`; `generalship/command.py`; and the registry entries for every ID used by the assigned sides.
- **Assigned engagements.** For each of the 21 engagements (42 sides) I inspected:
  - the full ledger side record, including citations, superior citations, candidates, successor, labels, echelon and rationale;
  - every frozen CWSAC commander-listing row, including rank and navy fields;
  - the frozen CWSAC battle description;
  - the dossier's responsibility claim, with all its citations and open questions.
- **Source sections read in context** (whole bounded section or at least ±1,500 characters around the cited quote):
  - Hobson (OR 23.1), around the Judah passage (p.660–661);
  - Shackelford (OR 23.1), p.643;
  - Hill (OR 30.2), `hill-chattanooga`, in full;
  - Hindman (OR 30.2), `hindman-1863-10-22` and `hindman-1863-10-25`, p.292–298;
  - Cist Chickamauga, `bragg-and-the-cove` (p.185–186);
  - Echols (OR 29.1), p.528–530, and Averell (OR 29.1), with a search for timing words;
  - Burnside Blue Springs (OR 30.2), p.547 and p.551;
  - Bratton (OR 31.1), in full;
  - Cist Reopening, the Wauhatchie passages (p.240–241);
  - Humphreys, the `bristoe-station` section, searched for "Warren";
  - Stuart (OR 29.1), around the Kilpatrick quote;
  - Cleburne Ringgold (OR 31.2), p.753–757;
  - Burnside Knoxville, Fort Sanders (p.277–278);
  - Longstreet East Tennessee, `longstreet-beans-station`;
  - Parke (OR 31.1), both dispatches;
  - Sturgis (OR 32.1), p.80–81 and the dispatch of 27 January;
  - Longstreet Dandridge (OR 32.1), p.93–94;
  - Hatch (OR 31.1), p.244–245;
  - Cist Chattanooga–Ringgold, the passage on the 23rd.
- **Nesting.** The nine recorded contained-interval pairs were listed. None involves an assigned engagement. I also checked the same-campaign intervals of the assigned records (Chickamauga; East Tennessee; Bristoe; Knoxville; Chattanooga–Ringgold; Dandridge; Morgan's Raid), and none contains another. **No nesting outcome is required for this batch.**
- **Not inspected:**
  - dossier claims in dimensions other than responsibility, except where a quote above sat in the same section;
  - sources outside those listed;
  - other batches;
  - design §3–9;
  - the model code.
- **Research limits.** I did no new research or network access, opened no source families beyond those the dossiers already cite, and did not rely on recollection.

## Per-side verdicts

"OK" means the choice, grade, labels, candidates and echelon follow the design, and the cited quotes support the rationale.

| Engagement | US | Confederate |
| --- | --- | --- |
| IN001 Corydon | OK (Jordan, B) | OK (Morgan, A). Duke's "Colonel Morgan" advance guard is subordinate context. |
| OH001 Buffington Island | **R1** | OK (Morgan, A) |
| OH002 Salineville | OK (Shackelford, A). The appointment is dated before 25 July; Way's fight is subordinate context. | OK |
| TN018 Chattanooga | OK (Wilder, A, brigade) | **R3** |
| GA003 Davis' Cross Roads | OK (Negley, A, division) | **R5**; see also A1 |
| GA004 Chickamauga | OK (Rosecrans, 3(a), `command_changed` → Thomas) | OK (Bragg, 3(a); General outranks Longstreet) |
| TN019 Blountsville | OK | OK |
| TN020 Blue Springs | OK (Burnside, A); see A6 | OK (Williams, A) |
| VA040 Bristoe Station | **R2**; see A3 | OK (A. P. Hill, A, corps) |
| VA042 Buckland Mills | OK (Kilpatrick, A). Stuart's "commanded by Brigadier-General Kilpatrick" refers to the Buckland force. | OK (Stuart, A) |
| TN021 Wauhatchie | OK (Hooker, A) | **R4**; see A2 |
| TN022 Collierville | OK (Hatch, A). Hatch ordered Trafton on the 8 a.m. report of picket firing; see A6 on echelon. | OK (Chalmers, A, division) |
| WV012 Droop Mountain | OK (Averell, A) | OK (Echols, A). Echols assumed command on reaching the position, before "Our artillery very soon after being placed in position opened upon the enemy", so the first combat on 6 November falls under him; see A7. |
| TN023 Campbell's Station | OK | OK |
| TN024 Chattanooga | OK (Grant, A, army) | OK (Bragg, A, army) |
| GA005 Ringgold Gap | OK (Hooker, A) | OK (Cleburne, A); see A4 |
| TN025 Fort Sanders | OK (Burnside, B; conservative) | OK (Longstreet, A) |
| TN026 Bean's Station | OK (Shackelford, A, `superior_directing` Parke); see A6 | OK (Longstreet, A) |
| TN027 Mossy Creek | OK | OK (Martin, A, corps_or_wing: "commander of Longstreet's Confederate cavalry") |
| TN028 Dandridge | OK (Sturgis, A, corps, `superior_directing` Parke). Sturgis's report shows Parke ordering the retirement of the combined force "after dark". | OK (Longstreet, A); see A6 on citation |
| TN029 Fair Garden | OK (Sturgis, 3(a) over McCook) | OK (Martin, A) |

## Required corrections

### R1 — OH001 US: Judah's takeover is dated after the first combat (misreading)

**Problem.** The rationale says Hobson's report puts Judah's assumption of command "without dating it against the first combat". The memo repeats this ("without dating it"). That misreads the same page that the ledger cites.

**Evidence.** Hobson's report (`or23-1-hobson-morgan-raid-selections-v2`, section `hobson-1863-09`) gives this sequence:

1. Hobson's own advance opened the action: "The advance, under Colonel Kautz, drove in the pickets of the enemy about 5 a. m. July 19." (p.660)
2. Hobson made his dispositions, and Ward and R. C. Morgan surrendered to Holloway.
3. Shackelford asked for reinforcements.
4. Only then: "Learning from one of my orderlies that a column of cavalry was comiug up the river, to my right and rear," Hobson found it to be Judah's command, and "General Judah immediately assumed command of the whole force, I protesting against it." (p.661)
5. "About 12 m." Duke's command was brought in.

Hobson also concedes "I told him it was true he was my supe- rior officer,". So the inspected record places a superior arriving and taking command after the first combat. Design rule 4 names exactly this case.

**Grade stays C.** NPS says "Kautz's and Judah's brigades attacked", and Hobson says there had been "no communication between General Judah and myself". So Judah's column may have been engaged as a separate command before Judah joined Hobson, and Hobson is an interested account. Whether Hobson held command of all the side's engaged forces at first combat therefore remains unresolved.

**Change (OH001, side US).** Commander ID, rule, grade and candidates are unchanged.

- `labels`: `["responsibility_unresolved", "command_changed"]`
- `successor`: `"us-judah"`
- `citations`: append these two entries.

  ```json
  {"source_id": "or23-1-hobson-morgan-raid-selections-v2", "section": "hobson-1863-09", "locator": "p.660 (OCR page markers; not checked against print)", "quote": "The advance, under Colonel Kautz, drove in the pickets of the enemy about 5 a. m. July 19.", "battle_id": "OH001"}
  ```

  ```json
  {"source_id": "or23-1-hobson-morgan-raid-selections-v2", "section": "hobson-1863-09", "locator": "p.661 (OCR page markers; not checked against print)", "quote": "Learning from one of my orderlies that a column of cavalry was comiug up the river, to my right and rear,", "battle_id": "OH001"}
  ```

- `rationale`: "NPS puts the pursuing columns 'under overall direction of' Hobson. Hobson's report has his advance under Kautz drive in Morgan's pickets about 5 a.m. on July 19; only later, after his dispositions and Shackelford's call for reinforcements, did Judah's column come up the river, and Judah, whom Hobson acknowledges as his superior, 'immediately assumed command of the whole force' (rule 4: command_changed, successor Judah). NPS also says Judah's brigade attacked, and Hobson had had no communication with Judah, so whether Hobson commanded all the side's engaged forces at first combat is unresolved; Hobson's is an interested account. The listing stands (grade C)."

**Memo.** In `docs/research/command-responsibility-v1.md`:

- Replace "OH001 US: Hobson says Judah assumed command of the whole force, without dating it;" with "OH001 US: NPS has Judah's brigade attacking; Hobson says Judah, arriving after Hobson's advance had engaged, assumed command of the whole force (also `command_changed`);".
- Update the `command_changed` count (see the count note at the end).

### R2 — VA040 US: a passage the ledger missed states Warren's command

**Problem.** The rationale says "Humphreys praises the handling of the Second Corps without naming Warren; no inspected passage states the command." But Humphreys, a source the VA040 dossier cites, names Warren as commanding the engaged Second Corps at Bristoe, in the same `bristoe-station` section:

- "the head of Warren's Second Corps, Webb's division, appeared," (p.25; this is where Heth's division is directed against it);
- "General Warren states that his force on the field at the time of the engagement, was about 3,000 infantry," (p.29).

Nothing inspected contradicts the listing. Humphreys was Meade's chief of staff, an interested but separate family from NPS/CWSAC.

**Change (VA040, side US).** Rule stays 2.

- `grade`: `"A"`
- `echelon`: `"corps_or_wing"`
- `citations`: append these two entries.

  ```json
  {"source_id": "humphreys-bristoe-selections-v1", "section": "bristoe-station", "locator": "p.25 (OCR running head; not checked against print)", "quote": "the head of Warren's Second Corps, Webb's division, appeared,", "battle_id": "VA040"}
  ```

  ```json
  {"source_id": "humphreys-bristoe-selections-v1", "section": "bristoe-station", "locator": "p.29 (OCR running head; not checked against print)", "quote": "General Warren states that his force on the field at the time of the engagement, was about 3,000 infantry,", "battle_id": "VA040"}
  ```

- `bindings.cited_sources`: add
  `"humphreys-bristoe-selections-v1": {"metadata_sha256": "0b338d50cd6447c4ad09cfd64df22c887e1daa74ee5a80c05f1fe9ad57b561f7", "raw_sha256": "c22e8fd033a1bc44dd8c302595b309e8adb8c5cd3111e042eb0079d0a321aa70"}`.
  I computed these values with `source_metadata_digest` and the registered `sha256`.
- `rationale`: "Humphreys (an interested history by the Army of the Potomac's chief of staff) names 'Warren's Second Corps' as the force Heth's division struck at Bristoe and gives Warren's own statement of 'his force on the field at the time of the engagement'. A cited passage states the command."

### R3 — TN018 Confederate: the cited quote does not state D. H. Hill's command of the engaged forces

**Problem.** The only non-listing citation is "I ordered Cleburne’s division to Harrison,". In context (`or30-2-hill-chattanooga-selections-v1`, section `hill-chattanooga`) this is Hill's *response after* the shelling, sending a division from his corps "encamped on the Chickamauga about Tyner's Station" to Harrison, away from the town: "The shelling of Chattanooga revealed the fact that the Yankees were in our immediate front, and I ordered Cleburne’s division to Harrison,".

The report also routes information to "the commander-in-chief". Nothing inspected states that Hill commanded the Confederate forces at Chattanooga when the shelling began. Nothing contradicts the single listing either, so the grade table gives B, not A.

**Change (TN018, side Confederate).** Commander ID, rule 2 and labels are unchanged.

- `grade`: `"B"`
- `citations`: keep only the listing citation (rank "Lieutenant General"). Remove the Hill citation, because the checker requires grade B to cite only the listing.
- `rationale`: "Single CWSAC listing (Lieutenant General). Hill's report shows him commanding a corps camped about Tyner's Station and guarding the river crossings, and ordering Cleburne's division to Harrison after the shelling revealed the Federals; no inspected passage states that he commanded the Confederate forces at Chattanooga when the shelling began, and none contradicts the listing."

The echelon may stay `unknown`; see A5.

### R4 — TN021 Confederate: a passage the ledger missed on Longstreet's role

**Problem.** Cist, which the dossier cites for this battle (`cist-reopening-tennessee-selections-v1`, section `brown-ferry-and-wauhatchie`, p.241), attributes the night attack's execution to Longstreet: "Dividing his com- mand into two detachments, Longstreet, about an hour later, with his strong one on his left, assaulted Geary's camp". It also says of the opening skirmish: "was a portion of Longstreet's corps getting into position for a night attack on the two encampments."

The ledger's `superior_directing` rests only on the frozen description ("decided to mount a night attack"). It does not cite or discuss Cist, although the grade B condition ("nothing inspected contradicting") depends on how this passage is read.

**Reading adopted.** I read the passage under the design's §2 carve-out: a superior (the corps commander) directing within the theater is not a contradiction. On that reading Jenkins stays, grade B. See A2 for the alternative reading, which the primary should decide.

**Change (TN021, side Confederate).** Commander ID, grade B, rule 2, labels and superior are unchanged.

- `superior_citations`: append

  ```json
  {"source_id": "cist-reopening-tennessee-selections-v1", "section": "brown-ferry-and-wauhatchie", "locator": "p.241 (OCR page markers; not checked against print)", "quote": "Dividing his com- mand into two detachments, Longstreet, about an hour later, with his strong one on his left, assaulted Geary's camp", "battle_id": "TN021"}
  ```

- `rationale`: "Single CWSAC listing; no inspected passage states Jenkins's command (Bratton reports as colonel commanding Jenkins' brigade without naming Jenkins's role). The description has Longstreet and Bragg deciding on the night attack, and Cist, an interested Union history written after the war, has Longstreet dividing his command and leading the left detachment against Geary. This is read as the corps commander directing within the theater (superior_directing: Longstreet), not as a contradiction of the listing."

### R5 — GA003 Confederate: Bragg arrived and took direct command before the fighting ended (rule 4)

**Evidence.** Hindman's report (`or30-2-hindman-mclemores-cove-selections-v1`, section `hindman-1863-10-25`, p.296–297) says: "About dark our ineffectual pursuit of the enemy ceased, under orders given to General Buckner direct by the general commanding, to whom I then reported in person at Davis’ Cross-Roads." Bragg then "ordered the command marched that night". Cist (`bragg-and-the-cove`, p.186) independently puts Bragg on the field from the morning of the 11th: "Bragg shortly after daylight joined Cleburne, where they waited nearly all day for Hindman's guns to open".

So a superior arrived and issued orders direct to Hindman's subordinate, ending the engagement: rule 4's "a superior arriving and taking command after the first combat". Hindman's report was written after his suspension, is self-defensive, and is not a contemporaneous record, as the dossier already notes. This label does not change the choice or the grade.

The current superior citation quotes only "waited nearly all day for Hindman's guns to open", which does not name Bragg. The fuller sentence in the same section does.

**Change (GA003, side Confederate).** Commander ID, rule 3a, grade A, superior and candidates are unchanged.

- `labels`: `["superior_directing", "command_changed"]`
- `successor`: `"cs-braxton-bragg"`
- `citations`: append

  ```json
  {"source_id": "or30-2-hindman-mclemores-cove-selections-v1", "section": "hindman-1863-10-25", "locator": "p.297 (OCR page markers; not checked against print)", "quote": "orders given to General Buckner direct by the general commanding, to whom I then reported in person at Davis’ Cross-Roads.", "battle_id": "GA003"}
  ```

- `superior_citations[0].quote`: `"Bragg shortly after daylight joined Cleburne, where they waited nearly all day for Hindman's guns to open"`. Keep the dossier reference `delay-and-suspension`/7.
- `rationale`: append "Hindman, in an interested report written after his suspension, says the pursuit ceased at dark under orders given direct to Buckner by the general commanding, to whom he then reported in person; Cist has Bragg with Cleburne from shortly after daylight (rule 4: command_changed, successor Bragg)."

### Count note for the memo and the checker summary

If R1–R5 are applied:

- **Grades:** A/B/C/D stay 149 / 15 / 15 / 3 (VA040 US +A −B; TN018 CS −A +B).
- **`command_changed`:** 11 → 13.
- **Sides with `unknown` echelon:** 76 → 75.
- **Commander IDs:** none changes, so the memo's commander table for the primary rows is not affected. I did not recompute that table.

## Advisories (not required)

- **A1. GA003 Confederate: the first fighting and stronger 3(a) citations.**
  - **What the same report shows about the first fighting.** The first fighting of the 10th was at Dug Gap against Hill's corps (Wood's brigade), outside Hindman's command. Hindman quotes Wood's dispatch that the enemy "had charged and broken his cavalry". Hindman's command grew to include Buckner's corps only at 4.45 p.m.
  - **Why the choice stands.** Under §2, Bragg's direction (already labelled) covers the divided command, and Breckinridge is correctly excluded ("kept in posi- tion south of La Fayette").
  - **Suggested citations.** For 3(a), add passages from the same section (p.293) that state Hindman's command more directly than the suspension order does:
    - "cavalry detachments, of which I assumed command,"
    - "At 4.45 p. m. General Buckner reached Morgan’s with his corps, and reported to me for orders."
- **A2. TN021 Confederate: the alternative reading.** Taken literally, Cist names Longstreet as leading the engaged force when the fighting began. Treated as a rule 2 contradiction, that would give Longstreet, grade C, `responsibility_unresolved`, with Jenkins as a candidate.
  - **Why R4 does not adopt it.** Longstreet was Jenkins's superior, and §2 excludes a superior's direction from being a contradiction. Cist is a single, interested, post-war Union history.
  - **Decision.** The primary should confirm the reading. Either way the Cist passage must be recorded (R4).
- **A3. VA040 US: Meade as a possible superior.** Humphreys shows army headquarters directing the Second Corps toward Bristoe and ordering support back to it:
  - "General Warren was di- rected to move as rapidly as possible, as the enemy would probably send a column to Bristoe."
  - "As soon as General Meade received intelligence of the enemy's appearance at Bristoe, ... those corps were or- dered back to its support." (Here "..." marks my elision.)

  The phrasing is passive. For consistency with the Parke-based labels at TN026 and TN028, consider `superior_directing: us-george-g-meade`.
- **A4. GA005 Confederate: a possible superior label.** Cleburne held the gap on an army-headquarters order ("The general desires that you will take strong position in the gorge of the mountain and attempt to check pursuit of enemy.", p.754). He withdrew only after "About 12 m. I received a dispatch from Lieutenant-General Har- dee, to the effect that the train was now well advanced, and I might safely withdraw." (p.757), with Breckinridge and Wheeler present "lending me their personal assistance".
  - **Consistency.** Under the standard applied at TN026 and TN028, this may call for `superior_directing`.
  - **What it would need.** Hardee is not in the registry, so it would need a passage-only entry, and binding `or31-2-cleburne-ringgold-gap-selections-v1` (metadata `b6805e4ed4e7e9e8a712837e6a1650ac6bab1dd7f33ce3a4f624a9fd5187ed62`, raw `45302ddc411ec6f54d7e496d05f7a8d7cb9bbd9dcddb3584063473b10fa953b3`).
  - **Why only advisory.** The order is signed by the AAG for an unnamed "general", and Hardee's dispatch permits a withdrawal rather than directing the defence.
- **A5. TN018 Confederate: echelon.** Hill's report heading ("commanding corps") and "was assigned to Hardee’s old corps" support echelon `corps_or_wing` for Hill. Whether that is the echelon of the force engaged at Chattanooga is what R3 leaves open, so `unknown` is also defensible.
- **A6. Optional stronger citations and echelons.**
  - **TN020 US.** "I left Knoxville on the morning of the 9th and overtook our forces on the same day at Bull’s Gap." dates Burnside's presence before the first combat on the 10th.
  - **TN026 US superior.** Parke's dispatch ("I have directed him to hold Bean’s Station in force,"; his heading reads "commanding United States forces in the field") is more direct than the description. The source `or31-1-parke-beans-station-selections-v1` is not yet bound.
  - **TN028 Confederate.** The cited description quote concerns 14 January, before the frozen date. Longstreet's report (`or32-1-longstreet-dandridge-selections-v2`, not yet bound) describes the 17th ("On the 17th, a part of Hood’s division was moved down to the enemy’s immediate front.") but in passive voice. Grade A is thin but tenable.
  - **TN022 US echelon.** Hatch's "Eight companies of this brigade" supports `brigade`.
  - **TN025 US.** Burnside's "Orders were issued for the whole command to be on the alert" is passive. Grade B is appropriately conservative.
- **A7. WV012 Confederate: echelon.** Echols assumed "command of the whole force": his brigade, Jackson's command and part of Jenkins's cavalry. `brigade` follows the frozen description; `detachment_or_post` would also be defensible. The choice is sound either way.
- **A8. Registry.** The passage-only `us-judah` has a citation that resolves. The `cs-d-h-hill` merge ("D. H. Hill" / "D.H. Hill") is on listing fields as the design allows. I found no other issue in the IDs used by this batch.

## Unresolved items kept visible

- **OH001:** whether Judah's column was engaged before Judah joined Hobson.
- **GA003:** the cause of the failed attack, disputed between Bragg's order and Hindman's account (the dossier leaves it open).
- **TN021:** the rule 2 reading of Cist (A2).
- **TN018:** whether any Confederate unit engaged the battery on 21 August, and under whom.

None of these is resolved by this review.
