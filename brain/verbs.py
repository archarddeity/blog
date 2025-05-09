# verbs.py

def get_verbs(mood):
    verbs = {
        'contemplative': ['examines', 'ponders', 'considers'],
        'wistful': ['remembers', 'reminisces', 'longs for'],
        'curious': ['questions', 'explores', 'investigates'],
        'melancholic': ['reflects on', 'feels', 'experiences']
    }
    return verbs.get(mood, ['reflects on', 'feels', 'experiences'])
