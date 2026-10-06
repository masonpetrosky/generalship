# How sure is rating run 3's verdict?

Descriptive, from the committed held-out predictions of [run 3](commander-ratings-v3.md) (SHA-256 `24f1040ec9a7…`). Nothing is refitted and the run's own verdict stands as recorded. Differences are commander-model log loss minus strength-only log loss, so **negative favours commanders**.

301 held-out rows in 108 campaigns.

| Weighting | Difference | 95% interval (campaign bootstrap) | 80% interval | Resamples ≥ 0 |
|---|---:|---:|---:|---:|
| Battle-weighted | -0.0121 | -0.0241 to -0.0005 | -0.0199 to -0.0045 | 2.1% |
| Campaign-weighted | -0.0065 | -0.0226 to +0.0102 | -0.0170 to +0.0044 | 21.7% |

Campaigns: commander model better in 61, strength only better in 47, ties 0; exact two-sided sign-test p = 0.211.

## Where the difference sits (no refit)

| Rows kept | Rows | Battle-weighted | Campaign-weighted |
|---|---:|---:|---:|
| All | 301 | -0.0121 | -0.0065 |
| Without rows with a post-start strength side | 284 | -0.0109 | -0.0060 |
| Without rows with a joint-command side | 283 | -0.0097 | -0.0021 |
| Without either | 267 | -0.0088 | -0.0021 |
| Without the rows of Nathan Bedford Forrest and Ulysses S. Grant | 278 | -0.0046 | -0.0024 |

Net log-loss gain over all rows: 3.643. The commanders whose rows carry the most and the least of it (a row counts for both of its commanders):

| Commander | Rows | Net gain |
|---|---:|---:|
| Nathan Bedford Forrest | 12 | +1.389 |
| Ulysses S. Grant | 11 | +0.982 |
| P.G.T. Beauregard | 7 | +0.913 |
| Benjamin Franklin Butler | 6 | +0.716 |
| Thomas J. Jackson | 8 | +0.694 |
| John Bell Hood | 9 | +0.601 |
| John McNeil | 3 | +0.340 |
| David G. Farragut | 4 | +0.332 |
| Horatio G. Wright | 2 | -0.313 |
| Abel Streight | 1 | -0.319 |
| Ambrose E. Burnside | 7 | -0.364 |
| James H. Wilson | 4 | -0.589 |
| Jubal A. Early | 8 | -0.623 |

## Limits

- Uses the committed held-out predictions; nothing is refitted, so a subset shows where the gain sits, not what a model fitted without those rows would give.
- A row counts toward both of its credited commanders.
- The bootstrap treats campaigns as exchangeable; it does not cover attribution, strength or source uncertainty.
- Not a new verdict: the run's own rule and result stand as recorded.
