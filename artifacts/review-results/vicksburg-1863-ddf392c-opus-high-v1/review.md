# Separate review: Grant's Operations Against Vicksburg (1863) first pass

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. I ran as a fresh-context
  `evidence-reviewer` subagent. I cannot see my own task identifier.
- **Date:** 2026-09-25.
- **Commits:** prepared `ddf392c36dc39eb63c2fe3506b35af530e3adbfd`; previous
  `d07efc6ab3658c9ebf91f7fb1a2423900267c0e4`; the assignment bundle was committed at
  `0f341660bdb72868683b27842fd6597eec8b8182` (worktree HEAD). It changes only `assignment.md` and `inputs.json`.
- **Assignment hashes:** `assignment.md` is `6dfb1b8c…f453a` and `inputs.json` is `138b3161…fec7`. Both
  match. All 82 bound paths match `inputs.json` in the worktree and at `ddf392c` (0 mismatches).
- **Status:** this is an AI review. It is not human historical adjudication, independent corroboration,
  proof of source independence or feature admission.

**Outcome: corrections required (9 findings, VB63-R1 to VB63-R9).** Most of the extraction is accurate. The
required fixes are narrow scope, attribution and OCR-reading problems, plus one uncited clause. I found no
fabricated quote, adopted strength or causal claim.

## Scope actually inspected

- **Governance:** I read AGENTS.md, the evidence contract, and the relevant parts of the methodology and
  roadmap (current priority, Vicksburg 1862/1863 entries, next group). I also read the Vicksburg 1863 memo,
  the README/methodology/sources.md diffs and the `cli.py`/test diffs.
- **Claims:** I read all 92 claims, all 369 citation occurrences, the 10 null unknowns, the boundary notes
  and the open questions in the ten dossiers. I checked each value clause against the cited passage and its
  surrounding section text. Every cited selection section was read in full: Greene's eleven sections plus
  title and preface; Bowen (3 sections); Sherman; Forney and Hébert; Gregg; Johnston (2 sections);
  Pemberton (3 sections); Dennis and the p.448 footnote; McCulloch; Reid; Walker; and Holmes.
- **Frozen data and NPS:** I read the frozen battle, force and commander rows for all eleven group records
  and all ten retained NPS summaries in full.
- **Replay:** I replayed the ten NPS HTML-to-text transforms and all 12 selections: 11 OR selections
  against the new parents, and Greene against `greene-mississippi-ocr-v1`. Every section matches
  byte-for-byte. Every parent hash matches.
- **Page locators:** For every section, I read the parent text before its starting offset to find the
  opening page. I checked the 242 sectioned locators against the OCR page markers, mechanically with manual
  follow-up on regex misses. All match, including Greene's misprinted markers (p.128 printed "123", p.148
  printed "118", p.164 printed "161").
- **OR catalog metadata:** I read the title, date, publisher, volume and contributor fields for all three
  volumes.
- **Mechanical checks:** diffs d07efc6→ddf392c; source registry; packets; `artifacts/receipt.json`; and
  `make check` (offline: 82 tests OK, `generalship check` OK, `artifacts_written: false`).
- **Not inspected:** whole volumes, compiled returns, maps, navy reports, print or facsimiles. I ran no
  build or packet command. I did not import `generalship.cli`.

## Mechanical results (all pass)

- **Coverage:** 87/127 dossiers, 40 without. By presence, 21 of 36 source campaigns are complete; I
  recomputed this from `cohort.json` and the frozen campaign labels. The Vicksburg group of 11 is complete.
- **Registry:** 417 records and 414 unique paths, against 379/376 previously. There are 38 new IDs. No
  earlier entry changed or disappeared.
- **Unchanged files:** The prepared commit only adds files under `data/evidence`, `data/raw` and
  `artifacts/research`. These are byte-identical to d07efc6:
  - `data/evidence/MS009.json`, all 52 files in `data/evidence/history/` and all older dossiers;
  - `data/pilot/cohort.json` and both admission proposals;
  - `artifacts/admission-check.json`, `baseline.json` and `battles.json`.
- **Receipt:** All 153 input, 417 source and 7 output hashes in `receipt.json` match the files. The ten new
  dossiers are among the inputs.
- **Packets:** In each of the ten packets, the three JSON blocks equal the `battles.json` record, the
  dossier and `data/sources.json`, compared by reading.
- **Model state:** zero promoted rows. Admission candidates: 18 blocked and 22 excluded. The baseline is 23
  eligible engagements in 13 groups, with strength Brier 0.2768816348133779 against 0.25 for equal odds.
