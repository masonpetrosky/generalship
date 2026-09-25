# Atlanta Campaign first pass: separate review (Opus 5.5, high)

**Outcome: corrections required.** Required findings: ATL-R1 to ATL-R8. Advisories: ATL-A1 to ATL-A11.

This is an AI review, a separate analysis. It is not human historical adjudication. It does not
establish that any source is independent, and it does not admit any feature.

## Record

| Field | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. Fresh-context subagent; the author's conversation was not an input. |
| Date | 2026-09-25 |
| Prepared commit reviewed | `1191d32433575d224120a6d2aa1df8e381dcecf7` |
| Previous commit | `4e705de56c131379d288356a7787f6e82b3e75c7` |
| Bundle commit (worktree HEAD) | `794993bcabea8dde394871fe31e50d8757357677` |
| `assignment.md` sha256 | `1a35dd523c14705c92f12f47646ec3d681e2fc6e4d0475fc2ddd667736fe279c` (verified) |
| `inputs.json` sha256 | `2fc80332400572936d479c232e099e5b10d30a641ef28a5c4edc5b76e51e06e7` (verified) |
| Input hashes | All 82 paths in `inputs.json` match both `git show 1191d32:<path>` and the worktree file. No mismatch. |
| `make check` (offline) | Passed at the bundle commit: `Ran 134 tests … OK`, then `python3 -m generalship check` reported 169 draft dossiers and 0 promoted admission rows. No build, packet or network command was run. |

## Scope actually inspected

- **Documents.**
  - Read in full: AGENTS.md, `docs/evidence-contract.md`, `docs/cohort-v2.md` and
    `docs/research/atlanta-first-pass-v1.md`.
  - Read in part: `docs/methodology.md` (research depth and coverage section) and the
    `docs/sources.md` diff from `4e705de`.
  - Not re-read: README and roadmap.
