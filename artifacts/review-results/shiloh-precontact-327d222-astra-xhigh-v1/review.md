# Separate AI review: Shiloh precontact segmentation v1

**Decision: changes requested for one literal-transcription finding containing two lexical corrections.** The conditional April 3–4 precursor recommendation is acceptable as research guidance with its stated limits. This review does not approve a complete opening boundary, adjudicate historical truth, or admit any feature.

Reviewer: `/root/shiloh_precontact_review`, GPT-6 Astra, `xhigh`, fresh context (`fork_turns: none`), 2026-09-20. Prepared commit: `327d222195b5526423390c25f59b8330a21e88c0`. The actual response is this file and [review-result.json](review-result.json).

## Required finding PS-R1: correct Jordan's April 4 order

The selected text in `or-april4-march-orders-v1`, section `p391-jordan-revision`, and the corresponding PS05 anchor contain two lexical discrepancies. On **OR Series I, volume X, part 2, printed p.391**, the lower Jordan-to-Polk document dated Monterey, April 4, 1862, visibly prints:

- **“to the support of the movement”**, where the excerpt says **“in support of the movement”**.
- **“Major-Generals Hardee and Bragg”**, where the excerpt says **“Generals Hardee and Bragg”**.

These are outside the declared whitespace, line-wrap, apostrophe and heading-dash normalization. Exact-quote validation passes because the source excerpt and anchor share the same mistakes.

Affected source raw SHA-256: `fd66fc18e82492c35eb208733d781553e568dc1dd7f2e577c4da366d6b5c53b5`. Source metadata SHA-256: `97f36798f8bdbc1de97f0ead960e99db71b68297c4705020b90984e1a24db43d`. Evidence image: `or10-2-precontact-p391-facsimile-v1`, raw SHA-256 `deaeba57026d32a63e228b3637ad0ded0f4946a10eca3711a5edd861f7bda135`, parent PDF SHA-256 `a52c65ca6fd0debeb8ab5c409bf09091f0478a3a2a3f9732f183f30502cbc955`.

Replace the selected paragraph/anchor, in a **versioned corrected successor**, with:

> The commanding general directs me to say, on reflection, he wishes you to march promptly with your command at 3 o'clock in the morning to the support of the movement ordered to be made at that hour by Major-Generals Hardee and Bragg. It is of the utmost importance for the success of this movement that your troops shall move precisely at the time designated.

Preserve the v1 source, prepared machine record and review inputs. Bind the correction to a new immutable source ID and a versioned correction record; do not silently rewrite the old evidence. Both changes are required for literal fidelity. Neither changes the supported distinction between an order, an acknowledgment, and actual execution, nor the bounded precursor recommendation.

Discovery record: the reviewer identified the missing “Major-” during its image inspection. The primary subsequently flagged the support-phrase discrepancy from its parallel inspection. The reviewer reopened the registered p.391 image and confirmed both printed readings directly. That communication is recorded rather than presenting the second discovery as an uninfluenced first-pass finding.

## Coverage and assertion assessment

Reviewed **10/10 assertions, 24/24 anchors, all 26 selected historical sections in 9/9 new text sources**, and the existing Reed p.68 anchor. Direct `view_image` inspection covered **19/19 registered pages: 18 OR pages and one Reed page**, including all 15 new images and four reused images. Relevant date headings, signatures and nearby context were inspected. One of 24 anchors and one of nine new text files has the two discrepancies above. No additional discrepancy was identified within the declared normalization.

This was selected-passage review, not a character-by-character audit of every page, an exhaustive volume review, or an extraction-error-rate estimate. The full older Reed transcription was not re-reviewed; only its cited p.68 selection and nearby context were.

