# Strength ledger v3: filling grade D sides from upstream tables

Status: primary-verified, 2026-10-06. This is a versioned successor of the v2 strength ledger
([v2 addendum](ledgers-v2.md)) under the [best-estimate design](strength-estimates.md); the design's
rules, constants and engine are unchanged. The v1 and v2 ledgers, their evaluations and rating runs
1–3 are unchanged.

## 1. Why and what

Run 3 had to model 262 of the 610 in-scope sides (grade E) for want of a usable reported figure.
The upstream package we already pin, Jeffrey B. Arnold's *American Civil War Battle Data* at commit
`3a6020d`, has more force tables than the four CWSAC tables the project uses. v3 adds their figures,
**only to sides the v2 ledger grades D**. Every other side keeps its v2 inputs.

The owner authorized this source scope on 2026-10-06
([record](../data/estimates/owner-decision-v3-sources-2026-10-06.json)). Under the owner's
self-verification policy of the same day, the primary designed, built and verified it with no
separate review.

## 2. Sources

Each table is pinned in `data/raw/arnold-tables-v1/`, with its SHA-256 and registry entry in
`data/sources.json` (CC-BY-4.0 per the pinned package metadata):

| Table | Registry ID | Independence group | Population, per Arnold's schema |
| --- | --- | --- | --- |
| CWSAC Report Updates (NPS, 2009–2013) | `arnold-cws2-forces` | `nps-cwsac` | an explicit count of the force, else missing |
| Civil War Soldiers and Sailors System | `arnold-cwss-forces` | `nps-cwsac` | troops engaged |
| Bodart (1908) | `arnold-bodart1908-forces` | `bodart-kriegs-lexikon-1908` | `strength_engaged`: personnel engaged; `strength`: total personnel, which Arnold notes is often the whole unit in the theater |
| Clodfelter (2008) | `arnold-clodfelter-forces` | `clodfelter-warfare-armed-conflicts-2008` | total personnel in the battle, basis not stated |

Bodart and Clodfelter rows reach a CWSAC record only through Arnold's concordances
(`arnold-bodart1908-to-cwsac`, `arnold-clodfelter-to-cwsac`). Arnold's Livermore table is pinned only
to cross-check the project's own transcription (§6). Livermore figures are still cited from that
transcription, as design §4 rule 2 requires.

## 3. Coding rules (mechanical, in `generalship/estimates_v3.py`)

