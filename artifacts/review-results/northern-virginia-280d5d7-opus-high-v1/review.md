# Separate review: Northern Virginia Campaign first pass (VA022–VA027)

**Outcome: corrections required.** There are two low-severity required corrections:

- **NV-R1:** two Cedar Mountain page locators are wrong.
- **NV-R2:** the scope of Ropes's Appendix D Confederate totals is misstated in VA026 and in the memo.

The other 54 claims are accepted as bounded draft extractions. Six nonblocking notes (NV-N1 to NV-N6) change no claim. This is an AI source review. It is not human historical adjudication, independent corroboration or feature admission.

## Reviewer record

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`) at `high` reasoning effort. I ran as a fresh-context subagent and did not see the author's conversation. No task ID was visible to me.
- **Date and conditions:** 2026-09-24. I worked offline: no network, no new sources, no extra source families, no agents. I did not commit or push. This file is the only one whose content I wrote.
- **Commits:** checked at HEAD `7c4902bd8cb01fe0d026c11207daab07e9a3d80f` (the review bundle). The prepared commit is `280d5d7dade3c49a82c45abc14f53f214b984ad3` and the previous commit is `c0013520981791b4b5d049bd15722a11a17fa58f`. `git diff 280d5d7 7c4902b` adds only `assignment.md` and `inputs.json`.
- **Input hashes:** `assignment.md` sha256 `b74e0709f9f2dafd1c95eed7d799acaddf5a075de1dc74a8ac104180bec68bab`; `inputs.json` sha256 `825d067d7f2b5b20204125fa47673515da4bcbf367cbf4f13e1ef5aa5dcf7fc7`. **All 51 bound input hashes match, both in the worktree and at `280d5d7`. There are no mismatches.**
- **Process deviation (disclosure):** the assignment forbade packet commands. While checking packets I imported and called `generalship.cli.research_packet` for VA022–VA027, not realising that it writes `artifacts/research/<id>.md`. This rewrote those six files in place. Afterwards `git status` was clean, `git diff` was empty and all 51 input hashes still matched. The contents are therefore byte-identical to the commit; only the file modification times changed. The call did, as a side effect, confirm that the packets regenerate byte-for-byte. I ran no build command.

## Scope actually inspected

- **Guidance:** AGENTS.md; the evidence contract; the roadmap's current-priority section and a keyword scan of the rest; the Northern Virginia section of `docs/sources.md`; and the memo in full. README and methodology were checked only through their diffs from `c001352`.
- **Dossiers:** all **56 claims and 142 citation occurrences** were read against their cited cells and passages: 18 Arnold battle cells, 2 commander-rank cells, 40 NPS and 82 Ropes citations.
  - This includes the **7 null unknowns**: six opening-personnel claims and VA022 logistics.
  - Every dossier has all seven dimensions and exactly two families: `nps-cwsac` and `ropes-army-under-pope-1881`.
  - The boundary note and the two shared open questions are identical in all six dossiers.
- **NPS:** all six retained summaries were read in full.
- **Ropes:**
  - catalog metadata: title, creator, date, publisher, sponsor, contributor and the page-number map;
  - the title/preface section;
  - all ten battle passages and Appendix D, in full, including running headers and footnotes.
  - I used the parent OCR only for section boundaries, the antecedents just before each section ("that officer" = Jackson on p.17; "He" = Buford on p.66) and page layout. I did not read the whole book or the OCR contents beyond the chapter list.
- **Frozen rows:** all six battle rows, 12 force rows and 14 commander rows.
- **Source records:** all 15 new records. OCR and selection are `retrospective_history`; the catalog record is `digital_catalog_metadata`; NPS is `government_secondary_history`. Document dates and all eleven section dates are null.

## Mechanical results

- **Derivatives:** all seven replay exactly.
  - The six NPS texts were rebuilt from the retained HTML with the recorded HTMLParser transform.
  - The eleven Ropes sections were rebuilt from `ropes-full.txt` using the recorded half-open ranges and `split`/`join` whitespace collapse.
- **Quotes:** each Ropes quote occurs in its declared section. `make check` confirms that every citation is present.
- **Ropes page locators:** 80 of 82 match the OCR body page markers. The two exceptions are NV-R1. I also checked the traps the assignment named:
  - The p.134 running header misread as "131" is handled correctly.
  - The unheaded chapter-opening pages p.75 and p.129, and section starts on pp.36, 50, 67, 102, 110, 147 and 190, are handled correctly.
  - p.22 (garbled) is not quoted.
  - The memo's page spans match the markers.
- **Coverage:**
  - 51/127 cohort dossiers and 76 without, which I recomputed from `cohort.json`, `cwsac_battles.csv` and `data/evidence`.
  - 10/36 complete groups by presence.
  - The registry has 301 records / 298 paths. Its first 286 entries equal the `c001352` registry exactly (283 paths); 15 records were added.
- **Protected files:** `git diff c001352 280d5d7` adds only VA022–VA027 under `data/evidence`. It does not touch:
  - the 45 older dossiers or the 7 history revisions;
  - `cohort.json`, either admission proposal or the three frozen CSVs;
  - `admission-check.json`, `baseline.json` or `battles.json`.
- **Baseline and admission:** 23 eligible / 13 groups; strength Brier `0.2768816348133779` against equal odds `0.25`. `promoted_rows` is 0, with 18 blocked / 22 excluded candidates.
- **Next group:** I confirmed independently that the earliest-starting incomplete group is **Maryland Campaign [September 1862]**, starting 1862-09-12: WV010, MD002, MD003 (drafted) and WV016. Iuka–Corinth (1862-09-19) comes next.
- **Packets:** each packet has three JSON blocks. They parse and equal the `battles.json` row, the current dossier and the 301-record registry.
- **Receipt:** all 72 input hashes, 301 source hashes (checked against both the registry and the files) and 7 output hashes match.
- **`make check`:** passes offline under Python 3.14.7 (82 tests OK; `artifacts_written: false`; draft_dossiers 51).

## Assignment-specific checks (confirmed unless a finding is noted)

- **Cedar Mountain force scope:** the frozen and live forces read 24,898 (US 8,030; CS 16,868). The following are kept separate and marked `disputed`:
  - Ropes: Banks's corps, less detached troops, "did not reach a total of 8,000"; Jackson "between 20,000 and 25,000".
  - NPS: 14,000 to Gordonsville in July, before A. P. Hill joined.
- **Zero fields:** the live zeros for VA023–VA027 are called "not measured absence" everywhere. All six opening strengths are null.
- **Casualties:** each claim records the frozen/live pair exactly: 2,707/3,900; 225/0; 1,100/0; 100/0; 22,180/22,179; and 2,100/2,100. The disputed pairs are marked `disputed`, and VA027 is `supported` because the figures agree.
  - Ropes's Union loss of 1,661 + 723 = 2,384 against his printed 2,393 is kept visible.
  - VA024's NPS component figures (about 600 at Kettle Run; several hundred at Bull Run Bridge) are not added.
  - The Appendix D figures are not treated as the interval's losses, but their scope is misstated: see **NV-R2**.
- **Result labels:**
  - VA023 and VA027 are Inconclusive (frozen) against Indecisive (live), and VA027 keeps its "Confederate strategic victory" qualifier.
  - Ropes's "indecisive character" is quoted.
  - For VA026's retreat, NPS's "precipitous" and Ropes's "not a rout" are both kept as `disputed`, and neither is adopted.
  - Ropes's August 28 "drawn battle" (NPS: "stalemate") stays inside VA026 as a sub-action and is not added as a separate engagement.
- **What Pope knew on August 30:** recorded as `disputed`.
  - NPS says he was "seemingly unaware".
  - Ropes (p.110) says Pope "now knew for a certainty that Longstreet had joined Jackson". Ropes (p.129) adds that Pope thought "the reinforcement had been but small", and (p.130) that he would not hear Porter's information.
  - The citations support the claim as worded.
- **Command roles:**
  - Ropes calls the Pelouze text "the order which General Banks received" but argues that it does not sustain Banks's reading. Its meaning is correctly marked `disputed`.
  - Banks's attack decision (p.24) and McDowell's detachment of Ricketts "on his own responsibility … contrary to the letter of the order of 9 p.m." (pp.68–69) are both `commander_created` and supported.
  - Winder's death and Taliaferro's succession (p.24) are recorded.
  - Stuart was ordered "as the ranking officer" to command the Manassas Junction capture (p.56).
  - Kearny's and Stevens's deaths are cited to both NPS and Ropes.
  - The live heading ranks for Longstreet (Major General; frozen Lieutenant General) and Lee (Major General; frozen General) cite the correct rank cells and are not adopted.
  - No listed commander receives sole credit.
- **Aggregation and attribution:**
  - VA024 is treated as an aggregate operation, with its component outcomes kept distinct.
  - Adjoining intervals carry no additive credit.
  - Ropes's "won only because he had the larger army", NPS's "virtually ensured Pope's defeat" and Jackson's captures as quoted by Ropes are all labelled as attributed judgments or claims, not causal effects or inventories.
  - No inspection of original orders, returns, maps or print is claimed.

## Required corrections

**NV-R1 (VA022, locators; low severity).** Two quotes lie on the unheaded chapter-opening p.19, not p.18.

Evidence:
- In the OCR, the "18 THE ARMY UNDER POPE." header is followed by 11 lines that close Chapter I ("…was at hand.").
- "CHAPTEE H. THE BATTLE OF CEDAR MOUNTAIN." follows. No running header appears for the next 25 lines, until "20 THE ARMY UNDER POPE.".
- Every other odd page in the section carries a "THE BATTLE OF CEDAR MOUNTAIN. nn" header, and the book's other chapter-opening pages are also unheaded and about 25 lines long (p.75, p.129).
- The catalog's page map lists leaves 40/41/42 as pp.18/19/20.

Exact replacements:
- `reported-force-scope`: the citation quoting `did not reach a total of 8,000 men of all arms` changes its locator from `p.18 (OCR page markers; not checked against print)` to `p.19 (OCR page markers; not checked against print)`.
- `reported-beliefs`: the citation quoting `General Pope, on the other hand, was well aware of his movements.` changes its locator from `p.18 (OCR page markers; not checked against print)` to `p.19 (OCR page markers; not checked against print)`.

The Jackson-report quote (`that only a part of General Pope's army was at Culpeper Court House`) is correctly on p.18. The memo's "pp.17–30" span is unaffected.

