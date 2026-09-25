# Separate review: Early's Raid and Sheridan's Valley first passes

**Outcome: corrections required.** There are 13 required corrections (VALLEY-R01 to R13) and 10 advisories (VALLEY-A01 to A10).

The required corrections fix extraction and attribution problems. None of them resolves a historical dispute. This is an AI review: a separate analysis. It is not human historical adjudication, independent corroboration, source-independence proof or feature admission. It does not change the dossiers, the registry, the cohort or the baseline.

## Reviewer record

| Item | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`, started as a fresh-context subagent. I did not receive the author's conversation. No task ID was shown to the reviewer. |
| Date | 2026-09-25 |
| Prepared commit reviewed | `586811f3d24d6d21fa217e498d22471e94e0beb2` |
| Previous commit | `1e791f7b8e9da05b030e355815ac0b68c43adf92` |
| Assignment bundle commit (worktree HEAD) | `4e705de56c131379d288356a7787f6e82b3e75c7` |
| `assignment.md` SHA-256 | `bb945b1a9388cc2dc32a59d447685c3b02cf6a9170210cde7d91f1afd8662d00` (verified) |
| `inputs.json` SHA-256 | `82b75da01af62b758c4100e8c9fab06af318d6b66cab3f99d0e8c941291478f7` (verified) |
| Input hashes | All **81/81** bound paths match `git show 586811f:<path>` and the worktree files. There were no mismatches. |
| `make check` (offline) | Exit 0. `unittest`: **134 tests OK**. `python3 -m generalship check` passed and reports `draft_dossiers: 153` and `artifacts_written: false`. |
| Diff scope | `1e791f7..586811f` adds 65 files and modifies none (insertions only). No v1 dossier, review, cohort, admission or baseline file changed. `artifacts/baseline.json` still reports `n_battles` 23, `n_campaigns` 13 and Brier 0.2768816 against 0.25. |

I ran no build, packet or network commands. I wrote only this file.

## Coverage actually inspected

- **Rules and docs.** I read AGENTS.md, `docs/evidence-contract.md` in full, and the research-depth section of `docs/methodology.md`. I read `docs/cohort-v2.md`, which the assignment names but the manifest does not bind; I read it at the commit. I read both memos in full and the `docs/sources.md` diff. I did not read README.md or `docs/roadmap.md`, and I did not read the admission files, `generalship/cli.py` or `tests/test_evidence.py`; `make check` exercised the tests.
- **Dossiers.** I read every claim, rationale, status, phase and citation in all 15 dossiers: 135 claims, 16 unknowns and 623 citations. I recounted the memo tables and they match.
- **Frozen rows.** I read all battle, force and commander rows for the 15 records.
- **NPS text snapshots.**
  - All 15: the commanders, forces, casualties, results and date fields.
  - Full page read for DC001. Descriptions read directly for VA114, WV013 and VA119, and compared with the frozen CSV description text for the rest.
  - The NPS HTML files were not opened.
- **Selections read in full.**
  - Wallace, both reports and the table.
  - Early, July 14 report.
  - Crook, both reports.
  - Averell, July 28 report.
  - Kelley, September 17 report.
  - Johnson, August 10 report.
  - Sheridan, all six sections.
  - Early's Volume XLIII selection, all eight sections.
  - All ten sections of Pond's Early's Raid selection.
  - These sections of Pond's Sheridan's Valley selection: `guard-hill`, `summit-point`, `smithfield`, `berryville`, `toms-brook` and `appendix-b-strength`.
- **Selections read only around citations.** For Pond's `opequon`, `fishers-hill` and `cedar-creek` sections, I read each cited passage with about 300 to 1,500 characters of context on each side. I did not read the rest of those sections word by word.
- **Parent OCRs (targeted searches only).**
  - `pond-full.txt`: Grant's August 9 message.
  - `or43-1-full.txt`: the No. 173 report list, "October 21" and the pp.560–563 boundary.
  - Catalog metadata JSON for all three parents.
- **Registry.**
  - All 16 non-NPS records among the 46 added, read field by field.
  - The 30 NPS records checked by ID and path only.
  - The existing same-author records (Sheridan Overland, Early 1863, Averell 1863, Wallace 1862), read for grouping context.

## Checks that passed

- **Quotes.** Every quote I checked occurs in its cited section; `make check` confirms presence. Most claims say only what their passages support.
- **Source families.**
  - Each record uses exactly three families: NPS/CWSAC with Arnold, Pond, and one Official Records author.
  - Pond is correctly declared dependent on the OR reports it quotes.
  - The OR volumes are treated as containers, not witnesses.
  - Documents that Pond quotes (Wright, Torbert, Rodes, Hunter, Grant) are not counted as extra families.
- **Unknowns.** All 15 opening strengths are null unknowns, and no quoted figure is adopted as an opening force. WV015 logistics is an explicit unknown. The imported bounds are kept and marked unvalidated. The live zeros are not treated as measured absence.
- **Outside-interval actions.** None is added to a record: Frederick, Purcellville, Ashby's Gap, Old Town, New Creek, Halltown on August 26, and Averell's 348 cavalry figure. Johnson's charges against McCausland are recorded as allegations. No commander receives automatic credit, and live ranks are not adopted.
- **Scans.** The `warofrebellion431unit_0` scan is correct. Its catalog lists `v.43:1`, and its OCR title reads "SERIES I— VOLUME XLIII— IN TWO PARTS. PAliT 1 … 1893". The gap is real: the New Market fragment on p.560 is followed directly by the p.563 running head, so pp.561–562 are absent. The registry and memo disclose this, and the section date is correctly null.
- **The `inherited` tag on Fort Stevens (DC001 `fortified-line`).**
  - The tag is sound for the pre-existing defences of Washington. Early "found" the works. Pond describes "regularly built field works" with timber felled "within cannon-range".
  - The Rives house cover is disclosed in the rationale as occupied during the engagement.
  - See VALLEY-A08 for the Sixth Corps' overnight intrenching.
- **Other phase tags.** VA118, VA120 and VA122 correctly avoid the `inherited` tag.
- **New 1864 groups for Averell and Wallace.** These follow registry precedent: Averell's 1863 reports are already in two separate groups. Placing Early's July and October 1864 reports in one group is conservative and acceptable.

## Required corrections

### VALLEY-R01 — MD007 `casualty-records`: missing qualifiers on the Union "missing"

The value reports Wallace's table (1,649 and 1,968) and Pond's 1,959. It omits two things from the same selected passages:

- the compiler's footnote on the missing column;
- Pond's range and his stragglers qualification.

Both bear directly on the basis of these totals.

- **Change the `value`.** Append: `The table's footnote says the missing are greatly in excess of the number reported by name and that many counted as missing probably returned to duty; Pond says some of the Union missing must have been stragglers and that the total may have been over 2,000 or, with returning stragglers, as low as 1,500.`
- **Add these citations:**
  - `or37-1-wallace-monocacy-selections-v1`, section `wallace-1864-08`, locator `p.199 (OCR page markers; not checked against print)`, quote: `Greatly in excess of the number reported by name. Many of the men here counted as missing probably returned to duty`
  - `pond-early-raid-selections-v1`, section `monocacy`, `p.58 (OCR page markers; not checked against print)`, quote: `some portion of the Union missing must have been stragglers.`
  - `pond-early-raid-selections-v1`, section `monocacy`, `p.59 (OCR page markers; not checked against print)`, quote: `so that the total losses may have been over 2,000 ; but on the other band, the return of stragglers may have eventually reduced it even to 1,500.`

