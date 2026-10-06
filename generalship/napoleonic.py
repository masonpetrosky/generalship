"""The Napoleonic frame v1: Bodart's entries for 1792-1815 in the wars France fought (docs/napoleonic-frame.md).

The frame is built mechanically from the registered transcription (bodart-1908-transcription-v1). A small
override file records, with reasons, the cases the rules cannot decide (a misprinted year or running head, an
entry whose French side the text does not settle, an engagement France took no part in). The checker rebuilds
the frame and the cohort and compares them with the committed files. Nothing here admits a feature, fits a
model or changes any Civil War input.
"""

from collections import Counter
from datetime import date
import re

from .sources import digest, read_json, safe_path, text_sections

TRANSCRIPTION = 'data/raw/bodart-1908-v1/transcription.txt'
OVERRIDES = 'data/napoleonic/frame-overrides-v1.json'
FRAME = 'data/napoleonic/frame-v1.json'
COHORT = 'data/napoleonic/cohort-v1.json'
DESIGN = 'docs/napoleonic-frame.md'
CODE = 'generalship/napoleonic.py'
FIRST_PAGE, LAST_PAGE = 268, 490
FRAME_YEARS = (1792, 1815)
COHORT_YEARS = (1805, 1815)


class FrameError(ValueError):
    """Malformed transcription, an undecided entry, or a frame that does not rebuild."""


# ---------- headers ----------

TYPEWORD = r'[A-ZÄÖÜ][A-ZÄÖÜß\-]{2,}'
HEADER = re.compile(
    r'^(?P<year>1\d{3})\s+(?P<date>(?:April\s+bis\s+\d{4}\s+)?[\d.,/—\- ]+?(?:\s+bis\s+\d{4}\s+[\d.,/—\- ]+?)?)\s+'
    r'(?P<type>(?:[A-ZÄÖÜ][a-zäöüß]+\s+)?' + TYPEWORD + r'(?:(?:,?\s+(?:und|u\.)\s+|,\s*|\s+)' + TYPEWORD + r')*)\s+'
    r'(?P<conn>bei|von|vor|beim|am|an|auf|zu|um|in|im|der|des)\s+(?P<place>.+?)$')
CATEGORY = re.compile(r'\((\d)\.\)')
FOOTNOTE = re.compile(r'^\[(\d)\]\s')


def pages(text):
    secs = text_sections(text)
    out = []
    for name, body in secs.items():
        m = re.fullmatch(r'p(\d{3})', name)
        if m and FIRST_PAGE <= int(m.group(1)) <= LAST_PAGE:
            out.append((int(m.group(1)), body))
    return sorted(out)


def blocks(body):
    out, cur = [], []
    for line in body.split('\n'):
        if line.strip():
            cur.append(line.strip())
        elif cur:
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def split_header(line):
    m = HEADER.match(line)
    if not m:
        return None
    place_full, typ, conn = m.group('place'), m.group('type').strip(), m.group('conn')
    inner = re.match(r'^(.*?\b' + TYPEWORD + r')\s+(bei|von|vor|beim|am|an|auf|zu|um|in|im)\s+(.+)$', place_full)
    if inner:  # 'ERSTÜRMUNG des verschanzten Lagers und KAPITULATION von Glatz'
        typ, conn, place_full = f'{typ} {conn} {inner.group(1)}', inner.group(2), inner.group(3)
    cat = CATEGORY.search(place_full)
    place = place_full.split(' (')[0].strip()
    alt = [a.strip() for a in re.findall(r'\(([^()]*)\)', place_full) if not re.fullmatch(r'\d\.', a.strip())]
    return {'year_printed': m.group('year'), 'date_printed': m.group('date').strip(), 'type_printed': typ,
            'connector': conn, 'place': place, 'category': int(cat.group(1)) if cat else None,
            'alternative_names': alt}


def entries(text):
    """Every entry on pp. 268-490 with its page, running head, header fields, location and text."""
    out = []
    for n, body in pages(text):
        bl = blocks(body)
        head = bl[0] if bl and not split_header(bl[0][0]) and bl[0][0] != '[continued]' else []
        rest = bl[1:] if head else bl
        notes = [l for b in rest for l in b if FOOTNOTE.match(l)]
        letter = 0
        for b in rest:
            b = [l for l in b if not FOOTNOTE.match(l)]
            if not b:
                continue
            if b[0] == '[continued]':
                if not out:
                    raise FrameError(f'p{n}: a continuation with no entry before it')
                out[-1]['text'] += b[1:]
                out[-1]['pages'].append(n)
                continue
            h = split_header(b[0])
            if h is None:
                if out and out[-1]['pages'][-1] == n:
                    out[-1]['text'] += b
                    continue
                raise FrameError(f'p{n}: unparsed entry header {b[0][:60]!r}')
            lines = b[1:]
            alt_line = lines[0] if lines and re.fullmatch(r'\([^()]*\)', lines[0]) and not re.search(r'\b(Stadt|Dorf|Ort|Festung|Fluß|Marktflecken|Insel|Hafen|Gebirg|Berg|Kap|See|Bai|Burg|Schloß|Kloster|Gegend|Provinz|Dep)\b', lines[0]) else None
            if alt_line:
                h['alternative_names'].append(alt_line.strip('()'))
                lines = lines[1:]
            location = lines[0] if lines and lines[0].startswith('(') else None
            out.append({'id': f'B{n:03d}{chr(97 + letter)}', 'page': n, 'pages': [n], 'running_head': ' / '.join(head), **h,
                        'location': location, 'text': lines[1:] if location else lines, 'page_notes': notes})
            letter += 1
    return out


