# Chancellorsville Campaign separate review (VA032, VA034, VA033)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`; a fresh-context
  `evidence-reviewer` subagent. This is an AI review: a separate analysis, not human historical
  adjudication, independent corroboration or feature admission.
- **Date:** 2026-09-25
- **Commits:** prepared `c3a49116df083863dee0a0ddf7d1947cb2d000ba`; previous
  `0f341660bdb72868683b27842fd6597eec8b8182`; worktree/bundle HEAD
  `4db650fb881ed1c2fd7199504c87e556a3d153ac`. The only difference between the bundle and the
  prepared commit is the two bundle files.
- **Assignment** `assignment.md` sha256 `3e9abe8c77e941e70a4d06187359db25065ac1fb7dc18e9f6b09eefd9cb7c857`;
  **input manifest** `inputs.json` sha256 `98e8e40d88ee654f77a3835205b427ac84032357963973c668d83277262ab892`.
  All **42/42** bound paths match their manifest hashes, both in the worktree and in the
  `git show c3a4911:<path>` blobs. **No mismatches.**
- **Outcome: corrections required** (CV-R1 to CV-R10). All are extraction, locator or wording
  fixes. None requires new research.

## Scope actually inspected

- **Claims and citations.** I read all 27 claims (9 per record), the 3 null unknowns, and all 7
  dimensions per dossier. I checked all 119 citation occurrences (VA032 50, VA034 33, VA033 36)
  for entailment and attribution in context, not only for quote presence. For each OR and NPS
  quote I printed about 350 characters of surrounding text. For each Doubleday quote I read the
  whole selected section.
- **Source files.** I read the three NPS text snapshots in full. I read all seven Doubleday
  selection sections in full. In the Doubleday parent OCR I read the regions around each range
  boundary and every page marker from p.2 to p.74, plus the 1883 preface signature, the "my
  division" passages at offsets 17935 and 23985, and the index entry. I read Lee's, Sedgwick's
  and Early's selections at every cited passage and at the surrounding passages used below.
  I read the Doubleday catalog `metadata` block. I did not read any whole book or the whole OR
  volume.
- **Frozen rows.** I checked the frozen `cwsac_battles`, `cwsac_forces` and `cwsac_commanders`
  rows for VA032, VA033 and VA034, including every cited cell.
- **Replays.** I replayed every derivative:
  - The three NPS text files from their HTML, using the recorded HTMLParser transform. All are
    byte-identical and hash-identical.
  - The seven Doubleday sections from `doubleday-ocr-v1`.
  - Two sections each for Lee, Sedgwick and Early from `or25-1-illinois-ocr-v1`.

  In every case the recorded half-open character ranges, with whitespace collapsed, equal the
  section text exactly. Parent hashes match. Section date maps and editorial sections are
  complete.
- **Page-marker maps.** Every OR locator (Lee pp.796–804, Sedgwick pp.558–562, Early
  pp.1000–1002) matches the nearest preceding printed-page marker. Early's p.1000 is correctly
  inferred before the p.1001 marker.
- **Registry.** 429 entries / 426 paths. The previous 417 entries are byte-for-byte equal and in
  the same order, with 414 paths. The 12 new IDs are as the memo states. All 429 raw hashes
  verify.
- **Coverage.**
  - Dossiers: 90/127, 37 without. There are 36 campaign groups and 22 are complete by presence.
  - The 87 older dossiers and all 52 history files are unchanged (`git diff 0f34166 c3a4911`
    shows only additions).
  - Unchanged files: `cohort.json`, both admission proposals, the frozen CSVs,
    `admission-check.json` (`promoted_rows` 0), `baseline.json` and `battles.json`.
  - Baseline: 23 eligible in 13 groups; strength Brier 0.2768816348133779 against 0.25 for
    equal odds.
- **Next group.** Streight's Raid, AL001, starting 1863-04-30, is confirmed as the earliest
  incomplete group. It ties with Chancellorsville on start date and sorts after it by label.
