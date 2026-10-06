# Commander residual ratings, run 4 (diagnostic)

**A residual rating is not command skill, a causal effect or a ranking of record.** It summarises how a commander's battles went relative to what force size and the theater and period predict, pulled towards zero, relative to their own side.

Rows: 301 battles in 108 campaigns; 120 with a modelled (grade E) side, of which 15 because their only figures were post-start; 18 with a joint-command side, which gets no commander term. 20 imputations. Every result carries `whole_engagement_leakage`, `conditional_on_source_availability`, `not_causal`, `side_relative`, `modelled_strength`.

## The verdict (pre-registered)

Rule: campaign-bootstrap 95th percentile of the log-loss difference (commander minus context) below zero under both the battle and the campaign weighting.

| Model | Log loss, battle-weighted | Log loss, campaign-weighted |
|---|---:|---:|
| Commander + context (τ estimated in each fold) | 0.6500 | 0.6685 |
| Context only | 0.6674 | 0.6771 |
| Commander + context (τ = 0.5) | 0.6513 | 0.6677 |
| Commander, no context (τ = 0.5) | 0.6446 | 0.6629 |
| Strength only | 0.6563 | 0.6678 |

| Commander minus context | Difference | 95th percentile (the rule) | 95% interval | Resamples ≥ 0 |
|---|---:|---:|---:|---:|
| Battle-weighted | -0.0174 | -0.0054 | -0.0320 to -0.0030 | 0.9% |
| Campaign-weighted | -0.0086 | +0.0092 | -0.0289 to +0.0130 | 20.9% |

**No improvement under the pre-registered rule: commander identity adds no detectable predictive signal beyond force size and context in these data. No ordered ranking is given.** The JSON keeps every estimate, labelled `no_heldout_signal`.

Descriptive, not part of the verdict: the commander model did better in 65 campaigns and worse in 43 (ties 0; exact two-sided sign-test p = 0.043); 236 of 301 held-out rows had a commander seen in another campaign; Monte Carlo check of the difference: imputations 1–10: -0.0179 battle, -0.0090 campaign; imputations 11–20: -0.0168 battle, -0.0082 campaign.

## Other held-out comparisons (descriptive)

| Comparison | Battle-weighted | Campaign-weighted | 95% interval, battle | 95% interval, campaign |
|---|---:|---:|---:|---:|
| Commander + context (τ = 0.5) − Context only | -0.0161 | -0.0095 | -0.0285 to -0.0043 | -0.0262 to +0.0076 |
| Commander, no context (τ = 0.5) − Strength only | -0.0118 | -0.0049 | -0.0232 to -0.0005 | -0.0203 to +0.0114 |
| Context only − Strength only | +0.0111 | +0.0093 | -0.0082 to +0.0325 | -0.0127 to +0.0312 |
| Commander + context (τ estimated in each fold) − Strength only | -0.0063 | +0.0007 | -0.0272 to +0.0161 | -0.0245 to +0.0263 |
| Bridge: run 3's configuration on the v3 ledger, commander − strength only | -0.0134 | -0.0073 | -0.0252 to -0.0017 | -0.0233 to +0.0096 |

Without the rows that had a post-start side or a joint-command side (267 kept; stored predictions, no refit), commander minus context is -0.0159 battle-weighted and -0.0055 campaign-weighted (95th percentiles -0.0029 and +0.0143).

Concentration (no refit): the net gain over all rows is 5.228; Nathan Bedford Forrest's 12 rows carry 2.408. Without them, commander minus context is -0.0098 battle-weighted and -0.0054 campaign-weighted (95th percentiles -0.0004 and +0.0069).

## How much do commanders differ? (τ, descriptive)

On all rows, the Laplace marginal likelihood (mean over imputations) peaks at τ = 0.6 on the grid 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.25, 1.5; grid values within 1.92 log units of the peak run from 0.2 to 1.0 (an approximate 95% profile interval; it excludes τ = 0, no commander spread). In the held-out folds, τ-hat was 0.5 in 2, 0.6 in 106 of 108 folds. Ratings below use τ = 0.6 (tau hat).