### VALLEY-R02 — VA116 `casualty-records`: overlapping sub-totals presented as parallel figures

Pond gives Duval's Second Division 513. He then says that Hayes's brigade, which was one of Duval's two brigades, reported 396. The value lists the 513 and the 396 as parallel items, which invites summing them (513 + 396 + 317 ≈ 1,226). It also drops Pond's statement that the loss is uncertain.

- **Change the `value`.** Replace `giving Duval's division 513, Hayes's brigade 396 and Mulligan's division 317, and says the Confederate loss was light.` with `giving Duval's Second Division 513, of which Hayes's brigade, one of its two brigades, reported 396 (a component of the 513, not an addition), and Mulligan's Third Division 317; he calls the loss somewhat uncertain because of fugitives, part of whom afterward returned, and says the Confederate loss was light.`
- **Change the `rationale`.** Append: `Hayes's 396 is part of Duval's 513; the component figures must not be summed toward Pond's 1,200.`
- **Add these citations** (`pond-early-raid-selections-v1`, section `kernstown`):
  - `p.98 (OCR page markers; not checked against print)`: `Crook's loss in this battle was somewhat uncertain, on account of the number of fugitives, a part of whom after- ward returned to their colors ;`
  - `p.99 (OCR page markers; not checked against print)`: `His Second Brigade, Johnson's`
  - `p.99 (OCR page markers; not checked against print)`: `but the other, E. B. Hayes's`

