# Chattanooga-Ringgold Campaign: separate AI review, v1

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), `high` effort. This was a fresh-context
  subagent that did not see the author's conversation.
- **Date:** 2026-09-25.
- **Commits:**
  - Prepared commit: `450a5ba46975e7f117cbe542d2d87a7d51cd1dc9`.
  - Previous commit: `803bfc6477ef15d668307991dfa3862c18bd2540`.
  - Bundle and worktree HEAD: `535f423bb58446532607b85e1aeeaceca6f97216`.
- **Inputs:**
  - `assignment.md` sha256 `2f2b6f32c9441a091b41a2b420c5191618c201e28b16222b922f04327a69be17`.
  - `inputs.json` sha256 `76f8d2d500bb008889a0adf0eed439b99ba38ad27679409d443b498f03f395fc`.
  - All 37 bound paths match their hashes at `git show 450a5ba:<path>`, and each is
    byte-identical in the worktree. No mismatches were found.
- **Outcome: corrections required** (R1–R5). The advisory notes A1–A5 are optional.

This AI review is a separate analysis. It is not human historical adjudication,
independent corroboration or feature admission.

## Coverage actually inspected

- **Claims and citations.** I inspected all 18 claims and all 82 citation occurrences
  (TN024: 9 claims, 48 citations; GA005: 9 claims, 34 citations), including both null
  strength unknowns. For each claim I read the value, rationale, phase and status against
  the cited passages. Each record covers all seven dimensions.
- **Frozen rows.** I read the frozen battle, force and commander rows for TN024 and GA005,
  one commander per side. The cited cells match (forces_text, results_text, casualties_text,
  rank). Strength bounds are blank, and TN024 `other_names` is blank.
- **Texts read in full.**
  - Both NPS text summaries. Both replay exactly from the pinned HTML using the recorded
    HTMLParser transform.
  - The complete Bragg, Cleburne and Cist selections.
- **Selection replay.** All 11 selection ranges (Bragg 3, Cleburne 3, Cist 6) replay exactly
  against their parents. The parents are `or31-2-illinois-ocr-v1` and
  `cist-cumberland-ocr-v1`, which is `data/raw/heartland-v1/cist-full.txt`, sha256
  `4a3f4c2c…29`. It is unchanged, and its registry entry is unchanged.
- **Section boundaries.** I read the parent text around each boundary, and no section is
  truncated. Bragg's Davis dispatch is the first Addenda item. The Cleburne section runs from
  the Tunnel Hill heading through the signature.
- **Page markers.** I mapped every running head in the parents. The OR heads for pp. 664, 665,
  666, 667, 753–756 and 758 are explicit. Page 757 reads "1T&7" and p.758 reads "15 8". The
  Cist heads for pp. 244, 246–248 and 253–262 are explicit; p.261 reads "201". Cist has no
  p.243 or p.245 head.
- **Locators.** A script checked all 59 selection-citation page locators against that map, and
  all agree. The only locator that rests on a missing head is p.243 (R5).
- **Title and metadata.** I checked the OR title page, which has no imprint line, and the
  catalog metadata (`warofrebellion312unit`, v.31:2, 1880, not adopted).
- **Registry.** It has 564 records and 544 paths, against 555 and 535 previously. The previous
  555 entries are an identical prefix, and there are 9 new IDs.
- **Coverage counts.** There are 123/127 dossiers. The 4 without are TN027, TN028, TN029 and
  VA044. Of 36 campaign groups, 34 are complete.
- **Next group.** I confirmed Mine Run Campaign [November-December 1863], VA044 (start
  1863-11-27). The group after it is Dandridge, starting 1863-12-29.
- **Unchanged files.** Between the two commits, only `data/evidence/GA005.json` and
  `TN024.json` were added under the evidence directory. All 121 older dossiers and all
  history files are unchanged. The following are also unchanged:
  - the cohort;
  - both admission proposals;
  - admission-check, which shows `promoted_rows` 0 and no emitted rows;
  - `baseline.json` (23 battles, 13 groups, Brier 0.2768816348133779 versus 0.25);
  - `battles.json`;
  - the three CSVs.
