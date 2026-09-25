# Separate review: 1861 Western and Trans-Mississippi first passes

**Outcome: corrections required** (14 required corrections, W61-R1 to W61-R14; 12 advisories,
W61-A1 to W61-A12).

This is an AI review. It is a separate analysis. It is not human historical adjudication, proof that
sources are independent, or admission of any feature. The primary agent should check each finding
against the cited passages before changing any evidence.

## Reviewer record

| Item | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), `high` reasoning effort, fresh-context reviewer subagent |
| Date | 2026-09-25 |
| Prepared commit reviewed | `8a97ac1f37f5d260329c682dab15af8443965c40` |
| Previous commit (diff base) | `0b4fbb8` |
| Assignment bundle commit (worktree HEAD) | `e72731fca9799260e77d670d691c2d0c20e8f6d9` |
| `assignment.md` SHA-256 | `b3c4e5e1c8e5d8546a704157b82705f544e0de7645d1b9b2c7e32654d35c09b8` (verified) |
| `inputs.json` SHA-256 | `dba5811a6c190804ede004205f54322b6bddfffc9807ae3c67204c91a549e4a2` (verified) |
| Input hashes | All 121 paths in `inputs.json` match both `git show 8a97ac1…:<path>` and the worktree. No mismatch. `git diff 8a97ac1 HEAD` touches only the two bundle files. |
| `make check` (offline) | Passed. 134 unit tests OK; `python3 -m generalship check` exited 0 (127 pilot battles, 23 eligible, 257 draft dossiers). |

I did no network research, opened no extra source families, spawned no agents and ran no build or
packet commands. I committed and pushed nothing. In the repository I wrote only this file. Outside the
repository I wrote two scratch files under `/tmp`: a read-only dossier-printing script and the
`make check` log.

## Scope actually inspected

- **Instructions and docs.**
  - Read: `AGENTS.md`, `docs/evidence-contract.md` (in full), `docs/cohort-v2.md` (in full) and the
    "Research depth and coverage" section of `docs/methodology.md`.
  - Read: all six first-pass memos, and in `docs/sources.md` the author-group rule and the 1861
    section.
  - Not read: `README.md`, `docs/roadmap.md` and the rest of `docs/methodology.md`.
- **Dossiers.** All 19. For every claim I read the value, status, phase and rationale.
  - I read all 759 citation occurrences against the full text of their cited section.
  - I read every report selection section in full, and every Snead and Britton narrative section in
    full. The Britton front matter was read once, from the Missouri selection; the other two Britton
    selections reproduce it from the same parent.
  - Recount: 171 claims, 20 null unknowns, 55 `disputed` and 759 citations. These match the memo
    totals and per-memo breakdowns: Missouri 72/8/334 with 25 disputed; Eastern Kentucky 36/5/148
    with 9; FL001 9/1/50 with 3; MO009 9/1/49 with 3; Indian Territory 27/3/116 with 10; Northeast
    Missouri 18/2/62 with 5.
  - Every dossier covers all seven dimensions. KY001 cites two families; each of the other 18 cites
    exactly three.
- **Frozen Arnold rows.** The battle, force and commander rows for all 19 records.
- **NPS pages.** All 18 retained NPS text snapshots. MO010 has only a registered empty-template HTML,
  which I did not open.
- **Source records.**
  - I read all 78 records added at the prepared commit, including their edition, section dates,
    group, dependency note and inspection fields.
  - I compared the author groups with the existing registry groups for Britton, Price, Grant, Nelson,
    Prentiss, Williams, Hindman and Sturgis, including those records' author fields.
- **Selections.**
  - For all 29 new selections, `parent_sha256` equals the registered parent's hash.
  - Re-extracting each of the 82 ranged sections with the documented split/join transform reproduces
    the snapshot text exactly.
  - Catalog metadata: I read the identifier, title, volume, date and contributor fields for OR III,
    IV, VI and VIII, Snead and Britton volume I. I also read the OR IV OCR title page.
