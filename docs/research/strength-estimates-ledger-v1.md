# Best-estimate side strength: ledger v1

Prepared 2026-09-25 under the [best-estimate design](../strength-estimates.md). The owner
accepted that design at `5151b57`; the bound design file still reads "Status: proposed",
because editing it would break the ledger's design binding.

**Status: reviewed and reconciled.** Five separate Claude Opus 5.5 `high` reviews (four
campaign batches and the engine) are recorded under `artifacts/review-results/est-review-*`.
Every required finding was applied after the primary checked it against the passages. No
model has been fitted, no feature is admitted, and the frozen baseline is unchanged. A fit
needs an explicit owner authorization naming the reviewed ledger's hash (design §6).

## Result

The ledger `data/estimates/side-strength-v1.json` covers:

- all 91 decisive, non-aggregate frozen engagements, with both sides each;
- the other 36 records, listed as out of scope with their reason.

`python3 -m generalship estimate-check` replays every estimate from its recorded inputs. It
also runs in `make check`.

| Measure | Count |
| --- | ---: |
| Sides graded A / B / C / D (of 182) | 59 / 21 / 26 / 76 |
| Engagements with an estimate for both sides | 43 |
| Fit-eligible rows, both sides grade A | 21 |
| Fit-eligible rows, both sides A or B | 29 |
| Fit-eligible rows, both sides A, B or C | 37 |
| Rows excluded as `post_start_information` | 7 (6 with both sides estimated, plus WV010, whose Confederate side is grade D) |
| Fit-eligible rows (A–C) that are also frozen baseline rows | 21 of 23 |
| Newly covered fit-eligible rows (A–C) | 16 |

**What changes from the frozen baseline.**

- **Coverage grows by about 60 per cent.** 43 decisive engagements have an estimate for both
  sides; 37 of them are fit-eligible at grades A–C (6 are excluded as
  `post_start_information`), against 23 frozen rows.
- **Two frozen rows drop out.**
  - **Gaines' Mill (VA017).** Its frozen Confederate figure, 57,018, is Livermore's total, and
    that total adds later losses.
  - **Cedar Mountain (VA022).** Livermore's p.87 note 4 (page image) says a Union division
    engaged after dark, and three Confederate brigades, are left out of his totals. The frozen
    Union 8,030 equals his total, so it groups with it and becomes a lower bound only. The
    Union side is grade D.
- **Some baseline rows become grade B.** The frozen CWSAC figure groups with Livermore's
  identical figure on a different basis (design rule 2), and the combined figure gets an
  `unknown` basis. This affects Beaver Dam Creek and the Gettysburg Union side. The Gettysburg
  Confederate side is also B: Livermore's effectives line is an intermediate figure before his
  prior-loss deduction, so it is `engagement_link_unknown`.
- **Chancellorsville (VA032) becomes grade C.** Its frozen pair equals Livermore's composite
  Chancellorsville-and-Fredericksburg entry, which also covers the separate Salem Church and
  Fredericksburg II records. The remaining figures are Doubleday's whole-army totals: Forbes's
  records-based 114,500 and 62,000, with scope unresolved.

**The 76 grade D sides stay blank.** 57 have no usable figure at all. The other 19 carry only
bounds, parts of the force or figures for another action; each has its reason recorded. Many
small cavalry, naval and garrison actions therefore still have no row.

## Extraction record

- **Sources.** The inputs come only from registered sources:
  - first-pass dossier citations;
  - the frozen CWSAC forces rows;
  - a new registered transcription of the Livermore entries
    (`livermore-transcription-v1`), made from the 25 pinned page images, because the OCR
    merges note markers into figures. It is a declared exception under design §2: rule 2
    names Livermore, and the transcription is derived from registered images.
  - One quote from a registered, already-cited selection that no dossier citation carries:
    MD002 `cs-mcclellan`, McClellan's "probably some thirty thousand in all" for the
    Confederates, from the same Palfrey `south-mountain` section as the dossier's Union
    figure. The primary read design §2's source scope (registered sources) as allowing it.
    The batch 2 reviewer noted that a narrower reading would drop the input and leave that
    side grade D.
- **Inventory.** Every strength claim, every typed quantity (Shiloh) and every frozen CWSAC
  figure is referenced by an input or recorded with a reason. Livermore entries list their
  entered lines and why the rest were not entered, including footnote figures read from the
  page images. The checker verifies that every input ID named in an inventory exists.
