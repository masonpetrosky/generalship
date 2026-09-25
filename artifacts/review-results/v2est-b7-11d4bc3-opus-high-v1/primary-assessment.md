# Primary assessment: Strength ledger v2, batch 7 of 8

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`. Its
SHA-256 is `529df35e737451413090b5b818b8dcd99a8cf97ec8f482a9b72220095d46ce0e`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `fe948a6e949e8d7b0fff25479bc9e64263ef8647`; see [dispatch.json](dispatch.json).

Each required finding was checked against the cited passage before it was applied, through the
batch builder; the rebuilt ledger replays under its checker. [correction.json](correction.json)
binds the corrected ledger files.

## Required findings

- **F1** (accepted applied): Checked or39-1-corse-allatoona-selections-v1 pp.760, 762-763. The Oct 7 1,500 is 'about 900 muskets' plus Tourtellotte's 'about 600' (infantry muskets only). The Oct 27 1,944 is garrison infantry 450+290+150=890 (the Twelfth Wisconsin Battery is listed with 6 guns and no men) plus the infantry detachment's 1,054. Both inputs are now coded [partial_scope] with bound 'lower' (class bound), the notes are the reviewer's text, and the rationale is replaced. One addition to the 1,944 note: the detachment's listed companies (280+207+267+61+155) sum to 970 in the OCR, not the printed 1,054. GA023 US stays A/1940. Low moves from 1430 to 1850, high stays 2040, the single_input label is added, range_groups become [us-cw], and the nested sets are unchanged. This matches the reviewer's replay.
- **F2** (accepted applied): Checked or39-1-burbridge-saltville-selections-v1 p.552. The Oct 7 figure is 'From prisoners I learn ... between G,0()0 and 8,000 ... Breckinridge was present with 4,000'. The Oct 10 dispatch gives 'from 0,000 to 10,000' with no source, so it is Burbridge's own estimate. 'it is said' belongs to the list of commanders. The VA076 Confederate null_reason and the cs-burbridge-breck note are replaced with the reviewer's text. Codes and grade D are unchanged.

## Advisories

- **A1** (primary decision): Text applied, basis and scope not changed. Checked or45-1-hood-tennessee-selections-v2 p.663. The table header reads 'Present. [Present] and absent. Effective. Total. Aggregate. Total. Aggregate.' The first column sums exactly: 25,889+2,306+2,405=30,600 and 18,342+2,306+2,405=23,053. The TN034 inventory line and the TN038 cs-hood-23053 note now say the arithmetic supports the effective column, while leaving basis and scope unresolved. Primary decision, once for both inputs: (a) basis 'reported_effective' for cs-hood-30600 and cs-hood-23053; replayed, this moves the TN034 CS point from 35,000 to 30,600 and the TN038 CS low from 21,900 to 22,050. (b) Whether the 2,306 cavalry line excludes Forrest (Cox: 9,209 joined about Nov 15), which would add partial_scope to cs-hood-30600; replayed, the TN034 CS low moves from 21,420 to 24,500 and single_input is added. The indorsement ties the 30,600 to 'Crossed Tennessee, November 21', after Forrest joined, so scope stays open.
- **A2** (not adopted): The reviewer itself leaves it as scope_unresolved. Price's short account does not show whether his 3 p.m. 3,000 excludes Sanborn's brigade, which arrived before sundown. MO029 US stays C/2,250.
- **A3** (accepted applied): VA122 CS cs-lv-total now has codes [post_engagement_state, derived_from_losses]. Livermore p.130 adds the October 19 loss (2,911) to reach 'Total engaged 18,410', which is visible derivation from losses (tier-2 §3 item 5). The input stays class C and nothing changes numerically; the VA122 CS point stays 15,270.
- **A4** (accepted applied): MO026 US null_reason reworded. It now calls Price's 6,000-8,000 an opponent estimate of a different scope (the whole Big Blue line after Curtis joined, without Pleasonton's division), not the force at Byram's Ford, and it no longer calls the figure 'a lower bound'. The input's coding and grade D are unchanged.

This AI review is a separate analysis, not historical adjudication, feature admission or
authorization of any fit. The ledger rates nobody and changes no model input.
