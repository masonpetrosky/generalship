# Roadmap and current handoff

## Milestone 0 — Working research foundation (complete)

- Public repository, Python package/CLI, local test and reproduction commands.
- Frozen 127-engagement Civil War cohort with complete source campaign groups.
- Pinned inputs, attribution, integrity checks, and exclusion accounting.
- Force-size logistic baseline with campaign-held-out evaluation and comparators.
- Three draft evidence dossiers and a prepared Shiloh research assignment.
- Deterministic coverage, predictions, research queue, report, and hash receipt.

“Complete” applies to this infrastructure milestone only. Historical validation,
AI extraction quality, command attribution, and improved generalship estimation
have not been established.

## Milestone 1 — First independently reviewed campaign dossiers (in progress)

The first [Shiloh source-enrichment pass](research/shiloh.md) is complete **as a
draft**, with 22 claims, 12 typed troop observations and seven chronology events.
Ten new source artifacts include original reports, orders, return transcriptions,
two independently authored histories, and two facsimiles. Version 1 is archived.
Neither canonical opening strengths nor effective command-transfer times have
been adjudicated, and no independent review has occurred.

Start now with Confederate reports Nos.136 and 137 in Official Records I.X.1,
which the p.396 return explicitly says disagree with its totals. Audit the Union
return's missing units and phase-specific arrivals next. The updated packet is
available with `python3 -m generalship packet TN003`. After review, complete all
pilot engagements in the same source campaign, including Fort Henry, Fort
Donelson, and Corinth.
Use Antietam to test outcome ambiguity and Champion Hill to test inherited orders
versus commander-created circumstances.

Deliverables:

- Campaign records and resolved commander/army identities (Shiloh now has local
  entity IDs and phase records; cross-engagement identity resolution remains).
- Source-dependent alternative estimates and a typed quantity schema (v2 now
  implemented for Shiloh; historical reconciliation and review remain).
- Explicit replacement boundaries and contemporary information sets.
- Named independent review records and an extraction-error audit.
- A feature-admission mapping tied to immutable sources and dossier versions.

Acceptance: every admitted fact has traceable evidence, source alternatives remain
visible, reviewers agree on population/timing or retain a dispute, and no post-outcome
quantity can enter a predecision feature without an explicit justified design.

## Milestone 2 — Baseline audit and expanded coverage

Document an exact reproduction route for the original Arsht analysis and access/
redistribution terms. Keep that track separate from the current reduced baseline.
Enrich the full frozen pilot by complete campaigns; add credible troop estimates
without selecting only famous or easily scored battles. Audit coverage by outcome,
commander, campaign, engagement scale, and evidence quality.

Acceptance: an immutable cohort, exclusion ledger, independent extraction sample,
and paired comparison rows defined before model selection. Sparse evidence must
not quietly turn into mediocre commander scores.

## Milestone 3 — Enriched prediction and command inference

Predefine the campaign estimand and causal graph. Add justified conditions and
opponent/army context, investigate commander-assignment confounding, and fit
hierarchical partial-pooling alternatives only when coverage supports them.
Evaluate by grouped held-out campaigns and a locked final test set; check temporal
generalization separately. Report calibration and clustered uncertainty.

Acceptance: improved out-of-sample prediction on comparable rows, robust source
and coding sensitivities, and a separately defended causal interpretation. A
familiar-looking greatest-generals list is not evidence of correctness.

## Milestone 4 — Inspectable research interface

Create the commander → campaign → engagement → assumption → passage explorer.
Show cumulative results, opportunity-adjusted estimates, coverage, uncertainty,
and source disputes separately. Provide scenario toggles and explain what changes.
No battle/campaign double counting and no unqualified cross-era rankings.

## Deferred implementation choices

No AI vendor/model policy or paid research automation has been selected. Evidence
packets work with the user's chosen researcher and model. LangExtract or another
extraction library can be evaluated later against a measured source-alignment need.
No web framework or hosting stack is selected before the evidence contract matures.
Use local tests; no hosted workflow is configured.
