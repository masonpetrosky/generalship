# Commander residual ratings, run 3: all battles (diagnostic)

**A residual rating is not command skill, a causal effect or a ranking of record.** It summarises how a commander's battles went relative to what force size predicts, pulled towards zero, relative to their own side.

Rows: 301 battles in 108 campaigns, 162 with a modelled (grade E) side and 17 with a post-start side. Grade E uncertainty is carried by 20 imputations. Pooling τ = 0.5. Every result carries `whole_engagement_leakage`, `conditional_on_source_availability`, `not_causal`, `side_relative`, `modelled_strength`.

## Held-out test (the verdict)

| Model | Log loss, battle-weighted | Log loss, campaign-weighted |
|---|---:|---:|
| Commander model | 0.6476 | 0.6586 |
| Strength only | 0.6597 | 0.6651 |

Effective denominator: 243 of 301 held-out rows had a commander seen in another campaign. Descriptive, not part of the verdict: campaigns where each model had lower log loss, commander model 61, strength only 47, ties 0; Monte Carlo check of the log-loss difference (commander minus strength) imputations 1–10: -0.0122 battle, -0.0068 campaign; imputations 11–20: -0.0120 battle, -0.0062 campaign.

Descriptive 1861–1863→1864–1865 split (no verdict): trained on 167, tested on 134; log loss 0.6530 (commander model) against 0.6606 (strength only).

Held-out log loss was lower under both weightings on these rows. This is not evidence of a persistent commander effect or of skill (design §5).

Within each side, commanders are listed by median within-side rank over the pooled rank draws (ties by the pooled point estimate). The order is a point summary under the design, not a finding that one commander did better than another; read it with the 80% rank intervals.

The view `strength_graded_only` reproduces run 2's primary fit (largest θ difference 0.00e+00).

## US commanders with two or more modelled battles

