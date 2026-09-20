# Separate AI review: Reid provenance packet

**Verdict: accepted within the inspected scope, with two nonblocking catalog precision comments.** No required correction to the five bounded assertions, no literal transcription error in the seven compared sections, and no feature admission. The original contributor, original statement, post identity and Saturday-to-Sunday continuity remain unknown.

This is the actual review response of task `/root/shiloh_reid_review`, run as `gpt-6-astra` with `xhigh` reasoning and fresh context (`fork_turns: none`), dated 2026-09-20. It reviews prepared commit `1c498e09b5a4b1248f43ee3ce7a8da9285ba4b5f`, under the adjacent `assignment.md` and `dispatch.json`. All 17 dispatched input SHA-256 bindings were checked and matched before substantive inspection. The exact bindings, inspected source hashes, findings and coverage are also recorded in `review-result.json`.

## Actual inspection coverage

- All 5 assertions (RV01–RV05), all 11 anchors, and all 10 distinct source-locator pairs were read and assessed for entailment.
- All 6 new historical text sections were compared literally with their registered images: Reid preface `p1-origin`, `p1-collection`, `p1-method`, `p2-miller`, `p2-dateline`; and Lindsey `p18-overnight`.
- The reused Reid section `p286-saturday-night` was compared literally with its registered image. Its duplicate use in RV03 and RV04 does not add a second section or witness.
- All 10 assigned images were opened with `view_image` and visually inspected: Reid I title and preface pp.1–2; Reid II pp.286–289; Lindsey title, copyright verso and p.18. The four complete Reid narrative pages were inspected for the claimed attribution absence, including page margins/end matter. The bibliographic pages and surrounding narrative on the supplied pages were also inspected.
- All 10 retained LOC extraction lines were read, including the three catalog citation anchors and their surrounding retained locator lines. This was text-only inspection of one JSON snapshot, not visual verification of the finding aid or inspection of manuscripts.
- Registry metadata for all 12 additions and the reused Reid text/image were inspected. README, methodology, roadmap, evidence contract, sources documentation, NOTICE, the research memo/record/search log/audit/prepared-validation record, the changed report-generation string, and the generated pilot report were read.
- Independently compared all 152 prior source entries with preservation base `ad1c3f1bc8bdb64a39e0bca99ed03a6e1b341681`: complete metadata, all 149 distinct raw paths, and the recorded metadata/raw hashes match. All 126 protected files match both their recorded SHA-256 bindings and their base-commit bytes. All 12 added source metadata/raw bindings match, and their raw files match the prepared commit. The registry has 164 entries and 161 raw paths.

## Assertion assessment

| Assertion | Assessment |
| --- | --- |
| RV01 | Accepted as Reid's self-description. Preface p.1 explicitly names William H. Moore, describes the publishers' contractual collection activity and visits, and says Reid corrected, verified or compared furnished material. The selected text matches the page under its disclosed normalization. Neither this passage nor the surrounding page identifies the particular collector, interview or informant for II p.286. The packet correctly withholds independent verification of Reid's claimed practice. |
| RV02 | Accepted. Preface p.2 credits Major Frank E. Miller for reducing supplied material to shape and preparing indexes, and visibly carries the December 24, 1867 dateline. The title image bears 1868. These are distinct from the composition date and original evidence of the regimental narrative; the packet does not assign that narrative or eyewitness status to Miller. |
| RV03 | Accepted as a bounded negative. Reid II pp.286–289 contain the 46th Ohio narrative from its heading through its end, without a contributor credit or source footnote for the overnight passage. Named officers and Sergeant Glenn appear as actors; that does not identify an informant. The preface's general acknowledgments do not supply the missing attribution. No claim about all other writings or archives is warranted or made. |
| RV04 | Accepted. The two page images support the close verbal parallel and the retained differences, including Reid's `columns`/`Rebel` and Lindsey's `column`/`Confederate`, plus the changed horse-checking sentence. Both transcriptions match their images. The title names T. J. Lindsey; the verso prints copyright in 1903. This does not establish the original evidence's date, a direct copying route or independent corroboration. The text does not identify Howell's post or say that weapons fire continued throughout the night. |
| RV05 | Accepted at the retained catalog-text level. The selected lines bind General Correspondence to I:A70–A184 / reels 119–193, interviews and the book label to I:A217 / reel 215, and “Agate” letters to I:A225–231 / reel 219. The series description expressly says a copy of the book. Adjacent labels do not prove the interviews supplied that book. Two small descriptions outside the substantive assertion should be narrowed as set out below. |

