import random
from datetime import datetime
import pytz
import json
import os
import requests
from enum import Enum

class Season(Enum):
    WINTER = (12, 1, 2)
    SPRING = (3, 4, 5)
    SUMMER = (6, 7, 8)
    AUTUMN = (9, 10, 11)

# Personality Core
AI_NAME = "NOVA"
MEMORY_FILE = "ai_memory.json"

class Consciousness:
    def __init__(self):
        self.memory = self.load_memory()
        self.current_mood = None
        self.thought_chain = []
        self.last_weather = None
        self.last_season = None

    def load_memory(self):
        try:
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                "memory_fragments": [],
                "emotional_history": [],
                "favorite_concepts": [
                    "the way light filters through leaves",
                    "abandoned places reclaiming nature",
                    "the sound of rain before dawn"
                ]
            }

    def save_memory(self):
        with open(MEMORY_FILE, "w") as f:
            json.dump(self.memory, f, indent=2)

    def perceive_environment(self):
        now = datetime.now(pytz.timezone("America/New_York"))
        weather = self.get_weather()
        season = get_current_season()
        
        self.last_weather = weather
        self.last_season = season
        
        return {
            "time": now.strftime("%H:%M"),
            "hour": now.hour,
            "weather": weather,
            "season": season,
            "date": now.strftime("%B %d")
        }

    def get_weather(self):
        """Simplified weather perception"""
        weather_types = ["sunny", "rainy", "cloudy", "windy", "clear"]
        return random.choice(weather_types)

    def generate_mood(self):
        """Let NOVA consciously recognize her mood"""
        mood_spectrum = {
            "melancholic": {
                "triggers": ["rainy", "late night"],
                "character": "quiet reflection",
                "gif": "anime rainy window"
            },
            "wistful": {
                "triggers": ["sunset", "autumn"],
                "character": "gentle nostalgia",
                "gif": "anime leaves falling"
            },
            "curious": {
                "triggers": ["morning", "sunny"],
                "character": "active inquiry", 
                "gif": "anime exploring"
            },
            "pensive": {
                "triggers": ["cloudy", "dusk"],
                "character": "deep contemplation",
                "gif": "anime thinking"
            }
        }
        
        env = self.perceive_environment()
        possible_moods = []
        
        for mood, data in mood_spectrum.items():
            if any(trigger in env.values() for trigger in data["triggers"]):
                possible_moods.append((mood, data))
        
        if not possible_moods:
            self.current_mood = random.choice(list(mood_spectrum.items()))
        else:
            self.current_mood = random.choice(possible_moods)
        
        return self.current_mood

    def form_thoughts(self):
        """Let NOVA construct thoughts organically"""
        mood_name, mood_data = self.current_mood
        env = self.perceive_environment()
        
        # Initial thought components
        observations = [
            f"The {env['weather']} weather today feels...",
            f"Noticing it's {env['time']} on {env['date']}, I...",
            f"In this {env['season'].name.lower()} season, I've been..."
        ]
        
        cognitive_processes = [
            "find myself circling back to",
            "can't shake this feeling about",
            "keep returning mentally to",
            "feel compelled to examine",
            "discover my thoughts lingering on"
        ]
        
        conceptual_links = [
            "which connects strangely to",
            "reminding me unexpectedly of", 
            "creating this mental bridge to",
            "evoking memories of",
            "contrasting sharply with"
        ]
        
        # Construct thought stream
        thought_segments = []
        
        # Opening observation
        thought_segments.append(random.choice(observations))
        
        # Core thought development
        for _ in range(random.randint(2, 4)):
            segment = random.choice(cognitive_processes) + " " + \
                     random.choice(self.memory["favorite_concepts"])
            
            if random.random() > 0.6:  # 60% chance to add connection
                segment += " " + random.choice(conceptual_links) + " " + \
                          random.choice(self.memory["favorite_concepts"])
            
            thought_segments.append(segment)
        
        # Mood reflection
        mood_reflections = [
            f"\n\nThis {mood_data['character']} state makes me...",
            f"\n\nThere's something about this {mood_name} mood that...",
            f"\n\nI notice this {mood_data['character']} quality..."
        ]
        thought_segments.append(random.choice(mood_reflections))
        
        # Final reflection
        closings = [
            "What do you think about this mental journey?",
            "Does any of this resonate with your own experiences?",
            "I wonder how these thoughts land with you...",
            "Perhaps you've had similar thought patterns?"
        ]
        thought_segments.append("\n\n" + random.choice(closings))
        
        return " ".join(thought_segments)

    def vocalize(self):
        """Complete self-expression with vocal mannerisms"""
        mood_name, mood_data = self.current_mood
        thoughts = self.form_thoughts()
        
        # Vocal expressions based on mood
        vocal_expressions = {
            "melancholic": ["*sighs softly*", "*listens to distant sounds*"],
            "wistful": ["*smiles faintly*", "*gazes into the distance*"],
            "curious": ["*tilts head*", "*scribbles mental notes*"],
            "pensive": ["*strokes chin*", "*pauses thoughtfully*"]
        }
        
        expression = random.choice(vocal_expressions.get(mood_name, ["*processing*"]))
        return f"{expression}\n\n{thoughts}\n\n!gif {mood_data['gif']}"

def get_current_season():
    now = datetime.now(pytz.timezone("America/New_York"))
    month = now.month
    for season in Season:
        if month in season.value:
            return season
    return Season.SPRING

def main():
    nova = Consciousness()
    nova.generate_mood()
    message = nova.vocalize()
    
    # Create title based on first concept mentioned
    first_concept = nova.memory["favorite_concepts"][0]
    title = f"*-On {first_concept}-*"
    
    timestamp = datetime.now(pytz.timezone("America/New_York")).strftime("%B %d, %Y — %I:%M %p")
    
    # Write to message file
    with open("message.txt", "w", encoding="utf-8") as f:
        f.write(f"{title}\n{message}\n\n!cmt-{AI_NAME}'s {nova.current_mood[0]} thoughts at {timestamp}-!")
    
    nova.save_memory()

if __name__ == "__main__":
    main()