# Primary assessment: Command-responsibility ledger v2, batch 3 of 8

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`. Its
SHA-256 is `8b4a6ed483751fd600b403d4cf22ad803842603ce80e436d92c213c1edcba78b`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `dddcefeb2b7adbe2b46607fb4128fed60b87319e`; see [dispatch.json](dispatch.json).

Each required finding was checked against the cited passage before it was applied, through the
batch builder; the rebuilt ledger replays under its checker. [correction.json](correction.json)
binds the corrected ledger files.

## Required findings

- **C1** (accepted applied): MO019 US: checked Britton hartville p.459-460 (Warren's orders reached him the morning of the 9th; column left Houston at noon and reached Hartville 'the next morning at sunrise', i.e. the 10th; the garrison was captured on the 9th). Rationale now says Merrill reached Hartville on the morning of the 10th and fought there on the 11th. Grade B unchanged.
- **C2** (accepted applied): SC004 CS: the full Beauregard sentence reads 'for the defense of the several land approaches to the position', and the same report says the Union land forces 'made no attempt to co-operate actually with the naval attack'. Removed superior (Beauregard), superior_citations and the superior_directing label; labels now ['responsibility_unresolved']; rationale rewritten as proposed. Ripley grade C, candidate Beauregard unchanged.
- **C3** (accepted applied): LA008 US: Irwin's 'From New Iberia Banks ordered Grover to send a detachment' introduces Kimball's Avery salt-works errand, not the Vermilion fight. Replaced that superior citation with the frozen description 'Banks, in pursuit, sent two columns, on different roads, toward Vermillion Bayou on the morning of April 17.' and revised the rationale. superior_directing: Banks kept; grade A unchanged.
- **C4** (accepted applied): OK006 US: Williams's report names 'Lieutenant-Colonel [Theodore H.] Dodd, commanding escort to the train' and says he 'concluded to accompany this train'; Britton p.95 says 'The escort to the train was commanded by Lieutenant-Colonel Theo dore H. Dodd' (the escort included Foreman's detachment, which made first contact) and that the forces were united 'under him' only that evening. Grade A -> C, labels ['responsibility_unresolved'], candidate us-theodore-h-dodd (new passage-only registry entry cited to OK006 command-roles #1). Added the Dodd, 'I concluded to accompany', 'to unite under him' and description citations (dossier citations via FQ/DQ rather than the reviewer's direct P() form; same source and quotes). Rationale rewritten. Commander stays Williams; echelon unknown.
- **C5** (accepted applied): Applied by the primary: the cs-hagood passage merge (merges.json) now cites SC007 command-roles 6, 'commanded succes- sively by Brigadier Generals Taliaferro, Johnson Hagood', with a basis naming that passage; the batch file's Taliaferro citation carries his full name.
- **C6** (accepted applied): cs-william-b-taliaferro passage citation quote changed to 'Brigadier General William B. Taliaferro, who was on duty at Savannah when the descent was made on Morris Island' (same dossier reference, SC007 reported-force-scope #2, Jones wagner-july-18 p.230; verified). SC007 CS choice unchanged.

## Advisories

- **A1** (primary decision): Systemic, cross-batch: surname-only identities for superiors and successors (in b3: LA007 CS successor cs-alfred-mouton from 'Mouton rode up'; OK006 CS superior cs-douglas-h-cooper from 'General Cooper'; LA009 CS superior cs-franklin-gardner from 'Gardner sent out Miles'). No change in b3; the primary should decide once across batches between passage-only IDs (e.g. cs-mouton, cs-cooper, cs-gardner) and a documented contextual-identity rule.
- **A2** (accepted applied): SC009 CS: the only stating passage (Elliott forwards the demand to Beauregard, who replies) shows authority over Sumter's surrender but does not state command of the works engaged first. Grade A -> B (listing-only citations, as the checker requires for B), consistent with GA002 CS; the Jones passage is quoted in the rationale, and the rationale now records the July Jones passage putting the harbor islands in Ripley's First Military Division without treating it as a contradiction for September 7-8.
- **A3** (kept as is): SC009 US: us-quincy-gilmore stays separate from us-quincy-a-gillmore (surnames differ; no passage basis offered). It is only a candidate here. Any merge is the primary's call.
- **A4** (accepted applied): SC004 CS: added Beauregard's Oct 15 citation 'Brig. Gen. E. S. Eipley, Col. William Butler, and Col. Alfred Bliett, who commanded at that period respect- ively in this military district the batteries on Sullivan’s Island and Fort Sumter' (SC004 obstructions-and-ranges #8, p.244; verified) and noted it in the rationale. Grade C unchanged.
- **A5** (accepted applied): SC005 US: added the Jones citation 'as officially reported by General Strong, who commanded in person on both occasions' (SC005 reported-force-scope #10, p.206) and recorded it in the rationale as subordinate context. Gillmore grade A unchanged.
- **A6** (kept as is): TX006 CS: the rationale already records Odlum ('commanding post') as context with no directing passage; no label added, as the reviewer agrees.
- **A7** (accepted applied): LA009 CS: added Irwin 'This brought on the action known as the battle of Plains Store.' and a rationale note that Irwin frames Miles's sortie as the battle while first contact is Powers's detachment in both accounts, and that Irwin's 'S. P. Powers' is linked by event, not name. Choice and grade unchanged.
- **A8** (accepted applied): Echelons: AR011 CS unknown -> division (frozen forces row 'division'; Marmaduke division at MO020/AR007). MO019 US unknown -> detachment_or_post (frozen forces row 'Detachment of infantry, cavalry, and artillery (approx. 700)'). Rationales note the basis.
- **A9** (kept as is): LA012 CS (Taylor), OK006 CS (Cooper) and GA002 US (Du Pont) superior_directing labels follow the MS001 precedent; reviewer finds them acceptable. Cross-batch threshold consistency is for the primary.
- **A10** (not adopted): Bundle manifest omissions (docs/commander-ratings.md, docs/ledgers-v2.md, docs/research/command-responsibility-v1.md, generalship/command.py) are outside this batch file; review bundles are immutable. For the primary to bind in future bundles.

This AI review is a separate analysis, not historical adjudication, feature admission or
authorization of any fit. The ledger rates nobody and changes no model input.
