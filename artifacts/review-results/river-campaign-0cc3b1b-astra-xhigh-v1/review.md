# Bounded river-campaign separate AI review

## Identity, inputs and decision

- Reviewer task: `/root/river_campaign_review`.
- Model: `gpt-6-astra`; reasoning effort: `xhigh`; fresh context.
- Review date: 2026-09-20.
- Prepared commit: `0cc3b1b442a1c7651ab6ddd6889dbed9019e6a6a`.
- Preservation comparison: `62c66db0c4ba2513e38d59670fbfbfdd80a74887`.
- Assignment: `assignment.md`, SHA-256 `ca579d33d09f0e7528e302dae2be2218d2ef4cad5f634f9455bdc99bfca4c18a`.
- Input manifest: `inputs.json`, SHA-256 `98cd24282ac712a8f9f63cce3927bac9e047f43eb28d9eebb3e9e6cf71e1f761`.

**Decision: accept the bounded first-pass extraction and preservation work with no required corrections.** All 33 new claims were inspected, including their rationales, citations and explicit unknowns. No unsupported historical assertion, material extraction error, silent population/timing substitution, automatic commander attribution or feature admission was found within this assignment. The three new dossiers remain drafts. This review is separate AI analysis, not human historical adjudication or proof of source independence.

All 23 manifest hashes matched both the prepared commit blobs and the working files at inspection. The exact input hashes are reproduced at the end of this review. The review concerns the prepared commit; subsequent primary finalization is outside this decision.

## Actual inspection scope

Read `AGENTS.md`, `README.md`, `docs/methodology.md`, `docs/roadmap.md`, `docs/evidence-contract.md`, `docs/sources.md`, the assignment and manifest, and `docs/research/river-campaign-first-pass-v1.md`. Read all claims and open questions in the three new dossiers and the generated pilot report. Inspected the prepared change to the report generator and dossier inventory test.

| Dossier | Claims inspected | Supported / disputed / unknown | Citation occurrences | Dimensions |
| --- | ---: | --- | ---: | --- |
| TN001 | 10/10 | 8 / 1 / 1 | 17 | All seven |
| TN002 | 11/11 | 9 / 1 / 1 | 22 | All seven |
| MS016 | 12/12 | 8 / 2 / 2 | 23 | All seven |
| Total | 33/33 | 25 / 4 / 4 | 62 | All seven in each draft |

The 62 citations comprise 43 Grant-text occurrences, 13 NPS-text occurrences and six exact CSV-cell occurrences. These resolve to 38 distinct source/locator anchors: 22 Grant sections, ten NPS field locators and six battle-row cells. All four null claims and all nine open questions were inspected for consistency with the retained evidence and stopping rule.

Read all **24 complete retained Grant paragraphs**, including both uncited context paragraphs (rows 419 and 444), and all three complete retained NPS summaries (21 nonempty extracted text nodes each). Grant rows inspected were:

- Chapter XXI: 392, 396, 397, 399, 400, 401.
- Chapter XXII: 408, 412, 416, 417, 419, 423, 425, 442, 444, 445.
- Chapter XXVI: 542, 544, 545, 547, 548, 549, 553, 555.

Independently replayed the documented HTMLParser transformations against the retained HTML. All 24 Grant paragraphs matched exactly after character-reference decoding and whitespace collapse, and their chapter headings matched. All three NPS plaintext files matched the documented script/style exclusion, text-node stripping and Return-to-Results/Experience-More bounds, including their final newline. The replay is a check against the retained digital parent, not a printed-edition transcription audit.

Also read the complete pinned Arnold battle rows for TN001, TN002 and MS016, and VA100 for next-campaign verification. Inspected all eight new registry records, their raw-file hashes and four parent links, plus the Grant digital title/header and the relevant NPS HTML fields. All new evidence inspection was **digital text/HTML/CSV only: zero facsimiles, maps or source images inspected**. The whole Grant HTML was parsed to replay row indexing; the whole book was not historically reviewed. The only two source families used by each new dossier are `nps-cwsac` and `or-grant`; copies, formats and chapters add no witnesses.

## Claim-level assessment

No required correction applies to any of the following inspected claims.

**TN001.** `zero-sentinel`, `recorded-result` and `opening-populations-unknown` retain the distinction between populated historical narratives, defective live strength fields and unresolved opening membership. `expedition-proposal` and `garrison-and-rearguard` correctly distinguish a proposed 17,000-person expedition, approximately 2,800 people in the fort/camp and roughly 100 retained at the guns. Rows 396, 399 and 401 support the attributed statements without supplying one opening census. `flooded-position`, `transport-and-approach` and `landing-reconnaissance` accurately summarize the cited passages; the Essex sequence retains the change of landing decision after rifled-gun fire. `river-access-objective` remains Grant's retrospective strategic rationale. `joint-operation` distinguishes the army plan, naval action and Tilghman's decisions; it does not distribute the outcome to every listed commander. Tilghman's report mentioned by Grant is correctly marked uninspected.

