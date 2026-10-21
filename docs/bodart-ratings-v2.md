# Bodart ratings v2: bounded alias migration

Fixed on 2026-10-21 before this rerun. The owner accepted a small source-backed
name cleanup followed immediately by rerunning the same model. That acceptance
authorizes this versioned descriptive experiment. The primary admits the eight
explicit groups in `data/bodart/aliases-v1/aliases.json` for this run only.

Use exactly the original 542 admitted engagement IDs and their original force,
year, outcome and source readings. No excluded row is rescued, no commander is
added to a joint label, and none of the 52 reserved-final entries is consulted
numerically. The raw table, first cohort, first run, its code and older studies
remain immutable. This changes the grouping of printed command labels only.

The eight groups cover Bonaparte/Napoleon, Archduke Karl of Austria, Melas,
Coburg/Koburg, Gouvion Saint-Cyr, Wellington/Wellesley, Bennigsen and Kray.
Selection uses exposure, spelling/title variants and Bodart's index support;
the first run's outcomes and rankings are already known. It is not blinded.
No fuzzy matching, automatic surname merging or reputation-based resolution is
allowed. Every admitted occurrence is enumerated against the frozen cohort.
Unlisted names and uncertain candidates stay separate after this bounded batch.

Evidence comes from inspected page images of Bodart's alphabetic index and
primary manual selections. This supports compiler-level co-reference, not
independent historical identity adjudication or verified command responsibility.
The index groups Wellesley/Wellington battle pages, including the compiler's
printed Marquis-Wellesley titles; those titles are preserved, not endorsed.
The Karl entry omits p.312 and the Melas entry omits p.355. These omissions remain
in the mapping; repeated identical scoped name strings connect those rows to
the aliases supported on other indexed pages. The Bonaparte entry explicitly
redirects Napoleon to Napoleon I while distinguishing Jérôme and Joseph.

Each group binds exact source IDs, locators, quotations, SHA-256s, facsimiles,
original normalized labels, raw strings and row/side occurrences. New sources
use a companion registry so existing registry bindings do not change. Numeric
page references in the index are bibliographic evidence, not additional model
observations. No dossier feature or opening/causal measurement is admitted.

Reuse the frozen v1 fitting engine without edits: symmetric force-adjusted
paired comparisons, no intercept, force prior SD 2, label prior SD 1. Keep the
same minimum three appearances, within-component ordering, marginal 95% Laplace
intervals, theta prior SD 0.5/2 sensitivities, personnel-checked sensitivity,
and leave-one-calendar-decade-out folds. If canonical sorting reverses a row,
swap both sides, negate the log force ratio and complement the binary outcome.
Never retain a winner-first orientation or give the same person two sides.

Report v1/v2 coverage, connectivity, exposures, forecast availability, rankings
and paired held-out metrics on identical rows/folds. A change in grouping also
changes partial pooling and effective prior structure; this is not a pure test
of biographical truth. Preserve worse results. No criterion, prior or alias is
chosen after viewing the rerun. This remains development evaluation, not final
or forward validation, causal WAR, or proof that AI improves generalship ratings.

The saved run binds the fixed mapping, prepared migration, sources, protocol,
fitting/migration code and original inputs by SHA-256, with the base Git commit
recorded. Code and this contract are fixed before fitting; the completed batch
is committed after primary verification. No second review or second-opinion
prompt is part of the process. Stop after this rerun, comparison and publication.

`python3 -m generalship.bodart_ratings_v2 --prepare` writes the scoped migration;
`--run` is the explicit historical job. The default checks saved results;
`--write` regenerates the report and CSV without fitting. Ordinary tests and
`make reproduce` never execute this historical fitting job.