- **Extractor policies,** recorded in the ledger:
  - Secondary histories are compiled totals for either side, unless the passage shows an
    opponent's estimate.
  - NPS and CWSAC force cells carry the engaged table basis and `derivation_unknown`; NPS
    zero cells are not counts.
  - A commander's own figure relayed by a compiler keeps the own-report role.
  - Pre-engagement figures (plans, departures, earlier returns) are
    `engagement_link_unknown` unless the source ties them to the force brought.
- **Implementation choices,** checked by the reviews:
  - The ledger binds the metadata and raw hashes of every **cited** source, not the whole
    registry. Adding unrelated sources then does not break replay, while any change to a
    cited source does. Design §7 says "the source registry snapshot"; this narrower binding
    is recorded as a deliberate choice.
  - NPS narrative restatements whose basis is unstated (IN001 US, OH002 Confederate, TN015
    US, TN006 Confederate) are not recorded as reproductions; linking would merge an
    engaged-basis figure with an unstated one. The engine review also named KY009 US
    `us-nps-desc` as a linked same-basis restatement. The batch 2 review then found that one
    to be a one-sided bound ("nearly 55,000"), and TN006's to have an unstated basis, so
    neither is linked now. An unlinked restatement counts as a second candidate, so those
    four sides lack `single_input`. That is reported, not corrected; counting them once
    would need a design revision.
  - A part of a side's force is a lower bound (`bound: lower`), never an upper bound: a cap
    on one part does not cap the whole side. Such caps are recorded with `bound: null`.
  - An opponent candidate that sets `high` under rule 5 counts as used for the range, so its
    §5 labels apply (engine review R1). A post-start opponent figure that sets `high`
    therefore excludes the row from the fits.
  - `basis_mixed` is set only when both sides have a point; a grade D side makes the row
    incomplete anyway.

Extraction is not blind (design §2). The per-engagement inventory is the structural
mitigation, and separate review checks classifications, grades and completeness.

**Known transcription gaps.** `livermore-transcription-v1` omits several notes and lines that
the page images carry:

