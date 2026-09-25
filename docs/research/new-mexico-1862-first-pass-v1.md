# Sibley's New Mexico Campaign: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). Both
**frozen records** in **Sibley's New Mexico Campaign [February-March 1862]** now have draft
dossiers: **18 claims, 2 explicit null unknowns and 133 citation occurrences**. All seven
dimensions are represented in each record. All dossiers are drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| NM001 — Valverde | 1862-02-20 to 02-21 | 9 | 1 | 57 | 3 |
| NM002 — Glorieta Pass | 1862-03-26 to 03-28 | 9 | 1 | 76 | 3 + 1 follow-up |

This pass was drafted alongside the four 1862 trans-Mississippi campaigns
([Pea Ridge](pea-ridge-first-pass-v1.md), [White River](white-river-1862-first-pass-v1.md),
[Cache River](cache-river-1862-first-pass-v1.md) and
[Boston Mountains](boston-mountains-1862-first-pass-v1.md)). Existing dossiers, reviews and
historical revisions are unchanged. Dossier presence is not first-pass acceptance, separate
review or model eligibility.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and both retained NPS pages in full. Both
live pages label the campaign "Sobley's New Mexico Operations" and date it "February-March 1862";
neither replaces the frozen campaign or interval. NPS/CWSAC and the Arnold tables are one family.

*Official Records* Series I, Volume IX (University of Illinois scan `warofrebellion09unit`) was
newly pinned with catalog metadata and full OCR. The catalog volume reads v.9 and the OCR title
page reads "SERIES I— VOLUME IX" with a 1883 imprint. The Valverde, Apache Canon and Glorieta
report lists were read. Each report author is its own family:

| Family (group) | Record | Passages selected (OCR pages) |
| --- | --- | --- |
| Canby (`canby-mobile-1865-reports`, the author's existing group) | NM001 | February 22 and March 1, 1862 reports (pp.487–493) and the compiled Union return (p.493, garbled) |
| Sibley (`sibley-new-mexico-1862-reports`) | NM001 | February 22 and May 4, 1862 reports, No. 8 (pp.505–512) |
| Slough (`slough-glorieta-1862-reports`) | NM002 | March 29 and March 30, 1862 reports (pp.533–535) |
| Scurry (`scurry-glorieta-1862-reports`) | NM002 | March 30 and March 31, 1862 reports (pp.541–545) |
| Chivington (`chivington-glorieta-1862-reports`) | NM002 | March 26 and March 28, 1862 reports (pp.530–531, 538–539); the one targeted follow-up |

Chivington was the Glorieta follow-up: the most consequential gap after Slough and Scurry was the
March 26 action and the destruction of the train at Johnson's Ranch, which NPS treats as
decisive. Slough's March 30 synopsis relays Chivington's actions, so these two Union families are
not independent on those points. Chivington's March 26 report is heavily garbled in its opening
lines, and Scurry's March 31 loss line is garbled.

The following were read but not selected:

- the Lord court of inquiry findings (No. 7);
- Walker's Apache Canon and Glorieta report;
- Sibley's March 31 Glorieta report (No. 5).

Not inspected:

- the reports of Roberts, Duncan, Carson, Pino and Valdez, and the Confederate subordinate reports
  (Pyron, Scurry at Valverde, Ragnet, Green, Steele, Jordan, Teel);
- Tappan's and Ritter's Glorieta reports;
- W. C. Whitford, *Colorado Volunteers in the Civil War: The New Mexico Campaign in 1862* (1906,
  Internet Archive `coloradocivilwar00whitrich`) and O. J. Hollister's 1863 regimental history.
  Both were located and left uninspected under the three-family ceiling.

Stop after this batch.

The pass adds **11 source records**:

- two NPS HTML/text pairs;
- OR IX catalog metadata and full OCR;
- five OR selections (Canby, Sibley, Slough, Scurry, Chivington).

## Decisions and limits

- **Scope.** The February 20 demonstration opposite Fort Craig is inside the Valverde interval.
  The March 27 lull and both Glorieta fights are inside the Glorieta interval. The retreat to
  Santa Fe and Sibley's later operations are context.
- **Opening strengths remain unknown.** The frozen bounds are blank for both records, and the live
  Glorieta field reads zero.
  - Valverde:
    - Canby: a Confederate nominal aggregate of nearly 3,000, reduced to about 2,600, and his own
      aggregate present of 3,810 on the morning of the 21st (including about 1,000 militia);
    - Sibley: never more than 1,500 engaged against about 3,500 on the field (February 22), and
      not more than 1,750 against at least 5,000 plus 3,000 at the fort (May 4).
    - The live NPS field (US 2,500; CS 3,000) reverses its own description (Sibley 2,500; Canby
      more than 3,000).
  - Glorieta:
    - Chivington's 418 on March 26;
    - Slough's nearly 1,300, less about 430 detached, on March 28;
    - Scurry's not over 600 fit for duty;
    - the estimates of the other side: 1,000, 1,200–1,300 and "1,200 to 3,400" (as read in OCR)
      by Slough, and 1,400 by Scurry.

  None is adopted.
- **Disputes preserved.**
  - Valverde losses: frozen US 202 against live US 263; Canby's estimate of 40 killed and 150
    wounded; the garbled return whose total line contains "263"; Sibley's 10 killed and about 100
    wounded against a frozen and live CS 187.
  - Glorieta: the train is 80 wagons (Chivington) or about 60 (Slough). Scurry claims a victory
    against the frozen Union victory. March 26 and March 28 losses are reported separately by
    each author and are not summed.
- **Command roles and ranks.**
  - Sibley says Green conducted the operations of the 20th and took over direction during the
    21st. The hour is lost in the February 22 report; the May 4 report gives 1.30 p.m. Canby
    names Roberts as immediate commander until 2.30.
  - The live pages style Canby Brigadier General and Chivington "Major General". The frozen
    ranks are kept.
  - No listed commander receives automatic sole credit.
- **Tags.** All claims are `unresolved` or `post_outcome`; nothing is tagged `inherited`.

The two null unknowns are the opening strengths. No morale/readiness score, probability, causal
effect or new commander ranking is introduced. The cohort, admission proposals and baseline are
unchanged, with zero promoted rows.

## Validation

`python3 -m generalship check` passes. Every quote occurs in its cited section, and `gs.MISSES` is
empty. `python3 -m unittest discover -s tests` passes (134 tests).

## Separate review

Pending. No review is claimed.