- **Next group:** confirmed independently. Among incomplete groups, the earliest engagement date is
  1863-04-30, shared by Chancellorsville and Streight's Raid. The campaign-label tie-break selects
  **Chancellorsville Campaign [April-May 1863]: VA032, VA033, VA034**.
- **Force bounds:** every frozen side-specific strength bound for the ten records is blank. Every live
  "Forces Engaged" field reads `0 total (US 0; CS 0;)`. Each dossier keeps opening strength as a null
  unknown and adopts no figure.
- **Nesting:** The boundary notes place Milliken's Bend, Goodrich's Landing and Helena inside MS011's
  May 18–July 4 interval. MS011 adds none of their figures. Greene's campaign-wide Union loss ("a little
  less than 10,000") is explicitly not assigned to the siege.
- **Goodrich's Landing surrender dispute:** kept as `disputed`. NPS says unconditional surrender on the
  29th; Walker gives prisoner-of-war terms for the officers and unconditional surrender for the Black
  soldiers, and dates the capitulation to the 30th. Reid's report of an attack on the 29th is kept as well.
- **Jackson clocks:** Johnston's retreat at 2 p.m., his dispatch's "about noon", Greene's entry between 3
  and 4 p.m. and NPS's "mid-afternoon" are all kept and not synchronized.
- **Phase tags:** the five `inherited` tags (MS004, MS010, MS011, LA014, AR008) apply to works that
  predate each start date, with rationales. Nothing is tagged `commander_created`.
- **Rank conflicts:** all four are recorded against the frozen ranks and not adopted: Grant as Lieutenant
  General (MS006, MS008, MS011), Johnston as Lieutenant Colonel, Sherman as General and Prentiss as
  Brigadier General.
- **Imprint:** the OR XXIV Part 2 year is not substituted; see R9 for how the OCR reading is quoted.

## Required corrections

**VB63-R1 — OCR readings silently normalized (MS004, MS006).** The cited OCR reads "12 oT 15" and "over
GOO". The values say "12 or 15" and "over 600" without noting the reading. This follows the TW-R5
precedent.
- In MS004 `casualty-records`, replace "Bowen reported 3 killed and 12 or 15 wounded." with "Bowen reported
  3 killed and 12 or 15 wounded (OCR '12 oT 15')."
- In MS006 `casualty-records`, replace "and says Union reports put Confederate prisoners at over 600." with
  "and says Union reports put Confederate prisoners at over 600 (OCR 'GOO')."

**VB63-R2 — MS007 `mounted-force-and-guns` understates Gregg's mounted force.** The value says Gregg had
"only a small State company of about 40". Gregg also reports that "Captain [ W. E.] Luckett, with a squadron
of 50 men, reported to me," during the night (p.736). That squadron was put on picket duty. The "40" is
exact in Gregg's text, not "about".
- **New value:** "Gregg says that on reaching Raymond he found none of Adams' cavalry except a sergeant and
  4 men; a squadron of 50 men reported during the night and was set to picket the roads toward his line of
  retreat; and that the smallness of the mounted force, Captain Hall's State company having but 40 men,
  mostly local youths, kept him from learning the enemy's strength. He says one of Bledsoe's guns burst.
  Greene says the only Union cavalry regiment present accompanied McPherson."
- **Add citations** from `or24-1-gregg-raymond-selections-v1`, section `gregg-1863-05-20`:
  - "Captain [ W. E.] Luckett, with a squadron of 50 men, reported to me," at p.736;
  - "Owing to the smallness of the mounted force" at p.737.

**VB63-R3 — MS008 `reported-force-scope`: the scope of Greene's figure is unclear, and a Johnston
inference is attributed to prisoners.** Greene's four brigades are Gregg's and Walker's, already present, plus
Gist's and Maxey's, expected the next day. "The four brigades expected" reads as expected-only. Also,
"half of Grant's army" is Johnston's conditional inference; the prisoners said McPherson's corps of four
divisions.
- Replace "Greene gives the four brigades expected about 12,000." with "Greene gives the four brigades —
  Gregg's and Walker's, just returning from Raymond, and Gist's and Maxey's, expected the next day — as about
  12,000."
- Replace "Johnston relayed prisoners' claims that the Union force at Jackson was half of Grant's army."
  with "Johnston's May 14 dispatch says prisoners identified McPherson's corps (four divisions) as marching
  from Clinton, and infers that if prisoners tell the truth the forces at Jackson must be half of Grant's
  army."
