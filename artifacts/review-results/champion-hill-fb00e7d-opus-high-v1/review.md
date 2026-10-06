# Champion Hill (MS009) separate source review

- **Reviewer:** the `evidence-reviewer` subagent, model `claude-opus-5-5` (Claude Opus 5.5), reasoning effort `high`, started with fresh context. The primary's conversation was not an input. No task ID was visible to the reviewer. It ran in the `wt-champion-hill` worktree.
- **Date:** 2026-10-06.
- **Commits:** prepared commit `fb00e7da75b1a21d10033f2dde39379c45949ce0`. The worktree HEAD was `379da810d11e86945ed1907d17a3e3a3a5870fed`, which adds only the two review-assignment directories (`git diff --stat fb00e7d HEAD`). `git diff 4547657 fb00e7d -- data/evidence/MS009.json` is empty, so the dossier has not changed since `4547657`.
- **Input hashes:** all 21 SHA-256 values in `inputs.json` match the blobs at `fb00e7d` and the worktree files. They include `data/evidence/MS009.json` `f1d093f1…c413`, `data/raw/cwsac_battles.csv` `952b5d08…5f1f`, `data/raw/cwsac_forces.csv` `a462f6be…d7d5` and `data/raw/cwsac_commanders.csv` `6c587c29…00c7`. These also match the `data/sources.json` entries for `arnold-cwsac-battles`, `-forces` and `-commanders`.
- **Validation:** I ran `make check` offline. It exited 0 and ran 151 tests (OK). The baseline is unchanged: 127 pilot battles, **23 eligible / 13 groups**, strength-logistic Brier **0.2768816348133779** against **0.25** for equal odds, and `admission_promoted_rows: 0`. I ran no build or packet commands. The worktree was clean before this file was written.
- **Status:** this is an AI review, not human historical adjudication, independent corroboration or feature admission.

## Inspected scope

- **Dossier:** all of `data/evidence/MS009.json`. That covers 7 claims, 4 citation occurrences, the 3 null unknowns, all seven dimensions, the null replacement boundaries, the boundary note and the 3 open questions.
- **`arnold-cwsac-battles` MS009 row:** every cell, including `description` (read in full), `results_text`, `result`, `forces_text`, `strength` (blank) and `casualties_text`.
- **`arnold-cwsac-forces` MS009 rows:** both rows. The Confederate row is "Department of Mississippi and East Louisiana" and the US row is "Army of the Tennessee (three corps)". `strength_min` and `strength_max` are blank in both rows. The casualty figures are 4300 and 2457.
- **`arnold-cwsac-commanders` MS009 rows:** both rows, John C. Pemberton (CS) and Ulysses S. Grant (US). Johnston is not listed.
- **Project guidance:** AGENTS.md, README, methodology, sources, the evidence contract, the Vicksburg first-pass record for its conventions, and the roadmap mentions of MS009. I also read the citation checks in `generalship/evidence.py`, which reject empty or whitespace-only quotes.
- **Quote checks:** every quote below, existing or proposed, occurs exactly once in its cell. I checked this by script.
- **Source family:** all of these rows belong to one family, `nps-cwsac`, which is a retrospective NPS/CWSAC summary digitized by Arnold. They do not corroborate one another, and none is a contemporary record.
- **Not opened:** other source families, the other Vicksburg dossiers (beyond the first-pass record), Antietam and the network.

## Claim findings

| Claim | Finding |
|---|---|
| `pemberton-order` | **Correction required (CH-R1).** The attribution is correct. The quote's "he" refers to Johnston in the preceding clause ("Gen. Joseph E. Johnston retreated, … but he ordered Lt. Gen. John C. Pemberton"), and the value matches the content of the order. The rationale's "later repeated direction" is supported by the cell but not by any cited passage. |
| `alternate-plan` | Supported. The value matches the source's collective attribution to "Pemberton and his generals". The `logistics` dimension is acceptable because the target was the opponent's supply trains. `commander_created` is acceptable as a draft hypothesis. See advisory notes A1 and A2. |
| `force-candidate` | **Correction required (CH-R2).** The "about 23,000" figure is correctly framed as a force under command, not personnel engaged. The value's second clause ("the structured force table has no numerical estimate") is true: both forces rows have blank `strength_min` and `strength_max`, and the battles `strength` cell is blank. No citation supports that clause, though, and blank cells cannot be quoted. |
| `result` | Supported. `results_text` is "Union victory" and `result` is "Union", so the frozen result is retained. |
| `terrain-unknown` | **Correction required (CH-R3).** The already-inspected `description` cell contains terrain evidence, so the rationale "Not established by the sources inspected for this draft" is wrong. |
| `information-unknown` | **Correction required (CH-R4).** The same cell contains information evidence. |
| `responsibility-unknown` | **Correction required (CH-R5).** The same cell attributes specific orders to named commanders. |

