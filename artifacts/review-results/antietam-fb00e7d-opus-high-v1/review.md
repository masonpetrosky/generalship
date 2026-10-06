# Antietam (MD003): separate source review

- Reviewer: `evidence-reviewer` subagent, Claude Opus 5.5 (`claude-opus-5-5`), effort `high`,
  fresh context. The author's conversation was not an input.
- Date: 2026-10-05/06 (the session crossed midnight).
- Prepared commit: `fb00e7da75b1a21d10033f2dde39379c45949ce0`. The worktree HEAD was `379da81`,
  which only adds the two review-assignment folders (Antietam and Champion Hill).
  `data/evidence/MD003.json` is byte-identical between `4547657` and `fb00e7d`.
- Input hashes: I recomputed all 22 SHA-256 values in `inputs.json`, both in the worktree and
  from `git show fb00e7d:<path>`. All 22 match. These include MD003.json `3b9432c4…1bc7`,
  nps-md003.txt `d71c7a98…4e4` (it also matches its `data/sources.json` entry) and
  cwsac_battles.csv `952b5d08…585f1f`.
- Status: this is an AI review. It is not human historical adjudication, independent
  corroboration or feature admission.

## Coverage I actually inspected

- **The dossier:** all 9 claims, including the 5 null unknowns, and all 5 citation occurrences.
  I also checked the boundary note, the null replacement dates, the 3 open questions and
  coverage of all seven dimensions.
- **The snapshot:** the whole of `data/raw/nps-md003.txt` (22 lines), plus its
  `snapshot_transform` note. It is normalized HTMLParser text, not the original HTML.
- **CWSAC battles:** the whole MD003 row of `cwsac_battles.csv` (row 103), every column.
- **CWSAC forces and commanders, for context:** both MD003 rows of each file. The forces rows
  (204–205) are blank in every value column. The commanders rows (232–233) are Robert E. Lee,
  "General", and George B. McClellan, "Major General".
- **Repository guidance:** AGENTS.md, the README status section, the methodology review
  passages, the roadmap's Maryland and Antietam passages, the evidence contract, the "Live NPS
  evidence snapshots" section of `docs/sources.md`, the quote validator in
  `generalship/evidence.py` (non-blank, exact-substring match) and the MD003 assertions in
  `tests/test_evidence.py`.
- **Calibration:** the reviewed MD002 and WV016 outcome, terrain and responsibility claims, read
  for consistency only.
- **Not inspected:** Palfrey, the other Maryland sources, the Champion Hill review, the network
  and any new source family.

I ran `make check` offline. It exited 0 after running 151 tests with no failures. The baseline
is unchanged: **23 eligible battles in 13 campaign groups**, with battle-weighted Brier
**0.2768816348133779** against equal odds at **0.25**, and `admission_promoted_rows: 0`.
`git status` was clean before I wrote this file.

## Findings by claim

- **`zero-sentinel`: correct.** The snapshot's Forces Engaged line reads `0 total (US 0; CS 0;)`.
  - The `disputed` status and the rationale correctly decline to treat this as a measured count.
  - The frozen CWSAC row has `forces_text` = "Armies" and a blank `strength`. Both MD003 force
    rows are blank, and the test asserts the US strength is null. The frozen record therefore
    has missing strength, not zero strength, and nothing in the pipeline uses the zeros.
  - The blank cells cannot be quoted, because the validator rejects blank quotes. See advisory A1.
- **`force-narrative`: correct.** The quote is exact. The claim attributes it to "the same page",
  gives no number, and the rationale rejects reading it as a count.
  - The NPS narrative does not state the population behind "two-to-one" (present, available or
    engaged). See advisory A2.
  - The identical sentence appears in the CWSAC `description` cell. That is a copy within the
    same family, and the dossier correctly does not present it as corroboration.
