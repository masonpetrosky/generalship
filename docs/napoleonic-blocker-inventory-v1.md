# Development measurement blocker inventory v1

This is a mechanical inventory of the 273 development dossiers in the frozen
evaluation partition, grouped into its 13 complete source campaigns. The owner
accepted this step after the Naples measurement pilot stopped. It inventories
recorded fields and existing citation metadata; it adopts no new historical
proposition. Source passages and images require primary inspection again before
their meaning is used in a new measurement mapping.

## Selection rule fixed before the campaign comparison

Choose one complete development campaign for a bounded existing-source
measurement pass. Exclude `third-coalition 1806`: that four-entry pilot is stopped.
Cap the next batch at 12 entries, three times the pilot's size. This is an effort
bound for the next batch, not a change to the cohort or evaluation partition.

Among the remaining complete campaigns within that cap, require each entry to
have an existing non-Bodart citation in both strength and responsibility, and
require every such citation to resolve to a registered image. Compare eligible
campaigns by the fewest distinct non-Bodart image IDs used by those two dimensions
across the whole campaign, then fewest entries, then campaign name. Count a page
once when several claims, transcript selections or entries reuse its image ID.
Keep missing direct image links explicit; do not substitute zero pages for missing
links. A legacy source without this metadata link can still have an inspected
facsimile elsewhere; mapping that relationship requires a later check.

This rule prioritizes a bounded amount of existing material to inspect, without
reading outcome values, commander labels, reputation or final-set dossiers into
the comparison. It is not a quality score or a forecast of how many mappings will
be resolved. Fewer pages can reflect thinner coverage as well as reuse. The
complete comparison table and all exclusions remain visible. Different source
IDs with identical image hashes are disclosed, not silently counted as independent
pages. Family reuse uses the existing research-convention aliases; families are
navigation groups, not a finding of independent corroboration.

## Observable fields and limits

- Preserve all 273 development entries and 546 sides as denominators. Check the
  unchanged partition against cohort and frame. Count the 52 reserved entries
  and three groups from that partition, but do not open their dossiers here.
- Record dossier status, schema version, explicit null/missing tactical and
  campaign boundaries, typed `entities`/`events`/`quantities` field presence, and
  brief-v3 completion-record presence. Earlier drafts are not failed or silently
  migrated because their completion record is absent.
- Count claims by dimension and status, including explicit unknowns and disputes.
  Only strength/responsibility citation metadata enters the page comparison.
  Do not infer side attribution by searching claim prose. Brief-v3 per-side
  references are an index to inspect, not resolved strength or command mappings.
- Preserve claim IDs, citation indices, source IDs, sections, locators, quote
  hashes, raw and complete metadata hashes, and linked image IDs/hashes. A field
  path in a hash-bound dossier is the evidence for this inventory's presence
  claim. Existing citations remain references to inspect, not newly adopted
  historical findings or assertions that every relevant passage was re-read.
- Index the separate Naples ledger, boundary and authority packages and their
  recorded selections. A package's absence means no record in these indexed v1
  packages; it is not proof that the historical evidence is absent. No text
  keyword, repeated name or common source family establishes a person, force,
  authority interval, army continuity, or model eligibility.

The resulting inspection needs distinguish unset dossier boundaries, no typed
quantity records, no indexed side mapping, and an indexed but blocked pilot
mapping. Counts of non-null selections are record-presence counts only. There is
no feature-admission decision, new source fetching, calibration scoring, model
run, separate review or subagent work.

## Reproduction and verification

`python3 -m generalship.napoleonic_inventory --write` regenerates the JSON and
Markdown inventory. Without `--write` it checks their exact contents. The shared
Makefile runs these alongside the existing checks and reproduction commands;
the frozen earlier modules and verification records remain unchanged.

The scope binds the partition, frame, cohort, conventions, source registry, all
273 development dossier versions, and the three pilot data packages. The report
also hashes its protocol and module/test code. A primary-verification record
records actual test and reproduction results; it certifies this inventory's
mechanical checks, not historical entailment or independent review.

The next measurement pass should inspect the selected complete campaign's
existing strength and command passages and their full pinned pages, record
source-specific populations, times and authority scopes in one combined table,
and ask whether either side can be paired at a common opening boundary. Stop
after that complete campaign. Preserve unresolved mappings; do not create an
automatic follow-up series or fit outcomes. A new fetch must identify the
particular admission decision it could change and receive its own bounded scope.