**NV-R2 (VA026 `casualty-records` and memo; scope; low severity).** The rationale says "Ropes's Confederate figures span the campaign, not this interval alone." The memo similarly says "His Confederate Manassas figures span the campaign."

Ropes does not give the 7,241 a campaign scope. On p.191 he gives it as "The official list of casualties at Manassas Plains, in August, 1862, gives as the killed and wounded…". Only Jackson's 4,387 is "from the Rappahannock to the Potomac". Ropes himself would distribute that figure "between the four days of fighting, 28th, 29th, 30th August, and 1st of September". Neither figure is bounded to August 28–30, but they have different stated scopes. The conclusion (not this interval's loss) stands.

Exact replacements:
- `value`: replace "Ropes cites a Confederate official list of 7,241 killed and wounded and Jackson's 4,387 from the Rappahannock to the Potomac," with "Ropes cites the Confederate official list of casualties at Manassas Plains in August 1862 as 7,241 killed and wounded, and Jackson's reported total loss of 4,387 from the Rappahannock to the Potomac,". The rest of the value is unchanged.
- `rationale`: replace the final sentence with "Neither Ropes Confederate figure is bounded to this interval: the 7,241 is labelled only 'at Manassas Plains, in August, 1862' (killed and wounded), and Jackson's 4,387 runs from the Rappahannock to the Potomac, which Ropes would distribute over August 28–September 1."
- `citations`: add `{"source_id": "ropes-northern-virginia-selections-v1", "section": "appendix-d-losses", "locator": "p.191 (OCR page markers; not checked against print)", "quote": "The official list of casualties at Manassas Plains, in August, 1862"}`. The quote occurs once in the section, after the "APPENDIX D. 191" header.
- Memo (`docs/research/northern-virginia-first-pass-v1.md`, casualty bullet): replace "His Confederate Manassas figures span the campaign," with "His Confederate figures are not bounded to August 28–30: an official killed-and-wounded list 'at Manassas Plains, in August, 1862' and Jackson's total 'from the Rappahannock to the Potomac',".