Calibration: with outcomes simulated 100 times from the context model (no commander differences; first 5 imputations), the largest log-evidence gain over the grid had median 0.00 and 95th percentile 0.89; the observed gain on the same imputations is 2.51 (p = 0.010).

| τ | Log evidence minus context model |
|---:|---:|
| 0.0 | +0.00 |
| 0.1 | +0.19 |
| 0.2 | +0.68 |
| 0.3 | +1.29 |
| 0.4 | +1.84 |
| 0.5 | +2.21 |
| 0.6 | +2.36 |
| 0.8 | +1.99 |
| 1.0 | +0.95 |
| 1.25 | -0.89 |
| 1.5 | -3.01 |

Descriptive 1861–1863→1864–1865 split (no verdict): trained on 167, tested on 134, τ-hat 0.6 on the training years; log loss commander + context (τ estimated in each fold) 0.6321, context only 0.6457, commander + context (τ = 0.5) 0.6343, commander, no context (τ = 0.5) 0.6429, strength only 0.6505.

## US commanders with two or more modelled battles (alphabetical)

| Commander | Battles | Modelled-strength rows | W–L | Pooled θ | 80% interval | 95% interval | Rank 80% | SD ratio | Labels |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| A.J. Smith | 2 | 1 | 2–0 | +0.15 | -0.58 to +0.88 | -0.96 to +1.26 | 4–42 | 0.95 | no_heldout_signal, not_connected |
| Alfred Pleasonton | 3 | 2 | 2–1 | +0.01 | -0.70 to +0.72 | -1.07 to +1.09 | 7–44 | 0.92 | no_heldout_signal |
| Alfred Torbert | 2 | 1 | 2–0 | +0.23 | -0.50 to +0.95 | -0.89 to +1.34 | 3–40 | 0.94 | no_heldout_signal, not_connected |
| Ambrose E. Burnside | 7 | 3 | 5–2 | +0.16 | -0.47 to +0.79 | -0.80 to +1.13 | 5–40 | 0.82 | no_heldout_signal |
| Benjamin Franklin Butler | 5 | 2 | 2–3 | -0.17 | -0.83 to +0.50 | -1.18 to +0.85 | 11–46 | 0.87 | no_heldout_signal |
| Benjamin M. Prentiss | 2 | 0 | 2–0 | +0.22 | -0.50 to +0.95 | -0.88 to +1.33 | 3–40 | 0.94 | no_heldout_signal, not_connected |
| Cuvier Grover | 3 | 3 | 2–1 | +0.08 | -0.61 to +0.79 | -0.99 to +1.17 | 5–43 | 0.92 | no_heldout_signal |
| David G. Farragut | 2 | 2 | 2–0 | +0.19 | -0.54 to +0.93 | -0.93 to +1.30 | 4–41 | 0.95 | no_heldout_signal, not_connected |
| David Hunter | 2 | 0 | 1–1 | -0.02 | -0.73 to +0.69 | -1.09 to +1.07 | 7–45 | 0.92 | no_heldout_signal |
| E. R. S. Canby | 3 | 1 | 2–1 | -0.05 | -0.75 to +0.67 | -1.11 to +1.03 | 8–45 | 0.92 | no_heldout_signal |
| Edward O.C. Ord | 2 | 1 | 2–0 | +0.25 | -0.47 to +0.97 | -0.84 to +1.35 | 3–39 | 0.93 | no_heldout_signal |
| Erastus Tyler | 2 | 1 | 0–2 | -0.27 | -0.99 to +0.45 | -1.37 to +0.82 | 12–47 | 0.93 | no_heldout_signal |
| Fitz John Porter | 4 | 2 | 2–2 | -0.07 | -0.75 to +0.62 | -1.10 to +0.97 | 8–45 | 0.88 | no_heldout_signal |
| Franz Sigel | 2 | 0 | 0–2 | -0.28 | -1.00 to +0.45 | -1.38 to +0.82 | 13–47 | 0.94 | no_heldout_signal |
| Frederick Steele | 3 | 2 | 3–0 | +0.26 | -0.46 to +0.97 | -0.82 to +1.34 | 3–39 | 0.92 | no_heldout_signal |
| G.K. Warren | 4 | 1 | 4–0 | +0.46 | -0.23 to +1.14 | -0.58 to +1.50 | 2–33 | 0.89 | no_heldout_signal |
| George B. McClellan | 3 | 0 | 3–0 | +0.41 | -0.29 to +1.11 | -0.65 to +1.48 | 2–35 | 0.91 | no_heldout_signal |
| George Crook | 2 | 0 | 1–1 | -0.03 | -0.74 to +0.68 | -1.12 to +1.06 | 7–45 | 0.93 | no_heldout_signal |
| George G. Meade | 4 | 0 | 3–1 | +0.18 | -0.50 to +0.86 | -0.87 to +1.21 | 4–40 | 0.88 | no_heldout_signal |
| George H. Thomas | 5 | 2 | 4–1 | +0.07 | -0.61 to +0.75 | -0.97 to +1.11 | 6–43 | 0.89 | no_heldout_signal |
| George Stoneman | 2 | 1 | 2–0 | +0.23 | -0.49 to +0.95 | -0.88 to +1.34 | 3–40 | 0.94 | no_heldout_signal |
| H. Judson Kilpatrick | 4 | 3 | 2–2 | -0.24 | -0.92 to +0.45 | -1.29 to +0.79 | 12–47 | 0.89 | no_heldout_signal |
| Horatio G. Wright | 2 | 0 | 1–1 | -0.03 | -0.75 to +0.68 | -1.11 to +1.05 | 7–45 | 0.93 | no_heldout_signal |
| Irvin McDowell | 2 | 0 | 0–2 | -0.24 | -0.97 to +0.49 | -1.34 to +0.87 | 11–47 | 0.94 | no_heldout_signal |
| Jacob D. Cox | 2 | 1 | 1–1 | -0.04 | -0.77 to +0.68 | -1.15 to +1.07 | 7–45 | 0.94 | no_heldout_signal |
| James G. Blunt | 6 | 4 | 4–2 | +0.09 | -0.57 to +0.73 | -0.93 to +1.08 | 6–41 | 0.85 | no_heldout_signal |
| James H. Wilson | 4 | 0 | 1–3 | -0.25 | -0.92 to +0.42 | -1.28 to +0.78 | 13–47 | 0.87 | no_heldout_signal |
| James M. Williams | 2 | 1 | 1–1 | -0.03 | -0.75 to +0.69 | -1.14 to +1.07 | 7–45 | 0.94 | no_heldout_signal, not_connected |
| James Negley | 2 | 1 | 2–0 | +0.18 | -0.54 to +0.90 | -0.92 to +1.30 | 4–41 | 0.94 | no_heldout_signal, not_connected |
| James Shackelford | 2 | 1 | 1–1 | -0.15 | -0.88 to +0.57 | -1.27 to +0.94 | 9–46 | 0.95 | no_heldout_signal |
| John G. Foster | 2 | 2 | 2–0 | +0.26 | -0.45 to +0.98 | -0.83 to +1.34 | 3–40 | 0.93 | no_heldout_signal, not_connected |
| John G. Parke | 2 | 1 | 2–0 | +0.22 | -0.49 to +0.95 | -0.86 to +1.33 | 4–40 | 0.93 | no_heldout_signal, not_connected |
| John M. Schofield | 4 | 2 | 3–1 | +0.03 | -0.66 to +0.73 | -1.03 to +1.10 | 6–43 | 0.90 | no_heldout_signal |
| John McNeil | 3 | 1 | 3–0 | +0.41 | -0.30 to +1.09 | -0.68 to +1.44 | 2–35 | 0.90 | no_heldout_signal |
| John T. Wilder | 2 | 2 | 1–1 | -0.11 | -0.84 to +0.61 | -1.20 to +0.99 | 9–46 | 0.94 | no_heldout_signal, not_connected |
| Joseph A. Mower | 2 | 1 | 2–0 | +0.15 | -0.58 to +0.88 | -0.96 to +1.26 | 4–42 | 0.95 | no_heldout_signal |
| Joseph Hooker | 3 | 1 | 1–2 | -0.31 | -1.02 to +0.39 | -1.40 to +0.75 | 13–47 | 0.91 | no_heldout_signal |
| Nathaniel Lyon | 2 | 0 | 1–1 | -0.07 | -0.80 to +0.65 | -1.17 to +1.04 | 8–45 | 0.94 | no_heldout_signal |
| Nathaniel P. Banks | 7 | 1 | 4–3 | -0.09 | -0.74 to +0.55 | -1.07 to +0.91 | 9–44 | 0.84 | no_heldout_signal |
| Philip Sheridan | 8 | 1 | 6–2 | +0.29 | -0.35 to +0.93 | -0.67 to +1.27 | 4–36 | 0.82 | no_heldout_signal |
| Quincy A. Gillmore | 4 | 1 | 1–3 | -0.38 | -1.06 to +0.30 | -1.44 to +0.65 | 16–48 | 0.89 | no_heldout_signal, not_connected |
| Robert Milroy | 2 | 0 | 0–2 | -0.27 | -0.99 to +0.44 | -1.37 to +0.83 | 12–47 | 0.93 | no_heldout_signal |
| Samuel D. Sturgis | 4 | 3 | 2–2 | -0.25 | -0.93 to +0.44 | -1.31 to +0.79 | 13–47 | 0.90 | no_heldout_signal |
| Samuel R. Curtis | 3 | 1 | 2–1 | +0.01 | -0.69 to +0.70 | -1.06 to +1.08 | 7–44 | 0.91 | no_heldout_signal |
| Ulysses S. Grant | 10 | 2 | 9–1 | +0.47 | -0.15 to +1.10 | -0.48 to +1.44 | 2–30 | 0.81 | no_heldout_signal |
| William S. Rosecrans | 5 | 0 | 4–1 | +0.13 | -0.53 to +0.80 | -0.89 to +1.16 | 5–41 | 0.87 | no_heldout_signal |
| William T. Sherman | 10 | 5 | 5–5 | -0.38 | -0.98 to +0.23 | -1.29 to +0.54 | 18–47 | 0.79 | no_heldout_signal |
| William W. Averell | 3 | 1 | 3–0 | +0.34 | -0.36 to +1.04 | -0.73 to +1.41 | 3–37 | 0.91 | no_heldout_signal, not_connected |
| Winfield Scott Hancock | 4 | 3 | 0–4 | -0.57 | -1.24 to +0.11 | -1.61 to +0.47 | 22–49 | 0.88 | no_heldout_signal |