- **Not inspected:**
  - the OCR parents outside their selected ranges, beyond the OR IV title page;
  - the NPS HTML files;
  - the Illinois scans said to be other series, which were not retained and cannot be checked
    offline;
  - every deferred family listed in the memos.

Checks establish passage presence, not truth. Where I say a quote supports a claim, that is an
extraction judgment, not historical adjudication.

## Required corrections

Unless stated otherwise, each new citation uses the section's existing locator convention
("p.N (OCR page markers; not checked against print)"). Every quote below occurs exactly once in the
named section; I checked this against the retained snapshot.

**W61-R1: FL001 `command-roles` (support).**
- **Problem.** The value says Brown "sent Vogdes and Arnold out from the fort and ordered Wilson to
  attack". No cited quote supports the Wilson order. Citation [4] shows Arnold first ordered to
  "man the guns on the ramparts", not sent out.
- **Value.** Replace "Brown sent Vogdes and Arnold out from the fort and ordered Wilson to attack;"
  with "Brown sent Vogdes out with two companies and had Arnold man the ramparts, then ordered Arnold
  forward with two companies to support Vogdes and sent Wilson an order to advance and attack;".
- **Add citations.** Both are `or6-brown-santa-rosa-selections-v1`, section `brown-1861-10-11`,
  p.440:
  - "ceed to support Major Yogdes with two compauies"
  - "sent an order to Colonel Wilson to advance and attack the enemy"

**W61-R2: MO009 `stated-aims` (completeness; NPS and frozen description).**
- **Problem.** The claim records Grant's November 20 statement that his object "was accomplished to
  the fullest extent". It omits the contrary assessment in the NPS page and the frozen description.
- **Add citation.** `nps-mo009-v1`, locator `Description`: "Grant did not accomplish much in this
  operation".
- **Value.** Append "NPS says Grant did not accomplish much in this operation."
- **Status.** Change from `supported` to `disputed`.
- **Rationale.** Append "Grant's own after-action assessment and the NPS assessment differ; neither
  is a campaign-contribution finding."

**W61-R3: MO002 `reported-force-scope` (scope of the NPS figure).**
- **Problem.** NPS's "approximately 4,000" describes the force Lyon chased from Jefferson City and
  Boonville. It is not an estimate of the Governor's force at Carthage.
- **Value.** Replace "NPS says Sigel had about 1,000 and the Governor approximately 4,000." with
  "NPS says Sigel led a force of about 1,000, and that Lyon had earlier chased the Governor and
  approximately 4,000 State Militia from Jefferson City and Boonville; that figure is not a count at
  Carthage."
- **Citation [3].** Replace the quote with "had chased Governor Claiborne Jackson and approximately
  4,000 State Militia from the State Capital at Jefferson City and from Boonville" (`nps-mo002-v1`,
  `Description`).

**W61-R4: MO005 `recorded-result` (date and engagement attribution).**
- **Problem.** Lane's "drove back the advanced guard" recalls an earlier, undated message. The same
  sentence reports the loss of Weer's mules, which Britton places on the evening of September 1. The
  passage does not establish that the advanced guard was driven back in the September 2 action.
- **Value.** Replace "Lane reports driving back the enemy's advanced guard and a gallant fight before
  falling back that night;" with "Lane's September 3 letter recalls an earlier, undated report that
  his men drove back the enemy's advanced guard (in the same sentence as the loss of Weer's mules,
  which Britton places on September 1). It says his cavalry engaged the whole enemy force for two
  hours the day before, calls the fight a gallant one and says he fell back that night;".
- **Citation [3].** Replace the quote with the full sentence "I informed you that we drove back the
  advanced guard of the enemy and of the loss of Weer's mules."
- **Add citation.** `or3-lane-dry-wood-selections-v1`, `lane-1861-09-03`, p.163: "My cavalry engaged
  the whole force of the enemy yesterday for two hours".