- **Packets.** In all three packets, the assigned-record block equals the `battles.json`
  record, the draft block equals the dossier file, and the registry block equals
  `data/sources.json`.
- **Receipt.** All 156 input hashes, 429 source hashes and 7 output hashes verify. All 90
  dossiers and 52 history files are bound.
- **`make check`.** Run offline: 82 tests OK, `generalship check` exit 0, `draft_dossiers` 90,
  `admission_promoted_rows` 0, `artifacts_written: false`. I ran no build or packet commands.

### Confirmed without correction

- **Nesting.** VA034 (May 3) and VA033 (May 3–4) fall inside VA032 (Apr 30–May 6). No
  multi-engagement total is assigned or added: not Doubleday's 17,197 / 13,019 or Sixth Corps
  4,601, not Sedgwick's 4,925, and not Early's 136/838/500.
- **Force scopes.**
  - VA032's 97,382 / 57,352 are kept as imported, with `strength_min` cited.
  - VA033 and VA034 read "Corps" and have blank bounds.
  - Live zeros are not treated as measured.
  - Sedgwick's 15,000 is correctly treated as a report he received.
- **Ranks.** Lee is General in the frozen rows and Major General in the live heading. Jackson is
  Major General in the frozen row and "Lieutenant-General" in Lee's report. Neither heading rank
  is adopted.
- **Early's flag of truce.** It is correctly attributed and no causal inference is drawn from it.
- **Doubleday's status.** He is correctly recorded as an interested participant. The division
  command is supported in the pinned parent OCR: "I went with part of my division" (offset
  17935) and "aimed at my division" (offset 23985). Those pages are not in the selection.
- **Registry claims.** The 1882 imprint and the preface signed "New Yobk, January, 1883" are
  correct.
- **Remaining claims.** All other claims are entailed by their passages. Phase tags are
  hypotheses only; there is no `inherited` tag. No score, probability or causal effect is
  introduced.

## Required corrections

**CV-R1: the Hooker-injury locator is p.53, not an inferred p.54.** In the OCR, the p.53
running head "THE BATTLE OF THE THIRD OF MAY." / "53" is at offset 113018. The selected section
runs from 113999 to 114883. A legible p.54 header, "54 CHANCELLORSVILLB AND GETTYSBURG." (an OCR
misspelling), follows at 115251. The locator's basis ("no p.54 header is legible") is therefore
false, and the passage lies on p.53.

- **Fix.** In VA032 `bridges-and-idle-corps` ("37,000 men were kept out of the fight,") and
  `command-roles` ("was manifestly unfit…"), replace the locator with:
  `p.53 (OCR page markers: follows the p.53 running head 'THE BATTLE OF THE THIRD OF MAY.', outside the selected range, and precedes the '54 CHANCELLORSVILLB AND GETTYSBURG.' header; not checked against print)`.
- **Memo.** Replace the bullet with: "Hooker's injury is on p.53: it follows the p.53 running
  head and precedes the legible (OCR-misspelled) p.54 header; the May 3 date comes from that
  running head, outside the selected range."
- **Registry.** In the `inspection` of `doubleday-chancellorsville-selections-v1`, replace
  "(p.54, inferred)" with "(p.53, between the p.53 running head and the p.54 header)". Apply
  this as a contract `metadata_only` revision (new ID, `supersedes` hash), not an in-place edit.

**CV-R2: the losses-table locators rest on a false basis.** The markers "70 CHANCELLORSVILLE"
(offset 148897) and "72 CHANCBLLORSVILLE" (152538) are legible. The section's introductory
sentence lies between the p.70 marker and an unnumbered odd-page running head, "ATTACK ON
SEDGWICK'S FORCE." (150987). The table follows that running head.

- **Fix.** In VA032 `casualty-records`:
  - For "it is said the Confederate statement is far from being accurate.", replace the locator
    with `p.70 (OCR page markers; not checked against print)`.
  - For "Total 12,197", "17,197" and "13,019", replace the locator with
    `p.71 (inferred: follows the unnumbered 'ATTACK ON SEDGWICK'S FORCE.' running head between the legible p.70 and p.72 markers; not checked against print)`.