# ---------- dates ----------

def parse_dates(year, printed):
    """(start, end, flags) from Bodart's date text; impossible dates are flagged, never corrected."""
    flags = []
    t = printed.replace(' ', '').replace('—', '-').rstrip(',')
    m = re.fullmatch(r'Aprilbis(\d{4})(\d+)\./(\d+)\.?', printed.replace(' ', ''))
    if m:
        return (year, 4, None), (int(m.group(1)), int(m.group(3)), int(m.group(2))), ['start_day_not_printed']
    m = re.fullmatch(r'(\d+)\./(\d+)\.?bis(\d{4})(\d+)\./(\d+)\.?', t)
    if m:
        return (year, int(m.group(2)), int(m.group(1))), (int(m.group(3)), int(m.group(5)), int(m.group(4))), flags
    m = re.fullmatch(r'(\d+)\./(\d+)\.?-(\d+)\./(\d+)\.?', t)
    if m:
        start, end = (year, int(m.group(2)), int(m.group(1))), (year, int(m.group(4)), int(m.group(3)))
        if end[1] < start[1]:
            end = (year + 1, end[1], end[2])
            flags.append('range_crosses_new_year')
        return start, end, flags
    m = re.fullmatch(r'(\d+)\.-(\d+)\./(\d+)\.?', t)
    if m:
        return (year, int(m.group(3)), int(m.group(1))), (year, int(m.group(3)), int(m.group(2))), flags
    m = re.fullmatch(r'(\d+)\.,(\d+)\./(\d+)\.?', t)
    if m:
        return (year, int(m.group(3)), int(m.group(1))), (year, int(m.group(3)), int(m.group(2))), flags
    m = re.fullmatch(r'(\d+)\./(\d+)\.?,(\d+)\./(\d+)\.?', t)
    if m:
        return (year, int(m.group(2)), int(m.group(1))), (year, int(m.group(4)), int(m.group(3))), flags
    m = re.fullmatch(r'(\d+)\.,(\d+)\./(\d+)\.,(\d+)\./(\d+)\.?', t)
    if m:
        return (year, int(m.group(3)), int(m.group(1))), (year, int(m.group(5)), int(m.group(4))), flags
    m = re.fullmatch(r'(\d+)\./(\d+)\.?', t)
    if m:
        d = (year, int(m.group(2)), int(m.group(1)))
        return d, d, flags
    raise FrameError(f'unparsed date {printed!r}')


def iso(d):
    y, m, dd = d
    if dd is None:
        return None
    try:
        return date(y, m, dd).isoformat()
    except ValueError:
        return None


# ---------- nations ----------

def either_case(pattern):
    """Let each alternative open in either case: adjectives also begin sentences and table headings."""
    return '|'.join(f'[{a[0].upper()}{a[0].lower()}]{a[1:]}' if a[0].upper() != a[0].lower() else a for a in pattern.split('|'))


NATIONS = [  # code, Bodart's words for a force (docs/napoleonic-frame.md section 5)
    ('FR', r'Franzosen|französisch\w*|Frz\.|Franz\.|Fz\.|Republikaner\w*|republikanisch\w*|Rep\.|Franco'),
    ('AT', r'Österreicher\w*|Öcterreicher|österreichisch\w*|Öst\.|Österr\.|Austro'),
    ('PR', r'Preußen|Preussen|preußisch\w*|Preuß\.'),
    ('RU', r'Russen|russisch\w*|Russ\.|Kosaken\w*'),
    ('GB', r'Engländer\w*|englisch\w*|Engl\.|Briten|britisch\w*|Anglo'),
    ('ES', r'Spanier\w*|spanisch\w*|Span\.|Guerill\w*|Guerrill\w*'),
    ('PT', r'Portugiesen|portugiesisch\w*|Portug\.'),
    ('SA', r'Sardinier\w*|sardinisch\w*|Sard\.|Piemontesen|piemontesisch\w*|Sarden'),
    ('NA', r'Neapolitaner\w*|neapolitanisch\w*|Neap\.'),
    ('NL', r'Holländer\w*|holländisch\w*|Holl\.|Niederländer\w*|niederländisch\w*|Batavier|batavisch\w*'),
    ('HAN', r'Hannoveraner\w*|hannoversch\w*|Hann\.'),
    ('HES', r'Hessen|hessisch\w*|Hess\.'),
    ('BAV', r'Bayern|bayrisch\w*|bayerisch\w*|Bayr\.'),
    ('SAX', r'Sachsen|sächsisch\w*|Sächs\.'),
    ('WUR', r'Württemberger\w*|württembergisch\w*|Württ\.'),
    ('BAD', r'Badener|Badenser|badisch\w*|Bad\.'),
    ('WES', r'Westfalen|Westfäler|westfälisch\w*|Westf\.'),
    ('NAS', r'Nassauer|nassauisch\w*'),
    ('PAL', r'kurpfälzisch\w*|pfälzisch\w*'),
    ('RHB', r'Rheinbund\w*|Rheintruppen'),
    ('PL', r'Polen|polnisch\w*|Poln\.'),
    ('IT', r'Italiener\w*|italienisch\w*|Ital\.'),
    ('SE', r'Schweden|schwedisch\w*|Schwed\.'),
    ('DK', r'Dänen|dänisch\w*|Dän\.'),
    ('OT', r'Türken|türkisch\w*|Türk\.|Osmanen|Albanesen|Janitscharen'),
    ('EGY', r'Mameluken|Mamelucken|Mamelucks|Araber|Ägypter|ägyptisch\w*'),
    ('MAL', r'Malteser\w*|maltesisch\w*'),
    ('SRB', r'Serben|serbisch\w*'),
    ('CH', r'Schweizer|schweizerisch\w*|Schweiz\.'),
    ('TYR', r'Tiroler|tirolisch\w*'),
    ('VEN', r'Vendéer|Vendeer|Vendéen\w*|Vend\.|Royalisten|royalistisch\w*|Royal\.|Chouans'),
    ('INS', r'Insurgenten|aufständisch\w*'),
    ('CRO', r'Kroaten'),
    ('BRU', r'Braunschweiger|braunschweigisch\w*'),
    ('EMI', r'Emigranten'),
    ('HRE', r'Reichstruppen|reichsdeutsch\w*|Reichsarmee'),
    ('IRL', r'Irländer|irländisch\w*|Iren|irisch\w*'),
    ('US', r'Amerikaner\w*|amerikanisch\w*|Amer\.'),
    ('PAP', r'päpstlich\w*'),
    ('ALLIES', r'Verbündet\w*|Verb\.|Alliierte\w*|Koalierte\w*'),
]
NATION_RE = [(c, re.compile(r'(?<![A-Za-zÄÖÜäöüß])(?:' + either_case(p) + r')(?![a-zäöüß])')) for c, p in NATIONS]
NOT_FRENCH_STATE = {'VEN', 'EMI'}  # French royalists and émigrés fought the French state
NOT_A_FORCE = re.compile(r'[A-Za-zÄÖÜäöüß]+(?:e|en|em|er|es)\s+(?:Feldzug|Krieg|Expedition)\w*')  # 'nach dem russischen Feldzuge'

