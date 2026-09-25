# Chickamauga Campaign: separate source review (Opus 5.5 `high`)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This was a fresh-context subagent. The author's conversation was not an input.
- **Date:** 2026-09-25.
- **Commits:**
  - prepared `93a269449577504ad3818278d7a08883024ab127`;
  - previous `5b83af9d3d8f715697f8656a11b5f9224ce0f311`;
  - assignment bundle `5948133d5ea4010e0f644b5aa32749241c14f075`. Worktree HEAD is this bundle commit. Its only difference from the prepared commit is the two assignment files.
- **Assignment:**
  - `assignment.md` sha256 `8e13c622cc1bfd2bb2e60c655583b2169d6493c67c8fa6026369b04981c22774`;
  - `inputs.json` sha256 `0d8a8b140294378038086a4b8d95e4a0a7dfb169f202b90af31ae5e2b202332d`.
- **Input hashes:** all 42 bound paths match, both in `git show 93a2694:<path>` and in the worktree. There are **no mismatches**.
- **Outcome: corrections required** (CH-R1 to CH-R8, all minor extraction/scope fixes). No finding changes a status, phase tag, unknown or model input.

This is an AI review: a separate analysis. It is not human historical adjudication, independent corroboration or feature admission.

## Coverage actually inspected

- **Governance:** read AGENTS.md, the evidence contract and the committed diffs to README, the roadmap, methodology, sources.md, cli.py and the tests. I skimmed but did not reread README, methodology and roadmap in full.
- **Dossiers and memo:** read TN018, GA003 and GA004 in full: **27 claims, 3 null unknowns and 135 citation occurrences**, with 7 dimensions per record. Also read the memo `docs/research/chickamauga-first-pass-v1.md`.
- **Frozen rows:** checked every cited frozen cell against the battle, force and commander rows for all three records.
- **Sources read in full:**
  - the three NPS text snapshots;
  - the Cist selection (13 sections);
  - the Hill selection;
  - the Hindman selection (October 22 transmittal and October 25 report);
  - the Bragg selection (September 24; September 29 with the September 27 return; October 9; three December 28 passages).
- **Source records:** inspected all 12 new source records and the OR catalog metadata fields.
- **Parent OCR:** I did not read the whole parent volumes. I read only the page-header context around every selection, plus the OR XXX Part 2 summary of principal events near parent lines 330–410.

**Derivative replay (mechanical).**
- The three NPS `.txt` files reproduce byte-for-byte from their HTML parents under the recorded transform.
- All four sectioned selections (Cist, Hill, Hindman, Bragg) reproduce exactly from their recorded character ranges with whitespace-only collapsing. There are no extra or missing sections.
- `cist-cumberland-ocr-v1` has an unchanged entry and file (`4a3f4c2c…2429`).

**Page-marker maps.** Each locator was checked against the nearest parent running head.

| Source | Pages | Header notes |
| --- | --- | --- |
| Cist | pp.178–181, 185–186, 195, 203, 205–208, 211, 220–223, 225, 227–229 | p.194 is a plate page with the p.195 head directly after it. The p.209 head comes after the Horseshoe Ridge passage, so p.208 is correct. p.206 reads "20'j" and is correctly marked inferred. |
| Hill | p.136 → "87" → p.138 | p.137 is correctly inferred. |
| Hindman | pp.292–298 | The p.292 head precedes the transmittal. |
| Bragg | pp.23–27, 31–35, 36 → "87" | The September 29 letter and the return lie on p.25, before the p.26 head. p.37 is correctly inferred. |

No locator relies on a missed or misread header. OCR readings are reported, not corrected; examples are "jniles", "imj)assable", "watei", "Total effective^" and the blank in Hill's "fast day (August)".

**Mechanical state at the prepared commit:**
- Dossier coverage:
  - 108/127 dossiers, 19 without;
  - 27/36 complete groups by presence.
- Registry: 504 records / 488 raw paths, up from 492 / 476. No earlier record is changed or missing.
- Frozen files: only the three dossiers were added under `data/evidence`. The 105 older dossiers and 76 history files are unchanged, as are the cohort, both admission proposals, admission-check, baseline, battles and the three CWSAC CSVs.
- Model state: zero promoted rows. The baseline has 23 eligible engagements in 13 groups, with Brier 0.2768816348133779 against 0.25.
- Receipt: all 198 input, 504 source and 7 output hashes verify. Only cli.py and sources.json changed as inputs. Baseline, battles and admission-check outputs are unchanged.
- Packets: each has three JSON blocks. The draft equals its dossier and the registry equals `data/sources.json`.
- Tests: `make check` ran offline: 82 tests OK and `artifacts_written: false`. No build or packet command was run.
- Next group, confirmed independently from the frozen CSV: **East Tennessee Campaign [September-October 1863]**, TN019 and TN020 (earliest start 1863-09-22).