- **Missouri memo, Dry Wood dispute bullet.** Replace "Lane claims to have driven back the enemy's
  advance guard" with "Lane recalls, without a date, that his men drove back the enemy's advanced
  guard, and says his cavalry engaged the whole enemy force for two hours on September 2".

**W61-R5: MO006 `command-roles` (attribution within Britton).**
- **Problem.** The quote cited for Britton "blames the department commander or his subordinates"
  ([7]) is Britton's report of what Mulligan's council felt ("They were deeply sensible that…"). It is
  not his own judgment.
- **Value.** Replace "and blames the department commander or his subordinates for the garrison's
  plight" with "says Mulligan's council was sensible that the blunder or incompetency of the
  department commander or his subordinates had placed them there, and himself ascribes the disaster
  to unpardonable blunders and want of concert among subordinate Federal commanders".
- **Citation [7].** Extend the quote to "They were deeply sensible that through the blunder or
  incompetency of the Depart- ment commander or his subordinates" (p.142).
- **Add citation.** `britton-border-1-missouri-1861-selections-v1`, `lexington`, p.143: "It was a
  disaster that was due to a series of unpardonable blunders and want of concert of action among
  subordinate Federal commanders".

**W61-R6: MO003 `command-roles` (passive voice).**
- **Problem.** The source says "it was deemed advisable to fall back". It does not name who decided.
  The review-correction precedent PRV-R2 treated a passive order the same way.
- **Value.** Replace "Scott decided to fall back." with "Scott reports that it was deemed advisable
  to fall back." The citation is unchanged.

**W61-R7: MO007 `recorded-result` (completeness; dispute visibility).**
- **Problem.** Thompson's October 22 dispatch to Polk, in the selected passages, calls the action his
  defeat. The claim quotes only his October 23 "we were victorious".
- **Value.** Replace "Thompson writes that he was victorious though he fell back before an
  overwhelming force." with "Thompson's October 22 dispatch to Polk asks for troops because the
  people 'may be discouraged by my defeat'; his October 23 letter says he was victorious though he
  fell back before an overwhelming force."
- **Add citation.** `or3-thompson-fredericktown-selections-v1`, `thompson-1861-10-22`, p.228: "as
  they may be discouraged by my defeat."
- **Missouri memo, Fredericktown dispute bullet.** Add "and Thompson's own October 22 'my defeat'".

**W61-R8: KY003 `reported-force-scope` (unsupported rationale; figure timing).**
- **Problem.** The rationale says Williams's "two reports differ on the mounted companies". His
  November 13 report gives no company count. The difference is between the CWSAC's "two of mounted
  men" and his November 9 "five companies of mounted men". His November 9 figure of 1,100 describes
  his command after the fight ("We have now").
- **Value.** Replace "and gives his command as nine infantry and five mounted companies, 1,100 in
  all" with "and gives his command at the time of writing ('We have now') as nine infantry and five
  mounted companies, two of the latter not full, 1,100 in all".
- **Rationale.** Replace "his two reports differ on the mounted companies and on the men at the
  pass" with "the CWSAC's two mounted companies do not match the five mounted companies of his
  November 9 report (the November 13 report gives no company count), and his two reports differ on
  the men at the pass (about 300 against 250)".

