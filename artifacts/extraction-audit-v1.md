# Extraction audit v1

A seeded random sample of 150 of the 3116 cited dossier claims (seed 20261006), each read against its cited passages. Auditor: the primary agent (Claude Opus 5.5), self-audit. A primary self-audit, not an independent extraction sample: the auditor is the same model that drafted and verified the dossiers and that ran most of their separate reviews, so errors that model makes systematically are invisible to it.

| Verdict | Claims |
|---|---:|
| correct | 142 |
| minor | 8 |
| material | 0 |

- Material errors: 0.0% (Wilson 95% interval 0.0%–2.5%).
- Any issue, material or minor: 5.3% (2.7%–10.2%).

| Dimension | Correct | Minor | Material |
|---|---:|---:|---:|
| information | 17 | 1 | 0 |
| logistics | 12 | 1 | 0 |
| objectives | 18 | 0 | 0 |
| outcome | 44 | 0 | 0 |
| responsibility | 11 | 5 | 0 |
| strength | 24 | 0 | 0 |
| terrain | 16 | 1 | 0 |

## Claims with issues

- **LA003 `rations-water-and-sickness`** (logistics, minor): Breckinridge says he ordered the enemy's camps and stores 'to be destroyed'; the claim says he burned them. The source does not give the method. Correction: Now 'ordered the enemy's camps and stores destroyed', as the report says. Dossier revision 'extraction-audit-correction-2026-10-06'; the audited version is archived at data/evidence/history/LA003.v2.json.
- **MN002 `command-roles`** (responsibility, minor): Sibley's cited report names 'The Renville Guards, under Lieutenant Gorman'; the claim calls them 'Gorman's Renville Rangers', the name used in other reports, without noting the variant. Correction: Now names the Renville Guards under Lieutenant Gorman, as Sibley's report does. Dossier revision 'extraction-audit-correction-2026-10-06'; the audited version is archived at data/evidence/history/MN002.v2.json.
- **TX001 `express-and-messenger`** (information, minor): 'or Crocker's three' compares with Crocker's report, which this claim does not cite. The dossier's other claims cite Crocker, so the point is evidenced there, but this claim carries no citation for it. Correction: Now names Crocker's Kensington and two schooners and cites Crocker's report. Dossier revision 'extraction-audit-correction-2026-10-06'; the audited version is archived at data/evidence/history/TX001.v2.json.
- **VA036 `command-roles`** (responsibility, minor): The claim says the live page gives the same commanders and ranks but cites only the frozen rows. The retained NPS snapshot does list Brigadier General Hugh Kilpatrick and Colonel Thomas Munford, so the statement is true but uncited. Correction: Cites the live page's two commander lines. Dossier revision 'extraction-audit-correction-2026-10-06'; the audited version is archived at data/evidence/history/VA036.v2.json.
- **VA058 `command-roles`** (responsibility, minor): Humphreys relays the point that Torbert's other brigades were not seriously engaged as Sheridan's ('General Sheridan says'); the claim attributes it to Humphreys alone. Correction: Now attributes the 'not seriously engaged' statement to Sheridan, as relayed by Humphreys. Dossier revision 'extraction-audit-correction-2026-10-06'; the audited version is archived at data/evidence/history/VA058.v2.json.
- **VA084 `close-lines-and-forts`** (terrain, minor): Humphreys gives the darkness statement as Parke's ('It was so dark, General Parke says'); the claim attributes it to Humphreys alone. Correction: Now attributes the darkness statement to Parke, as relayed by Humphreys. Dossier revision 'extraction-audit-correction-2026-10-06'; the audited version is archived at data/evidence/history/VA084.v2.json.
- **VA096 `command-roles`** (responsibility, minor): 'Humphreys names Walker's train' has no citation in this claim; the dossier's reported-force-scope claim cites Humphreys's 'capturing Walker's train of artillery and wagons'. Correction: Cites Humphreys's 'capturing Walker's train of artillery and wagons'. Dossier revision 'extraction-audit-correction-2026-10-06'; the audited version is archived at data/evidence/history/VA096.v2.json.
- **VA107 `command-roles`** (responsibility, minor): The claim says the live page gives the same commanders but cites only the frozen rows; the retained NPS snapshot does list Brigadier General Robert Milroy and Lieutenant General Richard Ewell. Correction: Cites the live page's two commander lines. Dossier revision 'extraction-audit-correction-2026-10-06'; the audited version is archived at data/evidence/history/VA107.v2.json.

## Protocol and limits

- Each cited quote was read in context (about 220 characters either side) and, where a detail lay outside that window, in its full cited section.
- quote_supports_claim: every element of the value is supported by the claim's own citations or by text in the cited sections.
- attribution: each statement is credited to the source that makes it, including relayed statements.
- scope_and_time: populations, units, dates and intervals match the source.
- status: supported or disputed fits what the sources show.
- Verdicts: correct (all four hold); minor (wording, relayed attribution or a missing citation, with the meaning unchanged); material (an element unsupported or contradicted, misattributed, or wrong in scope, number or date).

- Explicit unknowns were not audited; whether a dimension is truly absent from the sources is a different check.
- The audit tests extraction against the cited passages, not historical truth or the completeness of the sources inspected.
- With no material errors in 150, the true rate could still be up to about 2.5% (Wilson 95% upper bound).
- Dossier hashes are the audited versions; minor findings were corrected afterwards in versioned dossier revisions.
