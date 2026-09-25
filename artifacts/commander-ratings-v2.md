# Commander residual ratings (diagnostic)

**A residual rating is not command skill, a causal effect or a ranking of record.** It summarises how a commander's battles went relative to what force size predicts, pulled towards zero, relative to their own side.

Rows: 126 battles in 66 campaigns. Pooling τ = 0.5. Every result carries `whole_engagement_leakage`, `conditional_on_source_availability`, `not_causal`, `side_relative`.

## Held-out test (the verdict)

| Model | Log loss, battle-weighted | Log loss, campaign-weighted |
|---|---:|---:|
| Commander model | 0.6540 | 0.6795 |
| Strength only | 0.6633 | 0.6844 |

Effective denominator: 87 of 126 held-out rows had a commander seen in another campaign (Ambrose E. Burnside, Benjamin M. Prentiss, Braxton Bragg, E. R. S. Canby, Earl Van Dorn, Franz Sigel, George B. McClellan, George Crook, George G. Meade, George H. Thomas, Horatio G. Wright, James R. Chalmers, John Bell Hood, John C. Breckinridge, John Hunt Morgan, John M. Schofield, John McNeil, John S. Marmaduke, Joseph E. Johnston, Joseph Wheeler, Jubal A. Early, Nathan Bedford Forrest, Nathan Evans, Nathaniel P. Banks, P.G.T. Beauregard, Philip Sheridan, Quincy A. Gillmore, Richard S. Ewell, Richard Taylor, Robert E. Lee, Robert Milroy, Sterling Price, Tom Green, Ulysses S. Grant, William S. Rosecrans, William W. Averell). Campaigns where each model had lower log loss: commander model 39, strength only 27, ties 0.

Descriptive 1861–1863→1864–1865 split (no verdict): trained on 79, tested on 47; log loss 0.6592 (commander model) against 0.6666 (strength only).

Held-out log loss was lower under both weightings on these rows. This is not evidence of a persistent commander effect or of skill (design §5).

## US commanders with two or more modelled battles

| Commander | Battles | W–L | θ mode | 80% interval | 95% interval | Rank 80% | SD ratio | Labels |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| John McNeil | 2 | 2–0 | +0.23 | -0.38 to +0.83 | -0.70 to +1.16 | 2–17 | 0.95 |  |
| Benjamin M. Prentiss | 2 | 2–0 | +0.20 | -0.41 to +0.81 | -0.73 to +1.13 | 2–17 | 0.95 | not_connected |
| Philip Sheridan | 3 | 3–0 | +0.20 | -0.40 to +0.80 | -0.72 to +1.12 | 2–17 | 0.94 |  |
| George B. McClellan | 2 | 2–0 | +0.17 | -0.44 to +0.78 | -0.77 to +1.10 | 2–18 | 0.95 |  |
|  | unranked in: alternative_WV003_US_us-william-s-rosecrans | | | | | | | |
| William S. Rosecrans | 5 | 4–1 | +0.16 | -0.42 to +0.73 | -0.72 to +1.04 | 2–17 | 0.90 | not_connected |
| William W. Averell | 2 | 2–0 | +0.16 | -0.45 to +0.77 | -0.78 to +1.09 | 2–18 | 0.95 | not_connected |
| William T. Sherman | 2 | 2–0 | +0.15 | -0.46 to +0.76 | -0.78 to +1.08 | 2–18 | 0.95 |  |
| John M. Schofield | 2 | 2–0 | +0.14 | -0.47 to +0.76 | -0.79 to +1.08 | 2–18 | 0.96 |  |
|  | unranked in: command_changed_excluded | | | | | | | |
| Ulysses S. Grant | 5 | 4–1 | +0.14 | -0.44 to +0.71 | -0.75 to +1.02 | 2–18 | 0.90 |  |
| George H. Thomas | 2 | 2–0 | +0.12 | -0.49 to +0.74 | -0.82 to +1.06 | 2–18 | 0.96 |  |
| Nathaniel P. Banks | 3 | 2–1 | +0.06 | -0.54 to +0.65 | -0.86 to +0.97 | 3–19 | 0.93 |  |
| Ambrose E. Burnside | 3 | 2–1 | +0.02 | -0.57 to +0.62 | -0.89 to +0.93 | 3–19 | 0.93 |  |
| Nathaniel Lyon | 2 | 1–1 | -0.04 | -0.65 to +0.56 | -0.98 to +0.89 | 3–20 | 0.95 |  |
|  | unranked in: command_changed_excluded, command_changed_successor, alternative_MO004_US_us-samuel-d-sturgis | | | | | | | |
| Horatio G. Wright | 2 | 1–1 | -0.05 | -0.66 to +0.56 | -0.98 to +0.88 | 3–20 | 0.95 |  |
|  | unranked in: command_changed_excluded, command_changed_successor, alternative_VA122_US_us-philip-sheridan | | | | | | | |
| George Crook | 2 | 1–1 | -0.05 | -0.66 to +0.56 | -0.98 to +0.88 | 3–20 | 0.95 |  |
|  | unranked in: command_changed_excluded | | | | | | | |
| George G. Meade | 2 | 1–1 | -0.05 | -0.66 to +0.56 | -0.98 to +0.88 | 3–20 | 0.95 |  |
|  | unranked in: alternative_VA062_US_us-ulysses-s-grant | | | | | | | |
| E. R. S. Canby | 2 | 1–1 | -0.08 | -0.69 to +0.53 | -1.01 to +0.86 | 4–20 | 0.95 | not_connected |
|  | unranked in: command_changed_excluded | | | | | | | |
| Robert Milroy | 2 | 0–2 | -0.22 | -0.82 to +0.39 | -1.15 to +0.71 | 5–21 | 0.95 |  |
|  | unranked in: command_changed_excluded, command_changed_successor, alternative_VA102_US_us-robert-schenck | | | | | | | |
| Franz Sigel | 2 | 0–2 | -0.22 | -0.83 to +0.39 | -1.15 to +0.71 | 6–21 | 0.95 | not_connected |
|  | unranked in: superior_directing | | | | | | | |
| Irvin McDowell | 2 | 0–2 | -0.25 | -0.86 to +0.36 | -1.18 to +0.68 | 6–21 | 0.95 |  |
| Quincy A. Gillmore | 2 | 0–2 | -0.29 | -0.90 to +0.31 | -1.22 to +0.64 | 6–21 | 0.95 | not_connected |
|  | unranked in: superior_directing, command_changed_excluded | | | | | | | |