| Assertion | Anchors | Result | Actual inspection |
|---|---:|---|---|
| PS01 | 2 | No required correction | April 3 headings, Chalmers signature, Craft signature and selected wording verified on OR I.X.2 pp.387-388. Clanton's report is verbal and provisional; feared captures and incoming information are not confirmed observations or independent witnesses. |
| PS02 | 1 | No required correction | Grant's April 5 dateline and 'yesterday and day before' verified on OR I.X.2 p.94. This supports attributed April 3-4 skirmishing without identifying it with Chalmers/Craft incidents. |
| PS03 | 3 | No required correction | Sherman's April 5 heading on p.89 and return-after-night selection on p.90, Buckland's April 5 heading on p.90 and return selection on p.91, and Ricker's uncertain April 4 [?] heading and retirement on p.92 verified. Shared chain and lack of proof every outpost ceased firing remain explicit. |
| PS04 | 1 | No required correction | April 4 dateline and Clanton retirement/repulse verified on OR I.X.1 p.93. Opposing descriptions are retained as attributed reports, without exact location or casualty admission. |
| PS05 | 4 | PS-R1 required | All four selected passages and April 4 datelines inspected on OR I.X.2 pp.390-392. Johnston staging, Bragg delay, later Jordan order and Polk receipt are distinguished. Two lexical differences occur in the later Jordan paragraph. Earlier Jordan reserve order is a separate same-page document; 3 a.m. execution remains unproven. |
| PS06 | 4 | No required correction | Hardee's February 7, 1863 dateline on p.566, three sequence passages on p.567 and lapse-of-time caveat on p.571 verified. The caveat belongs to the report ending before the separate October 29, 1862 documents on p.571. |
| PS07 | 3 | No required correction | Wood's April 15 heading on p.590, brigade-specific Saturday and Sunday passages on p.591, and Hardee's Sunday passage on p.568 verified. No-advance is not no-contact; Sunday screen contact is retained before brigade/main advance; rival clocks are not adjudicated. |
| PS08 | 2 | No required correction | Sherman's two April 5 documents across OR I.X.2 pp.93-94 verified, including the Not found footnote on the prior Grant note. Quiet-now and attack expectation remain local statements and belief, not evidence of no Howell encounter. |
| PS09 | 3 | No required correction | Compiler headings on OR I.X.1 pp.89 and 93 and Ricker's opening-fight language on p.92 verified. Editorial dates are not composition/knowledge dates; broader participant framing remains visible. |
| PS10 | 1 | No required correction | Reed p.68 visibly reports another engagement near Howell's on Saturday. The paragraph also narrates Friday and Sunday contacts; that juxtaposition does not establish continuity or an inspected underlying participant source. No 4:55 clock is adopted. |

The dateline controls are appropriate: Chalmers/Craft are April 3, the approach correspondence and Hardee letter April 4, Sherman/Buckland/Grant April 5, Wood April 15, and Hardee's long report **February 7, 1863**. Ricker's printed **April 4, [?] 1862** remains uncertain/null. The separate October 29, 1862 documents later on p.571 do not date Hardee's preceding lapse-of-time caveat. Compiler headings and Reed's 1909 publication are not historical knowledge timestamps. Keeping all `historical_knowledge_at` values null is appropriate: Polk's acknowledgment establishes receipt as a source assertion without establishing an exact intraday knowledge time.

## Nonblocking assessment and retained limits

**PS-N1 — Continuity rule.** The written rule does not make overnight rest, a date change, an order, quiet claims, or a compiler's heading decisive. April 4 has positive return/retirement evidence from Sherman, Buckland and Ricker, alongside reported Confederate retirement/repulse and later renewed movement. The packet uses these as a provisional episode distinction, does not split April 6 from April 7 merely for overnight rest, and retains screen action before the main advance. That is defensible research framing. It is not proof that every outpost ceased hostile contact. No wording change is required for the current bounded use.

**PS-N2 — April 3.** Both the memo and machine record expressly state that April 3 has weaker event-specific closure, possible overlapping incidents, and no separately reconstructed ending for each contact. The inference rests on the later reported return/reset sequence. Those qualifications are adequate for a **working, non-admitting recommendation**, not for a completed boundary gate. Carry the same limitation forward if the recommendation is summarized. No new historical conclusion or replacement wording is requested.

**PS-N3 — Howell and dependence.** Reed's p.68 reports the Saturday Howell encounter, but its juxtaposition with Friday and Sunday does not prove continuity. Wood's brigade-specific no-advance statement and Sherman's quiet-now/expectation do not establish that no Saturday contact occurred elsewhere. The packet correctly keeps Howell unresolved and labels negative OCR searches as leads, not evidence of absence. The review did not repeat those searches or inspect park commission/tablet archives.

Chalmers/Clanton/Craft, Sherman/Buckland/Ricker, and the Confederate command reports/orders remain dependent reporting environments. Hardee's 1863 narrative is retrospective and explicitly warns about accuracy after delay. Additional scans or transcription files are not additional witnesses. The mixed Sherman/Grant source has section-level reporting groups; those labels do not certify historical independence. No morale/readiness value, causal attribution, additional battle row, commander credit or combined battle/campaign score is created.

## Provenance and preservation verification

All five dispatch-bound files match both the working tree and the prepared commit:

