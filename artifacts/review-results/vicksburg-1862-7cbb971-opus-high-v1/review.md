# Separate review: Operations Against Vicksburg [December 1862–January 1863] (MS003, AR006)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. I ran as a fresh-context subagent (`evidence-reviewer` policy) and did not see the author's conversation.
- **Date:** 2026-09-25 (the session started 2026-09-24).
- **Commits:** prepared `7cbb97100ca5db247610b8e198b58f44fd5f5be4`; previous `e865cffa9390b65fd2015ff19c2f8ce15e950ba2`; assignment bundle `d6ea24b52ad36edd88ea86d023a06f3efd08cfd5`. The bundle adds only `assignment.md` and `inputs.json` on top of the prepared commit.
- **Assignment:** `assignment.md` sha256 `6b5a70c45eccac4af67c512c06ee3a19e8801c26f8f0025af495db0f7fb5b9a2`; `inputs.json` sha256 `c7dbd5a4ae3542dd8c91d499f84bb27860da50d796388d470ad34ae98547842b`.
- **Input hashes:** I checked all 33 bound paths in both the worktree and `git show 7cbb971:<path>`. **33/33 match. There are no mismatches.**
- **Outcome: corrections required.** There are six minor extraction/scope corrections (VB-R1 to VB-R6) and five non-blocking notes (VB-N1 to VB-N5). There are no source-integrity, locator, derivative or preservation failures.
- **Status of this review:** This is an AI review, a separate analysis. It is not human historical adjudication, independent corroboration or feature admission.

## What I actually inspected

- **Guidance:** I read `AGENTS.md`, the evidence contract, the memo and the 7cbb971 diffs to the README, methodology, roadmap, `sources.md`, `cli.py`, the tests, the report, the queue and the quality artifacts. From the roadmap and methodology I read only the sections I needed (current priority, identification/phase labels). I did not reread every older historical section.
- **Dossiers:** I read both in full: **19 claims, 62 citation occurrences** (MS003 30, AR006 32) and 2 null unknowns. All seven dimensions are present in each dossier.
- **Frozen rows:**
  - Battles: MS003 and AR006, all cited cells.
  - Forces: MS003/AR006 × US/Confederate. Every `strength_min`/`strength_max` is blank.
  - Commanders: MS003 has Sherman (US) and Pemberton (Confederate). AR006 has McClernand and Porter (US) and Churchill (Confederate).
  - I checked every CSV citation for an exact cell match.
- **NPS snapshots:** I read both retained summaries (`nps-ms003-v1`, `nps-ar006-v1`) in full.
- **Greene selection:** I read the new selection in full: the transcription note, title/preface, `chickasaw-bayou` (OCR pp.73–81) and `arkansas-post` (pp.83–88). For the parent `greene-mississippi-ocr-v1`, I inspected only about 120 characters at each range boundary. I did not read the whole book.
- **Not inspected:** original reports, returns, maps, print pages, or anything online. I used no network, no new sources and no agents.

## Mechanical results (all pass)

- **Derivative replays:** I replayed all three.
  - Each NPS HTML file matches its pinned sha256. An HTMLParser replay (skip script/style; strip and join non-empty nodes; slice from "Return to Results" up to "Experience More"; strip and add a newline) reproduces both `.txt` files byte for byte.
  - The Greene parent matches `536715e8…051e`. Each half-open range (`title-and-preface` 319–1971, `chickasaw-bayou` 153444–169012, `arkansas-post` 173253–183591), whitespace-collapsed, equals its section.
  - The `arkansas-post` section starts just after the "THE FIRST MOVE AGAINST VICKSBURG. 83" running header, so the p.83 locators are correct.
- **Quotes and locators:** Every Greene quote occurs exactly once in its cited section. I computed each quote's page from the preceding OCR page marker, and all 40 Greene locators agree. All 10 NPS quotes fall in the field their locator names. All 12 CSV quotes match their cells exactly.
- **Registry:**
  - It now has 349 entries / 346 distinct paths; the previous version had 344/341.
  - All 344 earlier entries are identical, in their original order.
  - Five entries were added: `nps-ms003-v1(-html)`, `nps-ar006-v1(-html)` and `greene-vicksburg-1862-selections-v1`. The Greene metadata and OCR are unchanged.
- **Preservation:** Between e865cff and 7cbb971:
  - The only changes under `data/evidence` are the two new dossiers. All 65 older dossiers and all 18 history revisions are byte-identical.
  - Cohort, both admission proposals, `admission-check.json`, `baseline.json` and `battles.json` are unchanged.
  - `promoted_rows` is 0.
- **Coverage:**
  - 67/127 dossiers, 60 without.
  - Of 36 campaign groups, 17 are complete by dossier presence.
  - The earliest incomplete group is **Middle Tennessee Operations [February–April 1863], TN012–TN016** (start 1863-02-03, no tie). I confirm it as next.
