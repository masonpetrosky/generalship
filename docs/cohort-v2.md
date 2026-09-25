# Cohort v2: the full-war research frame

**Status: adopted 2026-09-25 on the owner's instruction.** After the first commander-rating run
found no detectable signal on the 1862–1863 pilot, the owner was asked whether to research the
remaining engagements and replied "Sounds good, go ahead".

## Frame

`data/pilot/cohort-v2.json` (`acw-full-frame-v2`) lists every source-listed battle in the pinned
Arnold CWSAC battles table: **384 engagements in 119 campaign groups**, in all five theaters, from
1861 to 1865.

- **Selection.** No rule depends on outcome, commander reputation or numerical force
  availability.
- **Relation to v1.** It contains the frozen v1 cohort (`acw-eastern-western-1862-1863-v1`, 127
  engagements, 36 campaigns). No campaign is split between the v1 cohort and the remaining 257
  engagements, which fall in 83 campaigns.

## What does not change

The v1 cohort stays the frame for:

- the frozen baseline (`artifacts/baseline.json`);
- the admission contract and its snapshot;
- the reviewed strength and command ledgers;
- the first rating run.

All v1 records and reviews are unchanged. v2 is a research-coverage frame. Dossier validation now
accepts any v2 engagement. Code that applies to v1 still passes or reads the v1 cohort
explicitly.

Extending the strength and command ledgers, and any rating run, to v2 needs versioned successors
(for example `side-strength-v2`) and a new owner authorization naming their hashes. Nothing here
changes a model input.

## Research order

This is a decision recorded before the research starts. First passes go by complete campaign,
under the bounded protocol in [methodology](methodology.md#research-depth-and-coverage) and
[AGENTS.md](../AGENTS.md).

1. **The 1864–65 campaigns of the main armies come first.** These are the campaigns where
   commanders accumulate battles across campaigns, which the rating needs:
   - Overland;
   - Bermuda Hundred;
   - Richmond-Petersburg;
   - Appomattox;
   - Atlanta;
   - Franklin-Nashville;
   - Savannah;
   - Carolinas;
   - Early's Raid;
   - Sheridan's Valley;
   - Lynchburg;
   - Red River;
   - Camden;
   - Price's Missouri Expedition;
   - Mobile Bay and Mobile;
   - Fort Fisher.
2. **All other campaigns follow in chronological order.**

The order affects only which coverage exists at any interim point. The target is all 257
engagements.
