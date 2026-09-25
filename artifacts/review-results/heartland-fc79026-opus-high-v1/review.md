# Separate review: Confederate Heartland Offensive first pass (TN005, TN006, KY007–KY009)

**Outcome: corrections required.** There is one low-severity required correction (HO-R1). The other 53 claims are accepted as bounded draft extractions. Five nonblocking notes (HO-N1 to HO-N5) do not change any claim. This is an AI source review. It is not human historical adjudication, independent corroboration or feature admission.

## Reviewer record

- Reviewer: Claude Opus 5.5 (`claude-opus-5-5`), `high` reasoning effort. I ran as the repository's `evidence-reviewer` subagent with fresh context and did not see the author's conversation. No task ID was visible to me.
- Date: 2026-09-24. Work was offline: no network, no new sources, no agents. I modified no primary artifact, did not commit and did not push. This file is the only one I wrote.
- Checked at HEAD `4180a69fe8f324b64599e3f416b077f30c19723f` (review bundle). Prepared commit: `fc79026845cde8b8e3544ab460e2b4e3d6d595d1`. Previous commit: `686b787c7bbd797e3bece51681f387b54bf49f17`. Policy commit: `29ab815b10cb07148de1c259dfe1f83693e6f593`.
- Assignment `assignment.md` has sha256 `8277e41b7a744af630fcc40be9ccb2f492c0e94b3dcd40ad85efb549df65baba`. Input manifest `inputs.json` has sha256 `ab93fbc34ef06308d0ebbc52f0c8493db92b1e0845146425b75adae7f9197e21`. **All 48 bound input hashes match; there are no mismatches.** The working tree was clean before and after the review.
- `git diff fc79026 29ab815` touches only `.claude/agents/evidence-reviewer.md`, AGENTS.md, README.md and docs/roadmap.md. No evidence, source or generated artifact changed.

## Scope actually inspected

- Documents: AGENTS.md, README, methodology, evidence contract, the roadmap's current-priority section, the Heartland diff in `docs/sources.md`, and the Heartland memo in full.
- Dossiers: all **54 claims / 155 citation occurrences** in the five dossiers were read against their cited passages. That includes the **6 null unknowns**: five opening-personnel claims and Richmond logistics. Each dossier has all seven dimensions and exactly two families (`nps-cwsac`, `cist-cumberland-1882`). Arnold/CWSAC is correctly grouped with NPS.
- NPS: all five retained summaries were read in full.
- Cist: I read the catalog metadata (title, creator, date, publisher, sponsor, scan provenance), the OCR title page, preface and contents, and all five battle selections in full, including running headers and the Perryville map-label OCR. Parent OCR was used only for section boundaries and the page markers before each section. I did not read the whole book.
- Frozen CSV rows: all battle, force and commander row sets for the five records (5 battle, 10 force, 12 commander rows). Every cited cell matches, including the five rank-cell citations covering the four commanders with live-heading conflicts: Negley, Kirby Smith (TN005 and KY007), Forrest and Bragg.
- Source records: all 13 new records and their `source_kind` values. The OCR and selection are `retrospective_history`; the catalog record is `digital_catalog_metadata`; NPS is `government_secondary_history`. None is recorded as a participant witness. The preface's missing date is recorded as null, and every selection's section date is null.

## Mechanical results