**Confirmed without correction:**
- **Scope.** TN018 is limited to one day. GA004's interval ends September 20.
- **Force figures kept separate and not adopted:** Cist's 55,000 / 67,548 / 70,000, Bragg's 70,000 / 35,000 / 5,000 and the September 27 return of 38,846, Hindman's order estimate, Mackall's estimate and Cist's 30,000.
- **Casualty arithmetic.** Cist's totals add up: 16,336 = 1,687 + 9,394 + 5,255, and 20,950 = 2,673 + 16,274 + 2,003. "Nearly if not quite 18,000", "two-fifths" and the frozen/live 34,624 are all kept separate.
- **Frozen versus live commanders.** Breckinridge's frozen entry is kept apart from Cist's placement south of La Fayette. The live ranks (Hill "Colonel", Hindman Brigadier General, Bragg Major General) are not adopted.
- **Dispute framing.** The McLemore's Cove dispute is framed correctly, with Bragg's suspension order attributed as quoted by Hindman. The judgments by Bragg on Polk and by Cist on Rosecrans are attributed. No commander receives additive or automatic credit.

## Required corrections

All replacement quotes below were verified to occur exactly once in the named section. Where a quote is new to the dossier, its page was checked against the header map.

- **CH-R1 — TN018 `unwarned-town`: attribution.**
  - *Problem:* "General Clayton, sent up the river" misstates Hill. According to Hill, Clayton's *brigade* moved up to Birchwood, and Clayton was instructed to send an *officer* up the river.
  - *Replace* "and that a few nights before General Clayton, sent up the river, had found no cavalry pickets for 40 miles" *with* "and that a few nights before, after Clayton's brigade had been moved up to Birchwood, General Clayton, instructed to send an officer up the river to meet the cavalry pickets, reported finding no pickets for 40 miles".
  - *Add citation:* `or30-2-hill-chattanooga-selections-v1`, section `hill-chattanooga`, the existing p.137 inferred locator, quote "General Clayton was instructed to send an officer up the river until he met our cav- alry pickets".
- **CH-R2 — TN018 `feint-and-attention`: interval scope.**
  - *Problem:* NPS attributes the attention effect to shelling "continued periodically over the next two weeks", which is outside the one-day frozen record.
  - *Replace* "and that the shelling helped keep his attention there" *with* "and that the shelling, continued periodically over the next two weeks (beyond this one-day record), helped keep his attention there".
  - *Add citation:* `nps-tn018-v1`, Description, quote "Continued periodically over the next two weeks,".
- **CH-R3 — GA003 `cove-and-blocked-gaps` rationale: unsupported "by both sides".**
  - *Problem:* No inspected passage says Union troops obstructed any gap, and Cist does not name who obstructed Stevens's Gap.
  - *Replace the rationale with:* "Hindman reports the Dug and Catlett's Gap blockade as information from citizens and cavalry, confirmed by his scouts, existing for several days before September 10. Cist has Hill report both gaps closed by felling timber and says Stevens's Gap was found obstructed, without naming who obstructed it. The obstructions predate or fall within the operations and their makers are not all identified, so no inherited tag is used. No map verification."
  - *Add citation:* `cist-chickamauga-selections-v1`, section `bragg-and-the-cove`, p.185, quote "both gaps — Dug and Catlett's — had been closed by felling timber,".
- **CH-R4 — GA003: Hindman's post-suspension interest is missing from the dossier.**
  - *Problem:* The memo and source record say this, but the dossier never cites the October 22 transmittal or labels Hindman's construction as retrospective self-defense.
  - *`delay-and-suspension` rationale:* prepend "Hindman's October 25 report was written after Bragg's September 29 suspension order, and his October 22 transmittal asks leave to publish it against 'calumnies'; his account is interested self-defense, not a contemporaneous record."
  - *`attack-orders-and-withdrawal` rationale:* replace it with "Stated orders and the recipient's construction from interested accounts; Hindman's construction of the midnight order was written after his suspension. Not a causal estimate."
  - *Add to `delay-and-suspension`:*
    - (a) `or30-2-hindman-mclemores-cove-selections-v1`, section `hindman-1863-10-22`, locator "p.292 (OCR page markers; not checked against print)", quote "Many calumnies have been circulated against me in connection with that affair.";
    - (b) section `hindman-1863-10-25`, p.298, quote "The general commanding saw fit, on September 29, to issue the fol- lowing order :".
- **CH-R5 — Value content without a citation.**
  - *GA003 `recorded-result`:* "under constant pursuit and fire" is uncited. Add `nps-ga003-v1`, Description, quote "All of this was accomplished under constant pursuit and fire from the Confederates."
  - *GA004 `sweep-and-hold-the-road`:* "he says his reconnaissance found the road to Chattanooga open" is uncited within the claim. Add `or30-2-bragg-chickamauga-selections-v1`, section `bragg-1863-12-28-battle`, p.33, quote "proved the important fact that this greatly desired position was open to our possession."
