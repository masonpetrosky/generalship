"""Review-record index and extraction audit (generalship/audit.py)."""

import copy
from pathlib import Path
import unittest

from generalship import audit as a
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]


class ReviewIndexTests(unittest.TestCase):
    def test_every_historical_disposition_is_in_the_vocabulary(self):
        index = a.review_index(ROOT)
        self.assertTrue(set(index['totals']) <= set(a.VOCABULARY))
        self.assertTrue(set(a.DISPOSITIONS.values()) <= set(a.VOCABULARY))
        counted = sum(r.get('findings', 0) for r in index['reviews'])
        self.assertEqual(counted, sum(index['totals'].values()))

    def test_both_record_shapes_and_unknown_dispositions(self):
        self.assertEqual(len(a.findings({'findings': [{'disposition': 'adopted'}, {'disposition': 'deferred'}]})), 2)
        self.assertEqual(len(a.findings({'finding_id': 'R1', 'disposition': 'adopted'})), 1)
        with self.assertRaises(a.AuditError):
            a.findings({'summary': 'no finding here'})


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.audit = read_json(ROOT / a.AUDIT)

    def test_committed_audit_matches_its_seeded_sample(self):
        s = a.check_audit(ROOT, self.audit)
        self.assertEqual(s['audited'], self.audit['sample_size'])
        self.assertEqual(sum(s['verdicts'].values()), s['audited'])

    def test_tampered_audits_fail(self):
        bad = copy.deepcopy(self.audit)
        bad['judgments'][0]['verdict'] = 'fine'
        with self.assertRaises(a.AuditError):
            a.check_audit(ROOT, bad)
        bad = copy.deepcopy(self.audit)
        bad['judgments'][0], bad['judgments'][1] = bad['judgments'][1], bad['judgments'][0]
        with self.assertRaises(a.AuditError):
            a.check_audit(ROOT, bad)
        bad = copy.deepcopy(self.audit)
        j = next(j for j in bad['judgments'] if j['verdict'] == 'correct' and not j['note'])
        j['verdict'] = 'material'
        with self.assertRaises(a.AuditError):  # a material verdict needs a note
            a.check_audit(ROOT, bad)
        bad = copy.deepcopy(self.audit)
        bad['judgments'][0]['dossier_sha256'] = '0' * 64
        with self.assertRaises(a.AuditError):
            a.check_audit(ROOT, bad)

    def test_wilson_interval(self):
        self.assertEqual(a.wilson(0, 150)[0], 0.0)
        lo, hi = a.wilson(8, 150)
        self.assertLess(lo, 8 / 150)
        self.assertLess(8 / 150, hi)
        self.assertEqual(a.wilson(5, 5)[1], 1.0)