- **Memo.** Replace the losses bullet with: "The losses table is on an inferred p.71: it follows
  an unnumbered running head between the legible p.70 and p.72 markers."
- **Registry.** In the same `metadata_only` revision, replace "(pp.70–72, page numbers not
  legible)" with "(pp.70–71; p.71 inferred from an unnumbered running head)".

**CV-R3: p.25 is also an inferred locator but is not labelled as one.** "no pre- cautions were
taken…" follows CHAPTER IV, between the p.24 marker (51687) and the p.26 marker (55619). The OCR
has no p.25 marker.

- **Fix.** In VA032 `warning-and-flank`, replace the locator with:
  `p.25 (inferred: chapter IV opening page between the p.24 and p.26 markers; no p.25 header in OCR; not checked against print)`.
- **Memo.** Count three inferred Doubleday locators, not two.

**CV-R4: VA032 `command-roles` overstates or leaves uncited parts of the Doubleday and Lee
judgments.**

- (a) Doubleday himself qualifies the council tally. The value omits that qualification.
- (b) The countermand clause is uncited.
- (c) "Stunned" is not Doubleday's word.
- (d) "Lee credits Jackson" has no citation for the credit itself.

Replace the first two sentences of the value with:

> "Doubleday says Hooker ordered the May 1 withdrawal, refused Couch's request to remain, then
> countermanded too late; that on May 3 Hooker was prostrated and severely injured, was
> manifestly unfit to give orders, though he soon resumed command; and that Hooker ordered the
> recrossing although the majority of council votes were against it, while adding that Meade's
> and Howard's votes were qualified so as to give the impression they favored retreat. Lee says
> the turning movement that decided the day was conducted by Jackson, who was fired upon by his
> own skirmishers, and credits Stuart, who took his command."

Keep the rank sentence unchanged. Add these citations:

- Doubleday `may-1`, p.14: "Hooker soon afterward changed his mind and countermanded his first order, but it was then too late ;"
- Doubleday `may-3-hooker-injured`, with the CV-R1 locator: "was prostrated and severely injured."
- Doubleday `council-and-recrossing`, p.68: "The votes of Meade and Howard, however, were qualified in such a way as to give the impression they were in favor of a retreat."
- Lee `lee-1863-09-21`, p.803: "The movement by which the enemy’s position was turned and the fortune of the day decided was conducted by the lamented Lieutenant- General Jackson,"

Add to the rationale: "Lee's 'fortune of the day decided' and Doubleday's criticisms are
attributed judgments, not causal effects."

**CV-R5: the Howard judgment in VA032 `warning-and-flank` is paraphrased as "apathy", which is
not Doubleday's word.**

- **Fix.** Replace "Doubleday's view of Howard's apathy is his judgment." with "Doubleday's view
  that only Howard's 'utter want of appreciation of the gravity of the situation' prevented a
  strong line of defence is his judgment."
- **Citation to add.** Doubleday `may-2-warning-and-rout`, with the CV-R3 p.25 locator:
  "There was no reason other than Howard's utter want of appreciation of the gravity of the situation"

**CV-R6: VA032 `recorded-result` misreads "lost" as "leaving".**

- **Fix.** Replace "…retired without being followed, leaving 14 guns and 20,000 stand of arms."
  with "…retired without being followed; Hooker left his killed and wounded behind and had lost
  14 guns and 20,000 stand of arms."
- **Citation to add.** Doubleday `council-and-recrossing`, p.68: "Hooker left his killed and wounded behind,"

**CV-R7: the VA032 `casualty-records` attribution and the table's arithmetic.** Doubleday
relays hearsay ("it is said"). He does not himself assert that the Confederate figures are
inaccurate. The OCR table also contains a discrepancy that should stay visible.

- **Fix.** Replace "which he says is from the official reports and inaccurate on the
  Confederate side," with "which he gives as an extract from the official reports, adding that
  'it is said' the Confederate statement is far from accurate,".
