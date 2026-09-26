# Next war: French Revolutionary and Napoleonic Wars (scoping, not started)

Owner decision, 2026-09-25: after the Civil War run 3, the owner asked which war to do next and
accepted the Napoleonic Wars as the next priority ("go ahead and get prepared for that and mark it
as our next but don't actually run any expensive steps"). Work resumes the following week. This
note prepares the first decisions; it records no evidence, fetches no sources, drafts no dossiers
and runs no agents or reviews. Nothing here changes the Civil War cohorts, ledgers or runs.

## Why this war

- **Commanders meet repeatedly.** The same commanders appear across many battles and against each
  other, which should connect the rating comparisons. In Civil War run 3, 19 of 94 ranked
  commanders were `not_connected` to others of their side.
- **Strengths are often reported for both sides**, so fewer sides should need grade E modelled
  strengths. That tests the method on a well-counted war before sparser eras such as the ancient
  battles the owner has in view.
- **A candidate pre-modelling battle list exists.** Gaston Bodart, *Militär-historisches
  Kriegs-Lexikon (1618–1905)* (Vienna, 1908), tabulates engagements with strengths and losses and
  should be public domain. **Unverified**: no copy has been located or inspected, and its coverage,
  outcome coding and reliability are not yet checked. It would be a candidate frame, not an
  authority, like the CWSAC list for the Civil War.

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
6. **Usage budget.** Research and separate reviews dominate Claude usage. Decide the first-pass
   ceiling per engagement and whether reviews run per campaign or in larger batches.

## What carries over and what must be versioned

- **Carries over:** the evidence contract, dossier format, bounded first-pass protocol, source
  registry and hashing, strength ledger grades A–E, command-responsibility rules, the rating design
  (partial pooling, leave-one-campaign-out verdict, both weightings) and the grade E method.
- **Civil War-specific, needs a versioned design for the new war:**
  - `dataset.py`, `baseline.py`: import and audit of the CWSAC tables.
  - `imputation.py`: `SIDES` (US/CS), `PERIODS` (1861–1865), `THEATERS`, `ECHELONS` and the
    reference level.
  - `command.py`: rank orders (`RANK_ORDER_V2`) and the two-sided rule; naval handling.
  - Campaign units: the Civil War uses CWSAC campaigns; the new war needs a frozen campaign table.
  - Ratings are pooled within a war; comparing commanders across wars is a later, separate design.

## Suggested order when work resumes

1. Present decisions 1–6 to the owner with options and a recommendation.
2. Locate and pin the frame source; transcribe the frozen list offline with hashes.
3. Write the cohort and campaign-table design; one separate review of that design.
4. Only then begin first passes, by complete campaign.