**TN002.** `zero-sentinel`, `recorded-result` and `opening-populations-unknown` preserve source defects and missing matched populations. `marching-and-late-forces` keeps the 15,000-person marching force separate from the 27,000 at the fall, including supply-road guards; row 445 also retains the later-arriving reinforcements in context. `surrender-estimates` properly distinguishes NPS's 12,000 from Grant's secondhand recollection of Buckner's uncertain 12,000–15,000. Context row 444 supports the warning that Grant's 21,000 reconstruction draws on prisoners, casualties and escapes and is not an opening return. `defensive-ground`, `winter-exposure`, `escape-inference`, `nashville-objective`, `army-navy-plan` and `confederate-command-transfer` are supported as attributed descriptions, recollections or plans. The draft does not adopt the adjoining morale judgments, certain-victory claims or judgments of character. The February 14 naval withdrawal is consistent with its chapter and retained surrounding date context; no exact Confederate command-transfer clock is invented.

**MS016.** `zero-sentinel`, `opening-populations-unknown` and `halleck-information-unknown` preserve the necessary unknowns. `may-force-perspectives` correctly separates Grant's retrospective effective-force estimate (probably not much over 50,000), his reported Union-side enemy estimate (70,000) and a rounded Union total (120,000); no date precision, same-population interval or Union population basis is invented. `wooded-ridge` and `roads-bridges-and-works` follow the retained terrain/preparation passages without importing their evaluative judgments as scored advantages. `recalled-evacuation-warning` retains the uncertain “probably” May 28 timing and does not infer Halleck's receipt. `rail-center-objective` is the NPS operational target, not a recovered directive or numerical utility. `command-and-authority` accurately separates Grant's formal position from his claimed practical exclusion. `evacuation-and-occupation` and `recorded-result` preserve attributed withdrawal, occupation and source outcome labels. `operation-window-and-result-text` reproduces both pinned dates and the unexplained raid wording, distinguishes the live campaign-like date field, and treats the June 10 pursuit connection as a possibility rather than the proven basis for the table's end date.

## Metadata, preservation and coverage

The new metadata identifies Grant's retrospective participant role and the shared `or-grant` dependence group; all 24 historical section dates remain null. The July 1, 1885 preface date is not assigned to the chapters. NPS retrieval dates, displayed campaign dates and unknown composition/publication dates remain separate. The source families' bookkeeping does not establish historical independence. No original report named within Grant's text or failed retrieval lead is represented as separately inspected.

Compared every previous registry record with its prepared-commit counterpart: **176/176 entries are unchanged**. Compared every previous distinct registered raw path across the previous commit, prepared commit and working copy: **173/173 raw files are byte-identical**, and their SHA-256 values match the registry. All 184 current registered source hashes were also checked. The addition is exactly eight entries/eight raw paths, producing **184 entries / 181 distinct raw paths**.

Verified byte identity across the same two commits and working files for the Shiloh dossier, frozen cohort, both admission proposals and baseline. Shiloh's 62 claims were **not re-reviewed**; this assignment establishes preservation only. Earlier raw materials were hash-checked, not reread or historically reconsidered.

Recomputed coverage from the frozen IDs and pinned campaign column: **127 engagements / 36 groups; six dossiers; 121 engagements without dossiers; one complete group by dossier presence**, with members TN001, TN002, TN003 and MS016. These counts do not claim comparable research depth or completed review of all four dossiers in this run. Sorting remaining complete source groups by earliest engagement date and then label yields **Blockade of the Potomac River, VA100, January 3, 1862** next, as the roadmap states.

The memo's casualty-field comparisons match the inspected rows and summaries: Henry 146 versus 119, Donelson 19,832 versus 17,398, Corinth 2,000 versus unknown. They are source discrepancies, not reconciled casualty estimates. The zero-strength and rank/date inconsistencies remain visible. There is no silent replacement of the frozen Corinth row or substitution of October Corinth.

The report retains **23/127 baseline-eligible engagements across 13 groups**, Brier **0.276882 versus 0.250000** for equal odds, 18 blocked / 22 excluded admission candidates and **zero promoted rows**. The disappointing baseline is unchanged. The report-generator change only updates research-priority prose; the test change adds the three new IDs while retaining resolvable-passage and draft-status checks. No new runtime dependency or model job is introduced.

## Offline checks and remaining limits

Commands/checks run:

1. `git show` / `git diff` for the exact prepared and previous commits; `git status --short --branch` for the shared checkout.
2. Read-only Python standard-library SHA-256, JSON and Git-blob comparisons for all 23 manifest entries, all current registered source hashes, prior-entry/raw preservation and the five protected inputs.
3. Independent read-only HTMLParser extraction replay for 24 Grant sections and all three NPS text snapshots; CSV/JSON recomputation of source-family, claim, citation and campaign coverage counts.
4. `PYTHONDONTWRITEBYTECODE=1 make check`: **82 tests passed**; the pipeline/source/evidence/admission check passed and reported `artifacts_written: false`. The tests include offline reproducibility and receipt checks. No `make reproduce` or packet-writing command was run by this reviewer.

Remaining limits are the documented historical ones: unmatched opening boundaries/populations; uninspected original reports, separately authored scholarship and print facsimiles; Grant's interested hindsight and secondhand statements; uncertain contemporary information and command-transfer timing; live/pinned field conflicts; and Corinth's unresolved operation grain. The reported unsuccessful retrievals were not retried or independently reproduced. No browsing, new research, primary evidence edits, commits or additional agents were used. Nothing in this review admits a feature or warrants a causal performance claim.

## Verified input hashes

Each entry below matched the prepared commit and the inspected working file.

| Input | SHA-256 |
| --- | --- |
| `data/sources.json` | `eb98b53996d0132e3a6309ca5b2709b26d60a08509676b3dc1970831665daad9` |
| `data/evidence/TN001.json` | `c388b057ec17936f2265c052f9536679c0721248c88b77dc8fca627d5b2bd7e0` |
| `data/evidence/TN002.json` | `4b8100e70db24c51cc4a8c31b341d9fb0764d25c20528d3b8be568e018fabc05` |
| `data/evidence/MS016.json` | `d5e4f027c91abc96ee3f454ee7c33d6479e0ad09bcb97753ee60498932eeb78e` |
| `data/evidence/TN003.json` | `fb622c81b48110d1d7b25212b5c3f10881c4a7724a9ccbb93ef793816cf100ee` |
| `data/pilot/cohort.json` | `17d08348ed1399a0f0033ded3b1ba40c541d342b6aeed920cf2c26818ee6adc8` |
| `data/admission/shiloh-opening-v1.json` | `a4eca5a91e8c93baa2243a314e8d8e76c754d44ef42d7926435847efe849f5b6` |
| `data/admission/shiloh-opening-v2.json` | `20709e0fd46e53906aa9a89c55883fa684a3213e233177b6e6b0d3cac89c5e52` |
| `artifacts/baseline.json` | `592b62bef69b4f76a626fa7c06f17f8813b02bcf4c6753601d4ad2b413e09595` |
| `docs/research/river-campaign-first-pass-v1.md` | `3a5ea8c829380fece89dea092c69bfdaae3250a0b8d2f173a531cd9e0f7e3b88` |
| `docs/sources.md` | `82ce19371de304d474b482c06194716783b7b5f2d7912999d832e3e48b42153f` |
| `docs/roadmap.md` | `e9fa850ddb8e32bb8585bb73a3014b6e8849ac79889ca685cbe91e78b8837489` |
| `README.md` | `de6c54c4622419800a331b99d35e623ffe13f95df628c98a41306ef752e2133d` |
| `generalship/cli.py` | `052463d1d8d2767aa3be55b99a1aec81d863e513b848765e63139c080af10712` |
| `tests/test_evidence.py` | `db7e450de07489b207016a2d129b0508b6ac056950fcd50aa420ae29dec10fc9` |
| `data/raw/river-campaign-v1/grant-memoirs-gutenberg-4367.html` | `4eff08719acba1714238f297908fb1326747e2b01c12d81b572f26567271b850` |
| `data/raw/river-campaign-v1/grant-memoirs-selections.txt` | `c63afe5027ba3e302f8ece36777abeccb226b3eeeacffaa6d5ea264fdba7dc6c` |
| `data/raw/river-campaign-v1/ms016-nps.html` | `fe9276a9d2126321761933321e9a5f860dab37bd8fc7e95ff9067e9401eb46e6` |
| `data/raw/river-campaign-v1/ms016-nps.txt` | `235360db899697a8b75c7eac4a4de3a8217a6a3940ab90fe9c96f748e2fae760` |
| `data/raw/river-campaign-v1/tn001-nps.html` | `57529e87dbfbea642d1a42abf8a40d268511ffaa893572c01a4fc2f288b1c4be` |
| `data/raw/river-campaign-v1/tn001-nps.txt` | `b33016ca730a085c43ee2cdce24073bca91fdb505dc7a13a819053fff007e502` |
| `data/raw/river-campaign-v1/tn002-nps.html` | `ffe3a3fe1b96788ec0b35625f90311bd6fe96d97df8d807e78eea90eb2ec7f8d` |
| `data/raw/river-campaign-v1/tn002-nps.txt` | `959c0dfb0814880e9547ba0d4a03b8dec64723074eafbbe85f3b8915e906610d` |
