# Peninsula Campaign: bounded first pass

Prepared 2026-09-20. All **16 frozen records** in **Peninsula Campaign [March-July
1862]** now have draft dossiers. They contain **152 claims, 39 explicit null
unknowns and 209 citation occurrences**; all seven dimensions are represented.
Separate Astra `xhigh` [review](../../artifacts/review-results/peninsula-aa30f97-astra-xhigh-v1/review.md)
accepted all 152 claims and 209 citations with no required corrections. All dossiers
remain drafts; no features are admitted.

| Record | Claims | Unknowns | Citations | Families |
| --- | ---: | ---: | ---: | ---: |
| VA008 — Hampton Roads | 10 | 5 | 12 | 1 |
| VA009 — Yorktown | 9 | 2 | 11 | 2 |
| VA010 — Williamsburg | 9 | 3 | 11 | 2 |
| VA011 — Eltham's Landing | 9 | 2 | 13 | 2 |
| VA012 — Drewry's Bluff | 10 | 2 | 13 | 1 |
| VA013 — Hanover Court House | 9 | 2 | 12 | 2 |
| VA014 — Seven Pines | 9 | 2 | 13 | 2 |
| VA015 — Oak Grove | 10 | 3 | 12 | 2 |
| VA016 — Beaver Dam Creek | 10 | 3 | 13 | 2 |
| VA017 — Gaines' Mill | 9 | 2 | 12 | 2 |
| VA018 — Garnett's & Golding's Farms | 9 | 2 | 13 | 2 |
| VA019 — Savage's Station | 10 | 2 | 15 | 2 |
| VA020 — Glendale/White Oak Swamp | 9 | 2 | 13 | 2 |
| VA020A — White Oak Swamp | 10 | 2 | 17 | 2 |
| VA020B — Glendale | 10 | 2 | 17 | 2 |
| VA021 — Malvern Hill | 10 | 3 | 12 | 2 |

Coverage is **33/127 draft dossiers**, **94 without**, and **7/36 complete source
campaigns by dossier presence**. All seventeen earlier dossiers remain unchanged.
Complete campaign coverage means membership, not equal research depth, independent
historical adjudication or model eligibility. The drafts are under
[`data/evidence`](../../data/evidence); prepared assignments are under
[`artifacts/research`](../../artifacts/research).

## Inspection and stopping record

Read all sixteen frozen battle rows, their force and commander rows, and fifteen
live NPS battle pages. The VA020 response has no battle record and is retained
only as an empty-template diagnostic. VA020A has structured fields but an empty
narrative; its frozen description is preserved. Page campaign dates do not
replace the frozen per-engagement intervals. All NPS/CWSAC representations count
as one family, including the additional Drewry's Bluff park history.

