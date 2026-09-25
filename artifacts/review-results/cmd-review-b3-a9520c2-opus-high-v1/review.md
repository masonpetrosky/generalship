# Command-responsibility ledger: separate review, batch 3 of 4

## Reviewer record

| Field | Value |
| --- | --- |
| Reviewer | Separate Claude subagent, fresh context (not a fork of the author's conversation) |
| Model / effort | `claude-opus-5-5` / `high` |
| Date | 2026-09-25 |
| Prepared commit reviewed | `a9520c2d5628c25b49437f4f54bfc78268a85393` |
| Previous commit | `16a32116067912a1b5cb380097d75092a2a430b4` |
| Bundle commit (worktree HEAD) | `7c986eff354f6fb6311808f7be3245b69ec687fd` |
| `assignment.md` sha256 | `54cf2a53041dbbfd58644bf591892eef40935cda19c9b2e1f03e9ae4619b40e0` (verified) |
| `inputs.json` sha256 | `11f34d78cb94fd48165b789ec37c0e0ff8ad82f6acee3d1d7e90581f9b5e3a62` (verified) |
| Design bound by the ledger | `docs/commander-ratings.md` sha256 `0ab4b7d541baf4f8e642634f316628f9cb372d68dcdbbc047a305f5a1fb704bb` (matches the ledger binding and is unchanged between the prepared commit and the bundle commit) |

**Input hashes.** All 24 paths in `inputs.json` were hashed from
`git show a9520c2…:<path>` and from the worktree. All 24 match at both, with no mismatch. Among
them are the ledger (`7735d8f7…`), the registry (`0466adc0…`), the memo (`d305ccc4…`) and
`generalship/command.py` (`2dde93fc…`). The bundle commit changes only the three review-bundle
directories after the prepared commit.

**Checks run offline.** `make check` ran 126 tests, OK, exit 0. `python3 -m generalship
command-check` covered 91 engagements and 182 sides: grades A/B/C/D are 149/15/15/3, the registry
has 128 commanders, nesting is nested 2 / not_nested 6 / unresolved 1, and `rated: false`. No
build, packet, evaluation or network command was run. No primary artifact was modified. This file
is the only file written.

## Scope actually inspected

- **Coverage.** All 23 assigned engagements, both sides (46 sides): TN012, TN013, NC010, TN014,
  TN015, TN016, MS004, MS005, AL001, VA032, MS006, VA033, VA034, MS007, MS008, MS009, MS010,
  MS011, LA011, VA107, TN017, PA002, AR008. For each side I inspected:
  - the ledger entry (choice, rule, grade, labels, candidates, successor, superior, echelon,
    citations, rationale);
  - the registry entries it references;
  - the frozen CWSAC description, commander listing and `forces_text`;
  - the bound dossier's responsibility claim, plus other claims where they bear on command
    (orders, warnings, force scope).
- **Source text read in full or in the relevant sections.** All of these are dossier-cited
  registered sources:
  - Foster and D. H. Hill (Tidewater);
  - Cist and Jordan (Middle Tennessee and Streight's Raid);
  - Greene (Vicksburg 1863: Grand Gulf, Port Gibson, Raymond, Jackson, Big Black, Siege,
    Helena sections);
  - Bowen, Hébert/Forney, Sherman (Snyder's Mill), Pemberton (Big Black section), Dennis and
    McCulloch (OR XXIV);
  - Lee, Sedgwick and Early (Chancellorsville; OR XXV) and Doubleday (Chancellorsville);
  - Lee's Gettysburg report, and Doubleday (Gettysburg), searched only for command statements;
  - Cist (Tullahoma) and Bate (Hoover's Gap).
- **Nesting.** All seven contained-interval pairs involving assigned engagements: MS005⊃MS004,
  MS005⊃MS006, MS011⊃AR008, MS011⊃LA011, VA032⊃VA033, VA032⊃VA034 and VA033⊃VA034.
- **Not inspected:**
  - engagements outside this batch;
  - NPS HTML snapshots and the full-volume OCR files (`or22-1-full.txt`, `or24-1-full.txt`,
    `or24-2-full.txt`, `doubleday-full.txt`);
  - the Holmes and Johnston selections beyond the dossier quotes;
  - NPS `.txt` snapshots other than through the frozen description text they share.

  No new research was done.
- **Quote checks.** Every replacement quote below was resolved through
  `generalship.command.resolve` against the named dossier citation (claim ID and citation
  index), or against the frozen CSV cell. Each occurs in its passage.

## Summary

**Outcome: corrections required.** Seven sides need changes: R1–R7. The other 39 sides are
sound under the design's rules, subject to the advisories.

- **Choices confirmed.** No choice of commander needs to change. The listed commander, or at
  TN017 CS the passage-named officer, stands on every side. The rule order (5, 3, 2, 6, then 4)
  is applied correctly:
  - rule 3(a) at VA032 CS and MS008 CS;
  - rule 2 everywhere else;
  - no rule 5 side in this batch. MS004 and MS005 each have one listing per side.
- **What the corrections fix.**
  - Grades at first combat: R1, R5, R6, R7.
  - Labels the passages call for, by the ledger's own practice elsewhere (for example
    NC006/TN009/TN026 US and MS007 CS for superiors who ordered the operation): R2, R3, R4, R7.
  - Missed stating passages: R6, R7.
- **Citations.** Every cited quote occurs in its source, and I found no misread quote. Several
  quotes are weaker than passages available in the same sections (advisory A7).
- **Registry.** No merge or passage-only entry in the batch is unsound. R2 and R3 each need one
  new passage-only entry.
- **Nesting.** All seven outcomes are acceptable. See A9 on the MS011/LA011 reason.

## Required corrections

The field values below use the ledger's schema. A "dossier ref" means
`{"dossier": {"claim_id": …, "citation_index": …}, "source_id": …, "quote": …, "battle_id": …}`.
The checker resolves it to the whole section of that dossier citation. Where a correction cites a
source not yet in `bindings.cited_sources`, that source's binding (`metadata_sha256`,
`raw_sha256` from `data/sources.json`) must be added:

- `or25-1-sedgwick-chancellorsville-selections-v1` (R4);
- `or24-2-mcculloch-selections-v2` (R6);
- `cist-tullahoma-selections-v1` (R7).

### R1: NC010 US: grade A is not supported at first combat

**Evidence.**

- The frozen interval is 1863-03-13 to 03-15, and the frozen description includes "an initial
  success at Deep Gully on March 13".
- The side's first combat was on the 13th, on the Trent road and at Deep Gully:
  - Foster: "on the evening of the 13th the enemy appeared in force on the Trent road, driving
    in our picket posts on that road".
  - Hill: "On Friday we drove them to their first line of works at Deep Gully, 8 miles from New
    Berne." and "It was defended by five companies and two pieces of artillery."
- The cited Foster passages put Anderson in command of the work north of the Neuse attacked "At
  daylight of the 14th". No inspected passage states that Anderson commanded the side's engaged
  forces when the fighting began.
- No passage names another officer commanding them either. Foster directs the whole defence
  ("ordered to fall back to my defenses where 1 proposed making the j fight"), which is
  `superior_directing` and is already recorded.
- The grade table therefore gives B: rule 2, the single listing, no stating passage and no
  contradiction. The listing choice (Anderson) stands.

**Change (NC010, US):**

- `grade`: `"B"`.
- `citations`: only the `arnold-cwsac-commanders` rank citation (`"Lieutenant Colonel"`). The
  checker requires grade B to cite only the listing.
- `superior_citations` (keep `labels: ["superior_directing"]` and
  `superior: "us-john-g-foster"`), each a dossier ref to `command-roles` index 6,
  `or18-foster-tidewater-selections-v1`:
  - "I instructed him to defend and hold the work."
  - "although they | were ordered to fall back to my defenses where 1 proposed making the j
    fight."
- `echelon`: keep `detachment_or_post`. The rationale should name its basis: Foster, same
  section, "a small work on north side of the Neuse Eiver, occupied by the Ninety second New
  York Volunteers, ; Lieutenant-Colonel Anderson."
- `rationale`: "Single CWSAC listing. The side's first combat was on March 13 on the Trent road
  and at Deep Gully (Foster; Hill), where no inspected passage names the Union commander. Foster
  puts Anderson in command of the work attacked at daylight on the 14th, and says he instructed
  him to hold it (superior_directing: Foster). No passage states Anderson's command at first
  combat or names another officer (rule 2, grade B)."

### R2: TN013 US: missing `superior_directing` (Gilbert)

**Evidence.** Cist (TN013 `warning-and-order-to-advance`, index 1, section
`thompsons-station`):

- "On March 4th, Gilbert at Franklin ordered Colonel Coburn" to lead the expedition;
- when Coburn reported a superior force and suggested falling back, "Gilbert, however, ordered
  him to advance."

This is a superior in the theater directing the operation. It is the design's MS001 pattern and
the ledger's NC006/TN009 pattern. The dossier itself notes "Gilbert's order to advance came from
outside the listed commanders."

**Change (TN013, US):**

- `labels`: `["superior_directing"]`.
- `superior`: `"us-gilbert"`.
- `superior_citations`: two dossier refs to `warning-and-order-to-advance` index 1,
  `cist-middle-tennessee-selections-v1`, quotes "On March 4th, Gilbert at Franklin ordered
  Colonel Coburn" and "Gilbert, however, ordered him to advance."
- Append to `rationale`: "Cist says Gilbert at Franklin ordered the expedition and, when Coburn
  suggested falling back, ordered him to advance (superior_directing: Gilbert)."

Grade stays A.

**Registry:** add `{"id": "us-gilbert", "name": "Gilbert", "side": "US", "cwsac_names": [],
"passage_citation": {"dossier": {"claim_id": "warning-and-order-to-advance", "citation_index": 1},
"source_id": "cist-middle-tennessee-selections-v1", "quote": "Gilbert, however, ordered him to
advance.", "battle_id": "TN013"}}`.

### R3: VA032 US: missing `command_changed` (Hooker → Couch)

**Evidence.** Doubleday (VA032 `command-roles`, index 4; same section as index 3) says that on
May 3 Hooker "was prostrated and severely injured", "it was some time before he turned over the
com- mand to Couch, who was second in rank", and "although he soon resumed the command."

Rule 4 names wounding as a command change within the interval, to be labelled with the
successor. The ledger has no label. The turnover was temporary, and the rationale should say so.
Whether §6 view (ii) should credit a temporary successor is a design question outside this
review, but the label keeps it visible.

**Change (VA032, US):**

- `labels`: `["command_changed"]`.
- `successor`: `"us-couch"`.
- Add to `citations` two dossier refs to `command-roles` index 4,
  `doubleday-chancellorsville-selections-v2`:
  - "it was some time before he turned over the com- mand to Couch, who was second in rank."
  - "although he soon resumed the command."
- `rationale`: "A cited passage states the command. Doubleday says that after Hooker was
  injured on May 3 he turned over the command to Couch, second in rank, and soon resumed it
  (rule 4; temporary)."

Grade stays A. VA032 is a primary row.

**Registry:** add `{"id": "us-couch", "name": "Couch", "side": "US", "cwsac_names": [],
"passage_citation": {"dossier": {"claim_id": "command-roles", "citation_index": 4}, "source_id":
"doubleday-chancellorsville-selections-v2", "quote": "it was some time before he turned over the
com- mand to Couch, who was second in rank.", "battle_id": "VA032"}}`.

### R4: VA034 US: missing `superior_directing` (Hooker)

**Evidence.** Sedgwick (VA034 `orders`, index 0, section `sedgwick-1863-05-15`) received "an
order, dated 10.10 p. m., directing me to cross the Rappahannock at Fredericksburg immediately
upon receipt of the order, and move in the direction of Chancellorsville until I connected with
the major-general commanding ; to attack and destroy any force on the road". The same section
identifies the army as "the forces under General Hooker". Hooker, in the theater, ordered the
crossing and the attack that make up this record.

This differs from VA033. There Hooker's dispatch says "he was too far away to direct my
operations", so no label is warranted (see A10).

**Change (VA034, US):**

- `labels`: `["superior_directing"]`.
- `superior`: `"us-joseph-hooker"`.
- `superior_citations`: dossier refs to `orders` index 0,
  `or25-1-sedgwick-chancellorsville-selections-v1`, with quotes "directing me to cross the
  Rappahannock at Fredericksburg immediately upon receipt of the order, and move in the
  direction of Chancellorsville until I connected with the major-general commanding ; to attack
  and destroy any force on the road" and "leaving him free to proceed against the forces under
  General Hooker."
- Append to `rationale`: "Sedgwick says the commanding general ordered him to cross at
  Fredericksburg and attack and destroy any force on the road (superior_directing: Hooker)."
- Bind the Sedgwick source.

Grade stays A.

### R5: MS010 CS: Greene disputes that anyone was in command

**Evidence.** Greene (MS010 `command-roles`, index 3, section `big-black`): "On the Confederate
side everything was at odds and ends. There seemed to be no one in command,". Pemberton says
Bowen "received his instructions from my own lips" and the description has Pemberton ordering
Bowen to man the works. The sources therefore disagree about who commanded, and Greene names no
other officer.

This is the TN006 US pattern ("With no one in command"), which the ledger grades C with
`responsibility_unresolved` and the listing kept. The grade table puts "inspected sources
disagree about who commanded" in C. Greene's "seemed" is hedged, and the rationale should say
so.

**Change (MS010, Confederate):**

- `grade`: `"C"`.
- `labels`: `["superior_directing", "responsibility_unresolved"]`.
- Add to `citations` a dossier ref to `command-roles` index 3,
  `greene-vicksburg-1863-selections-v1`, quote "On the Confederate side everything was at odds
  and ends. There seemed to be no one in command,".
- `rationale`: "Pemberton ordered Bowen, with three brigades, to man the fortifications
  (superior_directing: Pemberton). Greene says there seemed to be no one in command. He names no
  other officer, so the listing stands, but the sources disagree (rule 2, grade C)."

Choice (Bowen), superior and echelon are unchanged.

### R6: LA011 CS: stating passages were missed; the grade should be A

**Evidence.** The rationale says "no inspected passage states or contradicts the command". The
dossier-cited reports state it at first combat:

- McCulloch (LA011 `command-roles`, index 2, section `mcculloch-1863-06-08`): "According to
  orders, on the night of the 6th my brigade took up the line of march for Milliken’s Bend, to
  attack the Yankee force at that place." and, at 2.30 a.m. on the 7th, "when the enemy’s
  pickets fired upon my cavalry scouts and skirmishers."
- Dennis (index 0): "The enemy consisted of one brigade, numbering about 2,500, in com- mand of
  Genera] [H. E.] McCulloch, and 200 cavalry."
- Nothing contradicts them.

**Change (LA011, Confederate):**

- `grade`: `"A"`.
- `echelon`: `"brigade"`.
- `citations`: the listing rank, plus a dossier ref to `command-roles` index 2,
  `or24-2-mcculloch-selections-v2`, with quotes "According to orders, on the night of the 6th my
  brigade took up the line of march for Milliken’s Bend, to attack the Yankee force at that
  place." and "when the enemy’s pickets fired upon my cavalry scouts and skirmishers."
- Optionally add a dossier ref to index 0, `or24-2-dennis-selections-v2`, with the Dennis quote
  above.
- `rationale`: "McCulloch reports that his brigade marched to attack Milliken's Bend and that
  the enemy's pickets fired on his scouts at 2.30 a.m. on the 7th. Dennis puts the attacking
  brigade in McCulloch's command (rule 2)."
- Bind `or24-2-mcculloch-selections-v2`, and the Dennis source if cited.

The quotes use the source's curly apostrophes.

### R7: TN017 US: stating passages were missed; the grade should be A, and `superior_directing` (Rosecrans) is missing

**Evidence.** The rationale says "no inspected passage states or contradicts Thomas's command".

- The frozen description: "Maj. Gen. George H. Thomas's men, on the 24th, forced Hoover's
  Gap."
- Cist, same section as TN017 `command-roles` index 0:
  - Rosecrans's written order: "\"The Fourteenth Corps, Major-General Thomas, to advance on the
    Manchester pike, seize and hold with its advance, if practicable, Hoover's Gap,"
  - "On the 24th, General Thomas moved direct on the Manches- ter pike from Murfreesboro,
    Beynolds's division in advance,"

The same section shows Rosecrans directing the operation from the field: "The plan then of
Eosecrans in the advance on Tullahoma,"; the corps commanders each "received in writing his
orders as to his part in the movement."; and his headquarters reached Manchester on the 27th.
The description agrees: "he feigned an attack on Shelbyville but massed against Bragg's right.
His troops struck out toward the gaps".

**Change (TN017, US):**

- `grade`: `"A"`.
- `echelon`: `"corps_or_wing"`.
- `citations`:
  - the listing rank;
  - `arnold-cwsac-battles` description, quote "Maj. Gen. George H. Thomas's men, on the 24th,
    forced Hoover's Gap.";
  - dossier refs to `command-roles` index 0, `cist-tullahoma-selections-v1`, quotes "\"The
    Fourteenth Corps, Major-General Thomas, to advance on the Manchester pike, seize and hold
    with its advance, if practicable, Hoover's Gap," and "On the 24th, General Thomas moved
    direct on the Manches- ter pike from Murfreesboro, Beynolds's division in advance,".
- `labels`: `["superior_directing"]`.
- `superior`: `"us-william-s-rosecrans"`.
- `superior_citations`:
  - `arnold-cwsac-battles` description, "he feigned an attack on Shelbyville but massed against
    Bragg's right. His troops struck out toward the gaps";
  - a dossier ref to `command-roles` index 0, `cist-tullahoma-selections-v1`, "each one
    received in writing his orders as to his part in the movement."
- `rationale`: "The description has Thomas's men forcing Hoover's Gap on the 24th. Cist gives
  Rosecrans's written order for the Fourteenth Corps, under Thomas, to seize the gap, and says
  Thomas moved on the Manchester pike with Reynolds's division in advance (rule 2;
  superior_directing: Rosecrans)."