- **Receipt.** All 229 input hashes, all 564 source hashes (the IDs match the registry) and all
  7 output hashes verify.
- **Packets.**
  - Each has three JSON blocks, and all parse.
  - The record block equals `battles.json`.
  - The draft block equals the dossier.
  - The registry block equals `data/sources.json`.
- **`make check`.** Run offline: 82 tests, OK, exit 0, `artifacts_written: false`. The
  worktree was clean afterwards.
- **Not done.** No build or packet commands were run, no network was used, and no new
  sources or print pages were consulted.

## Checks that pass

- **Scope.** The November 26 pursuit is kept outside both records.
- **Strength statements.** Bragg's "at least double" (Nov 20 dispatch, before the record) and
  "greatly outnumbered", Cist's 8,000 (a two-division bridgehead by the 24th) and "less than
  ten thousand" (Hooker at Lookout), and Cleburne's 4,157 (545+1,330+1,266+1,016, with
  "1 1,330" disclosed) are all attributed. None is adopted, and the unknowns stay null.
- **Responsibility dispute.** Bragg on the troops of the left and Cist on "without orders, and
  even against orders" are both attributed. Grant's remark is presented as Cist's
  retrospective quotation.
- **Ringgold Gap outcome dispute.** NPS's "five hours / failed" and Cist's "over an hour /
  driven from the pass" are both kept.
- **Casualties.** Cleburne's 20+190+11=221 is shown equal to the live figure, with the frozen
  480 retained and no derivation claimed.
- **Ranks.** The live ranks for Grant (Lieutenant General) and Bragg (Major General) are shown
  and not adopted.
- **Attribution.** There is no additive or automatic commander credit and no causal effect.
  Cist is labelled an interested Union staff history, and Bragg and Cleburne are labelled
  interested Confederate accounts.
- **OCR readings.** These are reported ("sis", "1 1,330", "201", "1T&7"), and the quotes keep
  the raw OCR.

## Required corrections

**R1: TN024 `casualty-records` and the memo. "Printed" 3,951 overstates what was inspected.**
The Cist source is OCR "not verified against print". The same `losses-and-captures` passage
has a digit discrepancy of the same kind. Sheridan's "135 killed, 1,151 wounded … aggregate
1,256" sums to 1,286. The two-division total "2,287" equals 1,286 + 1,001, where Wood's 1,001
is internally consistent. Whether the 3,951 comes from the OCR or from the print is therefore
unverified.

- **Value.** Replace "printed as an aggregate of 3,951 though the components sum to 2,951 (a
  computation here)" with: "with an aggregate that reads 3,951 in the unverified OCR, though
  the components sum to 2,951 (a computation here; OCR misreading versus misprint
  unresolved)".
- **Rationale.** Replace "Cist's printed aggregate does not match its components." with:
  "Cist's aggregate as read in the OCR does not match its components. In the same OCR
  paragraph Sheridan's aggregate reads 1,256 against components summing to 1,286, and the
  two-division total 2,287 equals 1,286 + 1,001. The print was not checked."
- **Memo.** In the `Disputes preserved` bullet, replace "Cist's printed aggregate of 3,951"
  with "Cist's aggregate of 3,951 as read in the unverified OCR".

**R2: TN024 `boundary_note` and the memo `Scope` bullet. The scope is misattributed.** The live
"Other Name" field lists only "Missionary Ridge, Lookout Mountain", and the frozen
`other_names` cell is blank. Orchard Knob's inclusion rests instead on the frozen November
23–25 interval and on the frozen and live descriptions: "On November 23-24, Union forces
struck out and captured Orchard Knob and Lookout Mountain."

- **Boundary note.** Replace "covering Orchard Knob, Lookout Mountain and Missionary Ridge as
  the live page's other names indicate." with: "covering Orchard Knob, Lookout Mountain and
  Missionary Ridge. The frozen and live descriptions place the first two on November 23–24 and
  the Missionary Ridge assault on November 25, within the frozen interval. The live page's
  other names list Missionary Ridge and Lookout Mountain; the frozen other_names cell is
  blank."