The phase tags `inherited`, `commander_created`, `post_outcome` and `unresolved` are reasonable draft hypotheses given the rationales and the unset boundaries. No claim attributes credit automatically to both listed commanders. The boundary note and all three open questions are appropriate and should be kept.

## Required corrections

These corrections use only the already-inspected `arnold-cwsac-battles` and `arnold-cwsac-forces` MS009 rows; no new source is needed. In each citation, `row_key` is `{"battle": "MS009"}` and `source_id` is `arnold-cwsac-battles` unless stated otherwise. The primary should verify each correction and choose how to version the change (for example, archiving the v1 dossier). Claim IDs for CH-R3 to CH-R5 are suggestions. The contract also allows the existing IDs to be kept when a claim's interpretation is amended.

### CH-R1 `pemberton-order`: cite the repeated order

Keep the value and the existing citation. Append this citation (`column: description`):

> "On May 16, though, Pemberton received another order from Johnston repeating his former directions."

Replace the rationale with:

> "The NPS summary reports Johnston's order, placed after the Union occupation of Jackson but otherwise undated, and a further order from Johnston repeating those directions, which Pemberton received on May 16. Both are retrospective NPS paraphrases, not the correspondence (see open question 1). Inherited is a hypothesis relative to Pemberton; Johnston is not a listed MS009 commander."

### CH-R2 `force-candidate`: support or relocate the table clause

Replace the value with:

> "The NPS narrative reports Pemberton commanding about 23,000 men at the time of Johnston's order; the structured MS009 force descriptions name formations without numbers."

Use these citations:

1. `description`: "he ordered Lt. Gen. John C. Pemberton, commanding about 23,000 men". This replaces the shorter existing quote, which is a substring of it.
2. `forces_text`: "Department of Mississippi and East Louisiana [CS]".
3. `forces_text`: "Army of the Tennessee (three corps) [US]".

Replace the rationale with:

> "A force under command when the order was issued, not personnel engaged, and not tied by the source to the Department of Mississippi and East Louisiana named in the force row; it is not automatically promoted. arnold-cwsac-forces MS009/Confederate and MS009/US have blank strength_min and strength_max, and the arnold-cwsac-battles strength cell is blank; blank cells cannot be quoted, so this absence is recorded as an inspected observation. No Union figure is given."

The `phase` stays `unresolved` and the `status` stays `supported`.

### CH-R3 terrain: replace `terrain-unknown`

Suggested ID `terrain-ridge-line`, dimension `terrain`, phase `unresolved`, status `supported`.

Value:

> "The NPS summary places Pemberton's defensive line along a ridge crest overlooking Jackson Creek, with Lee's men atop Champion Hill as a lookout, and gives the Raymond Road crossing of Bakers Creek as the one escape route still open during the withdrawal."

Rationale:

> "Qualitative terrain from one retrospective NPS summary; no elevations, distances (other than the rear's position) or assessment of advantage. Phase is unresolved because the boundaries are unset."

Citations (`description`):

- "Pemberton's force drew up into a defensive line along a crest of a ridge overlooking Jackson Creek."
- "Pemberton posted Brig. Gen. Stephen D. Lee's men atop Champion Hill where they could watch for the reported Union column moving to the crossroads."
- "the one escape route still open: the Raymond Road crossing of Bakers Creek"

### CH-R4 information: replace `information-unknown`

Suggested ID `information-left-flank`, dimension `information`, phase `unresolved`, status `supported`.

