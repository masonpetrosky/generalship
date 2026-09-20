# Separate review: Shiloh regimental and post comparison

**Verdict: requires two literal corrections, comprising three word/abbreviation replacements.** All seven historical assertions remain supported within their stated limits. The packet correctly leaves post identity, incident continuity, location, timing and complete populations unresolved. The required findings concern the map transcription and its two RP06 anchors; neither requires a new historical interpretation or permits feature admission.

Reviewer: `/root/shiloh_regimental_review`; GPT-6 Astra (`gpt-6-astra`), `xhigh`, fresh context (`fork_turns: none`), September 20, 2026. This is the actual separate AI analysis, not human historical adjudication or proof of source independence.

Reviewed input commit: `dc669f4ddb8388eea9c9029738f4f6b6e65c069c`. Preservation base: `af5075a8a8c51ab35d049720297a260bdd6bd676`. HEAD and all 16 dispatch-bound file hashes matched before inspection and again before writing the result. The exact assignment, dispatch, source, section and image bindings are retained in `review-result.json`.

## Actual inspection coverage

- **7/7 assertions; 21/21 anchors; 19/19 distinct source-section pairs.** These comprise every one of the 17 selected historical sections in the five new text sources and the two reused sections.
- **16/16 named page images visually inspected with `view_image` at original detail:** 13 new facsimiles and three reused facsimiles. The inspection included all supplied bibliographic/context pages, the complete two map halves, every quoted selection and the relevant surrounding narrative. It did not transcribe or audit unrelated force tables or every map symbol.
- Of the 19 distinct sections, 17 match the images under the declared normalization; the two remaining map sections require the corrections below. The corresponding anchor counts are 19 matching and two requiring correction. These are inspection counts, not an estimated extraction-error rate.
- Read the research memo, research record, search log, registry entries, audit implementation, README, roadmap, sources document, NOTICE and generated pilot report, together with AGENTS, methodology and evidence-contract instructions. Checked the preservation and non-promotion assertions independently.

| Source | Sections inspected | Image coverage |
|---|---|---|
| `reid-1868-regimental-posts-v1` | `p286-saturday-night`, `p413-april3-to6` | `reid-posts-title-facsimile-v1`, `reid-posts-p286-facsimile-v1`, `reid-posts-p413-facsimile-v1` |
| `lemmon-1875-regimental-posts-v1` | `p5-6-april4`, `p6-rescuers`, `p6-rain`, `p7-transition` | `lemmon-posts-heading-facsimile-v1`, `lemmon-posts-p5-facsimile-v1`, `lemmon-posts-p6-facsimile-v1`, `lemmon-posts-p7-facsimile-v1` |
| `worthington-facts-posts-v1` | `p2-item11`, `p2-item14` | `worthington-posts-front-facsimile-v1`, `worthington-posts-flank-title-facsimile-v1`, `worthington-posts-facts-heading-facsimile-v1`, `worthington-posts-facts-p2-facsimile-v1` |
| `worthington-1872-post-locations-v1` | `p140-distances`, `p140-saturday-posts` | Reused `worthington-howell-p140-facsimile-v1` |
| `buell-battles-leaders-map-posts-v1` | `p502-howell-label`, `p502-camp-legend`, `p502-phase-legend`, `p503-title`, `p503-topography`, `p503-camps`, `p503-revision` | `buell-posts-p502-facsimile-v1`, `buell-posts-p503-facsimile-v1` |
| Reused `worthington-1872-howell-v1` | `p137-sherman-denial` | Reused `worthington-howell-p137-facsimile-v1` |
| Reused `medkirk-1886-howell-v1` | `p537-saturday` | Reused `medkirk-howell-p537-facsimile-v1` |

The repeated anchors are Reid `p286-saturday-night` and Lemmon `p5-6-april4`; they do not add independent sections or witnesses.

## Required findings

Both findings concern `buell-battles-leaders-map-posts-v1`:

- Raw SHA-256: `2add17ef1ae7f7e9a0e7cd849735e69c3ceb1c15525af7902d0f1beb998d3fca`.
- Complete metadata SHA-256: `055dde66399a34f36169e6d918936ee9b4b776506f03ca21681459078560504c`.
- Direct image: `buell-posts-p503-facsimile-v1`, printed p.503 / PDF p.533; raw SHA-256 `0e38e2000330132030e03fcd310b32a870255cad12973bb99fc8eeb1eaf5699d`.
- Parent PDF SHA-256: `ced04dc52ad80568640bd53ba055d0d012c870787e5e0471e1e3ffa87e203a4e`.

**SHILOH-RP-R1 — Restore “camps” in `p503-camps` (medium; required).**

The image prints **“All camps referred to in the official reports have been carefully identified.”** The selected text and RP06 anchor instead say **“All changes referred to…”**. This changes the object of the map maker's provenance claim from camps to changes. The retained full-page image and an enlarged in-memory image detail directly establish the reading.

Exact replacement section:

> The camps are located partly in accordance with a camp map made prior to the battle by Gen. W. T. Sherman (see fac-simile, p. 496); partly from information, original or confirmatory, obligingly furnished by Capt. Andreas, and from other authority. All camps referred to in the official reports have been carefully identified.

**SHILOH-RP-R2 — Preserve both “Vol.” abbreviations in `p503-title` (low; required).**

The title prints **“U. S. Vol.”** after both Grant and Buell; the transcription and RP06 anchor contain **“U. S. Vols.”** twice. Adding `s` falls outside the declared normalization. This reading was checked against the retained image and a scale-6 in-memory render of PDF p.533 after independently matching the locally available parent's SHA-256.

