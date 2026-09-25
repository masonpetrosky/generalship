# Morgan's Raid separate review: IN001, OH001, OH002

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), `high` reasoning effort. This was a separate subagent started with fresh context. It did not see the author's conversation.
- **Date:** 2026-09-25.
- **Commits:**
  - Prepared commit: `11c96f5d5ac5de7a6f31c3d76d36422283777360`.
  - Previous commit: `8546a8f6a53f671b2a91863e48b746dd1f03a777`.
  - Bundle and worktree HEAD: `5b83af9d3d8f715697f8656a11b5f9224ce0f311`.
- **Input hashes:**
  - `assignment.md` sha256 `4c1ccddeeb233914569faac21b080e0f7c0b9b07c78b931af0f272f950de70a0`.
  - `inputs.json` sha256 `a93d9d7d2aabbd5d364a14fb0a07f00e9c6dca050ed0260a7dea4f092461457e`.
  - All 42 bound paths match `git show 11c96f5:<path>`, with **no mismatch**.
  - Six paths differ in the worktree because of the out-of-scope commits `1a0ba8b` and `567e7b1`: README, `docs/roadmap.md`, `docs/sources.md`, `data/sources.json`, `artifacts/quality.json` and `artifacts/receipt.json`. I read their prepared-commit versions.
- **Status of this review:** it is an AI review, not human historical adjudication, independent corroboration or feature admission. I did no network access or new research, and spawned no agents. The only file I wrote is this review.

## Outcome: corrections required (MR-R1 to MR-R5)

All five are small extraction and wording corrections. No citation fails, no raid-wide figure is assigned or added to a record, and no disputes are hidden.

## Coverage actually inspected

### Dossiers and citations

- All 3 dossiers: 28 claims, 3 null unknowns and 143 citation occurrences. Each record has all seven dimensions. Counts are 9/1/45 for IN001, 9/1/51 for OH001 and 10/1/47 for OH002.
- Every quote was checked mechanically against its CSV cell or selected section:
  - 0 failures;
  - all 15 CSV citations resolve to exactly one row.
- Every non-CSV quote was also read in context for entailment, attribution, scope and phase.

### Frozen rows

- I read the frozen battle, force and commander rows for IN001, OH001 and OH002 in full.
- Frozen figures:
  - IN001: 400 / 1,800 people, with 360 / 41 casualties.
  - OH001: "Brigades:" 3,000 / 1,700 people, with 25 / 900 casualties.
  - OH002: 2,600 / 400 people, with casualties "none" / 364. The force row gives 0.
- The listed commanders are Jordan (Brevet Colonel), Hobson, Shackelford and J. H. Morgan (Brigadier Generals).

### NPS summaries

- I read all three NPS summaries in full.
- I replayed the HTMLParser transform from each pinned HTML file. All three texts reproduce byte-for-byte.

### Sectioned selections

- I replayed all four selections from their parents using the recorded half-open ranges and `split`/`join` whitespace collapse:
  - Duke: 8 sections;
  - Burnside: 4 sections;
  - Hobson: 2 sections;
  - Shackelford: 3 sections.
- Every section matches.
- I also inspected about 80 characters of parent text at each range boundary.
- `or23-1-illinois-ocr-v1` is unchanged: same record, same raw file hash `b26ba107…`, and no diff since `8546a8f`.

### Page-marker maps

- **Duke pp.407–461.**
  - The markers before each section confirm the opening pages: 407, 415 ("JUDAII CHECKED. 415"), 428, 431 ("CAPTAIN IIINES. - 431") and 446.
  - "45-1" (p.454) sits in the parent gap between the Buffington and last-days sections, after "…453".
  - "GETTING OUT OF A TRAP. 456" is a recto topic head between 454 and "456 HISTORY OF". The p.455 inference is sound.
  - "458 HISTORY OP" is p.458.
  - "(459) 0/ those who mude THEIE ESCAPE FROM OHIO…" is the plate caption. It is directly followed by "460 HISTORY OF".
  - Every Duke locator falls between the correct markers.
- **OR pp.635–662.** Markers found: 635, "63G" (636), 637, 638, 639, 640, 641, 642, "'643", 644, 645, 658, 659, 660, 661 and "1)62".
  - Every OR locator falls between the correct markers.
  - No locator depends on a missed or misread header, apart from the disclosed p.455 inference.

### Source metadata and documents

- I read the 12 new source records, the Duke catalog metadata fields and the Duke title page and preface.
- I read the memo, the Morgan's Raid passages in README, the roadmap, `docs/sources.md` and the report, plus the three packets.

### Not inspected

- The rest of either book.
- Maps, other reports, prisoner rolls and print.

## Required corrections

### MR-R1 (IN001): unsupported initials for Colonel Morgan

