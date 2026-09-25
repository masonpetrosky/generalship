# Carolinas Campaign: bounded first pass

Prepared 2026-09-25 under the [cohort v2](../cohort-v2.md) research order, which lists the Carolinas
among the 1864–65 main-army campaigns. All **five records** in **Carolinas Campaign [February-March
1865]** now have draft dossiers: **45 claims, 5 explicit null unknowns and 307 citation occurrences**
(292 before the review correction below).
All seven dimensions are represented in each record. All dossiers are drafts; no features are
admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| SC011 — Rivers' Bridge | 1865-02-03 | 9 | 1 | 50 | 3 |
| NC017 — Wyse Fork | 1865-03-07 to 03-10 | 9 | 1 | 76 | 3 + follow-up |
| NC018 — Monroe's Cross Roads | 1865-03-10 | 9 | 1 | 55 | 3 |
| NC019 — Averasborough | 1865-03-16 | 9 | 1 | 53 | 3 + follow-up |
| NC020 — Bentonville | 1865-03-19 to 03-21 | 9 | 1 | 73 | 3 + follow-up |

Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read all five frozen battle, force and commander row sets and the five retained NPS pages in full.
NPS/CWSAC and the Arnold tables are one family. Every live page carries the campaign header
"Campaign of the Carolina's" and "February-March 1865"; the header is recorded and not adopted.
Each record uses two further families:

| Records | Second family | Third family |
| --- | --- | --- |
| SC011 | Blair | G. P. Harrison |
| NC017 | J. D. Cox (report and history) | Bragg |
| NC018 | Kilpatrick | Wheeler |
| NC019 | Slocum | Hardee |
| NC020 | Slocum | J. E. Johnston |

The one targeted follow-up is the **No. 3 return of Union casualties** at Kinston, Averasborough
and Bentonville, used for NC017, NC019 and NC020. The frozen and live casualty figures disagree for
all three, and Cox's and Slocum's reports carry compiler's footnotes pointing to this "revised table".

- ***Official Records* Series I, Volume XLVII, Part 1** (Illinois scan `warofrebellion471unit`; its
  catalog volume field reads v.47:1, checked before use):
  - the No. 3 return (pp.60–76), relied on only for its grand totals;
  - Blair's No. 47 report of April 4 (Salkehatchie passage pp.374–377, conclusion p.384, casualty
    Appendix C p.385);
  - Kilpatrick's No. 212 report of April 5 (opening pp.857–858, March passage pp.861–863, casualty
    inclosure p.863);
  - Cox's No. 258 report of May 16 (pp.973–980), in full;
  - Johnston's No. 284 dispatches of March 18–23, his March 27 report and the addenda (pp.1050–1060);
  - Hardee's No. 287 dispatches of March 16–17 (pp.1073–1075);
  - Harrison's February 3 Rivers' Bridge casualty report, printed as an addendum to Hardee's
    reports (p.1076);
  - Bragg's No. 288 dispatches of March 6–15 (pp.1077–1079);
  - Wheeler's No. 304 synopsis of March 1–April 15 (pp.1130–1133).
- **Cox**, *The March to the Sea; Franklin and Nashville* (1882): title and preface, and the Kinston
  narrative (OCR pp.154–162). The book narrates the Carolinas campaign in Chapters IX–XI. Its
  metadata and OCR records were registered by the Franklin-Nashville pass, so this pass adds only a
  new selection from that parent.

The following were read but not selected:

- Mower's No. 48 report of February 5 on Rivers' Bridge (it refers to a separately transmitted
  casualty list);
- Howard's February 5 letter printed with Blair's report;
- Hampton's No. 303 reports, which contain no narrative of March 10 or March 16;
- Slocum's and Kilpatrick's reports outside the selected ranges, in part, with Sherman's covering
  letter and indorsements;
- Hardee's other dispatches, including the January–February Salkehatchie telegrams, and his corps's
  prisoner report;
