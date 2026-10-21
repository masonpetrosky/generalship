# Generalship

**Can AI improve WAR-style ratings of historical generals?**

We use AI to assemble source-backed battle data and develop our own commander models.
Data comes directly from historical sources; we do not import Arsht’s dataset or code or
use his ranking as a target. This is an exploratory project for fun. Provisional estimates, uncertain
inputs and unsuccessful experiments stay visible; the estimates do not establish causal
wins above replacement.

**[Explore the expanded battle table, 1618–1905](https://masonpetrosky.github.io/generalship/results/artifacts-bodart-bulk-v1.html)**:
1,682 detected entries from Bodart’s compilation, with source pages, commander strings,
personnel readings and explicit unknowns. [Download the CSV](artifacts/bodart-bulk-v1.csv).
It combines 708 existing checked entries with 974 new OCR candidates; 34 new entries have
scoped image corrections. This provisional table is not a new ratings run.

## Results so far

The [Civil War comparison](artifacts/commander-comparison-v1.md) covers **301 battles in 108 source campaign groups** and shows
provisional within-side orders for **91 commanders** with at least two credited battles.
The other 222 saved commanders retain their coverage records without an assigned order.
Both methods put Grant first among the 49 Union commanders and Forrest first among the
42 Confederates. Most model intervals overlap widely. Disconnected opponent networks
limit comparisons; the report marks the saved model’s connectivity flags.

**A better ranking is not demonstrated.** On the same held-out campaigns:

| Model | Battle log loss | Campaign log loss |
| --- | ---: | ---: |
| Strength-only baseline | 0.656313 | 0.667838 |
| Full commander model | 0.650044 | 0.668521 |
| Simpler commander variant, saved diagnostic | 0.644558 | 0.662931 |

Lower is better. The full model is slightly better per battle and slightly worse when each
campaign counts equally. The simpler variant has better point results, with campaign
uncertainty spanning no improvement. These are reused development results, not a new final
test. Both score columns already use our AI-researched data; this is an adaptation of
Arsht’s scoring idea, not a reproduction of his published rankings or a test isolating AI’s
benefit over his data. See the [comparison](artifacts/commander-comparison-v1.md) and the
[unchanged run-4 record](docs/research/commander-ratings-v4.md).

## Data and evidence

- **Bodart, 1618–1905:** all 552 battle-description pages processed; 1,682 candidate entries,
  1,040 paired personnel readings, 121 naval entries and 70 unresolved year readings.
  OCR errors are measured and retained; printed names are not resolved commander identities.
- **American Civil War:** 384 engagements in 119 source campaign groups, all with first-pass
  dossiers. Strength and command ledgers cover 305 in-scope engagements; four nested records
  are excluded from the 301-battle model. In 120 battles, at least one strength is modelled.
- **Napoleonic Wars:** 325 land engagements of 1805–1815 across 16 groups, all with first-pass
  dossiers. The existing compiler-strength benchmark scores 194 of 273 development entries;
  52 final entries remain reserved. Force size improves grouped prediction, while the 1813
  forward check is weak and sensitivity-dependent. No Napoleonic commander ranking exists.
- **Sources:** preserved snapshots, exact passages, locators and SHA-256 hashes. Missing
  evidence, conflicting accounts and differences between people present and engaged remain
  explicit. AI verification checks extraction; it does not establish historical truth.

[Browse the evidence](https://masonpetrosky.github.io/generalship/), or explore
[Napoleonic battles that surprised the troop-count model](https://masonpetrosky.github.io/generalship/napoleonic/surprises.html).

## Working approach

Reuse existing data, compare results quickly, and expand through source-linked structured
battle tables. Research consequential exceptions selectively. A complete seven-dimension
dossier is not required for each exploratory table row. New predictors still need their
admission contract before entering a frozen model. Existing research and model records
remain intact. The [roadmap](docs/roadmap.md) holds the current priority; the
[research log](docs/research-log.md) retains completed batches and experiments.

## Run it

Python 3.11 or newer; standard library only. From the repository root:

```sh
make bodart-bulk                        # regenerate the broad source table; no fit or fetch
make commander-comparison              # regenerate the comparison from saved results; no fit
make check                             # offline tests and data-contract checks
make reproduce                         # regenerate committed derived artifacts offline
python3 -m generalship site             # build the explorer in _site/
python3 -m generalship inspect TN003    # inspect one engagement (Shiloh)
```

Historical rating jobs remain explicit commands; ordinary tests and reproduction do not
rerun them. `python3 -m generalship fetch` explicitly restores missing pinned upstream CSVs.
Historical snapshots are restored from Git. To work from another directory, install with
`python3 -m pip install -e .` and use the CLI’s `--root` option.

## Documentation and attribution

- [Methodology and limits](docs/methodology.md)
- [Evidence contract](docs/evidence-contract.md) and [feature admission](docs/feature-admission.md)
- [Sources and original-project audit](docs/sources.md), [source registry](data/sources.json)
- [Full Civil War cohort](docs/cohort-v2.md), [Napoleonic frame](docs/napoleonic-frame.md)
- [Earlier commander experiments](docs/research/commander-ratings-v4.md)

Project code is MIT-licensed. Third-party sources retain their own terms; see [NOTICE](NOTICE.md).
The original inspiration was [Ethan Arsht’s military rankings](https://github.com/ethanarsht/military_rankings).
The Civil War frame comes from pinned CWSAC tables in Jeffrey B. Arnold’s
[American Civil War Battle Data](https://acw-battle-data.readthedocs.io/en/latest/).
GitHub Actions checks Python 3.11 and 3.14 and publishes the explorer from each pushed commit.