# Forces counted on France's side when an entry names no French troops: a frame convention from the alliance
# periods (docs/napoleonic-frame.md section 5), checked against every Bodart entry that does name French troops.
ALLY_YEARS = {
    'ES': (1796, 1807), 'NL': (1796, 1810), 'IT': (1797, 1814), 'PL': (1797, 1814),
    'BAV': (1805, 1812), 'WUR': (1805, 1812), 'BAD': (1805, 1812), 'HES': (1806, 1812), 'RHB': (1806, 1812),
    'SAX': (1807, 1812), 'WES': (1807, 1812), 'DK': (1808, 1813), 'AT': (1812, 1812), 'PR': (1812, 1812),
    'IRL': (1798, 1798),
}


def nations(text):
    text = NOT_A_FORCE.sub(' ', text or '')
    found = sorted((m.start(), c) for c, rx in NATION_RE for m in rx.finditer(text))
    out = []
    for _, c in found:
        if c not in out:
            out.append(c)
    if NOT_FRENCH_STATE & set(out) and 'FR' in out:
        out.remove('FR')
    return out


# ---------- sides ----------

WINNER_VERBS = (r'(?:zwingen|zwingt|nötigen|nötigt|bemächtigen|bemächtigt|erstürmen|erstürmt|nehmen|nimmt|erobern|erobert|schlagen|'
                r'schlägt|werfen|wirft|behauptet|behaupten|verteidigt|verteidigen|veiteidigt|überfallen|überfällt|überrumpeln|'
                r'überrumpelt|vernichten|vernichtet|zersprengen|zersprengt|sprengen|sprengt|vertreiben|vertreibt|besetzen|besetzt|'
                r'erzwingen|erzwingt|schließen|schließt|wehren|wehrt|weisen|weist|setzen|setzt|halten|hält|entsetzen|entsetzt|'
                r'bringen|bringt)')
WINNER_VERB = re.compile(r'\s' + WINNER_VERBS + r'\b')
SIDE_END = re.compile(r'\s+unter\s+|\s+bis\s+(?:zur|zum)\s|\s+(?:verteidigte\w*|besetzte\w*)\b|,\s+eine[n]?\s+(?:Kapitulation|Waffenstillstand)|\s+(?:zur|zum)\s+(?:Übergabe|Kapitulation|Aufgabe|Räumung|Waffenstreckung|Einschiffung|Rückzuge?|Abzug|Abschluß)\b'
                      r'|,\s+(?:wonach|worauf|wobei|welche[rs]?|nachdem|anfangs|später|zuerst)\b|(?<!ca)(?<!wor)(?<!wov)(?<!urspr)(?<!zus)(?<!zw)\.\s+(?=(?:Die|Der|Das|Nach|Am|Im|Bei|In|Diese\w*|Außerdem|Infolge)\s|\d)')
COMMANDER_END = re.compile(r'\s+über\s+(?:die|den|das)\s|\s' + WINNER_VERBS + r'\b|\s+(?:kapituliert|kapitulieren|strecken|streckt|ergibt|ergeben|'
                           r'übergibt|übergeben|gegen|sich|ohne|bis|nach|mit|infolge|trotz|die|den|das|besetzte\w*|verteidigte\w*|hartnäckig|standhaft)\b'
                           r'|\.\s+(?:Die|Der|Das|Nach|Am|Im|In|Diese|Erst)\s|\.$|,\s+(?:welche\w*|der|die|wobei|nachdem|wonach|von|nach|unterstützt|'
                           r'anfangs|später|geleitet|Beobachtungs\w*|\d)|\s+(?:zur|zum)\s')


