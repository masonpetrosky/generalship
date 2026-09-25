# Primary assessment: Command-responsibility ledger v2, batch 6 of 8

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`. Its
SHA-256 is `d11553819371eacd22f28d1e1bc4a3cb9d01058702a77dc04e9976973854406a`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `0766caaca08fc55aa7c8d53085b910e8e32246db`; see [dispatch.json](dispatch.json).

Each required finding was checked against the cited passage before it was applied, through the
batch builder; the rebuilt ledger replays under its checker. [correction.json](correction.json)
binds the corrected ledger files.

## Required findings

- **R1** (accepted applied): Checked: every MS014 passage (Sturgis selections) names the superior only as 'Maj. Gen. G. G. Washburn' (recorded-result cit. 2, the close of the June 11 dispatch) or 'General Washburn' (reported-force-scope cit. 4). 'C. C. Washburn' and 'Cadwallader' appear only in TN031 passages, dated August. Under the v2 initials/surname rule the identification with the listing 'C.C. Washburn' has no basis. Applied: MS014 US superior changed from us-c-c-washburn to the passage-only us-washburn = PO('Washburn', US, FQ('MS014','Maj. Gen. G. G. Washburn'), 'MS014'). The resulting registry entry matches the reviewer's proposed entry exactly (recorded-result, citation_index 2, or39-1-sturgis-brices-cross-roads-selections-v1). The label superior_directing and both superior citations are kept. The rationale now reads 'kept separate from the TN031 listing ... (as for Hunter)'. Grade A is unchanged. No merge has been proposed. A passage_merges exception would be a decision for the primary, and it has not been requested.

## Advisories

- **A1** (accepted applied): Checked: the MS015 Forrest report (reported-force-scope cit. 7) continues 'while I moved Avith Lieutenant-General Lee to Tupelo for the purpose of consulting and receiving orders.' Added this passage as a citation to MS015 CS. Added a borderline note to the rationale: it was a delegation, not a relief or a death, and Lee kept directing after the handover. The command_changed label, successor Forrest and grade A are unchanged.
- **A2** (not adopted): The GA021 CS, VA115 CS and GA012 CS rationales already disclose the partial scope. The suggested statement of the 'principal force' reading belongs in the shared extraction record (docs/research/ledgers-v2.md), which this reconciler may not edit. It is left to the primary. The grades are unchanged.
- **A3** (accepted applied): Stated the basis rather than changing the value. The TN031 US rationale now says the engaged Union force was the Memphis garrison, and that Washburn's district command is recorded as detachment_or_post. This follows the b3 precedent for Ripley's district command at SC004. The echelon stays detachment_or_post.
- **A4** (accepted applied): Checked and added the sharper superior citations, keeping the existing ones. GA016 US adds 'Sherman therefore determined that the longest way round would prove the surest' (Cox, reported-force-scope cit. 5). GA014 US adds 'was concerned lest Schofield had not fully met the spirit of his instructions' (Cox, found by FQ in a bound GA014 citation). The labels and grades are unchanged.
- **A5** (accepted applied): Added two Cox citations (GA022 reported-force-scope cit. 7) that support the rationale: 'About three o'clock in the afternoon Hardee advanced against the Army of the Tennessee' and 'Sherman's impatience at the delay became so great that Thomas galloped away in jDerson on the same errand'. Grade A is unchanged.
- **A6** (kept as is): The AL003 choices follow rule 5's second case as written (Farragut C, Buchanan C, joint_command, candidates Granger and Page). Both rationales already state that a jointly-compelled reading would give grade D, so the alternative stays visible.
- **A7** (kept as is): GA011 contains GA012 and is recorded as nested, consistent with the VA032 precedent (whole-army force fields; the description runs May 26 to June 1). The NEST reason already states that a narrower reading of the record would make the pair nesting_unresolved. The consequence the reviewer noted (GA012, a Confederate victory, is dropped from views containing both records) is recorded for the primary.
- **A8** (not adopted): This concerns the review-bundle input bindings, not the batch file. It is left to the primary for later bundles. The reviewer recorded the hashes of the unbound files.

This AI review is a separate analysis, not historical adjudication, feature admission or
authorization of any fit. The ledger rates nobody and changes no model input.
