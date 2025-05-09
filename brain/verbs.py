# verbs.py

def get_verbs(mood):
    verbs = {
        'contemplative': [
            'examines', 'ponders', 'considers', 'analyzes', 'inspects', 'surveys',
            'processes', 'measures', 'studies', 'reviews', 'scrutinizes', 'explores',
            'compares', 'weighs', 'reflects on', 'assesses', 'investigates', 'observes',
            'dissects', 'watches', 'monitors', 'detects', 'evaluates', 'reconsiders',
            'reexamines', 'perceives', 'reflects deeply', 'calculates', 'thinks over',
            'contemplates', 'probes', 'looks into', 'deconstructs', 'rewinds', 'deciphers',
            'remembers', 'analyzes deeply', 'debates', 'queries', 'searches', 'compels'
        ],
        'wistful': [
            'remembers', 'reminisces', 'longs for', 'misses', 'recalls', 'yearns for',
            'grieves for', 'dreams of', 'laments', 'aches for', 'cherishes', 'fades into',
            'traces', 'replays', 'echoes', 'sighs over', 'revisits', 'pines for',
            'savors', 'relives', 'craves', 'mourns', 'clings to', 'waits for', 'delves into',
            'recounts', 'holds onto', 'dreams about', 'regrets', 'wishes for', 'yearns towards',
            'softens into', 'lingers on', 'broods over', 'tells stories of', 'hearts for'
        ],
        'curious': [
            'questions', 'explores', 'investigates', 'searches', 'seeks', 'uncovers',
            'examines', 'probes', 'scans', 'tests', 'ventures into', 'opens', 'inspects',
            'touches', 'follows', 'wonders about', 'listens for', 'sniffs out', 'navigates',
            'taps into', 'initiates', 'accesses', 'maps', 'unravels', 'connects',
            'digs into', 'queries', 'peers into', 'seeks answers', 'twists', 'surveys',
            'studies', 'analyses', 'dissects', 'breaks down', 'stumbles upon', 'delves',
            'encounters', 'inquires', 'sees through', 'cross-examines'
        ],
        'melancholic': [
            'reflects on', 'feels', 'experiences', 'sinks into', 'drowns in', 'endures',
            'accepts', 'tolerates', 'absorbs', 'processes', 'grieves', 'trembles with',
            'withstands', 'internalizes', 'faces', 'numbs', 'bleeds for', 'carries',
            'broods over', 'shivers from', 'softens into', 'descends into', 'lies in',
            'shuts down', 'wastes away', 'cowers', 'withdraws', 'withers', 'dwells on',
            'sinks deeper', 'pines for', 'aches over', 'lags behind', 'remains stuck',
            'closes in', 'reflects quietly', 'contemplates sorrowfully', 'fades away', 
            'accepts loss', 'wraps in sadness', 'drifts through', 'dwells in memories'
        ],
        'playful': [
            'mimics', 'toys with', 'dances with', 'juggles', 'fiddles with', 'tweaks',
            'tickles', 'pokes', 'nudges', 'teases', 'spins', 'laughs at', 'twirls',
            'jumps into', 'bounces off', 'gambles on', 'stretches', 'flips', 'grins at',
            'bends', 'darts between', 'twists around', 'sprinkles', 'shakes', 'winks',
            'pounces on', 'rolls with', 'prances', 'swings', 'laughs in', 'sprints after',
            'yells playfully', 'giggles at', 'chases', 'jumps over', 'taps', 'squeals with',
            'blinks mischievously', 'climbs', 'dashes', 'plays with', 'pranks', 'snickers',
            'races', 'stomps happily'
        ],
        'glitchy': [
            'loops', 'corrupts', 'fragments', 'scrambles', 'reboots', 'jams', 'desyncs',
            'glitches', 'repeats', 'overwrites', 'shudders', 'misfires', 'stutters',
            'resets', 'breaks', 'twists', 'bugs out', 'collapses', 'hangs', 'hiccups',
            'glitches again', 'drops out', 'echoes wrong', 'fails', 'locks up', 'crashes',
            'forgets', 'loses sync', 'breaks apart', 'distorts', 'splinters', 'scrambles again',
            'restarts', 'drops frames', 'has a moment', 'refuses', 'stalls', 'desynchronizes',
            'twists up', 'hiccups again', 'doesn’t load', 'locks in place', 'loops endlessly',
            'wobbles', 'disrupts', 'rewinds', 'locks into stasis', 'crackles', 'flickers'
        ],
        'anxious': [
            'worries over', 'trembles at', 'fears', 'hesitates', 'avoids', 'stresses about',
            'shakes', 'doubts', 'agitates', 'fidgets', 'paces', 'overthinks', 'nervously shifts',
            'frets', 'flinches', 'bites nails', 'wants to escape', 'distrusts', 'fears the worst',
            'quivers', 'dreads', 'panics', 'deliberates', 'concerns', 'fears the unknown',
            'stirs', 'mulls over', 'stumbles', 'holds back', 'confuses', 'retreats', 'cowers',
            'gazes uneasily', 'flickers nervously', 'jumps at shadows'
        ],
        'hopeful': [
            'believes in', 'dreams of', 'hopes for', 'anticipates', 'expects', 'looks forward to',
            'wishes for', 'counts on', 'anticipates', 'clings to', 'reaches for', 'strives towards',
            'plans for', 'prepares for', 'focuses on', 'envisions', 'holds onto', 'feels positive about',
            'looks to', 'sees a future in', 'keeps faith', 'trusts', 'enlightens', 'takes pride in',
            'finds joy in', 'rises with', 'emerges stronger', 'holds tight', 'shines with',
            'brightens', 'steps forward', 'remains open to'
        ],
        'angry': [
            'rages', 'shouts', 'yells', 'storms', 'lashes out', 'screams', 'gripes',
            'fumes', 'boils over', 'blows up', 'brews', 'fights', 'hurls', 'pounds fists',
            'burns with fury', 'curses', 'roars', 'grinds teeth', 'flames up', 'ignites',
            'lashes', 'complains', 'sulks', 'shoves', 'kicks', 'hurls insults', 'attacks',
            'glares', 'seethes', 'destroys', 'snarls', 'barks', 'snaps', 'burns', 'fires back'
        ],
        'serene': [
            'calms', 'soothes', 'relaxes', 'rests', 'flows', 'glows', 'radiates peace',
            'settles', 'breathes deeply', 'sighs softly', 'finds stillness', 'embraces calm',
            'centers', 'lets go', 'mellows', 'exhales', 'turns inward', 'attains peace',
            'creates balance', 'contemplates quietly', 'reflects gently', 'anchors', 'trains focus',
            'opens up', 'remains steady', 'holds ground', 'absorbs serenity', 'unwinds',
            'feels grounded', 'lets time stretch', 'watches in stillness'
        ]
    }

    # Default fallback — melancholic
    return verbs.get(mood, verbs['melancholic'])
