"""The static explorer (generalship/site.py): it builds offline and every internal link and anchor resolves."""

from html.parser import HTMLParser
from collections import Counter
import html
from pathlib import Path
import re
import tempfile
import unittest

from generalship.site import build_site, markdown, slug
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.ids.add(a['id'])
        for key in ('href', 'src'):
            if a.get(key):
                self.hrefs.append(a[key])


class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name).resolve() / 'site'
        cls.result = build_site(ROOT, str(cls.out), 'abc123')
        cls.pages = {}
        for path in cls.out.rglob('*.html'):
            parser = Links()
            parser.feed(path.read_text(encoding='utf-8'))
            cls.pages[path] = parser

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_every_engagement_commander_and_campaign_has_a_page(self):
        cohort = read_json(ROOT / 'data/pilot/cohort-v2.json')['battle_ids']
        for b in cohort:
            self.assertTrue((self.out / f'engagements/{b}.html').is_file(), b)
        credited = {e['sides'][s]['commander_id'] for e in read_json(ROOT / 'data/command/responsibility-v2.json')['engagements']
                    for s in ('US', 'Confederate')} - {None}
        for c in credited:
            self.assertTrue((self.out / f'commanders/{c}.html').is_file(), c)
        self.assertEqual(self.result['pages'], len(self.pages))

    def test_every_internal_link_and_anchor_resolves(self):
        broken = []
        for path, parser in self.pages.items():
            for href in parser.hrefs:
                if href.startswith(('http://', 'https://', 'mailto:', 'data:')):
                    continue
                target, _, frag = href.partition('#')
                dest = (path.parent / target).resolve() if target else path
                if not dest.is_file():
                    broken.append((str(path.relative_to(self.out)), href))
                elif frag and dest.suffix == '.html' and frag not in self.pages[dest].ids:
                    broken.append((str(path.relative_to(self.out)), href))
        self.assertEqual(broken, [])

    def test_a_claim_shows_its_passage_source_and_hash(self):
        page = (self.out / 'engagements/VA111.html').read_text(encoding='utf-8')
        sha = read_json(ROOT / 'data/sources.json')['sources']
        source = next(s for s in sha if s['id'] == 'arnold-cwsac-forces')
        self.assertIn('<blockquote>8,500</blockquote>', page)
        self.assertIn(source['sha256'][:12], page)
        self.assertIn('https://github.com/masonpetrosky/generalship/blob/abc123/' + source['path'], page)

    def test_napoleonic_cohort_and_complete_groups_are_browsable(self):
        cohort = read_json(ROOT / 'data/napoleonic/cohort-v1.json')
        entries = {e['id']: e for e in read_json(ROOT / 'data/napoleonic/frame-v1.json')['entries']}
        pages = self.out / 'napoleonic'
        self.assertEqual({p.stem for p in (pages / 'engagements').glob('*.html')}, set(cohort['battle_ids']))
        self.assertEqual({p.stem for p in (pages / 'campaigns').glob('*.html')},
                         {slug(group) for group in cohort['campaign_groups']})
        index = (pages / 'engagements.html').read_text()
        for b in cohort['battle_ids']:
            group = entries[b]['campaign_group']
            self.assertIn(f'engagements/{b}.html', index)
            self.assertIn(f'engagements/{b}.html', (pages / 'campaigns' / f'{slug(group)}.html').read_text())
        overview = (pages / 'index.html').read_text()
        self.assertIn('325/325 draft dossiers', overview)
        self.assertIn('16 campaign groups', overview)

    def test_every_napoleonic_claim_preserves_value_rationale_and_passages(self):
        ids = read_json(ROOT / 'data/napoleonic/cohort-v1.json')['battle_ids']
        sources = {s['id']: s for s in read_json(ROOT / 'data/sources.json')['sources']}
        statuses = Counter()
        for b in ids:
            d = read_json(ROOT / f'data/napoleonic/evidence/{b}.json')
            path = self.out / f'napoleonic/engagements/{b}.html'
            rendered = path.read_text()
            self.assertIn('Draft claims are not admitted predictors', rendered)
            self.assertNotIn('Latest Civil War rating run', rendered)
            self.assertIn('Unestablished', rendered)
            for c in d['claims']:
                with self.subTest(battle=b, claim=c['id']):
                    self.assertIn(f'claim-{c["id"]}', self.pages[path].ids)
                    self.assertIn(html.escape(c['rationale']), rendered)
                    if c['value'] is None:
                        self.assertIn('Unknown — not established by the inspected evidence.', rendered)
                    else:
                        self.assertIn(html.escape(c['value']), rendered)
                    for cite in c['citations']:
                        src = sources[cite['source_id']]
                        self.assertIn(html.escape(cite['quote']), rendered)
                        self.assertIn(f'../../sources.html#{cite["source_id"]}', rendered)
                        self.assertIn(src['sha256'], rendered)
                        self.assertIn('/blob/abc123/' + src['path'], rendered)
                statuses[c['status']] += 1
        self.assertEqual(statuses, {'supported': 3621, 'disputed': 140, 'unknown': 1085})

    def test_napoleonic_force_labels_preserve_both_compiler_orientations(self):
        ids = set(read_json(ROOT / 'data/napoleonic/cohort-v1.json')['battle_ids'])
        entries = [e for e in read_json(ROOT / 'data/napoleonic/frame-v1.json')['entries'] if e['id'] in ids]
        for orientation in ['winner', 'loser']:
            e = next(e for e in entries if e['french_side'] == orientation)
            page = (self.out / f'napoleonic/engagements/{e["id"]}.html').read_text()
            self.assertIn('<td>A</td><td>' + html.escape(e[f'{orientation}_text']), page)
            self.assertIn('not resolved identities, selected opening strengths or automatic command credit', page)

    def test_measurement_comparisons_cover_exactly_the_two_complete_pilots(self):
        ids = {'B370c', 'B370d', 'B371a', 'B379c', 'B430a', 'B430b', 'B430c', 'B431a',
               'B431b', 'B432a', 'B432b', 'B441a'}
        pages = self.out / 'napoleonic/comparisons'
        self.assertEqual({p.stem for p in pages.glob('*.html')}, ids | {'index'})
        index = (pages / 'index.html').read_text()
        self.assertIn('12 engagements · 24 sides', index)
        self.assertIn('do not estimate corpus-wide feasibility', index)
        for b in read_json(ROOT / 'data/napoleonic/cohort-v1.json')['battle_ids']:
            dossier = (self.out / f'napoleonic/engagements/{b}.html').read_text()
            self.assertEqual(f'../comparisons/{b}.html' in dossier, b in ids)
            if b in ids:
                self.assertIn(f'{b}.html', index)
                page = (pages / f'{b}.html').read_text()
                self.assertIn('both opening mappings unresolved', page)
                self.assertIn('select no model input or commander credit', page)
                self.assertIn('mapping-A', self.pages[pages / f'{b}.html'].ids)
                self.assertIn('mapping-B', self.pages[pages / f'{b}.html'].ids)
                self.assertNotIn('>None<', page)
        self.assertIn('comparisons/index.html', (self.out / 'napoleonic/index.html').read_text())

    def comparison_card(self, battle, observation):
        page = (self.out / f'napoleonic/comparisons/{battle}.html').read_text()
        match = re.search(r'<article class="observation" id="observation-' + re.escape(observation) + r'">(.*?)</article>',
                          page, re.S)
        self.assertIsNotNone(match, (battle, observation))
        return match.group(1), page

    def test_comparisons_keep_every_strength_population_time_and_explicit_gap(self):
        ledger = read_json(ROOT / 'data/napoleonic/ledger-design-v1/examples.json')
        peninsula = read_json(ROOT / 'data/napoleonic/peninsula-1812-measurement-v1/records.json')
        observations = ledger['strength_records'] + [r for r in peninsula['observations'] if r['kind'] == 'strength']
        unknowns = 0
        for r in observations:
            card, page = self.comparison_card(r['battle_id'], r['id'])
            for key in ('population', 'basis', 'state_description', 'boundary_relation', 'derivation',
                        'population_or_scope', 'reported_time', 'source_role', 'note'):
                if r.get(key):
                    self.assertIn(html.escape(r[key]), card, (r['id'], key))
            missing = r['amount']['kind'] == 'unknown' if 'amount' in r else r['value'] is None
            if missing:
                unknowns += 1
                self.assertIn('<h4>Unknown people</h4>', card)
                self.assertNotIn('<h4>0 people</h4>', card)
            for ref in re.findall(r'href="#(passage-\d+)"', card):
                self.assertIn(ref, self.pages[self.out / f'napoleonic/comparisons/{r["battle_id"]}.html'].ids)
        self.assertEqual(len(observations), 82)
        self.assertEqual(unknowns, 9)
        # Source precision, equipment and inhabitants must survive the shared display path.
        for b, rid, label in [('B370d', 'B370d-A-bunbury-more-than', '&gt; 6,000 people'),
                              ('B371a', 'B371a-A-koch-lacour-bound', '≤ 2,400 people'),
                              ('B371a', 'B371a-B-koch-garrison-bound', '&lt; 6,000 people'),
                              ('B379c', 'B379c-B-koch-guns', '4–5 guns'),
                              ('B432b', 'B432b-A-s02', 'About 48,500 people')]:
            card, _ = self.comparison_card(b, rid)
            self.assertIn(f'<h4>{label}</h4>', card)
        inhabitants, _ = self.comparison_card('B379c', 'B379c-B-colletta-inhabitants')
        self.assertIn('town_population', inhabitants)
        self.assertIn('not established as defenders', inhabitants)

    def test_comparisons_keep_every_authority_scope_and_unresolved_identity(self):
        authority = read_json(ROOT / 'data/napoleonic/authority-v1/mappings.json')
        peninsula = read_json(ROOT / 'data/napoleonic/peninsula-1812-measurement-v1/records.json')
        roles = authority['roles'] + [r for r in peninsula['observations'] if r['kind'] == 'authority']
        self.assertEqual(len(roles), 73)
        for r in roles:
            card, _ = self.comparison_card(r['battle_id'], r['id'])
            for key in ('actor_label', 'authority_type', 'force_scope', 'population_or_scope', 'reported_time', 'note'):
                if key in r:
                    self.assertIn(html.escape(r[key]), card, (r['id'], key))
            self.assertIn('<dt>Resolved person identity</dt><dd><span class="muted">Unestablished</span>', card)
        franceschi, _ = self.comparison_card('B371a', 'B371a-A-capitulation-franceschi')
        self.assertIn('delegated_negotiation', franceschi)
        self.assertIn('do not establish exclusive siege command', franceschi)

    def test_comparison_observations_link_to_their_own_exact_passages_and_hashes(self):
        sources = {s['id']: s for s in read_json(ROOT / 'data/sources.json')['sources']}
        ledger = read_json(ROOT / 'data/napoleonic/ledger-design-v1/examples.json')
        authority = read_json(ROOT / 'data/napoleonic/authority-v1/mappings.json')
        peninsula = read_json(ROOT / 'data/napoleonic/peninsula-1812-measurement-v1/records.json')
        groups = [(ledger['strength_records'], None), (authority['roles'], authority['passages']),
                  (peninsula['observations'], peninsula['passages'])]
        for records, passages in groups:
            indexed = {p['id']: p for p in passages} if passages else None
            for r in records:
                card, page = self.comparison_card(r['battle_id'], r['id'])
                linked = [re.search(r'<article class="passage" id="' + pid + r'">(.*?)</article>', page, re.S).group(1)
                          for pid in re.findall(r'href="#(passage-\d+)"', card)]
                for evidence in r['evidence']:
                    passage = indexed[evidence] if indexed else evidence
                    cite = passage['citation']
                    src = sources[cite['source_id']]
                    matches = [p for p in linked if '<blockquote>' + html.escape(cite['quote']) + '</blockquote>' in p
                               and html.escape(cite['source_id']) in p and html.escape(cite['locator']) in p]
                    self.assertTrue(matches, r['id'])
                    block = matches[0]
                    self.assertIn(src['sha256'], block)
                    self.assertIn('/blob/abc123/' + src['path'], block)
                    image_id = passage.get('facsimile_source_id') or passage.get('image_source_id')
                    if image_id:
                        image = sources[image_id]
                        self.assertIn(image['sha256'], block)
                        self.assertIn('/blob/abc123/' + image['path'], block)
                if not r['evidence']:
                    self.assertIn('Explicit evidence gap; no supporting passage indexed.', card)

    def test_comparison_findings_preserve_disagreements_and_non_admitted_arithmetic(self):
        ledger = read_json(ROOT / 'data/napoleonic/ledger-design-v1/examples.json')
        authority = read_json(ROOT / 'data/napoleonic/authority-v1/mappings.json')
        boundaries = read_json(ROOT / 'data/napoleonic/boundaries-v1/records.json')
        peninsula = read_json(ROOT / 'data/napoleonic/peninsula-1812-measurement-v1/records.json')
        for records in (ledger['discrepancies'], ledger['sum_proposals'], authority['reconciliations'],
                        boundaries['scenarios'], boundaries['membership_cases'], peninsula['co_reports'], peninsula['arithmetic_checks']):
            for r in records:
                path = self.out / f'napoleonic/comparisons/{r["battle_id"]}.html'
                self.assertIn('record-' + r['id'], self.pages[path].ids)
                if r.get('note'):
                    self.assertIn(html.escape(r['note']), path.read_text())
        rodrigo = (self.out / 'napoleonic/comparisons/B430a.html').read_text()
        self.assertIn('Not a candidate strength.', rodrigo)
        self.assertIn('No local strength-role association indexed for this entry.', rodrigo)
        gaeta = (self.out / 'napoleonic/comparisons/B371a.html').read_text()
        self.assertIn('same-side status', gaeta.lower())
        self.assertIn('Source labels', gaeta)

    def test_source_counts_include_both_research_cohorts(self):
        class SourceRows(HTMLParser):
            def __init__(self):
                super().__init__()
                self.rows, self.row, self.cell = [], None, None

            def handle_starttag(self, tag, attrs):
                if tag == 'tr':
                    self.row = []
                elif tag == 'td':
                    self.cell = []

            def handle_data(self, data):
                if self.cell is not None:
                    self.cell.append(data)

            def handle_endtag(self, tag):
                if tag == 'td':
                    self.row.append(''.join(self.cell))
                    self.cell = None
                elif tag == 'tr' and self.row:
                    self.rows.append(self.row)

        expected = Counter()
        for cohort_path, directory in [('data/pilot/cohort-v2.json', 'data/evidence'),
                                       ('data/napoleonic/cohort-v1.json', 'data/napoleonic/evidence')]:
            for b in read_json(ROOT / cohort_path)['battle_ids']:
                d = read_json(ROOT / directory / f'{b}.json')
                expected.update(c['source_id'] for claim in d['claims'] for c in claim['citations'])
        parsed = SourceRows()
        parsed.feed((self.out / 'sources.html').read_text())
        counts = {row[0]: int(row[4]) for row in parsed.rows}
        for sid, count in expected.items():
            self.assertEqual(counts[sid], count, sid)
        self.assertEqual(sum(counts.values()), sum(expected.values()))


class MarkdownTests(unittest.TestCase):
    def test_tables_lists_and_links(self):
        out = markdown('# T\n\n| A | B |\n| --- | ---: |\n| x | 1 |\n\n- one\n  - two\n- three [l](docs/x.md)\n', lambda t: 'L:' + t)
        self.assertIn('<h1 id="t">T</h1>', out)
        self.assertIn('<td class=n>1</td>', out)
        self.assertIn('<ul><li>one<ul><li>two</li></ul></li><li>three <a href="L:docs/x.md">l</a></li></ul>', out)

    def test_text_is_escaped(self):
        self.assertIn('&lt;script&gt;', markdown('a <script> b', lambda t: t))


if __name__ == '__main__':
    unittest.main()