- **`recorded-result`: correct in what it states, but incomplete (R1).** The frozen `result`
  value "Inconclusive" is cited exactly and kept, and NPS "Indecisive" is cited exactly.
  - The frozen `results_text` cell reads "Inconclusive (Union strategic victory.)". The value
    describes "the imported CWSAC record" but leaves out the strategic label that the record
    carries.
  - The rationale's "campaign result" therefore refers to an uncited label that is actually in
    the cited row. The live NPS field omits that label.
  - "Inconclusive" and "Indecisive" do not conflict materially, so `supported` can stand. The
    strategic label is a different scope from the tactical result, and its absence from the
    live field is an omission, not a contradiction.
- **`withdrawal`: attribution correct.** The NPS quote is exact. The text is ordered so that
  "After dark" follows skirmishing "throughout the 18th". That places the order on the night of
  18 September, which matches the frozen end date of 1862-09-18.
  - The value says "withdrawing", but the passage records that Lee *ordered* the withdrawal.
    The timing is also left out. Neither is a misstatement. See advisory A3.
  - The `post_outcome` tag is a reasonable hypothesis while the boundaries are unset. The
    withdrawal falls at the very end of the frozen engagement window, and the tag needs the
    boundary review the boundary note already requires.
- **Phase tags.** `unresolved` on the strength and unknown claims, and `post_outcome` on the
  outcome claims, are hypotheses consistent with the contract's rule for unset boundaries. None
  is presented as a reviewed causal classification.
- **Independence.** Nothing in the dossier presents NPS–CWSAC agreement as independent
  corroboration. The two outcome citations are framed as two records in the same group.
- **Unknowns.**
  - **Terrain (R2):** the snapshot names the features of the field, so "not established by the
    sources inspected" is inaccurate for this dimension.
  - **Responsibility (R3):** the snapshot names the principal commanders and attributes the
    commitment decisions to them, so the same rationale is inaccurate here.
  - **Information:** the unknown should stand. No passage concerns intelligence, reports or
    either side's knowledge.
  - **Objectives:** the unknown should stand. No passage states either side's aims. The
    CWSAC row gives only the campaign name.
  - **Logistics:** the unknown should stand. Only "removing his wounded south of the river"
    comes close, and a post-combat casualty evacuation does not characterize supply or movement
    capacity.
- **Boundary note and open questions.** All remain accurate and should be retained. A dossier
  kept from 2026-09-20 does not supersede the frozen row.

## Required corrections

These three corrections leave 9 claims and 3 null unknowns (logistics, information and
objectives), and raise the citation occurrences from 5 to 13. Every new quote was checked as an
exact, single-occurrence substring of the named cell or snapshot. Under the contract's
stable-ID rule, the primary may keep the old IDs in R2 and R3 instead of renaming them.

### R1 — `recorded-result`: add the frozen `results_text` and scope the labels

Keep the `id`, `dimension`, `phase` (`post_outcome`), `status` (`supported`) and both existing
citations. Replace `value` and `rationale`, and add one citation:

```json
"value": "The frozen CWSAC result is Inconclusive; its result text adds a Union strategic victory. The NPS page as retrieved on 2026-09-20 gives Indecisive and does not carry the strategic label.",
"rationale": "Retain the frozen result value Inconclusive. The parenthetical is a strategic label, not a tactical result: do not relabel the tactical outcome to fit it, and do not read the live page's omission as a contradiction. All three cells are in the nps-cwsac group, so they are not independent corroboration.",
```

Add this as the second citation:

```json
{"source_id": "arnold-cwsac-battles", "row_key": {"battle": "MD003"}, "column": "results_text", "quote": "Inconclusive (Union strategic victory.)"}
```

### R2 — replace `terrain-unknown` with a narrow supported claim

```json
{
  "id": "named-terrain",
  "dimension": "terrain",
  "value": "NPS places the fighting at Miller's cornfield, the Dunker Church and the Sunken Road, and has Burnside's corps crossing the stone bridge over Antietam Creek.",
  "phase": "unresolved",
  "status": "supported",
  "rationale": "A modern NPS narrative that names features but does not describe ground, cover or their tactical effect, which remain unknown. It also does not show that any commander chose or created these conditions.",
  "citations": [
    {"source_id": "nps-md003", "locator": "Description", "quote": "Attacks and counterattacks swept across Miller's cornfield and fighting swirled around the Dunker Church"},
    {"source_id": "nps-md003", "locator": "Description", "quote": "Union assaults against the Sunken Road eventually pierced the Confederate center"},
    {"source_id": "nps-md003", "locator": "Description", "quote": "crossing the stone bridge over Antietam Creek"}
  ]
}
```

