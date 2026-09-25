# Florida Expedition, 1864: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The
single frozen record in **Florida Expedition [February 1864]** now has a draft dossier:
**9 claims, 1 explicit null unknown and 56 citation occurrences**. All seven dimensions are
represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| FL005 — Olustee | 1864-02-20 | 9 | 1 | 56 | 3 |

This pass was drafted in one batch with eight other Atlantic-coast campaigns. Dossier presence
is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full.
NPS/CWSAC and the Arnold tables are one family. Two further families from newly pinned
*Official Records* Series I, Volume XXXV, Part 1 (1891 imprint; `or35-1-illinois-ocr-v1`):

- **Seymour's** papers: Appendix P (February 17, his intention to advance without supplies),
  Appendix R (February 22) and Appendix S (his March 25 battle report), printed with
  Gillmore's No. 1 report (pp.284–290), and the return of casualties signed by him and dated
  February 25 (p.298), whose table is garbled in OCR.
- **Finegan's** February 13, 23 and 26 reports (pp.324–333) and the unsigned Confederate
  casualty addenda "Compiled from nominal lists" (p.337), kept as a separate undated section.
  Finegan is one author family across this record and Tampa (`finegan-florida-reports`).

Read but not selected: the District of Florida record of events, the report list (pp.274–275),
the appendix references in Gillmore's No. 1 report (its main text not read), Appendix O,
Gillmore's November 1, 1865 indorsement on Seymour's report and the addenda, Seymour's
February 17 reports on the advance and his general orders, and in Finegan's No. 17 Beauregard's
and Gardner's indorsements, Governor Milton's telegram, the February 25 report, the flag
correspondence, Gardner's and Cross's letters and the March 18 artillery papers. The brigade,
regimental and artillery reports (Nos. 3–15, 18–27) were located by heading only. No history
covering Olustee was found in this pass (Samuel Jones's *Siege of Charleston* ends in 1863). No
targeted follow-up was used. Stop after this record.

**Consequential gap.** Gillmore's indorsement disputes Seymour's authority, his claim of
disparity in numbers and the presence of intrenchments. It belongs to the Gillmore family,
which would be a fourth family here, and was read but not selected.

## New source records

This campaign adds **6 records**: the FL005 NPS HTML/text pair, the Volume XXXV Part 1 catalog
metadata and full OCR, and the Seymour and Finegan selections.

## Decisions and limits

- **Scope.** The February 7–14 advance from Jacksonville (Camp Finegan, Barber's, Lake City,
  Gainesville) and the retreat to Jacksonville are context.
- **Opening strength remains unknown.** The frozen bounds are blank; the live page gives 5000
  total (US 0; CS 5000). Figures recorded with date and scope, none adopted:
  - Seymour: his own force near 5,500 and sixteen guns (March 25); the enemy supposed 4,000 to
    5,000 (February 22); "the disparity in numbers was too great" (March 25).
  - Finegan: his effective force 4,600 infantry, less than 600 cavalry and three batteries of
    twelve guns; the enemy estimated at 8,000 infantry and 1,400 cavalry; a force of less than
    2,000 at Ocean Pond for several days before reinforcements (February 26); about 1,800
    infantry and 450 cavalry on February 13.
- **Disputes preserved.**
  - Whether the fighting took place at the Confederate works: Seymour and NPS say intrenched;
    Finegan says he sent Colquitt forward because the enemy would not approach the works.
  - Authority for the advance: Seymour denies violating the general plan; Gillmore's contrary
    statements were not selected.
  - Result: Seymour's orderly withdrawal and near-victory against Finegan's complete victory and
    rout.
  - Casualties: frozen and live 2,806 (US 1,860; CS 946). Seymour's return's total row reads, in
    OCR, 55 officers and 1,806 men, aggregate 1,861, followed by an unexplained "1,801 120".
    Finegan reports 93 killed and 841 wounded; the compiled table's grand total reads 946. He
    puts the Union loss at 2,000 or 2,500, with 418 wounded removed, about 400 dead buried and
    nearly 200 prisoners.
  - Guns: Seymour left five (February 22) or six (March 25); Finegan claims five captured.
- **Command roles and ranks.** The frozen commanders are Brigadier Generals Truman Seymour and
  Joseph Finegan. Seymour blames the Seventh New Hampshire's breaking; Finegan says he sent the
  whole command forward and went on the field, halted the pursuit on Colquitt's advice, and that
  his cavalry commander failed to execute pursuit orders. No listed commander receives automatic
  sole credit.
- **Tags.** All claims stay `unresolved` or `post_outcome`.

The one null unknown is the opening strength. No morale/readiness score, probability, causal
effect or new commander ranking is introduced. The cohort, the admission proposals and the
baseline are unchanged, with zero promoted rows.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed the nine
Atlantic-coast first passes (15 dossiers) together at prepared commit `0e6063c` as
`atlantic-review-0e6063c-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": eleven
required findings (R1 to R11) and thirteen advisories (A1 to A13) across the nine passes. It is
an AI review within its stated scope, not human historical adjudication, proof of source
independence or feature admission.

## Review correction

Each finding for this campaign was checked against the retained selection text (or the registry
record) before any change; every new quote occurs in its cited section, and the dossiers were
regenerated from the builder.

FL005 is unchanged. No required finding or advisory concerns this campaign; the reviewer
judged the separate section for the unsigned Confederate casualty table, and the reuse of the
Finegan and Gillmore author groups, sound.

Claims (9), unknowns (1), citations (56) and disputed claims are unchanged. No model input,
cohort file, admission proposal or baseline is changed.

After the review correction, `python3 -m generalship check` and `python3 -m unittest discover -s
tests` pass (134 tests) in the main repository, and `gs.MISSES` is empty.
