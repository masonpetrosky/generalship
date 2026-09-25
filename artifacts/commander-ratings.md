# Commander residual ratings (diagnostic)

**A residual rating is not command skill, a causal effect or a ranking of record.** It summarises how a commander's battles went relative to what force size predicts, pulled towards zero, relative to their own side.

Rows: 37 battles in 19 campaigns. Pooling τ = 0.5. Every result carries `whole_engagement_leakage`, `conditional_on_source_availability`, `not_causal`, `side_relative`.

## Held-out test (the verdict)

| Model | Log loss, battle-weighted | Log loss, campaign-weighted |
|---|---:|---:|
| Commander model | 0.6636 | 0.6280 |
| Strength only | 0.6639 | 0.6161 |

Effective denominator: 21 of 37 held-out rows had a commander seen in another campaign (Ambrose E. Burnside, Braxton Bragg, John Hunt Morgan, Richard S. Ewell, Robert E. Lee, Robert Milroy, Ulysses S. Grant, William S. Rosecrans). Campaigns where each model had lower log loss: commander model 8, strength only 11, ties 0.

Descriptive 1862→1863 split (no verdict): trained on 19, tested on 18; log loss 0.6602 (commander model) against 0.6696 (strength only).

**No improvement under the both-weightings rule (a lower held-out log loss was required under both weightings, and it was not lower under both): commander identity adds no detectable predictive signal in these data. No ordered ranking is given.** The JSON keeps every estimate, labelled `no_heldout_signal`.

## US commanders with two or more modelled battles (alphabetical)

| Commander | Battles | W–L | θ mode | 80% interval | 95% interval | Rank 80% | SD ratio | Labels |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Ambrose E. Burnside | 3 | 2–1 | -0.02 | -0.62 to +0.58 | -0.94 to +0.90 | 1–4 | 0.94 | no_heldout_signal, not_connected |
| Robert Milroy | 2 | 0–2 | -0.25 | -0.86 to +0.36 | -1.18 to +0.68 | 1–4 | 0.95 | no_heldout_signal, not_connected |
|  | unranked in: command_changed_excluded, command_changed_successor, alternative_VA102_US_us-robert-schenck | | | | | | | |
| Ulysses S. Grant | 3 | 3–0 | +0.17 | -0.43 to +0.78 | -0.75 to +1.10 | 1–4 | 0.95 | no_heldout_signal, not_connected |
| William S. Rosecrans | 4 | 3–1 | +0.06 | -0.53 to +0.65 | -0.84 to +0.97 | 1–4 | 0.92 | no_heldout_signal, not_connected |

## Confederate commanders with two or more modelled battles (alphabetical)

| Commander | Battles | W–L | θ mode | 80% interval | 95% interval | Rank 80% | SD ratio | Labels |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Braxton Bragg | 2 | 1–1 | +0.08 | -0.53 to +0.69 | -0.85 to +1.02 | 1–5 | 0.95 | no_heldout_signal, not_connected |
|  | unranked in: command_changed_excluded, alternative_GA004_Confederate_cs-james-longstreet | | | | | | | |
| John Hunt Morgan | 4 | 1–3 | -0.08 | -0.67 to +0.51 | -0.98 to +0.82 | 2–5 | 0.92 | no_heldout_signal, not_connected |
| Richard S. Ewell | 2 | 2–0 | +0.28 | -0.33 to +0.89 | -0.65 to +1.21 | 1–5 | 0.95 | no_heldout_signal |
|  | unranked in: superior_directing | | | | | | | |
| Robert E. Lee | 5 | 2–3 | +0.09 | -0.49 to +0.67 | -0.80 to +0.97 | 1–5 | 0.90 | no_heldout_signal, not_connected |
| Thomas J. Jackson | 5 | 4–1 | +0.39 | -0.18 to +0.97 | -0.49 to +1.27 | 1–4 | 0.90 | no_heldout_signal |

Outcome-only views (no force term, `includes_force_size_advantage`) estimate a different quantity; each commander's view results and differences from the primary rating are in the JSON.

Commanders with one modelled battle are in the JSON with their estimate, which is almost entirely the prior. Commanders outside the model are listed there with coverage only.