Exact replacement section:

> MAP OF THE FIELD OF SHILOH,
> Near Pittsburg Landing, Tenn., showing the positions of the U. S. forces under
> Maj.-Gen'l U. S. Grant, U. S. Vol., and Maj.-Gen'l D. C. Buell, U. S. Vol., on the 6th and 7th of April, 1862.

For both findings, add a new source version and explicit correction overlays for the two RP06 anchors. Preserve the v1 raw text, metadata, images, frozen research record and this review. Change only the three literal occurrences; retain null exact document dates, dependency notes and historical unknowns. Full current and replacement section text, source/image hashes and affected assertions are machine-readable in `review-result.json`. The primary agent must verify and apply the correction; the reviewer changed no evidence.

## Entailment, context and metadata assessment

**RP01:** Reid p.286 supports the 46th Ohio B/K Saturday picket assignment, overnight “feeling the lines constantly,” daylight deployment and sunrise cavalry encounter. The retained paragraph also says “comparative quiet.” The surrounding passage subsequently describes the fatal exchange with the cavalry officer, but does not name Howell or establish an overnight firing schedule. Unknown contributor identity and unlocated post remain justified limits.

**RP02–03:** Reid p.413 explicitly prints A/D/F; Lemmon p.6 prints A/D/I. No silent correction or merged rescue account is warranted. The retained spans move from April 4 to April 6–7 without describing Saturday Howell contact, which supports only the stated bounded omission. Lemmon's rain interruption is followed by resumed firing within his April 4 narrative. It cannot supply Saturday termination or a Sunday reset.

**RP04–05:** Worthington p.140 prints the Howell–Weaver distance, camp–Moore limit, Saturday Moore post, brigade-relative left and Sharpe's express limit on other brigades' pickets. The reused p.137 passage prints Sherman's opposing house/picket account. The appended tract's items 11/14 print occupation and the 46th Ohio 7 a.m./half-mile allegation without naming Howell or Moore. None supplies a surveyed datum, unique post match, synchronized incident chain or authenticated official testimony. “It was proven” remains Worthington's allegation.

**RP06:** The actual map supports the bounded interpretation after the literal fixes: p.502 labels Howell Farm, distinguishes regimental camps from line symbols and defines later battle phases; p.503 explicitly names April 6–7. The caption claims a retrospective combination of Thom, Andreas, Michler, Sherman and official-report material. It is not independent verification of those inputs. Neither a Saturday Howell house/picket coordinate nor Weaver/Moore identification is established. No compass orientation or battle polygon is inferred from page layout.

**RP07:** Medkirk's E/C of the 72d east of Howell farm and Reid's B/K of the 46th on an unnamed line cannot be joined into continuous fire or assigned a post relationship. Neither identity nor contradiction follows. A source-to-Reed link also remains unestablished; Whitelaw Reid is properly distinguished from D. W. Reed.

The source-date distinctions are appropriate. Reid's title visibly gives 1868. Lemmon's heading dates speech delivery June 17, 1875 without establishing printing or composition days. The Worthington composite front is undated, its separate *Flank March* title bears 1880, and *Facts Developed* dates the trial August 1862. The packet correctly leaves the appended tract's date null. Buell's caption has June 1885 and an edition note referring to corrections beyond March 1886; no exact day is fabricated. Medkirk's March 22, 1886 letter attribution is visible on p.537. The older Worthington 1872 publication label and Medkirk volume's 1887 copyright basis were retained from existing metadata, not independently re-established by newly inspecting their earlier title/copyright images in this review.

Repeated Worthington selections share their publication family and do not add witnesses. The two Reid entries are one compilation with unknown particular contributors. The Medkirk map cross-reference is a publication linkage, not independent proof of a post. Different source groups do not prove independence. The README, roadmap, sources, NOTICE, research memo and generated report retain these material limits and make no new admission or improvement claim. There are no additional nonblocking comments.

## Independent preservation and validation

The reviewer independently compared the actual base commit with the current repository: all **133 prior registry entries, 130 prior distinct raw paths and 109 bound preserved files** are unchanged. This checked the original metadata and bytes, not only the hashes asserted by the new packet. The current registry contains **151 entries / 148 raw paths**. Earlier review bundles, dossier, both admission proposals, frozen cohort and baseline remain preserved.

The bounded offline audit passed. `PYTHONDONTWRITEBYTECODE=1 make check` passed **82 tests** and the pipeline check, which reported `artifacts_written: false`. These mechanical checks cannot detect a quote faithfully copied from an incorrectly transcribed source file; they do not override the two image findings.

Direct admission validation retains v1 **18 blocked / 22 excluded** and v2 **7 blocked / 33 excluded**, with zero complete, emitted or promoted rows over **127 engagements / 36 campaigns**. TN003 remains draft with **62 claims / 40 quantities / 26 events**. The baseline remains **23 engagements / 13 groups**, with Brier **0.2768816348133779**, worse than equal odds **0.25**. No improved result, canonical opening strength or feature admission is established.

No network fetching, source mutation, git mutation, artifact regeneration or historical feature release was performed by this reviewer. Only the two assigned review outputs were written. The existing test suite includes offline reproducibility coverage; `make reproduce` was not invoked because it would rewrite generated artifacts outside this assignment.

Original trial records, Medkirk manuscripts/editorial records, Reid contributor records, survey inputs and commission correspondence remain uninspected. Only the already registered *Battles and Leaders* parent was reopened for supplemental p.503 magnification; the primary agent's broader parent-render checks are separate and are not claimed as reviewer coverage. An accurate transcription can still preserve an inaccurate historical account.