- Bind `cist-tullahoma-selections-v1`.

**Consequences for the memo.** If R1–R7 are applied:

| Measure | Before | After |
| --- | --- | --- |
| Grades A/B/C/D | 149/15/15/3 | 149/14/16/3 |
| `superior_directing` sides | 15 | 18 |
| `command_changed` sides | 11 | 12 |
| `responsibility_unresolved` sides | 11 | 12 |
| Registry commanders | 128 | 130 (passage-only entries 9 → 11) |
| `unknown` echelons | 76 | 74 |

The memo's counts and its passage-only list would need updating.

## Advisories (not required)

- **A1: VA034 CS, consistency with VA107 CS.** The ledger's own citation says "Gen. Robert E.
  Lee left Maj. Gen. Jubal A. Early's division to hold Fredericksburg". Early says he "received
  instructions from Lieutenant- General Jackson to remain behind with my division and one of
  McLaws’ brigades (Barksdale’s), to observe the enemy". VA107 CS labels Lee `superior_directing`
  for ordering Ewell to clear the Valley. Leaving a holding force is weaker than ordering an
  attack, so this is a judgment call, but the two sides should be treated consistently or the
  distinction stated.
- **A2: LA011 US.**
  - **Label.** Dennis, the district commander, writes "in accordance with instructions received
    from me, Colonel Lieb … made a reconnaissance" and "I immediately started the Twenty-third
    Iowa Volunteer Infantry to their assistance,". By NC010 practice that could be
    `superior_directing` (a passage-only "Elias S. Dennis" entry would be needed).
  - **Timing.** The grade-A quote ("Col. Hermann Lieb with the African Brigade") dates to the
    June 6 reconnaissance, outside the interval. "The 23rd Iowa Infantry and two gunboats came
    to his assistance" is closer support for June 7 and should be cited.
  - **Echelon.** Dennis calls Lieb "commanding the Ninth Louisiana, African descent" and says he
    "formed his regiment", against the description's "African Brigade". The rationale should
    note that `brigade` is disputed, or set `unknown`.