### VALLEY-R03 — WV013 `casualty-records` and the Early's Raid memo: Johnson's net loss misread

Johnson writes: "I reached the Valley with about 300 men missing (150 have come in), leaving that number as my net loss killed, wounded, and missing." The value states his net loss as about 300. Because 150 have come in, "that number" most naturally refers to 150. The sentence is ambiguous either way, and the value should not assert 300.

- **Change the WV013 `value`.** Replace `Johnson gives his brigade's net loss as about 300 missing (150 having come in)` with `Johnson says he reached the Valley with about 300 men missing, 150 of whom had come in, "leaving that number as my net loss killed, wounded, and missing" (read here as a net of about 150; the antecedent is ambiguous and is not resolved)`. The existing citation is sufficient.
- **Change the Early's Raid memo** (Disputes, Moorefield). Replace `Johnson gives his net loss as about 300 missing.` with `Johnson reports about 300 missing on reaching the Valley, of whom 150 had come in; his net loss reads as about 150, but the sentence is ambiguous.`

### VALLEY-R04 — VA117 `reinforcement-reports`: value asserts content the cited passage lacks

The value says Grant's August 9 message said "no brigade had been sent". The cited selection says only that the message "had been positive the other way". The "not one brigade" wording is in the Pond parent OCR, outside the selection.

- **Change the `value`.** Replace `Pond says Grant's August 9 message that no brigade had been sent contradicted reports from Harper's Ferry, and that Sheridan` with `Pond says Weber at Harper's Ferry reported reinforcements under Hill and Longstreet within five days' march and Leet sent a like telegram, but Grant's message of the 9th had been positive the other way; and that Sheridan`.
- **Add these citations** (`pond-sheridan-valley-selections-v1`, section `guard-hill`):
  - `p.126 (OCR page markers; not checked against print)`: `I have information from a source always found reliable that reinforcements under Hill and Longstreet are within five days' march of Early's pres- ent position,`
  - `p.127 (OCR page markers; not checked against print)`: `Captain Leets sent a like telegram.`
- **Change the `rationale`.** Append: `Pond's text dates Weber's message "July 11th" in this OCR; the context is August.`

### VALLEY-R05 — WV015 `casualty-records`: date scope stated that Pond does not give

Pond's sentence, "The loss of Gibbs's brigade, Merritt's division, was 35 killed and wounded", follows his account of both the August 28 Leetown action and the August 29 Smithfield action. It does not name a day.

- **Change the `value`.** Replace `Pond gives the August 29 loss of Gibbs's brigade as 35 killed and wounded;` with `Pond gives the loss of Gibbs's brigade, Merritt's division, as 35 killed and wounded, in a sentence following his account of both the August 28 Leetown and August 29 Smithfield actions, without stating the day;`
- **Add this citation:** `pond-sheridan-valley-selections-v1`, section `smithfield`, `p.141 (OCR page markers; not checked against print)`: `Merritt moved forward to Leetown, and there finding a cavalry force, handsomely defeated it,`

### VALLEY-R06 — VA118 and VA119 `reported-force-scope`, and the Sheridan's Valley memo: Pond's 17,195 is not "from a September 10 return"

Pond builds 17,195 by adding an assumed 1,700 for Fitz Lee to the September 10 "present for duty" figures. The 1,700 comes from Fitz Lee's June 30 and July 10 inspection reports. The result is Pond's mixed-date reconstruction, not a return total, and the contract requires such totals to be labelled as such.

- **Change the VA118 `value`.** Replace `Pond's appendix, from a September 10 return, gives Early's infantry with Fitz Lee as 17,195 without Kershaw and about 21,000 with him,` with `Pond's appendix adds an assumed 1,700 for Fitz Lee's division, taken from its June 30 and July 10 inspection reports, to the September 10 "present for duty" figures (a table garbled in OCR), giving 17,195 without Kershaw and, in round numbers, about 21,000 with him;`
- **Change the VA119 `value`.** Replace `Pond's appendix computes Early's infantry plus Fitz Lee at 17,195 without Kershaw (from a September 10 return)` with `Pond's appendix computes 17,195 without Kershaw by adding an assumed 1,700 for Fitz Lee's division, from its June 30 and July 10 inspection reports, to the September 10 "present for duty" figures`.
- **Add these citations to both dossiers** (`pond-sheridan-valley-selections-v1`, section `appendix-b-strength`, `p.266 (OCR page markers; not checked against print)`):
  - `If 1,700, for Fitz Lee, should be added to the figures already given,`
  - `The Inspection Reports of June 30th gave Fitz Lee's division`
