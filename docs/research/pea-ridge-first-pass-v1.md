# Pea Ridge Campaign: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
**frozen record** in **Pea Ridge Campaign [March 1862]** now has a draft dossier: **9 claims, 1
explicit null unknown and 62 citation occurrences**. All seven dimensions are represented. The
dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| AR001 — Pea Ridge (Elkhorn Tavern) | 1862-03-06 to 03-08 | 9 | 1 | 62 | 3 |

This pass was drafted alongside the [New Mexico](new-mexico-1862-first-pass-v1.md),
[White River](white-river-1862-first-pass-v1.md), [Cache River](cache-river-1862-first-pass-v1.md)
and [Boston Mountains](boston-mountains-1862-first-pass-v1.md) passes. Existing dossiers, reviews
and historical revisions are unchanged. Dossier presence is not first-pass acceptance, separate
review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family.

*Official Records* Series I, Volume VIII (University of Illinois scan `warofrebellion08unit`) was
newly pinned with catalog metadata and full OCR. The catalog volume reads v.8 and the OCR title
reads "SERIES I— VOLUME VIII", imprint read as "1 883". The Pea Ridge report list (Nos. 1–56) was
read. A parallel pass may register the same volume; the primary will deduplicate. Two author
families are selected:

| Family (group) | Passages selected (OCR pages) |
| --- | --- |
| Curtis (`curtis-pea-ridge-1862-reports`) | March 6–14 dispatches and correspondence (pp.191–195; the section has no single date), with Halleck's congratulation and Van Dorn's and Maury's letters printed with them; April 1, 1862 report (pp.195–204) |
| Van Dorn (`van-dorn-pea-ridge-1862-reports`) | March 9 telegram, March 18 letter and March 27, 1862 report, No. 35 (pp.281–286) |

Part of Curtis's March 9 report on p.192 is garbled in OCR.

The following were read but not selected:

- Halleck's No. 1 telegram;
- Curtis's addenda casualty return (pp.204–206, garbled) and the May 21 letter and inclosures on
  Indian troops;
- Van Dorn's April 20 addendum.

Not inspected:

- the 53 other division, brigade and regimental reports (Sigel, Osterhaus, Asboth, Davis, Carr,
  Pike, Price, Greer and others) and the Confederate returns;
- Britton's Pea Ridge chapters in volume I, located by search only.

No targeted follow-up was used. Stop after this batch.

The pass adds **6 source records**:

- one NPS HTML/text pair;
- OR VIII catalog metadata and full OCR;
- two OR selections (Curtis, Van Dorn).

## Decisions and limits

- **Scope.** The March 6 rear-guard action near Bentonville is inside the frozen interval. The
  winter march, the March 10–14 correspondence and Van Dorn's later plans are context.
- **Opening strength remains unknown.** The frozen bounds are blank. The live field gives 24,250
  (US 10,250; CS 14,000). The inspected figures are:
  - Curtis: 12,095 and fifty guns on February 12; not more than 10,500 with forty-nine guns on
    March 7;
  - Curtis's estimates of the enemy: 20,000 to 30,000 on March 6; at least 30,000 or 40,000 in
    the April report;
  - Van Dorn: about 16,000 under his command; less than 14,000 in action;
  - Van Dorn's estimates of the enemy: 20,000 (March 9) and 17,000 to 24,000 (March 27).

  None is adopted.
- **Disputes preserved.**
  - Result: Curtis's rout against Van Dorn's "not defeated, but only foiled".
  - Losses: frozen 5,949 (US 1,349; CS 4,600) against live 3,384 (US 1,384; CS 2,000).
    - Curtis: over 1,000 killed and wounded.
    - Van Dorn's March 18 letter: not more than 800 or 1,000 killed and wounded and 200 to 300
      prisoners.
    - Van Dorn's March 27 report: about 600 and 200.
    - Van Dorn's two estimates of Union loss differ.
  - NPS's closing sentence on Union control of Missouri is a campaign claim, recorded and not
    adopted as a tactical result.
- **Command roles and ranks.** The frozen rows give Curtis as Brigadier General. The live page
  gives him no rank, and the NPS description styles him Major General. Subordinates (Sigel, Carr,
  Davis, Osterhaus, Price, McCulloch, McIntosh) are named as attributed actors, not rated. No
  listed commander receives automatic sole credit.
- **Tags.** Curtis's works on Sugar Creek were built on March 6, inside the frozen interval, and are
  not tagged `inherited`. All claims are `unresolved` or `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect or
new commander ranking is introduced. The cohort, admission proposals and baseline are unchanged,
with zero promoted rows.

## Validation

`python3 -m generalship check` passes. Every quote occurs in its cited section, and `gs.MISSES` is
empty. `python3 -m unittest discover -s tests` passes (134 tests).

## Separate review

Pending. No review is claimed.
