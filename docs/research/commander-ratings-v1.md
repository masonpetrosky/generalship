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

- Under the battle weighting, the commander model's log loss was 0.0004 lower (0.66356 against
  0.66392). Under the campaign weighting, it was 0.0118 higher (0.62799 against 0.61615). The
  rule required a strictly lower value under both, so this is no improvement.
- The commander model did better in 8 of 19 held-out campaigns and worse in 11.
- Only 21 of the 37 held-out rows had a commander seen in another campaign, the effective
  denominator. A commander whose modelled battles all fall in one campaign, such as Jackson (all
  five in Jackson's Valley Campaign), never has his own θ used in a held-out prediction. His rows
  still inform α, β and his opponents' θs in other folds. For example, Jackson's VA102 row
  informs Milroy's θ, which is used when VA107 (Gettysburg Campaign) is held out.

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
- **Rank intervals span almost the whole list.** The 80% rank intervals are 1–4 of 4 for every
  Union commander. Of the five Confederates, they are 1–5 for Bragg, Ewell and Lee, 2–5 for Morgan
  and 1–4 for Jackson. Every 95% rank interval is the whole list (1–4 or 1–5).
- **Connections are weak.** Seven of the nine are `not_connected`: they share no chain of
  opponents with another ranked commander on their side, so comparisons between them rest on the
  prior.
- **No commander is `view_sensitive`.** In the robustness views where they were ranked, no 80%
  interval moved to the other side of zero, and no 80% rank interval failed to overlap the primary
  one. Three commanders were `unranked_in_view` in six refits, where their rank could not be
  tested:
  - Milroy in `command_changed_excluded`, `command_changed_successor` and
    `alternative_VA102_US_us-robert-schenck`;
  - Bragg in `command_changed_excluded` and `alternative_GA004_Confederate_cs-james-longstreet`;
  - Ewell in `superior_directing`.

  That reflects how wide the intervals are, not how robust the estimates are.
- **Outcome-only views.** These have no force term, are labelled `includes_force_size_advantage`,
  estimate a different quantity and do not set `view_sensitive`.
  - **View (i), 37 primary rows:** the nine modes move by at most 0.03.
  - **View (ii), 89 rows:** these are the 91 engagements less VA033 and VA034, which are dropped
    as nested in VA032. The largest moves are Grant (+0.17 to +0.46), Burnside (−0.02 to +0.24)
    and Jackson (+0.39 to +0.57). Jackson's 80% interval there (+0.02 to +1.11) is the only
    interval of any commander in that view to exclude zero.
  - View (ii) credits force concentration and every other advantage the commander did not
    create, and it has no held-out test. It is not a finding about Jackson.
- **Lee.** Lee's 2–3 record in the modelled rows reflects which of his battles have usable
  strength estimates. Gaines' Mill is excluded as post-start, and Malvern Hill, Second Manassas
  and Salem Church have grade D strengths (4 of his 9 attributed battles are out). The JSON now records each commander's out-of-model
  reasons (`out_of_model_reasons`). It is a coverage artifact, not a finding about Lee.

## What this means

- **The method works as designed.** It refused to rank when the data could not support a
  ranking.
- **In these data, the model does not distinguish commanders.** Likely contributors are the
  37 battles, 52 commanders, only nine with two or more modelled battles, and weak connections
  through shared opponents. The run does not test which of these limits it, or which of the
  design's choices does (τ = 0.5, side-relative θ, the attribution rules).
- **More coverage is necessary but may not be sufficient.** A Civil War rating needs at least:
  - the other 257 source-listed engagements (1861, 1864–65 and the Trans-Mississippi);
  - more of the existing 91 engagements with usable strengths on both sides.

  More battles per commander, across campaigns, would narrow the intervals and allow a sharper
  held-out test. They would not by themselves show that commanders differ. A positive result
  would still not be evidence of skill (design §§5, 8).
- **For sparser eras,** the same machinery is designed to give the same answer, or wider
  intervals, whenever evidence is thin. That is untested.

## Review

A separate Claude Opus 5.5 `high` [review](../../artifacts/review-results/ratings-run-review-14c8c3b-opus-high-v1/review.md)
checked the code against design §§3–7 and recomputed the verdict with its own implementation. The
fitted parameters, intervals, rank intervals and temporal split all match. Its seven required
corrections are applied: five memo and roadmap wording fixes, and two additions to the outputs (the
per-commander out-of-model reasons, and the outcome-only views reported with their differences).
The outputs were regenerated under the same authorization, which binds the ledgers, not the code.
The regenerated outputs keep the same verdict, estimates and rank intervals; the SDs differ by at
most 4e-9, because the covariance is now taken at the final iterate.

## Limits

- **Not a causal measure.** Force size is only partly conditioned on. Army quality, subordinates,
  opponents and theaters remain in the residual.
- **Attribution is not blind.**
- **Coverage depends on the sources.** Every result carries `whole_engagement_leakage`,
  `conditional_on_source_availability`, `not_causal` and `side_relative` (design §8).