The shared land-battle follow-up used Alexander S. Webb's 1881
[*The Peninsula: McClellan's Campaign of 1862*](https://archive.org/details/peninsulamcclell00webb)
for fourteen records. Read the retained catalog, title and complete preface,
then twelve bounded passages: Yorktown approach (OCR pp.44–45); Williamsburg
command (pp.71–72); Eltham transport/orders (pp.81–82); Hanover contact/support
(pp.94–96); Seven Pines crossing (pp.110–111); Oak Grove (p.120); Beaver Dam
position (p.125); Gaines' Mill position (p.130); south-bank context for Garnett's
(p.135); Savage's hospital (p.141); White Oak crossing and Glendale (pp.142–144);
and Malvern position/command (p.154). The June 30 passage serves the combined
record and both components; it is not three independent witnesses.

Webb identifies himself as a participant and says he used memory and new War
Department materials, while seeking to explain the campaign's failure. His
interpretation is interested retrospective history, not a verified neutral
reconstruction. Embedded officer quotations and a Jackson report footnote remain
part of Webb's account; their originals were not separately inspected. The
November 1881 preface has no day, and neither it nor the publication year dates
the narrative sections. Section dates remain null. Later NPS dependence is
unestablished, so two families are not proof of independent corroboration.

The naval follow-ups were bounded separately. Read the full retained 1862 portion
of the [NPS Drewry's Bluff history](https://www.nps.gov/rich/learn/historyculture/drewrys-bluff.htm)
for fort preparation, ammunition and command roles; later 1864–1865 operations
are outside this dossier. Hampton Roads' targeted search for changing command
and naval constraints located NHHC and NOAA accounts, but downloads failed:
Python reported certificate verification failure for the NHHC photography page,
curl returned 404, and NOAA's anniversary page returned 403. Search snippets are
not evidence. No second family is claimed for either naval record; Hampton Roads
keeps five unknown dimensions rather than filling them from recollection.

This was **at most one targeted follow-up per record**, reusing a shared history
for the land operations and treating source-access recovery as part of the same
Hampton Roads question. Stop here; original orders/returns, source reconciliation,
precise clocks and print verification remain deferred. No extra depth cycle is
required simply because questions remain.

Thirty-six new records bring the registry to **259 entries / 256 raw paths**,
preserving all previous **223/220**. They comprise fifteen NPS HTML/text pairs,
one empty HTML diagnostic, one park-history HTML/text pair and Webb catalog/full
OCR/selected text. All selected text was read. Half-open Unicode offsets and
whitespace-only normalization reproduce the Webb excerpts. OCR errors, split
words and headers are preserved; no maps, facsimiles, manuscript or whole-book
inspection is claimed. Full source IDs, locators, URLs and hashes are in
[`data/sources.json`](../../data/sources.json).

## Decisions and limits

- **Opening personnel remains unknown for all sixteen.** Williamsburg, Beaver
  Dam Creek and Gaines' Mill retain their imported numerical estimates without
  newly validating an opening boundary. Reinforced corps, whole armies, ships,
  surrendered or hospital populations are not interchangeable denominators.
- Casualty differences remain visible: Yorktown **320 / 482**; Eltham **242 / 234**;
  Drewry's **41 / 39** plus the park history's different killed/wounded account;
  Hanover **1,327 / 1,101**; Seven Pines **13,736 / 11,100**; Oak Grove **1,057 /
  1,067**; Beaver Dam **1,700 / 1,845**; Gaines' Mill **15,500 / 15,587**;
  Garnett's/Golding's **830 / 627**; Savage's **4,700 / 1,363**; White Oak **500 /
  zero**; Glendale **6,500 / 6,300**; Malvern **8,500 / 8,355** (frozen/live).
  Missing categories, cutoffs and scope prevent silent replacement or addition.
- Savage's hospital population includes preexisting sick/wounded and attendants
  in Webb's account. It is not a count of newly wounded in that day's action.
  Oak Grove's local advance and the frozen final-withdrawal wording stay distinct.
  Beaver Dam and Malvern's later withdrawals do not erase their frozen Union wins.
- Williamsburg's reported pursuit-command ambiguity, Johnston's wounding and
  temporary replacement at Seven Pines, and Humphreys's placement role at Malvern
  remain attributed sequences, not exact authority clocks or individual scores.
  The live Seven Pines heading's Johnston rank conflicts with its own narrative;
  it is not adopted. South-bank apprehension is reported through Webb, not a
  validated information state or proof of a causal deception effect.
- **VA020, VA020A and VA020B overlap.** All are retained for the frozen denominator;
  casualty totals and command credit must not be summed. VA020 currently fails
  decisive-outcome and numerical-strength rules, **not** an aggregate-operation
  flag. Future admission must resolve overlap explicitly. This pass changes no
  imported grain or model row.

The 39 null unknowns comprise sixteen opening strengths, fifteen information
states, six logistics states, and Hampton Roads terrain and assigned objectives.
No morale/readiness numbers, causal effects or probabilities are invented.
All previous evidence, the cohort and both admission proposals remain unchanged.
There are **zero promoted rows**, and the baseline remains **23/127 eligible
engagements in 13 groups**, with strength Brier **0.276882** versus **0.250000**
for equal odds. More draft coverage does not establish predictive improvement.

The [primary assessment](../../artifacts/review-results/peninsula-aa30f97-astra-xhigh-v1/primary-assessment.md)
accepts the bounded result. Author and reviewer each passed all 82 tests and
offline checks, replayed all 17 text derivatives and sixteen prepared packets,
and verified preservation. The report was inspected and reproduced. Reviewed
evidence and packets remain unchanged; historical unknowns and disputes remain.

Next is **Jackson's Valley Campaign [March-June 1862]**, seven frozen
records: VA101, VA102, WV009, VA103, VA104, VA105 and VA106.
