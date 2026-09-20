# Shiloh regimental accounts and post locations, v1

Prepared September 20, 2026, from base `af5075a8a8c51ab35d049720297a260bdd6bd676`.
This additive research packet follows the [Howell trace](shiloh-howell-trace-v1.md).
It changes no dossier, admission proposal, frozen cohort or model input.

Reid's 46th Ohio narrative supplies a new overnight-contact lead, but neither
that account nor the map establishes that Saturday's Howell fighting continued
into the Sunday opening. Post identity, continuity, termination, exact first
contact, mapped area and full populations remain unknown. Preserving that result
is the outcome of this comparison; additional narrative is not feature admission.

## Inspected evidence and dates

Seven source-attributed assertions bind **21 passage anchors / 19 distinct
source-section pairs** in the [research record](../../design/shiloh-regimental-posts-v1/research-record.json).
All **17 selected sections in five new text files** were checked against retained
page images. The comparison visually inspected **16 retained pages**: 13 new
facsimiles and three reused pages (Worthington pp.137/140 and Medkirk p.537).
The registry grows from **133 entries / 130 raw paths to 151 / 148**; every earlier
entry and raw file is preserved. The record also binds 109 earlier research,
review, dossier, admission, cohort and baseline files. This is purposive coverage,
not an extraction accuracy estimate or an exhaustive search of either regiment.

| Source ID | Inspected locator | Date and dependency limits |
|---|---|---|
| `reid-1868-regimental-posts-v1` | *Ohio in the War* II, pp.286 and 413; title, PDF 11 | Imprint 1868; particular narrative contributors and composition days unknown. Both entries share one compilation. Whitelaw **Reid** is distinct from D. W. **Reed**. |
| `lemmon-1875-regimental-posts-v1` | Reunion speech, pp.5–7; printed heading, PDF 9 | Heading gives delivery June 17, 1875; composition and printing days unestablished. Retrospective participant speech, not contemporary dispatch. |
| `worthington-facts-posts-v1` | Appended *Facts Developed*, printed p.2, items 11/14; PDF 155 heading, PDF 157 passage | Undated tract in a composite volume headed *Brief History*. August 1862 dates the trial. A different bound *Flank March* title (PDF 57) prints 1880; neither that nor the catalog's date dates this tract. Same interested author family as the earlier Worthington selections. |
| `worthington-1872-post-locations-v1` | *Shiloh*, p.140, Sharpe selections | New excerpts from the already retained publication/page, not a new witness. Original official testimony remains uninspected. |
| `buell-battles-leaders-map-posts-v1` | *Battles and Leaders* I, pp.502–503, both halves | Buell caption dated June 1885, edition note mentions changes beyond the March 1886 printing. Later reconstruction of April 6–7; exact composition day null. Explicit map/report dependencies are retained. |

Every source has its parent PDF URL/hash, retained raw hash, page mapping and
transformation in [the registry](../../data/sources.json). The research record
binds complete metadata hashes as well as raw bytes. Public-domain full pages
provide context around short selected text. Downloaded parent PDFs remain research
scratch inputs; their hashes identify the originals used to render retained pages.
OCR and bibliography/search results were leads, not quotations. See the bounded
[search log](../../design/shiloh-regimental-posts-v1/search-log.json).

## What the comparison establishes

**RP01 — A possible overnight link, without a located post.** Reid p.286 says
companies B and K were on picket Saturday, April 5, then says the enemy was
“feeling the lines constantly” during the night. It proceeds to daylight deployment
and a sunrise cavalry encounter. That wording must remain visible alongside the
same paragraph's “comparative quiet.” It does not name Howell, identify who supplied
the account, or specify the action and intervals meant by “feeling.” It cannot
establish continuous firing, an exact first-shot clock, or the same episode as
Sharpe's disputed morning expulsion or Sunday contact elsewhere.

