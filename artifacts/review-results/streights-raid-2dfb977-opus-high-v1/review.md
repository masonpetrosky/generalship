# Separate review: Streight's Raid in Alabama and Georgia (AL001, Day's Gap)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`) subagent, reasoning effort `high`; fresh context. This is an AI review, not human historical adjudication, independent corroboration or feature admission.
- **Date:** 2026-09-25
- **Prepared commit:** `2dfb977b75537c2598429b9399e15287949d78d1`; previous `4db650fb881ed1c2fd7199504c87e556a3d153ac`; assignment bundle `b5f7fec5439f566c8eeeef16ce5d2202f73dbbaa`
- **Assignment** sha256 `2dda65050bce70a4d46cd9b412502d2f0e84974a66dcd727ddc866ac2f523b2c`; **inputs.json** sha256 `64bc70b731c2b1dbc10c1de8a04cd9eba48437e5a9d9ae449a89b8ed9222822c`
- **Outcome:** **corrections required** (SR-R1 to SR-R3, all narrow wording and scope fixes). Advisory notes SR-A1 to SR-A5 are optional.

## Input verification

All 30 paths in inputs.json matched their bound SHA-256 values, both in the worktree and in `git show 2dfb977:<path>`. There were no mismatches. `b5f7fec` differs from `2dfb977` only in the assignment and inputs.json. The worktree was still clean after `make check`.

## Scope actually inspected

- **Dossier:** all of `data/evidence/AL001.json`. It has 9 claims and 41 citation occurrences (0+6+5+5+3+3+8+5+6); 1 claim is a null unknown (`opening-personnel-unknown`, with no citation). All seven dimensions are covered. I also checked the boundary note, the open questions and the phase and status tags.
- **Every citation, checked mechanically:** each of the 36 text quotes occurs exactly once in its declared section. The 5 CSV citations resolve to exactly one row and cell (battles `forces_text`/`results_text`/`casualties_text`; commanders `rank` for Streight and for Forrest). I also checked every page locator against the OCR page markers.
  - **Cist:** p.145 begins at `IN MURFREESBORO. 145`; p.146 at `VII.— 7 146`; p.147 at `IN MURFREESBORO. 147`.
  - **Jordan and Pryor:** p.249 follows `248`; p.250 at `250 Campaigns`; p.256 follows `256`; then `257`, `258` and `259`; p.260 follows `26o Campaigns of General Forres L`.
  - Every locator is correct.
- **Entailment:** I read every claim value and rationale against its cited passages and the surrounding section text.
- **Frozen rows:**
  - The `cwsac_battles`, `cwsac_forces` and `cwsac_commanders` row sets for AL001 have 1, 2 and 2 rows. The force rows carry casualties of 65 (Confederate) and 23 (US) and no counts.
  - In `artifacts/battles.json`, AL001 has null bounds and `missing_numeric_strength`.
- **Derivatives replayed:**
  - `nps-al001.txt` is regenerated exactly from the HTML using the recorded HTMLParser transform.
  - All Cist sections (2) and Jordan sections (4) reproduce exactly. Each was made by slicing the pinned parent at the recorded half-open character ranges and collapsing whitespace.
  - Both parents (`cist-cumberland-ocr-v1`, `jordan-pryor-forrest-ocr-v1`) are hash-verified and unchanged between `4db650f` and `2dfb977`.
  - I viewed the parent text just before and after each range. The duplicated, cropped p.261 lies in the gap between `days-gap` (end 592896) and `evening-pursuit` (start 595509), so it is excluded as the author states.
- **Registry:** 433 records / 430 paths; previous 429 / 426. The first 429 entries are byte-identical to `4db650f`. The four new records' metadata was read.
- **Coverage and artifacts:**
  - 91/127 dossiers and 36 without. 23 of 36 campaign groups are complete by dossier presence.
  - Only `AL001.json` was added under `data/evidence`. The 90 older dossiers and 52 history files are unchanged.
  - `data/pilot`, `data/admission` (both proposals), `admission-check.json`, `baseline.json` and `battles.json` are unchanged since `4db650f`.
  - `promoted_rows` is 0, with 40 candidates (18 blocked, 22 excluded).
  - The baseline has 23 battles in 13 campaigns. Brier is 0.2768816348133779 versus 0.25 for equal odds.
- **Next group:** I independently computed the earliest incomplete group as **Gettysburg Campaign [June-July 1863]**. Its ten records are VA035, VA107, VA036, VA037, VA038, PA001, PA002, MD004, MD006 and VA108. They are sorted by (start date, ID) and match the memo, roadmap and report.
- **Packet and receipt:**
  - `artifacts/research/AL001.md` has 3 JSON blocks. They equal, in order, the AL001 battles record, the dossier and the full `data/sources.json`.
  - All 157 input hashes, 433 source hashes and 7 output hashes in `receipt.json` match.