- Bragg's February 25 Wilmington report and his Hoke's-division return for March 19–22;
- Johnston's February 23–March 17 and March 24–25 dispatches;
- Palmer's No. 259 report, at its opening;
- Cox's Chapter X (no Rivers' Bridge narrative), his Chapter XI passages on Monroe's Cross Roads,
  Averasboro and Bentonville, and Appendix E.

The following were not inspected:

- Sherman's No. 1, Howard's No. 9 and Schofield's No. 231 reports;
- Cox's No. 237 journal abstract;
- all corps, division, brigade and regimental reports, including Williams's, Davis's, Ruger's,
  Carter's and Taliaferro's;
- the Confederate organization and parole tables, the itineraries and the correspondence;
- maps and print pages.

Stop after this batch.

### New source records

This pass adds **23 source records**, and its review correction adds three metadata-only successors
(below). The commit that added this pass (`e83348c`) also carried six metadata-only successors from
the Franklin-Nashville and Savannah reconciliation; they are not Carolinas records.

- Five NPS HTML/text pairs (`nps-sc011-v1` … `nps-nc020-v1`, with `-html` parents).
- OR XLVII Part 1 catalog metadata and full OCR (`ia-or47-1-illinois-metadata-v1`,
  `or47-1-illinois-ocr-v1`). The imprint year is illegible in OCR ("18 0 5") and is left null
  rather than inferred.
- Ten report and return selections:
  - `or47-1-blair-salkehatchie-selections-v1`;
  - `or47-1-harrison-rivers-bridge-selections-v1`;
  - `or47-1-hardee-averasborough-selections-v1`;
  - `or47-1-kilpatrick-carolinas-selections-v1` (superseded by the metadata-only `-v2`);
  - `or47-1-wheeler-carolinas-selections-v1`;
  - `or47-1-cox-kinston-selections-v1` (superseded by the metadata-only `-v2`);
  - `or47-1-bragg-kinston-selections-v1`;
  - `or47-1-slocum-carolinas-selections-v1`;
  - `or47-1-johnston-carolinas-selections-v1`;
  - `or47-1-union-casualty-return-selections-v1`.
- A Cox selection, `cox-carolinas-selections-v1`, whose parent is `cox-march-ocr-v1`; it is superseded by the
  metadata-only `cox-carolinas-selections-v2`, whose parent is the metadata-only `cox-march-ocr-v2` (same
  parent bytes).

### Independence groups

- **Existing author groups reused** (following the Humphreys and G. W. Smith precedents):
  - Cox's report and book selection join `cox-atlanta-1882` (NASH-R2), whose dependency notes assign
    his official reports to that family. His report and history are one family at Kinston, not two
    witnesses.
  - Kilpatrick joins `kilpatrick-atlanta-reports`, where NASH-R3 placed his Savannah report.
  - Wheeler joins `wheeler-savannah-report`.
  - Hardee joins `hardee-atlanta-reports`.
  - Johnston joins `johnston-atlanta-report`.
  - Bragg joins `bragg-chattanooga-report`.
- Several of these authors already had more than one registered group:
  - Johnston (`johnston-mississippi-report`);
  - Bragg (`bragg-chickamauga-reports`, plus forwarding signatures under `or-beauregard`);
  - Hardee (Shiloh documents under `or-beauregard`).

  This pass uses the most recent group in each case and does not merge the others. Each dependency
  note says so.
- **New groups:**
  - `blair-carolinas-report`;
  - `gp-harrison-rivers-bridge-report`;
  - `slocum-carolinas-report`;
  - `or47-1-union-casualty-return`, the compiler's table;
  - `or-series-i-volume-xlvii`, the container.
- Harrison's report is printed with Hardee's but written by Harrison. It covers only one detachment.
- The No. 3 return is a post-war compilation from nominal lists. The live NPS Union figures at
  Averasborough (682) and Bentonville (1,527) match its totals. Matching figures are not independent
  corroboration.

## Decisions and limits

