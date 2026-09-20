# Shiloh April 3–5 contact chain and opening segmentation, v1

Prepared 2026-09-20 for a separate Astra `xhigh` review. This is a **working
research recommendation**, not a change to the frozen dossier, either admission
proposal, the cohort or the model. The [machine record](../../design/shiloh-precontact-segmentation-v1/research-record.json)
binds every cited passage, source metadata revision, page image and preserved input.

Recommend treating the reported **April 3–4 clashes as precursor encounters**
for the proposed local battle-opening profile. The positive evidence is return
from contact, bivouac, renewed approach orders and a postponed general attack.
The **April 5 Howell encounter remains unresolved**. We therefore do not certify
a complete engagement boundary, first-contact time, area or opening population.
This narrows the earlier packet's segmentation question without pretending to
have settled every link.

## The working rule and its limits

Anchor the proposed battle episode to the sustained assault documented on April 6,
then work backward through linked hostile contacts, including outposts and cavalry.
Separate a precursor when affirmative evidence describes termination/return and a
subsequent approach or attack phase. A change of date, overnight rest, an order,
an assertion that one command was quiet, or a compiler's heading alone does not
establish a break. Stop at an unresolved continuity link and retain it explicitly.
This rule was formulated after inspecting these sources; it is not preregistered.

The rule addresses the **opening**, not a new battle-end definition. It does not
split April 6 from April 7 merely because troops rested overnight. Nor does it
move the opening to a main-line advance while omitting the earlier screen action.
No average or preferred clock is selected from the conflicting April 6 accounts.

April 3 has weaker event-specific closure evidence than April 4. Its working
classification relies on the subsequently reported return/reset in the approach
sequence, not a documented ending for every April 3 skirmish. Local incident
identity, duration and overlaps remain unknown. Ricker's broader framing of
April 4 as the opening fight is preserved. An operation covering April 3–7 is a
legitimate alternative research unit, but would require its own boundary and
population analysis. It must not be added to the battle as independent credit.
Nothing here establishes a campaign contribution or causal effect.

## What was inspected

| Reported sequence | Evidence and locator | Interpretation and limit |
|---|---|---|
| April 3 | Chalmers and Craft, OR I.X.2 pp.387–388 (`PS01`); Grant's April 5 dispatch, p.94 (`PS02`) | Chalmers relays Clanton's provisional verbal report and suspected captures. Craft reports pickets driven in on two roads and troops marching. Same reporting chain, not independent confirmations; Grant does not identify the same incidents precisely. |
| April 4 encounter | Sherman pp.89–90; Buckland pp.90–92; Ricker p.92; Hardee p.93, OR I.X.1 (`PS03–04`) | Sherman says the scattered units returned after night; Buckland reports return with cavalry; Ricker describes an orderly retirement. Hardee reports Clanton retiring toward infantry/artillery. These are attributed accounts, not a synchronized event log. |
| Renewed approach | Johnston, Bragg, Jordan and Polk, April 4, OR I.X.2 pp.390–392 (`PS05`) | Staged movement and revised next-morning orders; Polk acknowledges receipt. Planned 3 a.m. departure is not actual execution. Jordan's earlier message on p.391 concerns reserve movement and is not silently merged with the later order. |
| Retrospective sequence | Hardee, **February 7, 1863**, OR I.X.1 pp.566–568, 571 (`PS06`) | April 4 bivouac, renewal after dawn on April 5, delayed concentration and postponement of attack. The report itself warns about exact accuracy after the lapse of time. It is not an April 1862 order or an independent confirmation of every subordinate report. |
| Saturday and Sunday | Wood, April 15, pp.590–591; Hardee p.568 (`PS07`); Sherman April 5, OR I.X.2 pp.93–94 (`PS08`) | Wood's brigade did not advance Saturday, posted night pickets and responded to Sunday firing. Sherman's quiet report and expectation concern his lines/belief. Neither disproves contact elsewhere near Howell's. Wood's 5 o'clock and Hardee's dawn do not resolve the earlier clock dispute. |
| Competing segmentation | Compiler headings, OR I.X.1 pp.89, 93; Ricker p.92 (`PS09`) | The 1884 compilation labels April 4 a skirmish and April 6–7 the battle. Ricker calls the earlier action the opening fight. Cataloging supports context, not an automatic historical boundary. Ricker's printed April 4 date includes **[?]**, so its document date remains null. |
| Howell's Saturday encounter | Reed, revised 1909, p.68 (`PS10`) | The claim remains visible. No underlying participant passage, definite unit/location match, termination or continuing sequence is established here. |

All report dates mean document composition as printed, not event timestamps or
when information reached a commander. Every `historical_knowledge_at` remains
null, including Polk's undated-within-the-day acknowledgment. No new headcount,
casualty total, morale/readiness score or quantitative predictor is extracted.

The Howell follow-up included a literal OCR search of both OR parts and reading
Cleburne's opening report/context on pp.580–582 as OCR. It did not identify an
underlying Howell passage. These are **negative leads, not evidence of absence**:
OCR spelling, location variants, missing reports and later testimony remain possible.
The retained [context OCR](../../design/shiloh-precontact-segmentation-v1/context-ocr.json)
is uncorrected and not a verified transcription. Search coverage is not an
exhaustive audit of either volume or of the park commission archive.

## Coverage, migration and verification

This packet adds **9 selected text sources and 15 whole-page images**, reusing
three existing OR scans and Reed p.68. Selected passages and nearby context were
visually inspected on **19 pages: 18 OR pages and one Reed page**. There are
**10 assertions / 24 anchors / 24 source-section pairs**. All anchors bind
registered image parents and section dates. This is purposive source inspection,
not a character-by-character audit of every page or an extraction-error estimate.
The text sources contain additional headings for date verification.

The registry grows from **87 entries / 84 raw paths** to **111 / 108**. Additions
live under `data/raw/shiloh/precontact-segmentation-v1/`; no old source is replaced.
Mixed-author dispatch metadata identifies the Sherman and Grant section groups.
Images may contain multiple documents; their presence does not create independent
witnesses. The bounded audit preserves all 87 prior metadata records and their raw
hashes, plus 72 dossier, admission, cohort, prior packet/review and baseline files.
The prepared TN003 assignment is regenerated for the expanded registry.

```sh
python3 design/shiloh-precontact-segmentation-v1/reference-audit.py
python3 design/shiloh-contact-location-v1/reference-audit.py
python3 design/shiloh-contact-location-corrections-v1/reference-audit.py
make check
make reproduce
make packet
```

The earlier whole-registry boundary audit is replayed at its exact reviewed
commit `330599b8882ef9974f4641056c4c1091b0013912`, not against an expanded registry.
The new audit checks mechanical provenance and preservation, not historical truth.

The full frame remains **127 engagements / 36 campaigns**, with three draft
dossiers. TN003 remains **62 claims / 40 quantities / 26 events**. Admission v1
remains **18 blocked / 22 excluded**; v2 **7 blocked / 33 excluded**. There are
zero complete candidate rows, emitted rows or promotions. Baseline remains
**23 engagements / 13 groups**, Brier **0.2768816348133779**, worse than equal
odds **0.25**. These results have not improved through this research packet.

## Next bounded action

Trace Reed's Saturday Howell claim through the Shiloh park commission reports,
tablet documentation and candidate participant accounts. Record the exact
attribution chain and whether the encounter ended or led into Sunday's screen
action; leave the link unknown if the underlying testimony cannot be inspected.
The working precursor recommendation can guide that search, but Howell prevents
closing the complete segmentation gate. The April 6 first shot/clock, mapped
area, ford guards, afloat rule and both full populations remain later gates.
