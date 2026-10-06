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

## Status

As of 2026-10-05:

- **American Civil War: first-pass research is complete.** The [full-war frame](docs/cohort-v2.md)
  is every engagement in the pinned Civil War Sites Advisory Commission (CWSAC) battle list:
  384 engagements in 119 campaign groups, 1861–1865. No inclusion rule depends on outcome,
  commander reputation or available force figures. Every engagement has a draft evidence
  dossier ([coverage table](artifacts/pilot-report.md#draft-evidence-dossiers)).
- **Reviewed model inputs.** Versioned ledgers grade each side's strength evidence and name one
  responsible commander per side for the 305 in-scope engagements
  ([record](docs/research/ledgers-v2.md)). The other 79 are inconclusive, aggregate records, or
  involve a Native American belligerent, which the two-sided model does not cover.
- **Latest result.** [Rating run 3](docs/research/commander-ratings-v3.md) found slightly better
  held-out predictions with commander identity than with force size alone. The gain is fragile:
  under a campaign bootstrap, its campaign-weighted part cannot be told apart from zero. It is not
  a ranking of skill ([results](#results-so-far)).
- **Next: the French Revolutionary and Napoleonic Wars.** Chosen on 2026-09-25 and not yet
  started. The [scoping note](docs/napoleonic-scoping.md) lists the decisions needed before
  research begins.

## How the research is produced

AI agents do the research, under rules meant to make every claim checkable. The project
owner (the maintainer) sets the scope and authorizes each rating run.

1. **A frozen frame.** The engagement list comes from a pinned, checksum-verified source
   table and is fixed before modelling, with defeats and inconclusive results included.
2. **Draft dossiers.** Agents research by complete campaign. Each dossier covers seven
   dimensions: strength, terrain, logistics, information, objectives, responsibility and
   outcome. Every claim quotes an exact passage with its source ID and locator, and every
   source snapshot is stored with its SHA-256. Gaps and disagreements become explicit unknowns
   or disputed claims, never model recollection. A first pass inspects up to three source
   families per battle, plus one targeted follow-up.
3. **Verification.** Every Civil War dossier batch had a separate, fresh-context AI review
   (GPT-6 Astra at `xhigh` reasoning effort, then Claude Opus 5.5 at `high` from 2026-09-24).
   The authoring agent checked each proposed correction against the source before applying it.
   Since 2026-10-06, by owner policy, the authoring agent verifies its own work against the
   sources and checks before committing, and labels it primary-verified. A separate review runs
   only when the owner asks for one.
4. **Gated model inputs.** Draft dossiers never change model inputs. The frozen baseline uses
   only the pinned source tables. Rating runs use separately reviewed, versioned strength and
   command ledgers, and each is bound to the SHA-256 of its exact inputs by a recorded owner
   authorization.

AI reviews and AI verification are not human historical adjudication or proof that sources are
independent; a passage-backed claim can still be historically wrong. The code itself never
calls a model, and only the explicit `fetch` command uses the network. See
[AI's role and validation](docs/methodology.md#ais-role-and-validation) and the
[evidence contract](docs/evidence-contract.md).

## Results so far

Every result below is scored on held-out campaigns: each campaign in turn is left out of the
fit and then predicted. Lower Brier score and log loss are better. None of these is a ranking
of skill or a causal estimate, and the later runs leave the frozen baseline unchanged.

| Run | Battles | Question | Result |
| --- | --- | --- | --- |
| [Pilot baseline](artifacts/pilot-report.md) | 23 of the 127 pilot engagements | Does relative force size beat equal odds? | No: Brier 0.277 against 0.250 |
| [Strength evaluation](docs/research/estimate-evaluation-v1.md) | 21–37 pilot battles with graded strengths | Do reviewed strength estimates predict results? | Weakly: worse than equal odds on the 21 grade A rows; on the 37 A–C rows, better than equal odds but not than the training prior (campaign-weighted) |
| [Rating run 1](docs/research/commander-ratings-v1.md) | 37 pilot battles | Does adding commanders lower held-out log loss? | No detectable commander signal, so no ordered list |
| [Rating run 2](docs/research/commander-ratings-v2.md) | 126 full-war battles with graded strengths | The same test on the full war | Lower under both weightings (0.6540 vs 0.6633 by battle, 0.6795 vs 0.6844 by campaign); every commander's interval includes zero |
| [Rating run 3](docs/research/commander-ratings-v3.md) | 301 in-scope battles, 162 with a modelled side | The same test with missing strengths modelled (grade E) | Lower again (0.6476 vs 0.6597; 0.6586 vs 0.6651), but fragile: the campaign-weighted gain's 95% bootstrap interval includes zero, and Forrest's and Grant's rows carry much of the gain ([uncertainty](artifacts/commander-ratings-v3-uncertainty.md)); only Forrest's 80% interval excludes zero |

Runs 2 and 3 pass the test fixed in advance, which is read only as lower held-out log loss on
those rows; that test has no uncertainty threshold. The residual still mixes command with army quality, subordinates, theater,
opponents, coding choices and modelling error, so the ordered lists in those reports are point
summaries, not rankings. Each record names the `make` target that reproduces it.

## Planned work

Beyond the Napoleonic work, the [roadmap](docs/roadmap.md) plans a campaign-level estimand
defined before any enriched model (battle execution and campaign contribution are separate
and never added together), opponent and army context, graded outcomes rather than win or loss
only, and an interface that traces any result from commander to campaign, engagement,
assumption and passage. None of this is implemented yet.

## Run it

Requires Python 3.11 or newer and nothing else. From the repository root:

```sh
make check                              # tests plus source, evidence and pipeline validation
make reproduce                          # regenerate the committed artifacts offline
python3 -m generalship inspect TN003    # print one engagement's record (TN003 is Shiloh)
python3 -m generalship packet TN003     # prepare a research assignment; makes no AI call
python3 -m generalship admission-check  # offline proposal audit; promotes nothing
```

`python3 -m generalship fetch` restores missing pinned upstream CSVs; it is the only command
that uses the network. Checked-in historical snapshots are restored from Git, not silently
refreshed. To run from another directory, use
`python3 -m generalship --root /path/to/generalship check` with the package on the Python
path, or install it with `python3 -m pip install -e .`.

## Repository layout

| Path | Contents |
| --- | --- |
| `generalship/` | Python package and command-line interface |
| `data/` | Source registry (`sources.json`) and raw snapshots, cohorts, dossiers (`evidence/`), strength and command ledgers, and authorization records |
| `artifacts/` | Reports, predictions, research packets, review records and the input/output hash receipt |
| `docs/` | Methodology, evidence contract, designs and roadmap; `docs/research/` holds pass, ledger and run records |
| `tests/` | Offline tests |
| `design/`, `reviews/`, `prompts/`, `scripts/` | Supporting material for the Shiloh packets and review, and the researcher prompt |

## Documentation

- [Methodology and limitations](docs/methodology.md)
- [Evidence contract and review workflow](docs/evidence-contract.md)
- [Roadmap and current handoff](docs/roadmap.md)
- [Research log](docs/research-log.md): pilot campaign passes and the Shiloh source investigations
- [Reviewed feature-admission design](docs/feature-admission.md)
- [Source provenance and original-project audit](docs/sources.md)
- [Source manifest](data/sources.json), [pilot cohort](data/pilot/cohort.json) and
  [full-war cohort](data/pilot/cohort-v2.json)

## Terms

| Term | Meaning |
| --- | --- |
| Engagement, campaign group | One record in the CWSAC battle list, and the list's grouping of records into campaigns. Research, review and evaluation keep whole campaigns together. |
| Cohort | A fixed list of engagements chosen before modelling: v1 is the 127-engagement 1862–1863 pilot, v2 the 384-engagement full war. |
| Dossier | An engagement's research record in `data/evidence/`: source-cited claims across the seven dimensions. |
| Explicit unknown | A claim recording that the inspected sources do not establish a dimension. |
| Source family | Sources that share an origin; copies and reprints count once. |
| First pass | The bounded research protocol: up to three source families per battle and one targeted follow-up. |
| Primary | The main AI agent that prepares and maintains the evidence, as distinct from the separate reviewer. |
| Owner | The project maintainer. Owner decisions and run authorizations are recorded with dates. |
| Strength grades | A–C: reported figures, from A (directly applicable) to C (for example an opponent's estimate); D: no usable figure; E: a modelled typical size for a D side, used in run 3. |
| Admission | The reviewed contract an enriched predictor must pass before it can join the frozen baseline. The rating runs are exploratory diagnostics outside it. |

## License and attribution

Project code is MIT-licensed. Third-party data keeps its own terms and attribution; see
[NOTICE](NOTICE.md). The engagement frame and baseline strengths come from four pinned,
checksum-verified CWSAC tables in Jeffrey B. Arnold's
[American Civil War Battle Data](https://acw-battle-data.readthedocs.io/en/latest/). No paid
services, scheduled jobs or hosted CI are needed.
