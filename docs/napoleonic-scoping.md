# Next war: French Revolutionary and Napoleonic Wars (scoping, not started)

Owner decision, 2026-09-25: after the Civil War run 3, the owner asked which war to do next and
accepted the Napoleonic Wars as the next priority ("go ahead and get prepared for that and mark it
as our next but don't actually run any expensive steps"). Work resumes the following week. This
note prepares the first decisions; it records no evidence, pins no sources, drafts no dossiers
and runs no agents. The 2026-10-06 additions use only pinned Civil War tables, one unpinned upstream
read (named where it is used) and catalogue identifiers. Nothing here changes the Civil War cohorts,
ledgers or runs.

## Why this war

- **Commanders meet repeatedly.** The same commanders appear across many battles and against each
  other, which should connect the rating comparisons. In Civil War run 3, 19 of 94 ranked
  commanders were `not_connected` to others of their side.
- **Strengths are often reported for both sides**, so fewer sides should need grade E modelled
  strengths. That tests the method on a well-counted war before sparser eras such as the ancient
  battles the owner has in view.
- **A candidate pre-modelling battle list exists.** Gaston Bodart, *Militär-historisches
  Kriegs-Lexikon (1618–1905)* (Vienna, 1908), tabulates engagements with strengths and losses and
  should be public domain. It would be a candidate frame, not an authority, like the CWSAC list for
  the Civil War. What is known so far (2026-10-06):
  - **Copies.** Internet Archive holds two digitized copies (`bub_gb_Eo4DAAAAYAAJ`,
    `bub_gb_A0kNAAAAYAAJ`). Neither has been opened, pinned or inspected; coverage, outcome coding and
    legibility are unchecked.
  - **A Civil War check of its figures.** Arnold's machine-readable Bodart table, pinned for
    [ledger v3](ledgers-v3.md), can be compared with the Civil War ledger
    ([agreement artifact](../artifacts/strength-compilation-agreement.json)). On the 66 sides where
    Bodart's total can be compared with a v2 point graded A–C:
    - 44 are within 25%;
    - 7 differ by more than a factor of two;
    - the median ratio is 1.09.

    Bodart's `strength` column often counts a whole army or theater force rather than the troops
    engaged, so a Bodart frame needs an explicit population rule before its figures are used.
  - **Another tabulation.** Arnold's package at the same commit also links 49 battles of the CAA
    Database of Battles (CDB90, a licensed dataset) one-to-one to CWSAC records, 43 of them in the
    Civil War ledgers' scope. This comes from an unpinned read of `cdb90_to_cwsac.json` (SHA-256
    `68aba256…`). CDB90 itself was not consulted.

## Owner decisions needed before research (the first, cheap step)

1. **Frame source.** Which list defines the cohort: Bodart, another tabulation, or a merged list
   with explicit rules. It must be frozen before modelling and pinned with hashes, like the four
   CWSAC tables.
2. **Period and size.** 1792–1815, 1805–1815, or a size cutoff (for example total engaged at or
   above a fixed number). The full period likely runs to hundreds of engagements; a smaller frozen
   first cohort keeps the research affordable.
3. **What a side is.** Coalitions mix Austrian, Prussian, Russian, British and other contingents,
   and allies fight with France. Options: the coalition as the side, the nation of the responsible
   commander, or the belligerent nation holding most of the force. This sets what "side-relative"
   means in the ratings.
4. **Outcome coding.** Decisive, inconclusive and aggregate rules, and whose report settles a
   disputed result, under the evidence contract.
5. **Sources and language.** Which source families are in scope (French, Austrian, Prussian and
   Russian official histories and reports, British dispatches, standard modern tabulations) and how
   non-English passages are cited (original text with locator; any translation marked as such).
6. **Usage budget.** Research dominates Claude usage. Decide the first-pass ceiling per engagement.
   Since 2026-10-06 there are no separate reviews unless the owner asks for one
   ([AGENTS.md](../AGENTS.md#review-policy)).
7. **Research dimensions** (added 2026-10-06). Decide which dossier dimensions are researched to the
   first-pass standard.

   Only two dimensions feed a model today: strength (the strength ledgers) and responsibility (the
   command ledgers). Outcome comes from the frozen frame.

   | Dimension | Share of Civil War claims | Share of citations | Feeds a model |
   | --- | ---: | ---: | --- |
   | Strength | 23% | 19% | yes |
   | Responsibility | 11% | 17% | yes |
   | Outcome | 22% | 28% | no (the frozen frame) |
   | Terrain, logistics, information, objectives | 44% | 36% | no |

   Shares are of 3,577 claims and 16,090 citations.

   **Recommendation:**
   - Research strength and responsibility fully.
   - Research outcome only where the frame's result is disputed (decision 4).
   - Record the four context dimensions only from passages already read for the first two, until a
     reviewed feature-admission design names one as a model input. Posture and fortification, coded
     from those same passages, are the first candidate predictors.

   That would cut roughly a third to two fifths of the research per battle, without reducing what
   the models use.

## What carries over and what must be versioned

- **Carries over:** the evidence contract, dossier format, bounded first-pass protocol, source
  registry and hashing, strength ledger grades A–E, command-responsibility rules, the rating design
  (partial pooling, leave-one-campaign-out verdict, both weightings) and the grade E method.
- **Already war-agnostic (2026-10-06).** Rating run 4's code reads a war profile
  (`generalship/frame.py`) instead of Civil War constants: sides, outcome mapping, tables, ledgers,
  grade E levels and the temporal split. A commander's sign comes from the side commanded in each
  row, so one commander may fight on either side, as coalition wars need
  ([design §10](commander-ratings-v4.md#10-a-profile-for-each-war)). A new war adds a profile.
- **Civil War-specific, needs a versioned design for the new war:**
  - `dataset.py`, `baseline.py`: import and audit of the CWSAC tables.
  - The strength-estimate engine and its checkers (`estimates*.py`): the two-sided `SIDES` and the
    source groups.
  - `command.py`: rank orders (`RANK_ORDER_V2`) and the two-sided rule; naval handling.
  - Campaign units: the Civil War uses CWSAC campaigns; the new war needs a frozen campaign table.
  - Ratings are pooled within a war; comparing commanders across wars is a later, separate design.

## Suggested order when work resumes

1. Present decisions 1–7 to the owner with options and a recommendation.
2. Locate and pin the frame source; transcribe the frozen list offline with hashes.
3. Write and verify the cohort and campaign-table design, and a profile for the war.
4. Only then begin first passes, by complete campaign.