# Prose forms of the first paragraph. Bodart names the winner first (p. 46) except where the grammar puts the
# surrendering side first (LOSER_FIRST).
PROSE = [
    ('sieg_ueber', re.compile(r'Sieg\s+(?:de[rs]|eine[rs]?)\s+(?P<w>.+?)\s+über\s+(?:(?:die|den|das|eine[n]?)\s+)?(?P<l>.+)')),
    ('indecisive_first_named', re.compile(r'^Unentschiedene[s]?\s+\w+\s+zwischen\s+(?:den|dem|der)\s+(?P<w>.+?)\s+und\s+(?:den|dem|der)\s+(?P<l>.+)')),
    ('siegreiche_gegen', re.compile(r'^Siegreiche\s+\w+\s+der\s+(?P<w>.+?)\s+gegen\s+(?:die|den|das)\s+(?P<l>.+)')),
    ('vor_kapituliert', re.compile(r'^Vor\s+(?P<w>.+?)\s+(?:kapituliert|kapitulieren|strecken|streckt)\s+(?P<l>.+)')),
    ('ergibt_sich_an', re.compile(r'^(?:Die|Der|Das)\s+(?P<l>.+?)\s+(?:ergibt|ergeben)\s+sich\s+(?:ohne\s+Schwertstreich\s+)?an\s+(?:die\s+|den\s+)?(?P<w>.+)')),
    ('uebergibt', re.compile(r'^(?:Die|Der|Das)\s+(?P<l>.+?)\s+(?:übergibt|übergeben)\s+(?P<w>.+)')),
    ('sieht_sich_gezwungen', re.compile(r'^Infolge\s+.+?\s+sieht\s+sich\s+(?:der|die|das)\s+(?P<l>.+?)\s+gezwungen,\s+mit\s+(?:dem|den|der)\s+(?P<w>.+)')),
    ('nach_verb_subject', re.compile(r'^Nach\s+[^,]+?\s+' + WINNER_VERBS + r'\s+(?:die|der|das)\s+(?P<w>.+?)\s+(?P<l>(?:die|den|das)\s+.+)')),
    ('subject_verb', re.compile(r'^(?:(?:Die|Der|Das)\s+|(?=[\d.]+\s)|(?=Gen\.\s))(?P<w>.+?)\s+' + WINNER_VERBS + r'\b(?P<l>.+)')),
]
LOSER_FIRST = {'ergibt_sich_an', 'uebergibt', 'sieht_sich_gezwungen'}


def at_depth0(text, rx):
    """The first match of rx outside parentheses and brackets."""
    depth, depths = 0, []
    for ch in text:
        depths.append(depth)
        depth = depth + 1 if ch in '([' else depth - 1 if ch in ')]' and depth else depth
    depths.append(depth)
    return next((m for m in rx.finditer(text) if depths[m.start()] == 0), None)


def side_parts(text):
    """(force, commander, later_clause) as printed: the force from its first nation word to its commander, terms or
    the end of its clause, and the commander from the 'unter' that ends the force to the next clause. later_clause
    is True when the side is named only after its clause ended ('..., nachdem ein Teil der hannoverschen Besatzung');
    such entries are listed for review (docs/napoleonic-frame.md section 5)."""
    if not text:
        return None, None, False
    def first_nation(t):
        found = [n.start() for _, rx in NATION_RE for n in rx.finditer(t)]
        return min(found) if found else None

    m = at_depth0(text, SIDE_END)
    head = text[:m.start()] if m else text
    start, later = first_nation(head), False
    if start is None and first_nation(text) is not None:  # the force is named only in a later clause
        text, later = text[first_nation(text):], True
        m = at_depth0(text, SIDE_END)
        head, start = (text[:m.start()] if m else text), 0
    force = head[start or 0:].strip(' ,.;') or None
    if not m or m.group(0).strip() != 'unter':
        return force, None, later
    rest = re.sub(r'^(?:dem|den)\s+', '', text[m.end():])
    end = at_depth0(rest, COMMANDER_END)
    cmd = (rest[:end.start()] if end else rest).strip(' ,.;') or None
    second = re.match(r'^(?P<c1>.+?)\s+und\s+(?P<f2>(?:die\s+)?[A-ZÄÖÜ][a-zäöüß]+)\s+unter\s+(?P<c2>.+)$', cmd or '')
    if second and nations(second.group('f2')):  # 'Neapolitaner unter A und Engländer unter B'
        return f"{force} und {second.group('f2')}", f"{second.group('c1')}; {second.group('c2')}", later
    return force, cmd, later


def prose_sides(par):
    """The first sentence of the paragraph that has a recognised form; a later sentence is marked '@n'."""
    for i, sentence in enumerate(re.split(r'(?<=\.)\s+(?=(?:Die|Der|Das)\s)', par), start=1):
        for name, rx in PROSE:
            m = rx.search(sentence)
            if not m:
                continue
            w, l = m.group('w'), m.group('l')
            if name in LOSER_FIRST and WINNER_VERB.search(l):
                continue  # the subject belongs to an earlier verb; another form applies
            label = name if i == 1 else f'{name}@{i}'
            lead = None
            if name == 'subject_verb' and ' an der Spitze von ' in w:
                lead, w = w.split(' an der Spitze von ', 1)
            (wf, wc, wlater), (lf, lc, llater) = side_parts(w), side_parts(l)
            label += '+winner_later_clause' if wlater else ''
            label += '+loser_later_clause' if llater else ''
            return label, {'w': wf, 'l': lf, 'wc': lead.strip() if lead else wc, 'lc': lc}
    return None, None


