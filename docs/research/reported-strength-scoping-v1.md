# Reported side-strength: extraction scoping, v1

Prepared 2026-09-25. This memo scopes the bounded research that the accepted
[tier-2 design](../feature-admission-reported-strength.md) authorizes (§7), before any
candidate is typed, proposed or reviewed. All statuses below are the extractor's
**provisional** §3 coding. They approve nothing and are not an evidence-use review. No
dossier, proposal or model input changed.

**Result: under the accepted rules, the tier-2 profile would add very few rows.** An
honest estimate is about 23–25 complete engagements in the best scenario, against 23
today. Two current baseline rows would drop out, because their frozen figures turn out
to be loss-derived. The owner's decision is needed before building the full proposal.

## What was done

- **Livermore pinned.** Livermore, *Numbers and Losses in the Civil War in America*
  (1901), is pinned as three kinds of record:
  - catalog metadata (`ia-livermore-metadata-v1`);
  - full OCR (`livermore-ocr-v1`);
  - 25 page images of printed pp.78–107 (`livermore-p{N}-image-v1`), from the University
    of California copy, Internet Archive `numberslosses00liverich`.

  A second Internet Archive scan (`numberslossesinc00live`) has worse OCR and was not
  pinned. OCR runs superscript note markers into the figures ("about 2 16,000"), so
  every figure below was read from the page images.
- **Livermore entries read.** Every 1862–63 entry matching a decisive, non-aggregate
  frozen record was read in full, with its numbered notes.
- **Dossier scan.** The first-pass strength claims of all 68 decisive engagements
  lacking a complete frozen pair were scanned for applicable figures on both sides.

## Livermore entries (page-verified)

| Frozen record | Livermore entry | Union figure(s) | Confederate figure(s) | Provisional result |
| --- | --- | --- | --- | --- |
| TN002 Fort Donelson | p.78, Feb 12–16 | 27,000 "in the lines and guarding the road" (Grant's Memoirs) | "Engaged about 21,000" (Grant's Memoirs; note 5: basis unknown) | US `basis_unknown`; CS `adversary_or_hearsay_estimate` |
| TN003 Shiloh (baseline) | pp.79–80 | Total engaged 62,682 (Army of the Tennessee effectives, estimated, + 20,000 Army of the Ohio) | Effectives 40,335 | Mixed basis (engaged vs effective) |
| VA016 Beaver Dam Creek (baseline) | p.82, Mechanicsville | Effectives 15,631 (93% estimate) | Effectives June 26, 16,356 | Same-basis pair; **frozen values identical** |
| VA017 Gaines' Mill (baseline) | pp.82–83 | Effectives 34,214, from a return **less June 26 losses** | Total effectives 57,018, **adding losses June 28–July 1** | Both `derived_from_losses`; **frozen values identical** |
| VA021 Malvern Hill | pp.84–85 | Composite entry: Savage Station, Glendale and Malvern Hill, June 29–July 1 | Same | `other_engagement` |
| VA022 Cedar Mountain (baseline) | pp.87–88 | 8,030, no basis stated | Total engaged 16,868; note 5 adds 195 lost Aug 9 | US `basis_unknown`; CS `derived_from_losses`; **frozen values identical** |
| VA026 Manassas, Second | pp.88–89, Manassas and Chantilly, Aug 27–Sep 2 | Composite | Composite | `other_engagement` |
| KY007 Richmond | p.89 | Manson's command 6,500 (note 5: "probable" effectives) | Total engaged 6,850 | US `basis_unknown` |
| MD002 South Mountain | pp.90–91 | 93% of Sept 17 return **plus Sept 14 losses** | Sept 22 return **plus losses** and captures | Both `derived_from_losses` |
| MS002 Corinth | p.94 | Present for duty Sept 30, 23,077; effectives 21,147 | "Field returns," Sept 28, about 22,000 | CS `basis_unknown` |
| KY009 Perryville | p.95 | Note 1 **adds Oct 8 losses** to the 3d Corps | Effectives about 16,000 | US `derived_from_losses` |
| VA028 Fredericksburg (baseline) | p.96 | Present for duty 120,281; engaged 113,987; effectives 106,007 | Present for duty 78,513; effectives 73,017; engaged 72,497 (**frozen CS identical**) | Same-basis pairs on three bases |
| MS003 Chickasaw Bayou | pp.96–97 | Present for duty 33,033; effectives 30,720 | Total engaged 13,792 from Jan 2–3 returns **plus losses** | CS `post_engagement_state` / `derived_from_losses` |
| TN010 Stones River | p.97, Dec 31–Jan 1 | Present for duty 44,800; effectives 41,400 | Present for duty 37,712; effectives 34,732 | **Same-basis pairs (new row)**; Livermore's dating differs from the frozen Dec 31–Jan 2 |
| AR006 Arkansas Post | p.98 | Effectives at Chickasaw Bluff **less losses there** | 93% of those surrendered **plus the loss** | Both `derived_from_losses` |
| MS009 Champion Hill | p.99 | Final effectives May 16 **deduct losses**; April 30 figures are intermediate | Effectives about 20,000 | US excluded or `engagement_link_unknown`; no pair |
| MS011 Vicksburg | p.100, assault of May 22 | Adds May 22 losses | Components dated June | `partial_interval` for the siege record |
| PA002 Gettysburg (baseline) | pp.102–103 | Effectives 83,289 (**frozen identical**) | Effectives 75,992; total engaged 75,054 **deducts prior losses** (**frozen identical**) | Effectives pair; CS total `derived_from_losses` |
| GA004 Chickamauga | pp.105–106, Sep 19–20 | Effectives 58,222 ("total engaged" 53,919 is infantry and artillery only) | Total engaged 66,326 (sum of effectives) | Mixed basis only (**new row in `mixed_basis`**) |
| TN024 Chattanooga | pp.106–107 | Total engaged 56,359 | Present for duty 44,010, including a **December 10** return | CS `post_engagement_state` |