- **Add citations:**
  - `greene-vicksburg-1863-selections-v1`, section `jackson`, p.146: "Gist's South Carolina brigade and
    Maxey's Port Hudson brigade were expected to arrive the next day.";
  - `or24-1-johnston-selections-v1`, section `johnston-1863-11-01-jackson`, p.240: "say that it was
    McPherson’s corps (four divisions) which marched from Clinton."

**VB63-R4 — MS011 `assault-of-may-22` drops Greene's "not known" and blurs scope.** Greene writes: "The
Confederate loss is not known ; it prob- ably did not much exceed 500." That sentence is in his May 22
passage. The value places the 500 after the two-assault Union figure and omits the qualifier.
- **New value:** "Greene says the May 22 assault was unsuccessful at all points and that Grant's losses in
  the two assaults of May 19 and 22 were over 4,000, more than three-fourths of them on the 22d. He says the
  Confederate loss on May 22 is not known but probably did not much exceed 500, Forney's division losing
  only 42 killed and 95 wounded."
- **Add citations** from `greene-vicksburg-1863-selections-v1`, section `assault-of-may-22`:
  - "The Confederate loss is not known ;" at p.184;
  - "more than three-fourths of them being on the 22d" at p.185;
  - "the loss was only 42 killed and 95 wounded." at p.185.

**VB63-R5 — LA011 `casualty-records` has an uncited clause.** "(his return table prints 185)" rests on
McCulloch's return table. The source record says that table was read but not selected, so no retained
passage supports the clause. It is true in the parent, but uncited. McCulloch himself gives the 184 total.
- In the value, replace "McCulloch reports 44 killed, 130 wounded and 10 missing, 184 in all (his return
  table prints 185), and puts the Union loss at over a thousand." with "McCulloch reports 44 killed, 130
  wounded and 10 missing, says this makes his casualties 184, and puts the Union loss at over a thousand."
- Add the citation `or24-2-mcculloch-selections-v1`, section `mcculloch-1863-06-08`, p.469: "This makes my
  casualties 184,".
- Append to the rationale: "McCulloch's 184 differs from the frozen and live 185; his return table was read
  but not selected and is not cited."

