# Cohort v2 ledgers: scope addendum

Status: working addendum, 2026-09-25. It extends two accepted designs to the full-war frame
without changing their rules:

- the [best-estimate side-strength design](strength-estimates.md) (v1 ledger
  `data/estimates/side-strength-v1.json`);
- the command-responsibility rules of the [commander residual-rating design](commander-ratings.md)
  §2 (v1 ledger `data/command/responsibility-v1.json`).

The v1 ledgers, the estimate-layer evaluation and the first rating run stay frozen on cohort v1.
Nothing here admits a feature, fits a model, rates anyone or changes the baseline.

## Scope

- **Cohort.** [Cohort v2](cohort-v2.md) (`data/pilot/cohort-v2.json`): 384 engagements. The
  decisive, non-aggregate rule is unchanged, so 317 engagements are in scope and 67 are listed
  as out of scope with their reason. Of the 317, 91 are the v1 engagements and 226 are new.
- **Carry-forward.** The 91 v1 entries of each ledger are copied unchanged, with their dossier
  bindings. They are not re-extracted or re-reviewed. A v1 dossier that has changed since its v1
  binding would be re-extracted; none has.
- **Successors.** `data/estimates/side-strength-v2.json` and `data/command/responsibility-v2.json`,
  with the registry `data/command/commanders-v2.json`, which keeps every v1 commander ID.

## Sources for the strength ledger

The owner set the source scope on 2026-09-25
([record](../data/estimates/owner-decision-v2-sources-2026-09-25.json)):

- the first-pass dossier citations registered at or before the coverage commit `cbc5935`;
- the pinned Livermore records;
- new Livermore page images and a transcription, limited to printed pages that carry an entry
  matching a cohort-v2 decisive, non-aggregate engagement. As in v1, a Livermore figure is cited
  from the transcription, never from the OCR.

No other new source research is authorized for this layer. An unfilled side stays grade D.

## Rules

- **Strength.** Design §§2–6 apply unchanged, with the same constants. The engine is the
  unchanged `generalship/estimates.py`; `generalship/estimates_v2.py` replays a successor
  ledger against the cohort its bindings name. The v1 extractor policies apply.
- **Command responsibility.** Design §2 rules 1–7, the grade table, labels, echelons and the
  declared rank order apply unchanged; `generalship/command.py` replays the v2 ledger. Every
  contained-interval pair in cohort v2 gets one nesting outcome.
- **Registry.** Identical CWSAC name strings on one side are one person. Other merges need the
  listing's own fields (same side and surname; given names differ only by abbreviation or
  spelling) or a passage, and each is recorded with its basis.

## Review

The 226 new entries of each ledger are reviewed in campaign batches by a separate Claude Opus 5.5
`high` reviewer, and every required finding is checked against its passage before it is applied.
A reviewed v2 ledger is a reviewed estimate, not historical adjudication.

## After review

A v2 estimate-layer evaluation or rating run needs a new owner authorization that names the
hashes of the reviewed v2 ledgers and registry.