- **Scope and overlaps.** Only one pair of records shares a date: Monroe's Cross Roads (March 10)
  falls on the last day of Wyse Fork (March 7–10). They are separate operations by different forces,
  and neither dossier draws on the other's figures. Actions outside the frozen dates are context
  only:
  - the February 1–2 Whippy Swamp, Broxton's Bridge and causeway skirmishes;
  - the other names in the SC011 frozen field (Hickory Hill, Owens' Crossroads, Lawtonville, Duck
    Creek);
  - Kilpatrick's March 15 contact before Averasborough;
  - the March 22 rear-guard fighting at Mill Creek and Hannah's Creek.

  Campaign-wide figures are not assigned to one record:
  - Blair's corps losses (384) and Kilpatrick's division losses (604) for the whole campaign;
  - Slocum's wing losses (2,352);
  - Kilpatrick's 5,068 men for duty at the start;
  - Wheeler's effective totals (4,442, 5,172 and 4,965).
- **Opening strengths remain unknown.** One record has blank frozen bounds (NC020). Every figure is
  recorded with its date, basis and scope, and none is adopted:
  - **Rivers' Bridge.** The frozen record gives US 5,000 and CS 1,200; the live page gives US 0. Blair
    gives no count for February 3. His nearest figure is about 3,000 Confederates at Salkehatchie
    bridge on January 20. Harrison's detachment strength is not stated.
  - **Wyse Fork.** The frozen record gives US 12,000 and CS 8,500. Cox's Provisional Corps had 13,056
    effectives as organized, excluding 2,000 in garrisons; he names about 6,000 garrison effectives
    and about 3,000 convalescents. On May 16 Cox put Bragg's force at about 16,000. His history
    infers thirteen to fifteen thousand from Confederate figures of eight or ten thousand plus
    3,950, and gives Johnston's six or eight thousand and Beauregard's ten thousand plus six
    thousand.
  - **Monroe's Cross Roads.** The frozen record gives US 1,850 and CS 3,000; the live page gives
    CS 3,050. Kilpatrick had Spencer's brigade of three regiments, 400 dismounted men and a section
    of guns, "less than one-third" of his command. He names three Confederate divisions.
  - **Averasborough.** The frozen record gives US 25,992 for two whole corps. Slocum sent four
    divisions, two of each corps; NPS says four divisions of the XX Corps. No basis for the frozen
    CS 5,400 was found in this record's families. Johnston's March 27 field return gives Hardee
    5,400 infantry on the morning of March 19. The coincidence is recorded in NC019's open
    questions, not adopted.
  - **Bentonville.** Johnston's figures:
    - March 18 effective totals: Bragg 6,500, Hardee 7,500, Army of Tennessee 4,000;
    - field return: 14,913 (Bragg 4,775 infantry and 782 artillery, Stewart 3,956 infantry, Hardee
      5,400 infantry);
    - "about 15,000" taken into action on the 19th;
    - the Union force estimated at above 20,000, then about 10,000 more, and near 44,000 on the 20th
      and 21st.

    Slocum relays a deserter's 40,000 for Johnston's army. The frozen label "Sherman's Right Wing
    (XX and XIV Corps)" conflicts with Slocum's heading, Johnston's account and the NPS description,
    all of which place these corps in the Left Wing.
