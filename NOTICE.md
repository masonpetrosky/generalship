# Attribution and third-party material

## American Civil War Battle Data

Jeffrey B. Arnold, **American Civil War Battle Data**, version 11.0.0 metadata,
snapshot commit `3a6020dbfcbcfc650a268b10a9f155588472432b`.

- [Original repository](https://github.com/jrnold/acw_battle_data)
- [Pinned license metadata](https://github.com/jrnold/acw_battle_data/blob/3a6020dbfcbcfc650a268b10a9f155588472432b/rawdata/metadata/datapackage.yaml)
- [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)

The four `data/raw/cwsac_*.csv` files are unmodified copies. Their historical
source is the U.S. National Park Service / Civil War Sites Advisory Commission
battle summaries, digitized and organized by Arnold. The cohort, normalized records,
research claims, audit results, and model outputs are Generalship's transformations
and interpretations. They have not been endorsed by Arnold, NPS, or CWSAC.

The older hosted version 8.0.0 documentation displays ODC-BY; this repository follows
the CC-BY-4.0 metadata of the exact version used and retains that metadata locally.
MIT licensing of Generalship code does not relicense third-party material.

## National Park Service text

`data/raw/nps-*.txt` contains government-authored NPS battle-summary text retrieved
on 2026-09-20. Source links and normalization details are in `data/sources.json`.
No NPS images, marks, or logos are included. Dossiers quote and interpret the
identified accounts; these are not independent corroboration of NPS-derived CSVs.

## Inspiration

Ethan Arsht's [military_rankings](https://github.com/ethanarsht/military_rankings)
inspired the battle residual approach. His notebook was inspected for methodology;
no code, notebook, or dataset from that repository is distributed here. Generalship
does not reproduce his published rankings or imply his endorsement.
