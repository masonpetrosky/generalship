# Commander residual ratings v1: first run

Run 2026-09-25 under the accepted [design](../commander-ratings.md). This is an exploratory
diagnostic. It is not a ranking of generals, a measure of command skill or a causal estimate.
The baseline is unchanged.

## Authorization

The owner authorized the run for the exact files named in the question, replying "Yeah, sounds
good to me" ([record](../../data/command/rating-authorization-v1.json)):

| File | SHA-256 |
| --- | --- |
| Strength ledger | `0656b03c…fde89` |
| Command ledger | `0e3f1443…cdd67e` |
| Commander registry | `2b3bbef5…0706b1` |

The code is at `0bdc480`. `python3 -m generalship commander-ratings` (`make
commander-ratings`) refuses to fit unless the record names the current hashes. It replays both
ledger checkers first. It writes [`artifacts/commander-ratings.md`](../../artifacts/commander-ratings.md)
and `artifacts/commander-ratings.json`.

## The verdict: no detectable commander signal

The design fixed the test in advance (§5). The test is leave-one-campaign-out on the 37 primary
rows, at τ = 0.5 with the primary attribution. It compares the commander model with the
strength-only model on held-out log loss. An improvement had to hold under both the battle and
the campaign weighting.

| Model | Log loss, battle-weighted | Log loss, campaign-weighted |
| --- | ---: | ---: |
| Commander model | 0.6636 | 0.6280 |
| Strength only | 0.6639 | 0.6161 |

- The battle-weighted difference is negligible (0.0003), and the campaign-weighted score is
  worse.
- The commander model did better in 8 of 19 held-out campaigns and worse in 11.
- Only 21 of the 37 held-out rows had a commander seen in another campaign, the effective
  denominator. Commanders whose battles all fall in one campaign, such as Jackson in the Valley,
  never affect a held-out prediction.

**Reading, fixed in advance.** Commander identity adds no detectable predictive signal in these
data. The Markdown report therefore gives no ordered ranking. The JSON keeps every estimate, each
labelled `no_heldout_signal`.

The descriptive 1862-to-1863 split carries no verdict. There the commander model scored slightly
lower log loss (0.660 against 0.670, trained on 19 rows and tested on 18).

## What the estimates look like

These are the nine commanders with two or more modelled battles, alphabetically within each side.
θ is on the log-odds scale and is relative to the commander's own side.

| Side | Commander | Battles (W–L) | θ mode | 95% interval |
| --- | --- | --- | ---: | ---: |
| US | Burnside | 3 (2–1) | −0.02 | −0.94 to +0.90 |
| US | Grant | 3 (3–0) | +0.17 | −0.75 to +1.10 |
| US | Milroy | 2 (0–2) | −0.25 | −1.18 to +0.68 |
| US | Rosecrans | 4 (3–1) | +0.06 | −0.84 to +0.97 |
| CS | Bragg | 2 (1–1) | +0.08 | −0.85 to +1.02 |
| CS | Ewell | 2 (2–0) | +0.28 | −0.65 to +1.21 |
| CS | Jackson | 5 (4–1) | +0.39 | −0.49 to +1.27 |
| CS | Lee | 5 (2–3) | +0.09 | −0.80 to +0.97 |
| CS | Morgan | 4 (1–3) | −0.08 | −0.98 to +0.82 |

- **Every interval includes zero.** The posterior standard deviation is 0.90–0.95 of the prior's,
  so these ratings are still mostly the prior (design §4).
- **Rank intervals span almost the whole list:** 1–4 of 4 for the Union and 1–5 or 2–5 of 5 for
  the Confederates.
- **Connections are weak.** Seven of the nine are `not_connected`: they share no chain of
  opponents with another ranked commander on their side, so comparisons between them rest on the
  prior.
- **No commander is `view_sensitive`.** No robustness view moved an 80% interval to the other side
  of zero, and none produced a non-overlapping rank interval. That reflects how wide the
  intervals are, not how robust the estimates are.
- **Lee.** Lee's 2–3 record in the modelled rows reflects which of his battles have usable
  strength estimates. Gaines' Mill is excluded as post-start, and Malvern Hill, Second Manassas
  and Salem Church have grade D strengths (4 of his 9 attributed battles are out). It is a coverage artifact, not a finding about Lee.

## What this means

- **The method works as designed.** It refused to rank when the data could not support a
  ranking.
- **These data cannot tell commanders apart.** That follows from 37 battles, 52 commanders, only
  nine with two or more battles, and weak connections through shared opponents.
- **The bottleneck is coverage, not method.** A meaningful Civil War rating needs:
  - the other 257 source-listed engagements (1861, 1864–65 and the Trans-Mississippi);
  - more of the existing 91 engagements with usable strengths on both sides.

  Only then will commanders accumulate enough battles, across campaigns, to be distinguishable.
- **For sparser eras,** the same machinery gives the same honest answer, or wider intervals,
  whenever evidence is thin.

## Limits

- **Not a causal measure.** Force size is only partly conditioned on. Army quality, subordinates,
  opponents and theaters remain in the residual.
- **Attribution is not blind.**
- **Coverage depends on the sources.** Every result carries `whole_engagement_leakage`,
  `conditional_on_source_availability`, `not_causal` and `side_relative` (design §8).
