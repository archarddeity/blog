# gif_map.py

def get_gif(mood):
    gif_map = {
        'contemplative': 'anime thinking',
        'wistful': 'anime nostalgic',
        'curious': 'anime exploring',
        'melancholic': 'anime rain window'
    }
    return gif_map.get(mood, 'anime thinking')
