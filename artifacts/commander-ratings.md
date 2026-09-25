# Commander residual ratings (diagnostic)

**A residual rating is not command skill, a causal effect or a ranking of record.** It summarises how a commander's battles went relative to what force size predicts, pulled towards zero, relative to their own side.

Rows: 37 battles in 19 campaigns. Pooling τ = 0.5. Every result carries `whole_engagement_leakage`, `conditional_on_source_availability`, `not_causal`, `side_relative`.

## Held-out test (the verdict)

| Model | Log loss, battle-weighted | Log loss, campaign-weighted |
|---|---:|---:|
| Commander model | 0.6636 | 0.6280 |
| Strength only | 0.6639 | 0.6161 |

Effective denominator: 21 of 37 held-out rows had a commander seen in another campaign. Campaigns better: {'commander_model': 8, 'strength_only': 11}.

**No improvement under both weightings: commander identity adds no detectable predictive signal in these data. No ordered ranking is given.** The JSON keeps every estimate, labelled `no_heldout_signal`.

## US commanders with two or more modelled battles (alphabetical)

| Commander | Battles | W–L | θ mode | 80% interval | Rank 80% | Labels |
|---|---:|---:|---:|---:|---:|---|
| Ambrose E. Burnside | 3 | 2–1 | -0.02 | -0.62 to +0.58 | 1–4 | no_heldout_signal, not_connected |
| Robert Milroy | 2 | 0–2 | -0.25 | -0.86 to +0.36 | 1–4 | no_heldout_signal, not_connected |
| Ulysses S. Grant | 3 | 3–0 | +0.17 | -0.43 to +0.78 | 1–4 | no_heldout_signal, not_connected |
| William S. Rosecrans | 4 | 3–1 | +0.06 | -0.53 to +0.65 | 1–4 | no_heldout_signal, not_connected |

## Confederate commanders with two or more modelled battles (alphabetical)

| Commander | Battles | W–L | θ mode | 80% interval | Rank 80% | Labels |
|---|---:|---:|---:|---:|---:|---|
| Braxton Bragg | 2 | 1–1 | +0.08 | -0.53 to +0.69 | 1–5 | no_heldout_signal, not_connected |
| John Hunt Morgan | 4 | 1–3 | -0.08 | -0.67 to +0.51 | 2–5 | no_heldout_signal, not_connected |
| Richard S. Ewell | 2 | 2–0 | +0.28 | -0.33 to +0.89 | 1–5 | no_heldout_signal |
| Robert E. Lee | 5 | 2–3 | +0.09 | -0.49 to +0.67 | 1–5 | no_heldout_signal, not_connected |
| Thomas J. Jackson | 5 | 4–1 | +0.39 | -0.18 to +0.97 | 1–4 | no_heldout_signal |

Commanders with one modelled battle, and those outside the model, are in the JSON with their coverage; their ratings are almost entirely the prior.