| Commander | Battles | Modelled-strength rows | W–L | Pooled θ | 80% interval | 95% interval | Rank 80% | SD ratio | Labels |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Ulysses S. Grant | 11 | 3 | 10–1 | +0.51 | -0.02 to +1.03 | -0.30 to +1.31 | 2–27 | 0.82 |  |
| G.K. Warren | 4 | 4 | 4–0 | +0.31 | -0.28 to +0.92 | -0.58 to +1.23 | 2–38 | 0.92 |  |
| David G. Farragut | 4 | 4 | 4–0 | +0.30 | -0.29 to +0.89 | -0.60 to +1.20 | 3–38 | 0.92 | not_connected |
| John McNeil | 3 | 1 | 3–0 | +0.29 | -0.31 to +0.88 | -0.63 to +1.22 | 3–39 | 0.93 |  |
| George B. McClellan | 3 | 1 | 3–0 | +0.25 | -0.36 to +0.84 | -0.66 to +1.16 | 3–41 | 0.93 |  |
| Frederick Steele | 3 | 3 | 3–0 | +0.23 | -0.38 to +0.83 | -0.69 to +1.13 | 3–41 | 0.94 |  |
| William W. Averell | 3 | 1 | 3–0 | +0.22 | -0.39 to +0.83 | -0.69 to +1.13 | 3–41 | 0.94 | not_connected |
| George Stoneman | 2 | 2 | 2–0 | +0.19 | -0.42 to +0.79 | -0.75 to +1.10 | 4–42 | 0.95 |  |
| Benjamin M. Prentiss | 2 | 0 | 2–0 | +0.18 | -0.43 to +0.79 | -0.76 to +1.10 | 4–43 | 0.95 | not_connected |
| James Negley | 2 | 1 | 2–0 | +0.18 | -0.43 to +0.79 | -0.75 to +1.11 | 4–43 | 0.95 | not_connected |
| Edward O.C. Ord | 2 | 1 | 2–0 | +0.18 | -0.44 to +0.78 | -0.77 to +1.12 | 4–43 | 0.96 |  |
| Philip Sheridan | 8 | 5 | 6–2 | +0.15 | -0.39 to +0.70 | -0.68 to +0.99 | 5–41 | 0.85 |  |
| Joseph A. Mower | 2 | 2 | 2–0 | +0.15 | -0.46 to +0.77 | -0.79 to +1.09 | 4–43 | 0.96 |  |
| Alfred Torbert | 2 | 1 | 2–0 | +0.15 | -0.46 to +0.77 | -0.77 to +1.09 | 4–44 | 0.96 | not_connected |
| John G. Foster | 2 | 1 | 2–0 | +0.14 | -0.47 to +0.77 | -0.79 to +1.09 | 4–43 | 0.96 | not_connected |
| William S. Rosecrans | 5 | 0 | 4–1 | +0.14 | -0.43 to +0.72 | -0.71 to +1.03 | 5–43 | 0.89 |  |
| John G. Parke | 2 | 2 | 2–0 | +0.14 | -0.48 to +0.75 | -0.80 to +1.10 | 4–44 | 0.96 | not_connected |
| A.J. Smith | 2 | 0 | 2–0 | +0.13 | -0.47 to +0.75 | -0.80 to +1.06 | 4–44 | 0.95 | not_connected |
| George H. Thomas | 5 | 3 | 4–1 | +0.13 | -0.44 to +0.70 | -0.75 to +1.00 | 5–43 | 0.89 |  |
| Ambrose E. Burnside | 7 | 3 | 5–2 | +0.13 | -0.43 to +0.67 | -0.72 to +0.95 | 5–42 | 0.86 |  |
| George G. Meade | 4 | 2 | 3–1 | +0.11 | -0.48 to +0.69 | -0.78 to +0.98 | 5–44 | 0.91 |  |
| James G. Blunt | 6 | 5 | 4–2 | +0.06 | -0.51 to +0.61 | -0.81 to +0.92 | 7–44 | 0.88 |  |
| John M. Schofield | 4 | 2 | 3–1 | +0.05 | -0.53 to +0.65 | -0.84 to +0.95 | 6–46 | 0.92 |  |
| Cuvier Grover | 3 | 3 | 2–1 | +0.04 | -0.56 to +0.63 | -0.89 to +0.95 | 6–46 | 0.93 |  |
| Alfred Pleasonton | 3 | 3 | 2–1 | +0.02 | -0.58 to +0.62 | -0.89 to +0.94 | 6–46 | 0.93 |  |
| Samuel R. Curtis | 3 | 2 | 2–1 | +0.02 | -0.59 to +0.62 | -0.91 to +0.94 | 6–46 | 0.94 |  |
| E. R. S. Canby | 3 | 1 | 2–1 | -0.01 | -0.60 to +0.60 | -0.93 to +0.90 | 7–47 | 0.94 |  |
| Jacob D. Cox | 2 | 1 | 1–1 | -0.04 | -0.65 to +0.57 | -0.96 to +0.88 | 7–48 | 0.95 |  |
| John T. Wilder | 2 | 2 | 1–1 | -0.04 | -0.65 to +0.57 | -0.96 to +0.89 | 7–48 | 0.95 | not_connected |
| James M. Williams | 2 | 1 | 1–1 | -0.04 | -0.65 to +0.57 | -0.97 to +0.90 | 7–48 | 0.95 | not_connected |
| John Pope | 2 | 2 | 1–1 | -0.04 | -0.65 to +0.56 | -0.97 to +0.91 | 8–48 | 0.95 |  |
| Alfred H. Terry | 2 | 2 | 1–1 | -0.05 | -0.65 to +0.56 | -0.97 to +0.88 | 7–48 | 0.94 |  |
| Horatio G. Wright | 2 | 0 | 1–1 | -0.05 | -0.67 to +0.56 | -1.00 to +0.89 | 8–48 | 0.96 |  |
| Nathaniel Lyon | 2 | 0 | 1–1 | -0.05 | -0.67 to +0.55 | -1.00 to +0.88 | 8–48 | 0.96 |  |
| George Crook | 2 | 0 | 1–1 | -0.06 | -0.66 to +0.56 | -0.97 to +0.88 | 8–48 | 0.95 |  |
| James Shackelford | 2 | 1 | 1–1 | -0.06 | -0.66 to +0.54 | -0.98 to +0.86 | 8–48 | 0.94 |  |
| David Hunter | 2 | 1 | 1–1 | -0.07 | -0.68 to +0.55 | -1.00 to +0.86 | 8–48 | 0.95 |  |
| Nathaniel P. Banks | 7 | 4 | 4–3 | -0.07 | -0.63 to +0.49 | -0.92 to +0.77 | 10–47 | 0.87 |  |
| Fitz John Porter | 4 | 2 | 2–2 | -0.10 | -0.67 to +0.49 | -0.97 to +0.79 | 10–48 | 0.90 |  |
| Samuel D. Sturgis | 4 | 3 | 2–2 | -0.10 | -0.68 to +0.47 | -1.00 to +0.78 | 9–48 | 0.90 |  |
| Frederick Crocker | 2 | 2 | 1–1 | -0.10 | -0.71 to +0.50 | -1.02 to +0.83 | 9–49 | 0.95 | not_connected |
| H. Judson Kilpatrick | 4 | 3 | 2–2 | -0.14 | -0.72 to +0.45 | -1.02 to +0.76 | 11–49 | 0.91 |  |
| Joseph Hooker | 3 | 2 | 1–2 | -0.17 | -0.76 to +0.43 | -1.07 to +0.74 | 11–49 | 0.93 |  |
| William T. Sherman | 10 | 7 | 5–5 | -0.17 | -0.70 to +0.35 | -0.97 to +0.62 | 14–49 | 0.82 |  |
| James H. Wilson | 4 | 3 | 1–3 | -0.23 | -0.80 to +0.35 | -1.10 to +0.64 | 13–50 | 0.90 |  |
| Erastus Tyler | 2 | 1 | 0–2 | -0.23 | -0.84 to +0.37 | -1.16 to +0.68 | 13–50 | 0.94 |  |
| Robert Milroy | 2 | 0 | 0–2 | -0.23 | -0.84 to +0.36 | -1.17 to +0.68 | 13–50 | 0.94 |  |
| Irvin McDowell | 2 | 0 | 0–2 | -0.23 | -0.84 to +0.38 | -1.18 to +0.69 | 13–50 | 0.95 |  |
| Franz Sigel | 2 | 0 | 0–2 | -0.24 | -0.85 to +0.37 | -1.18 to +0.69 | 13–50 | 0.95 |  |
| Benjamin Franklin Butler | 6 | 4 | 2–4 | -0.30 | -0.86 to +0.25 | -1.16 to +0.54 | 17–50 | 0.87 |  |
| Quincy A. Gillmore | 4 | 2 | 1–3 | -0.32 | -0.90 to +0.26 | -1.19 to +0.57 | 17–51 | 0.90 | not_connected |
| Winfield Scott Hancock | 4 | 2 | 0–4 | -0.51 | -1.09 to +0.07 | -1.39 to +0.38 | 25–52 | 0.90 |  |

