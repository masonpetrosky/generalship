# Shiloh review bundle: start here

Prepared on 2026-09-20; **review not yet performed**.

1. In a fresh review conversation, attach `TN003-a42f063-v1.zip` and paste the complete
   text of `PROMPT.md` (also available alongside the ZIP).
2. Ask the reviewer to open this archive. If ZIP access is unavailable, extract it
   locally and provide `CONTEXT.md`, `PROMPT.md`, `REVIEW-COVERAGE.json`, the source
   metadata and the 26 PNGs. Text-only access cannot complete the visual audit.
3. The prompt, context and blank coverage template live under `artifacts/review/TN003-a42f063-v1/`.
   Paths elsewhere in the bundle retain their repository layout. No repository,
   account, network fetch or paid job is needed to inspect the supplied evidence.
4. Optional byte verification: run `python3 verify_bundle.py` from the extracted root.
   Its standard-library check is not a signature or proof of historical truth.
5. Return the review narrative and completed `review-result.json` to the owner.
   Save the actual response and identity before reconciling individual findings.
   Do not promote the dossier or overwrite pinned inputs based on this template.

Contents: 50 registry entries and source files; 62 claims, 40 quantities,
26 events; 13 pinned table images and 13 supplementary page images; four prior
dossiers; methodology, source contract, research memos and baseline context.

Purposive diagnostic sample: all 13 existing table facsimiles plus 13 supplementary narrative/notes pages. No random selection or population extraction-error estimate is implied.

The parent PDFs are not bundled. The 13 additional PNGs are page copies rendered
from checksum-verified local parents, with printed/PDF locators in MANIFEST.json.
They do not add independent testimony or change the historical source registry.
The review remains incomplete wherever necessary passages or original images
cannot be inspected. A separate AI review is not human historical adjudication.

Rebuild in the source repository: `make review-bundle`. Inputs are pinned to the
recorded hashes. Mutable dossier/context files have frozen copies so later work
does not break reproduction. New evidence requires a separately versioned handoff.