- **Dossiers GA007–GA022.** For all 16, I read:
  - every claim's value, status, phase and rationale;
  - the boundary note and open questions.

  Every citation was checked:
  - **Text citations (491).** Each quote was shown with about 170–230 characters of context on
    each side. Where the attribution, date or scope needed it, I read wider passages. Examples:
    - Cox pp.39–40 (dates of the cavalry affairs);
    - Cox p.44 (Judah);
    - Cox pp.79–80 (Pickett's Mill footnote);
    - Cox pp.191–192 (Utoy dates);
    - Cox pp.201–202 (Jonesborough, August 31);
    - Johnston pp.615–616 (French's division, Cassville);
    - Hood p.630 (Hardee and the delay);
    - Logan pp.96, 105.
  - **CSV and NPS citations.** Checked against the frozen battle, force and commander rows for
    all 16 records and against all 16 live NPS text snapshots, which I read in full.
- **Selections.**
  - Read in full: Cleburne, Steedman, Schofield and Kilpatrick.
  - Read at every cited passage plus surrounding context, not end to end: Johnston, Hood,
    Hardee, Logan and Cox. Cox is about 311 KB.
  - Selection integrity: I re-derived every section of all nine selection files from its
    parent OCR using the recorded character ranges and whitespace collapse. All 43 sections
    match exactly, including the title sections.
- **Registry.** I compared all 47 new source records with `4e705de`: no earlier record
  changed. I read the full records for Cox (3), OR Parts 2 and 3 (4) and the eight OR
  selections, and one NPS HTML/text pair. I also checked the earlier groups
  `johnston-mississippi-report`, `cleburne-ringgold-report` and `or-beauregard`, including
  Hardee's two records there. Registry size is 736 entries and 715 distinct paths, against
  689 and 668 at `4e705de`.
- **Mechanical checks.**
  - Claim, unknown and citation counts: 144, 19 and 718, matching the memo.
  - Independence groups per dossier: exactly three each, with NPS and Arnold as one group.
  - Phases: only `unresolved` and `post_outcome`.
  - A heuristic check of OCR page locators against the nearest preceding running head found
    no locator mismatch. The "inferred page" locators are consistent with the adjacent heads.
- **Not inspected.**
  - The NPS HTML files (hash only; the HTML-to-text transform was not re-run).
  - The catalog metadata JSON contents.
  - The full OCR parents outside the selected ranges.
  - Uncited stretches of the Cox, Hood, Hardee, Johnston and Logan selections.

  No new research was done and no source family was added.

## Summary judgement

The dossiers are careful. Almost every value is entailed by its quotes read in context.
Disputes are generally kept visible: entrenchment at New Hope Church, the wagon counts, Hood's
account of Kolb's Farm, the attacking corps and artillery at Ezra Church, Utoy Creek, the
Hood–Hardee controversy and Kilpatrick's rout claim.

The records follow the rules:

- opening strengths are null;
- no figure is adopted;
- aggregate and period totals are labelled context;
- the three-family ceiling holds;
- no `inherited` tag is used;
- listed commanders get no automatic credit.

The required findings are:

- four extraction or scope errors (ATL-R2, R3, R5, R6);
- two disputes missed inside the inspected passages (ATL-R4, R7);
- a memo whose coverage, registry and validation statements are stale for this commit (ATL-R1),
  and one miscount (ATL-R8).

## Required corrections

### ATL-R1: memo coverage, registry counts and validation are wrong for `1191d32`

The memo is `docs/research/atlanta-first-pass-v1.md`. At the prepared commit there were already
153 dossiers before this pass:

- 127 v1 records;
- 11 Overland records;
- 7 Early's Raid records;
- 8 Sheridan's Valley records.

The pass brings the total to 169. `generalship check` reports 169 draft dossiers. Dossiers span
40 of 119 campaign groups. The registry grows from 689/668 to 736/715, which is what
`docs/sources.md` already says. `make check` passes. The test named in the memo already checks
membership in cohort v2 (`found <= cohort-v2 battle_ids`) and passes.

Exact replacements:

1. Replace the coverage paragraph (lines 28–31):

   > In this worktree, coverage is **143/384 cohort-v2 engagements** with draft dossiers (the
   > 127 v1 records plus these 16). By dossier presence that is **37/119 campaign groups**. A
   > parallel pass on another campaign is not counted here. All 127 earlier dossiers and all
   > historical revisions are unchanged.

   with:

   > At the prepared commit, coverage is **169/384 cohort-v2 engagements** with draft dossiers:
   > the 127 v1 records, the 26 records added by the earlier Overland, Early's Raid and
   > Sheridan's Valley first passes, and these 16. By dossier presence that is
   > **40/119 campaign groups**. All 153 earlier dossiers and all historical revisions are
   > unchanged.

2. Replace "bring the registry to **656 entries / 635 raw paths**, preserving the earlier
   **609/588**" with "bring the registry to **736 entries / 715 raw paths**, preserving the
   earlier **689/668**".

3. Replace the second Validation bullet, which begins "`python3 -m unittest discover -s tests`
   has one failure" and runs through "It was not edited in this pass.", with:

   > `make check` passes (134 tests, then `python3 -m generalship check`).
   > `test_repository_dossiers_have_resolvable_passages` already accepts any cohort-v2 ID.

### ATL-R2: GA009 `reported-force-scope` misses the conflict over French's division

**Problem.** The value says only that Cox has French's division joining at Adairsville. Two
inspected passages place it at Cassville on May 18, after the frozen date:

- Cox's own Appendix A;
- Johnston's report.

This is a family already used in GA009.

**Value.** Replace "Cox says French's infantry and Jackson's cavalry divisions joined at
Adairsville and that" with:

> Cox's narrative says French's infantry and Jackson's cavalry divisions joined Polk's corps at
> Adairsville, but his Appendix A lists French's division as joining at Cassville on May 18,
> and Johnston says French's division joined Polk's corps on the 18th. Cox also says that

**Add these citations:**

| Source | Section | Quote | Locator |
| --- | --- | --- | --- |
| `cox-atlanta-selections-v1` | `appendix-a` | "French's division joined at Cassville." | p.242 (OCR page markers; not checked against print) |
| `cox-atlanta-selections-v1` | `appendix-a` | "French's division, Cassville, May 18th 4,413" | p.243 (OCR page markers; not checked against print) |
| `or38-3-johnston-atlanta-selections-v1` | `johnston-1864-10-20` | "French’s division having joined Polk’s corps on the 18th," (curly apostrophes as in the OCR) | p.615 (OCR page markers; not checked against print) |

**Rationale.** Append:

> Where and when French's division joined is disputed (Adairsville in Cox's narrative;
> Cassville on May 18 in his Appendix A and in Johnston). Its presence on May 17 is not assumed.

### ATL-R3: GA012 `reported-force-scope` misstates Cleburne on the dismounted cavalry

**Problem.** Cleburne does not say the cavalry supported him on his right. He writes that
Granbury "had but just gotten into position and a dismounted cavalry force … had passed behind
him, when the enemy advanced". Later he says the enemy was "driving back some cavalry" at the
field on Granbury's right.

**Value.** Replace "supported by a dismounted cavalry force on his right and later Quarles's
brigade" with:

> and says a dismounted cavalry force had passed behind Granbury as the Union advance began;
> Quarles's brigade, sent up by Hood, later formed a second line

No citation change is needed. The existing quotes "a dismounted cavalry force, in line behind a
few disconnected heaps of ston loosely piled together," and "Quarles’ brigade, of Stewart’s
division, just then evidentially sent up by General Hood" support the replacement.

### ATL-R4: May 27 entrenchment conflict between GA010 and GA012 is not cross-referenced

**Problem.** Two inspected passages conflict about entrenchment in the May 27 action:

- **GA010 `wooded-ridges-and-works`** records Johnston: "In these two actions our troops were
  not intrenched." The two actions are May 25 and May 27.
- **GA012 `wooded-ravine-and-angle`** cites Cleburne's statement about the May 27 action that
  "Intrenchments were thrown up in tl afternoon and night of the 26th and in the morning of the
  27tli."

Neither dossier notes the conflict. Under the family ceiling, each dossier should record it in
its rationale only, with no new cross-family citation.

**GA012 `wooded-ravine-and-angle` rationale.** Append:

> Johnston's report (cited in GA010 `wooded-ridges-and-works`; not a GA012 family) says the
> troops were not entrenched in the May 25 and May 27 actions; Cleburne's statement of
> entrenchments thrown up on the 26th-27th conflicts with it and is unresolved.

**GA010 `wooded-ridges-and-works` rationale.** Append:

> For May 27, Cleburne's May 30 report (GA012 `wooded-ravine-and-angle`; not a GA010 family)
> says his division's entrenchments were thrown up on the 26th and the morning of the 27th,
> contrary to Johnston's statement.

### ATL-R5: GA018 `casualty-records` rationale asserts an unsupported scope for Logan's 562

**Problem.** Logan writes "My losses were 50 killed, 439 wounded, and 73 missing". Neither
report says whether the figure includes the roughly 1,000 men lent by Blair and Dodge who fought
under his command. The rationale asserts that it excludes them.

**Rationale.** Replace "The frozen US 562 equals Logan's Fifteenth Corps aggregate, which does
not cover the reinforcing regiments of the other corps; whether the frozen figure derives from
it is not established." with:

> The frozen US 562 equals Logan's aggregate for 'my losses'; the inspected passages do not
> say whether it includes the regiments lent by Blair and Dodge, and it does not cover the rest
> of the Army of the Tennessee. Whether the frozen figure derives from it is not established.

### ATL-R6: GA020 `reported-force-scope` treats Steedman's 1,800 as the relief force alone

**Problem.** The number comes from "The troops engaged were … Second Missouri, Twenty-ninth,
Fifty-first, and Sixty-eighth Indiana, … and Fourteenth U. S. Colored Troops; in all, 1,800
effective". The next sentence names "Colonel Laiboldt, Second Missouri Volunteers, commanding
Dalton". So the list begins with the regiment of the garrison commander. The figure is not
shown to be the relief column alone.

**Value.** Replace "Steedman says his relief force was 1,800 effective, that he readied rail
transport for 2,000 men," with:

> Steedman gives the troops engaged (a list beginning with the Second Missouri, the regiment of
> Colonel Laiboldt, who commanded Dalton) as 1,800 effective in all; he says he readied rail
> transport for 2,000 men,

**Value.** Replace "The garrison's own strength is not given in the selected passage." with:

> The passage gives no separate strength for the garrison or for the relief column.

**Rationale.** Replace "Steedman's relief-force figure and his opinions of the enemy's size"
with:

> Steedman's figure for all Union troops engaged (not shown to be the relief column alone) and
> his opinions of the enemy's size

**Add these citations:**

| Source | Section | Quote | Locator |
| --- | --- | --- | --- |
| `or38-2-steedman-dalton-selections-v1` | `steedman-1864-09-11` | "Second Missouri, Twenty-ninth, Fifty-first, and Sixty-eighth Indiana," | p.496 (OCR page markers; not checked against print) |
| `or38-2-steedman-dalton-selections-v1` | `steedman-1864-09-11` | "Colonel Laiboldt, Second Missouri Volunteers, commanding Dalton," | p.496 (OCR page markers; not checked against print) |

The memo's "Steedman's 1,800 effective" should read "Steedman's 1,800 effective troops engaged".

### ATL-R7: GA019 misses Schofield's statement about August 4–5

**Problem.** Cox has Baird carrying the entrenched skirmish line on the 5th, inside the frozen
interval: "carried with a loss of 83 killed and wounded. One hundred and forty prisoners were
captured". GA019 `casualty-records` cites this. Schofield's selected passage says the opposite:
"During the 4th and 5th no movement of consequence was made." The dispute belongs in the
record.

**GA019 `casualty-records` value.** Replace "Schofield's inspected passage gives no figure." with:

> Schofield's inspected passage gives no figure and says no movement of consequence was made
> during the 4th and 5th, without mentioning the skirmish-line action Cox places on the 5th.

**Add this citation:**

| Source | Section | Quote | Locator |
| --- | --- | --- | --- |
| `or38-2-schofield-utoy-selections-v1` | `schofield-1864-09-10-utoy` | "During the 4th and 5th no movement of consequence was made." | p.517 (OCR page markers; not checked against print) |

**Rationale.** Append:

> Schofield and Cox differ on whether there was fighting of consequence on August 5.

The status is already `disputed`.

### ATL-R8: miscount of the Cox passages

**Problem.** `cox-selections.txt` has sixteen narrative sections plus `title`. They run from
`opposing-armies-strength` to `appendix-a`, and the memo's own list enumerates the same sixteen.
The memo says "Seventeen passages are selected and read in full".

**Memo.** Replace "Seventeen passages are selected and read in full:" with "Sixteen passages
(plus the title page) are selected and read in full:".

**Registry.** `cox-atlanta-selections-v1.inspection` says "Transcription note, title and
seventeen passages read in full". Correcting it to "sixteen passages" is a metadata correction.
Under the evidence contract that means a `metadata_only` revision under a new source ID,
unless the owner treats this unpublished prepared record as still amendable. The miscount does
not affect any citation.

## Advisories (optional)

- **ATL-A1.** GA009 `engineer-reports-and-maps`: Cox's "maps of the country were almost
  worthless … inhabitants were hostile" passage describes the May 18 pursuit toward Cassville.
  Note that scope in the rationale.
- **ATL-A2.** GA013:
  - Cox's beef-on-the-hoof passage (p.93) describes the early-June change of base, before
    June 9.
  - Johnston's "41,000 infantry and artillery and 10,000 cavalry" is the July 18 transfer,
    after the July 3 end of the interval.

  The rationale says "different dates". Naming these dates would make the scope explicit.
- **ATL-A3.** GA022 `recorded-result`: the Hardee family says Cleburne achieved something on
  August 31.
  - Aug 31 telegram: "carried the enemy's intrenchments on the left and holds them".
  - 1865 report: Cleburne "carried the temporary works", and part of his command crossed the
    Flint and took 2 guns.
  - Cox, by contrast, says Cleburne's corps "took little part in the affair beyond preventing
    Kilpatrick" from crossing.

  This is a real dispute within the inspected passages. It could be added as a disputed
  element.
- **ATL-A4.** GA018: Logan's two reports differ on duration. The July 29 report says fighting
  lasted "until about 3 o'clock"; the campaign report says "until darkness". Cox says the enemy
  drew off "before sunset". This is minor.
- **ATL-A5.** GA017 `casualty-records`: Hood's claim that 13 guns were captured (5 by Cheatham,
  8 by Hardee) sits against Cox's Union loss of "ten pieces of artillery". The value lists both
  figures; one sentence noting the conflict would help.