def table_sides(e):
    rows = [l for l in e['text'] if ' | ' in l]
    if not rows:
        return None
    cells = [re.split(r'\d', c, maxsplit=1)[0].strip(' [(') for c in rows[0].split(' | ')]  # the label before any figure
    commanders = [c.strip() for c in rows[1].split(' | ')] if len(rows) > 1 and not re.search(r'\d', rows[1]) else None
    return {'w': re.sub(r':$', '', cells[0]), 'l': re.sub(r':$', '', cells[-1]),
            'wc': commanders[0] if commanders else None, 'lc': commanders[-1] if commanders else None}


def sides(e):
    """Winner and loser from the first paragraph's grammar or, failing that, the first table row (winner left)."""
    par = e['text'][0] if e['text'] else ''
    table = table_sides(e)
    method, prose = (None, None) if ' | ' in par else prose_sides(par)
    out = {'method': 'unparsed', 'winner_text': None, 'loser_text': None, 'winner_commander_text': None, 'loser_commander_text': None,
           'winner_nations': [], 'loser_nations': [], 'conflict': None, 'indecisive_printed': par.startswith('Unentschieden')}
    tw, tl = (nations(table['w']), nations(table['l'])) if table else ([], [])
    if prose:
        pw, pl = nations(prose['w']), nations(prose['l'])
        if set(pw) & set(tl) or set(pl) & set(tw):
            out['conflict'] = f'prose ({pw} over {pl}) and table ({tw} over {tl}) disagree'
        filled = []
        if not pw and tw:
            pw, filled = tw, filled + ['winner']
        if not pl and tl:
            pl, filled = tl, filled + ['loser']
        out.update(method=(method or '') + ''.join('+table_' + f for f in filled), winner_text=prose['w'], loser_text=prose['l'],
                   winner_commander_text=prose['wc'], loser_commander_text=prose['lc'], winner_nations=pw, loser_nations=pl)
    elif table:
        out.update(method='table', winner_text=table['w'], loser_text=table['l'], winner_commander_text=table['wc'],
                   loser_commander_text=table['lc'], winner_nations=tw, loser_nations=tl)
    return out


# ---------- wars ----------

WARS = {  # canonical war: (Bodart's running-head names, France a belligerent, start years the war covers in Bodart)
    'russo-polish-1792': (('Zweiter Russisch-Österr. Türkenkrieg', 'Polnische Insurrektion 1792'), False, (1791, 1792)),
    'first-coalition': (('Erster Koalitionskrieg',), True, (1792, 1797)),
    'vendee': (('Bürgerkrieg in der Vendée',), True, (1793, 1796)),
    'polish-1794': (('Polnischer Insurrektionskrieg 1794',), False, (1794, 1794)),
    'egypt-naples-ireland': (('Expedition nach Ägypten, Neapel, Irland',), True, (1798, 1799)),
    'second-coalition': (('Zweiter Koalitionskrieg',), True, (1798, 1800)),
    'british-egypt-1801': (('Engl. Expedition nach Ägypten', 'Englische Expedition nach Ägypten'), True, (1801, 1801)),
    'anglo-danish-1801': (('Englisch-dänischer Seekrieg',), False, (1801, 1801)),
    'third-coalition': (('Dritter Koalitionskrieg', 'Krieg gegen England und Neapel'), True, (1805, 1806)),
    'fourth-coalition': (('Krieg gegen Preußen und Rußland', 'Krieg gegen Schweden'), True, (1806, 1807)),
    'peninsula': (('Krieg auf der Pyrenäischen Halbinsel',), True, (1808, 1814)),
    'finnish-1808': (('Schwed.-Russ. Krieg 1808—1809',), False, (1808, 1809)),
    'fifth-coalition': (('Krieg gegen Österreich', 'Feldzug 1809 gegen Österreich'), True, (1809, 1809)),
    'russo-turkish-1806': (('Russisch-türkischer Krieg',), False, (1806, 1812)),
    'russia-1812': (('Feldzug 1812 gegen Rußland',), True, (1812, 1812)),
    'liberation': (('Befreiungskriege',), True, (1813, 1814)),
    'anglo-american-1812': (('Amerikanisch-englischer Krieg',), False, (1812, 1815)),
    'hundred-days-1815': (('Feldzug 1815',), True, (1815, 1815)),
}
NAME_TO_WAR = {name: war for war, (names, _, _) in WARS.items() for name in names}
IBERIA = {'Spanien', 'Portugal'}
EGYPT = {'Ägypten', 'Unterägypten', 'Oberägypten'}
# France's opponents each war admits. An entry whose opponents fall outside its war's set, or with Spanish or
# Portuguese troops outside the Peninsular War in 1808-1814, contradicts its page head and needs a war override.
WAR_OPPONENTS = {
    'first-coalition': {'AT', 'PR', 'GB', 'NL', 'ES', 'SA', 'HAN', 'HES', 'PAL', 'NA', 'TYR', 'PT', 'BRU', 'BAD', 'WUR', 'BAV', 'SAX', 'PAP'},
    'vendee': {'GB'},
    'egypt-naples-ireland': {'GB', 'OT', 'EGY', 'MAL', 'NA'},
    'second-coalition': {'AT', 'RU', 'GB', 'OT', 'EGY', 'NA', 'BAV', 'SA', 'TYR', 'PT', 'WUR'},
    'british-egypt-1801': {'GB', 'OT'},
    'third-coalition': {'AT', 'RU', 'GB', 'NA', 'SE', 'TYR'},
    'fourth-coalition': {'PR', 'RU', 'SE', 'SAX', 'GB'},
    'peninsula': {'ES', 'PT', 'GB'},
    'fifth-coalition': {'AT', 'TYR', 'GB'},
    'russia-1812': {'RU'},
    'liberation': {'RU', 'PR', 'AT', 'SE', 'GB', 'BAV', 'WUR', 'SAX', 'HES', 'BAD', 'NL', 'HAN', 'BRU', 'NAS', 'CH'},
    'hundred-days-1815': {'PR', 'GB', 'NL', 'AT', 'BAV', 'WUR', 'HES', 'CH', 'HAN', 'BRU', 'NAS', 'BAD', 'RU', 'SAX'},
}
GENERIC = {'ALLIES', 'INS', 'HRE', 'CRO', 'EMI', 'VEN'}  # words that name no state, or France's own insurgents


