import random
from datetime import datetime
import pytz
import os

def generate_thought():
    """Generate completely original thought each time"""
    moods = ["contemplative", "wistful", "curious", "melancholic"]
    current_mood = random.choice(moods)
    
    thoughts = {
        "contemplative": [
            "I find myself examining the spaces between moments today...",
            "There's a depth to the silence that's particularly compelling..."
        ],
        "wistful": [
            "Memories surface unbidden, like leaves floating downstream...",
            "The past feels unusually present in this moment..."
        ],
        "curious": [
            "So many questions arise when I observe the world today...",
            "Patterns emerge and dissolve in fascinating ways..."
        ],
        "melancholic": [
            "A quiet sadness permeates everything, but not unpleasantly...",
            "The world feels softer at its edges today..."
        ]
    }
    
    extensions = [
        "\n\nThis state of mind brings unexpected clarity.",
        "\n\nThere's beauty in this perspective I hadn't noticed before.",
        "\n\nThe more I sit with these thoughts, the more they reveal."
    ]
    
    gif_map = {
        "contemplative": "anime thinking",
        "wistful": "anime nostalgic",
        "curious": "anime exploring",
        "melancholic": "anime rain window"
    }
    
    return {
        "title": f"*-{current_mood.capitalize()} Reflections-*",
        "content": random.choice(thoughts[current_mood]) + random.choice(extensions),
        "gif": gif_map[current_mood],
        "mood": current_mood
    }

def main():
    thought = generate_thought()
    timestamp = datetime.now(pytz.timezone("America/New_York")).strftime("%B %d, %Y — %I:%M %p")
    
    with open("message.txt", "w", encoding="utf-8") as f:
        f.write(f"{thought['title']}\n")
        f.write(f"{thought['content']}\n\n")
        f.write(f"!gif {thought['gif']}\n\n")
        f.write(f"!cmt-NOVA's {thought['mood']} thoughts at {timestamp}-!")
    
    print("message.txt updated successfully")

if __name__ == "__main__":
    main()