- **ATL-A6.** GA010 `reported-force-scope`:
  - The advance-guard fight (Geary alone) came before the three-division assault. The current
    wording runs the two together.
  - Appendix A adds "200 for officers" to Quarles's 2,200 effectives.
- **ATL-A7.** GA015: Cox names French's and Walker's divisions opposite Logan. Johnston names
  French's and Featherston's of Loring's corps as the most heavily assailed. This is a minor
  unit discrepancy.
- **ATL-A8.** GA008 `command-roles`: the quote "They were unable to get a foothold …" does not
  itself name Judah. The preceding sentence does. Extending the quote, or adding "His right
  division (Judah's) marched against the angle", would make the passage self-contained.
- **ATL-A9.** The memo's "Separate review pending" section should be updated once this review is
  reconciled.
- **ATL-A10. Per-campaign groups for authors registered earlier (Johnston, Cleburne, Hardee).**
  This is acceptable for this batch:
  - no Atlanta dossier cites two groups by the same author;
  - each dependency note names the earlier group;
  - Hardee's earlier papers really are in `or-beauregard`, as `or-hardee-april4-contact-v1` and
    `or-hardee-1863-precontact-v1` show.

  But separate group names are not evidence of independence. Any cross-campaign use that
  counts families should treat same-author groups as dependent. That grouping sits under a
  container-level group (`or-beauregard`) for Shiloh and an author-level group here. The
  principle differs between campaigns, and a future registry note should record it. No change
  is required now.
- **ATL-A11. The other sub-question 4 choices are sound on the inspected evidence.**
  - **GA013** cites only monthly and campaign totals, as context, and avoids repeating or adding
    the Kolb's Farm and Kennesaw figures. That is the correct way to avoid double counting
    between an aggregate operation and its separate frozen components.
  - **Campaign label.** Not adopting the live NPS label "Morgan's Raid Into Kentucky" is
    correct. All sixteen live pages carry it, together with a campaign-wide date string that
    does not match the engagement. It is an evident database defect and is recorded, not used.
  - **Cox edition.** The 1882 Cox choice is supported by the OCR title page ("NEW YORK CHARLES
    SCKIBNER'S SONS 1882 COPTBIGHT … 1882"). The rejected 1883 Toronto scan was never
    registered, so no pinned input was deleted.
  - **OR imprint.** The OR imprint of 1891 is shown in both title selections. The 1880 catalog
    date is correctly not substituted.

## Items checked and found sound (not exhaustive)

- **Johnston attributions.**
  - Dug Gap is credited to Hardee and Granbury.
  - The instructions to Hood were revoked after 9 p.m. on the 14th.
  - Stewart's division did not receive the countermand.
  - The Cassville wagons are given as 250.
  - Kennesaw: Cheatham 195, Cleburne 11, Loring 236 (sum 442, computed correctly).
  - Militia: about 1,500.
- **Hood attributions.** In the Peachtree Creek delay, Hood's text blames Hardee: "I was careful
  to call General Hardee's attention … This unfortunately was not attended to". The June 22
  note and the undated corps report on Kolb's Farm are correctly dated and distinguished.
- **Hardee attributions.** The telegrams and the 1865 report are dated per section. Hood's
  1,400, Hood's 5,247 and Hardee's "considerably exceeded 7,000" are correctly attributed as
  quotations or claims, and the period totals are kept as context.
- **Logan and Cleburne.** Logan's Dallas figures (379; 97 prisoners; over 300 buried; 2,000
  estimated) are correct. So are Cleburne's 85 killed, 363 wounded and 4,683 muskets.
  Kilpatrick's loss is correctly scoped to the whole August 18–22 raid.
- **Frozen and live fields.** Every frozen casualty, force, result and commander value quoted
  matches the CSV rows. Every live NPS field quoted matches the snapshots, including the zeros
  and the rank errors ("Lieutenant Colonel" Johnston, "Hugh" Kilpatrick).