- **Disputes preserved** (16 claims marked `disputed`: five force-scope, four casualty, four result,
  two command-roles and one information):
  - **Kinston.** Bragg claims three guns captured; Cox reports one lost. Cox's report says the
    Fifteenth Connecticut was the regiment captured, while his history says it was brought off and
    the other regiment captured. Bragg's March 8 dispatch says Schofield was not in his front; Cox
    reports the department commander on the field on the 8th and the 10th.
  - **Monroe's Cross Roads.** Kilpatrick says Hampton led Butler's division in the charge; Wheeler
    says he himself commanded his own and Butler's cavalry. Kilpatrick reports the Confederates
    driven in confusion; Wheeler calls the attack a decided success. The frozen result reads
    Inconclusive and the live result Indecisive.
  - **Averasborough.** Slocum reports three guns captured; Hardee reports two abandoned. Hardee relays
    Hampton's view that the troops fought were the Fourteenth Corps and one division of the Twentieth;
    Slocum describes two divisions of each corps.
  - **Bentonville.** Johnston believed the Seventeenth Corps arrived on the 19th; Slocum says the
    Right Wing came up on the morning of the 21st, though he also has Hazen's Fifteenth Corps
    division arriving on the morning of the 20th. Slocum says the Mill Creek bridge was burned; NPS
    says it was saved. Johnston implies four Union guns taken on the 19th (three brought off, a
    fourth left); Slocum says three were captured.
  - **Casualty figures:**
    - Wyse Fork, Union: frozen 1,101, Cox 1,257, live 1,300 and return 1,337;
    - Averasborough: frozen 1,419 total; Slocum 564 killed and wounded; live and return 682 Union;
      live CS 865; Hardee 400–500;
    - Bentonville, Union: frozen 1,646; return and live 1,527;
    - Bentonville, Confederate: frozen 3,092; Johnston about 2,294 from his letter's components,
      2,462 and 2,606, the last matching the live figure. The 2,462 table includes rows for March 22
      and for the cavalry on March 18 to 21, so it is not a strict three-day total; the 2,606
      statement is headed March 19 to 21;
    - Monroe's Cross Roads: Kilpatrick's 103 prisoners lost against Wheeler's 350 taken.
- **Command roles and ranks.**
  - The frozen Kilpatrick is a Brigadier General; his report heading reads brevet major general.
  - The frozen Wheeler is a Major General; he signs as Lieutenant-General.
  - The live NC018 page omits Hampton.
  - The live NC017 page gives Bragg as "Major General"; the frozen rank is General.
  - The live NC020 page lists "Lieutenant Colonel Joseph Johnston" and omits Slocum.
  - At Kinston, Cox's report names only "the general commanding the department"; his history
    identifies him as Schofield. Cox writes in the first person only for the March 7 advance and the
    orders of the 9th; most orders of the 8th and 10th are in the passive voice.
  - At Monroe's Cross Roads, Kilpatrick says he reached the cavalry camp on foot; the rally and the
    retaking of the camp and guns are narrated as "we".
  - At Bentonville, the inspected passages do not show Sherman directing on March 19.
  - None of these is adopted, and no listed commander receives automatic sole credit.
- **Tags.** No claim is tagged `inherited`. The Salkehatchie and Southwest Creek works existed before
  the Union arrival, but their construction dates are not stated. All non-outcome claims stay
  `unresolved`, and outcomes are `post_outcome`.
- **OCR limits.** Page locators rely on OCR running heads:
  - Cox's p.976 is flagged as reading '97G';
  - Johnston's p.1055 is inferred, because its running head reads '1056';
  - Wheeler's p.1131 and the return's p.72 were located by hand;
  - Blair's report year reads 'I860' and is mapped to 1865.

  The No. 3 return is largely garbled. Its Kinston and Bentonville grand totals print components
  that sum to them; the Averasborough 682 is read by position (the aggregate column's 116, 485 and 81
  sum to it, and the 485 matches the Twentieth Corps total line). Quotes preserve OCR corruption, for
  example "Eiver", "Avere" and "0 o’clock".

The five null unknowns are the five opening strengths.

No morale/readiness score, probability, causal effect or commander ranking is introduced. The v1
cohort, the frozen baseline and both admission proposals are unchanged, with zero promoted rows.

## Validation

- After the review correction, `python3 -m generalship check` passes and
  `python3 -m unittest discover -s tests` passes (134 tests).

## Separate review

A fresh-context `evidence-reviewer` (Claude Opus 5.5, reasoning effort `high`) reviewed this
pass at commit `e83348c` as `carolinas-review-e83348c-opus-high-v1` on 2026-09-25. Its outcome
was "corrections required": five required findings (CAR-R1 to CAR-R5) and eight advisories
(CAR-A1 to CAR-A8). It is an AI review within its stated scope, not human historical
adjudication, proof of source independence or feature admission.

## Review correction

Each required finding was checked against the retained selection text or the registry before
any change; every new quote occurs once in its section, and the dossiers were regenerated from
the builder. All five dossiers are revised under `carolinas-review-correction-2026-09-25` and
supersede byte-for-byte archives at `data/evidence/history/<ID>.v1.json` for SC011, NC017,
NC018, NC019 and NC020.