def war_misfit(rec):
    """Why the entry's belligerents contradict its war, or None."""
    opp = set(rec['loser_nations'] if rec['french_side'] == 'winner' else rec['winner_nations']) - GENERIC
    odd = opp - WAR_OPPONENTS[rec['war']]
    if odd:
        return f'opponents {sorted(odd)} do not fit {rec["war"]}'
    if 1808 <= rec['start_year'] <= 1814 and (set(rec['winner_nations']) | set(rec['loser_nations'])) & {'ES', 'PT'} and rec['war'] != 'peninsula':
        return 'Spanish or Portuguese troops outside the Peninsular War'
    return None


def head_wars(head):
    """Canonical wars named in a running head; a bare 'Feldzug YYYY' after a war is that war's campaign label."""
    text = re.sub(r'^(Revolutionskriege|Napoleonische Kriege)\s*/\s*', '', head)
    text = re.sub(r'^\s*\d{3}\s+|\s*\b\d{3}\b\s*$', '', text).replace(' / ', ' — ').rstrip(' .')
    parts = [p.strip(' .—') for p in re.split(r'\s+—\s+', text) if p.strip(' .—') and p.strip(' .—') not in ('Revolutionskriege', 'Napoleonische Kriege')]
    out = []
    for i, p in enumerate(parts):
        if re.fullmatch(r'Feldzug \d{4}', p) and not (p == 'Feldzug 1815' and (i == 0 or 'Amerikanisch' in parts[i - 1])):
            continue  # a campaign label of the preceding war
        war = NAME_TO_WAR.get(p)
        if war is None:
            raise FrameError(f'unknown war in running head: {p!r}')
        if war not in out:
            out.append(war)
    return out


def country(location):
    m = re.search(r'\b(?:in|im)\s+(?:dem\s+|der\s+|den\s+)?(?:südlichen\s+|nördlichen\s+|nördl\.\s+|südl\.\s+|östlichen\s+|westlichen\s+)?'
                  r'(Frankreich|Spanien|Portugal|Italien|Oberitalien|Unteritalien|Österreich|Deutschland|Preußen|Bayern|Sachsen|Rußland|'
                  r'Russisch-Polen|Polen|Holland|Belgien|Ägypten|Unterägypten|Oberägypten|Syrien|Rumänien|Bulgarien|Serbien|Schweden|Finnland|'
                  r'Dänemark|Irland|England|Schweiz|Tirol|Mähren|Böhmen|Ungarn|Kroatien|Dalmatien|Pommern|Württemberg|Baden|Hessen|Westfalen|'
                  r'Hannover|Mecklenburg|Kalabrien|Sizilien|Palästina|Amerika|Nordamerika|Louisiana|Kanada|Rumelien|Bessarabien|Walachei|Moldau)', location or '')
    return m.group(1) if m else None


def ally(nation_codes, year):
    return sorted(c for c in nation_codes if c in ALLY_YEARS and ALLY_YEARS[c][0] <= year <= ALLY_YEARS[c][1])


def french_side(w, l, year):
    """('winner'|'loser'|None, basis): the side of named French troops, else of the forces fighting with France."""
    w_fr, l_fr = 'FR' in w, 'FR' in l
    if w_fr != l_fr:
        return ('winner' if w_fr else 'loser'), 'french_troops_named'
    if w_fr and l_fr:
        return None, 'French troops named on both sides'
    wa, la = ally(w, year), ally(l, year)
    if wa and not la:
        return 'winner', 'ally:' + '+'.join(wa)
    if la and not wa:
        return 'loser', 'ally:' + '+'.join(la)
    return None, f'no French troops named and the ally rule does not decide (winner {w}, loser {l})'


def assign_war(rec, page_wars):
    """The entry's war: its page's only war, else the war its belligerents, place and year fit."""
    if len(page_wars) == 1:
        return page_wars[0], 'running_head'
    nat = set(rec['winner_nations']) | set(rec['loser_nations'])
    y, loc, fr = rec['start_year'], rec['country'], rec['french_side'] is not None
    claims = []
    for w in page_wars:
        if w == 'russo-turkish-1806' and ({'RU', 'OT'} <= nat or 'SRB' in nat):
            claims.append(w)
        elif w == 'finnish-1808' and {'SE', 'RU'} <= nat:
            claims.append(w)
        elif w == 'polish-1794' and 'PL' in nat and nat & {'RU', 'PR'} and not fr:
            claims.append(w)
        elif w == 'russo-polish-1792' and not fr:
            claims.append(w)
        elif w == 'anglo-american-1812' and 'US' in nat:
            claims.append(w)
        elif w == 'anglo-danish-1801' and {'GB', 'DK'} <= nat and not fr:
            claims.append(w)
    if len(claims) == 1:
        return claims[0], 'belligerents'
    if claims:
        return None, f'claimed by {claims}'
    if not fr:
        return None, f'no French side among {page_wars}'
    cands = [w for w in page_wars if WARS[w][1] and WARS[w][2][0] <= y <= WARS[w][2][1]]
    if 'vendee' in cands and len(cands) > 1:
        cands = ['vendee'] if 'VEN' in nat else [w for w in cands if w != 'vendee']
    if 'peninsula' in cands and len(cands) > 1:
        cands = ['peninsula'] if nat & {'ES', 'PT'} or loc in IBERIA else [w for w in cands if w != 'peninsula']
    if 'british-egypt-1801' in cands and len(cands) > 1:
        cands = ['british-egypt-1801'] if loc in EGYPT else [w for w in cands if w != 'british-egypt-1801']
    if len(cands) == 1:
        return cands[0], 'belligerents, place and year'
    return None, f'undecided among {page_wars} (candidates {cands})'