| Input | SHA-256 |
|---|---|
| `data/sources.json` | `1b73c52f95dc8308b5ad3d3a9fef8759aaf7ac61286ea4ef2a4fd5ea881f9fd4` |
| `data/evidence/TN003.json` | `fb622c81b48110d1d7b25212b5c3f10881c4a7724a9ccbb93ef793816cf100ee` |
| `design/shiloh-precontact-segmentation-v1/research-record.json` | `c654c55d678692590d5ac2223e92f8b110f9dafc05c0b9c8f6ac75da0f65cafe` |
| `design/shiloh-precontact-segmentation-v1/reference-audit.py` | `f24a677dbf3725af460e0acd1a3cdcabdb49714fb066e3e1c79f726d2f9014bd` |
| `docs/research/shiloh-precontact-segmentation-v1.md` | `14b4ff5ea9704254deba46ba1d785dc017871b11c8cc6e5d5eae7b81f2623dc7` |

Dispatch SHA-256: `edb8b9bb4bfc7062122a8cefb0dea357bfbf5b729219f99251bb2d8ea276904b`.

Independently of the primary's parallel checks, I compared the prior registry at `10ba606b66e8433e248f52f39c5821e94b886680` with the prepared inputs: **87/87 complete metadata records and 84/84 distinct raw paths are unchanged**. All **72/72 preserved-file bindings** match the base commit, prepared commit and working tree. This includes the frozen dossier, cohort, admission proposals, earlier evidence/review artifacts and baseline bindings. All 19 inspected image hashes were rechecked. The registry contains **111 entries / 108 raw paths**, adding nine text records and 15 images. No tracked worktree difference was present at check time.

The dossier remains **62 claims / 40 quantities / 26 events**. The frame remains **127 engagements / 36 campaigns**, with three draft dossiers. Admission v1 remains **18 blocked / 22 excluded** and v2 **7 blocked / 33 excluded**. Both have zero complete candidate rows. The baseline remains **23 engagements / 13 groups**, with Brier **0.2768816348133779**, worse than equal odds **0.25**. No predictive improvement was demonstrated.

## Offline commands

Python **3.14.7** was used. All commands exited 0:

- `PYTHONDONTWRITEBYTECODE=1 make check`: **82 tests passed**; source/evidence/pipeline check passed; `artifacts_written=false`.
- `python3 design/shiloh-precontact-segmentation-v1/reference-audit.py`: passed all bound counts, hashes, dates, passage presence, preservation and zero-promotion checks.
- `python3 design/shiloh-contact-location-v1/reference-audit.py`: passed the preceding packet's mechanical provenance/admission checks.
- `python3 design/shiloh-contact-location-corrections-v1/reference-audit.py`: passed both earlier corrections and 38 earlier anchor replays.
- Reviewer inline Python/Git comparison: passed the independent 87-record / 84-path / 72-file preservation comparison and all 19 inspected-image hash checks.

The actual command output is preserved in `review-result.json`. Audits establish mechanical integrity, not literal source fidelity or entailment; PS-R1 illustrates the distinction.

I did not run repository-root `make reproduce` or `make packet`, which write outside the assigned review outputs. The offline reproduction test did run in `make check`. The primary's exact-commit artifact replay and historical `330599b` boundary-audit results are separate evidence and are not claimed here as reviewer executions.

## Inspected source bindings

New text raw hashes (full metadata and section dates are in `review-result.json`):

| Source ID | Raw SHA-256 |
|---|---|
| `or-chalmers-craft-precontact-v1` | `f41f7f36a33b529ee7f7589659bccda062830f029cdd35b05ccaf41c4b5e5fba` |
| `or-sherman-april4-return-v1` | `3954b361f1a0593d15938048cf57ad613bae6a6816e6c32a7443818e580b0b77` |
| `or-buckland-ricker-return-v1` | `adba8a2237f87350b91b97316e92187fcdca18fefe840bf91df849117dedce33` |
| `or-hardee-april4-contact-v1` | `4454df47ff916345bc65a646c3c35e1ff2ee1d58a16048733364ef4b18106dfe` |
| `or-april4-march-orders-v1` | `fd66fc18e82492c35eb208733d781553e568dc1dd7f2e577c4da366d6b5c53b5` |
| `or-april5-precontact-dispatches-v1` | `018879c39dd271f76c70851802d0ffc28f7e90ef78895c2fed1ffb45f3f62ca5` |
| `or-hardee-1863-precontact-v1` | `2edbe1e769caf3898612340fac64cc96506c3967feb25d85a210b4028c2e1574` |
| `or-wood-precontact-v1` | `a403f4b3923f840be7b2fc173b7cd7d6f3d67567be78af2acde6bdf753b531d4` |
| `or-precontact-editorial-headings-v1` | `1998aedbe481367dbe66fa8caede3efb3ecc301db987f9279aa039049f89a05f` |