1. **Which cells.** For each grade D side, take:
   - its CWS2 `strength` cell and its CWSS `TroopsEngaged` cell;
   - the Bodart `strength_engaged` and `strength` cells and the Clodfelter `strength` cell of the
     row reached by a concordance link.

   A link counts only if it has relation `eq`, a single CWSAC target, and no other `eq` link reaching
   the same record. A link covering several records (Bodart's Seven Days entry), a link of another
   relation (`neq`, `<`, `gt`), an empty cell and a zero cell are recorded in the side's inventory
   with that reason and give no input. A zero is not a count.
2. **Classification.** Each cell is coded from its table's schema, and every cell also carries
   `derivation_unknown`. The engine then classes it under design §3.

   | Table and column | Basis | Other codes | Class |
   | --- | --- | --- | --- |
   | CWS2, CWSS | `reported_engaged` | none | A |
   | Bodart `strength_engaged` | `reported_engaged` | none | A |
   | Bodart `strength` | `unknown` | `scope_unresolved` | C, `applicability_unresolved` |
   | Clodfelter `strength` | `unknown` | none | B, `basis_unknown` |
3. **Copies are one figure.** An upstream figure equal to an NPS/CWSAC or Livermore figure already on
   the same side is recorded as its reproduction (`reproduction_of`). The engine then counts them as
   one dependence group, which keeps any scope finding attached to the original.
   - This extends design §4 rule 2's compiled-dependence link to the new tables.
   - Example: Cedar Mountain's Union 8,030 appears in CWSAC, NPS, Livermore, CWS2, CWSS and
     Clodfelter. Livermore shows it excludes a division engaged after dark, so it stays a lower
     bound in every copy.
4. **Two documented exceptions** (`OVERRIDES`). These CWS2 cells describe only part of their side,
   so they are coded `partial_scope` lower bounds:
   - **Hatteras Inlet, Union, 935:** the description sums the landing units and names the Atlantic
     Blockading Squadron without a count.
   - **Saltville I, Confederate, 300:** the description names only the "Confederate Home Guard".
5. **Estimates.** The unchanged engine applies design §4 to the v2 inputs plus the new ones.
   - Bounds, opponent estimates and post-start rules all apply as before.
   - A side whose basis becomes `unknown` gives both sides of the row the `basis_mixed` label. This
     is the only change v3 makes to sides graded A–C in v2.

## 4. Result

| | Sides |
| --- | ---: |
| Grade D in v2 | 262 |
| Filled in v3 | 99 (A 54, B 41, C 4) |
| Still grade D | 163 |

- **Grade A (54):** all from CWS2 counts, chiefly the 1864–65 Virginia campaigns that the 1993 CWSAC
  table left blank.
- **Grade B (41):** Clodfelter totals with no stated basis.
- **Grade C (4):** Bodart totals of unresolved scope:
  - Dallas, both sides;
  - Cedar Mountain, Union;
  - Harpers Ferry, Confederate.

The [check](../artifacts/strength-ledger-v3-check.json) gives the full grade and row-set counts.

Known weak points, each flagged by its labels rather than hidden:

- **Bodart totals overstate.** Cedar Mountain's Union point becomes Bodart's 18,000, which conflicts
  with Ropes's statement that Banks's corps did not reach 8,000 (`bound_conflict`). Bodart's totals
  also widen ranges where they enter the hull: Appomattox Court House, Union, runs from 19,950 to
  105,000. Every such side carries `applicability_unresolved`.
- **Clodfelter may count whole armies.** For example, Jonesborough, Union, is 60,000, and Raymond
  and Jackson are 25,000 each. These carry `basis_mixed` and grade B.
- **Agreement is not corroboration.** These compilations share sources: CWS2 is NPS's own update of
  the CWSAC report, and Clodfelter likely draws on Livermore and NPS.

## 5. Verification

`python3 -m generalship estimate-check --ledger data/estimates/side-strength-v3.json` replays the
ledger, as do `make check` and `tests/test_ledgers_v3.py`. The checker verifies that:

- every v2 input is carried forward unchanged;
- no input is added to a side graded A–C;
- every new input re-derives from the pinned tables by the §3 rules, with its cell quote, value,
  class, document key, dependence group and concordance link checked;
- each side's upstream inventory lists every row examined, with its use or reason;
- every estimate, grade-D reason and row-set membership reproduces under the engine;
- the ledger binds exactly the dossier versions v2 binds, replayed through the
  [replay design](ledger-replay.md)'s bound views.

## 6. Cross-checks (descriptive; [artifact](../artifacts/strength-compilation-agreement.json))

**Against sides v2 already grades A–C:**

| Table | Sides compared | Median ratio to the v2 point | Within 25% | Off by more than 2× |
| --- | ---: | ---: | ---: | ---: |
| CWSS | 152 | 1.00 | 144 | 3 |
| CWS2 | 105 | 1.00 | 82 | 9 |
| Clodfelter | 150 | 1.00 | 112 | 8 |
| Bodart totals | 66 | 1.09 | 44 | 7 |

**Livermore transcription.** On 83 sides, Arnold's machine-readable Livermore figure matches the
project's own transcription on 81. The two differences are not transcription errors:

- **South Mountain, Confederate:** Arnold has Livermore's p.91 alternative "Total engaged 17,852".
  The v2 ledger deliberately set it aside, because it covers only the Turner's and Fox's Gap
  divisions.
- **Chattanooga, Confederate:** Arnold has Livermore's engaged total of 46,165, printed on p.108, a
  page the project did not retain. The v2 ledger uses the p.107 present-for-duty figure, 44,010.
  That side is graded C and outside v3's scope, so a later revision could transcribe p.108.

## 7. Limits

- v3 is a reviewed estimate only in the sense of being primary-verified. It is not historical
  adjudication or an admitted feature.
- Which sides gained a figure depends on which battles the compilers covered. Major battles and
  the 1864–65 Virginia operations dominate, so the selection pattern of design §8 remains.