- **Problem:** Duke's Corydon passage says only "Colonel Morgan's advance guard" (p.435). None of IN001's citations supplies "[R. C.]".
  - The OR editors' bracket "[R. C.] Morgan" appears in the Hobson and Shackelford selections, which IN001 does not cite.
  - Those passages concern the July 19 surrenders. They do not identify the officer at Corydon.
- **Fix, `reported-force-scope` value:** replace "at Corydon he describes Colonel [R. C.] Morgan's advance guard and one regiment of the second brigade." with:
  > "at Corydon he describes a Colonel Morgan's advance guard (Duke gives no initials) and one regiment of the second brigade."
- **Fix, `command-roles` value:** replace "Duke attributes the Corydon attack to Colonel [R. C.] Morgan's advance guard and a regiment of the second brigade" with:
  > "Duke attributes the Corydon attack to a Colonel Morgan's advance guard (no initials in Duke's passage) and a regiment of the second brigade"

### MR-R2 (OH002 and memo): unsupported time-of-day labels for Salineville

- **Problem:** no inspected passage gives "morning" for Way's fight, or "afternoon" or "near New Lisbon" for the surrender.
  - NPS gives no time.
  - Duke's only "afternoon" in the selections is Garnettsville on July 7.
  - Shackelford gives this sequence: Hammersville "at daylight on Sabbath morning, the 26th"; five miles on; "Before reaching there, I learned of the fight between Major Way and the enemy"; about 7 miles on the New Lisbon road; the surrender at the fork (pp.643–644).
- **Fix, OH002 `boundary_note`:** replace its second sentence with:
  > "Shackelford's sequence places Major Way's fight, of which he learned after leaving Hammersville at daylight on July 26, before Morgan's surrender on the New Lisbon road the same day; no inspected source gives a clock time for either, and which the frozen record covers is not established."
- **Fix, memo "Salineville scope" bullet:**
  > "**Salineville scope.** Shackelford places Major Way's fight, learned of after he left Hammersville at daylight, before Morgan's surrender on the New Lisbon road; both fall on July 26 and no inspected source gives a clock time. Which of them the frozen record covers is not established."
- **Fix, memo strength bullet:** replace "Duke's 250 after Way's fight" with:
  > "Duke's 250 after 'a fresh disaster on the 2Gth' [OCR] (Duke does not name Way)"
- The OH002 dossier value already quotes Duke correctly.

### MR-R3 (OH001 `recorded-result`): Duke's escape figures are not eyewitness

- **Problem:** Duke says he was captured in the ravine during the withdrawal ("…and myself… soon afterward captured", p.452).
  - His "Between eleven and twelve hundred men retreated with Gen- eral Morgan" and the three hundred who crossed "about twenty miles above" (p.453) therefore describe events after his capture.
  - The source note's cut-off, "after July 19", understates this, and the claim does not flag it.
- **Fix:** append to the rationale:
  > "Duke was captured during the withdrawal from the valley (p.452); his figures for the men who retreated with Morgan and the three hundred who crossed above Buffington describe events after his capture and are not eyewitness."
- **Optional:** a future `metadata_only` revision could say "after his capture on July 19" instead of "after July 19". This review does not require one.

### MR-R4 (memo): Hobson's 5 or 6 are casualties, not deaths

- **Problem:** Hobson wrote "The casualties in my command did not ex- ceed 5 or 6" (p.661). The memo reads "Hobson gives 5 or 6 Union and 57 Confederate killed". The OH001 dossier states this correctly.
- **Fix, memo:** replace that bullet with:
  > "Buffington: casualties. Hobson says his command's casualties did not exceed 5 or 6 and gives 57 Confederate killed on the report of Dr. D. K. Scriver of the Ohio militia; Duke gives about 700 prisoners and some twenty-odd of his men killed by musketry, the Union losing 'quite as many'."

### MR-R5 (OH002 `dust-couriers-and-news` and OH001 `ammunition-and-horses`): missing timing scopes

**OH002.** Duke's dust passage (p.455, inferred) describes the march "back to- ward "Blennerhassett's Island,"" after a council during the six-day pursuit. It is not the July 26 action.
- **Fix, value:** replace "Duke says clouds of dust made the position of every column known to the others" with:
  > "Duke says that on an earlier march back toward Blennerhassett's Island, during the six-day pursuit, clouds of dust made the position of every column known to the others"
- **Fix, citation:** add
  - source: `duke-morgans-cavalry-ohio-raid-selections-v1`
  - section: `last-days-and-surrender`
  - locator: the same inferred p.455 locator
  - quote: `moved the column back to- ward "Blennerhassett's Island,"`
- **Fix, rationale:** append:
  > "Duke was then a prisoner; the dust passage is not specific to July 26."