## Confederate commanders with two or more modelled battles (alphabetical)

| Commander | Battles | Modelled-strength rows | W–L | Pooled θ | 80% interval | 95% interval | Rank 80% | SD ratio | Labels |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| A.P. Hill | 3 | 0 | 1–2 | -0.13 | -0.82 to +0.56 | -1.20 to +0.95 | 9–39 | 0.90 | no_heldout_signal |
| Braxton Bragg | 5 | 1 | 1–4 | -0.09 | -0.76 to +0.59 | -1.12 to +0.95 | 8–39 | 0.88 | no_heldout_signal |
| D. H. Hill | 2 | 2 | 0–2 | -0.25 | -0.97 to +0.46 | -1.36 to +0.84 | 11–41 | 0.93 | no_heldout_signal |
| Douglas H. Cooper | 2 | 0 | 1–1 | -0.01 | -0.74 to +0.71 | -1.11 to +1.09 | 6–39 | 0.94 | no_heldout_signal |
| Earl Van Dorn | 5 | 3 | 1–4 | -0.21 | -0.88 to +0.47 | -1.22 to +0.82 | 11–40 | 0.87 | no_heldout_signal |
| George A. Anderson | 2 | 1 | 1–1 | +0.14 | -0.59 to +0.87 | -0.97 to +1.25 | 4–37 | 0.95 | no_heldout_signal, not_connected |
| George Pickett | 2 | 1 | 1–1 | +0.11 | -0.60 to +0.83 | -0.99 to +1.21 | 5–37 | 0.94 | no_heldout_signal |
| Henry Heth | 3 | 2 | 1–2 | -0.11 | -0.79 to +0.59 | -1.16 to +0.97 | 9–39 | 0.90 | no_heldout_signal |
| Humphrey Marshall | 2 | 2 | 1–1 | +0.03 | -0.69 to +0.76 | -1.08 to +1.15 | 6–38 | 0.94 | no_heldout_signal |
| J.E.B. Stuart | 3 | 1 | 1–2 | -0.06 | -0.76 to +0.63 | -1.13 to +1.00 | 8–39 | 0.90 | no_heldout_signal |
| James Longstreet | 7 | 4 | 4–3 | +0.34 | -0.28 to +0.97 | -0.61 to +1.32 | 3–31 | 0.82 | no_heldout_signal |
| James R. Chalmers | 3 | 1 | 2–1 | +0.23 | -0.46 to +0.92 | -0.83 to +1.30 | 4–34 | 0.90 | no_heldout_signal |
| John B. Floyd | 2 | 1 | 1–1 | +0.03 | -0.70 to +0.75 | -1.08 to +1.15 | 6–38 | 0.94 | no_heldout_signal |
| John B. Gordon | 2 | 0 | 0–2 | -0.24 | -0.96 to +0.48 | -1.34 to +0.86 | 11–41 | 0.94 | no_heldout_signal, not_connected |
| John B. Magruder | 2 | 1 | 2–0 | +0.36 | -0.36 to +1.08 | -0.73 to +1.45 | 2–32 | 0.93 | no_heldout_signal, not_connected |
| John Bell Hood | 9 | 4 | 1–8 | -0.42 | -1.06 to +0.22 | -1.38 to +0.55 | 17–41 | 0.83 | no_heldout_signal |
| John C. Breckinridge | 5 | 1 | 3–2 | +0.23 | -0.42 to +0.89 | -0.77 to +1.22 | 4–33 | 0.85 | no_heldout_signal, not_connected |
| John C. Pemberton | 3 | 2 | 1–2 | +0.09 | -0.61 to +0.81 | -1.00 to +1.18 | 5–37 | 0.93 | no_heldout_signal |
| John Hunt Morgan | 6 | 1 | 2–4 | +0.07 | -0.58 to +0.73 | -0.93 to +1.09 | 6–36 | 0.85 | no_heldout_signal |
| John S. Bowen | 3 | 2 | 1–2 | +0.12 | -0.59 to +0.83 | -0.96 to +1.21 | 5–36 | 0.93 | no_heldout_signal |
| John S. Marmaduke | 10 | 2 | 3–7 | -0.22 | -0.83 to +0.39 | -1.15 to +0.70 | 13–40 | 0.79 | no_heldout_signal |
| John S. Williams | 2 | 1 | 0–2 | -0.14 | -0.87 to +0.59 | -1.27 to +0.96 | 8–40 | 0.95 | no_heldout_signal |
| Joseph E. Johnston | 9 | 3 | 5–4 | +0.39 | -0.23 to +1.02 | -0.57 to +1.35 | 3–29 | 0.81 | no_heldout_signal |
| Joseph Wheeler | 5 | 2 | 0–5 | -0.44 | -1.13 to +0.24 | -1.46 to +0.62 | 16–41 | 0.88 | no_heldout_signal |
| Jubal A. Early | 8 | 1 | 3–5 | -0.11 | -0.74 to +0.51 | -1.07 to +0.83 | 10–39 | 0.81 | no_heldout_signal |
| Lawrence O'Bryan Branch | 2 | 0 | 0–2 | -0.25 | -0.95 to +0.47 | -1.33 to +0.85 | 11–41 | 0.93 | no_heldout_signal |
| Nathan Bedford Forrest | 12 | 4 | 9–3 | +0.96 | +0.38 to +1.54 | +0.09 to +1.83 | 1–13 | 0.75 | no_heldout_signal |
| Nathan Evans | 3 | 1 | 2–1 | +0.26 | -0.44 to +0.96 | -0.81 to +1.31 | 3–34 | 0.91 | no_heldout_signal, not_connected |
| P.G.T. Beauregard | 7 | 2 | 6–1 | +0.64 | +0.01 to +1.27 | -0.33 to +1.61 | 2–23 | 0.82 | no_heldout_signal |
| Patrick R. Cleburne | 2 | 0 | 2–0 | +0.43 | -0.29 to +1.15 | -0.65 to +1.54 | 2–30 | 0.93 | no_heldout_signal |
| Richard H. Anderson | 2 | 1 | 1–1 | +0.04 | -0.67 to +0.75 | -1.05 to +1.11 | 6–38 | 0.92 | no_heldout_signal, not_connected |
| Richard S. Ewell | 4 | 1 | 2–2 | +0.04 | -0.64 to +0.71 | -0.99 to +1.08 | 6–37 | 0.89 | no_heldout_signal |
| Richard Taylor | 7 | 3 | 1–6 | -0.41 | -1.07 to +0.25 | -1.42 to +0.60 | 16–41 | 0.86 | no_heldout_signal |
| Robert E. Lee | 18 | 5 | 8–10 | +0.05 | -0.48 to +0.58 | -0.76 to +0.85 | 9–35 | 0.69 | no_heldout_signal |
| Robert Hoke | 2 | 1 | 1–1 | +0.01 | -0.71 to +0.74 | -1.07 to +1.11 | 6–38 | 0.94 | no_heldout_signal |
| Sterling Price | 10 | 5 | 4–6 | +0.00 | -0.61 to +0.61 | -0.93 to +0.94 | 8–37 | 0.79 | no_heldout_signal |
| Thomas C. Hindman | 2 | 0 | 0–2 | -0.24 | -0.96 to +0.49 | -1.33 to +0.89 | 10–41 | 0.94 | no_heldout_signal, not_connected |
| Thomas J. Jackson | 8 | 1 | 6–2 | +0.36 | -0.28 to +0.99 | -0.61 to +1.34 | 3–30 | 0.83 | no_heldout_signal |
| Tom Green | 5 | 3 | 3–2 | +0.18 | -0.48 to +0.85 | -0.83 to +1.20 | 4–34 | 0.86 | no_heldout_signal |
| Wade Hampton | 2 | 0 | 2–0 | +0.32 | -0.40 to +1.05 | -0.77 to +1.42 | 3–33 | 0.93 | no_heldout_signal |
| William C. Quantrill | 2 | 2 | 2–0 | +0.39 | -0.33 to +1.10 | -0.72 to +1.48 | 2–31 | 0.94 | no_heldout_signal, not_connected |
| William T. Martin | 2 | 2 | 0–2 | -0.17 | -0.90 to +0.55 | -1.29 to +0.95 | 9–40 | 0.95 | no_heldout_signal |

Views, the per-view table, every held-out prediction and the per-fold τ are in the JSON. Commanders with one modelled battle are there with their estimate, which is almost entirely the prior.
