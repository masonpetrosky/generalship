# Operations Against Baton Rouge: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). Both **frozen
records** in **Operations Against Baton Rouge [July-August 1862]** now have draft dossiers:
**18 claims, 2 explicit null unknowns and 88 citation occurrences**. All seven dimensions are
represented in each record. All dossiers are drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| LA003 — Baton Rouge | 1862-08-05 | 9 | 1 | 60 | 3 |
| LA004 — Donaldsonville | 1862-08-09 | 9 | 1 | 28 | 3 |

This pass was drafted alongside the other 1862-1863 Louisiana campaigns. Existing dossiers,
reviews and historical revisions are unchanged. Dossier presence is not first-pass acceptance,
separate review or model eligibility.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and the two retained NPS pages in full.
NPS/CWSAC and the Arnold tables are one family.

- **LA003** uses two further families:
  - **Irwin, *History of the Nineteenth Army Corps*** (Putnam's, 1892), already registered for
    the Red River pass. A new selection (`irwin-baton-rouge-selections-v1`) reuses the
    registered parent `irwin-nineteenth-corps-ocr-v1`. Irwin was the corps' later assistant
    adjutant-general, and his chapter quotes Breckinridge's report, so it is an interested Union
    history and not independent of that report. Selected: Chapter III, Baton Rouge (OCR
    pp.32-42), and the paragraphs on the department's effective strength at the end of Chapter IV
    (pp.50-51).
  - **Breckinridge's** report of September 30, 1862 (*Official Records* Series I, Volume XV,
    No. 24, pp.76-81), newly pinned from the University of Illinois scan `warofrebellion15unit`
    with catalog metadata and full OCR. Before use, the catalog volume ("v.15") and the OCR title
    ("SERIES I — VOLUME XV.", 1886 imprint) were checked.
- **LA004** uses two further families, both printed in the *Official Records of the Navies*,
  Series I, Volume 19 (1905 imprint), newly pinned from the Trent University scan
  `officialrecordso0019unse` with catalog metadata and full OCR. The catalog date (1894) is not the
  volume imprint; a 1987 reprint scan was found and not used.
  - **Farragut's** order of August 8 (p.140), report of August 10 (p.141) and a proclamation over
    his name printed after the committee report (p.143), whose date is not printed and whose
    covering document is not stated.
  - **The St. James Parish citizens' committee** report and resolutions of August 11 (p.142), a
    Confederate-side civilian account.

  Neither Irwin nor the inspected Mahan passages cover the August 9 bombardment, so this record has
  no history family; the gap is recorded.

The following were read but not selected:

- the rest of Irwin's Chapter IV (its Georgia Landing passage is selected in the La Fourche 1862
  pass);
- Breckinridge's list of officers mentioned and the opening of the No. 25 return;
- Bell's August 9 report on the firing near Donaldsonville and the opening of Farragut's August 10
  order to Caldwell.

Williams's, Butler's, Cahill's, Dudley's and the regimental reports (Nos. 5, 9, 11-23), the Union
return (No. 10), Van Dorn's report (No. 2), Ruggles's and the other Confederate reports, the naval
reports on Baton Rouge, the ships' logs of August 9 (seen only as search hits) and print pages were
not inspected. No targeted follow-up was used. Stop after this batch.

**Consequential gap.** For Baton Rouge, the Union return (No. 10) and Ruggles's report were not
inspected, so the Union loss and the Confederate left are known only through Irwin and
Breckinridge. For Donaldsonville, no casualty figure or partisan strength appears in any inspected
document.

**New source records.** This pass adds **12 source records**:

- two NPS HTML/text pairs;
- the OR Volume XV catalog metadata and full OCR (shared with the La Fourche 1862 and West
  Louisiana passes);
- the Breckinridge selection;
- the ORN Volume 19 catalog metadata and full OCR;
- the Farragut and St. James committee selections;
- the Irwin Baton Rouge selection (reusing the registered parent).

## Decisions and limits

- **Scope.** The destruction of the Arkansas on August 6, the evacuation of Baton Rouge on
  August 20 and the Confederate occupation of Port Hudson are context. The firing on the Sallie
  Robinson, the Brooklyn and the St. Charles before August 9 is context for LA004. The live
  campaign label reads Confederate Offensive Against Baton Rouge.
- **Opening strengths remain unknown.** Every frozen bound is blank. Every figure is recorded with
  its date and scope, and none is adopted:
  - Breckinridge: somewhat less than 4,000 leaving Vicksburg (July 27); not more than 3,400 on the
    march; 3,000 effectives by the August 4 morning report; not more than 2,600 in action, besides
    some 200 partisan rangers; the enemy not less than 5,000 (reported on the march) and not less
    than 4,500 in action, with eighteen guns to his eleven.
  - Irwin: Breckinridge's 3,600 effective on July 30 including Ruggles; about 2,600 Confederates
    in action plus 400 or 500 rangers and militia; Williams about 2,500 fighting men; Williams's
    Vicksburg troops down from 3,200 to about 800 effective; Weitzel's "not 1,200" fit to march;
    Butler's department hardly above 7,000 effective.
  - Donaldsonville: two sloops of war and one gunboat (St. James committee); no partisan count.
- **Disputes preserved.**
  - Breckinridge's July 30 strength (3,400 in his report; 3,600 attributed to him by Irwin).
  - Baton Rouge result: Breckinridge's "completely routed" against Irwin's failed attack and NPS.
  - Baton Rouge losses: the frozen and live 849 (US 371; CS 478) against Breckinridge's 467, the
    printed footnote's 446, and Irwin's 453 Confederate and 383 Union.
  - Donaldsonville: Farragut's account of firing on the Brooklyn against the committee's "no armed
    vessels"; the frozen "Union victory (inconclusive)" against the live "Union Victory".
- **Command roles and ranks.**
  - Clark and Ruggles led Breckinridge's two divisions; Williams was killed, and Irwin says Dudley
    rather than Cahill seems to have commanded the troops engaged afterwards, while NPS gives Cahill
    ordering the retreat.
  - Farragut signs as Flag-Officer; the frozen row gives Rear Admiral and the live page Admiral.
    Landry's command is reported only as hearsay.
  - No listed commander receives automatic sole credit, and live ranks are not adopted.
- **Tags.** All claims stay `unresolved` or `post_outcome`.
- **Families.** Irwin stays in `irwin-nineteenth-corps-1892`. Breckinridge is placed in
  `breckinridge-baton-rouge-1862-report`, Farragut in `farragut-donaldsonville-1862-documents` and
  the committee in `st-james-parish-committee-1862`; none had an earlier registry group. The OR
  parent is in `or-series-i-volume-xv` and the ORN parent in `orn-series-i-volume-19`.

The two null unknowns are the two opening strengths. No morale/readiness score, probability,
causal effect or new commander ranking is introduced. The cohort, both admission proposals and the
baseline are unchanged, with **zero promoted rows**. `python3 -m generalship check` passes, the
unit tests pass, and the baseline still reports **23/127 eligible engagements in 13 groups**, with
strength Brier **0.276882** against **0.250000** for equal odds.

## Separate review pending

No separate review has been run for this campaign. A Claude Opus 5.5 `high` evidence-reviewer
assignment should be prepared by the primary after commit, bound to the exact commit, dossiers
and source hashes. Coverage, separate review and feature admission stay distinct.
