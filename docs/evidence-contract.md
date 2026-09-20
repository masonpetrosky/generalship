# Evidence contract, versions 1, 2 and 3

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

Metadata corrections add a new source ID while preserving the old entry and raw
file. A `metadata_only` revision records `supersedes.source_id` and the SHA-256
of the previous complete entry serialized as sorted-key, compact, UTF-8 JSON
(`ensure_ascii=False`). Validation checks this binding and unchanged raw path,
hash, format and parent hash. `revision_note` documents the reason. These new
metadata records are not additional historical witnesses or new raw artifacts.

For mixed-document snapshots, `document_dates_by_section` maps every historical
section to its document date or null. The source-wide `document_date` must be null;
`document_date_note` explains the distinctions. `editorial_sections` explicitly
excludes local transcription notes from historical dates. Missing/extra sections,
invalid dates and a non-null source-wide fallback fail validation. The
`source_document_date` helper returns a mapped null unchanged and rejects a missing
section; it never borrows a neighboring report's date. These are document dates,
not event dates, public availability or a commander's knowledge. A transcript's
`facsimile_source_id` must resolve to an image with the same parent hash and
dependence group; this link does not prove independence from other reports.

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
research observations; version 3 adds explicit estimation provenance. None
supplies admitted model features.

## Version 2 phase records

Shiloh introduced v2 phase records and now uses v3. Antietam and Champion Hill
remain valid v1 drafts; archived v2 dossiers retain their original contract.
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

## Version 3 estimation provenance

Every v3 quantity retains its numeric bounds and `estimate_kind` independently of
`estimation_status`. The latter describes the supplied evidence's characterization
of that observation:

| Status | Meaning |
|---|---|
| `explicit_estimate` | A word, probable range or linked table marker explicitly qualifies the observation as estimated/approximated |
| `aggregate_includes_estimates` | The printed total contains identified estimated components |
| `reported_without_explicit_estimation_qualifier` | No explicit qualifier for this observation in the inspected passages; not proof of measurement, exactness or non-estimation elsewhere |
| `unknown` | Estimation provenance is unestablished or has not been classified |

`estimation_note` is a required rationale. `estimation_citations` contains exact
passages with source IDs and locators (including table footnotes on other pages)
and is required to be nonempty for any classified status. Unknowns may have an
empty list; never invent a quote for an unknown. Passage checks establish presence,
not entailment or the absence of qualifiers in unseen material. If a printed total
is itself explicitly estimated, use `explicit_estimate`; otherwise a total with
identified estimated components uses `aggregate_includes_estimates`. Preserve
remaining uncertainty in the rationale. Never infer an uncertainty interval from
an estimation marker, and never infer estimation from roundness alone.

The [review-correction migration](research/shiloh-review-corrections.md) archives
the prior draft as `TN003.v5.json` and adds estimation provenance to all 40
observations. The six TN003-R1 targets retain every printed number, including
7,553/7,552. Version 2 remains valid without these fields; a v3 record cannot
silently downgrade to v2 while retaining them. The dossier stays `draft` and
the baseline still ignores all typed research observations.

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

The owner authorizes a separate GPT-6 Astra `xhigh` reviewer subagent in the
current task. Give it fresh context and an exact frozen evidence assignment;
record its actual response, task identity, model/effort, date, input hashes and
coverage. The primary agent checks proposed corrections against sources before
changing the dossier. A separate user-managed chat is optional. An AI review
must remain labeled AI: it does not establish human historical adjudication,
source independence or automatic feature admission. See [AGENTS.md](../AGENTS.md).

The current pipeline **never promotes dossiers into baseline inputs**, even if a
dossier is marked reviewed. The feature-admission mechanism does not exist yet.
That deliberate boundary prevents draft interpretations from changing results.

Automatic checks establish byte identity, reference integrity, and passage presence.
They cannot establish truth, claim entailment, source independence, command
causality, or the sincerity of a reviewer record. These limits should remain visible.
