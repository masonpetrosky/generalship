# Best-estimate side strength: ledger v1

Prepared 2026-09-25 under the accepted [best-estimate design](../strength-estimates.md).
**Status: a draft ledger awaiting separate review in campaign batches.** No model has been
fitted, no feature is admitted, and the frozen baseline is unchanged. A fit needs the reviewed
ledger and an explicit owner authorization naming its hash (design §6).

## Result

The ledger `data/estimates/side-strength-v1.json` covers:

- all 91 decisive, non-aggregate frozen engagements, with both sides each;
- the other 36 records, listed as out of scope with their reason.

`python3 -m generalship estimate-check` replays every estimate from its recorded inputs. It
also runs in `make check`.

| Measure | Count |
| --- | ---: |
| Sides graded A / B / C / D (of 182) | 62 / 25 / 23 / 72 |
| Fit-eligible rows, both sides grade A | 21 |
| Fit-eligible rows, both sides A or B | 31 |
| Fit-eligible rows, both sides A, B or C | 40 |
| Rows excluded as `post_start_information` | 6 |
| Fit-eligible rows (A–C) that are also frozen baseline rows | 22 of 23 |
| Newly covered fit-eligible rows (A–C) | 18 |

**What changes from the frozen baseline.**

- **Coverage roughly doubles.** At the widest grade set, 40 decisive engagements have an
  estimate for both sides, against 23 frozen rows.
- **Gaines' Mill (VA017) drops out.** Its frozen Confederate figure, 57,018, is Livermore's
  total, and that total adds later losses.
- **Some baseline rows become grade B.** The frozen CWSAC figure groups with Livermore's
  identical figure on a different basis (design rule 2), and the combined figure gets an
  `unknown` basis. This affects Beaver Dam Creek, Cedar Mountain and the Gettysburg Union
  side.
- **Chancellorsville (VA032) becomes grade C.** Its frozen pair equals Livermore's composite
  Chancellorsville-and-Fredericksburg entry, which also covers the separate Salem Church and
  Fredericksburg II records. The remaining figures are Doubleday's whole-army totals.

**The 72 grade D sides stay blank.** Their sources give formation names, vessels,
brigade-level parts, one-sided bounds or nothing. Many small cavalry, naval and garrison
actions therefore still have no row.

## Extraction record

- **Sources.** The inputs come only from registered sources:
  - first-pass dossier citations;
  - the frozen CWSAC forces rows;
  - a new registered transcription of the Livermore entries
    (`livermore-transcription-v1`), made from the 25 pinned page images, because the OCR
    merges note markers into figures.
- **Inventory.** Every strength claim, every typed quantity (Shiloh) and every frozen CWSAC
  figure is referenced by an input or recorded with a reason. Livermore entries list their
  entered lines and why the rest were not entered.
- **Extractor policies,** recorded in the ledger:
  - Secondary histories are compiled totals for either side, unless the passage shows an
    opponent's estimate.
  - NPS and CWSAC force cells carry the engaged table basis and `derivation_unknown`; NPS
    zero cells are not counts.
  - A commander's own figure relayed by a compiler keeps the own-report role.
  - Pre-engagement figures (plans, departures, earlier returns) are
    `engagement_link_unknown` unless the source ties them to the force brought.
- **Two implementation choices** for the reviewer to check against the design:
  - The ledger binds the metadata and raw hashes of every **cited** source, not the whole
    registry. Adding unrelated sources then does not break replay, while any change to a
    cited source does.
  - NPS narrative restatements of a frozen figure ("about 400 Home Guards") are not recorded
    as reproductions. Linking them would merge an engaged-basis figure with an unstated one.
    They are separate candidates that never set a point above their class.

Extraction is not blind (design §2). The per-engagement inventory is the structural
mitigation, and separate review checks classifications, grades and completeness.

## Estimates by engagement

Each cell gives the grade, the point, the plausible range and the point's basis. "—" is
grade D. "Best row set" names the widest grade set the row belongs to, or why it is out of
the fits.