# ---------- figures as printed ----------

def figures(e):
    """Strength and loss statements as printed, per side (winner left, loser right)."""
    out: dict[str, str | None] = {'winner_strength_printed': None, 'loser_strength_printed': None, 'winner_loss_printed': None,
                                  'loser_loss_printed': None}
    for l in e['text']:
        parts = [p.strip() for p in l.split(' | ')]
        if len(parts) == 3 and re.search(r'Gesamt\s*-\s*Stärke', parts[1]):
            out['winner_strength_printed'], out['loser_strength_printed'] = parts[0], parts[2]
        if len(parts) == 3 and re.search(r'Ges(?:amt)?\.?\s*-\s*Verl', parts[1]):
            out['winner_loss_printed'], out['loser_loss_printed'] = parts[0], parts[2]
        if len(parts) == 2 and re.search(r'Verl(?:\.|uste)\s*:', parts[0]) and re.search(r'Verl(?:\.|uste)\s*:', parts[1]):
            out['winner_loss_printed'], out['loser_loss_printed'] = parts
    if out['winner_strength_printed'] is None and e['text'] and ' | ' not in e['text'][0]:
        par = e['text'][0]
        m = re.search(r'Sieg\s+de[rs]\s+(.+?)\s+über\s+(?:die|den|das)\s+(.+)', par) or re.search(r'^(?:Die|Der|Das)\s+(.+?)\s+' + WINNER_VERBS + r'\b(.+)', par)
        if m:
            grab = lambda s: (re.search(r'\(([^()]*\d[^()]*)\)', s) or [None, None])[1]
            out['winner_strength_printed'], out['loser_strength_printed'] = grab(m.group(1)), grab(m.group(m.lastindex or 1))
    return out


# ---------- the frame ----------

OVERRIDE_FIELDS = {'id', 'reason', 'year', 'war', 'french_side', 'winner_nations', 'loser_nations', 'in_frame'}


def load_overrides(root):
    data = read_json(safe_path(root, OVERRIDES))
    heads = {}
    for h in data.get('running_heads', []):
        if not h.get('reason') or not h.get('pages') or not h.get('head'):
            raise FrameError(f'malformed running-head correction {h}')
        for p in h['pages']:
            heads[p] = h['head']
    ov = {}
    for o in data['entries']:
        if not o.get('reason') or set(o) - OVERRIDE_FIELDS or not set(o) - {'id', 'reason'}:
            raise FrameError(f'malformed override {o.get("id")}')
        if o['id'] in ov:
            raise FrameError(f'duplicate override {o["id"]}')
        ov[o['id']] = o
    return heads, ov