Value:

> "The NPS summary says Pemberton was unaware that a Union column was moving along the Jackson Road against his unprotected left flank, while also saying he posted Lee to watch for 'the reported Union column'; after Lee and the Union troops sighted each other, Pemberton received warning and sent troops to his left flank."

Rationale:

> "The summary does not reconcile 'unaware' with 'the reported Union column' or give times for these steps; keep the sequence unresolved rather than infer what Pemberton knew when. No information-quality score is implied."

Citations (`description`):

- "Pemberton was unaware that one Union column was moving along the Jackson Road against his unprotected left flank."
- "Pemberton posted Brig. Gen. Stephen D. Lee's men atop Champion Hill where they could watch for the reported Union column moving to the crossroads."
- "Lee spotted the Union troops and they soon saw him."
- "Pemberton received warning of the Union movement and sent troops to his left flank."

The Lee quote also appears in CH-R3, and quoting it twice is permitted. The primary may cite only the phrase "where they could watch for the reported Union column" here instead.

### CH-R5 responsibility: replace `responsibility-unknown`

Suggested ID `responsibility-orders`, dimension `responsibility`, phase `unresolved`, status `supported`.

Value:

> "The NPS summary attributes the countermarch and the order withdrawing his men from the field to Pemberton, and the order to begin the attack (on his arrival around 10:00 am) and the later counterattack with forces just arrived from Clinton to Grant; it names Bowen's division's counterattack and Tilghman's rearguard as subordinate actions."

Rationale:

> "Attribution of orders as narrated in one retrospective summary; it does not apportion credit or blame, and no action is automatically credited to both listed commanders. Clock times are the source's approximate labels."

Citations (`description`):

- "Thus, when he ordered a countermarch, his rear, including his many supply wagons, became the advance of his force."
- "When Grant arrived at Champion Hill, around 10:00 am, he ordered the attack to begin."
- "One of Pemberton's divisions (Bowen's) then counterattacked"
- "Grant then counterattacked, committing forces that had just arrived from Clinton by way of Bolton."
- "so he ordered his men from the field to the one escape route still open"
- "Brig. Gen. Lloyd Tilghman's brigade formed the rearguard"

In the countermarch quote, "he" refers to Pemberton, who is the subject of the preceding sentence. In the withdrawal quote, "he" refers to Pemberton through "Pemberton's men could not stand up to this assault".

### Net effect

- **Claims:** still 7, now with 0 null unknowns.
- **Citations:** 4 become 21 (+1 for CH-R1, +2 for CH-R2, +3, +4 and +6 for CH-R3 to CH-R5).
- **Source families:** still one (`nps-cwsac`).
- **Model inputs:** unchanged. The baseline and admission state are not affected.

## Advisory notes (not required)

- **A1.** The `alternate-plan` rationale could state that the source attributes the decision jointly to "Pemberton and his generals". A `commander_created` tag therefore does not give Pemberton sole credit. The decision could also reasonably be classed under `objectives`. The current `logistics` classification is defensible and does not need to change.
- **A2.** The description also says that Pemberton "had already started after the supply trains" when the repeated order arrived, and that the countermarch made his supply wagons "the advance of his force". These passages bear on logistics and on the consequences of the decision. The primary may cite them in `alternate-plan` or in CH-R5, but neither citation is required.
- **A3.** MS009 rests on one retrospective source family, the NPS/CWSAC summary as digitized by Arnold. The first-pass ceiling allows up to three families, and the other Vicksburg records each use three. This is a coverage gap to record. It is not a correction in this review's scope, and under the stopping rule it does not automatically justify a new research packet.
- **A4.** The summary gives the engagement starting "about 7:00 am" and Grant ordering "the attack to begin" around 10:00 am. If these clocks are recorded later, keep them as source-qualified labels and do not reconcile them.
- **A5.** `casualties_text` (6,757 total; US 2,457; CS 4,300) is post-outcome and correctly unused.

## Outcome

Five required corrections (CH-R1 to CH-R5), all extraction or citation errors that the already-inspected MS009 rows can fix. No historical dispute is adjudicated, nothing is admitted, and the frozen result "Union victory" stays.