- **A3: MS008 US (grade B).** Greene, section `jackson`: "in pursuance of Grant's orders of the
  night of May 12th, already referred to, McPherson had moved from Raymond to Clinton on the
  13th, and from there toward Jackson on the 14th." With the description's "Grant who had been
  travelling with Sherman's corps", this arguably states Grant's direction of the engaged
  corps. That would support A, or at least a corrected rationale. For MS008 CS, Greene's
  "He instructed them to make enough of a defence to gain time" is a stronger stating passage
  for Johnston.
- **A4: MS005.**
  - **US.** Sherman's letter (`or24-1-sherman-snyders-mill-selections-v1`, section
    `sherman-1863-05-01`) gives the heading "commanding Fifteenth Army Corps." and says "I
    disembarked the command at Blake’s negro quarters, and made disposition as for attack,". The
    frozen force reads "XV Army Corps, Department of the Tennessee [US]". These are better
    grade-A evidence than "Sherman had received orders…" and support `corps_or_wing`. Breese's
    gunboats were navy, not "parts of" Sherman's force; only the army commander is listed, so
    rule 2 still applies, but the rationale should say so.
  - **CS.** Hébert's own report (section `hebert-1863-05-04`) refers to "all the oflicers and
    soldiers of my command." and says "The major-general command- ing district, while present,"
    saw the troops. Forney's presence on the field should be recorded as context. B is
    defensible, but the rationale's "does not state the command" overlooks Hébert's own text.