| Record | Union | Confederate | Best row set |
| --- | --- | --- | --- |
| KY005 Middle Creek | C 1,800 (1,260–2,340) unknown | C 1,880 (1,250–2,500) unknown | ABC |
| KY006 Mill Springs | — | A 5,000 (4,750–5,250) engaged | incomplete |
| TN001 Fort Henry | C 17,000 (11,900–22,100) unknown | C 2,100 (1,400–2,800) unknown | ABC |
| NC002 Roanoke Island | A 7,500 (7,130–7,880) engaged | A 3,000 (2,850–3,150) engaged | A |
| TN002 Fort Donelson | B 15,000 (12,750–17,250) unknown | B 13,000 (11,050–21,000) unknown | AB |
| MO012 New Madrid/Island No. 10 | — | — | incomplete |
| NC003 New Berne | — | — | incomplete |
| NC004 Fort Macon | — | B 500 (430–580) unknown | incomplete |
| VA101 Kernstown, First | A 8,500 (8,080–8,930) engaged | A 3,800 (3,230–3,990) engaged | A |
| TN003 Shiloh | A 62,680 (59,550–68,340) engaged | A 44,970 (42,720–47,220) engaged | A |
| MS016 Corinth | B 120,000 (102,000–138,000) unknown | C 37,500 (25,000–70,000) effective | ABC |
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
| VA022 Cedar Mountain | B 8,030 (6,830–9,230) unknown | B 22,500 (19,130–25,880) unknown | AB |
| VA025 Thoroughfare Gap | — | — | incomplete |
| VA026 Manassas, Second | — | — | incomplete |
| KY007 Richmond | B 6,500 (5,530–8,050) unknown | A 6,850 (6,510–12,600) engaged | AB |
| WV010 Harpers Ferry | C 11,000 (7,700–14,950) unknown | — | excluded (post-start) |
| KY008 Munfordville | — | — | incomplete |
| MD002 South Mountain | A 30,000 (28,500–31,500) engaged | C 18,710 (13,100–24,330) effective | excluded (post-start) |
| MS001 Iuka | A 4,250 (4,040–9,450) engaged | A 3,200 (3,040–14,700) engaged | A |
| WV016 Shepherdstown | — | — | incomplete |
| MS002 Corinth | A 23,000 (21,850–24,150) engaged | B 22,000 (18,700–25,300) unknown | AB |
| TN007 Hatchie's Bridge | — | — | incomplete |
| KY009 Perryville | A 55,000 (52,250–57,750) engaged | A 16,000 (15,200–16,800) effective | A |
| TN008 Hartsville | A 2,000 (1,900–2,100) effective | — | incomplete |
| VA028 Fredericksburg I | A 100,010 (95,010–119,690) engaged | A 72,500 (68,870–76,120) engaged | A |
| NC007 Kinston | C 22,500 (15,000–30,000) unknown | B 2,000 (1,700–6,000) unknown | ABC |
| NC009 Goldsborough Bridge | — | — | incomplete |
| TN009 Jackson | — | A 400 (380–2,210) engaged | incomplete |
| MS003 Chickasaw Bayou | A 30,720 (29,180–33,600) effective | C 13,790 (9,650–17,930) engaged | excluded (post-start) |
| TN010 Stones River | A 45,000 (41,230–47,250) engaged | A 34,730 (33,000–53,590) effective | A |
| TN011 Parker's Cross Roads | A 3,000 (2,850–3,150) engaged | — | incomplete |
| AR006 Arkansas Post | B 28,940 (24,600–33,290) effective | A 3,000 (2,850–7,000) effective | AB |
| TN012 Dover | A 800 (570–840) engaged | A 2,500 (2,380–2,630) engaged | A |
| TN013 Thompson's Station | — | B 10,000 (8,500–11,500) unknown | incomplete |
| NC010 Fort Anderson | — | C 12,000 (8,400–15,600) unknown | incomplete |
| TN014 Vaught's Hill | A 1,300 (1,240–1,370) engaged | A 3,500 (3,330–3,680) engaged | A |
| TN015 Brentwood | A 400 (380–420) engaged | — | incomplete |
| TN016 Franklin | — | — | incomplete |
| MS004 Grand Gulf | — | B 4,700 (4,000–5,410) unknown | incomplete |
| MS005 Snyder's Bluff | — | — | incomplete |
| AL001 Day's Gap | A 2,000 (1,900–2,200) engaged | — | incomplete |
| VA032 Chancellorsville | C 114,500 (80,150–161,850) effective | C 46,500 (31,000–62,000) unknown | ABC |
| MS006 Port Gibson | B 23,000 (19,550–26,450) unknown | B 5,500 (4,680–5,500) unknown | AB |
| VA033 Salem Church | — | C 11,250 (7,500–15,000) unknown | incomplete |
| VA034 Fredericksburg II | — | — | incomplete |
| MS007 Raymond | — | A 2,500 (2,380–2,630) engaged | incomplete |
| MS008 Jackson | — | B 6,000 (5,100–13,800) unknown | incomplete |
| MS009 Champion Hill | B 29,370 (24,970–35,600) effective | A 20,000 (19,000–24,150) effective | AB |
| MS010 Big Black River Bridge | — | B 4,000 (3,400–4,600) unknown | incomplete |
| MS011 Vicksburg | C 71,140 (49,800–92,480) unknown | A 20,000 (19,000–21,000) effective | excluded (post-start) |
| LA011 Milliken's Bend | B 1,060 (900–1,220) unknown | C 1,880 (1,250–2,500) unknown | ABC |
| VA107 Winchester, Second | A 7,000 (6,650–7,350) engaged | A 12,500 (11,880–13,130) engaged | A |
| TN017 Hoover's Gap | — | — | incomplete |
| PA002 Gettysburg | B 83,290 (70,800–95,780) unknown | A 75,990 (72,190–79,790) effective | AB |
| AR008 Helena | B 4,130 (3,510–4,750) unknown | A 7,650 (7,260–15,000) engaged | AB |
| IN001 Corydon | A 400 (380–420) engaged | A 1,800 (1,710–3,000) engaged | A |
| OH001 Buffington Island | A 3,000 (2,850–3,150) engaged | A 1,700 (1,620–1,790) engaged | A |
| OH002 Salineville | A 2,600 (2,470–2,730) engaged | A 400 (380–420) engaged | A |
| TN018 Chattanooga | — | — | incomplete |
| GA003 Davis' Cross Roads | C 3,380 (2,250–13,500) unknown | B 15,000 (12,750–34,500) unknown | ABC |
| GA004 Chickamauga | A 55,000 (52,250–61,130) effective | A 66,330 (63,010–69,640) engaged | A |
| TN019 Blountsville | — | A 1,200 (1,140–6,000) engaged | incomplete |
| TN020 Blue Springs | C 11,250 (7,500–15,000) unknown | — | incomplete |
| VA040 Bristoe Station | — | — | incomplete |
| VA042 Buckland Mills | — | — | incomplete |
| TN021 Wauhatchie | — | — | incomplete |
| TN022 Collierville | A 850 (810–890) engaged | A 2,500 (2,380–2,630) engaged | A |
| WV012 Droop Mountain | C 2,630 (1,750–7,000) unknown | A 1,700 (1,620–4,000) engaged | ABC |
| TN023 Campbell's Station | — | C 20,000 (14,000–26,000) unknown | incomplete |
| TN024 Chattanooga | A 56,360 (53,540–59,180) engaged | C 44,010 (30,810–57,210) pfd | excluded (post-start) |
| GA005 Ringgold Gap | — | — | incomplete |
| TN025 Fort Sanders | C 12,000 (8,400–15,600) effective | C 16,130 (10,750–21,500) unknown | ABC |
| TN026 Bean's Station | B 4,000 (3,400–4,600) unknown | — | incomplete |
| TN027 Mossy Creek | — | A 2,000 (1,900–2,100) engaged | incomplete |
| TN028 Dandridge | — | — | incomplete |
| TN029 Fair Garden | — | — | incomplete |

common=22 new=18

Row sets: `A` is both sides grade A; `AB` is both sides A or B; `ABC` is both sides A, B or
C. Ranges are plausible ranges, not probability intervals. Points and ranges are rounded to
10 for storage, which does not imply that precision.

## Next

Separate review of the ledger in campaign batches (design §7), reconciliation, then a
decision by the owner on whether to authorize the locked evaluation (design §6).
