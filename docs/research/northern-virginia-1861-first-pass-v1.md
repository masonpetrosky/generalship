# McClellan's Operations in Northern Virginia, 1861: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). Both frozen
records in **McClellan's Operations in Northern Virginia [October-December 1861]** now have draft
dossiers: **18 claims, 2 explicit null unknowns and 101 citation occurrences**, unchanged by the
review correction. All seven dimensions are represented in each record. All dossiers are drafts; no
features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| VA006 — Ball's Bluff | 1861-10-21 | 9 | 1 | 54 | 3 |
| VA007 — Dranesville | 1861-12-20 | 9 | 1 | 47 | 3 |

This pass was drafted with five other 1861 eastern campaigns. Its slug is distinct from the
existing `northern-virginia-v1` directory, which belongs to the 1862 campaign. It adds no parent
source; it reuses the Official Records Volume V parent registered by the Western Virginia pass.
Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and both retained NPS pages in full.
NPS/CWSAC and the Arnold tables are one family. No Scribner history covering these actions was
inspected: Nicolay's volume ends in July 1861, and Webb's registered *The Peninsula* was not
opened. Each record uses one Union and one Confederate report family from ***Official
Records* Series I, Volume V** (1881; Illinois scan `warofrebellion05unit`):

- **Stone's** papers for Ball's Bluff:
  - the October 29 preliminary report (pp.293–299);
  - the November 2 letter blaming Baker, with the orders found in Baker's hat (pp.300–304);
  - the November 6 memoranda of boat capacity (p.304).
- **Evans's** October 31 report (pp.348–352), whose own casualty statement is omitted and
  referred to the No. 22 return, and his March 7, 1862 letter on Jenifer's command (p.352).
- **Ord's** December 21 report (pp.477–480).
- **Stuart's** December 21 telegram and December 23 report with his loss table (pp.490–494).

Read but not selected:

- Ball's Bluff: Stone's October 19 letter, December 2 statement and the opening of his November 7
  letter; the Union casualty return (921 as printed); the opening of Devens's report; the
  Confederate return (No. 22) and the indorsements to Evans's letter;
- Dranesville: McCall's December 20 telegram, his December 19 order and the opening of his
  December 22 report, and General Orders No. 63.

Not inspected: McClellan's report, the regimental reports on both sides, Buxton's strength report,
the Dranesville return, the sketches (not in OCR) and print pages. No targeted follow-up was used.
Stop after this batch.

The pass adds **8 source records**:

- two NPS HTML/text pairs;
- four selections: `or5-stone-balls-bluff-selections-v1`,
  `or5-evans-balls-bluff-selections-v1`, `or5-ord-dranesville-selections-v1` and
  `or5-stuart-dranesville-selections-v1`.

Stuart's new group, `stuart-dranesville-reports`, is the same author family as the registered
`stuart-bristoe-reports` and `stuart-gettysburg-reports`; the dependency note says so.

## Decisions and limits

- **Scope.** McCall's move to Dranesville in October, the October 20 demonstration and October 22
  action at Edwards Ferry, and the Confederate forage expedition are context.
- **Opening strengths remain unknown.**
  - Ball's Bluff is frozen and live at US 2,000 and CS 1,600. Stone gives Baker 1,600–1,700
    bayonets on the field and the enemy nearly three to one; Evans gives his own force as 1,709
    and the Union's as about 8,000, including Edwards Ferry.
  - Dranesville's bounds are blank. Stuart gives 1,200 in his telegram but 1,600 infantry, 150
    cavalry and four guns in his report; the Union prisoners' report gave him a six-gun battery.

  None is adopted.
- **Disputes preserved.**
  - Ball's Bluff's objective: NPS describes an attempt to cross and capture Leesburg; Stone
    describes a demonstration and a raid, with Baker limited to a position near Leesburg.
  - Ball's Bluff losses: Evans's 1,300 killed, wounded and drowned and 710 prisoners against the
    frozen US 921.
  - Dranesville's result: the Union victory against Stuart's claim that he saved his wagons and
    withdrew in order.
  - Dranesville losses:
    - Ord's 7 killed and 60 wounded, and his estimate of 50–75 Confederate dead;
    - Stuart's table of 43/143/8, with only 27 found dead on the field;
    - the frozen 301 (US 71; CS 230).
- **Command roles.**
  - Ball's Bluff lists Evans, Stone and Baker. Stone's attribution of fault to Baker was written
    under newspaper attack; Baker, killed about 4 p.m., left no report in the inspected pages.
  - Evans says Jenifer commanded only the first five companies.
  - At Dranesville, McCall (not listed) arrived during the action and Reynolds arrived too late.
  - The live page gives "James Stuart" without rank.
  - No listed commander receives automatic sole credit or blame.
- **Political contribution.** NPS's link between Ball's Bluff and the Joint Committee on the
  Conduct of the War is recorded as political contribution, not tactical outcome.
- **Tags.** No claim is tagged `inherited`; all stay `unresolved` or `post_outcome`.

The two null unknowns are the opening strengths. No morale/readiness score, probability, causal
effect or new commander ranking is introduced. Nothing in this pass changes a model input.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed this pass
together with the other five 1861 Eastern passes at commit `c298447` as
`e1861-review-c298447-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": eight
required findings (E1861-R1 to E1861-R8) and fifteen advisories (E1861-A1 to E1861-A15). None
changes a model input. It is an AI review within its stated scope, not human historical
adjudication, proof of source independence or feature admission.

## Review correction

Each finding was checked against the retained selection text or the registry before any change;
every new quote occurs in its section, and the dossiers were regenerated from the builder. No
required finding or advisory concerns VA006 or VA007; the reviewer read the Stone, Evans, Ord and
Stuart selections and raised no correction. The builder was rerun under the review binding, and both
dossiers are unchanged and not revised.

Shared finding:

- **E1861-R8** (`docs/sources.md`): the 1861 section's "thirty report selections" should read
  twenty-seven report selections (thirty selections with Nicolay's three); the 78 records are
  correct. That document belongs to the primary and is not edited here. This pass's own record count
  is unchanged.

The review correction adds **no source records**. Citations (101), claims (18), unknowns (2) and
disputed claims are unchanged. No model input, cohort file, admission proposal or baseline is
changed.

After the review correction, `python3 -m generalship check` passes and
`python3 -m unittest discover -s tests` passes (134 tests).