- **A5: TN017 CS.** Two points should stay visible in the rationale:
  - **Earlier first combat.** Before Bate's detachment, the side's first combat within the
    interval was Butler's 3rd Kentucky Cavalry picket being driven from the gap. The frozen
    description says "under Col. J.R. Butler, held Hoover's Gap". Bate says "while on picket
    they had been scattered and driven from be- yond tioover’s Gap".
  - **Rule 2, second bullet.** Bate's detachment was sent on Stewart's order ("a courier
    arrived from Major- General Stewart, directing me to send one regiment and a battery"), and
    Bate reported his dispositions to Stewart at Fairfield. The second bullet (a subordinate
    leading the force is not a contradiction) could therefore keep Stewart.

  The ledger's grade C with `responsibility_unresolved` and Stewart as candidate and successor
  keeps the dispute visible. I do not require a change.
- **A6: PA002 US.** Lee's report says "Major-General Reynolds, who was in com- mand, was
  killed." and puts "the remainder of that army, under General Meade" as approaching. Record
  this as subordinate context in the rationale, as MS006 does for McClernand. It does not
  contradict Meade's command authority.
- **A7: Stronger quotes available** in the same dossier sections:
  - MS004 CS: Bowen, "have been bombarding my batter- ies terrifically since 7 a. rn.".
  - MS006 CS: Bowen, "the battle of Port Gibson, fought by a portion of my command on May 1".
    Greene says Bowen reached the field before 9 a.m., after the first fighting; this is
    compatible with command authority.
  - AR008 US: Greene, "The entire force num- bered 4,129 men, and was commanded by Maj.-Gen. B.
    Prentiss.". This also supports `detachment_or_post`, since it is the Helena garrison.
  - NC010 CS: Hill's report is headed "commanding Expedition".
  - TN016 US: the description's "he believed it, and sent away most of his cavalry" is
    stronger than "Granger decided to attack Van Dorn".
- **A8: Echelons left `unknown` that frozen fields support.**
  - MS004 CS: `forces_text` "Bowen's Division and attached troops [CS]" supports `division`.
  - MS005 US: "XV Army Corps" supports `corps_or_wing`.
- **A9: MS011/LA011 `not_nested`.** The outcome is right, but the reason should rest on the
  Confederate side and the place. McCulloch's Brigade was not part of the "Army of Vicksburg",
  and the fight was on the west bank. The inspected passages do not exclude the Union African
  Brigade and 23rd Iowa from MS011's US force scope, which is "Army of the Tennessee".
- **A10: VA033.**
  - **US.** Cite Sedgwick's "he was too far away to direct my operations." as the reason no
    `superior_directing` is recorded.
  - **CS.** Lee's report shows that McLaws, "with his three brigades and one of General
    Anderson's, was ordered to re-enforce General Wilcox" on May 3 and that Lee sent Anderson
    on the 4th. Lee directed from Chancellorsville. The choice stands, but record Wilcox and
    McLaws as subordinate context.
- **A11: NC010 CS `superior_directing` (Longstreet).** The NPS passage shows the department
  commander directing Hill to advance. That fits the ledger's practice, but the design excludes
  departmental superiors "not directing this operation in the field". State why Longstreet
  qualifies (Hill's report is addressed to him) or drop the label.

## Sides with no findings

The following sides are sound as recorded. I checked choice, rule, grade, labels, echelon and
quote support.

- TN012 both sides;
- TN013 CS;
- TN014 both sides;
- TN015 both sides;
- TN016 CS;
- AL001 both sides;
- MS007 both sides;
- MS009 both sides (the rationale already addresses Grant's 10 a.m. arrival);
- MS010 US;
- MS011 both sides;
- VA107 both sides;
- PA002 CS;
- AR008 CS;
- VA032 CS (rule 3(a), with Jackson as candidate; Jackson's wounding is a corps change, not the
  side's).

The following sides are sound apart from the advisories above: TN016 US, MS004 both sides,
MS005 both sides, MS006 both sides, MS008 both sides, VA033 both sides, VA034 CS, LA011 US,
TN017 CS, PA002 US, AR008 US and NC010 CS.

## Limits

This is a separate AI analysis within the scope stated above. It is not human historical
adjudication, it is not evidence of source independence, and it does not admit any feature or
authorize any fit. Retrospective histories (Cist, Greene, Doubleday, Jordan and Pryor) and the
commanders' own reports are interested or derivative accounts, and agreement between them within
one family is not corroboration. The corrections above make the ledger consistent with the
design and with its own practice. They do not settle who historically deserves credit.

**Finding IDs:** R1, R2, R3, R4, R5, R6, R7 (required); A1–A11 (advisory).