**W61-R9: KY004 `command-roles` (timing of Hindman's absence).**
- **Problem.** By his own report, Hindman was present at the first exchange of skirmish fire. He left
  during a half-hour lull, and the firing recommenced before he returned. "Both listed commanders
  were away when the fight began" overstates the passage for Hindman.
- **Value.** Replace "Hindman had gone to choose a camp, leaving Colonel Terry in command, and later
  withdrew his command." with "Hindman, present at the first exchange of skirmish fire, went to
  choose a camp during a lull of about half an hour, leaving Colonel Terry in command, and the firing
  recommenced before he returned; he later withdrew his command."
- **Rationale.** Replace "Both listed commanders were away when the fight began, by their own
  reports;" with "By their own reports, Willich was at division headquarters when the general alarm
  was given, and Hindman was away choosing a camp when the skirmish fire recommenced after a lull;".
- **Citation [6].** Replace it with these two, both `or7-hindman-rowletts-station-selections-v1`,
  `hindman-1861-12-19`, p.20:
  - "The firing ceased for about half an hour, and I went in person to select a suitable place for
    camp"
  - "Before returning to the column the fire from the skirmishers recom- menced."
- **Eastern Kentucky memo, "Command roles" bullet.** Make the same wording change.

**W61-R10: OK001 `command-roles` (passive voice).**
- **Problem.** Cooper writes "A charge was ordered to be made by the detachment of Texas cavalry".
  The value turns this into "Cooper ordered".
- **Value.** Replace "Cooper ordered Quayle's Texas cavalry to charge the camp and rode forward in
  person at the night encounter." with "Cooper's report says, in the passive, that a charge was
  ordered to be made by Quayle's Texas cavalry upon the camp, and Britton says Quayle charged it;
  Cooper rode forward in person with Bourland at the night encounter."
- **Add citation.** `britton-border-1-indian-territory-selections-v1`, `indian-territory`, p.166:
  "Colonel Quayle charged this camp with his Texas cavalry".

**W61-R11: OK001 `recorded-result` (completeness; dispute visibility).**
- **Problem.** Britton, in the selected chapter, says that no engagement took place that night.
  Cooper and the frozen description describe a short night fight at close range. The dossier does not
  record this conflict.
- **Value.** Append "Britton also says that when Cooper came up it had become very dark and no
  engagement took place that night; Cooper describes a short but sharp night conflict."
- **Add citations:**
  - `britton-border-1-indian-territory-selections-v1`, `indian-territory`, p.167: "no engagement took
    place that night."
  - `or8-cooper-indian-territory-selections-v1`, `cooper-1862-01-20`, p.6: "After a short but sharr
    conflict the firing of the enemy ceased".
- **Indian Territory memo, Round Mountain dispute bullet.** Add this point.

**W61-R12: OK002 `command-roles` (passive voice).**
- **Problem.** Cooper's report states both the formation and the Creek regiment's order in the
  passive.
- **Value.** Replace "Cooper formed three columns and ordered D. N. McIntosh's Creek regiment to turn
  the enemy's right." with "Cooper's report says, in the passive, that the forces were formed in three
  columns and that D. N. McIntosh's Creek regiment was ordered to turn the enemy's right; Britton says
  Cooper ordered his train parked and formed his troops in three columns."
- **Add citations:**
  - `or8-cooper-indian-territory-selections-v1`, `cooper-1862-01-20`, p.8: "the forces were formed in
    three columns"
  - `britton-border-1-indian-territory-selections-v1`, `indian-territory`, p.169: "Colonel Cooper
    ordered his train parked in the prairie"

**W61-R13: MO011 `command-roles` (passive voice in a disputed command claim).**
- **Problem.** Torrence reports the assignment to Hunt and the First Iowa charge in the passive. This
  matters because the claim is `disputed` precisely on who commanded.
- **Value.** Replace "assigned Hunt the carbine companies and ordered the First Iowa charge." with
  "and his report states in the passive that Hunt was assigned the carbine-armed force and that three
  First Iowa companies and part of Merrill's Horse were ordered to charge, without naming who gave the
  orders."
- **Add citation.** `or8-torrence-roans-tan-yard-selections-v1`, `torrence-1862-01-10`, p.50: "I
  marched my command to Boone ville".
- **Rationale.** Append "Torrence's orders are reported in the passive."

**W61-R14: Registry/docs (author-group reconciliation not carried out).**
- **Britton.** Five Britton volume I records carry the group `britton-civil-war-border` while volume
  II is registered as `britton-civil-war-border-1899`. The five are `ia-britton-border-1-metadata-v1`,
  `britton-border-1-ocr-v1` and the three selections. Their dependency notes still say "the primary
  should reconcile the group name at merge".
- **Price.** The Price Lexington record (`price-lexington-report`) says there is "No earlier registry
  group for this author in this worktree" and asks for reconciliation at merge. The registry already
  has `price-camden-1864-report` and `price-missouri-1864-reports`.
- **Effect.** No reconciliation is recorded in `docs/sources.md` or the memos. Under the
  `docs/sources.md` same-author rule, no independence is actually overcounted. The records still
  describe an unexecuted step.
- **Minimum correction** (records stay immutable, following the A4 precedent in the Price memo). Add
  this to the 1861 section of `docs/sources.md` and to the Missouri memo's "Independence groups":

  > "Britton volume I (`britton-civil-war-border`) and volume II (`britton-civil-war-border-1899`)
  > are one witness family. Price's Lexington report (`price-lexington-report`) is the same family as
  > `price-camden-1864-report` and `price-missouri-1864-reports`. The volume I and Price dependency
  > notes that ask for reconciliation at merge predate the merge; the records are left unchanged."

  In the Missouri memo, this replaces "the primary should reconcile the two volumes' group at merge"
  and "(the Price 1864 pass may register Price reports; reconcile at merge)".
- **Optional.** Metadata-only successors aligning the volume I group, as in PRV-R4. This review does
  not require them.

## Assignment questions on source choices

- **University of California OR III and IV scans.** Sound.
  - The retained OCR title pages read Series I Volume III (1881) and Series I Volume IV (1882). The
    catalog identifiers are `warofrebellion03secrrich` and `warofrebellion04secrrich`.
  - All selections re-extract from the pinned parents.
  - The statement that the Illinois `…03unit`, `…03unit_0` and `…04unit` scans are other series is
    recorded but was not verifiable offline, because they were not retained.
- **Britton volume I, 1891 second edition.** Sound and documented. The title page reads "SECOND
  EDITION, REVISED … ]89i", copyright 1890, and the preface is dated Washington, 1890. The registry
  records that no 1890 first-edition scan was found. Text may differ from the first edition; the
  edition is pinned.
