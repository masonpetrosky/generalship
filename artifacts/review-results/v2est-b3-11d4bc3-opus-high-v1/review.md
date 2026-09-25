# Strength ledger v2, batch 3 of 8: separate review

**Outcome: corrections required (V2E3-R1, V2E3-R2).** There are also six advisories, V2E3-A1 to V2E3-A6.

This is an AI review: a separate analysis, not human historical adjudication, independent
corroboration or feature admission. It authorizes no fit.

## Record

| Field | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`, fresh-context subagent; the harness did not give the reviewer a task ID |
| Date | 2026-09-25 |
| Prepared commit reviewed | `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372` (against `96110cf`) |
| Bundle commit / worktree HEAD | `8f1e11cb5b622ee785156a20bc914bbfce66dd7f`; `git diff 11d4bc3 HEAD -- data generalship docs` is empty |
| Assignment | `assignment.md` sha256 `7daeecccb83828ecbba3117e6cdb9106e59397d0c9901da31737f2aa711fa235` (matches) |
| Input manifest | `inputs.json` sha256 `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0` (matches) |
| Input hashes | All 25 bound paths match both `git show 11d4bc3:<path>` and the worktree. No mismatch. |
| Ledger | `data/estimates/side-strength-v2.json` sha256 `e594047072a99c84e5239658df444f2946c945916d744de2ca6a82c8082629e8` |

**Other files read but not bound by `inputs.json`.** The assignment calls the addendum
`docs/ledgers-v2.md`, but `inputs.json` binds `docs/research/ledgers-v2.md`, which is the
extraction record. I read both. The unbound files, with their sha256 values:

- `docs/ledgers-v2.md`: `a7e05ddf…aa49eb1`
- `docs/strength-estimates.md`: `795212ad…6ba3`
- `docs/feature-admission-reported-strength.md`: `0699152d…4c48`
- `data/estimates/owner-decision-v2-sources-2026-09-25.json`: `28da7610…89e9`
- `docs/research/strength-estimates-ledger-v1.md`: `9d9f7d30…1926`
- `generalship/estimates.py`: `af540a92…a32f`
- `generalship/estimates_v2.py`: `368c5052…943a`
- `data/raw/strength-v2/livermore-transcription-v2.txt`: `688ea736…103f`, equal to the ledger's cited-source binding

The ledger's bindings for the 28 dossiers were verified by `estimate-check`.

**Checks run offline:**

- `make check`: exit 0. It ran 143 tests, all OK, and the v2 ledger checkers passed.
- `python3 -m generalship estimate-check --ledger data/estimates/side-strength-v2.json`:
  - 305 engagements in scope and 79 out of scope;
  - side grades A/B/C/D: 184/60/114/252;
  - fit-eligible rows: 61 in set1_A, 83 in set2_AB and 130 in set3_ABC;
  - 20 rows excluded as `post_start_information`.

Nothing was built, and no packet or network command was run. No primary artifact was
modified. The only file written is this review.

## Scope actually inspected

All 28 assigned engagements, both sides of each:

- TX003, MO018, MO019, GA002;
- SC004, SC005, SC007, SC009;
- LA006, LA007, LA008, MO020, AR007;
- LA009, LA010, LA012, LA013, LA015, LA016;
- OK006, OK007, AR009, KS001, TX006;
- AR010, AR011, KS002, FL004.

For each engagement I checked:

- **Inputs and inventory.** Every input and every inventory line in the ledger.
- **Dossier claims.** Every citation in every `strength` claim of the bound dossier. None of these dossiers has typed quantities.
- **CWSAC rows.** Both frozen forces rows (`strength_min`, `strength_max` and the description).
- **Passages in context.** For each cited dossier passage I read the surrounding text of the registered section, usually ±500–1,600 characters. I read in full:
  - Marmaduke's report of February 1, 1863;
  - the opening of Davis's Galveston report;
  - the text around every other quoted figure.
- **Livermore.** I checked which transcription sections have an entry heading that matches any of the 28 engagements. Only p101 (Port Hudson assaults of May 27 and June 14) and p104 (Fort Wagner assault of July 18) do. I read both sections and compared them with the page images `livermore-p101.jpg` and `livermore-p104.jpg` in `data/raw/strength-v2/`. I also checked `livermore-p105.jpg` in `data/raw/reported-strength-v1/`, which carries only the Wagner Confederate loss line. The transcribed figures agree with the images.
- **Replays.** I replayed the proposed corrections in memory with the unchanged engine functions (`estimate_side`, `estimate_row`, `nested_sets`, `classify`). No file was written.

The 91 carried-forward v1 entries are out of scope. I looked at two of them (MS011 and TN024)
only to see how the reviewed v1 ledger codes Livermore's single-assault entries inside a
siege record. The engine's own logic was not re-reviewed.

## Required corrections

### V2E3-R1: SC005 Confederate `cs-wagner-1200` covers only July 11

The frozen record SC005 runs from 1863-07-10 to 1863-07-11. Jones (`jones-charleston-1863-selections-v1`,
section `morris-island-july-10-11`, p.216–217) introduces the 1,200 as the garrison at the
dawn assault of the 11th:

> "The assault of Battery Wagner, which the troops were too much exhausted to attempt on the
> 10th, was made about day dawn the next morning by General Strong. The garrison of Wagner at
> that time consisted of the shattered remainder of the troops which had contested the landing
> the previous morning, … in all about five hundred men, Colonel Olmstead commanding. The
> aggregate force was about twelve hundred men."

So the passage limits the figure to one day, the July 11 assault. It also counts the survivors of this record's
July 10 fighting. Tier-2 §3 item 2 makes a figure limited to one day or phase
`partial_interval`, and design §3 tests row 5 before row 3.

The ledger's own coding points the same way:

- The same batch codes Jones's parallel Wagner-garrison figure for the July 18 assault
  (SC007 `cs-jones-1700`) as `partial_interval`.
- The reviewed v1 ledger codes Livermore's Vicksburg assault entries (MS011 `cs-lv-assault`)
  as `partial_interval` plus `post_engagement_state`.

**Changes (SC005, Confederate):**

- **Input `cs-wagner-1200`:**
  - `codes`: `["partial_interval", "post_engagement_state"]`;
  - `bound`: `"lower"`;
  - `class`: `"bound"`;
  - `loss_timing`: `"not_prior"`. The value is "the shattered remainder of the troops which had contested the landing the previous morning", so it rests on survivors of this engagement. This field does not change the class.
- **`estimate`:** grade `D`, with point, low, high, `exact` and `point_basis` all null. `method` is `grade_D_no_candidate`, `labels` is `["whole_engagement_leakage"]`, and `point_groups` and `range_groups` are empty.
- **`null_reason`:** "Only parts and one-day figures: the 927 on Morris Island on July 10 (before the Georgian reinforcement), the about 700 that met the landing, and Jones's about 1,200 in Wagner at the July 11 assault (survivors of July 10 plus the Georgians). All are recorded as lower bounds."
- **`nested`:** `{"sets": [], "excluded_post_start_information": false}`.
- **`rationale`:** "No whole-side figure for either side. Union: Strong's brigade and a scope-unresolved island total, as bounds. Confederate: the July 10 Morris Island figure, the landing force and the July 11 Wagner garrison, each a part or a single day, as bounds."

**Effect (replayed):** the Confederate side goes from C 1,200 to D. The row was already
incomplete, because the US side is D. The row is no longer counted as a `post_start_information` exclusion.

### V2E3-R2: LA010 Livermore assault entries cover single days of the siege record

The frozen record LA010 (Port Hudson) runs from 1863-05-21 to 1863-07-09. Livermore p.101
(`livermore-transcription-v2`, section `p101`, which matches page image p101) prints two separate
entries: "ASSAULT ON PORT HUDSON, MAY 27, 1863" and "ASSAULT ON PORT HUDSON, JUNE 14, 1863".
The ledger's own Livermore reason calls them "Two entries (May 27 and June 14 assaults) inside
the one frozen record". Each is limited to one day of a 50-day record, which makes it
`partial_interval` under tier-2 §3 item 2.

Two precedents treat such entries this way:

- the same batch's SC007 treatment of Livermore's "ASSAULT ON FORT WAGNER, JULY 18" lines
  (`us-lv-eng`, `us-lv-eff`, `cs-lv`: "July 18 assault only");
- the reviewed v1 Vicksburg entry (MS011 `us-lv-assault`, `cs-lv-assault`: "assault entry
  covers only May 22").

The LA010 inputs instead carry only `post_engagement_state` or `derived_from_losses`. That
leaves them as class C candidates, which set both points.

**Changes (LA010):**

| Side | Input | Quote | New `codes` | `bound` | `class` |
| --- | --- | --- | --- | --- | --- |
| US | `us-lv-may27` | "Banks's command, effectives 13,000" | `["partial_interval", "post_engagement_state"]` | `"lower"` | `"bound"` |
| Confederate | `cs-lv-may27` | "Deduct losses May 22-26 134 [c] 4,192" | `["derived_from_losses", "partial_interval"]` (`loss_timing` stays `not_prior`) | `"lower"` | `"bound"` |
| Confederate | `cs-lv-june14-pfd` | "Present for duty in Gardiner's command, June 14, estimated at [3] 3,750" | `["derived_from_losses", "partial_interval", "post_engagement_state"]` | `"lower"` | `"bound"` |
| Confederate | `cs-lv-june14-eff` | "Effectives estimated at 93 per cent. 3,487" | `["derived_from_losses", "partial_interval", "post_engagement_state"]` | `"lower"` | `"bound"` |

`cs-lv-may19` ("Gardner's command, effectives May 19, estimated at 93 per cent. of present for
duty May 19 [1] 4,326") is left as it is. It is a pre-start state of the whole garrison, and its
note 1 ("The returns are incomplete, and possibly omit the 1st, 11th, 14th, 17th, and 18th
Arkansas…") supports the recorded `scope_unresolved`. See V2E3-A6.

**Resulting estimates (replayed with the unchanged engine):**

- **US.** Grade `D`, with every value null and `method` `grade_D_no_candidate`.
  - `null_reason`: "Only bounds: Livermore's May 27 assault effectives (13,000) and June 14 columns of attack (about 6,000) are single days of the siege record; Irwin's 'at no time exceeded 17,000' effective is an upper bound, and his 'less than 12,000' and 'hardly exceeded 8,000' are caps on parts."
- **Confederate.** Grade `C`.
  - Values: point 4,330, low 3,030, high 9,100, `point_basis` `reported_effective`, `method` `rule3_median`.
  - `exact`: `{"point": "4326", "low": "15141/5", "high": "9100"}`, as the engine writes it.
  - `labels`: `["applicability_unresolved", "compiled_dependence", "whole_engagement_leakage"]`.
  - `point_groups`: `["cs-lv-may19"]`; `range_groups`: `["cs-irwin-7000", "cs-lv-may19"]`.
- **`nested`:** `{"sets": [], "excluded_post_start_information": false}`.

**Rationale text:** "No Union whole-interval figure: Livermore's two assault entries are single days of the siege, and Irwin gives caps. Confederate from Livermore's May 19 effectives before the siege (scope unresolved, note 1), with Irwin's 'about seven thousand' (state date unresolved) in the range; the May 27 and June 14 lines are single-day lower bounds."

**Effect:**

- The US side goes from C 13,000 to D.
- The Confederate side stays grade C. Its point moves from 4,190 to 4,330, and it loses `post_start_information`.
- The row was set3_ABC but excluded as post-start. It becomes incomplete.

**Ledger-wide effect of R1 and R2 together, by arithmetic from the check output:**

- side grades A/B/C/D go from 184/60/114/252 to 184/60/112/254;
- the fit-eligible counts (61/83/130) are unchanged;
- rows excluded as `post_start_information` go from 20 to 18.

The extraction record `docs/research/ledgers-v2.md` would need its tables updated after
reconciliation.

## Advisories (no correction required)

- **V2E3-A1 (LA006 Confederate, reproduction link; the primary should decide).**
  - **The passages.** Irwin (`irwin-west-louisiana-1863-selections-v1`, `bisland`, p.103) says "while Taylor reports but 4,000 men". Taylor's own report (`or15-taylor-west-louisiana-selections-v1`, `taylor-1863-04-23`, p.391) gives "our little army, which at the commencement of the contest was less than 4,000".
  - **The inconsistency.** The ledger's note on `cs-irwin-taylor` calls it "Taylor's own figure relayed by Irwin". Yet the only Taylor figure in the inspected passages is the one-sided "less than 4,000" (`cs-taylor-cap`). At Irish Bend (LA007), Irwin relays Taylor with the qualifier kept ("less than 1,000").
  - **Option 1: link the relay.** Set `cs-irwin-taylor.reproduction_of = "cs-taylor-cap"`.
    - Rule 2 would then group the two inputs as one bound-only group.
    - The LA006 Confederate side would become D, with Taylor's 4,000 recorded as an upper bound.
    - LA006 would leave set2_AB/set3_ABC (replayed).
  - **Option 2: keep the relay unlinked.** Record in the note why Irwin's unqualified figure is treated as separate. The v1 reconciliation left a qualified NPS restatement unlinked (KY009, memo "Implementation choices"), which supports this option.
  - I leave this advisory because v1 practice supports not linking a figure to a bound.
- **V2E3-A2 (KS002 Confederate, `cs-britton`).**
  - **The passage.** Britton's "between three and four hundred strong" is the column that "took up the line of march south" on October 2, four days before Baxter Springs.
  - **The inconsistency.** Extractor policy 4 codes departure figures `engagement_link_unknown`, and this batch does so for MO018 (`cs-sum` operands) and MO019 (`us-britton-column`). Adding that code would make `cs-britton` class C and add `applicability_unresolved` to the Confederate side.
  - **Effect.** Grade A, point 400 and range 330–420 are unchanged (replayed), and the row is incomplete anyway.
  - **KS001.** KS001's `cs-britton-300` ("set out on his raid into Kansas … with three hundred men", the evening before) is more directly tied to the raid and can stay as it is.
- **V2E3-A3 (results that look odd from their inputs, not coding errors):**
  - **MO019 Confederate.** C 3,750 comes from three-quarters of the prisoners' 5,000. Marmaduke's own column figures (Shelby about 1,000 and MacDonald about 270 at the December 31 departure, and Porter about 700 at the January 2 departure) have different state times and are not all in this dossier's citations, so rule 6 does not allow a sum. The rationale could say so.
  - **AR007 Confederate.** C 5,630 comes from Vandever's hearsay. It sits above Marmaduke's own "did not exceed 3,500" effective cap, which on an unknown-basis point is the declared B3 consequence. The rationale already says this.
  - **AR010.** Both points rest on Price's whole-army figures ("barely 8,000" and "nearly or quite 20,000"), given before September 10. The frozen US force is Davidson's cavalry division, and Price's passage gives Dobbin's "about 1,200" as the force first engaged. The C grades and `applicability_unresolved` labels already show this, and the row sits in set3_ABC.
- **V2E3-A4 (LA016 US, `us-irwin-2500`).** Irwin's "This division was about 2,500 strong" is Herron's (Dana's) whole division at Morganza. The passage names "the outposts … at Sterling's plantation" as what Green attacked, so the division is a superset of the engaged force, not an unsettled scope. Recording it as `scope_unresolved` widens the US high end to 2,880 and adds `applicability_unresolved`. The tier-2 codes have no "superset" code; a note would be enough.
- **V2E3-A5 (smaller coding notes, no effect on any value):**
  - **MO020 `us-nps-desc`.** "with his combined force of about 2,000 men, at Bloomfield" describes McNeil before his retreat. `engagement_link_unknown` fits better than `scope_unresolved` (both are row 4).
  - **LA013 `us-green-500`.** "between 500 and 000" has an unreadable upper figure, and `unreadable_value` could be noted.
  - **OK006.** The CWSAC and NPS "1,600–1,800" equals the prisoners' range that Williams relays. No passage shows the tables citing it, so class A is correct under tier-2 §3 item 3.
  - **AR011.** The engine groups the prisoners' 2,000–3,000 with Clayton's 2,500 (same document, same basis, equal midpoints), which gives `single_input`. The point and range are the same either way; this is engine behaviour, outside this batch.
  - **MO018 US.** Britton's full unit list (453 + 289 + 223 + 378 + 400 + 350) goes beyond the cited quote and was correctly not summed. It would not move the grade-A point.
- **V2E3-A6 (LA010 `cs-lv-may19`).** This line is an intermediate figure of Livermore's May 27 assault entry, before an in-record loss deduction. The v1 Gettysburg precedent coded such a line `engagement_link_unknown`, and adding that code beside `scope_unresolved` would not change the class. It should not be coded `partial_interval` without care. If it were, the Confederate point would fall to `cs-march` (present for duty, 16,287), the end-of-March garrison that Irwin shows was cut by four brigades sent to Vicksburg in May.

## Per-engagement results

| Battle | Checked | Finding |
| --- | --- | --- |
| TX003 | Davis's "not less than 3,000" (opponent estimate, shore force only, one-sided); Magruder's 300 and 500 are parts; no US figure in Davis's section | Both sides D confirmed |
| MO018 | CWSAC 2,000; the sum of Marmaduke's own departure columns is supported by "With Shelby and MacDonald, I attacked Springfield"; opponent 4,200/5,000–6,000 only raise the high end | OK (A5) |
| MO019 | CWSAC 700; Britton's 800 departure column coded C; the prisoners' 5,000 (rule 4) | OK (A3) |
| GA002 | Vessel and gun counts only | Both sides D confirmed |
| SC004 | Du Pont's conditional "1,200 men and 32 guns", scope unresolved (C); only Confederate gun counts | OK; Confederate D confirmed |
| SC005 | Jones p.207, 211, 216–217, 244; Gillmore p.8–12 | **R1** |
| SC007 | CWSAC 5,000/1,800; the Livermore p104 image agrees with the transcription; July 18 lines are partial-interval bounds and `bound_conflict` is correct; p105 has only a loss line | OK |
| SC009 | CWSAC 413; Sumter's 205 is part of the defenders | OK; Confederate D confirmed |
| LA006 | Irwin 10,000 / "Taylor reports but 4,000"; Taylor's "less than 4,000" and "at least 14,000" | A1 |
| LA007 | Irwin's 5,000 for Grover; the Confederate figures cap only the charge | OK; Confederate D confirmed |
| LA008 | Ratio and unit identifications only | Both sides D confirmed |
| MO020 | NPS 2,000; Marmaduke's own 5,000 is expedition-wide (C); McNeil's 8,000 raises the high end | OK (A5) |
| AR007 | Marmaduke's 8,000 for the pursuers (rule 4); Vandever's "7,000 or 8,000" (rule 4); the own cap does not apply | OK (A3) |
| LA009 | Miles's 400 (with Irwin's relay) is part of the force | Both sides D confirmed |
| LA010 | Livermore p101 (image checked) and Irwin p.163–217 | **R2**, A6 |
| LA012 | CWSAC 838 and Stickney's "only about 600 were engaged", lower-middle median; Irwin's June 22 figure is after the record | OK; Confederate D confirmed |
| LA013 | Irwin's 180 garrison and 1,300–1,500; the 1,811 includes this action's losses (C); Green's 800 is the assault party | OK (A5) |
| LA015 | Green's "not over 800" and "not over 750" are caps on parts | Both sides D confirmed |
| LA016 | NPS 1,000-man detachment (B); Irwin's 2,500 division | OK (A4); Confederate D confirmed |
| OK006 | CWSAC description 1,600–1,800 (the strength fields read 1,600; the inventory notes this) and NPS 1,500 | OK (A5); US D confirmed |
| OK007 | NPS 3,000; Cooper's aide's 4,000; Cabell's 2,000 arrived after the battle | OK; Confederate D confirmed |
| AR009 | Cabell's own 1,250 on Aug 31 (C) with his 1,600 field cap applied; the 900 after the action is unusable | OK; US D confirmed |
| KS001 | NPS 350; Pike's 700 raises the high end | OK; US D confirmed ("No Union troops") |
| TX006 | CWSAC 44; Dowling's 47 (B) | OK; US D confirmed |
| AR010 | Price's 8,000 and 20,000 | OK (A3) |
| AR011 | Clayton's own 550; the Confederate side is opponent-only (rule 4) | OK (A5) |
| KS002 | CWSAC 400; Britton's 300–400 | A2; US D confirmed |
| FL004 | Landing party only (100 or 130) | Both sides D confirmed |

**Grade D reasons.** The recorded reason is accurate for all 24 grade D sides in the batch,
and no usable figure was missed in the cited dossier passages or the matching Livermore pages.
After R1 there would be 25 grade D sides. The inventory is complete: every dossier strength
citation, frozen CWSAC figure and figure in a matching Livermore entry (p101, p104, p105) is an
input or is recorded with an accurate reason.

## Outcome

**Corrections required:** V2E3-R1 (SC005) and V2E3-R2 (LA010). Advisories: V2E3-A1 to V2E3-A6.
The primary should check each finding against its passage before changing the ledger.
