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

## Historical Shiloh sources

`data/raw/shiloh/` contains selected, transformed historical text and two rendered
table pages. These retain their source attribution and are not relicensed as code.

- U.S. War Department, *The War of the Rebellion: A Compilation of the Official
  Records of the Union and Confederate Armies*, Series I, Volume X, Parts I and II
  (Washington: Government Printing Office, 1884). Public-domain government
  compilation and nineteenth-century reports. Internet Archive scans identify
  the edition used. OCR excerpts, selected manual transcriptions, and page renders
  are identified in the source registry; editorial labels are not original prose.
- Manning Ferguson Force, *From Fort Henry to Corinth* (1881), public-domain
  historical text obtained from [Project Gutenberg ebook 24438](https://www.gutenberg.org/ebooks/24438).
  Only preface and strength-discussion excerpts are included; no modern foreword,
  illustrations or full ebook are redistributed.
- LTC Jeffrey J. Gudmens and the Staff Ride Team, *Staff Ride Handbook for the
  Battle of Shiloh, 6–7 April 1862*, Combat Studies Institute Press, Fort Leavenworth,
  DTIC ADA445681. Report date 2004; library catalog data uses 2005. Selected U.S.
  Army government-authored narrative and one table heading are included. Photos,
  maps, logos and modern third-party vignettes are omitted.

Original download links, parent hashes, page mappings, transformations and account
dependencies are preserved in `data/sources.json`. None of these authors,
institutions, or archive hosts endorses Generalship's interpretations.