- **Packets and receipt:**
  - Each packet has three JSON blocks, and all parse. The assigned record matches the frozen rows: strengths null/null, `missing_numeric_strength`, and commander lists as above. The draft block equals the dossier, and the registry block equals `data/sources.json`.
  - All 99 file hashes in the receipt match, including all 7 output artifacts. All 349 `source_sha256` values match the registry. The receipt covers 85 evidence files (67 + 18 history).
- **`make check`:** I ran it offline with Python 3.14.7. All 82 tests passed and `generalship check` exited 0: 23 eligible / 13 groups, Brier 0.2768816348133779 vs 0.25, 67 drafts, 0 promoted rows, `artifacts_written: false`. The worktree was clean afterward. I did not run build or packet commands.

## Claim-by-claim entailment

**Accepted as written, with required scope quantities checked:**

- **MS003 `reported-force-scope`:** about 32,000 with 60 guns; "not less than 12,000" vs the 6,000-man garrison; "not more than 6,000". Status `disputed`, none adopted. See VB-N3.
- **MS003 `surprise-lost`:** spies/detachments reported twice a day; reports reached Pemberton on the 23rd–24th; "knew nothing" of the reinforcements.
- **MS003 `surprise-and-junction-plan`.**
- **MS003 `unsupported-assault`:** De Courcy's and Blair's brigades plus one regiment; Thayer, Lindsey and Sheldon; the Sherman "General"/Major General conflict is kept and not adopted. See VB-N2.
- **MS003 `recorded-result`:** NPS "Sherman then withdrew" is in the cited Description; the January 2 re-embarkation and the command handover follow the interval.
- **AR006 `reported-force-scope`:** about 5,000 garrison vs the letter's "seven thou- sand"; 66 naval pieces; about 45 field pieces; no Union infantry count.
- **AR006 `fort-and-trench`.**
- **AR006 `fort-armament`:** 2 + 1 + 14 = 17 guns, which matches the 17 trophies.
- **AR006 `post-objective`:** see VB-N4.
- **AR006 `unauthorized-white-flag`:** `disputed`; "by order of General Churchill"; Churchill and his brigade commanders deny authorizing it; its origin "cannot be traced"; one brigade commander refused until Churchill arrived. This is a faithful summary.
- **AR006 `recorded-result`.**
- **AR006 `casualty-records`:** 977, exclusive of 31 on the gunboats; about 200 killed and wounded; 4,791 prisoners "counted and sent North"; frozen 6,547 (US 1,047; CS 5,500) vs live 6,096 (US 1,092; CS 5,004).

**Also verified:**

- Both null unknowns carry no citations.
- Status tags are appropriate.
- No morale/readiness score, probability, causal effect or additive commander credit is introduced. Greene's judgments ("doomed to failure", "entirely miscarried") stay attributed.
- Greene's source metadata is correct: a non-participant (preface), founded on the Records, so it depends on the Official Records. Quoted letters are not treated as separate families. NPS/CWSAC is treated as one family.

## Required corrections

Each correction keeps the claim ID, status and phase, and all existing citations unless stated otherwise. New quotes were checked as unique in the named section, with pages taken from OCR markers.

**VB-R1 — MS003 and AR006 `opening-personnel-unknown`: the missing frozen strength is not visible.**
- **Problem:** The rationale says "Imported numerical estimates remain unchanged". For both records, however, `cwsac_forces.csv` `strength_min`/`strength_max` are blank for both sides. The packet shows `low: null, high: null` and `exclusion_reasons: ["missing_numeric_strength"]`, and the queue lists `missing_numeric_strength`. There are no imported estimates, and the rationale hides that gap.
- **Replacement rationale for both dossiers:** "No inspected return establishes matched personnel at a common opening boundary. The frozen side-specific numerical strength bounds are blank (missing_numeric_strength), and the live NPS zeros are not measured absence. No figure in this pass is adopted as a simultaneous opening force."

**VB-R2 — AR006 `combined-command`: the commander set is incomplete.**
- **Problem:** "The frozen commanders are McClernand and Porter" leaves out the frozen Confederate row (`AR006, Confederate, Thomas J. Churchill, Brigadier General`). The live heading also lists only "Rear Admiral David Porter [US]" and "Brigadier General Thomas Churchill [CS]"; McClernand does not appear in it.
- **Replacement value:** "Greene says McClernand assumed formal command on January 4 and asked Porter to begin the bombardment as arranged. The frozen Union commanders are McClernand and Porter, and the frozen Confederate commander is Churchill. The live heading lists only Porter [US] and Churchill [CS], omitting McClernand, and ranks Porter Rear Admiral against the frozen Acting Rear Admiral."
- **Optional added citation:** `nps-ar006-v1`, locator `Principal Commanders`, quote `Brigadier General Thomas Churchill [CS]`.

