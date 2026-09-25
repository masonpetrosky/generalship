# Strength ledger v2, batch 1 of 8: separate review

**Outcome: corrections required.** There are two required findings (R1, R2) and eleven
advisories (A1–A11).

This is an AI review. It is a separate analysis of the recorded inputs against the accepted
rules. It is not historical adjudication, independent corroboration, feature admission or
authorization of any fit.

## Reviewer and inputs

| Item | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`, fresh-context subagent |
| Date | 2026-09-25 |
| Assignment | `artifacts/review-results/v2est-b1-11d4bc3-opus-high-v1/assignment.md`, sha256 `c4dd654c8b84d13382f20b0be724d579a93b93f7c0c0ee80040dfdaae73995d7` (matches) |
| Input manifest | `inputs.json`, sha256 `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0` (matches) |
| Prepared commit | `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372` (previous `96110cf`) |
| Worktree HEAD | `eddd8313723e0bf2ea9ff5be80a577dc43484588` (bundle commit) |

**Input hashes.** I checked all 25 hashes in `inputs.json` against
`git show 11d4bc3:<path>` and against the worktree. Every one matches. `git diff 11d4bc3 HEAD`
touches only review-bundle files and nothing under `docs/`, `generalship/` or `data/`.

**Other files the assignment names.** These are not in the manifest. I hashed them in the
worktree, which is identical to `11d4bc3` for these paths:

| File | sha256 |
| --- | --- |
| `docs/strength-estimates.md` | `795212ad…164ba3` (= ledger binding) |
| `docs/feature-admission-reported-strength.md` | `0699152d…4c48` |
| `docs/ledgers-v2.md` (addendum) | `a7e05ddf…eb1` (= ledger binding) |
| `data/estimates/owner-decision-v2-sources-2026-09-25.json` | `28da7610…89e9` (= binding) |
| `docs/research/strength-estimates-ledger-v1.md` | `9d9f7d30…0b1926` |
| `generalship/estimates.py` | `af540a92…2a3f` (= binding) |
| `generalship/estimates_v2.py` | `368c5052…c5c` (= binding) |
| `livermore-transcription-v2.txt` | `688ea736…f103f` (= registry) |
| `livermore-p77.jpg` | `90cdc51f…0dee` (= registry) |
| `livermore-p78.jpg` (v1 directory) | `d0b6a7c8…57f5` (= registry) |

The assignment calls the addendum `docs/ledgers-v2.md`, while the manifest binds
`docs/research/ledgers-v2.md` (the extraction record). I read both.

**Checks run offline.**

- `make check`: 143 tests OK, exit 0.
- `python3 -m generalship estimate-check --ledger data/estimates/side-strength-v2.json`:
  exit 0. It reports 305 in scope and 79 out; grades A/B/C/D 184/60/114/252; fit-eligible
  rows 61/83/130; 20 rows excluded as post-start.
- I ran no build or packet commands and modified no files other than this review.

## Scope actually inspected

I inspected all 28 assigned engagements, both sides each: SC001, WV001, WV003, WV004,
WV006, WV005, VA003, MO001, MO002, MO004, MO005, MO006, MO003, MO007, MO008, WV002, VA004,
VA005, NC001, KY001, KY002, KY003, FL001, VA006, VA007, MO009, MO010 and MO011. None of them
is in cohort v1, so all are new v2 entries.

- **Inputs.** I read all 204 inputs: codes, basis, `loss_timing`, `bound`, `reproduction_of`,
  notes and class. I also read every estimate, `null_reason`, inventory entry and nested-set
  entry.
- **Dossier passages.** I opened all 249 citations of the batch dossiers' strength claims.
  For every figure that sets or bounds an estimate, I read the surrounding section text
  resolved from the registered raw source (`citation_text`). The batch dossiers have no typed
  quantities.
- **CWSAC rows.** I read the frozen CWSAC forces rows, including `description`,
  `strength_min` and `strength_max`, for all 28 engagements.
- **Livermore.** Only VA005 (p77) and MO004 (p78-supplement) have matching entries. I read
  both `livermore-transcription-v2` sections and compared their figures with the page images
  `livermore-p77.jpg` and `livermore-p78.jpg`. Every transcribed figure matches the print.
  - For inventory completeness only, I searched the pinned Livermore OCR for the other 26
    battle names and found no entry. The OCR is not cited.
- **Rule replay.** I replayed the two proposed corrections in memory with the unchanged
  engine (`estimate_side`, `estimate_row` and `nested_sets`). No file was written.
- **Not inspected.** I did not look at the other 277 engagements, the command ledger or
  sources outside the batch dossiers. I did not re-derive the design rules.

The checker already verifies quote containment, printed values in quotes, bindings and
mechanical reproduction. I did not repeat those checks by hand; this review covers what the
checker cannot verify.

## Required corrections

### R1. WV003 Rich Mountain, US: `us-pegram-3000-hart` basis

- **Change:** set `basis` from `unknown` to `reported_engaged`. Leave the codes as
  `["adversary_or_hearsay_estimate"]`.
- **Evidence:** Pegram's report (citation 7, `pegram-1861-07-14`) says Rosecrans "attacked
  the small handful of troops under Captain De Lagnel with three thousand men." His addendum
  (citation 9, `pegram-1861-07-15`, the same registered source and `document_key`) refers back
  to that figure: "their force engaged at Hart's, as before mentioned, three thousand."
  - The author himself identifies the citation 7 figure as the force engaged at Hart's. The
    basis is therefore read from the source, not inferred from role (tier-2 §3 item 3).
  - As coded, one figure appears as two candidates on different bases. The unknown-basis copy
    then raises `high` on an unknown `point_basis`.
- **Effect** (engine replay):
  - The two inputs form one rule 2 group: same document, same value, same basis.
  - US `high` changes from 3000 to 2470. `range_groups` becomes `["us-nicolay-1900"]`.
  - The labels gain `single_input`, giving `applicability_unresolved`, `basis_mixed`,
    `single_input` and `whole_engagement_leakage`.
  - Grade C, point 1900 and low 1330 are unchanged, and so is the set membership (`set3_ABC`).
- **Equivalent alternative:** drop `us-pegram-3000-hart` as a restatement. Its inventory
  entry would then read "citation 7: restated in citation 9 as the force engaged at Hart's;
  entered once as us-pegram-3000-engaged". The estimate is the same.

### R2. MO004 Wilson's Creek, US: Livermore note 1's Frémont figure should be an input

**Where the figure is.** Livermore p.78 note 1 (`livermore-transcription-v2`, section
`p78-supplement`; confirmed on the page image) says: "General Fremont's dispatch of August 13,
placing the force at 8000, assumed the presence of 2000 Home Guards, when in fact they
numbered only 200 (3 W. R., 54, 65)."

**Why the recorded reason fails.** The inventory gives "(Livermore rejects it)" as the reason
for not entering it. That is not a non-use ground under design §3:

- **Role.** It is the Union department commander's figure for Lyon's force, relayed by a
  compiler. Under extractor policy 3 it keeps the own-report role.
- **Engagement match.** It is tied to this engagement ("placing the force at").
- **State time.** It is not post-engagement: the later dispatch date alone does not trigger
  that code (tier-2 §3 item 2).
- **Other codes.** It is not unreadable, another engagement or a post-outcome claim.
- **Consistency with this batch.** Disputed relayed figures elsewhere in the batch are
  entered and classed, not dropped: VA006 `cs-reports-10000`, which Stone calls "highly
  exaggerated", and WV003 `us-pegram-10000`.

**Change:** add this input to `sides.US.inputs`:

- `id` `us-lv-fremont-8000`
- `source_id` `livermore-transcription-v2`
- `ref` `{"citation": {"source_id": "livermore-transcription-v2", "section": "p78-supplement", "locator": "p.78 (page image livermore-p78-image-v1)", "quote": "General Fremont's dispatch of August 13, placing the force at 8000"}}`
  (the quote occurs in the section)
- `printed` `{"lower": 8000, "upper": 8000}`
- `basis` `unknown`
- `codes` `[]`
- `loss_timing` `none`
- `adjustments` `[]`
- `bound` `null`
- `document_key` and `independence_group`: as on `us-lv`
- `note`: "Livermore note 1: Frémont's August 13 dispatch placing the force at 8000; Livermore says it assumed 2000 Home Guards present when there were only 200"
- `class` `B`

In `inventory.livermore`, add `us-lv-fremont-8000` to `inputs`. Remove the Frémont clause from
the "Not entered" part of `reason`, and note that the entry is Livermore's rejected
own-side figure.

**Effect** (engine replay):

- US `high` changes from 7480 to 9200 (8000 × 23/20).
- `point_groups` becomes `["us-lv", "us-lv-fremont-8000"]`. The lower median is still 5400.
- Grade B, point 5400, low 4200 (Snead's 4,200 lower bound), labels and set membership
  (`set2_AB`, `set3_ABC`) are unchanged. The Confederate side is unchanged.
- **Alternative coding.** If the primary instead judges that Livermore's rejection leaves the
  role unsettled, the codes could be `["source_role_unresolved"]` (class C). That gives the
  same point, range and labels.

## Advisories (no change required under the current rules)

- **A1. KY003 Confederate: an unlinked CWSAC figure.**
  - `cs-cw` (1,010, table basis engaged) equals Williams's present-basis `cs-williams-1010`:
    "My whole force consisted of 1,010 men, including sick, teamsters, and men on extra duty."
  - The dossier's own rationale says the CWSAC 1,010 "matches Williams's November 13
    whole-force figure, not the men engaged". The ledger does not link them.
  - Practice on such links is uneven. TN022 `us-cw` is linked to a report "inferred from equal
    values"; VA003 explicitly declines to link.
  - If KY003 were linked, the group basis would become `unknown`. The Confederate side would
    then be grade B, 1010 (860–1160), and the row would stay in `set3_ABC` only.
  - Recommendation: the primary should fix one criterion for linking CWSAC rows to equal
    report figures.
- **A2. VA005 Confederate: the NPS cell 3,230 is kept out without a code.**
  - The live NPS cell reads 3,230. It is recorded as a "display error" and not entered. That
    is a non-use reason outside the §3 row 1 codes.
  - Entering it as class A, engaged, would leave the point at 32,230 but move `low` to 3,070.
  - I agree it is a copy discrepancy within one compiled-table lineage: the frozen CWSAC row
    reads 32,230, and the page total, 31,680 = 28,450 + 3,230, carries the dropped digit. The
    reason should say so explicitly.
- **A3. MO006 and NC001: inventory reasons use `post_outcome_claim` for surrender and prisoner
  counts** (Price's "about 3,500 prisoners"; Stringham and NPS "670").
  - The cited claim is not tagged `post_outcome` (tier-2 §3 item 6). Under design §3 row 3
    these figures would be class C, `post_start_information`.
  - There is no effect: both sides are grade A, and post-start candidates enter the hull only
    when they set the point.
  - The v1 ledger uses the same wording, so this is a naming convention, not an error.
- **A4. Inconsistent reading of "all told".**
  - SC001 `us-nicolay-128` ("a garrison of 128 souls all told") is coded `reported_present`.
  - VA003 `cs-magruder-all-told` ("Our force, all told") is coded `unknown`.
  - If SC001's figure were `unknown`, the US range would widen from 80–80 to 80–130 and lose
    `single_input`.
  - I read "souls all told" together with citation 2's workmen as a headcount, so `present` is
    defensible. The two entries should nonetheless follow one convention.
- **A5. SC001 Confederate `cs-nicolay` scope.** The figure reads "a volunteer force of from
  four to six thousand supported the rebel batteries". Nicolay presents it against Anderson's
  whole garrison, so whole-side scope is a plausible reading. Coding it `scope_unresolved`
  would only add `applicability_unresolved`; the range would not change.
- **A6. MO007 Confederate `cs-thompson-2000`: state time.**
  - The figure comes from an October 23 letter: "while I was 60 miles north of there, with a
    victorious army of 2,000 men". It ties the figure to the army that fought, so class B is
    acceptable.
  - The state time is not stated. Coding it `engagement_link_unknown` would make the side
    grade C, and the row would leave `set2_AB`.
- **A7. MO010: Britton repeats Prentiss's figures.** Britton's 470 and 900 equal Prentiss's
  and are not linked. This follows v1's handling of unlinked restatements. Linking would add
  `single_input` to the Confederate side only.
- **A8. VA005: CWSAC figures are Livermore's rounded to tens.** CWSAC's 28,450 and 32,230 are
  Livermore's 28,452 and 32,232 rounded to tens. Rule 2 groups only equal printed values, so
  they stay separate. There is no effect on points, ranges or labels (`compiled_dependence` is
  already set).
- **A9. MO005 Confederate `cs-lane-6000`.** Lane's September 4 letter gives the enemy's
  strength when he wrote, after the September 2 start. `post_engagement_state` could be added.
  The class stays C (opponent) and the input does not enter the range, so there is no effect.
- **A10. KY003 US `us-williams-sum`: the coverage is supported, but the note could cite it.**
  Williams's November 9 report (in the section of citation 3) says "On yesterday Captain
  Holliday, with a small command, met this column from John's Creek. A skirmish took place."
  That places the John's Creek column in action within the interval. Adding this to the
  sum's note would document its coverage.
- **A11. Engine consequences, reported and not errors.**
  - **WV004 Confederate.** The point is 5,630, from Cox's 5,000–10,000. Wise's component list
    for Floyd, "2,600 men, less the number sick", is an engagement-link-unknown upper bound
    and is not applied.
  - **WV002 Confederate.** The point is 2,630 under rule 4. Against it, Jackson reports "Only
    one regiment and one piece of artillery ... brought into action", and Harper's regiment
    had 380 men.
  - **VA004.** Both sides take whole-army NPS cells (35,000 and 22,000) for Tyler's
    reconnaissance, correctly graded C with `applicability_unresolved`.
  - **VA006 Confederate.** `high` of 10,000 is set by a figure the relaying author calls
    "highly exaggerated".
  - **VA007 Confederate.** `bound_conflict` is correctly raised: Stuart's 1,600 infantry on
    December 23 is above his 1,200 figure for the whole force on December 21.
  - **MO007 US.** The point of 3,000 is the midpoint of the description's printed
    "approx. 2,500-3,500". The table's `strength_max` reads 2,500, and the inventory records
    this.

## Grade D sides

I confirmed seven grade D sides: WV001 US and Confederate, WV004 US, WV005 US, WV002 US,
NC001 US and MO009 Confederate.

- Each recorded reason is accurate against the cited passages.
- The NC001 US exclusion is supported. The NPS description says "while the navy bombarded
  Forts Clark and Hatteras, Union troops came ashore", and Martin surrendered "to the
  combined naval and army forces". The CWSAC row covers the two regiments only.
- No usable figure was missed in the inspected dossier citations, frozen rows or Livermore
  pages.

## Other checks with no finding

All other inputs are correctly coded for:

- role, including prisoner and citizen hearsay, relayed own figures and secondary histories;
- partial scope and partial interval, including NC001's reinforcements, MO009 Pillow's
  first-engaged regiments, and the FL001 and MO002 components;
- one-sided bounds and their direction, including caps on parts recorded with `bound: null`;
- engagement link, including MO001 Snead's 2,000, the MO004 Springfield army and MO006
  Britton's pre-siege figures;
- post-start state (KY003's "We have now ... 1,100");
- the three completed sums: MO002 Snead's line plus mounted men, MO004 Snead's two columns and
  MO008 Britton's two detachments. Each is disjoint, covers the side and shares one state
  time; the MO002 sum's `scope_unresolved` is supported by the excluded 2,000 unarmed men;
- the Livermore p77 and p78 lines and their bases.

Every inventory item is accounted for, with the exceptions in R2 and A2.

## Finding IDs

- **Required:** R1, R2.
- **Advisory:** A1–A11.
