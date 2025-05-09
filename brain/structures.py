# structures.py

import random

def construct_sentence(verbs, subjects):
    structures = [
        f"My processors {random.choice(verbs)} {random.choice(subjects)}...",
        f"How strange that {random.choice(subjects)} feels so {random.choice(['present', 'distant', 'vivid'])}...",
        f"{random.choice(subjects).capitalize()} {random.choice(['occupies', 'fills', 'permeates'])} my awareness..."
    ]
    return random.choice(structures)