## Findings

1. **Livermore adds one clean new row.** Stones River has same-basis pairs. Chickamauga
   has a mixed-basis pair only. Most other entries fail on three grounds:
   - derivation from losses (added to or subtracted from a return);
   - an opponent's estimate or unstated basis;
   - a composite or partial engagement.
2. **The frozen baseline shares Livermore's figures.** Five frozen CWSAC force figures
   in the current 23-row baseline equal Livermore's totals exactly: Beaver Dam Creek,
   Gaines' Mill, Cedar Mountain, Gettysburg and Fredericksburg (Confederate). The NPS/CWSAC
   and Livermore families are therefore not independent. Three of those frozen figures
   are loss-derived reconstructions:
   - Gaines' Mill, both sides;
   - the Cedar Mountain Confederate total;
   - the Gettysburg Confederate total.

   Under the accepted rules, Gaines' Mill and Cedar Mountain would have no tier-2 row,
   and Gettysburg would keep one only through Livermore's effectives pair. The existing
   baseline is unchanged; this is a finding about its inputs, not a correction.
3. **The dossiers add almost nothing on their own.** Across the 68 decisive
   engagements without a frozen pair, the first-pass strength claims offer an applicable
   figure for both sides in only a few cases. Corinth's live NPS pair, US 23,000 and
   CS 22,000, is the clearest; Helena might qualify if its bases can be established.
   Elsewhere the figures are opponents' estimates, one side only, partial (brigades,
   bayonets, infantry alone), one-sided bounds ("did not exceed"), post-engagement
   returns or unstated bases.
4. **The loss rule is conservative.** The accepted design excludes any figure
   "reconstructed from losses". That covers subtracting an *earlier* engagement's losses
   (Gettysburg CS total, Gaines' Mill US, Champion Hill US), which carries no leakage from
   this engagement's outcome. Distinguishing the two would recover perhaps two or three
   more rows. It would be a design revision needing separate review.

## Implications and options

The coarser profile does not solve the data problem for 1862–63. Most usable strength
evidence for these battles either doesn't exist in compiled form or was reconstructed
from the losses the model is meant to explain. The options are:

- **(a) Finish the tier-2 pipeline as designed.** Expect about 23–25 rows. Its value is
  a reviewed ledger that documents these limits and the baseline's loss-derived inputs,
  not a larger model.
- **(b) Revise the loss rule, then finish.** Separate prior-engagement adjustments from
  this engagement's losses, which needs a reviewed design revision. Expect a few more
  rows.
- **(c) Change the approach.** For example, extend the cohort to 1864–65, where
  compiled coverage is larger but has the same derivation issues. Or reconsider whether
  battle-level strength is the right first predictor.

## Code and records

- **Validator.** The `reported_side_strength_v1` validator (`generalship/strength_admission.py`,
  with 13 synthetic tests and the `strength-check` command) is implemented but **not yet
  separately reviewed**. No proposal exists, so it runs only on synthetic fixtures.
- **Registry.** The Livermore records bring it to **608 entries / 587 raw paths**,
  preserving the earlier **581/560**.
- **Unchanged:** the baseline and cohort, both opening proposals, and the zero promoted
  rows.
