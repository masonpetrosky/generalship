# Roadmap

This file holds the current priority, the decisions waiting on the owner and the status of each
milestone. Completed work is recorded in the [research log](research-log.md), which also keeps
everything this roadmap recorded up to 2026-10-06. Registered sources are listed in
[source additions](source-additions.md).

## Current priority: the French Revolutionary and Napoleonic Wars (frame built)

The owner chose the Napoleonic Wars on 2026-09-25 and decided the seven scoping questions on
2026-10-06 ([scoping note](napoleonic-scoping.md),
[record](../data/napoleonic/owner-decision-scoping-2026-10-06.json)):

- **Frame:** Bodart's 1908 *Kriegs-Lexikon*, every entry for 1792–1815 in the wars France fought,
  frozen as printed.
- **First cohort:** the 1805–1815 campaigns.
- **Sides:** France and its allies against their opponents.
- **Outcome:** Bodart's recorded winner.
- **Sources:** each side's own public-domain sources.
- **Research:** strength and responsibility researched in full.

**Done (2026-10-06):** the frame is built and frozen ([design](napoleonic-frame.md)).

- Bodart's scan is pinned, and pp. 268–490 are transcribed twice from the page images, reconciled
  and audited.
- The frame holds **663 engagements** of 1792–1815 in France's wars, out of 708 entries.
- **Cohort v1** holds the **325 land engagements of 1805–1815** in 16 campaign groups.

**Next:**

1. A Napoleonic evidence path: a cohort-aware dossier validator, its own directory, and a research
   brief applying decisions 5–7.
2. First passes by complete campaign group, starting with `third-coalition 1805` (22 entries),
   logging usage per campaign and giving the owner a projection after the first.

No dossiers have been drafted. The Civil War work below is complete as recorded, and its cohorts,
ledgers and runs are unchanged.

## Open owner decisions

- **Weekly usage cap for the Napoleonic first passes:** optional (scoping decision 6). Without one,
  passes continue campaign after campaign, with a projection after the first.
