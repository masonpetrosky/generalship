# Shiloh review handoff

Prepared 2026-09-20. **The review has not been performed.** This handoff packages
the draft at evidence commit `a42f06390651eea01d952a7cb7c329f410a6f9ab`; it does
not revise evidence, record an independent review or admit model features.

## Send to the reviewer

Run `make review-bundle`, then use a fresh review conversation:

1. Attach [TN003-a42f063-v1.zip](../../artifacts/review/TN003-a42f063-v1/TN003-a42f063-v1.zip).
2. Paste the full [review prompt](../../artifacts/review/TN003-a42f063-v1/PROMPT.md).
3. Bring back the review narrative and completed `review-result.json`.

The prompt is model-independent and can be used with the owner's chosen AI or
human reviewer. A separate AI conversation supplies another analysis, not
independent human historical adjudication or independent underlying sources.
No model job, external message or paid service is started by this workflow.

If the reviewer cannot open the ZIP, extract and provide its contents. The
[text companion](../../artifacts/review/TN003-a42f063-v1/CONTEXT.md) includes the
full dossier, cited text snapshots and cited CSV rows, but the visual audit also
requires the PNGs. Missing access must be reported as incomplete coverage.

## Contents and scope

- All 62 claims, 40 troop observations and 26 events, including three unknowns.
- All 50 registered source files and their original metadata/hashes. Uncited
  context files are included for completeness, not additional corroboration.
- All 13 existing table facsimiles and 13 supplementary narrative/notes pages.
  The page images are complete renderings from checksum-verified OR I.X.1,
  Reed (1909) and Michigan (1863) parent PDFs. Full parent volumes are not included.
- Four prior dossier versions, source and methodology contracts, the four
  research memos, attribution and baseline context.
- A blank [coverage template](../../artifacts/review/TN003-a42f063-v1/REVIEW-COVERAGE.json),
  file manifest and a standalone standard-library verifier.

The visual sample is purposive, covering known ambiguities and table extraction.
It is not a random sample and cannot estimate an overall extraction-error rate.
Every scan is mapped to the snapshot sections to compare; reviewers must state
which sections/cells they actually inspected. Full-page context beyond the
selected sections can reveal other issues, but has not automatically become a
new admitted claim.

The prompt asks for field-specific findings, exact replacement proposals,
source IDs, passages, locators, hashes and remaining uncertainty. It explicitly
allows disputes and unknowns to remain. Each coverage row starts `not_reviewed`;
reviewer identity/date are null and `review_completed` is false. These are response
instructions, not a fabricated review record.

## Reproduction and validation

`make review-bundle` runs [the offline builder](../../scripts/prepare_shiloh_review.py).
It checks frozen input hashes before writing the output and uses fixed ZIP
ordering/timestamps. Mutable dossier/context files are copied into the versioned
recipe so later research does not break this handoff's reproduction. Pinned raw
sources and archived dossiers are reused unchanged. New evidence needs a new
bundle version, not silent replacement of this assignment.

The recipe records supplementary page parent hashes, original URLs, printed and
one-based PDF page numbers, rendering transformations and PNG hashes. Rendering
used the optional local pypdfium2 research tool; rebuilding the bundle and running
tests need only Python 3.11+ standard library. The 13 new images were visually
checked for page identity and legibility. Those packaging checks are not an
independent transcription or historical review.

Inside the extracted archive, `python3 verify_bundle.py` verifies each payload
hash against MANIFEST.json. [bundle.sha256](../../artifacts/review/TN003-a42f063-v1/bundle.sha256)
records the full ZIP hash. Hashes establish byte consistency, not authenticity
against an attacker who can change both payload and manifest, or historical truth.
The ZIP is reproducible and ignored by Git to avoid duplicating source images;
the recipe, images, prompt, text companion, blank template and manifests are tracked.

Tests cover payload/source completeness, deterministic archives, exact coverage
IDs, explicitly unreviewed templates, extracted verification, corrupted inputs,
and rebuilding the frozen handoff after a later live-dossier change.
Run `make check`, `make reproduce`, `make packet` and `make review-bundle`.
On 2026-09-20 all 41 tests and the offline contract check passed. Repeated ZIP
builds matched; extraction and verification succeeded; deliberate tampering was
rejected. Comparison against the evidence commit confirmed the dossier, pinned
data, baseline code and all existing generated artifacts remained byte-identical.
The current dossier, pinned data and baseline remain unchanged: 23/127 engagements
in 13 eligible campaign groups within a 36-campaign frame; Brier 0.276882, worse
than equal odds at 0.25.

## Reconcile the returned review

Preserve the actual response with reviewer identity, date, type, exact bundle and
dossier hash. Check its coverage before treating silence as agreement. Verify
each proposed correction against the cited source and retain unresolved disputes.
Any accepted evidence revision must archive the previous dossier and keep source
changes versioned. An AI response alone must not be relabeled as completed human
review. Feature admission remains a separate reviewed contract to implement later.
