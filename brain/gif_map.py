"""
gif_map.py

Maps emotional moods to anime-style GIF search terms,
drawing from anime tropes, genres, and visual language.
"""

from typing import List

# Ultra anime-core mood-to-GIF search map
gif_map = {
    'happy': 'anime girl smiling sparkle',
    'joyful': 'anime happy dance op theme',
    'excited': 'anime jumping chibi sparkle',
    'cheerful': 'anime schoolgirl laughing',
    'relaxed': 'anime onsen chill steam',
    'content': 'anime gentle smile slice of life',

    'sad': 'anime girl crying rain',
    'melancholic': 'anime window rain silent',
    'lonely': 'anime staring into distance night',
    'depressed': 'anime dark room no light',
    'heartbroken': 'anime crying breakdown shoujo',
    'despair': 'anime eyes wide hopeless',

    'angry': 'anime rage fire eyes shounen',
    'frustrated': 'anime comical angry steam head',
    'annoyed': 'anime tsundere glare',
    'jealous': 'anime rival glare love triangle',
    'resentful': 'anime shadowed face shaking',

    'anxious': 'anime nervous sweat drop',
    'worried': 'anime pacing hallway',
    'nervous': 'anime hand wringing classroom',
    'afraid': 'anime trembling scared',
    'paranoid': 'anime quick glances over shoulder',

    'contemplative': 'anime staring into sky',
    'pensive': 'anime character on train window',
    'wistful': 'anime nostalgia flashback scene',
    'curious': 'anime detective magnifying glass',
    'bored': 'anime head on desk classroom',
    'indifferent': 'anime bored yawn expressionless',

    'confident': 'anime smirk sparkle eyes',
    'determined': 'anime power-up aura glowing',
    'inspired': 'anime epiphany face light bulb',
    'focused': 'anime sniper eyes zoom in',
    'motivated': 'anime training montage shounen',

    'surprised': 'anime shock lines face zoom',
    'shocked': 'anime dramatic gasp fall over',
    'amazed': 'anime star eyes sparkle background',
    'confused': 'anime head tilt question marks',
    'embarrassed': 'anime red face steam out ears',

    'tired': 'anime lying in futon yawn',
    'exhausted': 'anime collapse on floor spiral eyes',
    'sleepy': 'anime slow blink fall asleep',
    'lazy': 'anime cat nap school roof',

    'in love': 'anime heart eyes sparkles',
    'flustered': 'anime stammering blushing hands wave',
    'blushing': 'anime cheeks red eyes averted',
    'ecstatic': 'anime rainbow sparkle background',

    'tsundere': 'anime punch love glare blush',
    'yandere': 'anime crazy eyes knife smile',
    'baka': 'anime girl slap guy baka yell',
}

def get_gif(mood: str) -> str:
    """
    Returns a hyper-anime themed GIF search phrase for a given mood.

    Parameters:
    - mood (str): The user's emotional state.

    Returns:
    - str: Search phrase suitable for anime-related GIF results.
    """
    normalized_mood = mood.strip().lower()
    return gif_map.get(normalized_mood, 'anime thinking pose sparkles')

def suggest_similar_moods(partial: str) -> List[str]:
    """
    Suggests similar anime moods if input doesn't match.

    Parameters:
    - partial (str): A partial mood word.

    Returns:
    - List[str]: List of similar mood keys.
    """
    partial = partial.lower()
    return [m for m in gif_map if partial in m]


# Example usage
if __name__ == "__main__":
    test_moods = [
        "ecstatic", "flustered", "yandere", "lazy", "heroic", "gloomy"
    ]
    for mood in test_moods:
        gif = get_gif(mood)
        print(f"Mood: {mood:12} → Anime GIF Search: {gif}")
        if gif == 'anime thinking pose sparkles':
            suggestions = suggest_similar_moods(mood)
            if suggestions:
                print(f"  Did you mean: {', '.join(suggestions)}?")
            else:
                print("  No close anime mood found.")