- p78–79 most of note 4, and p79 note 3 figures (44,895; 1,000; 5,463);
- p84–85 (composite entry) deduction and subtotal lines;
- p87 notes 1–4, 6 and 7;
- p90 entry lines (Rosser's cavalry 700, 12,984, the Toombs deduction and 17,214) and note 3;
- p91 in full;
- p95 notes 1 and 2 (truncated);
- p98 note 2 (truncated);
- p99 notes 2–3 and the end of note 4;
- p100 lines, including the Union 42,315 and the Confederate component lines;
- p103 note 1.

The reviews read these from the page images, and the ledger records the relevant figures in
its inventories or as coding reasons (TN002, VA017, VA022, MD002, KY009, MS009, PA002, GA004,
TN024). The
registered transcription is immutable; filling the gaps needs a versioned successor, which is
deferred.

## Estimates by engagement

Each cell gives the grade, the point, the plausible range and the point's basis. "—" is
grade D. "Best row set" names the widest grade set the row belongs to, or why it is out of
the fits.

| KY005 Middle Creek | — | C 1,880 (1,250–2,500) unknown | incomplete |
| KY006 Mill Springs | — | A 5,000 (4,750–5,250) engaged | incomplete |
| TN001 Fort Henry | C 17,000 (11,900–22,100) unknown | C 2,100 (1,400–2,800) unknown | ABC |
| NC002 Roanoke Island | A 7,500 (7,130–7,880) engaged | A 3,000 (2,850–3,150) engaged | A |
| TN002 Fort Donelson | C 27,000 (18,900–35,100) unknown | B 13,000 (11,050–21,000) unknown | excluded (post-start) |
| MO012 New Madrid/Island No. 10 | — | — | incomplete |
| NC003 New Berne | — | — | incomplete |
| NC004 Fort Macon | — | B 500 (430–580) unknown | incomplete |
| VA101 Kernstown, First | A 8,500 (8,080–8,930) engaged | A 3,800 (3,230–3,990) engaged | A |
| TN003 Shiloh | A 62,680 (59,550–68,340) engaged | A 44,970 (42,720–47,220) engaged | A |
| MS016 Corinth | C 120,000 (84,000–156,000) unknown | C 37,500 (25,000–70,000) effective | ABC |
| VA102 McDowell | A 6,500 (6,180–6,830) engaged | A 6,000 (5,700–6,300) engaged | A |
| VA012 Drewry's Bluff | — | — | incomplete |
| WV009 Princeton Court House | — | — | incomplete |
| VA103 Front Royal | A 1,060 (1,010–1,120) engaged | A 3,000 (2,850–3,150) engaged | A |
| VA104 Winchester, First | A 6,500 (6,180–6,830) engaged | A 16,000 (15,200–16,800) engaged | A |
| VA013 Hanover Court House | — | — | incomplete |
| NC006 Tranter's Creek | — | — | incomplete |
| TN004 Memphis | — | — | incomplete |
| TN005 Chattanooga | — | — | incomplete |
| VA105 Cross Keys | A 11,500 (10,930–12,080) engaged | A 5,800 (5,510–6,090) engaged | A |
| VA106 Port Republic | A 3,500 (3,330–3,680) engaged | A 6,000 (5,700–6,300) engaged | A |
| VA016 Beaver Dam Creek | B 15,630 (13,290–17,980) unknown | B 16,360 (13,900–18,810) unknown | AB |
| VA017 Gaines' Mill | B 36,790 (29,080–42,310) pfd | C 57,020 (39,910–74,120) unknown | excluded (post-start) |
| VA021 Malvern Hill | — | — | incomplete |
| TN006 Murfreesboro | A 900 (860–950) engaged | A 1,400 (1,330–2,100) engaged | A |
| VA022 Cedar Mountain | — | B 22,500 (19,130–25,880) unknown | incomplete |
| VA025 Thoroughfare Gap | — | — | incomplete |
| VA026 Manassas, Second | — | — | incomplete |
| KY007 Richmond | B 6,500 (5,530–8,050) unknown | A 6,850 (6,510–12,600) engaged | AB |
| WV010 Harpers Ferry | C 11,000 (7,700–14,950) unknown | — | excluded (post-start) |
| KY008 Munfordville | — | — | incomplete |
| MD002 South Mountain | C 30,000 (21,000–39,000) engaged | C 22,500 (15,000–30,000) unknown | ABC |
| MS001 Iuka | A 4,250 (4,040–9,450) engaged | A 3,200 (3,040–14,700) engaged | A |
| WV016 Shepherdstown | — | — | incomplete |
| MS002 Corinth | A 23,000 (21,850–24,150) engaged | B 22,000 (18,700–25,300) unknown | AB |
| TN007 Hatchie's Bridge | — | — | incomplete |
| KY009 Perryville | A 55,000 (52,250–57,750) engaged | A 16,000 (15,200–16,800) effective | A |
| TN008 Hartsville | A 2,000 (1,900–2,100) effective | — | incomplete |
| VA028 Fredericksburg I | A 100,010 (95,010–119,690) engaged | A 72,500 (68,870–76,120) engaged | A |
| NC007 Kinston | C 22,500 (15,000–30,000) unknown | B 2,000 (1,700–6,000) unknown | excluded (post-start) |
| NC009 Goldsborough Bridge | — | — | incomplete |
| TN009 Jackson | — | A 400 (380–2,210) engaged | incomplete |
| MS003 Chickasaw Bayou | A 30,720 (29,180–33,600) effective | C 13,790 (9,650–17,930) engaged | excluded (post-start) |
| TN010 Stones River | A 45,000 (41,230–47,250) engaged | A 34,730 (33,000–53,590) effective | A |
| TN011 Parker's Cross Roads | A 3,000 (2,850–3,150) engaged | — | incomplete |
| AR006 Arkansas Post | B 28,940 (24,600–33,290) effective | A 3,000 (2,850–7,000) effective | AB |
| TN012 Dover | A 800 (570–840) engaged | A 2,500 (2,380–2,940) engaged | A |
| TN013 Thompson's Station | — | B 10,000 (8,500–11,500) unknown | incomplete |
| NC010 Fort Anderson | — | C 12,000 (8,400–15,600) unknown | incomplete |
| TN014 Vaught's Hill | A 1,300 (1,240–1,370) engaged | A 3,500 (3,330–3,680) engaged | A |
| TN015 Brentwood | A 400 (380–420) engaged | — | incomplete |
| TN016 Franklin | — | — | incomplete |
| MS004 Grand Gulf | — | C 4,700 (3,290–6,110) unknown | incomplete |
| MS005 Snyder's Bluff | — | — | incomplete |
| AL001 Day's Gap | A 2,000 (1,900–2,200) engaged | — | incomplete |
| VA032 Chancellorsville | C 114,500 (80,150–161,850) effective | C 62,000 (43,400–80,600) unknown | ABC |
| MS006 Port Gibson | B 23,000 (19,550–26,450) unknown | B 5,500 (4,680–5,500) unknown | AB |
| VA033 Salem Church | — | — | incomplete |
| VA034 Fredericksburg II | — | — | incomplete |
| MS007 Raymond | — | A 2,500 (2,380–2,630) engaged | incomplete |
| MS008 Jackson | — | B 6,000 (5,100–13,800) unknown | incomplete |
| MS009 Champion Hill | B 29,370 (24,970–35,600) effective | A 20,000 (16,630–24,150) effective | AB |
| MS010 Big Black River Bridge | — | B 4,000 (3,400–4,600) unknown | incomplete |
| MS011 Vicksburg | C 71,140 (49,800–92,480) unknown | A 20,000 (19,000–21,000) effective | excluded (post-start) |
| LA011 Milliken's Bend | B 1,060 (900–1,220) unknown | C 2,030 (1,350–2,700) unknown | ABC |
| VA107 Winchester, Second | A 7,000 (6,650–7,350) engaged | A 12,500 (11,880–13,130) engaged | A |
| TN017 Hoover's Gap | — | — | incomplete |
| PA002 Gettysburg | B 83,290 (70,800–95,780) unknown | B 75,050 (63,800–86,310) engaged | AB |
| AR008 Helena | B 4,130 (3,510–4,750) unknown | A 7,650 (7,260–15,000) engaged | AB |
| IN001 Corydon | A 400 (380–420) engaged | A 1,800 (1,710–3,000) engaged | A |
| OH001 Buffington Island | A 3,000 (2,850–3,150) engaged | A 1,700 (1,620–1,790) engaged | A |
| OH002 Salineville | A 2,600 (2,470–2,730) engaged | A 400 (380–420) engaged | A |
| TN018 Chattanooga | — | — | incomplete |
| GA003 Davis' Cross Roads | C 3,380 (2,250–13,500) unknown | C 30,000 (21,000–39,000) unknown | ABC |
| GA004 Chickamauga | A 55,000 (52,250–61,130) effective | A 66,330 (63,010–69,640) engaged | A |
| TN019 Blountsville | — | A 1,200 (1,140–1,260) engaged | incomplete |
| TN020 Blue Springs | — | — | incomplete |
| VA040 Bristoe Station | — | — | incomplete |
| VA042 Buckland Mills | — | — | incomplete |
| TN021 Wauhatchie | — | — | incomplete |
| TN022 Collierville | A 850 (810–890) engaged | A 2,500 (2,380–2,630) engaged | A |
| WV012 Droop Mountain | C 5,250 (3,500–7,000) engaged | A 1,700 (1,620–4,000) engaged | ABC |
| TN023 Campbell's Station | — | C 20,000 (14,000–26,000) unknown | incomplete |
| TN024 Chattanooga | A 56,360 (53,540–59,180) engaged | C 44,010 (30,810–57,210) pfd | excluded (post-start) |
| GA005 Ringgold Gap | — | — | incomplete |
| TN025 Fort Sanders | C 12,000 (8,400–15,600) effective | C 16,130 (10,750–21,500) unknown | ABC |
| TN026 Bean's Station | B 4,000 (3,400–4,600) unknown | — | incomplete |
| TN027 Mossy Creek | — | C 2,000 (1,400–2,600) engaged | incomplete |
| TN028 Dandridge | — | — | incomplete |
| TN029 Fair Garden | — | — | incomplete |

Row sets: `A` is both sides grade A; `AB` is both sides A or B; `ABC` is both sides A, B or
C. Ranges are plausible ranges, not probability intervals. Points and ranges are rounded to
10 for storage, which does not imply that precision.

## Reviews

| Review | Scope | Required findings | Bundle |
| --- | --- | --- | --- |
| est-review-b1 | 25 engagements, KY005 to VA021 | R1–R7 | `artifacts/review-results/est-review-b1-4fd1b51-opus-high-v1` |
| est-review-b2 | 22 engagements, TN006 to AR006 | R1–R10 | `artifacts/review-results/est-review-b2-4fd1b51-opus-high-v1` |
| est-review-b3 | 23 engagements, TN012 to AR008 | E3-R1–E3-R10 | `artifacts/review-results/est-review-b3-4fd1b51-opus-high-v1` |
| est-review-b4 | 21 engagements, IN001 to TN029 | R1–R7 | `artifacts/review-results/est-review-b4-4fd1b51-opus-high-v1` |
| est-review-engine | engine, checker, tests and memo | R1–R3 | `artifacts/review-results/est-review-engine-4fd1b51-opus-high-v1` |

Each bundle keeps the reviewer's response, the dispatch record, the correction list and the
primary's assessment. These are AI reviews: separate analyses, not human historical
adjudication or proof of source independence.

## Next

The owner decides whether to authorize the locked evaluation (design §6), naming the
reviewed ledger's SHA-256. Until then nothing is fitted.
