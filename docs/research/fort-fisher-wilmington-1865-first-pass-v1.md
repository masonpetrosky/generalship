# Operations Against Fort Fisher and Wilmington (1865): bounded first pass

Prepared 2026-09-25 under the [cohort v2](../cohort-v2.md) research order, which lists Fort Fisher
among the 1864–65 main-army campaigns. Both records in **Operations Against Fort Fisher and
Wilmington [January-February 1865]** now have draft dossiers: **18 claims, 2 explicit null unknowns
and 122 citation occurrences**. All seven dimensions are represented in each record. All dossiers
are drafts; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| NC015 — Fort Fisher | 1865-01-13 to 01-15 | 9 | 1 | 74 | 3 |
| NC016 — Wilmington | 1865-02-12 to 02-22 | 9 | 1 | 48 | 3 |

Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read both frozen battle, force and commander row sets and both retained NPS pages in full. NPS/CWSAC
and the Arnold tables are one family. Both live pages carry the campaign header "Operations Against
Fort Fisher & Wilmington" and "January-February 1865"; NC015's page is headed "Fort Fisher II". The
headers are recorded and not adopted.

| Record | Second family | Third family |
| --- | --- | --- |
| NC015 | Terry (*Official Records* XLVI Part 1) | Bragg (XLVI Part 1) |
| NC016 | Schofield (XLVII Part 1) | Bragg (XLVII Part 1) |

No targeted follow-up beyond three families was made.

- ***Official Records* Series I, Volume XLVI, Part 1** (already registered as
  `or46-1-illinois-ocr-v1`; reused as parent, not re-registered):
  - Selected: Terry's No. 1 reports of January 25 (pp.394–400) and January 20, 1865 (pp.401–402; the
    year reads "I<965" in OCR), and Bragg's No. 22 report of January 20 (pp.431–435), including the
    two January 15 dispatches it quotes.
  - Read, not selected: the chapter summary and report list (pp.393–394); Terry's addenda
    (Stanton's congratulation, General Orders No. 10); the abstract from the January 10 return
    (p.403; table garbled); the No. 2 organization and the No. 3 casualty return (pp.403–405;
    columns garbled).
  - Not inspected: Comstock's, Ames's, Paine's and the brigade reports; Whiting's No. 25, Gordon's
    No. 23, Saunders's No. 24 and Colquitt's No. 26 reports.
- ***Official Records* Series I, Volume XLVII, Part 1** (Illinois scan `warofrebellion471unit`,
  catalog volume v.47:1; the imprint year reads "18 0 5" in OCR and is left null). Pinned in this
  worktree with catalog metadata under the same IDs and with the same OCR bytes (SHA-256
  `4dcd50b3…`) as the Carolinas pass registered in the main repository; the records describe one
  artifact and should deduplicate on merge.
  - Selected: Schofield's No. 231 report of April 3, 1865 from its heading through his
    acknowledgment of the naval squadron (pp.909–911), and Bragg's No. 288 heading and report of
    February 25, 1865 with its postscript (pp.1077–1078).
  - Read, not selected: the chapter summary for February 12–26; the report list, Nos. 230–301; the
    rest of Schofield's report (Kinston and Goldsborough) and Sherman's indorsement; the opening of
    Russell's No. 232 signal report; Bragg's March 6–15 dispatches (selected separately by the
    Carolinas pass) and the Hoke's-division casualty return.
  - Not inspected: Cox's No. 254, Ames's No. 235, Paine's No. 236 and the other reports.

Porter's naval reports were not inspected. *Official Records of the Navies* Series I, Volume 11
(`officialrecordso0011unse`, to February 1, 1865) was located and its title page read but not
pinned under the three-family ceiling. The Internet Archive OCR of Volume 12
(`officialrecordso0012unse`, which would cover February 1865) returned a server error on two
attempts and was not obtained. Cox's *The March to the Sea; Franklin and Nashville* (1882, registered
earlier) narrates both actions in Chapters VIII–IX; only its table of contents was read, and it was
not used. Stop after this batch.

### New source records

This pass adds **10 source records**:

- two NPS HTML/text pairs (`nps-nc015-v1`, `nps-nc016-v1`, with `-html` parents);
- OR XLVII Part 1 catalog metadata and full OCR (`ia-or47-1-illinois-metadata-v1`,
  `or47-1-illinois-ocr-v1`), expected to deduplicate to the main repository's records of the same
  IDs on merge;
- four selections: `or46-1-terry-fort-fisher-selections-v1`,
  `or46-1-bragg-fort-fisher-selections-v1`, `or47-1-schofield-wilmington-selections-v1` and
  `or47-1-bragg-wilmington-selections-v1`.

Groups:

- Bragg's two reports join `bragg-chattanooga-report`, his most recent registered group, which also
  holds his March 1865 Kinston dispatches; he also has `bragg-chickamauga-reports` and forwarding
  signatures under `or-beauregard`. The dependency notes say these are one author family.
- Schofield joins `schofield-atlanta-report`, his only registered group.
- Terry is new (`terry-fort-fisher-reports`).
- The container group `or-series-i-volume-xlvii` matches the main registry.