The additional inspected anchor is `reed-1909-opening-v1` / `p68-screen`, raw SHA-256 `e9e5c93d244e790b79f88f305059ce503acaf5bcb6bc4257f91a3bf5469112f6`.

All directly inspected page images:

| Source ID | Raw SHA-256 |
|---|---|
| `or10-1-precontact-p89-facsimile-v1` | `180e459efffd626c61125772eb0604142bc0fdbc66371d96a6f21c136e13e0a2` |
| `or10-1-precontact-p93-facsimile-v1` | `3cdc23a0d8b9c0be0570758c2951636549833bd7f9df61a93f3ec4161e4c477f` |
| `or10-1-precontact-p566-facsimile-v1` | `bf8288a2c8f162e837618c9303b99ad12ef967954005cde6446889d6b84bb168` |
| `or10-1-precontact-p567-facsimile-v1` | `226e5ea908f48ee9465063e4d37380e001969b50b22ac8cf069d3550de3865df` |
| `or10-1-precontact-p568-facsimile-v1` | `8efe8fd3b283b05ea2b5008de72074590226e14c92c6e2de58ab9fc0750dff11` |
| `or10-1-precontact-p571-facsimile-v1` | `9be6630283c532cfc932299255b0fa9d403dbebd4222f7c80533e6e28c98f1ac` |
| `or10-1-precontact-p590-facsimile-v1` | `b3b9cc0f7253a060b33105d28a40012bd8e2ac04a2b34891c0bbf953ce0b394c` |
| `or10-1-precontact-p591-facsimile-v1` | `31cf1d8330b2f1b38d69039b4cdee46b422c7cd670a535feb4c3b53ee1a37485` |
| `or10-2-precontact-p93-facsimile-v1` | `eca1f96ecee69a9bcbd7c59012cc19ce536685096378e14cb3078b191a85f0be` |
| `or10-2-precontact-p94-facsimile-v1` | `6fb160ccc45d5663f7664182a896eca4b84f2bcfe58be991e61692fa2ba77cf8` |
| `or10-2-precontact-p387-facsimile-v1` | `ef42bbec7dc5ea3a51dd230a657511666304b531e7d7b05f4cd68f73aed6aa96` |
| `or10-2-precontact-p388-facsimile-v1` | `e0020a00f8e2f80c2f54bdb673d3863a73453b124b89ff76f52bf75e1c95216a` |
| `or10-2-precontact-p390-facsimile-v1` | `c4082975795747575ee5bd04a6f06014b125c0034b8d887f888e74428a3ecd39` |
| `or10-2-precontact-p391-facsimile-v1` | `deaeba57026d32a63e228b3637ad0ded0f4946a10eca3711a5edd861f7bda135` |
| `or10-2-precontact-p392-facsimile-v1` | `36c1db00197153745d1b12f85573b45e4b2ee7256a91502ac584efa755174418` |
| `or10-1-contact-p90-facsimile-v1` | `c31e3efffc7a10181f128d57ab7801047380336bfe86875aa28f72657bc6bef3` |
| `or10-1-contact-p91-facsimile-v1` | `e81eaeca4d692ee577bf5b81e75e1d978428045a7f171ff934df1340e7699838` |
| `or10-1-contact-p92-facsimile-v1` | `ba2d04a7fbfcc9676354847130874be30dc1b27b31fc0a473fb51708681e8ca6` |
| `reed-1909-contact-p68-facsimile-v1` | `bc33498cd910b2b01e20b03a0bc9735b1d305448259cace5fc282b0c153fe087` |

## Unresolved outcome

PS-R1 remains open at the reviewed commit. A source-bound correction can close its two literal errors without altering the historical recommendation. Howell's underlying testimony and contact link, April 3 event-specific endings, April 6 first contact/clock, mapped area, ford guards, transport/afloat rule, and both complete populations remain unresolved.

**Historical features admitted: 0. Emitted rows: 0. Promoted rows: 0.** No evidence or implementation file was modified; only the assigned review outputs were written. This is separate AI analysis, not human historical adjudication or proof of independent reporting. A faithfully transcribed, source-backed claim can still be historically wrong.

