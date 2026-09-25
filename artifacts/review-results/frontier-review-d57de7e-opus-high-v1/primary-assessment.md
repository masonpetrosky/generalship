# Primary assessment: Frontier and Texas coast first passes review

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `d57de7e5a8fd26540f132c1aa845ca711d66fc0f`. Its
SHA-256 is `26e1daa4d1d06b3713b1025fae180d3f7279695a648b9e90d8041ea7f68507f9`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `5a09f91d54f816372f6ef6907649d4b5f4dbea1f`; see [dispatch.json](dispatch.json).

Each required finding was checked against the retained source text before it was applied, and every
added quote occurs exactly once in its section; `python3 -m generalship check` passes. Superseded
dossiers are archived under `data/evidence/history/`. [correction.json](correction.json) binds the
corrected dossiers.

## Required findings

- **FRC-01** (accepted applied): Holds: OR XIII/XV/XXVI-1 and ORN 19 parents were deduplicated at merge (66 records added, not 74). Memos corrected (sioux-1862 10->8, texas-coast-1862 13->9, texas-coast-1863 7->5; galveston-1863 parent wording); metadata_only successors or15-davis-galveston-selections-v2 and or15-magruder-galveston-selections-v2 fix the stale dependency notes; TX003 cites them.
- **FRC-02** (accepted applied): Holds (Crocker p.218 'The next day ... Henry Janes was kedged over'; Spaight p.144 'Early the next morning'; Debray p.143 'this morning'). TX001 recorded-result value/rationale appended as proposed with the three citations; frozen interval retained.
- **FRC-03** (accepted applied): Holds: Spaight's 'no information as to the force of the enemy' is dated Sept 26 after the evacuation. TX001 express-and-messenger value replaced; p.145 citation added.
- **FRC-04** (accepted applied): Holds (Davis p.207; Magruder Jan 2 report p.211). TX003 casualty-records appended with Union naval dead and two citations.
- **FRC-05** (accepted applied): Holds: the passage says only the track 'had been permitted to remain'. TX003 guns-rail-and-stores wording replaced.
- **FRC-06** (accepted applied): Holds: (a) Bancroft 200 figure now cited (p.632); (b) marshal/warrants wording replaced with Kinney's requisition, cited p.187.
- **FRC-07** (accepted applied): Holds: retained catalog has no edition field and reads 'Also published separately, 1890'. metadata_only successors ia-bancroft-utah-metadata-v2, bancroft-utah-ocr-v2, bancroft-utah-bear-river-selections-v2 (reparented to ocr-v2) carry the proposed edition text; ID001 cites the selection v2.
- **FRC-08** (accepted applied): Holds: Sibley's 3 killed/4 wounded is his column's loss 'in actual combat' for the whole expedition. ND001 value/rationale corrected, p.358 citation added.
- **FRC-09** (accepted applied): Holds: Sibley's basis is 'various sources ... conversations with our half-breed scouts'; no prisoners. ND003 value and rationale corrected, p.356 citation added.
- **FRC-10** (accepted applied): Holds. ND004 ravines (inherited) value replaced and 'about 15 miles west of James Biver' cited (p.560); the line-of-battle statement moved, with its p.560 citation, to the unresolved command-roles claim.
- **FRC-11** (accepted applied): Holds (Sully p.559 ambuscade, 4 killed; Hall 6). ND004 casualty-records value/rationale appended, citation added; not reconciled.
- **FRC-12** (accepted applied): Holds (Crocker p.301 4 o'clock; Franklin p.297 3 o'clock; Dowling p.311 3.40). TX006 command-roles appended with three citations.
- **FRC-13** (accepted applied): Holds: (a) committee 'this massacre' cited p.iv; (b) Smith 'About- 500' cited p.6; (c) Smith on Chivington's positive orders and presumed General Curtis added to command-roles (p.8), plus 'On the day of the attack.'
- **FRC-14** (accepted applied): Holds: report's flag passage follows Smith's wording and cites 'the Indian interpreter and others'. metadata_only successor joint-committee-sand-creek-report-selections-v2 carries the proposed dependency note; CO001 cites it; open_questions[1] and memo family paragraph appended.
- **FRC-15** (accepted applied): Sand Creek memo bullet replaced with the proposed statement of consequences.

## Advisories

- **FRA-01** (not adopted): docs/sources.md is outside this reconciler's scope; proposed wording given to the primary. Groups unchanged.
- **FRA-02** (not adopted): docs/sources.md is outside this reconciler's scope; proposed wording given to the primary.
- **FRA-03** (accepted applied): Applied in TX005 reported-force-scope rationale with Barrett's 'to department headquarters at New Orleans' citation; the Barrett record's dependency note is not revised (no new source record).
- **FRA-04** (accepted applied): Verified absent from the July 31 selection. ND005 mountain-and-ravines and recorded-result record both NPS statements as not found, with NPS citations.
- **FRA-05** (accepted applied): TX006 command-roles records Crocker's signature (Acting Volunteer Lieutenant) against Franklin's Lieutenant-Commander/Captain; frozen Captain not adopted.
- **FRA-06** (accepted applied): All four verified in the Smith and committee selections and added to CO001 (casualty-records, stated-and-attributed-aims, command-roles); characterizations unchanged and not adopted.
- **FRA-07** (accepted applied): TX002 recorded-result wording now attributes the statement to the frozen description it cites.
- **FRA-08** (accepted applied): 'include' softened to 'may include' in TX003 and TX006 rationales and the texas-coast-1863 memo.
- **FRA-09** (accepted applied): ND003 reported-force-scope names Sibley's combined bands, cited p.356, and notes this is not evidence about Inkpaduta.
- **FRA-10** (accepted applied): McPhaill's Dead Buffalo Lake passage (p.360) cited in ND001 and ND002 casualty-records; his 31 killed kept unassigned.
- **FRA-11** (accepted applied): ND004 recorded-result records Hall's 'northeasterly' against NPS 'northwest' (both cited); casualty rationale notes the undated estimates.
- **FRA-12** (accepted applied): TX001 records the express's 'one gunboat and three or four transports' against Spaight's vessels, and Debray's ~900 relief force as unengaged context.
- **FRA-13** (accepted applied): MN002 command-roles cites Sibley p.279 'he led his men to a charge and cleared the ravine'.
- **FRA-14** (not adopted): Renaming magruder-big-bethel-reports needs a registry-wide documented migration; kept, as the memo already explains.

This AI review is a separate analysis, not historical adjudication or proof of source independence.
The dossiers remain drafts; no model input changes.
