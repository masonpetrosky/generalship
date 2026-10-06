"""The Napoleonic frame v1 built from the Bodart transcription (generalship/napoleonic.py, docs/napoleonic-frame.md)."""

from pathlib import Path
import json
import shutil
import tempfile
import unittest

import generalship.napoleonic as nap
from generalship.sources import digest, read_json

ROOT = Path(__file__).resolve().parents[1]


class NapoleonicFrameTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.frame = nap.build(ROOT)
        cls.by_id = {r['id']: r for r in cls.frame['entries']}

    def test_committed_frame_and_cohort_rebuild(self):
        self.assertEqual(nap.check(ROOT), self.frame['counts'])
        cohort = read_json(ROOT / nap.COHORT)
        self.assertEqual(cohort['frame_sha256'], digest(ROOT / nap.FRAME))

    def test_ids_are_unique_and_follow_page_and_position(self):
        ids = [r['id'] for r in self.frame['entries']]
        self.assertEqual(len(ids), len(set(ids)))
        for r in self.frame['entries']:
            self.assertRegex(r['id'], r'^B\d{3}[a-z]$')
            self.assertEqual(int(r['id'][1:4]), r['page'])

    def test_known_entries(self):
        expected = {  # id: (place, war, French side), read from the page images
            'B269c': ('Valmy', 'first-coalition', 'winner'),
            'B316a': ('Caldiero', 'first-coalition', 'loser'),
            'B355c': ('Marengo', 'second-coalition', 'winner'),
            'B367a': ('Caldiero', 'third-coalition', 'loser'),
            'B369c': ('Austerlitz', 'third-coalition', 'winner'),
            'B372a': ('Jena', 'fourth-coalition', 'winner'),
            'B388a': ('Bailén', 'peninsula', 'loser'),
            'B405a': ('Aspern und Eßling', 'fifth-coalition', 'loser'),
            'B438a': ('Borodino', 'russia-1812', 'winner'),
            'B461a': ('Leipzig', 'liberation', 'loser'),
            'B487a': ('Waterloo', 'hundred-days-1815', 'loser'),
        }
        for i, (place, war, side) in expected.items():
            r = self.by_id[i]
            self.assertEqual((r['place'], r['war'], r['french_side']), (place, war, side), i)
            self.assertEqual(r['outcome_side_a'], int(side == 'winner'))

    def test_every_in_frame_entry_has_a_french_side_and_a_campaign_group(self):
        for r in self.frame['entries']:
            if r['in_frame']:
                self.assertIn(r['french_side'], ('winner', 'loser'), r['id'])
                self.assertTrue(r['side_a_basis'], r['id'])
                self.assertEqual(r['campaign_group'], f"{r['war']} {r['start_year']}")
                self.assertTrue(nap.WARS[r['war']][1])
            else:
                self.assertIsNone(r['french_side'])
                self.assertTrue(r['out_of_frame_reason'], r['id'])

    def test_counts_and_denominators_are_consistent(self):
        c = self.frame['counts']
        self.assertEqual(c['entries_transcribed'], len(self.frame['entries']))
        self.assertEqual(c['in_frame'] + sum(c['out_of_frame_by_reason'].values()), c['entries_transcribed'])
        self.assertEqual(sum(c['in_frame_by_war'].values()), c['in_frame'])
        self.assertEqual(sum(c['side_a_basis'].values()), c['in_frame'])
        cohort = nap.cohort(self.frame, 'x')
        self.assertEqual(sum(cohort['campaign_groups'].values()), cohort['counts']['entries'])
        for i in cohort['battle_ids']:
            r = self.by_id[i]
            self.assertTrue(r['in_frame'] and not r['naval'] and 1805 <= r['start_year'] <= 1815, i)

    def test_misprints_are_corrected_only_by_recorded_overrides(self):
        self.assertEqual(self.by_id['B367b']['year_printed'], '1905')
        self.assertEqual(self.by_id['B367b']['start_date'], '1805-11-02')
        self.assertIn('year_override', self.by_id['B367b']['date_flags'])
        self.assertEqual(self.by_id['B459a']['start_year'], 1813)
        self.assertIsNone(self.by_id['B269d']['start_date'])  # printed 31./9., flagged and not corrected
        self.assertIn('impossible_printed_date', self.by_id['B269d']['date_flags'])
        for r in self.frame['entries']:
            if r['war_basis'] == 'override' or r['side_a_basis'] == 'override' or 'year_override' in r['date_flags']:
                self.assertTrue(r['override_reason'], r['id'])

    def test_prose_forms_put_the_winner_where_the_grammar_does(self):
        cases = {
            'Vor 800 französischen Husaren unter Brig.-Gen. Gf. Lasalle kapituliert ohne Schwertstreich die von 5.300 Preußen '
            'unter GM. v. Romberg besetzte Festung.': (['FR'], ['PR'], 'GM. v. Romberg'),
            'Die preußische Garnison (1.000 M.) unter Major v. Benekendorf ergibt sich ohne Schwertstreich an die Franzosen '
            'unter Marschall Lannes.': (['FR'], ['PR'], 'Major v. Benekendorf'),
            'Sieg der Franzosen (ca. 12.000 M.) unter Marschall Masséna über die Österreicher (ca. 4.000 M.) unter GM. Hillinger.':
                (['FR'], ['AT'], 'GM. Hillinger'),
            'Die Engländer (16.000 M.) zwingen die französische Garnison (4.500 M.) zur Übergabe, wonach die Besatzung '
            'den Franzosen übergeben wurde.': (['GB'], ['FR'], None),
        }
        for par, (w, l, lc) in cases.items():
            s = nap.sides({'text': [par]})
            self.assertEqual((s['winner_nations'], s['loser_nations'], s['loser_commander_text']), (w, l, lc), par)

    def test_a_side_named_only_in_a_later_clause_is_flagged_for_review(self):
        s = nap.sides({'text': ['Die Franzosen (14.000 M.) unter Div.-Gen. Moreau bemächtigen sich des Platzes, nachdem ein Teil '
                                'der hannoverschen Besatzung (urspr. 2.000 M.) unter GM. Fh. v. Hammerstein sich durchgeschlagen.']})
        self.assertEqual((s['winner_nations'], s['loser_nations']), (['FR'], ['HAN']))
        self.assertEqual(s['method'], 'subject_verb+loser_later_clause')
        flagged = sorted(r['id'] for r in self.frame['entries'] if 'later_clause' in r['side_method'])
        self.assertEqual(flagged, ['B287d', 'B293c', 'B427c', 'B482c'])  # each checked against its printed paragraph

    def test_royalists_are_not_the_french_side(self):
        self.assertEqual(nap.nations('französischen Royalisten (Vendéer)'), ['VEN'])
        self.assertEqual(self.by_id['B274a']['french_side'], 'loser')

    def test_an_undecided_entry_or_a_bad_override_stops_the_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for rel in (nap.TRANSCRIPTION, nap.OVERRIDES, nap.DESIGN, nap.CODE):
                (root / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(ROOT / rel, root / rel)
            overrides = read_json(root / nap.OVERRIDES)
            overrides['entries'] = [o for o in overrides['entries'] if o['id'] != 'B371b']  # Saalfeld under the Naples head
            (root / nap.OVERRIDES).write_text(json.dumps(overrides), encoding='utf-8')
            with self.assertRaisesRegex(nap.FrameError, r'B371b: opponents'):
                nap.build(root)
            overrides['entries'].append({'id': 'B371b', 'war': 'fourth-coalition'})  # no reason
            (root / nap.OVERRIDES).write_text(json.dumps(overrides), encoding='utf-8')
            with self.assertRaisesRegex(nap.FrameError, 'malformed override B371b'):
                nap.build(root)


if __name__ == '__main__':
    unittest.main()
