# Sand Creek Campaign, 1864: bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
**frozen record** in **Sand Creek Campaign [November 1864]** now has a draft dossier: **9 claims, 1
explicit null unknown and 82 citation occurrences** (69 before the review correction below). All
seven dimensions are represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| CO001 — Sand Creek | 1864-11-29 to 1864-11-30 | 9 | 1 | 82 | 4 |

It was drafted in a parallel worktree with eight other frontier and Texas-coast campaigns. Dossier
presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family.

- **Official Records, Series I, Volume XLI, Part 1** (1893; the registered University of Illinois
  OCR `or41-1-illinois-ocr-v1`, reused): **Chivington's** November 29, 1864 telegram, his December 16
  report and his November 29 letter to the editors of the *News*, with the compiler's report list
  (No. 1, pp.948–951).
- ***Massacre of Cheyenne Indians*** (Joint Committee on the Conduct of the War, 38th Congress, 2nd
  session, 1865; Boston College scan `massacreofcheyen00unit`), the congressional testimony the
  assignment names; an Internet Archive scan exists, so it is registered:
  - the **committee's report** (pp.i–vi), signed by B. F. Wade as chairman;
  - **John S. Smith's** testimony of March 14, 1865 (pp.4–12), as the **targeted follow-up** for the
    disputed account of the attack. Smith was the government interpreter trading in the village.

The committee report and Smith's testimony share a container but are separate families: the
committee is a political body stating findings, Smith an interested eyewitness. The committee report
draws on the testimony it took, including Smith's; agreement between them is not independent
corroboration. Read, not selected: the opening of Anthony's No. 2 report. Not inspected: the company
reports (Nos. 3–8), Wynkoop's No. 9 investigation with its statements and affidavits (OR XLI, part
1, pp.951–972), the other testimony in the committee's volume (including Anthony, the Colleys, Evans
and Chivington's own answers), the 1867 military commission record, any Cheyenne or Arapaho account
and maps. Stop after this record.

This pass adds **7 source records**: one NPS HTML/text pair; catalog metadata and full OCR of the
committee volume (`ia-massacre-cheyenne-metadata-v1`, `massacre-cheyenne-ocr-v1`); and the selections
`or41-1-chivington-sand-creek-selections-v1`, `joint-committee-sand-creek-report-selections-v1` and
`smith-sand-creek-testimony-selections-v1`. New author groups: `chivington-sand-creek-reports`,
`joint-committee-conduct-war-sand-creek-1865` and `john-s-smith-sand-creek-testimony`. No main-registry
group for the Joint Committee or these authors was found.

## Decisions and limits

- **Scope.** The councils at Denver and Fort Lyon, the marches from Denver and Fort Lyon, the pursuit
  toward the Arkansas to December 5 and the later investigations are context only.
- **Characterizations are recorded as disputed and adopted by neither side.** The frozen result reads
  "Union victory (massacre)" and the frozen other name "Chivington Massacre"; the live result reads
  Union Victory. Chivington calls it one of the most bloody battles ever fought on those plains and
  calls the Indians hostile and among the worst on the Platte and Arkansas routes. The committee calls
  it a massacre, finds the band friendly and under protection, and describes indiscriminate killing
  and mutilation; Smith says Black Kettle raised an American flag with a white flag under it, that
  women and children were killed indiscriminately and that he saw bodies mutilated by the troops.
- **Disputes preserved** (6 claims marked `disputed`):
  - **Force figures.** Frozen 700 (Third Colorado) and 500 Cheyennes and a few Arapahos; Chivington's
    about 450 and 125 in his November 29 line and 900 to 1,000 warriors in 130 lodges; the committee's
    over 700 at Fort Lyon on November 28 (read "TOO" in OCR) and 125 more, and about 100 Cheyenne and
    8 to 10 Arapaho lodges, more than half women and children; Smith's 800 to 1,000 troops, about 500
    people, about two hundred warriors and not over two hundred troops in the main fight.
  - **Status of the camp and what Chivington knew** (above). Smith's opinion that Chivington knew
    the band's friendly character rests partly on what Smith conceded he did not know of his own
    knowledge.
  - **Aims and motives.** Chivington's stated aims against hostile Indians against the committee's
    finding of a deliberately planned attack and the political motives it and Smith report as others'
    views or hearsay; NPS's statement that Chivington advocated extermination.
  - **Command and responsibility,** including whether Black Kettle was killed (Chivington says so;
    Smith says the body he took for Black Kettle was not his) and the committee's finding that no
    officer restrained the men, against Smith's statement that he hardly thinks the mutilations were
    done by officers' direction.
  - **Result** (above).
  - **Casualties.** Frozen US unknown and I 200; live 198 (US 48; CS 150); NPS about 200, two-thirds
    women and children; Chivington 400 to 500 besides chiefs (telegram), about 500 (letter) and 500 to
    600 (report), and his loss 9 killed and 38 wounded or 8 killed and 40 wounded; the committee more
    than one hundred dead, three-fourths women and children; Smith about seventy dead under the bank
    and ten troops killed and thirty-eight wounded.