- **Author groups.**
  - Sturgis (`sturgis-dandridge-operations-reports`, Samuel D.), Williams
    (`williams-east-tennessee-reports`, John S.), Hindman (`hindman-mclemores-cove-reports`, Thomas
    C.), Nelson (`or-nelson`) and Prentiss (`or-prentiss`) are the same authors as their existing
    groups. `or-nelson` and `or-prentiss` are Shiloh reporting-chain groups that also contain
    subordinates, which is a conservative grouping.
  - Grant goes in `or-grant`, correctly.
  - Britton and Price are the subject of W61-R14.
- **Turner relaying Hubbard as a separate family.** Acceptable. The underlying witness is Hubbard, a
  participant distinct from Torrence; Turner only relays him. See W61-A6.
- **Cooper's report for Chustenahlah.** Defensible.
  - The frozen force field names Cooper's brigade. Cooper's report is the one inspected source that
    addresses whether it was engaged.
  - Cooper was not present, and he says he heard of the attack on the 27th. His account of the fight
    is second-hand, and the dossier's rationales keep it so.
  - See W61-A5 on Britton.
- **Grant's Belmont report dated as printed.** Acceptable as recorded ("dated as printed"). See
  W61-A1.
- **MO011 kept outside its campaign label.** Sound. The frozen date is 1862-01-08, and the frozen
  campaign row and NPS both say December 1861. Changing it would alter the cohort.
- **KY001 with two families.** Sound under the effort ceiling. The OR IV heading prints only
  Zollicoffer's report for Barboursville, and the dossier keeps the gap explicit, with ground as a
  null unknown.