- **Memo.** Replace "as the live page's other names indicate" with the same basis.

**R3: TN024 `command-roles`. Two asserted elements have no cited passage.** The value says
Walthall's brigade was "not sustained by Stevenson" and that Bragg "credits … Cleburne", but
neither Stevenson nor Cleburne appears in any cited quote. Add the following two citations.
Both passages are in section `bragg-1863-11-30`, and I verified their positions against the
page heads.

- Stevenson: `{"source_id": "or31-2-bragg-chattanooga-selections-v1", "section":
  "bragg-1863-11-30", "locator": "p.664 (OCR page markers; not checked against print)",
  "quote": "The commander on that part of the field (Major-General Stevenson) had six brigades
  at his disposal."}`
- Cleburne: `{"source_id": "or31-2-bragg-chattanooga-selections-v1", "section":
  "bragg-1863-11-30", "locator": "p.666 (OCR page markers; not checked against print)",
  "quote": "Major-General Cleburne, whose command defeated the enemy in every assault on the
  25th,"}`

**R4: TN024 `ridge-works`. The `inherited` tag rests on a boundary inside the record.** The
rationale bounds the tag at "before the assault on the 25th". The frozen record opens on
November 23, so a Nov 25 boundary would let Nov 23–24 commander-created changes pass as
inherited. The tag remains supportable from Cist's "originally four lines" (already cited),
whose first line was taken on the 23d. However, Bragg's cited statements are post-assault
judgments, not state.

- **Rationale.** Replace it with: "Draft hypothesis relative to the frozen record's opening on
  November 23. Cist's 'originally four lines', the first taken on the 23d, and the natural
  slope place the works and ground before the record opens. Construction by Bragg's army
  before the campaign is neither credited nor excluded here. Bragg's skirmisher and
  exhaustion statements are his November 30 post-assault judgments, cited to describe the
  ground, not inherited state. Occupation and defence on the day are commander decisions not
  credited here. No map verification."
- **Memo.** In the `Tags` bullet, replace "in place before the November 25 assault" with "which
  Cist says were originally in place before the first line fell on November 23".

**R5: TN024 `plan-and-demonstrations`, citation 1. The locator claims a page marker that does
not exist.** The OCR has no p.243 head, because the Chapter XIV opening page carries no
running head (it falls between the "242" head and the "244" head). Replace the locator "p.243
(OCR page markers; not checked against print)" with: "p.243 (inferred: Chapter XIV opening
page has no running head in OCR, between the p.242 and p.244 heads; not checked against
print)".

## Advisory notes (no change required)

- **A1: GA005 `order-and-guides` and `check-the-pursuit`.** The quoted order reads "The general
  desires…" and is signed by Brent as Assistant Adjutant-General. Calling it "Bragg's" order
  relies on Brent's Army of Tennessee title and on Bragg's report heading. The rationale could
  say so.
- **A2: GA005.** Bragg's inspected report says the pursuit to "Binggold" was checked by
  "Major-General Cleburne and Briga- dier-General Gist, in command of their respective
  divisions". That bears on the frozen "one division [CS]" description. Leaving it uncited
  respects the three-family ceiling, but it could be recorded as an open question.
- **A3: TN024.** Cist's Sherman figure (1,989) and his Thomas figure both include Howard's
  command. The dossier does not sum them, which is correct. The overlap could be named.
- **A4.** The Cist `dependency_note` ("across five records"; Duke, Bragg, Buell) is shared
  boilerplate, now stale for every Cist record. Because source records are immutable, fixing
  it would take a versioned metadata revision, and nothing is needed for this batch.
- **A5.** The live TN024 title reads "Chattanooga III", and the live Date(s) field gives
  "November 1863". Neither is adopted, and neither needs a claim.

Finding IDs: R1, R2, R3, R4, R5, A1, A2, A3, A4, A5.