## Confederate commanders with two or more modelled battles

| Commander | Battles | W–L | θ mode | 80% interval | 95% interval | Rank 80% | SD ratio | Labels |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Nathan Bedford Forrest | 8 | 6–2 | +0.50 | -0.04 to +1.04 | -0.33 to +1.32 | 1–11 | 0.84 | not_connected |
| P.G.T. Beauregard | 5 | 4–1 | +0.39 | -0.18 to +0.96 | -0.48 to +1.26 | 1–13 | 0.89 |  |
| Thomas J. Jackson | 5 | 4–1 | +0.32 | -0.25 to +0.89 | -0.55 to +1.19 | 1–14 | 0.89 |  |
| Nathan Evans | 2 | 2–0 | +0.29 | -0.32 to +0.89 | -0.64 to +1.22 | 1–15 | 0.95 | not_connected |
| Richard S. Ewell | 2 | 2–0 | +0.25 | -0.36 to +0.85 | -0.68 to +1.18 | 2–16 | 0.95 |  |
|  | unranked in: superior_directing | | | | | | | |
| John C. Breckinridge | 3 | 2–1 | +0.15 | -0.45 to +0.74 | -0.76 to +1.05 | 2–16 | 0.92 | not_connected |
| Robert E. Lee | 7 | 3–4 | +0.10 | -0.45 to +0.65 | -0.75 to +0.94 | 3–16 | 0.86 |  |
| Sterling Price | 3 | 2–1 | +0.09 | -0.51 to +0.69 | -0.82 to +1.00 | 3–17 | 0.93 |  |
| Joseph E. Johnston | 2 | 1–1 | +0.05 | -0.56 to +0.66 | -0.88 to +0.98 | 3–17 | 0.95 |  |
|  | unranked in: alternative_VA005_Confederate_cs-p-g-t-beauregard | | | | | | | |
| Tom Green | 2 | 1–1 | -0.00 | -0.61 to +0.60 | -0.93 to +0.93 | 3–18 | 0.95 | not_connected |
|  | unranked in: superior_directing, command_changed_excluded, command_changed_successor, alternative_NM001_Confederate_cs-henry-hastings-sibley | | | | | | | |
| Jubal A. Early | 6 | 2–4 | -0.01 | -0.58 to +0.55 | -0.88 to +0.85 | 4–17 | 0.89 | not_connected |
| Braxton Bragg | 3 | 1–2 | -0.02 | -0.61 to +0.58 | -0.93 to +0.90 | 3–18 | 0.93 |  |
| John S. Marmaduke | 7 | 3–4 | -0.02 | -0.57 to +0.53 | -0.86 to +0.82 | 4–17 | 0.86 | not_connected |
| James R. Chalmers | 2 | 1–1 | -0.03 | -0.63 to +0.58 | -0.96 to +0.90 | 3–18 | 0.95 | not_connected |
|  | unranked in: grades_ab, superior_directing, command_changed_excluded, command_changed_successor, alternative_TN030_Confederate_cs-nathan-bedford-forrest | | | | | | | |
| John Hunt Morgan | 4 | 1–3 | -0.14 | -0.72 to +0.45 | -1.03 to +0.76 | 5–18 | 0.91 | not_connected |
| Richard Taylor | 2 | 0–2 | -0.16 | -0.77 to +0.45 | -1.09 to +0.78 | 5–18 | 0.96 |  |
| Earl Van Dorn | 2 | 0–2 | -0.18 | -0.79 to +0.43 | -1.11 to +0.75 | 5–19 | 0.95 |  |
| Joseph Wheeler | 2 | 0–2 | -0.21 | -0.82 to +0.40 | -1.14 to +0.72 | 5–19 | 0.95 | not_connected |
|  | unranked in: command_changed_excluded | | | | | | | |
| John Bell Hood | 5 | 0–5 | -0.39 | -0.97 to +0.19 | -1.27 to +0.49 | 8–19 | 0.90 |  |

Outcome-only views (no force term, `includes_force_size_advantage`) estimate a different quantity; each commander's view results and differences from the primary rating are in the JSON.

Commanders with one modelled battle are in the JSON with their estimate, which is almost entirely the prior. Commanders outside the model are listed there with coverage only.