## Confederate commanders with two or more modelled battles

| Commander | Battles | Modelled-strength rows | W–L | Pooled θ | 80% interval | 95% interval | Rank 80% | SD ratio | Labels |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Nathan Bedford Forrest | 12 | 4 | 9–3 | +0.62 | +0.12 to +1.12 | -0.13 to +1.38 | 1–19 | 0.78 |  |
| P.G.T. Beauregard | 7 | 2 | 6–1 | +0.54 | -0.01 to +1.09 | -0.31 to +1.38 | 1–23 | 0.86 |  |
| Thomas J. Jackson | 8 | 3 | 6–2 | +0.45 | -0.08 to +0.99 | -0.36 to +1.28 | 2–26 | 0.83 |  |
| William C. Quantrill | 2 | 2 | 2–0 | +0.29 | -0.31 to +0.89 | -0.64 to +1.21 | 2–33 | 0.94 | not_connected |
| John B. Magruder | 2 | 1 | 2–0 | +0.27 | -0.34 to +0.87 | -0.66 to +1.19 | 3–33 | 0.95 | not_connected |
| Wade Hampton | 2 | 2 | 2–0 | +0.25 | -0.35 to +0.87 | -0.67 to +1.18 | 3–33 | 0.95 |  |
| Patrick R. Cleburne | 2 | 1 | 2–0 | +0.25 | -0.35 to +0.86 | -0.68 to +1.19 | 3–33 | 0.95 |  |
| Joseph E. Johnston | 9 | 7 | 5–4 | +0.24 | -0.30 to +0.77 | -0.58 to +1.03 | 4–32 | 0.83 |  |
| James Longstreet | 7 | 6 | 4–3 | +0.22 | -0.32 to +0.77 | -0.61 to +1.06 | 4–32 | 0.85 |  |
| Nathan Evans | 3 | 0 | 2–1 | +0.21 | -0.38 to +0.80 | -0.70 to +1.11 | 3–34 | 0.93 | not_connected |
| John C. Breckinridge | 5 | 2 | 3–2 | +0.19 | -0.37 to +0.76 | -0.67 to +1.06 | 4–34 | 0.88 | not_connected |
| Tom Green | 5 | 3 | 3–2 | +0.17 | -0.38 to +0.74 | -0.69 to +1.04 | 4–34 | 0.88 |  |
| Robert E. Lee | 18 | 8 | 8–10 | +0.16 | -0.31 to +0.62 | -0.56 to +0.87 | 6–32 | 0.73 |  |
| James R. Chalmers | 3 | 1 | 2–1 | +0.13 | -0.47 to +0.72 | -0.77 to +1.03 | 4–36 | 0.93 |  |
| George Pickett | 2 | 2 | 1–1 | +0.10 | -0.52 to +0.70 | -0.84 to +1.03 | 5–37 | 0.96 |  |
| Richard S. Ewell | 4 | 1 | 2–2 | +0.07 | -0.51 to +0.65 | -0.80 to +0.95 | 5–37 | 0.90 |  |
| George A. Anderson | 2 | 1 | 1–1 | +0.07 | -0.54 to +0.67 | -0.85 to +1.00 | 5–37 | 0.94 | not_connected |
| John B. Floyd | 2 | 1 | 1–1 | +0.06 | -0.55 to +0.67 | -0.88 to +0.99 | 5–37 | 0.95 |  |
| Richard H. Anderson | 2 | 1 | 1–1 | +0.05 | -0.56 to +0.65 | -0.88 to +0.97 | 5–37 | 0.94 |  |
| Humphrey Marshall | 2 | 2 | 1–1 | +0.04 | -0.56 to +0.64 | -0.89 to +0.97 | 5–38 | 0.94 |  |
| Robert Hoke | 2 | 1 | 1–1 | +0.04 | -0.58 to +0.65 | -0.90 to +0.97 | 5–38 | 0.96 |  |
| Douglas H. Cooper | 2 | 1 | 1–1 | +0.04 | -0.58 to +0.66 | -0.89 to +0.98 | 5–38 | 0.96 |  |
| John C. Pemberton | 3 | 0 | 1–2 | +0.03 | -0.56 to +0.63 | -0.87 to +0.96 | 6–38 | 0.93 |  |
| John S. Bowen | 3 | 2 | 1–2 | +0.01 | -0.58 to +0.62 | -0.89 to +0.92 | 6–38 | 0.94 |  |
| Jubal A. Early | 8 | 2 | 3–5 | +0.00 | -0.54 to +0.55 | -0.83 to +0.83 | 7–37 | 0.85 |  |
| J.E.B. Stuart | 3 | 2 | 1–2 | -0.00 | -0.60 to +0.60 | -0.92 to +0.91 | 6–38 | 0.93 |  |
| Henry Heth | 3 | 2 | 1–2 | -0.02 | -0.61 to +0.58 | -0.94 to +0.89 | 7–38 | 0.93 |  |
| A.P. Hill | 3 | 3 | 1–2 | -0.03 | -0.63 to +0.56 | -0.96 to +0.89 | 7–39 | 0.93 |  |
| Sterling Price | 10 | 7 | 4–6 | -0.04 | -0.56 to +0.49 | -0.83 to +0.77 | 9–37 | 0.81 |  |
| John Hunt Morgan | 6 | 2 | 2–4 | -0.06 | -0.62 to +0.50 | -0.90 to +0.80 | 8–38 | 0.87 |  |
| John S. Marmaduke | 10 | 3 | 3–7 | -0.13 | -0.65 to +0.40 | -0.93 to +0.68 | 11–39 | 0.82 |  |
| Lawrence O'Bryan Branch | 2 | 2 | 0–2 | -0.14 | -0.77 to +0.47 | -1.07 to +0.80 | 9–40 | 0.96 |  |
| John B. Gordon | 2 | 1 | 0–2 | -0.15 | -0.76 to +0.47 | -1.09 to +0.77 | 9–40 | 0.96 | not_connected |
| John S. Williams | 2 | 1 | 0–2 | -0.15 | -0.76 to +0.46 | -1.08 to +0.79 | 9–40 | 0.95 |  |
| Braxton Bragg | 5 | 1 | 1–4 | -0.16 | -0.73 to +0.42 | -1.04 to +0.72 | 10–40 | 0.90 |  |
| William T. Martin | 2 | 2 | 0–2 | -0.17 | -0.78 to +0.44 | -1.11 to +0.77 | 9–40 | 0.95 |  |
| Thomas C. Hindman | 2 | 1 | 0–2 | -0.18 | -0.79 to +0.43 | -1.11 to +0.76 | 10–40 | 0.95 | not_connected |
| D. H. Hill | 2 | 2 | 0–2 | -0.20 | -0.80 to +0.41 | -1.14 to +0.72 | 11–41 | 0.95 |  |
| Earl Van Dorn | 5 | 3 | 1–4 | -0.22 | -0.79 to +0.35 | -1.08 to +0.66 | 12–40 | 0.89 |  |
| Richard Taylor | 7 | 5 | 1–6 | -0.32 | -0.89 to +0.24 | -1.19 to +0.53 | 15–41 | 0.88 |  |
| Joseph Wheeler | 5 | 3 | 0–5 | -0.39 | -0.97 to +0.18 | -1.29 to +0.47 | 17–42 | 0.89 |  |
| John Bell Hood | 9 | 3 | 1–8 | -0.43 | -0.95 to +0.12 | -1.22 to +0.40 | 20–41 | 0.84 |  |

Views, per-commander view results and every held-out prediction are in the JSON. Commanders with one modelled battle are there with their estimate, which is almost entirely the prior.