**OH001.** Hobson's "over 800 miles" and "twenty-one days and nights" cover the whole pursuit, including the days after July 19. His broken-down horses are narrated with the events of July 14.
- **Fix, rationale:** append:
  > "Hobson's march distance and duration cover the whole pursuit, including days after July 19, and his horse breakdown is narrated with July 14; neither is a July 19 measurement or assigned to this record."

## Checks passed and optional notes

### Raid-wide figures

None is assigned to one record, and none is added:
- the start strength (NPS about 2,450; Duke 2,460 effective, exclusive of four guns);
- Burnside's 3,000;
- the July 2–26 return;
- NPS's 6,000 paroled;
- Duke's judgments. These are recorded as attributed judgments, not causal effects.

**Return arithmetic:** the OCR total row reads "1 18 3 44 8 74", and 1+18+3+44+8 = 74. The row has six numbers against seven columns, so one column is blank or lost in OCR. The return lists volunteer, regular, staff and garrison commands and no Indiana militia. It cannot account for Corydon's 360.

**Optional:** Duke's p.415 figure is placed "at the Cumberland crossing". The selected passage does not state this. It comes from the parent text immediately before the selection ("On the 2nd of July, the crossing of the Cumberland began…"). That is acceptable because the parent is pinned.

### Force scopes

These are kept separate, with none adopted as a matched opening strength:

| Record | Figure | Source and scope | Frozen bound |
| --- | ---: | --- | --- |
| OH001 | 1,900 | Duke | 1,700 |
| OH001 | 250 each | Duke, two engaged regiments | — |
| OH001 | 2,500 | Hobson, July 6 at Lebanon | — |
| OH002 | 500 | Shackelford, July 21 | 2,600 / 400 |
| OH002 | 375 | Shackelford, Rue's men | 2,600 / 400 |
| OH002 | about 400 | Shackelford, crossing the railroad | 2,600 / 400 |

The OCR readings "Hobsoii", "Bue" and "2Gth" are kept in the quotes. Normalizing names in paraphrase is fine.

### Casualties

- IN001: frozen 401 (CS 41) against live 411 (CS 51). Both are internally consistent with US 360.
- OH002: 350 and 230 against 364 are kept unreconciled, and the Union zero is not treated as a measured absence.

**Optional (OH001):** the value's "militia surgeon" goes slightly beyond the text, which says "Dr. D. K. Scriver, of the Ohio militia".

### Disputes

These remain visible and attributed:
- the Buffington escape counts;
- Hobson's protest at Judah's assumption of command (p.661);
- the Burbeck surrender, with Duke on pp.457–458 against Shackelford's "unfair and illegal" on p.644.

No listed commander receives automatic credit, and the frozen rank "Brevet Colonel" is kept instead of the live "Colonel".

Duke's own statements are supported:
- he was not present at the conference with Bragg ("I was not present at the interview", p.410);
- he commanded a brigade ("two regiments of my brigade", p.448).

**Optional (OH001 `ford-valley-and-river`):** "two heavy guns" and "commanded the ford" are supported only by uncited text on p.447 ("two heavy guns were mounted in it." and "the work, which commanded the ford"). Citing them would close the gap.

**Deferred, not an error:** Shackelford's unused July 19–20 figures bear on the escape question but are left for later work: about 700 captured on the 19th, and on the 20th Morgan "with a detachment of about 600" escaping while 1,200–1,300 were captured.

### Metadata

- The Duke metadata is correct: the identifier, NYPL contributor, MSN sponsor, the 1867 Cincinnati imprint, and the 1866 copyright held by Henrietta Morgan.
- **Inherited OR edition issue:** confirmed. "1889." begins at parent offset 1084, just after the title range ends at 1081. The primary's planned `metadata_only` revisions for the three Morgan's Raid OR selections are the right fix, so no separate finding is needed.

### Repository state at `11c96f5`

- **Coverage:**
  - 105/127 dossiers, 22 without;
  - 26/36 complete campaign groups by presence.
- **Source registry:**
  - 486 records / 476 paths;
  - the first 474 records (464 paths) are byte-identical to `8546a8f`;
  - all 486 raw hashes match.
- **Unchanged files:** no diff to any older dossier, `data/evidence/history`, the cohort, either admission proposal, `admission-check.json`, `baseline.json` or `battles.json`.
- **Baseline:** 23 battles / 13 groups, Brier 0.2768816348133779 against 0.25, with 0 promoted rows.
- **Next group:** the next incomplete group is Chickamauga Campaign [August-September 1863] (GA003, GA004, TN018), first dated 1863-08-21.
- **Packets:** the three JSON blocks parse. The existing-draft blocks equal the dossiers, and the registry blocks equal `data/sources.json`.
- **Receipt:** all 486 source hashes and 184 file hashes match.

### `make check`

Run offline in this worktree at `5b83af9`: 82 tests OK, `check` exited 0 with 105 draft dossiers and 0 admission-promoted rows, and it wrote no artifacts.
