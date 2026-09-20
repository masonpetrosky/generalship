# Shiloh: tracing the Saturday Howell claim, v1

Prepared 2026-09-20 from `a90189d8955141ec267a6018c28cb3d14cc1f31e`.
Research packet only; no dossier, admission proposal or model input changes.
The [machine-readable record](../../design/shiloh-howell-trace-v1/research-record.json)
binds the passages, dates, images, raw hashes, metadata hashes and unknowns.

The search found a named participant's retrospective account of Saturday firing
near Howell farm and competing testimony selections about Howell house. It also
established that Reed's Saturday clause appears in the **1903 printing**, before
the revised 1909 edition. It **did not establish which account Reed used**, which
Saturday episode he meant, or whether contact ended before Sunday's action.

## What the passages establish

| Record | Inspected passage | Bounded finding and limit |
| --- | --- | --- |
| HW01 | `reed-1903-howell-v1`, p.68; existing `reed-1909-opening-v1`, p.68 | Both editions have the same sentence about an engagement with a picket post near Howell's on Saturday. The title marks 1902 but its GPO imprint is **1903**. No footnote marker is attached to the Howell clause in either inspected paragraph. The editions are one compiler lineage, not independent witnesses. |
| HW02 | `reed-1903-howell-v1`, Cadle preface p.5 | The commission describes report comparison, Washington research and participant interviews, while acknowledging missing/meager reports. This does not identify the source of the Howell sentence. |
| HW03 | `medkirk-1886-howell-v1`, *Battles and Leaders* I, p.537 | Editors date Medkirk's letter **March 22, 1886**. He places companies E and C of his regiment, the 72d Ohio, east of Howell farm on Saturday, reports frequent fire, enemy return fire toward evening and a brush with the 5th Ohio Cavalry. A separate sentence describes firing at an officer party that rode away. This is a retrospective published letter; no manuscript or link to Reed was inspected. |
| HW04 | `worthington-1872-howell-v1`, pp.137,140 | Worthington quotes Sharpe and Crary on pickets driven away around 7 a.m. Saturday, and Sharpe on enemy occupation of Howell house all day. He also prints Sherman's denial that pickets were driven from that house. These are selections in an adversarial publication, **not an authenticated official transcript**. They remain attributed and disputed. |
| HW05 | `worthington-abstract-howell-v1`, p.4 | The pamphlet cites Sharpe/Crary proceedings pp.44 and 47 for the disputed expulsion and elsewhere refers to a copy sent from Washington. These are useful search locators; the original record and its pagination remain uninspected. The trial date in the heading is not a publication date. |
| HW06 | `hardee-plaque-howell-v1`, NPS plaque O transcription | The inspected inscription goes from Saturday deployment to Sunday picket contact without naming the Howell encounter. This is limited negative coverage of **one modern plaque transcription**, not disproof of the incident or an audit of all tablets. |
| HW07 | `nara-rg92-howell-v1` §92.10.5 and `nara-rg79-howell-v1` §79.10.2 | The official guides identify OSW/commission correspondence for 1895–1911 and park commission correspondence for 1895–1900, among other records. They locate record series; their contents have not been inspected and no particular Howell letter is established. |

The Medkirk account is in a volume with an inspected 1887 copyright page.
Worthington's 1872 title page and selected testimony pages are retained. His
Crary passage contains “(Sept. 5, 1862.)”; this remains a reported testimony date
inside a later selection, not a verified original transcript date or an April
command-knowledge timestamp. Composition dates of these later selections remain
null. The undated *Abstract* is in the same Worthington source family. Its catalog
label 1862 is not adopted as a printing date: the heading dates the trial, and
the inspected text refers to subsequent fighting. No relative printing chronology
or independent corroboration is inferred from the pamphlet.

There are three candidate descriptions to keep separate: morning expulsion from
the **house**, firing on the **farm front** during Saturday, and an evening cavalry
brush. The officer-party departure is an additional local action within Medkirk's
account. Their overlap, precise positions and relationship to Reed's unnamed
incident remain unknown. Multiple descriptions do not prove multiple distinct
engagements. Occupation of a house is not continuous firing, and a party riding
away is not cessation along the whole front. None of these passages supplies the
missing Saturday-to-Sunday continuity or termination evidence.

The existing working precursor recommendation for April 3–4 is unchanged.
Saturday segmentation, April 6's earliest qualifying contact and clock, mapped
area, both full populations, ford guards and the afloat rule remain unresolved.
No additional strength, casualty, readiness or causal estimate is extracted.

## Provenance and coverage

This is an additive migration: **21 new entries** comprising **7 selected text
sources, 11 whole-page images and 3 exact HTML snapshots**. The registry grows
from **112 entries / 109 raw paths** to **133 / 130**. All old entries/raw hashes
and **96 existing dossier, admission, cohort, research/review and baseline files**
are preserved. The prepared TN003 assignment is regenerated for the new registry.

There are **7 attributed assertions / 14 anchors / 14 source-section pairs**.
Selected text and context were visually inspected on **12 retained pages**:
11 new pages plus the existing Reed 1909 p.68. Four of the new pages are title or
copyright context (Medkirk volume two, Worthington book one, Reed one); the
Abstract's heading page is a fifth bibliographic/context page. The three HTML
pages were read as text, not treated as facsimile inspections. All 12 historical
sections in the four new book transcriptions were image-checked, including
attribution headings not used as assertion anchors; the three selected web
sections are checked against retained HTML. This is purposive inspection, not a
page-by-page audit of the parent books or an extraction-error estimate.

The [search log](../../design/shiloh-howell-trace-v1/search-log.json) records scope,
failed access attempts and uninspected leads. Commission annual-report and modern
administrative-history leads were not successfully opened; neither is silently
represented as reviewed evidence. The guides do not establish whether particular
records are digitized or unavailable elsewhere. No external inquiry was sent.

```sh
python3 design/shiloh-howell-trace-v1/reference-audit.py
python3 design/shiloh-precontact-segmentation-v1/reference-audit.py
python3 design/shiloh-precontact-segmentation-corrections-v1/reference-audit.py
make check
make reproduce
make packet
```

The new audit checks hashes, exact anchor/section alignment, HTML extraction,
preservation and zero promotion; it cannot establish historical truth or source
independence. Prepared validation and the actual separate review are retained
separately from this source record.

The frame remains **127 engagements / 36 campaigns**, with three draft dossiers.
TN003 remains **62 claims / 40 quantities / 26 events**. Admission v1 remains
**18 blocked / 22 excluded**, v2 **7 blocked / 33 excluded**; complete candidate,
emitted and promoted rows are all zero. Baseline remains **23 engagements /
13 groups**, Brier **0.2768816348133779**, worse than equal odds **0.25**.
This research has not improved the model result.

## Next bounded action

Audit the 46th and 72d Ohio regimental accounts and the cited Howell farm map
against these candidate descriptions. Keep the house, farm edges and individual
picket posts distinct; seek an explicit end/return or continuing sequence before
closing segmentation. In parallel research planning, the official Worthington
proceedings (his cited copy pp.44/47) and the identified commission correspondence
are precise archival targets, but their availability and contents remain unknown.
