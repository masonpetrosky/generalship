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

`data/raw/shiloh/` contains selected historical text, rendered pages, maps and
catalog snapshots. These retain their source attribution and are not relicensed as code.

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
- D. W. Reed, *The Battle of Shiloh and the Organizations Engaged*, revised 1909,
  Shiloh National Military Park Commission, Government Printing Office.
  Public-domain historical compilation; selected transcriptions and facsimiles
  retain their report dependencies and reconstruction limits.
- Library of Congress, Geography and Map Division: *Map of the field of Shiloh.
  April 6 [1862]*, attributed to the US Army Department of the Tennessee,
  [item 2006636339](https://www.loc.gov/item/2006636339/); and Léon Joseph Frémaux,
  *Map of the battle field of Shiloh, April 6 & 7, 1862*, endorsed by G. T.
  Beauregard, [item 85690890](https://www.loc.gov/item/85690890/).
  Public-domain nineteenth-century maps. The full-resolution JPEG responses and
  catalog JSON responses are preserved verbatim; separately identified selected
  label transcriptions and interpretations are Generalship's work. Catalog dates
  do not establish when maps were available to historical commanders.

- Robert W. Medkirk, letter dated March 22, 1886, printed in Robert Underwood
  Johnson and Clarence Clough Buel, eds., *Battles and Leaders of the Civil War*,
  volume I (The Century Co., copyright 1887), p.537. Public-domain selected text
  and page facsimiles; editorial framing is distinguished from the letter.
- Thomas Worthington, *Shiloh; or, the Tennessee Campaign of 1862* (1872), and
  *Abstract of Evidence* (printing date not established). Public-domain selected
  pages/text; quotations from testimony are presented as his published selections,
  not an authenticated official trial record.
- D. W. Reed, commission edition marked 1902, GPO imprint 1903, selected pages.
  Same compiler lineage as the already retained revised 1909 edition.
- NPS, Hardee Third Corps plaque O webpage, and NARA, RG79/RG92 archival guides,
  HTML snapshots retrieved September 20, 2026. Selected government-authored text
  retained separately from template markup; linked media are not downloaded.

- Whitelaw Reid, *Ohio in the War*, volume II (Moore, Wilstach & Baldwin, 1868),
  selected 46th/72d Ohio passages and whole-page facsimiles. Public-domain history;
  the contributors behind the particular narratives remain unestablished.
- John M. Lemmon, speech delivered at the 72d Ohio reunion, June 17, 1875,
  selected pp.5–7 and printed heading. Public-domain speech; printing date not
  independently established from the retained pages.
- Thomas Worthington, composite volume headed *Brief History of the 46th Ohio
  Volunteers*, with appended *Facts Developed* allegations (printing date unknown)
  and a separate *Flank March* title bearing 1880. Selected public-domain pages;
  bound works and event/publication dates are not conflated.
- D. C. Buell, revised map and caption in *Battles and Leaders* I, pp.502–503,
  caption dated June 1885 with a later edition note. Public-domain facsimiles and
  selected labels/caption; explicit map/report dependencies are retained.

Original download links, parent hashes, page mappings, transformations and account
dependencies are preserved in `data/sources.json`. None of these authors,
institutions, or archive hosts endorses Generalship's interpretations.