## Decisions and limits

- **Scope.** The two records are separate actions and neither draws on the other's figures.
  Outside the frozen intervals, and context only:
  - the magazine explosion of January 16 and the abandonment of the lower Cape Fear works on January
    16–17;
  - Terry's January 18–19 reconnaissances;
  - Schofield's February 11 advance;
  - the March Kinston operations.

  Schofield's losses for February 11–22 are context, not assigned to one day. The December 1864
  expedition is the separate record NC014.
- **Opening strengths remain unknown.** NC015's frozen bounds are blank and its live field reads
  zero. NC016's frozen bounds (US 12,000; CS 6,600) are imported and match the live field; their
  basis is not stated. Every figure is recorded with its date, basis and scope, and none is adopted:
  - Fort Fisher (January 13–15):
    - Terry: 3,300 picked men each from Ames's and Paine's divisions, 1,400 from Abbott's brigade
      and two batteries; nearly 8,000 landed by 3 p.m. on the 13th; about 7,500 infantry for duty
      on January 20, after the assault.
    - Bragg: the garrison 1,200 strong before men from the adjacent forts were called in ("about
      000" in OCR); "fully 2,300 arms-bearing men" after 500 of 1,100 reinforcements arrived; about
      110 officers and 2,400 or 2,500 men in the struggle; Hoke's movable force about 6,000
      effectives including reserves and cavalry.
    - Fleet: nearly 60 vessels (NPS) against some 70 with at least 600 guns (Bragg).
  - Wilmington (February 12–22):
    - Schofield: Terry's line held by about 8,000 men when Cox's division landed on February 9.
    - Bragg (February 25): Union nearly 20,000; his own force not over 6,500 effectives including
      reserves and cavalry; Hagood's Fort Anderson garrison 2,000.
- **Disputes preserved** (eight claims marked `disputed`: two force-scope, two result, two
  casualty, one information, one logistics):
  - Bragg says he learned "with certainty" that the enemy had landed neither horses nor artillery;
    Terry says all the light guns were landed on the 14th.
  - The entry into Fort Fisher: Terry describes hand-to-hand fighting for the traverses until nearly
    9 p.m.; Bragg says the army column entered on the river flank "almost unopposed" and was then
    desperately resisted.
  - Terry's prisoner counts: 112 officers and 1,971 men (January 25) against 96 officers and 1,164
    men unhurt plus 8 officers and 278 men wounded (January 20).
  - The Fort Anderson evacuation: "the night of February 19 [18]" in Schofield (with the compiler's
    bracket) against the night of the 18th–19th in NPS.
  - Wilmington stores: Bragg says only some naval stores and a small lot of cotton and tobacco were
    burned; Schofield says steamers, cotton and military and naval stores; NPS says cotton, tobacco
    and government stores.
  - Casualties:
    - Fort Fisher: frozen 2,000; live 3,642 (US 1,059; CS 2,583); Terry's assault loss of 12
      officers and 107 men killed and 45 officers and 495 men wounded (659, a computation; army
      only); about 130 killed and wounded in the January 16 explosion; Bragg's 3 killed and 32
      wounded to 1.30 p.m. and about 500 killed and wounded after the enemy entered.
    - Wilmington: frozen 1,150; live zero; Schofield's about 200 Union killed and wounded and "not
      less than 1,000" Confederates from February 11; Hagood's loss of about 350 (Bragg); 375
      prisoners at Town Creek (Schofield).
- **Command roles and ranks.** The live pages give Bragg as "Major General" against the frozen
  General; frozen ranks are kept.
  - At Fort Fisher, Terry arranged the bombardment and assault with Porter, selected Ames's division
    (Ames commanded the troops engaged) and credits Comstock above himself.
  - Bragg approved Hoke's dispositions and suspended the attack order on the 14th. He says Hoke went
    forward with his skirmish line on the 15th. Terry says Hoke advanced about 4 p.m. and abandoned
    any attack after a skirmish.
  - Both name Lamb as the fort's commander. Bragg credits Whiting and Lamb with the resistance and
    declines to judge how the fort was lost.
  - At Wilmington, Bragg by his own account reached the town only on the 21st and withdrew the
    troops before daylight on the 22d. Schofield credits Cox with the Town Creek success and Terry
    with holding Hoke's force.
  - Porter's role is attested here only through Terry, Schofield, Bragg and NPS.
  - No listed commander receives automatic sole credit; subordinates are named as attributed
    actors, not rated.
- **Tags.** The fort and the Cape Fear works predate the operations, but their effect is not scored;
  no claim is tagged `inherited`. All claims stay `unresolved` or `post_outcome`.
- **Unknowns.** The two null unknowns are the opening strengths.

No morale/readiness score, probability, causal effect or new commander ranking is introduced. The
cohort, both admission proposals and the baseline are unchanged, with zero promoted rows.

## Validation

- `python3 -m generalship check` passes; every quote occurs in its cited section, and `gs.MISSES` is
  empty.
- `python3 -m unittest discover -s tests` passes (134 tests).

## Separate review pending

No separate review has been run for this pass.
