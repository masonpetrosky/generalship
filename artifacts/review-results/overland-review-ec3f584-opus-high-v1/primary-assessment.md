# Primary assessment: Overland Campaign first pass review

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `ec3f5843b73987db72ef9d23815ec3622063108f`. Its
SHA-256 is `4c15fb8cea4765467150e4a07dc5d046522116e2327b2ce807ee3f175f1e9add`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `1e791f7b8e9da05b030e355815ac0b68c43adf92`; see [dispatch.json](dispatch.json).

Each required finding was checked against the retained source text before it was applied, and every
added quote occurs exactly once in its section; `python3 -m generalship check` passes. Superseded
dossiers are archived under `data/evidence/history/`. [correction.json](correction.json) binds the
corrected dossiers.

## Required findings

- **OVR-R1** (accepted applied): VA046 contact-reports: 7.15 is when Meade received Warren's despatch; value corrected, p.23 citation added.
- **OVR-R2** (accepted applied): VA046 command-roles: 'on learning of Ewell's approach' replaced with Warren's report and 'what part of Lee's army was there'; citation added.
- **OVR-R3** (accepted applied): VA048 command-roles and memo: p.58 footnote read in context (night march of May 7-8, Provost-Marshal's mounted troops, Lacy house 'most important part of his duty'); value/rationale/memo bullet corrected; four citations added (reviewer's three plus the 'half-past eight in the evening' start for the date).
- **OVR-R4** (accepted applied): VA048 casualty-records: unsupported cavalry exclusion removed; May 8-19 scope and no-adding with VA052 stated; p.116 citation added.
- **OVR-R5** (accepted applied): VA052 forage-and-rations: half ration for one day identified as forage per the 1866 report; citation added.
- **OVR-R6** (accepted applied): VA052 recorded-result: outside-knowledge Meadow Bridge placement of Gordon's wound removed from rationale.
- **OVR-R7** (accepted applied): VA056 reported-force-scope: 'three guns' reattributed to Wild; Butler's cavalry/infantry/artillery composition added and cited; Wild quote extended; composition unresolved noted.
- **OVR-R8** (accepted applied): VA056 summons-and-reports: Butler (before attack) vs Wild (after 1.5 hours) timing conflict; status disputed; citations added (plus Wild's 'I declined').
- **OVR-R9** (accepted applied): VA056 recorded-result: Butler's repulse statement now cited ('repulsed', 'having completely failed').
- **OVR-R10** (accepted applied): VA056 casualty-records: 'about 20 dead' corrected to Butler's 'lost 20' (garbled noun); citation added.
- **OVR-R11** (accepted applied): VA099 hunter-and-rear-reports: June 16 dispatch (Staunton, no definite information) and 1866 report (prisoners of the 11th, Lexington) separated; status disputed; two citations added.
- **OVR-R12** (accepted applied): Memo validation section replaced: ec3f584 edits tests/test_evidence.py to admit the v2 frame; 134 tests OK; checks still pass after correction.

## Advisories

- **OVR-A1** (accepted applied): VA048 terrain: 'eastern half or more of the salient was covered by wood' (p.75) cited; wording corrected.
- **OVR-A2** (accepted applied): VA048 casualty-records: Humphreys says Badeau's wounded are too few; citation added.
- **OVR-A3** (accepted applied): VA055 force: Badeau's 9,162 dated to the Nov 27, 1863 return Humphreys could not find; two citations added.
- **OVR-A4** (accepted applied): VA062: Hoke's <6,000 attributed to Taylor; 'nominal' removed; McParlin's 14,129 = 11,729 + estimated 2,400 from the Pamunkey crossing, covering VA057-VA059 intervals; two citations added.
- **OVR-A5** (accepted applied): VA052/VA099: Sheridan's 'led to believe' scoped to his whole report period; Hampton's report scope June 8-24 cited.
- **OVR-A6** (accepted applied): VA052 fight-the-cavalry: 'on the 8th' dropped (not in selection).
- **OVR-A7** (accepted applied): VA052 casualty-records: Sheridan's 46 killed (garbled line) added and cited.
- **OVR-A8** (accepted applied): VA058 recorded-result: garbled 'driven back, leaving his dead' added and cited, marked as garbled.
- **OVR-A9** (accepted applied): VA059 recorded-result: 'toward' corrected to 'down to' Cold Harbor.
- **OVR-A10** (accepted applied): VA046: May 5 intrenching attributed to Griffin's statement (cited); trains sentence given as Humphreys' judgment (cited).
- **OVR-A11** (accepted applied): VA062 rationale and memo: Cold Harbor times as possibly different events; VA099 'exhaust' replaced with 'reduced to a very small compass'.
- **OVR-A12** (accepted applied): Partly applied: VA056 1,800 agreement labelled non-corroborating and unsupported 'works predate the attack' removed. The Humphreys north-anna/cavalry range overlap (1,179 chars) is recorded in the memo only; no metadata-only successor for humphreys-overland-selections-v1 was created (bytes, ranges and citations are correct; only the inspection note is silent) - primary may decide otherwise.

This AI review is a separate analysis, not historical adjudication or proof of source independence.
The dossiers remain drafts; no model input changes.