- **Graded outcomes:** see [owner ideas](#owner-ideas-to-design-later). Bodart's loss figures
  could supply the margins later.

## The American Civil War: where things stand

- **Frame.** [Cohort v2](cohort-v2.md): every engagement in the pinned CWSAC list, 384 in 119
  campaign groups. The 127-engagement 1862–1863 pilot (cohort v1) is kept as it was frozen.
- **Evidence.** All 384 engagements have a draft dossier. The dossiers hold 3,577 claims, 461
  explicit unknowns and 16,090 citations. Every dossier had a separate AI review before
  2026-10-06; see [review policy](#review-policy). An [extraction audit](extraction-audit.md) of
  150 random claims found no material error (Wilson 95% interval 0–2.5%) and 8 minor ones, all fixed.
- **Explorer.** A static site, built by `python3 -m generalship site` and published on
  [GitHub Pages](https://masonpetrosky.github.io/generalship/), traces each commander to their
  engagements, claims, quoted passages and pinned sources.
- **Ledgers.** The v1 ledgers cover the 91 decisive, non-aggregate pilot engagements and the v2
  ledgers the 305 in scope ([addendum](ledgers-v2.md)). Each names one responsible commander per
  side and gives a graded strength estimate. [Strength ledger v3](ledgers-v3.md) fills 99 of the
  262 sides that had no usable figure from upstream tables; the other 163 are modelled (grade E,
  [design](strength-imputation.md)).
- **Runs.** Rating runs 1–4 and two estimate evaluations; see the README's results table. Run 4
  ([memo](research/commander-ratings-v4.md)) was pre-registered with a context comparator,
  estimated τ, leakage handling and a bootstrap rule, and found no improvement under that rule.
  The runs are exploratory diagnostics outside the [admission contract](feature-admission.md), and
  the frozen baseline is unchanged.

## Milestones

| Milestone | Status |
| --- | --- |
| 0. Working research foundation | Complete (infrastructure only) |
| 1. First reviewed campaign dossiers | Coverage complete. Cross-engagement identities, replacement boundaries and information sets remain |
| 2. Baseline audit and expanded coverage | Full-war coverage done. Arsht reproduction route, independent extraction sample and paired comparison rows remain |
| 3. Enriched prediction and command inference | Exploratory rating runs only. Campaign estimand, causal graph and locked test set remain |
| 4. Inspectable research interface | Started: a static explorer. Opportunity-adjusted estimates, disputes views and scenario toggles remain |

### Milestone 0: working research foundation (complete)

- A public repository, a Python package and CLI, and local test and reproduction commands.
- A frozen 127-engagement Civil War cohort of complete source campaign groups.
- Pinned inputs, attribution, integrity checks and exclusion accounting.
- A force-size logistic baseline with campaign-held-out evaluation and comparators.
- Deterministic coverage, predictions, research queue, report and hash receipt.

"Complete" applies to this infrastructure milestone only. Historical validation, AI extraction
quality, command attribution and better estimates of generalship have not been established.

### Milestone 1: first reviewed campaign dossiers

Deliverables:

- Campaign records and resolved commander and army identities. Command ledgers carry a commander
  registry; cross-engagement army identities remain unresolved.
- Source-dependent alternative estimates and a typed quantity schema. The schema (v3) is in use
  for Shiloh; historical reconciliation remains.
- Explicit replacement boundaries and contemporary information sets.
- Named review records and an extraction-error audit. Review records exist for every batch through
  2026-10-06, indexed in one disposition vocabulary. [Extraction audit v1](extraction-audit.md),
  done by the primary, found 0 material and 8 minor errors in 150 random claims; an independent
  extraction sample remains (Milestone 2).
- A feature-admission mapping tied to immutable sources and dossier versions.

Acceptance requires that:

- every admitted fact has traceable evidence;
- source alternatives remain visible;
- a population or timing disagreement is resolved or kept as a dispute;
- the v1 opening profile excludes post-boundary state and participation, including indirect use
  through transformations.

### Milestone 2: baseline audit and expanded coverage

- Document an exact reproduction route for the original Arsht analysis and its access and
  redistribution terms, as a track separate from the reduced baseline.
- Enrich the frozen cohort by complete campaigns, adding credible troop estimates without
  selecting only famous or easily scored battles.
- Audit coverage by outcome, commander, campaign, engagement scale and evidence quality.

Acceptance requires an immutable cohort, an exclusion ledger, an independent extraction sample,
and paired comparison rows defined before model selection. Sparse evidence must not quietly
become mediocre commander scores.

### Milestone 3: enriched prediction and command inference

- Predefine the campaign estimand and the causal graph.
- Add justified conditions and opponent and army context.
- Investigate whether commander assignment is confounded.
- Fit hierarchical partial-pooling alternatives only when coverage supports them.
- Evaluate on grouped held-out campaigns and a locked final test set, and check temporal
  generalization separately.
- Report calibration and clustered uncertainty.

Acceptance requires:

- better out-of-sample prediction on comparable rows;
- results robust to source and coding sensitivities;
- a separately defended causal interpretation.

A familiar-looking list of great generals is not evidence of correctness.

### Milestone 4: inspectable research interface

- An explorer that traces commander → campaign → engagement → assumption → passage. A static
  version exists (2026-10-06): commander, campaign, engagement, claim, passage, source and hash
  pages, rebuilt and published from each pushed commit.
- Cumulative results, opportunity-adjusted estimates, coverage, uncertainty and source disputes,
  each shown separately.
- Scenario toggles that explain what changes.
- No double counting of battles and campaigns, and no unqualified cross-era rankings.

## Review policy

Owner policy since 2026-10-06 ([AGENTS.md](../AGENTS.md#review-policy)): there is no separate
design or evidence review step. The primary agent verifies its own work against the sources and
checks before committing, and that work is labelled primary-verified.

Earlier work had separate AI reviews:

- Claude Opus 5.5 `high`, from 2026-09-24 to 2026-10-06;
- GPT-6 Astra `xhigh`, before 2026-09-24.

Those reviews remain records of their own scope. A separate review runs only when the owner asks
for one.

## Deferred implementation choices

- **Research authoring and paid automation:** policies remain undecided.
- **External researchers:** evidence packets also work with an external researcher of the
  user's choice.
- **Extraction libraries:** LangExtract or another library can be evaluated later, against a
  measured need for source alignment.
- **Frozen-ledger corrections:** corrections to a dossier that a frozen ledger binds are installed
  under the [replay design](ledger-replay.md). Each frozen ledger replays in a temporary view that
  presents the archived bytes it binds.

## Owner ideas to design later

- **Graded outcomes, not win/loss only** (owner, 2026-09-25): "we should probably not reward the
  same reward for a pyrrhic victory as we would for Hannibal at Cannae. Both are wins, but one is
  much more beneficial."
  - **Now:** the ratings score every decisive result as 1 or 0.
  - **Possible design:** grade how much a result achieved, for example from loss ratios relative
    to force, each army's share of losses, pursuit or destruction of the beaten force, and
    strategic follow-through.
  - **Open questions:**
    - which margins are source-backed often enough to avoid omitting battles;
    - how to keep commander-created advantages (mediators) separate from the result;
    - how to avoid double counting a campaign's outcome in its battles;
    - how an ordinal or continuous outcome changes the held-out test.
  - **Before any run:** it needs a versioned design and owner authorization. It does not change
    existing runs.
