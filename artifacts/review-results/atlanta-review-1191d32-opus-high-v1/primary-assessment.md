# Primary assessment: Atlanta Campaign first pass review

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `1191d32433575d224120a6d2aa1df8e381dcecf7`. Its
SHA-256 is `a810d97afaffdf1666f6cdf0cf29ae9092b2972e82c817de3da7e0782f9fbef3`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `794993bcabea8dde394871fe31e50d8757357677`; see [dispatch.json](dispatch.json).

Each required finding was checked against the retained source text before it was applied, and every
added quote occurs exactly once in its section; `python3 -m generalship check` passes. Superseded
dossiers are archived under `data/evidence/history/`. [correction.json](correction.json) binds the
corrected dossiers.

## Required findings

- **ATL-R1** (accepted applied): Memo: repository-wide coverage (143/384, 37/119, '127 earlier dossiers') and registry totals (656/635, 609/588) removed rather than updated, per the RECONCILE brief; only campaign counts and 'adds 47 source records' remain. Stale validation bullet replaced: check and 134 tests pass; test_repository_dossiers_have_resolvable_passages already accepts cohort-v2 IDs. The reviewer's replacement totals (169/384, 40/119, 736/715) were not inserted.
- **ATL-R2** (accepted applied): GA009 reported-force-scope: Cox narrative (Adairsville) vs Cox Appendix A and Johnston (Cassville, May 18) on French's division; value and rationale corrected; three citations added (Cox pp.242, 243; Johnston p.615). Verified in context.
- **ATL-R3** (accepted applied): GA012 reported-force-scope: dismounted cavalry 'had passed behind' Granbury as the advance began; Quarles formed a second line. Value corrected; two supporting Cleburne citations added ('had passed behind him. when the enemy advanced.'; 'formed as a second line') beyond the reviewer's no-citation-change proposal.
- **ATL-R4** (accepted applied): GA010 wooded-ridges-and-works and GA012 wooded-ravine-and-angle rationales cross-reference the Johnston/Cleburne May 27 entrenchment conflict; no cross-family citation. GA012 adds that the inspected passages do not settle how far Cleburne's 26th-27th works covered the afternoon fight's ground (his entrenching passage precedes the move to the right).
- **ATL-R5** (accepted applied): GA018 casualty-records: unsupported 'does not cover the reinforcing regiments' removed; rationale says the inspected passages do not establish whether Logan's 'my losses' 562 includes the regiments lent by Blair and Dodge. Value's "his corps' loss" also changed to 'my losses'; memo observation reworded.
- **ATL-R6** (accepted applied): GA020 reported-force-scope: 1,800 is all troops engaged (list begins with Laiboldt's Second Missouri, commanding Dalton), not the relief column alone; value/rationale corrected; two p.496 citations added; memo bullet corrected.
- **ATL-R7** (accepted applied): GA019 casualty-records: Schofield's 'During the 4th and 5th no movement of consequence was made' added against Cox's Aug 5 skirmish-line action (Cox dates it via 'Orders for the 5th'); value/rationale corrected; p.517 citation added; already disputed.
- **ATL-R8** (accepted applied): Memo 'Seventeen passages' -> 'Sixteen passages (plus the title page)'. Registry: metadata_only successor cox-atlanta-selections-v2 registered (supersedes v1 with metadata sha256 b52d8fc4...; same path/bytes/ranges; inspection count corrected); all Cox citations in GA007-GA022 moved to v2, so all sixteen dossiers are revised and archived.

## Advisories

- **ATL-A1** (accepted applied): GA009 engineer-reports-and-maps rationale: Cox's maps/hostile-inhabitants passage scoped to the May 18 pursuit (context).
- **ATL-A2** (accepted applied): GA013: beef-on-the-hoof passage scoped to the early-June change of base; Johnston's 41,000/10,000 scoped to the transfer at his relief on the night of July 17, with the relief sentence cited.
- **ATL-A3** (accepted applied): GA022 recorded-result: Hardee's Aug 31 telegram and 1865 report (Cleburne carried the works; part crossed the Flint and took 2 guns) against Cox ('took little part'); three citations; status now disputed.
- **ATL-A4** (not adopted): Logan's July 29 report says the battle lasted until about 3 o'clock and that his lines were assaulted several more times later in the evening, so 'until darkness' is a difference of reference, not a conflict.
- **ATL-A5** (accepted applied): GA017 casualty-records rationale notes Hood's 13 guns taken vs Cox's ten Union guns lost; neither adopted.
- **ATL-A6** (accepted applied): GA010 reported-force-scope: Geary's advance-guard fight separated from the later three-division assault (Williams and Butterfield about five o'clock); Cox's 200 officers added to Quarles's 2,200; two citations.
- **ATL-A7** (accepted applied): GA015 command-roles: Cox's 'French's and Walker's divisions' opposite Logan cited against Johnston's French's and Featherston's; noted as a minor unresolved discrepancy.
- **ATL-A8** (accepted applied): GA008 command-roles: Cox's 'His right division (Judah's) marched against the angle...' sentence cited.
- **ATL-A9** (accepted applied): Memo 'Separate review pending' replaced with 'Separate review' and 'Review correction' sections.
- **ATL-A10** (kept as is): No change to independence groups; memo records that same-author groups across campaigns (Johnston, Cleburne, Hardee; container-level or-beauregard vs author-level here) must be treated as dependent in any cross-campaign family count. A future registry note is for the primary/owner.
- **ATL-A11** (kept as is): Confirmation that GA013 aggregate handling, the rejected live campaign label, the 1882 Cox edition and the 1891 OR imprint are sound; no change.

This AI review is a separate analysis, not historical adjudication or proof of source independence.
The dossiers remain drafts; no model input changes.