- **CAR-R1** (registry and this memo): the Franklin-Nashville/Savannah reconciliation (NASH-R3)
  moved Kilpatrick's Savannah report into `kilpatrick-atlanta-reports`, leaving
  `kilpatrick-savannah-report` with only a superseded record. The `metadata_only` successor
  `or47-1-kilpatrick-carolinas-selections-v2` (superseding v1, kept unchanged) moves this report to
  `kilpatrick-atlanta-reports` and names the Lovejoy and Savannah records in its dependency note.
  NC018's Kilpatrick citations move to v2.
- **CAR-R2** (registry and this memo): NASH-R2 moved *The March to the Sea* into
  `cox-atlanta-1882` through `cox-march-ocr-v2`. The `metadata_only` successors
  `cox-carolinas-selections-v2` (parent `cox-march-ocr-v2`, same parent bytes; its dependency
  note now names the registered *Atlanta* volume) and `or47-1-cox-kinston-selections-v2` move
  both Cox records to `cox-atlanta-1882`. NC017's Cox citations move to v2. The report and history
  remain one family at Kinston.
- **CAR-PRIMARY-1** (the primary's pending consistency change after the Franklin-Nashville and
  Savannah reconciliation): the same three successors; it is applied together with CAR-R1 and
  CAR-R2.
- **CAR-R3** (NC017 `command-roles`): Cox writes in the first person only for the March 7 advance
  and the orders of the 9th (Thomas' brigade to Palmer's flank; breastworks extended to the left);
  most orders of the 8th and 10th are passive. The value no longer attributes the dispositions of
  the 8th–10th to him; two p.978 citations added.
- **CAR-R4** (NC018 `command-roles`): Kilpatrick says he *reached* the cavalry camp on foot; the
  rally and the retaking of the camp and guns are narrated as "we". The value is corrected; four
  citations added (the reviewer's two, plus the swamp and the retaken camp).
- **CAR-R5** (NC020 `casualty-records` and this memo): the "Casualties at Bentonville" table that
  recapitulates 2,462 includes Hoke's division on March 22 (6) and the cavalry for March 18 to 21
  (113); the 2,606 statement is headed March 19 to 21. Value and rationale say so; four
  pp.1059–1060 citations added.

Advisories:

- **Adopted:** A1 (NC017: the live page gives Bragg as Major General; citation added and noted in
  this memo), A2 (NC019 `contact-and-dispatches`: Hardee's 1.30 a.m. relay of Hampton's view that
  the troops fought were the Fourteenth Corps and one division of the Twentieth, not adopted
  against Slocum), A3 (NC019: the recapitulation's 116 + 485 + 81 = 682, and the 485 matches the
  Twentieth Corps total line), A4 (NC018: the two accounts of who led the charge are in tension but
  not strictly incompatible; still disputed), A5 (NC020 `recorded-result`: Johnston's implied four
  guns against Slocum's three, recorded), A6 (this memo: Slocum also has Hazen's division arriving
  on the morning of the 20th), A7 in part (SC011: the February 3 date for Mower's daylight work is
  marked as inferred from Blair's sequence, with the February 4 citation), A8 (this memo: live CS
  865 at Averasborough; the six Franklin-Nashville/Savannah successors in `e83348c` are named as
  not Carolinas records).
- **Not adopted:** the registry part of A7. The dependency note of
  `or47-1-blair-salkehatchie-selections-v1` says the Rivers' Bridge crossing was made by the First
  and Fourth Divisions, while Blair puts Smith's Fourth Division crossing midway between the two
  bridges. The reviewer deferred this wording to the next revision, and it changes no family,
  group or citation, so no successor was added for it; it remains open.

The review correction adds **three source records** (`cox-carolinas-selections-v2`,
`or47-1-cox-kinston-selections-v2`, `or47-1-kilpatrick-carolinas-selections-v2`). Citations rise
from 292 to 307; claims (45), unknowns (5), disputed claims (16) and `inherited` tags (0) are
unchanged. No model input, cohort file, admission proposal or baseline is changed.
