"""Metadata-only temporal planning and immutable proposal checks."""

import copy
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

from generalship import napoleonic_temporal_calibration as prep
from generalship import napoleonic_temporal_calibration_run as run
from generalship.sources import digest, read_json

ROOT = Path(__file__).resolve().parents[1]


def constructed():
    rows, labels = [], {}
    for prefix, year in [('B', 1805), ('C', 1806), ('T', 1808)]:
        for i in range(10):
            b = prefix + str(i)
            rows.append({'battle_id': b, 'campaign_group': f'{prefix} {year}', 'start_year': year,
                         'start_date': f'{year}-01-01', 'end_date': f'{year}-12-31', 'eligible': True,
                         'sides': {'A': {'primary_value': 60 + i * 12}, 'B': {'primary_value': 100}}})
            labels[b] = int(i >= 3) if prefix == 'C' else i % 2
    return rows, labels


class TemporalBoundaryTests(unittest.TestCase):
    def test_ineligible_late_or_unknown_member_defers_the_whole_group(self):
        for end in ('1808-01-01', None):
            rows, _ = constructed()
            late = dict(rows[10], battle_id='ineligible', end_date=end, eligible=False)
            rows.append(late)
            fs = prep.folds(rows, [r for r in rows if r['eligible']], prep.fixed_protocol())
            fold = next(f for f in fs if f['target_year'] == 1808)
            self.assertIn('C 1806', fold['deferred_earlier_groups'])
            self.assertFalse(set(fold['expanding_ids']) & {f'C{i}' for i in range(10)})
            self.assertEqual(fold['status'], 'not_estimable')

    def test_base_must_finish_before_calibration_begins_with_no_fallback(self):
        for start, reason in [(None, 'unknown_calibration_start'),
                              ('1805-12-20', 'base_not_complete_before_calibration_start')]:
            rows, _ = constructed(); rows[10]['start_date'] = start
            fold = next(f for f in prep.folds(rows, rows, prep.fixed_protocol()) if f['target_year'] == 1808)
            self.assertEqual(fold['status'], 'not_estimable')
            self.assertIn(reason, fold['reasons'])
            self.assertEqual(fold['calibration_groups'], ['C 1806'])

    def test_duplicate_or_split_source_group_is_rejected(self):
        rows, _ = constructed()
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            prep.group_metadata(rows + [rows[0]])
        rows[0]['start_year'] = 1804
        with self.assertRaisesRegex(ValueError, 'cohort years'):
            prep.group_metadata(rows)


class PreparedPlanTests(unittest.TestCase):
    def test_full_plan_reconciles_without_labels_or_fits(self):
        protected = [ROOT / prep.RESULT, ROOT / (prep.BASE + 'owner-run-authorization.json')]
        before = [digest(p) if p.exists() else None for p in protected]
        with patch.object(run, 'load_outcomes') as labels, patch.object(run, 'fit_logistic') as force, \
                patch.object(run, 'fit_offset') as offset:
            result = prep.check(ROOT)
        labels.assert_not_called(); force.assert_not_called(); offset.assert_not_called()
        self.assertEqual(result['planned_parameter_fits'], 72)
        plan = read_json(ROOT / (prep.ARTIFACT + '.json'))
        primary = plan['populations']['primary']['regions']
        self.assertEqual([primary[k]['all_entries'] for k in ('warmup', 'decision', 'reused_1813_secondary')], [68, 141, 64])
        self.assertEqual([primary[k]['planned_scored_entries'] for k in ('warmup', 'decision', 'reused_1813_secondary')], [0, 115, 37])
        self.assertEqual(len(primary['decision']['groups']), 7)
        scope = read_json(ROOT / prep.SCOPE)
        data = {r['battle_id']: r for r in read_json(ROOT / prep.DATA)['entries']}
        self.assertEqual(len(data), 273)
        self.assertFalse(set(scope['reserved_final_ids']) & data.keys())
        for p in plan['populations'].values():
            for fold in p['folds']:
                self.assertFalse(set(fold['base_ids']) & set(fold['calibration_ids']))
                self.assertFalse(set(fold['expanding_ids']) & set(fold['test_ids']))
                if fold['status'] == 'planned':
                    self.assertTrue(all(data[b]['end_date'] < fold['calibration_start'] for b in fold['base_ids']))
                    self.assertTrue(all(data[b]['end_date'] < fold['cutoff'] for b in fold['expanding_ids']))
                    self.assertTrue(all(data[b]['start_date'] >= fold['cutoff'] for b in fold['test_ids']))
        self.assertEqual(before, [digest(p) if p.exists() else None for p in protected])

    def test_changed_source_binding_or_proposal_is_rejected(self):
        read = prep.read_json
        scope = copy.deepcopy(read(ROOT / prep.SCOPE))
        scope['bindings']['data/napoleonic/frame-v1.json'] = '0' * 64
        with patch.object(prep, 'read_json', side_effect=lambda p: scope if p == ROOT / prep.SCOPE else read(p)):
            with self.assertRaisesRegex(ValueError, 'changed frozen input'):
                prep.build(ROOT)
        bad = copy.deepcopy(read(ROOT / prep.PROPOSAL)); bad['bindings'][prep.RUN_CODE] = '0' * 64
        with patch.object(prep, 'read_json', return_value=bad):
            with self.assertRaisesRegex(ValueError, 'changed proposal'):
                prep.validate_proposal(ROOT)

    def test_reproduction_restores_only_frozen_output_bytes(self):
        proposal = read_json(ROOT / prep.PROPOSAL)
        scope = read_json(ROOT / prep.SCOPE)
        old = read_json(ROOT / prep.benchmark.PROPOSAL)
        paths = set(proposal['bindings']) | set(scope['bindings']) | set(old['bindings']) | {prep.PROPOSAL}
        outputs = [prep.ARTIFACT + '.json', prep.ARTIFACT + '.md']
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for path in paths - set(outputs):
                (root / path).parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / path, root / path)
            prep.write_artifacts(root)
            self.assertEqual(prep.check(root)['planned_parameter_fits'], 72)
            (root / outputs[1]).write_text('corrupt output')
            prep.write_artifacts(root)
            self.assertTrue(all(digest(root / path) == proposal['bindings'][path] for path in outputs))
            with patch.object(prep, 'report', return_value='changed generated bytes'):
                with self.assertRaisesRegex(ValueError, 'differs from frozen proposal'):
                    prep.write_artifacts(root)
            self.assertEqual(digest(root / outputs[1]), proposal['bindings'][outputs[1]])


if __name__ == '__main__':
    unittest.main()
