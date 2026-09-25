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
  decisive, non-aggregate rule is unchanged; 317 engagements meet it.
- **Two-sided rule.** Both ledgers describe a US side and a Confederate side. Twelve decisive
  records list a third belligerent, "Native American", in the frozen commander or forces rows:
  CO001, ID001, MN001, MN002 and ND001–ND005 (US against Native forces) and OK001–OK003
  (Confederate against Opothleyahola's force). They are out of scope, with that reason, because
  the two-sided model does not apply to them. Their dossiers are unchanged and remain in the
  research frame. So 305 engagements are in scope (91 from v1, 214 new) and 79 are listed as out
  of scope with their reason.
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
- **Command responsibility.** Design §2 rules 1–7, the grade table, labels and echelons apply
  unchanged; `generalship/command.py` replays the v2 ledger. Every contained-interval pair among
  the in-scope engagements gets one nesting outcome.
- **Rank order.** Cohort v2's listings use ranks the v1 order does not declare. The v2 order
  (`RANK_ORDER_V2`) inserts army Major, Captain and First Lieutenant below Lieutenant Colonel and
  above Lieutenant, and navy Admiral above Rear Admiral and Lieutenant Commander, Lieutenant and
  Master below Commander. "Brevet" and "Acting" rank as the named rank, as before. The v1 order and
  ledger are unchanged.
- **Registry.** Identical CWSAC name strings on one side are one person. Other merges need the
  listing's own fields (same side and surname; given names differ only by abbreviation or
  spelling) or a passage giving matching initials or the full name, and each is recorded with its
  basis (`merge_basis`, `passage_merges`).
- **Identification in passages.** A name in a record's passages is identified with a listed
  officer of the same side when the passages give matching initials or the full name, or when the
  surname matches exactly one listed officer of that side and no passage gives conflicting
  initials. Otherwise the officer gets a passage-only entry. Two review corrections keep stricter
  passage-only entries (MO009's "Major-General Polk" and VA076's "Major-General Breckinridge").
  Superiors and candidates identified this way are descriptive labels; they do not change a
  side's grade.

## Review

The 214 new entries of each ledger are reviewed in campaign batches by a separate Claude Opus 5.5
`high` reviewer, and every required finding is checked against its passage before it is applied.
A reviewed v2 ledger is a reviewed estimate, not historical adjudication.

## After review

A v2 estimate-layer evaluation or rating run needs a new owner authorization that names the
hashes of the reviewed v2 ledgers and registry.