Both corrections change only the locator/scope metadata of the dossiers. No model input changes; the rebuilt packets and receipt would change. The primary should check both corrections against the retained OCR before applying them.

## Nonblocking notes (no correction required)

- **NV-N1:** Several values include a clause taken from the same inspected passage but not quoted separately. I verified that each is present and accurately paraphrased:
  - VA022 `recorded-result`: the retreat to the Rapidan "on the day but one after", p.29.
  - VA024 `recorded-result`: Taylor's attack "was of course unsuccessful", p.57.
  - VA025 `recorded-result`: delay "during the rest of the day", p.68.
  - VA026 `stated-plans`: Lee "maturing and arranging for the great attack on our left flank", p.142.
  - VA026 `recorded-result`: "retreated in good order", p.141.
  - VA027 `recorded-result`: withdrawal "within the lines of Washington", p.150.

  Adding these quotes is optional.
- **NV-N2:** VA024 `unobserved-march`: Ropes says the railroad was cut "only by the enemy's cavalry, or at least by a small force of the enemy, whether cavalry or infantry". The value's "cut by cavalry" drops the qualifier.
- **NV-N3:** VA024 `separate-commands`: Ropes also records a Trimble–Stuart controversy over credit for the capture (p.57). This supports the claim's no-sole-credit rationale.
- **NV-N4:** VA027 `flank-march-objective`: Ropes attributes the hope of striking the line of communication to "they", meaning Lee's force with Jackson leading, then calls it "This movement of Jackson's". Attributing it to Jackson is acceptable.
- **NV-N5:** VA025: Ropes says Ricketts arrived "at 3 p.m." and the value says "about 3 p.m.". This is harmless.
- **NV-N6:** Minor unrecorded live/frozen differences: the VA024 heading "George Taylor" against frozen "G.W. Taylor" (same rank), and VA022's live other name "Belle Grove". Neither is used in a claim.

## Coverage and limits

This review covered the complete Northern Virginia group (6/6 records, 56/56 claims, 142/142 citations). It did not re-review any older dossier. I checked quote presence, entailment, attribution, scope, phase tags and locators against the retained snapshots only. I made no print, map, roster, original-report or third-family check. Dependence between Ropes and the NPS summaries remains unestablished. Supported claims remain passage-backed drafts, not adjudicated history, and nothing here admits a feature or changes the baseline.
