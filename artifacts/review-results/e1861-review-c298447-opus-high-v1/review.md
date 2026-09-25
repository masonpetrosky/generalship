# 1861 Eastern first passes: separate review (E1861)

**Outcome: corrections required.** There are 8 required corrections (E1861-R1 to R8) and 15
advisories (E1861-A1 to A15). None of these findings changes a model input. This is an AI review,
a separate analysis. It is not historical adjudication by a person, it is not independent
corroboration, and it does not admit any feature.

## Reviewer, date and inputs

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`, run as a separate
  subagent with fresh context. The author's conversation was not an input.
- **Date:** 2026-09-25.
- **Commits:**
  - prepared `c2984479b0f96581acfcc85fee50cb3b8a221488`;
  - previous `c5bcb389e38b6f79200e347aaa78ddacd9795953`;
  - review bundle `badefa6b3c7d8d914a616217be81551cc931864a`. The worktree was checked out at
    this commit.
- **Assignment:** `assignment.md`, sha256
  `30792d509e87a8e86ef8a21b887622f04721b57e3390bc064eec528c5c3865cf` (verified).
- **Input manifest:** `inputs.json`, sha256
  `ec2cb26dee9215dd0bc107388cc45db8dbd9b1a30857f969bcb1c16e4dd2a87a` (verified).
- **Bound inputs:** I checked all 119 paths against both `git show c2984479:<path>` and the
  worktree. There were **0 mismatches**.
- **One document outside the manifest:** the assignment asks for `docs/cohort-v2.md`, but the
  manifest does not bind it. I read the worktree copy, sha256
  `4dfa84e66e50b4ffe614dacc51ac7ffd89ee5365dd7acaa5431f26983b128b3c7d`. It is unchanged between
  `c298447` and `badefa6`.
- **`make check`:** run offline with Python 3.14.7. The 134 unit tests passed (`OK`),
  `python -m generalship check` completed, and the process exited 0. Afterwards `git status` showed
  no modified files. I ran no build, packet or network command.

## Scope actually inspected

- **Instructions and documents:**
  - `AGENTS.md`;
  - the research-depth section of `docs/methodology.md`;
  - `docs/evidence-contract.md` in full;
  - `docs/cohort-v2.md`;
  - the "Author groups across campaigns" paragraph of `docs/sources.md` and its 1861 addition;
  - all six campaign memos.
- **Dossiers:** all 17 dossiers in full, every claim and citation. For every text citation I read
  the quote inside its surrounding passage. Most whole selection files I read end to end.
  - I read the whole selection file for Anderson, Nicolay Sumter, Nicolay Western Virginia, Gwynn,
    Eagle, Ruggles, Ward, Pierce, Magruder, Morris, Pegram, Rosecrans, Wise, Floyd, Reynolds, Rust,
    H. R. Jackson, Jones, E. Johnson, Patterson, T. J. Jackson, Beauregard, Martin, Stringham, Ord
    and Stuart.
  - For Nicolay's Manassas sections I read `manassas-armies` and `blackburns-ford` in full. For
    `bull-run` and `retreat-and-losses` I read a window of about ±350 characters around each cited
    quote.
  - For McDowell, Stone and Evans I read the cited windows and Evans's October 31 report in full.
- **Frozen records:** I read the Arnold battles, forces and commanders rows for all 17 battles and
  all 17 NPS text snapshots.
- **Source registry:**
  - All 78 new records. I checked title, author, edition, archival identifier, dates by section,
    editorial sections, group, dependency note and inspection note.
  - For every new selection I rebuilt each section from the parent OCR using the recorded
    character ranges and whitespace collapse. All 30 selections reproduced exactly.
  - I checked the catalog JSON for the three Official Records scans, the three Navy volumes and
    Nicolay: identifier, volume, contributor and Trent collection.
  - I searched the full Nicolay OCR for Bethel, Falling Waters, Hatteras, Sewell and Aquia.
  - In the full OR V OCR I checked the Cross-Lanes section. In the full Navy Volume 5 OCR I checked
    Braine's May 22 statement.
- **Outside the assignment:** the diff also adds three metadata-only Carolinas successors
  (`cox-carolinas-selections-v2`, `or47-1-cox-kinston-selections-v2`,
  `or47-1-kilpatrick-carolinas-selections-v2`). I only confirmed that their ranges reproduce and
  that they carry `supersedes`. I did not review them.
- **Not inspected:**
  - the Illinois identifiers `warofrebellion01unit` and `warofrebellion02unit`, which were not
    registered. I cannot confirm the claim that they are Series III and II volumes;
  - print pages;
  - any unregistered report;
  - Webb's *The Peninsula*.
- **No research:** I did no new research and used no model recollection as evidence.

## Checks that passed

- **Counts:** the claim, unknown and citation counts in every memo table match the dossiers: 153
  claims, 17 null unknowns and 803 citations. Every dossier covers all seven dimensions, keeps the
  opening strength as a null `unknown` with no citation, is marked `draft`, and uses exactly three
  families: NPS/Arnold plus two others.
- **Phases:** only `unresolved` and `post_outcome` are used. Nothing is tagged `inherited`, which
  suits dates that are unset and works built during the action.
- **Figures kept apart:** no strength figure is adopted as an opening force. Frozen, live and
  report figures stay as separate observations, and live ranks are recorded but not adopted.
  Aggregate or overlapping figures are explicitly kept out of sums: Pierce's 21 casualties from
  friendly fire, Jones's McLean's Ford loss, Barksdale's action at Edwards Ferry, the July 13 and
  August 29 surrender counts, and Beauregard's July 18 total, which includes Mitchell's Ford.
- **Commander credit:** no listed commander receives automatic credit. The passages show that
  several listed commanders did not direct the fighting:
  - Braine at Sewell's Point;
  - Garnett at Rich Mountain;
  - Beauregard and McDowell at Blackburn's Ford;
  - Martin at the capitulation.

  Each dossier records this.
- **Families:** the grouping is sound. Nicolay is marked as dependent on the Official Records.
  Each container volume is noted as not being a witness. Reprints across the Army and Navy
  compilations are treated as copies. The Beauregard and Stuart groups are noted as one author
  family with the earlier registered groups.

## Required corrections

**E1861-R1: VA001 `recorded-result`. A figure has no quote.** The value says Gwynn has the
Monticello "driven off after an hour and a half", but none of the cited quotes contains the
duration. Add this citation:
`{"source_id": "or2-gwynn-sewells-point-selections-v1", "section": "gwynn-1861-05-20-report", "locator": "p.34 (OCR page markers; not checked against print)", "quote": "The engagement continued lor an hour and a half without intermission on either side,"}`.

**E1861-R2: VA002 `ammunition-and-supplies`. A cumulative figure is scoped too narrowly.** Ward's
"upward of 300 shots and shells, with 1,700 pounds of powder" is his total for "the several
cannonades in which we have been engaged, amounting altogether in the two weeks we are
commissioned to ten hours". It is not a figure for Aquia Creek. The same pass read Braine's May 22
statement in Navy Volume 5, pp.645, but did not select it. That statement records "the steamer
Thomas Freeborn came along and Commander Ward came on board" and fired "some twelve or fourteen
shots" at the Sewell's Point battery, which is VA001. So the total may include another record.

- **Replace the value with:** "Ward says he expended all ammunition suitable for distant firing on
  May 31 and on June 1 went to Washington to repair damages and refill his exhausted magazines. He
  adds a cumulative figure: in all the cannonades 'in which we have been engaged' during the two
  weeks in commission, ten hours in all, they had fired upward of 300 shots and shells with 1,700
  pounds of powder. Ruggles asked for heavy guns, a thousand volunteers and twenty thousand
  musket-rifle caps, and relays that the enemy threw 597 shots and shells on June 1 against 75
  from the battery."
- **Append to the rationale:** "Ward's 300 shots and 1,700 pounds cover every cannonade of his two
  weeks in commission. Braine's May 22 statement (Navy Volume 5, read, not selected) records the
  Thomas Freeborn under Ward firing on the Sewell's Point battery on May 18, so the total may
  include VA001. It is not assigned to this record or added across records."
- **Add this citation:**
  `{"source_id": "orn4-ward-aquia-creek-selections-v1", "section": "ward-1861-06-01", "locator": "p.492 (OCR page markers; not checked against print)", "quote": "after the several cannonades in which we have been engaged, amounting altogether in the two weeks we are commissioned to ten hours,"}`.

**E1861-R3: VA003 `casualty-records`. A figure has no quote.** The value's "then eighteen dead
found" is not in any cited quote. Add this citation:
`{"source_id": "or2-magruder-big-bethel-selections-v1", "section": "magruder-1861-06-12", "locator": "p.92 (OCR page markers; not checked against print)", "quote": "I have now to report that eighteen dead were found on the field,"}`.

**E1861-R4: WV004 `ferry-sickness-trains`. Misattribution.** The words "Troops sickly." come
straight after "General reports give Lee and Loring 10,000 men at Huntersville." The telegram
does not say they describe Rosecrans's own troops.

- **Replace the second sentence of the value with:** "Rosecrans relays that the Seventh Ohio's
  baggage trains were saved; his telegram's words 'Troops sickly' follow a report of Lee's and
  Loring's 10,000 men at Huntersville and do not say whose troops are meant."
- **Replace the quote** `"Troops sickly."` (same section and locator) with
  `"General reports give Lee and Loring 10,000 men at Huntersville. Troops sickly."`.

**E1861-R5: WV004 `reported-force-scope` and `reports-and-surprise`. An estimate's population is
misstated.** In the second August 28 telegram, "Enemy estimated at from 5,000 to 10,000" follows
"Has orders in full to hold his position at Gauley. Thinks he can do it." The first telegram gives
Floyd five regiments and three guns and "AVise, with about the same force, on New River". The
estimate may therefore cover Floyd and Wise together. The dossier presents it as the size of the
force that attacked at Cross-Lanes.

- **`reported-force-scope`: replace the value with:** "The frozen force field reads Brigades; the
  live field reads zero. Rosecrans's first August 28 telegram relays Cox's report that Tyler's
  Seventh Ohio, an advanced regiment, was surprised by Floyd, and places Floyd with five regiments
  and three guns at Cross-Lanes and Wise 'with about the same force' on New River. His second
  telegram, after relaying Cox's intention to hold Gauley, gives the enemy as estimated at 5,000
  to 10,000 without saying whether that covers Floyd alone or Floyd and Wise. Wise gives Floyd's
  command as 2,600 men, less the sick and furloughed, and calls Tyler's regiment the enemy's
  advance guard."
- **`reported-force-scope`: append to the rationale:** "The 5,000-10,000 estimate has an unstated
  population and is not assigned to the attacking force."
- **`reported-force-scope`: add this citation:**
  `{"source_id": "or5-rosecrans-kanawha-selections-v1", "section": "rosecrans-1861-08-28", "locator": "p.118 (OCR page markers; not checked against print)", "quote": "AVise, with about the same force, on New River."}`.
- **`reports-and-surprise`:** the claim does not cite the estimate. Delete ", with the enemy
  estimated at 5,000 to 10,000" from the value's first sentence.

**E1861-R6: WV002 `reported-force-scope`. Dates are conflated.** The value joins two dispatches
into one sentence. It gives the July 4 telegram (15,000–18,000 foot, 22 guns, 650 horse) and
then, as an apposition, the July 3 phrase "claimed in all to be thirty thousand; in reality,
thirteen thousand". That hides the fact that Patterson's own estimates differ from one day to the
next.

- **Replace the last sentence of the value with:** "Patterson's July 3 dispatch says the force
  scattered the day before was 3,500 strong and that, reinforced by Bee at a point seven miles
  off, it was 'claimed in all to be thirty thousand ; in reality, thirteen thousand'; his July 4
  telegram puts Johnston seven miles in advance with 15,000 to 18,000 foot, 22 guns and 650
  horse."
- **Append to the rationale:** "Patterson's July 3 and July 4 estimates of the force ahead of him
  differ and are not reconciled."

**E1861-R7: NC001 `casualty-records`. The rationale makes an unsupported statement about imported
data.** "Prisoners taken at the capitulation are counted in the frozen and live Confederate
totals" is not established for the frozen 770. Replace that sentence with: "The live Confederate
670 equals the compilers' count of Stringham's prisoner list, so it appears to be a prisoner
count; the basis of the frozen 770 is not established. Prisoners are not added to any other loss
figure."

**E1861-R8: `docs/sources.md`, 1861 section. The denominator is wrong.** The list gives 17 NPS
pairs (34), Nicolay metadata and OCR plus selections (2 + 3), OR I/II/V (6), Navies 4–6 (6) and
"thirty report selections". That adds up to 81, not 78. There are 27 report selections; the other
three selections are Nicolay's. Replace "- thirty report selections." with "- twenty-seven report
selections (thirty selections in all, with Nicolay's three)." The commit message uses the same
wording, but commits are immutable and it is noted here only.

## Advisories (optional; no correction required)

- **A1 (SC001 `fort-and-batteries`).** "brick work on an artificial island" is not quoted. Add
  `"built of brick upon an artificial island"`, section `sumter`, p.62.
- **A2 (SC001).** The Nicolay chapter holds information not captured: Anderson's offer to
  evacuate by noon on April 15 and the 3:20 a.m. one-hour notice. In the logistics claim it could
  also note that 50 barrels were taken from the magazine and "all but five" were rolled into the
  sea, next to Anderson's "four barrels and three cartridges".
- **A3 (VA001).** Braine's statement, read but not selected, places Commander Ward and the Thomas
  Freeborn at the May 18 firing, with "some twelve or fourteen shots". Ward is a listed VA002
  commander. An open-questions note would keep this visible. Do not infer that Gwynn's "steam-tug"
  is the Freeborn.
- **A4 (VA002).** The two sides disagree on timing and this is not recorded:
  - June 1: Ruggles gives 9 a.m. to 4 p.m.; Ward gives 11:30 a.m. to 4:30 p.m.
  - May 31: Ward reports about two hours and then "nearly an hour"; Ruggles gives 10 a.m. to
    1 p.m.

  Mapping the queried "May 30 [?]" section to a null date is right. The value's "on the 29th" is
  independently supported by Ward's "the day before yesterday".
- **A5 (VA003).** Two phrases are inferences with no quote: "fired on in the dark" in the
  information claim, and "two fresh regiments" in the result claim.
- **A6 (WV003).**
  - The surrender count differs between two claims. Nicolay gives 560 men and 33 officers;
    Pegram gives 359 + 166 = 525 men and 22 + 8 = 30 officers. Worth noting the difference in the
    rationale.
  - "Nicolay quotes Rosecrans … 135 burials" is Nicolay's paraphrase ("He also places"), not a
    quotation.
  - "the Union numbers quickly decided the contest" has no quote.
- **A7 (WV004 `floyd-and-cox`).** "his forces" is ambiguous. Suggested wording: "and Wise believed
  the Union advance guard was sent to draw Wise's own forces to Carnifix".
- **A8 (WV005 `prisoners-and-spies`).** Rust writes to Loring, "they were aware of your
  movements". Suggested wording: "knew of the movements of Loring's column (Rust's addressee)".
  The value currently says "Lee's".
- **A9 (VA004).** For the "three against five" dispute over Longstreet's regiments: Nicolay also
  says "three regiments of Longstreet's brigade, which bore the first assault". The rationale
  could say so.
- **A10 (VA005).**
  - Nicolay's 32,073 includes Kirby Smith's, Fisher's and Hill's troops, who arrived between noon
    and 4 p.m. It is a population across the whole day, not a single moment.
  - McDowell's "admitted 1,800" is followed by "much under the true number".
  - Nicolay's Union 481/1,011 repeats McDowell's return. Agreement between the two is dependence,
    not corroboration.
- **A11 (NC001).** Martin writes that "The report of Commodore Barron and Major Andrews of the
  action of the 29th contains all that is material". That report was read but not selected, so
  the Confederate side of the capitulation rests on the articles. An open-question note would
  help. Choosing Martin's report, copied from a newspaper clipping, is acceptable because the
  dependency note flags it.
- **A12 (registry, Beauregard).** The dependency note for
  `or2-beauregard-blackburns-ford-selections-v1` names `or-beauregard` but leaves out
  `beauregard-drewrys-bluff-report`. Not reusing `or-beauregard` is sound: that Shiloh group also
  holds Jordan, Bragg and returns material. A new per-campaign group is allowed under the
  cross-campaign author-group policy in `docs/sources.md`. Fix the omission only if a
  metadata-only revision is made for another reason. The Stuart note is complete.
- **A13 (registry, dates).**
  - Mapping these sections to null is conservative and allowed:
    - Nicolay's `title-and-preface` (the preface is signed February 26, 1881);
    - McDowell's "August 4" report, which has no year in the OCR;
    - Beauregard's "August —, 1861", with the day blank;
    - Stringham's two-date section.
  - The McDowell and Nicolay-preface dates could be filled if a print check confirms them.
  - The T. J. Jackson note's "in this worktree" is odd phrasing.
- **A14 (WV001).** Morris's Confederate "fifteen to forty" killed is relayed from Dumont's reports.
- **A15 (WV006, WV007, WV008).** Duration differences are not recorded:
  - WV006: Rosecrans says three hours; Floyd says nearly four.
  - WV007: Reynolds says four hours under fire; Jackson says 4½ hours, from 7 to 2:30.
  - WV008: Jones says about three hours; Johnson says 7:15 to 1:45.

## Answers to the assignment's source questions

- **University of California scans for OR I and II.** Sound. The catalog JSON gives
  `warofrebellion01secrrich` and `warofrebellion02secrrich` (volumes 01/02, University of
  California, `ucb:GLAD-218883`), and the OCR title pages read Series I, Volumes I and II. The
  records document that the scan's catalog date is not used as the volume imprint. I did not
  verify the Illinois alternatives.
- **Navies Volumes 4–6.** Sound as report sources. They are a separate compilation from the Army
  Official Records, the Trent collection is confirmed in the catalog, and reprints are marked as
  copies.
- **Hatteras without Army OR IV.** Acceptable for a first pass. It leaves the listed Union
  commander, Butler, without an account of his own, and the dossier and memo record this. See also
  A11.
- **Big Bethel and Hoke's Run.** Nicolay's coverage is confirmed. Bethel appears only in the
  passing "repulse at Great Bethel" and in McDowell's quoted remark. Falling Waters appears in a
  single clause. One report family per side is therefore the right substitute.
- **WV004.** OR V's Cross-Lanes section holds only Rosecrans's two telegrams, which is confirmed.
  Relying on a relayed telegram and on Wise's retrospective, polemical report is the only option
  within the ceiling, and both limits are recorded. The relayed estimate needs E1861-R5.
- **Beauregard and Stuart groups.** Sound. See A12.
- **Undated sections mapped to null.** Sound under the contract. See A13.
- **Martin's newspaper-clipping report.** Acceptable, with provenance flagged. See A11.

## Unresolved items handed back to the primary

The primary should check each required correction against the cited passages before editing.
No historical dispute recorded in these dossiers is resolved by this review.
