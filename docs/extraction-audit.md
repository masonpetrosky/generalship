# Extraction audit v1 (2026-10-06)

Every dossier had a separate AI review, and those reviews logged hundreds of applied corrections,
but no audit had estimated how many errors remain after review. This audit draws a seeded random
sample of cited dossier claims and checks each one against its passages. The record is
[`data/audit/extraction-audit-v1.json`](../data/audit/extraction-audit-v1.json). Its scored summary
is [`artifacts/extraction-audit-v1.md`](../artifacts/extraction-audit-v1.md), which `make check`
validates and `make reproduce` regenerates.

## Sample

- **Population.** Every supported or disputed claim with at least one citation, across all 384
  dossiers: 3,116 claims. The 461 explicit unknowns are excluded, because checking that a source
  is silent is a different task.
- **Draw.** A simple random sample of 150 claims, without replacement, using
  `random.Random(20261006)` over the claims in file and claim order (`generalship/audit.py`,
  `draw_sample`). Anyone can redraw it.
- **Binding.** Each judgment records the SHA-256 of the dossier version it audited.

## Checks and verdicts

Each cited quote was read in its surrounding text. Where an element of the claim lay outside that
window, the full cited section was searched. Four checks were applied:

- **quote_supports_claim:** every element of the value is supported by the claim's own citations
  or by text in the cited sections.
- **attribution:** each statement is credited to the source that makes it, including statements
  that one source relays from another.
- **scope_and_time:** populations, units, dates and intervals match the source.
- **status:** `supported` or `disputed` fits what the sources show.

Each claim then gets one verdict:

- **correct:** all four checks hold.
- **minor:** a wording, relayed-attribution or missing-citation problem that leaves the meaning
  unchanged.
- **material:** an element is unsupported or contradicted, misattributed, or wrong in scope,
  number or date.

## Result

| Verdict | Claims |
| --- | ---: |
| Correct | 142 |
| Minor | 8 |
| Material | 0 |

- **Material error rate:** 0 of 150 (Wilson 95% interval 0% to 2.5%).
- **Any issue, material or minor:** 8 of 150, or 5.3% (95% interval 2.7% to 10.2%).
- **Where the minor issues were:** 5 of the 8 are `command-roles` claims, which:
  - say the live NPS page agrees without citing it (2);
  - assert a cross-reference cited only in a sibling claim (1);
  - credit a relayed statement to the author who relays it (1);
  - give a unit's name from other reports rather than the cited one (1).

  The other three are:
  - "burned" where the source says "destroyed";
  - a relayed statement credited to the author who relays it;
  - a cross-reference cited only in a sibling claim.

All eight are corrected in dossier revisions named `extraction-audit-correction-2026-10-06`. Each
audited version is archived in `data/evidence/history/` and linked by `supersedes`, so frozen
ledgers still replay. The audit record keeps the audited hashes.

## Independence and limits

This is a **primary self-audit**. The auditor is the same model that drafted and verified the
dossiers and that ran most of their separate reviews, so it cannot see errors that this model
makes systematically. The owner set a self-verification policy on 2026-10-06. Roadmap Milestone 2
still calls for an *independent* extraction sample, by a human or by a model from a different
family; the frozen sample and protocol here can be reused for that.

The audit tests extraction against the cited passages. It does not test:

- historical truth;
- the completeness of the sources inspected;
- explicit unknowns.

A claim can match its sources and still be historically wrong.

## Review records

The same module normalizes every historical separate-review record into one vocabulary:
`applied`, `partly_applied`, `primary_found_applied`, `not_applied`, `deferred` and
`decided_by_primary`. The 17 disposition strings and two record shapes become one index,
[`artifacts/review-index.json`](../artifacts/review-index.json). A record with a disposition
outside the vocabulary fails `make check`.