- **CH-R6 — GA004 `reported-force-scope`: Bragg's 70,000 is undated.**
  - *Problem:* In the December 28 narrative, the figure is tied to August 20. As written, it can read as simultaneous with the late-August 35,000.
  - *Replace the Bragg sentence with:* "In his December 28 narrative Bragg says that when it was ascertained on August 20 that Rosecrans had crossed the mountains, his effective infantry and artillery amounted to fully 70,000; that after the last of August, with two small divisions from Mississippi, his own effective force exclusive of cavalry was a little over 35,000; and that five small brigades of Longstreet's corps, about 5,000 effective infantry, arrived in time to participate, three on the 19th and two on the 20th."
  - *Add citations:* `bragg-1863-12-28-opening` p.26 "On August 20, it was ascertained certainly that the Federal army"; p.27 "By the timely arrival of two small divisions from Mississippi"; `bragg-1863-12-28-battle` p.33 "three of them on the 19th and two more on the 20th."
  - *Memo, same fix:* replace "Bragg gives Rosecrans fully 70,000 and himself a little over 35,000 exclusive of cavalry at the end of August" with "Bragg's December 28 narrative gives Rosecrans fully 70,000 effective infantry and artillery as of August 20, and himself a little over 35,000 exclusive of cavalry after the last of August".
- **CH-R7 — GA004 `command-roles`: Cist's qualifier on Wood is dropped.**
  - *Problem:* Cist says "to this extent" Wood is responsible for "the great disaster". That is narrower than "responsible for the gap".
  - *Replace* "Cist holds Wood responsible for the gap" *with* "Cist says that, by executing an order he knew could not be carried out literally rather than asking what it meant, Wood was 'to this extent' responsible for the disaster that swept the right wing from the field".
  - *Replace the existing Cist p.223 quote with the fuller:* "and to this extent he is responsible for the great disaster which swept the right wing of the Army of the Cumberland from the field of battle on the 20th."
  - *Add citation:* p.222, "rather than ask an explanation of it from his commanding officer."
  - The memo line "Cist blames Wood's execution of the order" may stay.
- **CH-R8 — GA004 `casualty-records`: prisoner-count timing scope.**
  - *Problem:* The same December 28 narrative credits Wheeler with prisoners captured on the 20th **and 21st**.
  - *Append to the rationale:* "Bragg's prisoner figures are report-date cumulative claims; his December 28 narrative credits Wheeler's cavalry with captures on the 20th and 21st, so neither figure is confined to the September 18–20 interval."
  - *Add citation:* `bragg-1863-12-28-battle`, p.34, quote "important service was rendered both on the 20th and 21st by his command, especially in the capture of prisoners and property".

## Non-blocking observations (no correction required)

- **O1 — GA004 boundary note ("withdrawal to Rossville and Chattanooga on September 21–22").**
  - No dossier passage cites this. Support does exist in the pinned parent's summary of principal events: "21-22, 1863.— Army of the Cumberland retreats to Chattanooga, Tenn."
  - The OR30-2 OCR record's inspection note does not list that summary. It may be worth recording it there.
  - The same summary dates the battle to September 19–20. The frozen interval of September 18–20 rightly stays.
- **O2 — Stale Cist dependency note.**
  - `cist-chickamauga-selections-v1` inherits the parent's dependency note ("across five records"; "Duke, Bragg, Buell"). That is stale for this selection: Cist now spans 15 records, and this selection quotes Wood, McCook, Thomas, Hindman, Bragg and the Bond order.
  - The transcription note already excludes quoted material as separate families. A `metadata_only` revision is optional.
- **O3 — GA004 terrain: "night of the 19th".**
  - The cited Cist section says only "During the night". The parent context, which precedes the selection with Polk's delay on the 20th, supports the night of the 19th–20th. Widening the selection is optional.
- **O4 — Memo ranges.** The memo writes "4,000–5,000" and "12,000–15,000", while the dossier keeps the sources' "4,000 or 5,000" and "12,000 or 15,000". Using the sources' wording in the memo is preferable.
- **O5 — Cist's shelling date is ambiguous.** Cist's "opened fire on the next day" is internally ambiguous against his later "five days after the surprise" (August 26 → August 21). The dossier assigns no date, which is correct.

Unresolved and left visible, as the dossiers state:
- the start of TN018's shelling relative to the one-day record;
- all opening strengths;
- the McLemore's Cove responsibility dispute;
- the Chickamauga command judgments;
- casualty reconciliation.

Deferred items remain deferred: Union reports, returns, maps and Hindman's exhibits. No strengths, scores, causal effects or probabilities are proposed.
