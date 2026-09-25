# Operations at the Ohio and Mississippi River Confluence, 1861: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
frozen record in **Operations at the Ohio and Mississippi River Confluence [November 1861]** now has a
draft dossier: **9 claims, 1 explicit null unknown and 49 citation occurrences**, with all seven
dimensions represented. It is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| MO009 — Belmont | 1861-11-07 | 9 | 1 | 49 | 3 |

It was drafted in a parallel worktree with five other 1861 western campaigns and shares their Volume
III parent. Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and the
Arnold tables are one family. The two report families come from **Official Records, Series I, Volume
III** (1881; University of California scan `warofrebellion03secrrich`, registered with the Missouri
1861 pass as `or3-uc-ocr-v1`):

- **Grant's** November 17 and November 20 reports and his November 5 letter to C. F. Smith (No. 1,
  pp.267–273). The November 17 report is dated as printed. His November 6 orders to Cook and Marsh and
  November 8 thanks were read but not selected.
- **Pillow's** November 9, 10 and 12 reports (No. 15, pp.324–330). His casualty list is "Not found"
  by the compilers.

Manning F. Force's *From Fort Henry to Corinth* (Scribner, 1881) was located (its index lists Belmont
at pp.19–21) but not read or selected: the three-family ceiling was taken by the two commanders'
reports, which give both sides' numbers. Polk's No. 14 reports, McClernand's, Walke's and the
regimental reports on both sides, Brinton's medical report, returns, maps and print pages were not
inspected. No targeted follow-up was used. Stop after this record.

This pass adds **4 source records**: the NPS HTML/text pair and two Volume III selections
(`or3-grant-belmont-selections-v1`, `or3-pillow-belmont-selections-v1`). **Grant's** selection is
placed in his existing group `or-grant` (the registered Shiloh report and memoirs); **Pillow** has the
new group `pillow-belmont-reports`.

## Decisions and limits

- **Scope.** Oglesby's expedition against Thompson, the Paducah demonstration toward Columbus and the
  fire of the Columbus batteries are context only.
- **Opening strength remains unknown.** The frozen and live force fields have no figures. Grant gives
  3,114 of all arms (and on November 5 "probably not more than 3,000"), and later over 9,000 for the
  enemy from Southern sources. Pillow gives regiments each below 500 for duty and about 2,500 all told,
  "2,000 men ... against 7,450" in his November 9 dispatch, three times his number, and about 2,700
  effective in his division after the battle; he puts the Union cavalry at 450. Reinforcements crossed
  from Columbus during the day. None is adopted.
- **Disputes preserved** (3 claims marked `disputed`):
  - **Force scope,** as above.
  - **Result.** The frozen and live results read Union victory. Grant says his troops again defeated
    the enemy between them and the transports; Pillow calls the day glorious and a victory scarcely
    paralleled.
  - **Casualties.** Frozen 1,464 (US 498; CS 966) against live 1,248 (US 607; CS 641). Grant: 85
    killed, 301 wounded and 99 missing, 175 prisoners, and the enemy's killed and wounded not less than
    a figure read "GOO" in OCR. Pillow: about 400 (November 9); a list numbering a figure read "G32",
    562 of it in the force first engaged; 530 in his division (November 12); 295 Union dead buried and
    a Union loss of not less than 2,000.
- **Command roles and ranks.** Pillow crossed on Polk's instructions, placed Marks at the head of the
  flanking column, and says Polk ordered the pursuit continued with the whole force; Polk is not a
  listed commander. Grant praises McClernand. The live page gives Grant as Lieutenant General; the rank
  is not adopted. No listed commander receives automatic sole credit.
- **Campaign contribution.** Grant's November 20 statement that his object, preventing reinforcement
  of Price and the cutting off of his columns, was fully accomplished is recorded as his own
  after-action assessment, not as a tactical result.
- **Tags.** The river bottom and the abatis are not tagged `inherited`, because the abatis was
  prepared by the defenders; all claims stay `unresolved` or `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect or
commander ranking is introduced. No model input, frozen baseline or admission proposal is changed.

## Validation

`python3 -m generalship check` passes and `python3 -m unittest discover -s tests` passes (134 tests)
in the worktree.

## Separate review pending

No separate review has been run for this pass.
