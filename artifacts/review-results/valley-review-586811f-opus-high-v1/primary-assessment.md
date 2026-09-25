# Primary assessment: Early's Raid and Sheridan's Valley first passes review

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `586811f3d24d6d21fa217e498d22471e94e0beb2`. Its
SHA-256 is `3767d752798bc4943212fae4d4e59cbd9ba2f4788c9ccaed0b55d6fbe195fa64`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `4e705de56c131379d288356a7787f6e82b3e75c7`; see [dispatch.json](dispatch.json).

Each required finding was checked against the retained source text before it was applied, and every
added quote occurs exactly once in its section; `python3 -m generalship check` passes. Superseded
dossiers are archived under `data/evidence/history/`. [correction.json](correction.json) binds the
corrected dossiers.

## Required findings

- **VALLEY-R01** (accepted applied): MD007 casualty-records: Wallace table footnote on missing (p.199) and Pond's stragglers remark and 1,500 to over-2,000 range (pp.58-59, relaying Wallace's suggestion on Tyler's reports) added; four citations; rationale says they qualify totals, not separate counts.
- **VALLEY-R02** (accepted applied): VA116 casualty-records: Hayes's 396 stated as a component of Duval's 513; Pond's 'somewhat uncertain' fugitives qualification and Colonel Campbell as source of the 317 added; rationale forbids summing; four citations (reviewer's three plus Campbell).
- **VALLEY-R03** (accepted applied): WV013 casualty-records and Early's Raid memo: Johnson's net loss read as about 150 (300 missing, 150 come in) with the antecedent ambiguity stated.
- **VALLEY-R04** (accepted applied): VA117 reinforcement-reports: unselected 'no brigade' wording removed; Weber's and Leet's warnings vs Grant's message 'positive the other way'; two citations (pp.126-127); rationale notes OCR 'July 11th' in an August context.
- **VALLEY-R05** (accepted applied): WV015 casualty-records: Gibbs's 35 no longer dated August 29; stated as following Pond's account of both the Aug 28 Leetown and Aug 29 Smithfield actions; Leetown citation added.
- **VALLEY-R06** (accepted applied): VA118/VA119 reported-force-scope and Sheridan's Valley memo: 17,195/21,000 described as Pond's mixed-date reconstruction (Sept 10 present-for-duty plus assumed 1,700 for Fitz Lee from June 30/July 10 inspections); rationales corrected; citations added (three VA118, two VA119).
- **VALLEY-R07** (accepted applied): VA119 casualty-records: Pond's 3,900-4,000 described as derived from Early's 3,611 plus assumed cavalry ratio; Union table overlaps VA120 (Crook's Fisher's Hill losses); rationale forbids adding; three citations (reviewer's two plus Pond's reference to 3,611).
- **VALLEY-R08** (accepted applied): VA120 casualty-records: Pond's 1,300-1,400 derivation (1,340 from the 105 prisoner difference) stated; rationale says not an independent observation; citation added.
- **VALLEY-R09** (accepted applied): VA122 command-roles: Wright's cavalry order attributed to Torbert's report quoted by Pond; p.232 citation replaced with the full order sentence plus Pond's 'says Torbert' (p.231); rationale notes Torbert not separately selected.
- **VALLEY-R10** (accepted applied): VA115 scouts-and-underestimate: the Ramseur sentence attributed to Pond's own footnote after the Rodes quotation (footnote structure confirmed at p.87); value and rationale corrected.
- **VALLEY-R11** (accepted applied): Metadata-only or43-1-sheridan-valley-selections-v2 supersedes v1 (bound metadata hash) with the reviewer's dependency note; own group sheridan-valley-1864-reports kept (reviewer default; merging with sheridan-overland-reports left to the primary); VA117/WV014/WV015/VA118 citations moved to v2; memo Families bullet corrected.
- **VALLEY-R12** (accepted applied): Metadata-only or43-1-early-valley-selections-v2 (dependency note: Sept 25-Oct 20 plus two day-lost dispatches and the undated Cedar Creek fragment) and or43-1-illinois-ocr-v2 (inspection note: Cedar Creek report, heading and date not in OCR); selection v2s name the OCR v2 as parent; VA119-VA122 Early citations moved to v2; builder family note and VA122 open question no longer say 'October 21'.
- **VALLEY-R13** (accepted applied): Both memos: 153 draft dossiers at 586811f; registry 643/622 -> 670/649 -> 689/668; 'first v2 campaign group' wording replaced.

## Advisories

- **VALLEY-A01** (accepted applied): VA114 recorded-result: Early's retreat on the night of the 19th attributed to Pond (with 'Wright remained at Snicker's Gap through the 19th' cited).
- **VALLEY-A02** (accepted applied): WV014: dispatch basis ('Angust 1864', day lost, received 2 a.m. 23d) stated in reported-force-scope and casualty-records with the heading cited; casualty rationale notes Sheridan's 275 has no category vs Pond's 260 killed and wounded.
- **VALLEY-A03** (accepted applied): VA119: terrain rationale notes 'without field-works' vs Johnston's old rifle-pits; Grover's 6,797 labelled derived (4,890 after action + 1,907 losses), two citations.
- **VALLEY-A04** (accepted applied): VA119 divided-army-report: Pond's wording used (Averell 'attacked by two infantry divisions'; Sheridan moved directly against Winchester).
- **VALLEY-A05** (accepted applied): VA122 command-roles: Kershaw passage labelled as apparently from Early's memoir (Pond cites 'Early's Memoir' in the adjoining footnote); two citations added.
- **VALLEY-A06** (accepted applied): MD007 command-roles: Tyler took command at the bridge (August report) and Colonel Brown credited in the July 10 telegram; three citations; memo command bullet notes it.
- **VALLEY-A07** (accepted applied): VA116 recorded-result: Crook's own 'threw it in some confusion' and 'My left soon reformed' added and cited; memo Kernstown dispute bullet updated.
- **VALLEY-A08** (kept as is): DC001 fortified-line: advisory is conditional on a later extension; the inherited tag covers only the pre-existing works and the claim is not extended. Recorded in the Early's Raid memo.
- **VALLEY-A09** (accepted applied): Grouping-consistency rule belongs in docs/sources.md, which this reconciliation may not edit; left to the primary. The Sheridan v2 dependency note states same-author non-independence for that author. Applied by the primary: docs/sources.md now states that same-author groups never count as independent corroboration.
- **VALLEY-A10** (accepted applied): Raw transcription notes are immutable, so the note is added to the document_date_note of the new Sheridan and Early v2 records instead (section IDs sheridan-1864-08-22 and early-1864-09-23 name inferred dates mapped null).

This AI review is a separate analysis, not historical adjudication or proof of source independence.
The dossiers remain drafts; no model input changes.
