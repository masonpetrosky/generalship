# Generalship

**An evidence-first research project for measuring historical command performance.**

The long-term aim is to compare what commanders accomplished with the opportunities
and constraints they faced, including the advantages they created before battle.
Every result should be traceable from commander to campaign to engagement to
disputed assumptions and supporting passages.

Inspired by [Ethan Arsht's military rankings](https://github.com/ethanarsht/military_rankings),
this project starts with a reproducible battle-level baseline, then builds toward
campaign-level contribution. A battle residual is **not** an estimate of how many
wins a commander caused. No validated commander ranking exists here yet.

## What works today

- A frozen **127-engagement / 36-campaign** American Civil War pilot, selected by
  dates and theaters before modeling, including defeats and inconclusive outcomes.
- Four pinned, checksum-verified CWSAC tables from Jeffrey B. Arnold's
  [American Civil War Battle Data](https://acw-battle-data.readthedocs.io/en/latest/).
- An offline import and audit pipeline: unique keys, referential integrity,
  dates, force ranges, missingness, outcome codes, and cohort membership.
- A small regularized logistic baseline using relative force size. Evaluation
  holds out whole campaigns and compares with equal odds and a training-only prior.
- Three draft dossiers: **Shiloh, Antietam, and Champion Hill**, with exact source
  passages, explicit unknowns, command questions, and inherited/created distinctions.
- A [Shiloh research memo](docs/research/shiloh.md), original reports/orders, two
  independently authored histories, and return-table scans. The follow-up
  [Confederate return audit](docs/research/shiloh-confederate-returns.md) and
  [Union availability audit](docs/research/shiloh-union-availability.md) bring it
  to 29 typed troop observations and 14 events, preserving population/timing
  differences, unknown omissions and printed discrepancies.
- A reproducible report, battle predictions, exclusion reasons, research queue,
  and input/output hash receipt. No runtime dependencies beyond Python 3.11+.

## Run it

From the repository root:

```sh
make check                         # tests + source/evidence/pipeline validation
make reproduce                     # regenerate the committed artifacts offline
python3 -m generalship inspect TN003
python3 -m generalship packet TN003 # prepare a research assignment; makes no AI call
```

`python3 -m generalship fetch` can restore missing pinned upstream CSVs. Normal
checks and builds make no network requests. The checked-in historical snapshots are
restored from Git, not silently refreshed. Run from another directory with
`python3 -m generalship --root /path/to/generalship check` when the package is on
the Python path. Optional editable installation: `python3 -m pip install -e .`.

## First result

Only **23 of 127 engagements** currently have two numerical force estimates and a
decisive result suitable for this baseline. The other engagements remain visible
in the research queue. Do not treat missing strengths as zero or invent them.

On those 23 engagements across 13 eligible campaign groups, the strength model's
held-out Brier score is **0.276882**, compared with **0.250000** for equal odds
(lower is better). This small, selected subset does not show an improvement over
equal odds. It motivates source enrichment and better evaluation; it does not
validate a ranking or prove force size is generally uninformative.

Read the [generated pilot report](artifacts/pilot-report.md) for coverage and
evaluation details. The live NPS Antietam page's zero-strength table and Shiloh's
changing forces/command illustrate why reliable dossiers come before new rankings.

## Research direction

The first [Shiloh research pass](docs/research/shiloh.md),
[Confederate return audit](docs/research/shiloh-confederate-returns.md) and
[Union availability audit](docs/research/shiloh-union-availability.md) are complete
as drafts: 43 claims preserve competing returns, reinforcement phases, dated
orders and disputed responsibility. The Union audit traces Reed's Wallace
detachment accounting and unit arrivals, while retaining unidentified original
omissions, a ten-man comparison residual and Reed's Michigan narrative/table
conflict. Confederate source and subtotal discrepancies also remain unresolved.
No canonical opening strength or independently reviewed command attribution has
been established. Next audit Nelson/Ammen crossing phases and Buell's returns,
then obtain independent historical review. The [prepared packet](artifacts/research/TN003.md)
and [dossier](data/evidence/TN003.json) preserve the open questions. Expand by complete
campaign, retaining ordinary engagements and failures in the frame.

Then define a campaign replacement boundary and outcomes before fitting enriched
models. Battle execution and campaign contribution are separate estimands; adding
them together would double count. Partial pooling, opponent/army context,
measurement uncertainty, disputed-input scenarios, and a source-exploration UI
remain planned work, not implemented capabilities.

## Read next

- [Methodology and limitations](docs/methodology.md)
- [Evidence contract and review workflow](docs/evidence-contract.md)
- [Source provenance and original-project audit](docs/sources.md)
- [Milestones and next tasks](docs/roadmap.md)
- [Source manifest](data/sources.json) and [frozen cohort](data/pilot/cohort.json)

Project code is MIT-licensed. Third-party data retains its own terms and attribution;
see [NOTICE](NOTICE.md). No paid services, scheduled jobs, or hosted CI are needed.
