# Primary assessment: Command-responsibility ledger v2, batch 5 of 8

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`. Its
SHA-256 is `3342d76995b118342d813def5a2beaea0b47d7cdb74d7661d3a4c15ef1ebd0dd`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `2f63306ad033e2bda1710dd88dd47c99cf86f748`; see [dispatch.json](dispatch.json).

Each required finding was checked against the cited passage before it was applied, through the
batch builder; the rebuilt ledger replays under its checker. [correction.json](correction.json)
binds the corrected ledger files.

## Required findings

- **R1** (accepted applied): Checked against Humphreys reported-force-scope/3 (Smith took orders from Butler on the 14th; Hinks's rifle-pit 'early in the day'; Grant's staff officer about 4 p.m., despatch to Hancock before 5.30) and Meade rations-and-bridge/0 (orders late on the 15th; instructed on the 16th to take command in front of Petersburg). Humphreys's 'Grant's plan' footnote is self-described inference. VA063 US: Grant 3a/A/[] -> Grant 3b/C, labels command_changed+responsibility_unresolved, successor Meade, candidate Meade, superior null; four new quotes added, two existing Grant/Meade quotes lengthened; rationale rewritten (includes A8 context).
- **R2** (accepted applied): Checked Humphreys reported-force-scope/2: Hill 'had been sent down the Weldon Railroad to meet Meade's attempt', and the June 21 contact is unattributed. VA065 CS: Lee rule 2 A -> Lee rule 2 C, label responsibility_unresolved, candidate Hill; both quotes added; rationale replaced, alternative reading (Hill, cf. VA073) recorded.
- **R3** (accepted applied): Checked Lee dispatch of June 29 (Hampton 'at daylight this morning ... turned their left'), Wilson July 3 report ('By 7 a. m. of the 29th General Kautz's advance reached Beams' Station') and the frozen VA068 description (Wilson fighting Rooney Lee's elements before joining Kautz); VA067's frozen interval is 1864-06-28. First combat within the interval was Hampton's (unlisted). VA068 CS: Mahone 3a/C/division -> null 3c/D/unknown, candidates Mahone and Fitzhugh Lee, no successor/superior; Wilson 7 a.m. quote and the description's Rooney Lee sentence added; rationale rewritten. US side unchanged.
- **R4** (accepted applied): Checked Humphreys reported-force-scope/2 ('finding only Dealing's cavalry brigade'; 'General Dearing had reported to General Beauregard') and Lee's Aug 18 dispatch ('met by General Heth'). VA072 CS: Heth 3a/C and all fields unchanged; both quotes added; misreading sentence replaced with the reviewer's wording plus the rule 3(b) (Lee) alternative.

## Advisories

- **A1** (not adopted): Kept VA062/VA099 not_nested: rule 7 calls for nested only when a passage shows the containing record's fighting or force scope includes the contained record, and the recorded reason (separate Louisa County raid, not narrated in the Cold Harbor description) stands. Whether force-scope uncertainty should trigger nesting_unresolved is left to the primary, as the reviewer says.
- **A2** (primary decision): merges.json is shared and not editable here. Proposed: in merges.json _passage entry for cs-johnson-hagood (SC007), cite the passage that gives the given name, SC007 command-roles/6 (jones-charleston-1863-selections-v1, section wagner-siege-and-evacuation): 'commanded succes- sively by Brigadier Generals Taliaferro, Johnson Hagood', instead of the 'General Hagood relieved General Taliaferro' quote, which has no given name. VA047 outcome does not depend on it.
- **A3** (accepted applied): VA052 US rationale now calls superior_directing Meade borderline, quoting Sheridan's 'determined at once to march around the enemy's right flank'. Label kept.
- **A4** (accepted applied): VA077 US rationale notes that Humphreys's 'the right of the force on the north side of the James' implies a larger force with no named commander for October 7, so grade C would also be defensible. Choice and grade A kept. The August Birney quote is not in VA077's dossier and was not cited.
- **A5** (accepted applied): VA083 US rationale records the rule 3(a) Humphreys alternative and why it is not adopted (Gregg's Dinwiddie contact unordered in time and under neither listed officer). Grade D kept; authorship note already present.
- **A6** (kept as is): VA059 US: the repeated Torbert quote is the superior_citations entry, a separate field that must carry its own citation; the citations list itself has no duplicate. No change.
- **A7** (not adopted): No inspected passage attributes the June 21 contact to Hill's force, so rule 2's third bullet is not met; the Hill alternative is recorded in the VA065 CS rationale for the primary.
- **A8** (accepted applied): Folded into the R1 rationale: Butler (orders to Smith) and Smith are named as unlisted context only.

This AI review is a separate analysis, not historical adjudication, feature admission or
authorization of any fit. The ledger rates nobody and changes no model input.