## Nonblocking precision comments

### RV-C1 — Preserve the catalog's “letters” label

The RV05 table in `docs/research/shiloh-reid-provenance-v1.md:27` and the uninspected lead in `design/shiloh-reid-provenance-v1/search-log.json:10` call the Agate holdings “clippings.” The only retained format label is:

> L1010@P23: BOX I:A225-231 REEL 219 “Agate” letters, 1861-1864

Source: `loc-reid-guide-extract-v1`, raw SHA-256 `8b762feda019e8fb4873163dad1eb22b26a7f6c20d664d18adde6aa1f8ac4f72`. This line supports the box/reel/date lead and “letters” label, but does not establish clipping format. RV05's own claim already uses the supported wording, so this does not block acceptance of the assertion.

Exact suggested clarification: replace “wartime Agate clippings” with “cataloged ‘Agate’ letters, 1861–1864; material format unverified in the retained extraction.” For the search-log lead, use “LOC I:A225–231 / reel 219, cataloged ‘Agate’ letters, 1861–1864; inspect their contents and format before identifying a Shiloh dispatch.” Preserve the prepared packet and record any accepted clarification in a separate addendum/version; do not overwrite its frozen review inputs.

### RV-C2 — Distinguish provider page labels from unverified printed pagination

The retained snapshot contains provider labels `P10` and `P23`, but no printed-page footer or independently retained pagination mapping. Consequently this review cannot verify the additional “printed p.11 / p.24” labels in the RV05 table and its three citation locators. This is a coverage limitation, not a finding that those printed page numbers are false. The provider line/page labels and the box/reel references are sufficient to locate the retained evidence.

Exact suggested clarification: use “provider P10 L424–426,” “provider P10 L453–455 and P23 L998–1000,” and “provider P23 L1010,” with the note “Printed pagination was not independently verified from the retained extraction.” Alternatively retain the printed labels as explicitly unverified until a new source version preserves their mapping. No network fetch or new evidence was performed in this review.

## Validation and unchanged results

`PYTHONDONTWRITEBYTECODE=1 make check` passed: 82 tests, followed by a successful repository check reporting `artifacts_written: false`. `PYTHONDONTWRITEBYTECODE=1 python3 design/shiloh-reid-provenance-v1/reference-audit.py` passed with the stated 5/11/10 assertion/anchor/locator counts, 10 images and zero promoted rows. A separate reviewer-written, read-only comparison against Git base bytes verified the 152/149/126 preservation counts described above.

The dossier remains 62 claims / 40 quantities / 26 events. The unchanged baseline hash is `592b62bef69b4f76a626fa7c06f17f8813b02bcf4c6753601d4ad2b413e09595`; it covers 23 engagements in 13 campaign groups and retains Brier 0.2768816348133779, worse than equal odds at 0.25. Direct admission replay retains v1 18 blocked / 22 excluded and v2 7 blocked / 33 excluded across 40 observations and the 127-engagement / 36-campaign frame. Both have zero complete candidate engagements, zero emitted rows and zero promoted rows.

I did not run the artifact-writing `make reproduce` or `make packet` commands in the shared checkout because the review assignment permits only the two review outputs. Their prepared validation record was inspected; `make check` independently exercised offline reproduction in its test fixture. No source, dossier, model/admission input, prepared artifact or Git state was edited by this reviewer.

## Limits

This separate AI analysis can fulfill the bounded review step actually demonstrated here. It is not human historical adjudication, proof of source independence, proof of source truth, or a feature-admission decision. Parent PDFs were not independently rendered in this review; visual checks used the ten supplied, hash-verified page images. The LOC PDF and archival items were not obtained, and the earlier HTTP 403 access report was not independently reproduced. No whole-book Lindsey attribution search, unseen Reid correspondence search, original newspaper comparison or historical reconciliation was performed. The original contributor, original statement and interview date, direct transmission, independent corroboration, same-post match, continuity, earliest qualifying contact, exact time, area and both full populations remain unresolved.