- **Derivatives:** all six replay exactly. The five NPS texts were rebuilt from the retained HTML with the recorded HTMLParser transform. The six Cist sections were rebuilt from `cist-full.txt` using the recorded half-open Unicode ranges and whitespace-only collapsing.
- **Page locators:** all 77 Cist citations match the page implied by the OCR page markers. Each quote occurs once in its section and none crosses a page marker. The memo's page spans (32–34, 43–45, 53–54, 57–59, 61–70) match the markers and the OCR contents (Ch. IV p.31, Ch. V p.48, Ch. VI p.61).
- **Coverage:** 45/127 cohort dossiers, 82 without, and 9/36 complete campaign groups by presence. The registry has 286 records / 283 paths. All 273 previous records are identical and none of their 270 raw paths changed.
- **Protected files:** all 52 are byte-identical to `686b787`. They are 40 older dossiers, 6 history revisions, the cohort, both admission proposals, admission-check, baseline and battles.
- **Baseline and admission:** 23 eligible / 13 groups; strength Brier `0.2768816348133779` against equal odds `0.25`. Admission shows `promoted_rows` 0 and 18 blocked / 22 excluded.
- **Next group:** I confirmed independently that the earliest-starting incomplete group is **Northern Virginia Campaign [August 1862], VA022–VA027** (starts 1862-08-09). Maryland (1862-09-12) comes after it.
- **Packets:** each of the five packets matches the `research_packet` output rebuilt in memory, byte for byte. Their three JSON blocks parse and equal the cohort row, the current dossier and the 286-record registry.
- **Receipt:** all 65 input, 286 source and 7 output hashes match.
- **`make check`:** passes offline (82 tests OK; `artifacts_written: false`). No build or packet command was run.

## Assignment-specific checks (all confirmed unless noted)

- **Murfreesboro result:** the live NPS result field reads "Union Victory". Its own narrative says "all of the Union units had surrendered to Forrest's force". The frozen "Confederate victory" is kept and the conflict is recorded as `disputed`.
- **Force scopes:**
  - Murfreesboro: frozen approx. 1,400 CS / 900 US, against Cist's "about two thousand" and 1,700 surrendered. These are kept as different populations; the surrender count is not used as a garrison count.
  - Richmond: 7,000 / 12,000 are Cist's whole-command figures.
  - Perryville: live 55,000 and the narrative's "nearly 55,000" on October 7; Cist's 58,000 effective, "Less than one-half" in action, and Hardee's "some sixteen thousand". All are kept separate.
  - Live zeros are never treated as measured absence.
