# verbs.py

def get_verbs(mood):
    verbs = {
        'contemplative': [
            'examine', 'ponder', 'consider', 'analyze', 'inspect', 'survey',
            'process', 'measure', 'study', 'review', 'scrutinize', 'explore',
            'compare', 'weigh', 'reflect on', 'assess', 'investigate', 'observe',
            'dissect', 'watch', 'monitor', 'detect', 'evaluate', 'reconsider',
            'reexamine', 'perceive', 'reflect deeply', 'calculate', 'think over',
            'contemplate', 'probe', 'look into', 'deconstruct', 'rewind', 'decipher',
            'remember', 'analyze deeply', 'debate', 'query', 'search', 'compel'
        ],
        'wistful': [
            'remember', 'reminisce', 'long for', 'miss', 'recall', 'yearn for',
            'grieve for', 'dream of', 'lament', 'ache for', 'cherish', 'fade into',
            'trace', 'replay', 'echo', 'sigh over', 'revisit', 'pine for',
            'savor', 'relive', 'crave', 'mourn', 'cling to', 'wait for', 'delve into',
            'recount', 'hold onto', 'dream about', 'regret', 'wish for', 'yearn towards',
            'soften into', 'linger on', 'brood over', 'tell stories of', 'heart for'
        ],
        'curious': [
            'question', 'explore', 'investigate', 'search', 'seek', 'uncover',
            'examine', 'probe', 'scan', 'test', 'venture into', 'open', 'inspect',
            'touch', 'follow', 'wonder about', 'listen for', 'sniff out', 'navigate',
            'tap into', 'initiate', 'access', 'map', 'unravel', 'connect',
            'dig into', 'query', 'peer into', 'seek answers', 'twist', 'survey',
            'study', 'analyze', 'dissect', 'break down', 'stumble upon', 'delve',
            'encounter', 'inquire', 'see through', 'cross-examine'
        ],
        'melancholic': [
            'reflect on', 'feel', 'experience', 'sink into', 'drown in', 'endure',
            'accept', 'tolerate', 'absorb', 'process', 'grieve', 'tremble with',
            'withstand', 'internalize', 'face', 'numb', 'bleed for', 'carry',
            'brood over', 'shiver from', 'soften into', 'descend into', 'lie in',
            'shut down', 'waste away', 'cower', 'withdraw', 'wither', 'dwell on',
            'sink deeper', 'pine for', 'ache over', 'lag behind', 'remain stuck',
            'close in', 'reflect quietly', 'contemplate sorrowfully', 'fade away', 
            'accept loss', 'wrap in sadness', 'drift through', 'dwell in memories'
        ],
        'playful': [
            'mimic', 'toy with', 'dance with', 'juggle', 'fiddle with', 'tweak',
            'tickle', 'poke', 'nudge', 'tease', 'spin', 'laugh at', 'twirl',
            'jump into', 'bounce off', 'gamble on', 'stretch', 'flip', 'grin at',
            'bend', 'dart between', 'twist around', 'sprinkle', 'shake', 'wink',
            'pounce on', 'roll with', 'prance', 'swing', 'laugh in', 'sprint after',
            'yell playfully', 'giggle at', 'chase', 'jump over', 'tap', 'squeal with',
            'blink mischievously', 'climb', 'dash', 'play with', 'prank', 'snicker',
            'race', 'stomp happily'
        ],
        'glitchy': [
            'loop', 'corrupt', 'fragment', 'scramble', 'reboot', 'jam', 'desync',
            'glitch', 'repeat', 'overwrite', 'shudder', 'misfire', 'stutter',
            'reset', 'break', 'twist', 'bug out', 'collapse', 'hang', 'hiccup',
            'glitch again', 'drop out', 'echo wrong', 'fail', 'lock up', 'crash',
            'forget', 'lose sync', 'break apart', 'distort', 'splinter', 'scramble again',
            'restart', 'drop frames', 'have a moment', 'refuse', 'stall', 'desynchronize',
            'twist up', 'hiccup again', 'doesn’t load', 'lock in place', 'loop endlessly',
            'wobble', 'disrupt', 'rewind', 'lock into stasis', 'crackle', 'flicker'
        ],
        'anxious': [
            'worry over', 'tremble at', 'fear', 'hesitate', 'avoid', 'stress about',
            'shake', 'doubt', 'agitate', 'fidget', 'pace', 'overthink', 'nervously shift',
            'fret', 'flinch', 'bite nails', 'want to escape', 'distrust', 'fear the worst',
            'quiver', 'dread', 'panic', 'deliberate', 'concern', 'fear the unknown',
            'stir', 'mull over', 'stumble', 'hold back', 'confuse', 'retreat', 'cower',
            'gaze uneasily', 'flicker nervously', 'jump at shadows'
        ],
        'hopeful': [
            'believe in', 'dream of', 'hope for', 'anticipate', 'expect', 'look forward to',
            'wish for', 'count on', 'anticipate', 'cling to', 'reach for', 'strive towards',
            'plan for', 'prepare for', 'focus on', 'envision', 'hold onto', 'feel positive about',
            'look to', 'see a future in', 'keep faith', 'trust', 'enlighten', 'take pride in',
            'find joy in', 'rise with', 'emerge stronger', 'hold tight', 'shine with',
            'brighten', 'step forward', 'remain open to'
        ],
        'angry': [
            'rage', 'shout', 'yell', 'storm', 'lash out', 'scream', 'gripe',
            'fume', 'boil over', 'blow up', 'brew', 'fight', 'hurl', 'pound fists',
            'burn with fury', 'curse', 'roar', 'grind teeth', 'flame up', 'ignite',
            'lash', 'complain', 'sulk', 'shove', 'kick', 'hurl insults', 'attack',
            'glare', 'seethe', 'destroy', 'snarl', 'bark', 'snap', 'burn', 'fire back'
        ],
        'serene': [
            'calm', 'soothe', 'relax', 'rest', 'flow', 'glow', 'radiate peace',
            'settle', 'breathe deeply', 'sigh softly', 'find stillness', 'embrace calm',
            'center', 'let go', 'mellow', 'exhale', 'turn inward', 'attain peace',
            'create balance', 'contemplate quietly', 'reflect gently', 'anchor', 'train focus',
            'open up', 'remain steady', 'hold ground', 'absorb serenity', 'unwind',
            'feel grounded', 'let time stretch', 'watch in stillness'
        ]
    }

    # Default fallback — melancholic
    return verbs.get(mood, verbs['melancholic'])