Phase tags are sensible. The `inherited` tags cover natural ground: the Carthage ridge, Bloody Hill,
the Ivy defile, the Santa Rosa sand ground, the Round Mountain creek timber, the Chustenahlah hill,
and the Roan's Tan-Yard ravines and fog. Worked ground stays `unresolved`: the Lexington works, the
Belmont abatis and the Chusto-Talasah logs. Fredericktown's positions are `commander_created`. No
opening strength is adopted: all 19 `opening-personnel-unknown` claims are null. No morale or
readiness score, probability or causal credit appears.

## Advisories (no change required)

- **W61-A1 (MO009 Grant date).** The registry's "dated as printed" is accurate.
  - From general recollection, which I cannot cite and have not verified in any inspected source, the
    composition date of Grant's printed Belmont report has been questioned in later scholarship.
  - This is only a research lead. Keep the section date as printed, and do not treat it as a verified
    contemporaneous composition date.
- **W61-A2 (FL001 completeness).**
  - NPS's "Gen. Anderson then adopted a defensive stance to entice the Federals to leave the fort and
    attack" is not accounted for. Anderson says he retired at daylight.
  - Brown's October 9 "about a dozen of their dead; some 30 prisoners" is not recorded.
  - The Confederate paper's 175 is its upper bound for the Confederate loss. It paired this with 250
    for the Union loss ("while 250 will probably barely cover tbat of the Federalists."), and the
    value should say so.
- **W61-A3 (MO009 Pillow).**
  - "Each below 500" is an inference; Pillow writes that "These regiments … had been reduced to below
    500 meu for duty".
  - His November 9 "The enemy's double ours." (a loss comparison) is not recorded.
- **W61-A4 (KY004).** NPS says the bridge was "completed on December 17"; Willich says it was
  finished on the evening of the 15th. The dates differ and the `pontoon-bridge` claim does not note
  it.
- **W61-A5 (OK003).** Britton p.173 says "Colonel Mcintosh reported a loss of nine men killed and
  forty wounded." That bears on McIntosh's OCR closing line "Killed, 0 ; wounded, 40." Record it as a
  lead in the open questions. It would be a fourth family and is not independent of McIntosh, so do
  not cite it as corroboration.
- **W61-A6 (MO011).** Describe the third family as Hubbard's account relayed by Turner. If Hubbard's
  own report is registered later, it belongs to the same family. Both report families are Union; no
  Confederate account was inspected. The memo says so; the dossier's open questions could say so too.
- **W61-A7 (MO003).**
  - Scott's scouts "lost 4 killed and 1 wounded." That matches Atchison's morning picket claim.
  - Atchison's "3 or 4 o'clock" approach time agrees with Scott's 3 p.m. against NPS's 3:00 am.
  - Both points could be added to the existing claims.
- **W61-A8 (MO008).** Cite "clearing the town and neighborhood" for the value's "cleared the town".
- **W61-A9 (MO006).**
  - Britton says Price withdrew on the 13th "feeling that his force was not strong enough to make a
    successful assault, and being short of ammunition". Price says a short delay would make success
    certain. The difference could be added to `stated-aims`.
  - NPS's surrender "after noon" and Price's white flag "After 2 o'clock" are minor timing
    differences.
- **W61-A10 (MO002).** Snead's quoted Confederate-historian estimate of Sigel's loss is not recorded:
  150 to 200 killed and 300 to 400 wounded.
- **W61-A11 (KY003).** Williams's November 9 "lasting about four hours" and Nelson's "an hour and
  twenty minutes" are an unrecorded duration dispute.
- **W61-A12 (registry note).** The OCR heading of Zollicoffer's October 20 report reads "October 20,
  1801." The section date 1861-10-20 is right. The inspection note mentions only Schoepf's "1801",
  and could mention this one too.

## Unresolved items

None of the findings require new research. W61-A1 is a lead, not a finding. All other historical
disputes stay as the dossiers record them.
