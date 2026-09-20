# Evidence contract, version 1

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
reinforcement timing matters; phase-level chronology is a next-schema task.

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
locator. Quotes must occur exactly in the referenced cell or snapshot. Unknown
claims require null and no fabricated citation. Different accounts are separate
claims, never silently averaged. Imported strength bounds remain separate low/high
values and retain their source basis; an estimate of people present must not become
an estimate of people engaged.

For draft dossiers with unset replacement boundaries, phase tags are hypotheses
explained by the rationale. They cannot be treated as reviewed causal classifications.
Version 1 stores rich propositions as text, not numeric feature rows; phase-specific
quantities, commander identities, temporal availability, and source alternatives
need a subsequent typed schema before enriched modeling.

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