- **`make check`:** run offline, exit 0; 82 tests OK; `artifacts_written: false`.
- **Docs:** I read the diffs of the memo, README, roadmap, methodology, sources.md, pilot report, queue, quality and cli.py text.
- **Not inspected:** whole books, print scans, maps, Official Records reports and any source outside the bundle. I did no network access.

## Confirmed without correction

- **Scope:** the boundary note and memo say that the extent of the frozen record within April 30 is not established. They add neither Crooked Creek, Hog Mountain, the later engagements nor the May 3 surrender. The NPS description supports this.
- **Live force field:** "2000 total (US 2000; CS 0;)". The Confederate zero is correctly not treated as measured absence.
- **Cist's 1,466** is correctly treated as a May 3 surrender count and is not adopted.
- **Casualties:**
  - The frozen and live fields both read 88 (US 23; CS 65).
  - Cist gives seventy-five killed and wounded for Forrest and twenty-one for Streight. Jordan and Pryor give "at least seventy-five" for the Federal loss in this phase. The two histories really do assign "seventy-five" to opposite sides.
  - The `disputed` status and the refusal to reconcile the figures are correct.
- **Ranks:** the frozen rows give Colonel Streight and Brigadier General Forrest. The live headings give Brigadier General Abel Streight [US] and Major General Nathan Forrest [CS]. The dossier reports this conflict accurately and adopts neither.
- **Commander credit:** judgments are attributed to named histories, and no commander gets automatic or additive credit.
- **Jordan and Pryor** are correctly described as not independent of Forrest. His prefatory note says, "For the greater part of the statements of the narrative I am responsible."
- **Cist** is correctly described as an interested Union staff history.
- **OCR artifacts** such as "cap- ture", "hun- dred", "seventy- five", "onset ;" and "26o" are reported as they appear, not silently corrected.
- **Phase tags:** `unresolved` and `post_outcome` are plausible hypotheses given unset boundaries.
- **Invented values:** there are no morale scores, probabilities or causal effects.

## Required corrections

### SR-R1: `reported-force-scope` (strength). Population of the 350 and date scopes of 2,200 and "four-fifths"

**Problem.** The dossier says "Roddy's regiment numbered three hundred and fifty". The memo says Jordan and Pryor "give Roddy's regiment as 350". Neither is what the source says.

- Jordan and Pryor place "Roddy's Regiment and Julian's Battalion, mounted" together, with orders to advance (p.258).
- They then say "Roddy's men ... gave way ... leaving forty out of three hun- dred and fifty" (p.258).
- They then say "Roddy having dismounted his own regi- ment and Julian s Battalion" (p.259).

So the 350 is a count given as the denominator of the charge's losses, and its formation is unspecified. It is not stated to be the regiment's strength.

Two further figures lack their date scope:

- The 2,200 is an estimate of Streight's command "already at Tuscumbia", ascertained before Forrest reached Brown's Ferry on April 27 (p.250).
- Cist's "four-fifths" describes the command after gathering animals "En route to Fort Henry", before Eastport (p.145), not the state at Day's Gap.

**Replacement `value`:**
"The frozen force field names men from four infantry regiments and the 1st Middle Tennessee Cavalry, and three Confederate regiments, without counts; the live field reads 2000 total (US 2000; CS 0;). Jordan and Pryor say that by the time Forrest reached Brown's Ferry on the evening of April 27, his scouts had ascertained that Streight's command, already at Tuscumbia, was estimated at 2,200 cavalry or mounted infantry. In their Day's Gap narrative, Roddy's men, when repulsed, left forty out of three hundred and fifty killed or wounded; the passage does not say whether the 350 is Roddy's Regiment alone or includes Julian's Battalion, which was posted and later dismounted with it. Cist says that after gathering animals en route to Fort Henry, before the raid left Eastport, only four-fifths of Streight's men were mounted, and they poorly, and that the whole force surrendered on May 3 was 1,466."

**Replacement `rationale`:**
"A pre-contact estimate made while Streight was at Tuscumbia, a charge denominator of unspecified formation scope, an early-April mount fraction and a May 3 surrender count differ in population and date; none is adopted as matched opening strength. The live Confederate zero is not measured absence."

**Add citations.** Each quote occurs exactly once in its section.

- `jordan-streights-raid-selections-v1`, section `orders-and-estimates`, p.250: "already at Tuscumbia, were estimated,"
- `jordan-streights-raid-selections-v1`, section `days-gap`, p.258: "Roddy's Regiment and Julian's Battalion, mounted, were posted to the rightward of Edmondson,"
- `cist-streights-raid-selections-v1`, section `streights-raid`, p.145: "En route to Fort Henry his command secured as many animals as they could,"