- **Change both rationales.** Append: `Pond's 17,195 and 21,000 are his mixed-date reconstruction, not a return total.`
- **Change the Sheridan's Valley memo** (Opening strengths). Replace `Pond's appendix: Early's infantry with Fitz Lee, from a September 10 return, 17,195 without Kershaw and about 21,000 with him.` with `Pond's appendix: 17,195 without Kershaw and about 21,000 with him, reconstructed from the September 10 present-for-duty figures plus an assumed 1,700 for Fitz Lee taken from June–July inspection reports.`

### VALLEY-R07 — VA119 `casualty-records`: Pond's ranges are derived and overlap VA120

The value presents Pond's two ranges as if they were independent observations. Pond states two things about them in the same passage:

- He derives the Confederate 3,900–4,000 from Early's own 3,611 plus an assumed cavalry ratio.
- His Union table includes Crook's Fisher's Hill casualties, so it overlaps VA120. That overlap is a double-counting hazard.

- **Change the `value`.** Replace `Pond puts the Union loss at 4,900 to 5,000 and Early's at 3,900 to 4,000, nearly 2,000 of them prisoners.` with `Pond puts the Union loss at 4,900 to 5,000, saying exact figures are not ascertainable because his table's figures for Crook's Army of West Virginia include its slight Fisher's Hill casualties; he derives Early's 3,900 to 4,000 by adding to Early's reported 3,611 a cavalry loss assumed to be in the Union cavalry's ratio, about one-eleventh of the whole, and says nearly 2,000 were prisoners.`
- **Add these citations** (`pond-sheridan-valley-selections-v1`, section `opequon`):
  - `p.168 (OCR page markers; not checked against print)`: `The exact figures are not ascer- tainable, since in the following table the losses of Crook's Army of West Virginia include the very slight casualties it suffered at Fisher's Hill,`
  - `p.169 (OCR page markers; not checked against print)`: `supposing his cavalry loss to be in the same ratio as that of the Union cavalry, i.e., about one- eleventh of the whole,`
- **Change the `rationale`.** Append: `Pond's Confederate range is derived from Early's figure and is not an independent count; his Union figures for Crook's command overlap VA120 and must not be added to Fisher's Hill losses.`

### VALLEY-R08 — VA120 `casualty-records`: Pond's 1,300–1,400 is derived from Early's and Sheridan's figures

- **Change the `value`.** Replace `and puts Sheridan's loss at about 400 and Early's at 1,300 to 1,400.` with `and puts Sheridan's loss at about 400 and Early's at 1,300 to 1,400, deriving 1,340, besides some cavalry killed and wounded, by ascribing to the cavalry the 105 difference between Sheridan's 1,100 prisoners and Early's 995 missing.`
- **Add this citation:** `pond-sheridan-valley-selections-v1`, section `fishers-hill`, `p.180 (OCR page markers; not checked against print)`: `the difference of 105 between Early's and Sheridan's tally can be safely ascribed to the cavalry, thus making Early's total loss 1,340, besides some cavalry killed and wounded.`
- **Change the `rationale`.** Append: `Pond's range combines Early's report with Sheridan's prisoner count; it is not an independent observation.`

### VALLEY-R09 — VA122 `command-roles`: Torbert's report attributed to Pond

The cited order is quoted from Torbert's report. It is not Pond's own statement.

- **Change the `value`.** Replace `Pond says Wright, as senior officer, was left in charge while Sheridan went to Washington; that Wright ordered the cavalry to the left during the morning; and that Sheridan,` with `Pond says Wright, as senior officer, was left in charge while Sheridan went to Washington, and quotes Torbert's report that between nine and ten o'clock Wright, commanding the army temporarily, ordered him to move his whole cavalry force to the left of the army; Pond also says that Sheridan,`
- **Replace the citation.** Swap the existing p.232 citation for this quote, which is in the same section and on the same page: `Between nine and ten o'clock I was ordered by Major General Wright, commanding the army temporarily,`
- **Change the `rationale`.** Append: `Torbert's report is quoted by Pond and not separately selected.`

