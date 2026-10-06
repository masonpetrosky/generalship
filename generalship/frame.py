"""War frame profiles: everything the rating and grade E code needs to know about one war.

A profile names the two sides, how a frozen result maps to a binary outcome, the period and
theater predictors, the echelon levels, the files a run binds and the descriptive temporal split.
The model code reads these instead of hardcoding one war (docs/commander-ratings-v4.md §10).
Profiles are data; a new war adds a profile, not a new copy of the model code.
"""

from .sources import read_csv, safe_path

CIVIL_WAR = {
    'name': 'american-civil-war',
    # Side A is the positive class of every outcome and force ratio; side B is the other side.
    'sides': ('US', 'Confederate'),
    # Frozen CWSAC result strings that decide a binary row; anything else is not a decisive row.
    'outcomes': {'Union': 1, 'Confederate': 0},
    'battles': 'data/raw/cwsac_battles.csv',
    'campaigns': 'data/raw/cwsac_campaigns.csv',
    'cohort': 'data/pilot/cohort-v2.json',
    'strength_ledger': 'data/estimates/side-strength-v3.json',
    'command_ledger': 'data/command/responsibility-v2.json',
    'registry': 'data/command/commanders-v2.json',
    # Grade E predictors (docs/strength-imputation.md §2), with their reference levels.
    'echelons': ('army', 'corps_or_wing', 'division', 'brigade', 'regiment', 'detachment_or_post', 'flotilla', 'unknown'),
    'periods': (('1861-1862', 1861, 1862), ('1863', 1863, 1863), ('1864-1865', 1864, 1865)),
    'theaters': ('Eastern', 'Western', 'Trans-Mississippi', 'Lower Seaboard', 'Pacific Coast'),
    'reference': {'echelon': 'unknown', 'side': 'US', 'period': '1863', 'theater': 'Eastern'},
    'temporal_split': (('1861', '1862', '1863'), ('1864', '1865')),
}


def period(profile, start_date):
    year = int(start_date[:4])
    for label, first, last in profile['periods']:
        if first <= year <= last:
            return label
    raise ValueError(f'{start_date}: outside the profile periods')


def period_labels(profile):
    return tuple(label for label, _, _ in profile['periods'])


def battles(root, profile):
    return {r['battle']: r for r in read_csv(safe_path(root, profile['battles']))}


def theaters(root, profile):
    return {r['campaign']: r['theater'] for r in read_csv(safe_path(root, profile['campaigns']))}


def outcome(profile, result):
    """1 if side A won, 0 if side B won, None for an undecided or unmapped result."""
    return profile['outcomes'].get(result)