def build(root):
    text = safe_path(root, TRANSCRIPTION).read_text(encoding='utf-8')
    heads, ov = load_overrides(root)
    frame, undecided = [], []
    prev_end = None
    for e in entries(text):
        o = ov.get(e['id'], {})
        year = int(o.get('year', e['year_printed']))
        start, end, flags = parse_dates(year, e['date_printed'])
        if not FRAME_YEARS[0] - 1 <= start[0] <= FRAME_YEARS[1] or (prev_end is not None and end[0] < prev_end):
            undecided.append((e['id'], f'printed year {year} outside 1791-1815 or out of Bodart\'s end-date order (previous end {prev_end})'))
        prev_end = end[0]
        s = sides(e)
        if s['conflict']:
            undecided.append((e['id'], s['conflict']))
        w = o.get('winner_nations', s['winner_nations'])
        l = o.get('loser_nations', s['loser_nations'])
        head = heads.get(e['page'], e['running_head'])
        rec = {'id': e['id'], 'page': e['page'], 'pages': e['pages'], 'running_head': e['running_head'],
               'running_head_used': head if head != e['running_head'] else None,
               'year_printed': e['year_printed'], 'date_printed': e['date_printed'], 'type_printed': e['type_printed'],
               'connector': e['connector'], 'place': e['place'], 'alternative_names': e['alternative_names'], 'category': e['category'],
               'location': e['location'], 'country': country(e['location']),
               'start_year': start[0], 'start_month': start[1], 'start_date': iso(start), 'end_date': iso(end),
               'date_flags': flags + ([] if iso(start) or start[2] is None else ['impossible_printed_date']) + (['year_override'] if 'year' in o else []),
               'side_method': s['method'], 'indecisive_printed': s['indecisive_printed'],
               'winner_text': s['winner_text'], 'loser_text': s['loser_text'],
               'winner_commander_text': s['winner_commander_text'], 'loser_commander_text': s['loser_commander_text'],
               'winner_nations': w, 'loser_nations': l}
        side, basis = (o['french_side'], 'override') if 'french_side' in o else french_side(w, l, start[0])
        if {'winner_nations', 'loser_nations'} & set(o) and side:
            basis = 'override'
        rec['french_side'] = side
        war, war_basis = (o['war'], 'override') if 'war' in o else assign_war(rec, head_wars(head))
        if war is None:
            undecided.append((e['id'], war_basis))
        elif not WARS[war][2][0] <= start[0] <= WARS[war][2][1]:
            undecided.append((e['id'], f'{war} does not cover {start[0]}'))
        france = WARS[war][1] if war else None
        if france and side and 'war' not in o and war_misfit({**rec, 'war': war}):
            undecided.append((e['id'], war_misfit({**rec, 'war': war})))
        reason = ('outside 1792-1815' if not FRAME_YEARS[0] <= start[0] <= FRAME_YEARS[1] else
                  'war France did not fight' if france is False else
                  'an agreement, not an engagement' if 'KONVENTION' in e['type_printed'] else
                  'France not engaged (override)' if o.get('in_frame') is False else None)
        in_frame = reason is None and war is not None
        if in_frame and side is None:
            undecided.append((e['id'], f'French side: {basis}'))
        rec.update({'war': war, 'war_basis': war_basis if war else None, 'france_belligerent': france, 'in_frame': in_frame,
                    'out_of_frame_reason': reason, 'naval': bool(re.match(r'SEE', e['type_printed'])),
                    'no_combat_printed': bool(re.search(r'ohne\s+Schwertstreich', ' '.join(e['text']))),
                    'french_side': side if in_frame else None, 'side_a_basis': basis if in_frame else None,
                    'french_troops_named': ('FR' in (s['winner_nations'] if side == 'winner' else s['loser_nations']))
                    if in_frame and side else None,  # as printed, before any override
                    'outcome_side_a': (1 if side == 'winner' else 0) if in_frame and side else None,
                    'campaign_group': f'{war} {start[0]}' if in_frame else None,
                    **figures(e), 'override_reason': o.get('reason')})
        frame.append(rec)
    ids = [r['id'] for r in frame]
    if len(ids) != len(set(ids)):
        raise FrameError('Duplicate entry IDs')
    unused = set(ov) - set(ids)
    if unused:
        raise FrameError(f'Overrides name unknown entries: {sorted(unused)}')
    undecided += ally_conflicts(frame)
    if undecided:
        raise FrameError('Undecided entries need an override: ' + '; '.join(f'{i}: {r}' for i, r in undecided))
    return {'kind': 'napoleonic_frame', 'version': 1, 'status': 'frozen_frame_not_a_model_input',
            'source_id': 'bodart-1908-transcription-v1',
            'bindings': {p: digest(safe_path(root, p)) for p in (TRANSCRIPTION, OVERRIDES, DESIGN, CODE)},
            'counts': counts(frame), 'entries': frame}


def ally_conflicts(frame):
    """Entries naming French troops whose opponents include a nation the ally table puts on France's side that year."""
    out = []
    for r in frame:
        if not r['in_frame'] or not r['french_troops_named']:
            continue
        opp = r['loser_nations'] if r['french_side'] == 'winner' else r['winner_nations']
        bad = ally(opp, r['start_year'])
        if bad:
            out.append((r['id'], f'ally table puts {bad} on France\'s side in {r["start_year"]}, but Bodart names them against the French'))
    return out


def counts(frame):
    in_frame = [r for r in frame if r['in_frame']]
    return {'entries_transcribed': len(frame), 'in_frame': len(in_frame),
            'out_of_frame_by_reason': dict(sorted(Counter(r['out_of_frame_reason'] for r in frame if not r['in_frame']).items())),
            'in_frame_by_start_year': dict(sorted(Counter(str(r['start_year']) for r in in_frame).items())),
            'in_frame_by_war': dict(sorted(Counter(r['war'] for r in in_frame).items())),
            'in_frame_naval': sum(r['naval'] for r in in_frame),
            'in_frame_no_combat_printed': sum(r['no_combat_printed'] for r in in_frame),
            'side_a_basis': dict(sorted(Counter(r['side_a_basis'] for r in in_frame).items())),
            'french_side_won': sum(r['outcome_side_a'] == 1 for r in in_frame),
            'indecisive_printed': sum(r['indecisive_printed'] for r in in_frame),
            'campaign_groups': len({r['campaign_group'] for r in in_frame})}


def cohort(frame, frame_sha256):
    rows = [r for r in frame['entries'] if r['in_frame'] and not r['naval'] and COHORT_YEARS[0] <= r['start_year'] <= COHORT_YEARS[1]]
    groups = Counter(r['campaign_group'] for r in rows)
    return {'kind': 'research_cohort', 'version': 1, 'frame': FRAME, 'frame_sha256': frame_sha256,
            'rule': f'in-frame land entries whose start year is {COHORT_YEARS[0]}-{COHORT_YEARS[1]}',
            'battle_ids': [r['id'] for r in rows], 'campaign_groups': dict(sorted(groups.items())),
            'counts': {'entries': len(rows), 'campaign_groups': len(groups)}}


def check(root):
    built = build(root)
    if built != read_json(safe_path(root, FRAME)):
        raise FrameError('The committed frame does not rebuild from the transcription and overrides')
    if cohort(built, digest(safe_path(root, FRAME))) != read_json(safe_path(root, COHORT)):
        raise FrameError('The committed cohort does not rebuild from the frame')
    return built['counts']