- **Casualties:** all five frozen/live pairs match the CSV cells and NPS fields. Richmond's "approximately 4,000" captured (NPS) and "over two thousand captured" (Cist) are kept separate from the totals and are not added to them. Cist's Perryville OCR does print 4,348 with 916 / 2,943 / 189, and those components sum to 4,048.
- **Command and clocks:** confirmed as drafted.
  - Chattanooga: Kirby Smith "arrived on the 8th"; Duke, as quoted by Cist, names Leadbetter commandant.
  - Murfreesboro: Crittenden returned July 11 per Cist, against July 12 per NPS, and Cist says there was "no one in command".
  - Richmond: Manson and Cleburne led before Nelson and Smith arrived.
  - Munfordville: command passed Wilder → Dunham → Wilder (Gilbert's arrest order; 7 p.m.). Cist dates the first demand to the 13th; NPS dates the refusal to the 14th.
  - Perryville: Polk had immediate command. The two Bragg reports, dated October 12, 1862 and May 20, 1863 as quoted by Cist, are correctly attributed.
  - Murfreesboro clocks: NPS 4:15–4:30, Cist about 5:00.
  - No listed commander receives automatic sole credit.
- **Phase tags:** the one `commander_created` tag (Forrest refusing to withdraw at one o'clock) fits as an in-battle decision attributed by Cist. The assignment says there are two `inherited` tags, but the dossiers contain **three**: TN006 supply center, KY007 department change and KY008 bridge and works. I checked all three and each fits as inherited site or command context.
- **Attribution:** Duke's river counterfactual, NPS's statement on Buell's reserves, Cist's inference about Louisville intent and Wilder's reported 25,000 all remain attributed. None is treated as a verified message chain, a true strength or a causal effect.
- **Excluded neighbors:** Jasper, the October 7 Peters Hill fight and later pursuit are excluded. The night fight for the creek pools appears only as logistics context and is not added as an engagement.

## Required correction

**HO-R1 (KY009 `union-unengaged-forces`, population scope, low severity).** The rationale calls Crittenden's corps "the idle corps". But the same p.68 passage says "Wag- ner's brigade of Wood's division became engaged" and "The rest of Crittenden's corps was not engaged in the action." Cist therefore reports the corps as largely, not wholly, unengaged. The claim's value is a faithful paraphrase, but together with the rationale it overstates the unengaged population. Exact replacement:

- `value`: "Cist says Thomas, arriving with Crittenden's corps, was directed to take position on the right and wait for orders, and waited the entire day without receiving any; apart from Wagner's brigade of Wood's division, Crittenden's corps was not engaged. Only part of Gilbert's corps was engaged and McCook's corps bore the attack."
- `rationale`: "Retrospective account of command use. Cist reports one brigade of Crittenden's corps engaged, so that corps was largely, not wholly, unengaged. Whether Thomas's wait without orders reflects Buell's choice, missing information or both is not adjudicated; Buell is not assigned the tactical result automatically."
- `citations`: keep the four existing ones and append these two. Both quotes occur exactly once in the section.
  - `{"source_id": "cist-heartland-selections-v1", "section": "perryville-approach-and-battle", "locator": "p.68 (OCR page markers; not checked against print)", "quote": "Wag- ner's brigade of Wood's division became engaged"}`
  - `{"source_id": "cist-heartland-selections-v1", "section": "perryville-approach-and-battle", "locator": "p.68 (OCR page markers; not checked against print)", "quote": "The rest of Crittenden's corps was not engaged in the action."}`

This changes the counts: KY009 goes from 41 to 43 citations and the batch from 155 to 157. Those numbers appear in the memo table and header, README, roadmap, and the `cli.py` report text and generated report. The KY009 packet, evidence checks and receipt need regenerating. Claim and unknown counts do not change. The primary should verify the fix against the source before applying it.

## Nonblocking notes (no correction required)

- **HO-N1:** In the OCR title page, the second staff name is garbled: "STAFF OF MAJ0R-CENERAL THci"^,™". "Thomas" is a plausible reading, not a legible one. The characterization of Cist as an interested Union staff historian rests on the legible "ROSECKANS" (Rosecrans) alone. The primary could optionally write "Rosecrans and a second major-general (OCR garbled; apparently Thomas)".
- **HO-N2:** The Cist `edition` field says "vol. VII … per catalog and OCR title". The catalog gives no series or volume, and the OCR title reads "CAMPAIGNS OF THE CIVIL WAR.-VW.". The volume number is supported by OCR signature marks ("VII.— 1"), not by the catalog. This is wording only.
- **HO-N3:** The memo's "The whole Perryville chapter to Bragg's arms quotation, pp.61–70" is exact in its pages. But Chapter VI continues to p.86 (Ch. VII starts at p.87), so "whole" could mislead.
- **HO-N4:** KY008 `transport-center` paraphrases the NPS clause "the Confederate control affected the movement of Union supplies and men". That clause is in the cited sentence but outside the quoted span. Adding it would tighten the citation.
- **HO-N5:** Cist's Munfordville sequence has a second-demand "following day" and then "Two days later" another attack, while also dating the surrender to 2 a.m. on the 17th. This is an internal tension in Cist. The dossier adopts none of these relative dates, so it only adds to the deferred chronology question.
- **Out of scope:** `docs/evidence-contract.md` ("Research and review") and parts of the methodology still describe the Astra `xhigh` reviewer. Policy commit `29ab815` did not update those documents.

## Limits

All claims rest on NPS/CWSAC (one family) and on Cist, an interested 1882 retrospective history. Duke, Bragg and Buell appear only as quoted by Cist and were not inspected as originals. No orders, returns, maps or print pages were inspected by the author or by me. Every opening strength remains unknown, and every disputed value remains disputed. This review admits no features, does not change the baseline and does not establish that any source is independent.
