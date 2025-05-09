"""
gif_map.py

This module maps emotional moods to appropriate anime-themed GIF search phrases.
It is designed to be extensible and expressive for a wide range of emotional states.
"""

from typing import Optional

# Richer GIF mapping by mood — categorized and expansive
gif_map = {
    'happy': 'anime smiling joy',
    'joyful': 'anime happy dance',
    'excited': 'anime sparkle eyes',
    'cheerful': 'anime laughing',
    'relaxed': 'anime peaceful nature',
    'content': 'anime serene smile',

    'sad': 'anime crying',
    'melancholic': 'anime rain window',
    'lonely': 'anime alone night',
    'depressed': 'anime dark room',
    'disappointed': 'anime sigh',
    'heartbroken': 'anime tears breakup',

    'angry': 'anime rage flames',
    'frustrated': 'anime annoyed',
    'annoyed': 'anime twitching eyebrow',
    'resentful': 'anime shadowed face',
    'jealous': 'anime pout',

    'anxious': 'anime nervous sweat',
    'worried': 'anime pacing',
    'nervous': 'anime shaking hands',
    'afraid': 'anime scared eyes',
    'paranoid': 'anime suspicious glance',

    'contemplative': 'anime thinking',
    'pensive': 'anime deep thoughts',
    'wistful': 'anime nostalgic',
    'curious': 'anime exploring',
    'bored': 'anime sigh bored',
    'indifferent': 'anime blank stare',

    'confident': 'anime smirk',
    'determined': 'anime power-up',
    'inspired': 'anime light bulb',
    'focused': 'anime intense stare',
    'motivated': 'anime training montage',

    'surprised': 'anime shock face',
    'shocked': 'anime gasp',
    'amazed': 'anime sparkle eyes',
    'confused': 'anime question marks',
    'embarrassed': 'anime blush',

    'tired': 'anime sleepy',
    'exhausted': 'anime collapsed',
    'sleepy': 'anime yawning',
    'lazy': 'anime lying down',
}

def get_gif(mood: str) -> str:
    """
    Return a relevant anime GIF search term for a given mood.

    Parameters:
    - mood (str): The emotional state of the user.

    Returns:
    - str: A string that can be used as a search phrase to find an anime-style GIF.
    """
    normalized_mood = mood.strip().lower()
    return gif_map.get(normalized_mood, 'anime thinking')


# Optional: A function to suggest similar moods (if input mood is unknown)
def suggest_similar_moods(partial: str) -> list[str]:
    """
    Suggest moods from the gif_map that start with or contain the given partial input.

    Parameters:
    - partial (str): The partial or incorrect mood name.

    Returns:
    - list[str]: List of potential intended moods.
    """
    partial = partial.lower()
    return [m for m in gif_map if partial in m]


# Example usage (can be removed in production)
if __name__ == "__main__":
    test_moods = ["Melancholic", "joyful", "tired", "confused", "overjoyed", "burnt out"]
    for mood in test_moods:
        gif = get_gif(mood)
        print(f"Mood: {mood:15} → GIF Search: {gif}")
        if gif == 'anime thinking':
            suggestions = suggest_similar_moods(mood)
            if suggestions:
                print(f"  Did you mean: {', '.join(suggestions)}?")
            else:
                print("  No suggestions found.")
