# Reid's overnight account: bounded provenance trace, v1

Reid's publisher supplied collected material and the preface names an editorial
assistant, but this pass does **not** identify the original contributor, witness,
statement or interview behind *Ohio in the War* II p.286. A later wording parallel
in Lindsey is a possible transmission link, not a second established witness.
No Shiloh boundary, population or model input changes.

The [research record](../../design/shiloh-reid-provenance-v1/research-record.json)
binds five assertions to eleven passage anchors / ten distinct source-locator
pairs. Six new transcribed sections and the reused Reid section were checked
against page images. Ten retained pages were visually inspected: nine new images
and the reused volume II p.286. One LOC finding-aid extraction is text-only.
All 152 earlier registry entries / 149 raw paths and 126 prior research, review,
dossier, admission, cohort and baseline files remain byte/metadata-bound.
The expanded registry has **164 entries / 161 raw paths**. These are records and
files, not witness counts.

## What the inspected sources support

| Assertion | Inspected locator | Bounded result |
| --- | --- | --- |
| RV01 | `reid-preface-provenance-v1`, `p1-origin`, `p1-collection`, `p1-method` | Reid says William H. Moore initiated the project, publishers procured documents and personal statements through visits to officers/soldiers, and Reid compared or modified material. This is the author's description of his process, not proof of its execution or accuracy. |
| RV02 | Same source, `p2-miller`, `p2-dateline` | Major Frank E. Miller is credited for organizing supplied material and preparing indexes. The preface is dated December 24, 1867; the volume title bears 1868. Neither fact assigns the 46th Ohio passage to Miller or dates its original evidence. |
| RV03 | `reid-1868-regimental-posts-v1`, `p286-saturday-night`; complete narrative facsimiles pp.286–289 | No named contributor or source footnote for the overnight passage appears in these four pages. The preface likewise makes no such assignment. This is a bounded negative, not a claim about all of Reid's writings or archives. |
| RV04 | `lindsey-overnight-provenance-v1`, `p18-overnight`, compared with Reid II p.286 | Lindsey repeats the B/K picket, overnight activity and much of the sunrise encounter, with small wording changes. The title names T. J. Lindsey; the verso says copyright 1903. Possible reuse or a shared source is an inference; exact transmission and independence are unestablished. |
| RV05 | `loc-reid-guide-extract-v1`, printed pp.11,24 / provider zero-based pages10,23 and retained line labels | The catalog points to correspondence, interviews/book and wartime Agate clippings. The book entry is described as a copy; neither an original 46th Ohio statement nor a research manuscript has been inspected. |

The complete SHA-256 bindings for each cited raw file and source metadata record
are in the research record and [source registry](../../data/sources.json).
Reid's preface date is explicitly local to those prefatory sections. Lindsey's
copyright year does not become a composition date. Reid and Lindsey are
conservatively grouped together for dependence; this does not certify copying.

## Archival route and access limits

The [LOC finding aid](https://tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/ms003038/ms003038.pdf)
locates General Correspondence at **I:A70–A184, reels119–193**; interviews and
*Ohio in the War* at **I:A217, reel215**; and Agate letters at **I:A225–231,
reel219**. Its description calls the book a copy. Adjacent catalog labels do not
establish that the interviews supplied the book. No relevant letter, interview,
book annotation or manuscript has been identified from item contents.

Direct PDF downloads returned HTTP403. Web PDF text extraction succeeded; the
retained JSON contains selected literal response lines, request URL, retrieval
date and method. Its hash binds that snapshot only: the parent PDF hash is null,
and no PDF image verification is claimed. The separately mentioned correspondent
index was not located/read in this pass. These are archival leads, not historical
corroboration. No archive contact was sent.

The next concrete digital task is to locate Reid's original Cincinnati Gazette
Shiloh dispatch under his Agate byline and compare its overnight language. The
index search can then target Moore and Miller, and possible 46th Ohio correspondents,
without presuming such letters exist. A later compilation alone cannot recover
the original witness. See the [search log](../../design/shiloh-reid-provenance-v1/search-log.json)
for the deliberately limited search and uninspected leads.

## Consequences and validation

The unnamed picket post still cannot be identified with Howell or matched to
Medkirk's E/C account. Constant feeling of the lines does not specify continuous
weapons fire, an earliest qualifying contact or a Saturday-to-Sunday event chain.
The contributor, original statement, interview date, direct copying link, post
match, continuity, timestamp, area and both side populations remain unknown.

TN003 remains 62 claims / 40 quantities / 26 events. The frozen baseline remains
23 engagements / 13 campaign groups, Brier 0.2768816348133779, worse than equal
odds at 0.25. Admission v1 remains 18 blocked / 22 excluded and v2 remains 7 blocked /
33 excluded over the same 40 observations and 127-engagement / 36-campaign frame.
There are zero complete candidate engagements, emitted rows or promoted rows.

Run `python3 design/shiloh-reid-provenance-v1/reference-audit.py`, `make check`,
`make reproduce` and `make packet`. Binding checks do not adjudicate historical
truth. This prepared packet awaits a recorded separate review; no review outcome
is claimed here.
