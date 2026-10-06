"""The static explorer (generalship/site.py): it builds offline and every internal link and anchor resolves."""

from html.parser import HTMLParser
from pathlib import Path
import tempfile
import unittest

from generalship.site import build_site, markdown
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
                if href.startswith(('http://', 'https://', 'mailto:')):
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