**VB-R3 — MS003 `casualty-records`: the timing scope is over-extended.**
- **Problem:** "…for December 27–29" is attached to both of Greene's figures. Only the Confederate 187 is explicitly dated ("the entire losses of the Confederates dur- ing the skirmishing of the 27th and 28th and the assault of the 29th", p.79). Greene gives the Union 1,929 inside his assault paragraph as an "exact total" with no dates.
- **Replacement value:** "The frozen casualty text reads 1,983 total (US 1,776; CS 207); the live NPS field reads 1963 total (US 1776; CS 187;). In his account of the December 29 assault Greene gives the Union 'exact total' as 1,929 (191 killed, 982 wounded, 756 missing) without stating a date range. He gives Confederate losses for the skirmishing of December 27–28 and the assault of the 29th as 187 (57 killed, 120 wounded, 10 missing)."
- **Added citation:** `greene-vicksburg-1862-selections-v1`, section `chickasaw-bayou`, locator `p.79 (OCR page markers; not checked against print)`, quote `the entire losses of the Confederates dur- ing the skirmishing of the 27th and 28th and the assault of the 29th`.

**VB-R4 — AR006 `intelligence-prompting-expedition`: the letter does not name who captured the boat.**
- **Problem:** Sherman's quoted letter says the Blue Wing "has been captured by the enemy". It does not name the Arkansas Post garrison.
- **Replacement value:** "Greene quotes Sherman's January 5 letter that McClernand brought the first news that Grant had fallen back, and that one boat carrying dispatches, the Blue Wing, 'has been captured by the enemy'. The letter does not name the capturing force, though it links 'that enemy on our rear and flank' to the threat to communications."
- **Optional:** widen the second quote to `One boat, the Blue Wing, towing coal barges for the navy and carrying dis- patches, has been captured by the enemy` (p.83; unique).

**VB-R5 — MS003 `single-pontoon-and-causeway`: the obstacle is misstated.**
- **Problem:** Greene says Steele was blocked by Thompson's Lake, which "could only be crossed" on the enfiladed causeway. He was then ordered to "cross back in the transports" and support Morgan. The causeway was the crossing, not the blocker.
- **Replacement value:** "Greene says Morgan had the only pontoon train in the command, and that Steele found his way blocked by Thompson's Lake, crossable only on a narrow corduroy causeway enfiladed by a Confederate battery. His division was therefore ordered to cross back in the transports and come up in support of Morgan."
- **Added citations** (both `chickasaw-bayou`, p.77): `Steele found his way blocked by Thompson's Lake` and `cross back in the transports to the other side of Chickasaw Bayou, and come up in support of Mor- gan's division`.

**VB-R6 — MS003 `bluff-and-bottomland`: a conditional qualifier is dropped and one count is uncited.**
- **Problem:** Greene's bottom land was "overflowed in the highest stages of the liver [river]", not permanently overflowed. The "five practicable crossings in twelve miles" also has no quote.
- **Replacement value:** "Greene says the bluff was fully two hundred feet high with an unbroken view of the bottom land, which was low alluvial land, overflowed at the highest river stages and filled at all times with bayous and swamps. He says there were only five practicable crossings in twelve miles, all commanded by Confederate batteries. NPS calls the Walnut Hills strongly defended."
- **Added citations** (`chickasaw-bayou`): `overflowed in the highest stages of the liver` (p.75) and `there were but five points where it was practicable to pass from the Yazoo through the network of bayous` (p.76).

## Non-blocking notes (no change required)

- **VB-N1 — Terrain claims tagged `inherited`.**
  - Both tags are acceptable as draft hypotheses relative to the engagement start. The contract treats draft phase tags as hypotheses while the boundaries are null.
  - MS003's claim, however, bundles natural ground with Confederate batteries and "strongly defended" positions. Greene says those defenses were strengthened by reinforcements Pemberton ordered on December 23–26, before the frozen interval. Under a campaign boundary, that part could be commander-created.
  - Consider adding to the rationale: "Inherited relative to the December 26 landing only; defensive preparations and reinforcement may be commander-created under a campaign boundary."
  - AR006's Fort Hindman works are pre-existing in Greene. Who built them is not inspected.
- **VB-N2 — Which "M. L. Smith".** In the selection, Greene uses "M. L. Smith" for the Union division commander and "Martin L. Smith" for the Confederate garrison commander (p.79). Writing "Union division commander M. L. Smith" would prevent confusion.
- **VB-N3 — Assaulting population.** In MS003, "the brigades bearing the December 29 assault" should include Greene's "one regiment (Fourth Iowa) of Thayer's brigade". The memo and `unsupported-assault` already state this correctly.
- **VB-N4 — Who initiated Arkansas Post.** NPS says McClernand "undertook" the movement. Greene's quoted letter says Sherman proposed it, and McClernand agreed and Porter assented. Both appear in `post-objective`. Neither should be read as sole initiative credit.
- **VB-N5 — Follow-on regeneration.** If the primary applies these corrections, it will need to regenerate the dependent packets and receipt. The memo's 62-citation count would change with the citations added in VB-R3, R5 and R6 plus any optional ones; the claim count stays at 19. The memo's historical summaries remain accurate after the corrections.

## Returned finding IDs

VB-R1, VB-R2, VB-R3, VB-R4, VB-R5, VB-R6 (required); VB-N1, VB-N2, VB-N3, VB-N4, VB-N5 (non-blocking).
