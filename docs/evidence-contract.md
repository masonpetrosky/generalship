# Evidence contract, versions 1 and 2

The source registry is `data/sources.json`; dossiers are `data/evidence/<battle-id>.json`.
Run `python3 -m generalship check` to verify every source hash, dossier, and baseline.

## Source records

Each source has an ID, title, origin URL, local path, SHA-256, retrieval date,
format, rights note, source kind, and independence group. CSV sources additionally
declare a primary key. Immutable download URLs pin the exact upstream commit.
The checked-in NPS snippets are normalized plaintext; their manifest describes
the transformation and identifies the originals. Historical sources are not
independent simply because two websites host them.

New evidence should also record author, publication date, edition, page/section,
and archival identifier where available. An inaccessible source is a research
lead, not evidence. Keep private/licensed source material outside the public repo
unless redistribution is permitted; public dossiers can retain metadata and
appropriately short passages with reviewable locators.

## Dossiers and claims

Each dossier identifies a frozen-cohort battle, draft/reviewed status, proposed
tactical and campaign replacement dates (null until established), a boundary note,
claims, and open questions. Dates alone are insufficient when intraday command or
reinforcement timing matters; version 2 adds phase records without inventing exact
timestamps for qualitative time expressions.

Every dossier covers strength, terrain, logistics, information, objectives,
responsibility, and outcome. A dimension without evidence gets an explicit unknown.
Claims include:

| Field | Meaning |
|---|---|
| `id` | Unique within the dossier; stable when amended |
| `dimension` | One of the seven research dimensions |
| `value` | A supported proposition, disputed account, or null |
| `status` | `supported`, `disputed`, or `unknown`; supported means passage-backed, not adjudicated truth |
| `phase` | `inherited`, `commander_created`, `post_outcome`, or `unresolved` |
| `rationale` | Interpretation, scope, and why evidence is or is not usable |
| `citations` | Source ID, exact short quote, and locator |

CSV citations use a complete row key and column. Text citations use a human-readable
locator. Sources with `sectioned: true` also require a `section` matching exactly
one `## section-id` line in the snapshot; the quote must occur inside that section,
not elsewhere in the file. Legacy unsectioned sources still match the whole snapshot.
Quotes must occur exactly in the referenced cell or selected text. Unknown
claims require null and no fabricated citation. Different accounts are separate
claims, never silently averaged. Imported strength bounds remain separate low/high
values and retain their source basis; an estimate of people present must not become
an estimate of people engaged.

For draft dossiers with unset replacement boundaries, phase tags are hypotheses
explained by the rationale. They cannot be treated as reviewed causal classifications.
Version 1 stores rich propositions as text. Version 2 additionally preserves typed
research observations. Neither version supplies admitted model features.

## Version 2 phase records

Shiloh is the first v2 dossier. Antietam and Champion Hill remain valid v1 drafts.
`supersedes` identifies the archived previous dossier and its SHA-256. Archives
live under `data/evidence/history/`, are checked against the current revision's
hash, and are included in the build receipt but not counted as additional battles.
Existing claim IDs persist when their interpretation is amended.

The Confederate-return follow-up keeps schema version 2 and archives the first
enriched draft as `TN003.v2.json`. The Union-availability follow-up archives the
Confederate revision as `TN003.v3.json`; that revision links to it and
preserves the complete archive chain. The Ohio-reinforcement follow-up archives
that Union revision as `TN003.v4.json`; the latest dossier links to it. See the
[Confederate migration](research/shiloh-confederate-returns.md),
[Union migration](research/shiloh-union-availability.md), and
[Ohio migration](research/shiloh-ohio-reinforcements.md).
Report 136/137 branch subtotals and grand totals are overlapping observations,
not additional people to sum. Printed arithmetic discrepancies remain visible;
`reported_exact` records the number as printed, not its internal consistency.
The same precision rule applies to Reed's explicitly estimated entries: their
notes retain that estimation status. Mixed-date reconstructed totals, return
components, detached guards and later joining contingents are overlapping
source observations, never automatic opening-strength features.
An original report and a separately printed diary may have different or unknown
composition dates even under one source ID. A source's reported local clocks are
not automatically synchronized; events retain attribution rather than inventing
a common arrival/readiness time. Secondhand recalled strength without a settled
population basis may remain a prose claim instead of a typed quantity.

- `entities`: local IDs, names, person/formation kind, and US/CS side. They prevent
  confusing Lew Wallace's division with another formation; they are not yet a
  project-wide identity registry or proof of a command relationship.
- `events`: date, source-qualified `time_label`, entity IDs, evidenced claim IDs,
  and an interpretive note. A reported death time is not an effective command
  assumption time. Approximate clocks have no invented time-zone conversion.
- `quantities`: stable ID, supporting strength claim and `citation_index`, formation
  ID, lower/upper values, unit, population basis, estimate kind, period, location,
  scope, `recorded_at`, and note. Observations from different sources remain separate.

Units currently support people only. Bases distinguish `present_for_duty`,
`reported_effective`, `reported_engaged`, `reported_reinforcements` and
`reported_present`. They preserve a source's meaning rather than assert equivalence.
Estimate kinds are `reported_exact` (precision as written, not proven accuracy),
`approximate` (a rounded point) and `range` (source-estimated bounds, not confidence
limits). Nonfinite/negative/reversed values and incompatible point bounds fail.

The period has start/end dates and a required scope label. Both dates are null
when unstated, such as a return headed “after battle” without its muster date.
`recorded_at` is separately null or the known report/return/forwarding date; it
does not establish the date when a commander learned the information. Public
availability, historical event time and command knowledge must not be conflated.
Null dates are not zero-duration events or permission to infer missing dates.

Validation checks identity/reference integrity, known supporting claims, section
presence, required scope, date order and quantity bounds. It does **not** verify
that the numbers or interpretations entail the cited passage. A typed observation
still needs historical and feature-admission review. Adding a column or marking a
dossier reviewed never changes the baseline automatically.

## Research and review

1. Prepare an assignment with `python3 -m generalship packet TN003`.
2. Read the source passages; locate independent histories and original records.
3. Add new source snapshots and metadata without overwriting earlier versions.
4. Propose claims and preserve unknowns and conflicting estimates in a draft.
5. Run automated checks, then review entailment, source quality, chronology,
   command authority, and population definitions. Record reviewer, date, decision,
   and disagreements. A status label alone is not proof that review happened.
6. Build a separately reviewed feature-admission mapping tied to source/dossier
   hashes and a particular estimand before using any new evidence in a model.

The current pipeline **never promotes dossiers into baseline inputs**, even if a
dossier is marked reviewed. The feature-admission mechanism does not exist yet.
That deliberate boundary prevents draft interpretations from changing results.

Automatic checks establish byte identity, reference integrity, and passage presence.
They cannot establish truth, claim entailment, source independence, command
causality, or the sincerity of a reviewer record. These limits should remain visible.