**Memo bullet replacement:**
"**Opening strength remains unknown.** The live field reads 2,000 Union and zero Confederate. Jordan and Pryor relay a scouts' estimate of 2,200 for Streight's command while it was at Tuscumbia, and say Roddy's men left forty of 350 killed or wounded without stating whether the 350 includes Julian's Battalion. Cist gives 1,466 surrendered on May 3. None is adopted."

### SR-R2: `casualty-records` (outcome). Attribution precision

**Problem.**

- "Roddy left forty of 350" should read "Roddy's men", the source's wording, and the scope caveat from SR-R1 applies.
- "a Federal field hospital" is not in the source. The source says "in a field-hospital were found about seventy-five of their killed and wounded, with some thirty Confederates" (p.260). In context, "their" refers to the retiring Federals, but the hospital's side is not stated.

**Replacement `value`:**
"The frozen and live casualty texts read 88 total (US 23; CS 65). Cist gives Forrest's loss as seventy-five killed and wounded and Streight's as twenty-one, before separately describing a renewed attack that afternoon. Jordan and Pryor say Roddy's men left forty out of three hundred and fifty killed or wounded (formation scope unstated), that the Federal loss in that phase was at least seventy-five, and that a field hospital held about seventy-five of the Federals' killed and wounded, with some thirty Confederates."

Citations are unchanged. The Cist qualifier rests on "On the same afternoon the enemy attacked again," in section `streights-raid`, p.146, which may optionally be added as a citation.

### SR-R3: `command-roles` and `surprise-in-camp`. Two paraphrases that alter the source's meaning

**Problem 1: `command-roles`.** "Forrest disposed his men at a glance" merges two clauses. The source says he "com- prehended the situation at a glance, and forthwith disposed his men for the onset" (p.258).

**Replacement `value`:**
"Jordan and Pryor say Forrest comprehended the situation at a glance and forthwith disposed his men, that Roddy's comparatively raw men gave way, and that Streight's charge forced Edmondson back and left the Confederate guns abandoned to the Federals, and they judge that Streight handled his men with decided nerve; Cist says Streight's charge drove the enemy at all points, capturing their two pieces of artillery. The frozen ranks are Colonel Streight and Brigadier General Forrest; the live heading ranks Streight Brigadier General and Forrest Major General."

**Optional added citation:** `jordan-streights-raid-selections-v1`, section `days-gap`, p.259: "which were abandoned to the enemy."

**Problem 2: `surprise-in-camp`.** "apparently their first knowledge of Forrest's approach" broadens the source. The source's "this fact" is that the Confederates "got within four hundred yards of the ground before the enemy were aware of their proximity" (p.257). That is, the Federals' first intimation of the Confederates' **proximity**, not of any pursuit.

**Replace the first sentence of `value` with:**
"Jordan and Pryor say the advance guard found the Federals a mile ahead cooking, that the Confederates got within four hundred yards before the Federals were aware of their proximity, and that the Confederate artillery's discharge was apparently the first intimation of it."

**Optional added citation:** section `days-gap`, p.257: "got within four hundred yards of the ground before the enemy were aware of their proximity."

## Advisory notes (no correction required)

- **SR-A1.** The new Cist record's `dependency_note` was copied verbatim: "across five records". The `cist-cumberland-1882` group now has six records. This affects no claim. If it is fixed, use a `metadata_only` revision as the contract requires, rather than editing the pinned record in place.
- **SR-A2.** The live NPS description itself uses "Union Col. Abel D. Streight" and "Confederate Brig. Gen. Nathan Bedford Forrest". Those ranks match the frozen rows, so only the live *headings* conflict. The dossier's wording, "live heading", is accurate. The memo could add this for clarity.
- **SR-A3.** Cist describes a renewed engagement on "the same afternoon ... lasting from three o'clock until dark" (p.146). Jordan and Pryor say the Federals had gone about an hour before three p.m., and describe the evening fight near Long Creek at about 5 p.m. (pp.259–260). These timings bear on the unresolved question of how much of April 30 the frozen record covers. They should be kept as an open question, not reconciled.
- **SR-A4.** The terrain phrase "lying concealed behind its crest" combines two passages. The optional added quote "the men of which were lying down concealed." (`days-gap`, p.258) would support the "concealed" half.
- **SR-A5.** While checking the selection boundary, I saw that the OCR of Jordan's Chapter IX synopsis, just before `orders-and-estimates`, reads "Surrender ^ 1 365 Federals". That is a figure different from Cist's 1,466. It lies outside the selections and the surrender is outside scope, so I report it only as an unverified OCR lead. It is not evidence, and there is no correction.

## Limits

I did no historical adjudication beyond the bundled passages. Automated checks establish only byte identity and that each passage exists; the entailment judgments above are this reviewer's reading. Agreement between NPS and CWSAC is one family. Cist is a Union staff history, and Jordan and Pryor wrote with Forrest's endorsement, so neither is neutral. Nothing here admits features or changes model inputs.
