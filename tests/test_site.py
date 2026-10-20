"""The static explorer (generalship/site.py): it builds offline and every internal link and anchor resolves."""

from html.parser import HTMLParser
from collections import Counter
import html
from pathlib import Path
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