### R3 — replace `responsibility-unknown` with attributed command roles

```json
{
  "id": "army-command-decisions",
  "dimension": "responsibility",
  "value": "NPS lists McClellan (US) and Lee (CS) as principal commanders and displays both as Major General. Its narrative attributes the commitment decisions to them: Lee committed his entire force, while McClellan sent in less than three-quarters of his army and did not renew the assaults.",
  "phase": "unresolved",
  "status": "supported",
  "rationale": "This is a modern NPS narrative attribution, not a contemporary record. It names army-level decisions; it does not measure each commander's contribution. NPS's 'enabling Lee to fight the Federals to a standstill' remains its interpretation, not an established causal effect. The corps and division actions it names (Hooker, Burnside, A.P. Hill) are not attributed to the army commanders. The displayed rank is a structured field that needs scrutiny: the frozen arnold-cwsac-commanders row gives Lee as General.",
  "citations": [
    {"source_id": "nps-md003", "locator": "Principal Commanders", "quote": "Major General George McClellan [US]"},
    {"source_id": "nps-md003", "locator": "Principal Commanders", "quote": "Major General Robert Lee [CS]"},
    {"source_id": "nps-md003", "locator": "Description", "quote": "Lee committed his entire force, while McClellan sent in less than three-quarters of his army"},
    {"source_id": "nps-md003", "locator": "Description", "quote": "McClellan did not renew the assaults."}
  ]
}
```

## Advisory notes (not required)

- **A1 — `zero-sentinel`.** The primary may add
  `{"source_id": "arnold-cwsac-battles", "row_key": {"battle": "MD003"}, "column": "forces_text", "quote": "Armies"}`.
  The rationale could then add: "The frozen CWSAC row has no numeric strength (blank
  `strength`, blank force rows); a missing value is not a zero." This does not establish where
  the live zeros come from, so open question 3 still stands.
- **A2 — `force-narrative`.** The primary may append to the rationale: "NPS does not state
  whether the two-to-one ratio refers to present, available or engaged troops."
- **A3 — `withdrawal`.** A more precise value would be: "NPS records that after dark, following
  skirmishing throughout the 18th, Lee ordered the Army of Northern Virginia to withdraw across
  the Potomac." It would add the citation
  `{"source_id": "nps-md003", "locator": "Description", "quote": "Lee continued to skirmish with McClellan throughout the 18th"}`.
- **A4 — casualty records.** The inspected sources disagree on casualties, and the dossier does
  not record it:
  - NPS Estimated Casualties reads `22700 total (US 12400; CS 10300;)`.
  - The frozen CWSAC `casualties_text` reads `23,100 total`.
  - The CWSAC force rows have no casualty values.

  For consistency with the reviewed MD002 and WV016 `casualty-records` claims, the primary may
  add an `outcome` claim with status `disputed` and phase `post_outcome`. It would cite both
  strings, at locator `Estimated Casualties` and column `casualties_text`, and say they are
  same-group records that are not averaged or reconciled.
- **A5 — time scope.** "Live" and "current" in `zero-sentinel` and `recorded-result` mean the
  2026-09-20 retrieval. Saying so would keep the claims true if the page changes later.
- **A6 — A.P. Hill.** The arrival of A.P. Hill's division from Harpers Ferry during the battle
  is relevant to the open question about present versus engaged strength. It needs no claim in
  this first pass.

## Outcome

There are **3 required corrections**: R1 adds the frozen result text, and R2 and R3 replace two
unknowns the inspected snapshot can partly answer. None of them changes the frozen `result`
value, the zero-sentinel handling, the phase hypotheses or the open questions. The remaining
three unknowns should stand. The baseline is unchanged and no rows are promoted. The primary
should check each correction against the sources before applying it. The dossier remains a
draft.