**RP02–03 — The 72d accounts do not fill Saturday's gap.** Reid p.413 moves from
April 3 and the next day's encounter to April 6. Lemmon pp.5–7 narrates April 4,
then moves to April 6–7. The inspected spans do not describe Saturday Howell
contact; omission is not proof of quiet. Their Friday rescue-company lists also
differ: Reid A/D/F, Lemmon A/D/I. No correction or merged account is inferred.
Lemmon's rain paragraph explicitly resumes firing; that interruption is within
his April 4 narrative, not a Saturday-to-Sunday termination event.

**RP04–05 — Several reported post relationships, still no surveyed match.**

| Attributed account | Reported relationship | What remains unestablished |
|---|---|---|
| Sharpe in Worthington p.140, `p140-distances` | Headquarters at Weaver's; Howell post around April 1; Howell–Weaver 300 or 400 yards; Moore's no more than half a mile from camp | Exact houses, camp reference point, measurement method and coordinates |
| Same page, `p140-saturday-posts` | Saturday McDowell pickets at Moore's; Howell recognized as a 1st brigade post, on the brigade's left | Post occupation at each time and equivalence with an individual farm-front firing position; Sharpe expressly limits knowledge of other brigade pickets |
| Sherman as printed in the earlier `worthington-1872-howell-v1`, `p137-sherman-denial` | Howell house in Buckland's front about three-quarters of a mile from his center; pickets a mile in front of the house; denies Saturday expulsion | Disputed with the Sharpe/Crary selections; no independent authentication of either transcript |
| Worthington appended *Facts Developed*, items 11/14 | Post three-quarters of a mile from the center occupied all day; 46th Ohio pickets driven back at 7 a.m., then half a mile from camp | The items do not name Howell or Moore; matching them is unverified. “It was proven” is Worthington's allegation, not this project's adjudication |

These distances are not added, averaged or converted into GIS points. Brigade-relative
“left” is not a fixed compass bearing. Reported occupation does not establish
continuous fire, and Worthington's repeated publication is not independent support.

**RP06 — The cited map identifies a farm, not Saturday's post sequence.** Medkirk's
printed reference points to p.502. That half labels **HOWELL FARM**. The companion
p.503 title specifies positions on April 6–7; the legend distinguishes regimental
camps and numbered battle phases, including the evening of April 6 and the night
of April 6–7. The caption says topography and camps combine Thom, Andreas, Michler,
Sherman and other material. These are the map maker's provenance claims, not
independently verified accuracy. No uniquely identified Howell house, Weaver or
Moore point, or Saturday picket post is established in the inspected Howell region.
No page direction is treated as north and no battle polygon is drawn. Both full
halves are retained separately, without stitching or georeferencing.

**RP07 — Do not join the units into a continuous firing chain.** Medkirk's
`p537-saturday` describes companies E/C of the 72d east of Howell farm, daytime
fire and an evening cavalry brush. Reid p.286 describes B/K of the 46th on an
unnamed picket line. These are different regiments and descriptions. Same,
adjacent or relocated posts are hypotheses to test, not alternatives assigned
probabilities. Neither identity nor contradiction follows. No source-to-Reed
attribution or Saturday-to-Sunday closure is established.

## Preserved result and next action

TN003 remains a draft with **62 claims / 40 quantities / 26 events**; three draft
dossiers remain in the **127-engagement / 36-campaign** frame. Admission v1 stays
18 blocked / 22 excluded, v2 stays 7 blocked / 33 excluded: **zero complete,
eligible, emitted or promoted rows**. The baseline still uses 23 engagements in
13 groups, with Brier **0.2768816348133779**, worse than equal odds (**0.25**).
This research has not improved or refit that result.

Next trace the contributor or original evidence behind **Reid II p.286's overnight
narrative**, starting with compiler acknowledgments and attributable 46th Ohio
accounts. A located contemporary account might distinguish an unnamed screen from
Howell contact. Original court-martial proceedings and commission/Medkirk papers
remain separate archival targets; none has been inspected here.