**VB63-R6 — LA014 `plantation-raid` and the memo omit Walker's exception.** Walker says the roughly 2,000
captured people were "restored to their masters, with the excep- tion of those captured in arms, and a few
the property of disloyal citi- zens of Louisiana." The exception bears directly on the deferred question of
what happened to the soldiers who surrendered. The neutral, bracketed wording should stay.
- **New value:** "NPS says the Confederates meant to recapture freedpeople and destroy the crops on
  federally leased plantations. Walker says his forces broke up those plantations from Milliken's Bend to
  Lake Providence, capturing some 2,000 Black people who, he says, were returned to enslavement ('restored
  to their masters'), except those captured in arms and a few he describes as the property of disloyal
  citizens, and that he had planned to push on toward Providence and Ashton."
- Add the citation `or24-2-walker-selections-v1`, section `walker-1863-07-10`, p.466: "with the excep-
  tion of those captured in arms, and a few the property of disloyal citi- zens of Louisiana."
- In the memo, replace "returning about 2,000 captured Black people to enslavement." with "returning about
  2,000 captured Black people to enslavement, except, he says, those captured in arms and a few he
  describes as the property of disloyal citizens."

**VB63-R7 — AR008 `command-roles` overstates Holmes on Price.** Holmes records that Price attacked more than
an hour late. He then gives Price's explanation that he halted so as not to arrive prematurely, without
rejecting it. Holmes does not state blame of Price the way he does for Walker ("Bo satisfactory reason") or
McRae ("utterly failed").
- **New value:** "Holmes blames L. M. Walker for failing to cover Marmaduke's flank and says McRae utterly
  failed to aid Fagan; he records that Price attacked more than an hour after the time ordered, giving
  Price's explanation that he had halted to avoid arriving prematurely, and attributes the failure in very
  great measure to the men not being well in hand after success. Greene says Marmaduke's attack was feebly
  made. The live heading ranks Prentiss Brigadier General against the frozen Major General."
- Add the citation `or22-1-holmes-selections-v1`, section `holmes-1863-08-14`, p.410: "As an ex- planation
  of this delay, his report states that,".

**VB63-R8 — AR008 `relieve-vicksburg` misstates the structure of the aims.** Holmes gives two purposes. The
move was "a means of raising the siege" and of "keeping the Mississippi River closed, in the event of the
surrender of that city". The value makes keeping the river closed a means of raising the siege and drops
the surrender condition. "The same aims" also overstates NPS, which mentions only relieving pressure.
- **New value:** "Holmes says it was deemed very important to drive the Federals from their only stronghold
  in Arkansas, and that as a means of raising the siege of Vicksburg, and of keeping the Mississippi closed
  if that city surrendered, the policy of the move was apparent. Greene says Holmes hoped by capturing Helena
  to raise the siege or, if Vicksburg fell, to keep the river closed; NPS says the attack was an attempt to
  relieve pressure on Vicksburg."
- **Add citations:**
  - `or22-1-holmes-selections-v1`, section `holmes-1863-08-14`, p.409: "it was deemed of very great
    importance that they should be driven from this their only stronghold in Arkansas.";
  - `greene-vicksburg-1863-selections-v1`, section `helena`, p.235: "Vicksbiirg fell to still keep the
    river closed".

**VB63-R9 — the OR XXIV Part 2 imprint reading is quoted incompletely.** The parent OCR shows the imprint
line as `1 SS  9.` at offset 1525. The `edition` field quotes it as "('1 SS')". The recorded title range
`[1101,1521)` also ends inside "OFFICE" (1516–1522). As a result, all four Part 2 selections show "OFFIC"
and omit the imprint line; the Part 1 title ranges include the year. Not substituting the year is correct
and should stay.
- Following the evidence contract's route for source-metadata corrections, add `metadata_only` revisions of
  `ia-or24-2-illinois-metadata-v1`, `or24-2-illinois-ocr-v1` and the Dennis, McCulloch, Reid and Walker
  selections.
- In each `edition`, replace "imprint year garbled in OCR ('1 SS') and not substituted" with "imprint year
  garbled in OCR ('1 SS  9.', parent offset 1525, outside the selected title range) and not substituted".
- In `revision_note`, record that the title range ends inside "OFFICE". The raw files and hashes stay
  unchanged. Whether to add a re-bounded v2 title section is optional.

## Non-blocking observations

- **N1 — internal arithmetic in Greene.** These totals are printed as source values, but their components
  do not add up. A note in the rationale would keep the discrepancies visible:
  - Helena: Greene prints a Union loss of 57 killed, 127 wounded and 36 missing with "total, 230". The
    components sum to 220.
  - Raymond: 73 + 229 + 204 = 506, against Greene's printed "total 505".
  - Gregg: his own 73 / 229 / 201 sum to 503.
- **N2 — MS004 `command-roles`.** "Chief of artillery" is Greene's label; Bowen says "Col. William Wade, of
  the artillery".
- **N3 — LA014 `surrender-terms`.** Walker says the *officers proposed* the terms that Parsons accepted.
  Stating the proposer would sharpen the contrast with NPS's "decided to demand unconditional surrender".
- **N4 — dropped hedges.** Pemberton's "So far as I know" (MS011 `command-roles`) and Greene's "It is
  probable" (the temper of the men) are paraphrased away. The attribution itself is correct.
- **N5 — LA011 `warning-and-misinformation`.** McCulloch's account of Taylor's information is also his
  inference ("doubtless based upon information"). The rationale flags only his belief about Union warning.
- **N6 — Greene OCR duplication.** The Greene parent OCR repeats Chapter VI's opening page. The selection
  uses the second copy, which is harmless, but the transcription note does not say so.
- **N7 — MS005 `casualty-records`.** Hébert's narrative says "two privates"; his casualty list names a
  corporal and a private.

## Scope statement and limits

- **Verified:** after R1–R9, every value clause I inspected is entailed by its cited passage or cell, with
  correct attribution, scope and locator. Casualty comparisons in all ten records keep the frozen, live and
  source figures separate, and none is reconciled.
- **Attributed judgments and counterfactuals stay attributed:** Pemberton, Johnston, Greene, Holmes,
  McCulloch and NPS, including NPS's "tragedy" and Johnston's 11,000. None is recorded as a causal effect,
  score or probability.
- **Commander credit:** no listed commander receives automatic credit.
- **Not checked:** my checks rest on unverified OCR, not print. I did not assess the historical accuracy of
  any source, the independence of Greene from the Official Records, or any question the author deferred.
- **Model inputs:** none of this changes model inputs. The findings are proposals for the primary to check
  against the sources.