- **Opening strength remains unknown.** None of these figures is adopted as a matched opening
  strength.
- **Command roles.** The frozen commanders are Colonel Chivington and Black Kettle (no rank). The live
  page gives Chivington as major general and tags Black Kettle [CS]; neither is adopted. No listed
  commander receives automatic sole credit.
- **No Cheyenne or Arapaho account was inspected.** The camp's numbers, status, aims and losses
  therefore rest on Chivington's reports, the committee's findings (which draw on the testimony it
  took) and Smith, a white interpreter trading in the village, with NPS as a modern summary.
- **Tags.** No claim is tagged `inherited`; the creek-bank claim also records deployments. Outcomes
  are `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect or
commander ranking is introduced. No model input, frozen baseline or admission proposal is changed.

## Validation

`python3 -m generalship check` passes and `python3 -m unittest discover -s tests` passes (134 tests)
in the worktree. After the review correction, both pass again (134 tests) in the main repository,
and `gs.MISSES` is empty.

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed the nine frontier
and Texas-coast first passes together at prepared commit `d57de7e` as
`frontier-review-d57de7e-opus-high-v1` on 2026-09-25. Its outcome was "corrections required": fifteen
required findings (FRC-01 to FRC-15) and fourteen advisories (FRA-01 to FRA-14) across the nine
passes. It is an AI review within its stated scope, not human historical adjudication, proof of
source independence or feature admission.

## Review correction

Each finding for this campaign was checked against the retained selection text (or the registry
record) before any change; every new quote occurs in its cited section, and the dossiers were
regenerated from the builder. Each changed dossier's reviewed version is archived byte-for-byte as
`data/evidence/history/<ID>.v1.json` and linked by `supersedes` under the revision
`sand-creek-1864-review-correction-2026-09-25`.

- **FRC-13 (accepted, applied).** (a) `recorded-result` now cites the committee's own word ("how
  unprovoked and unwarranted was this massacre", p.iv). (b) `reported-force-scope` cites Smith's "About
  500 ... five to a lodge" (p.6). (c) `command-roles` adds Smith's testimony that Chivington, told of
  the Indians' character on the day of the attack, said his orders were positive to attack them, and
  that Smith presumed the orders came from General Curtis (p.8).
- **FRC-14 (accepted, applied).** A `metadata_only` successor
  `joint-committee-sand-creek-report-selections-v2` records that the committee's account of Black
  Kettle's flags and of the interpreter being fired on closely follows Smith's testimony, which it cites
  generally, so their agreement is not independent corroboration; CO001 cites it, and the dossier's
  family note and the paragraph above say so. They remain separate families for the effort ceiling.
- **FRC-15 (accepted, applied).** The consequence of the missing Cheyenne and Arapaho account is stated
  above.
- **FRA-06 (applied).** CO001 now records Smith's two statements on the dead under the bank (the greater
  portion women and children; perhaps one-half men); his statement that small children were taken
  prisoners near the camp, against Chivington's "I captured no prisoners"; his account of the killing
  of his son Jack in his lodge the afternoon after the attack, within the frozen interval; and the
  committee's statement that Chivington had no authority over Anthony.

The characterizations are unchanged: the result stays `disputed`, Chivington's and the committee's and
Smith's words are quoted as theirs, and none is adopted. CO001 is revised
(`sand-creek-1864-review-correction-2026-09-25`). The correction adds one `metadata_only` source record.