- **Add to the rationale:** "In OCR, the Confederate row totals sum to 13,029: Artillery and
  Cavalry show 227 killed and wounded, no missing figure, and a 237 total. The printed total is
  13,019 (10,266 + 2,753). Two Confederate missing entries carry '?' marks. Early's division
  shows 851 killed and wounded, against 974 in Early's own report (VA034). Neither figure is
  reconciled or checked against print."

**CV-R8: VA033 `casualty-records` drops Sedgwick's qualifier and the scope of his captures.**
Sedgwick's captures come "according to the best information we could obtain". Six of the 15
guns were lost again. The captures span all Sixth Corps operations, including Marye's Heights
(VA034).

- **Fix.** Replace the second sentence of the value with: "Sedgwick gives Sixth Corps losses in
  these operations as 4,925, footnoted to a revised statement, and says that, according to the
  best information he could obtain, the corps captured 5 battle-flags, 15 guns (9 brought off)
  and 1,400 prisoners."
- **Citation to add.** Sedgwick p.561: "according to the best information we could obtain, 5 battle-flags, 15 pieces of artil- lery— 9 of which were brought off,"
- **Rationale.** Change "Sedgwick's total also covers…" to "Sedgwick's loss and capture totals
  also cover…".

**CV-R9: VA032 omits a within-family flank conflict.** The frozen description and the live NPS
text both say Jackson marched "against the Federal left flank". Lee and Doubleday, cited in
`warning-and-flank`, say right.

- **Add to the `warning-and-flank` rationale:** "The CWSAC/NPS description says Jackson marched
  against the Federal left flank and calls him Lt. Gen., against the frozen commander row's
  Major General; this conflicts with Lee's and Doubleday's 'right' and is retained, not
  adopted."
- **Citations to add:**
  - `nps-va032-v1`, Description: "Lt. Gen. T.J. Jackson directed his corps on a march against the Federal left flank"
  - `arnold-cwsac-battles` `{battle: VA032}` `description`, with the same quote.

**CV-R10: the memo invents a strength range.** "113,000–114,500 effective" joins two things
into one range: Doubleday's doubt that Hooker had over 113,000 for actual combat, and Forbes's
114,500 total effective (113,000 infantry and artillery plus 1,500 cavalry).

- **Fix.** In the memo, replace "Doubleday gives Hooker about 124,500 of all arms or
  113,000–114,500 effective, and relays 62,000 for Lee." with "Doubleday gives Hooker about
  124,500 of all arms and doubts he had over 113,000 for actual combat; he relays Forbes's
  114,500 total effective and Forbes's 62,000 for Lee, and says Lee's army numbered about 62,000
  by Confederate official reports."
- **Note.** The dossier value already separates these correctly.

## Optional (not required)

- `edition` says "(Campaigns of the Civil War, VI), per catalog and OCR title". The catalog
  `metadata` has no series or volume field. The series comes from the OCR title
  ("CAMPAIGNS OF THE CIVIL WAR"), whose numeral is illegible, and "VI" from the signature
  marks ("VI.— 1"). Correct this only if a `metadata_only` revision is made anyway (CV-R1/R2).
- VA034 `reported-force-scope`: "Barksdale's Mississippians" is linked only through context
  ("the rest of Barksdale’s infantry"). Cite that clause, or name Griffin's 18th and 21st
  Mississippi instead.
- VA034 `casualty-records`: add Early's "the greater part of whom are, in all probability,
  stragglers."
- VA032 `warning-and-flank`: Lee says "Fitzhugh Lee’s cavalry, under General Stuart in person",
  not "Stuart's cavalry".
- VA033 `extended-line`: cite "My line was formed with the left resting on the river".
- VA032 `opening-personnel-unknown`: call the frozen bounds "imported source-reported
  forces-engaged figures" rather than "estimates".

## Unresolved (retain; no further depth required)

- Print pages were not checked. All Doubleday and OR locators rest on OCR page markers.
- The Confederate column of Doubleday's table was not checked against print.
- No original returns, maps, Hooker testimony or corps reports were inspected.
- Engagement-specific casualties for VA033 and VA034 remain unknown.