### VALLEY-R10 — VA115 `scouts-and-underestimate`: Pond's own sentence attributed to Rodes

The Rodes quotation ends at "…ought never to have occurred with old troops at all." The next sentence, "Ramseur supposed, from Vaughan's reconnoissance …", is Pond's own footnote text.

- **Change the `value`.** Replace `Pond, citing Rodes's letter, says Ramseur supposed` with `In a footnote, after quoting Rodes's letter, Pond says Ramseur supposed`.
- **Change the `rationale`.** Replace `Rodes's letter is quoted by Pond and not separately selected.` with `The Ramseur sentence is Pond's own, following his quotation of Rodes's letter, which is not separately selected.`

### VALLEY-R11 — Registry `or43-1-sheridan-valley-selections-v1` and the Sheridan's Valley memo: stale author-group statement

At the prepared commit, `or36-1-sheridan-overland-selections-v1` is already registered in group `sheridan-overland-reports`; it was added at `ec3f584`. It covers Sheridan's dispatches of May 13–June 16, 1864 and his report dated New Orleans, May 13, 1866. The new record's dependency note, "No earlier registry group for this author in this worktree; a parallel Overland pass is registering …", is therefore false for this repository. The memo repeats it.

- **Registry change.** Following the evidence contract, add a `metadata_only` revision, `or43-1-sheridan-valley-selections-v2`, that supersedes v1 and binds the previous entry's hash. In its `dependency_note`, replace `No earlier registry group for this author in this worktree; a parallel Overland pass is registering Sheridan's 1864 cavalry corps dispatches and 1866 report from Volume XXXVI as its own family, and the primary should reconcile the author grouping at merge.` with `The same author's Overland dispatches of May 13-June 16, 1864 and his report dated New Orleans, May 13, 1866 (Volume XXXVI Part 1) are registered as or36-1-sheridan-overland-selections-v1 in group sheridan-overland-reports. This Valley set is placed in its own group, following the registry's practice for separate report sets by one author (Averell's 1863 reports); the two groups are one author's accounts and are not mutually independent corroboration.`
- **Grouping choice.** Merging the two into one Sheridan 1864 group would also be defensible and would match the Early treatment; that choice belongs to the primary. Under either choice, the false sentence must go.
- **Memo change** (Families). Replace `A parallel Overland pass is registering Sheridan's Volume XXXVI dispatches and 1866 report as its own family. The primary should reconcile the author grouping at merge.` with `The Overland pass registered Sheridan's Volume XXXVI dispatches and May 13, 1866 report as sheridan-overland-reports; the Valley set is kept in its own group, and the two are one author's accounts, not mutually independent corroboration.`

### VALLEY-R12 — Registry: undated Early report and dispatches described as "October 21" and "September 23"

The Cedar Creek report's heading and date are on the missing pp.561–562, so its section date is correctly null. Nothing in the inspected OCR dates the report October 21. Pond calls it "Early's official report to Lee the day after the battle". The Mount Jackson dispatch's day is also lost. Only the free-text date descriptions are wrong; the section-date maps are correct.

- **`or43-1-early-valley-selections-v1`: metadata-only revision v2.** In the `dependency_note`, replace `Reports and dispatches of September 23-October 21, 1864 to Lee (and one to Lee's adjutant)` with `Reports and dispatches of September 25-October 20, 1864 to Lee (and one to Lee's adjutant), two dispatches whose day is lost in OCR (Mount Jackson and New Market), and the surviving end of the Cedar Creek report, whose heading and date are absent from this OCR`.
- **`or43-1-illinois-ocr-v1`: metadata-only revision v2, or record the fix in the reconciliation memo.** In the `inspection` note, replace `In this OCR Early's October 21 report begins mid-sentence on p.563` with `In this OCR Early's Cedar Creek report, whose heading and date are not in this OCR, begins mid-sentence on p.563`.

### VALLEY-R13 — Both memos: stale worktree counts

At `586811f`, the validator reports **153** draft dossiers: 127 from v1, 11 from Overland and these 15. The registry goes from **643/622** at `1e791f7` to **689/668**, and `docs/sources.md` already states this correctly. The memos instead say 142 dossiers, 609 → 636 → 655, and "first v2 campaign group".

**Early's Raid memo:**

- Replace `This is the first v2 campaign group outside the frozen v1 cohort in this worktree, drafted alongside` with `This v2 campaign group follows the Overland first pass and was drafted alongside`.
- Replace `The worktree now holds **142 draft dossiers** (the 127 v1 records and these 15).` with `The repository now holds **153 draft dossiers** (the 127 v1 records, the 11 Overland records and these 15).`
- Replace `from **609 entries / 588 raw paths** to **636 / 615**` with `from **643 entries / 622 raw paths** to **670 / 649**`.

**Sheridan's Valley memo:**

- Replace `The worktree now holds **142 draft dossiers** (the 127 v1 records and these 15).` with `The repository now holds **153 draft dossiers** (the 127 v1 records, the 11 Overland records and these 15).`
- Replace `from **636 entries / 615 raw paths** to **655 / 634**` with `from **670 entries / 649 raw paths** to **689 / 668**`.
- Replace `Before both campaigns the worktree registry held 609 / 588.` with `Before both campaigns the registry held 643 / 622 (after the Overland pass).`

## Advisories (not required)

- **VALLEY-A01 — VA114 `recorded-result`.** The sentence "Early retreated on the night of the 19th" follows "NPS says …", but its citation is Pond, p.84. Suggest writing "Pond says Early retreated that night (the 19th)".
- **VALLEY-A02 — WV014.**
  - `casualty-records`: Sheridan's 275 is "My loss", with no category. Pond's 260 is killed and wounded, "mainly in Getty's division". The categories and scope may differ; say so.
  - All claims: the dispatch the dossier calls "August 22" is headed "Angust 1864", with the day lost and "(Received 2 a.m. 23d.)". Its registry date is null. State this basis wherever the dossier dates it August 22.
- **VALLEY-A03 — VA119.**
  - `terrain`: Pond's "fought without field-works" sits beside Early's use of "the old rifle-pits constructed by General Johnston". Note the tension.
  - `reported-force-scope`: Grover's 6,797 is Pond's derivation from an after-action return (4,890 plus losses of 1,907); label it as derived.
- **VALLEY-A04 — VA119 `divided-army-report`.** Pond says Averell "sent word that he had been attacked by two infantry divisions". That is not the same as reporting that two divisions "had gone to Martinsburg". Suggest using Pond's wording.
- **VALLEY-A05 — VA122 `command-roles`.** Pond's Kershaw passage ("says Early … not in a condition to make the attack") sits next to a footnote citing "Early's Memoir". It is probably retrospective memoir text, not Early's report. Label it as possibly from the memoir.
- **VALLEY-A06 — MD007 `command-roles`.** Wallace's telegram credits Colonel Brown with holding the Baltimore pike bridge. His August report has Tyler take command there and obey the order to hold it ("This order General Tyler obeyed"). "Credits Tyler with holding the stone bridge" could note Brown.
- **VALLEY-A07 — VA116 `recorded-result`.** Crook's own report also says his left was thrown "in some confusion" before he ordered the withdrawal. Adding this would give a fuller account of the "good order" dispute.
- **VALLEY-A08 — DC001 `fortified-line`.** The `inherited` tag is sound for the permanent works. If the claim is later extended, keep the Sixth Corps' July 11 night intrenching of the picket line ("promptly intrenched the line", Pond p.68) separate: it is commander-created within the interval.
- **VALLEY-A09 — Grouping consistency.** Early's two 1864 volumes share one group. Sheridan's Overland and Valley sets, and Averell's 1863 and 1864 reports, are split. Whichever convention is kept, no count of corroboration may treat same-author groups as independent. Recording that rule once, in `docs/sources.md`, would prevent drift.
- **VALLEY-A10 — Section IDs that embed dates mapped null.** The IDs `early-1864-09-23` and `sheridan-1864-08-22` embed dates that the registry maps null. This is acceptable, but readers may take the ID as the date. The transcription notes could mention it.

## Unresolved and out of scope

- I did not adjudicate the preserved historical disputes. These include Monocacy fordability, the "good order" accounts at Kernstown and Tom's Brook, the gun and prisoner counts, the Guard Hill result, and the Cedar Creek losses.
- I did not seek the missing pp.561–562 of Early's Cedar Creek report or the basis of the frozen and live strength and casualty figures. Both are outside this offline review.
- Required corrections should be checked by the primary against the sources before any evidence change, as AGENTS.md requires.
