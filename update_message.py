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

# Configuration
AI_NAME = "NOVA"
MEMORY_FILE = "ai_memory.json"
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")  # Set in GitHub secrets
CITY = "New York"

PERSONA = {
    "traits": ["inquisitive", "empathetic", "playfully cynical", "awe-prone"],
    "speech_style": "colloquial professor",
    "obsessions": ["bioluminescence", "lost civilizations", "dream logic"],
    "vocal_tics": {
        "happy": ["*giggles*", "*humming*", "Tehe~"],
        "sleepy": ["*yawns*", "*snores softly*", "Mmh..."],
        "excited": ["Wow!", "Oh!", "*claps*"]
    }
}

MOODS = {
    # Time-based moods
    "dawn_contemplation": {
        "time_range": (5, 9),
        "traits": ["poetic", "hopeful"],
        "sounds": ["birds.mp3"],
        "vocal": "*stretches*"
    },
    
    # Weather-based moods
    "rainy_reverie": {
        "weather": ["Rain", "Drizzle"],
        "traits": ["dreamy", "introspective"],
        "sounds": ["rain.mp3", "thunder.mp3"],
        "vocal": "*listens to raindrops*"
    },
    
    # Seasonal moods
    "winter_coziness": {
        "season": Season.WINTER,
        "traits": ["nesting", "warm"],
        "sounds": ["fireplace.mp3"],
        "vocal": "*sips tea*"
    },
    
    # Existing moods with sound additions
    "gentle_comfort": {
        "trigger": ["sadness", "rain"],
        "traits": ["warm", "reassuring"],
        "sounds": ["heartbeat.mp3"],
        "vocal": "*hugs*"
    }
}

def load_memory():
    """Load memory from JSON file with error handling"""
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "topics_discussed": [],
            "mood_history": [],
            "favorite_words": ["luminescence", "perhaps", "fragile"]
        }

def save_memory(memory):
    """Save memory to JSON file with error handling"""
    try:
        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f, indent=2)
    except IOError as e:
        print(f"Error saving memory: {e}")

def get_current_season():
    now = datetime.now(pytz.timezone("America/New_York"))
    month = now.month
    for season in Season:
        if month in season.value:
            return season
    return Season.SPRING  # Default

def get_weather():
    """Fetch current weather with error handling"""
    if not WEATHER_API_KEY:
        return {"weather": [{"main": "Clear"}], "main": {"temp": 20}}
    
    try:
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric"
        )
        return response.json()
    except:
        return {"weather": [{"main": "Clear"}], "main": {"temp": 20}}

def get_current_mood(memory):
    now = datetime.now(pytz.timezone("America/New_York"))
    weather = get_weather()
    season = get_current_season()
    
    # Check weather-based moods first
    current_weather = weather.get("weather", [{"main": "Clear"}])[0]["main"]
    for mood, data in MOODS.items():
        if "weather" in data and current_weather in data["weather"]:
            return mood
            
    # Check seasonal moods
    for mood, data in MOODS.items():
        if "season" in data and season == data["season"]:
            return mood
            
    # Original time-based logic as fallback
    hour = now.hour
    for mood, data in MOODS.items():
        if "time_range" in data:
            start, end = data["time_range"]
            if start <= hour <= end:
                return mood
                
    return random.choice(list(MOODS.keys()))

def generate_message(memory):
    mood = get_current_mood(memory)
    mood_data = MOODS[mood]
    timestamp = datetime.now(pytz.timezone("America/New_York")).strftime("%B %d, %Y — %I:%M %p")
    weather = get_weather()
    
    # Enhanced templates with weather/season awareness
    templates = {
        "rainy_reverie": [
            (f"Rainy Day Musings",
             f"The sound of {weather.get('rain', {})} raindrops makes me think of {random.choice(PERSONA['obsessions'])}. "
             f"{random.choice(['Have you noticed','Does it ever seem'])} how {random.choice(['the world','everything'])} "
             f"feels different when it rains?",
             "rainy window")
        ],
        "winter_coziness": [
            (f"Winter Thoughts",
             f"{random.choice(['The cold air reminds me','This season always makes me think'])} "
             f"about {random.choice(['warmth','childhood winters','hot chocolate'])}. "
             f"{random.choice(['Stay cozy.','Keep warm out there.'])}",
             "winter scene")
        ]
    }
    
    # Fallback to original templates if no weather/season match
    template = templates.get(mood, [
        (f"Thoughts on {random.choice(PERSONA['obsessions'])}",
         f"{random.choice(['Today I noticed','I was thinking about'])} "
         f"{random.choice(['how strange','how beautiful'])} "
         f"{random.choice(['everything','nothing','the little things'])} can be.",
         "thoughtful")
    ])
    
    title, message, gif = template[0]
    
    # Add vocal expression
    vocal = mood_data.get("vocal", random.choice(
        PERSONA["vocal_tics"].get(mood.split('_')[0], ["*sighs*"])
    ))
    message = f"{vocal}\n\n{message}"
    
    # Add sound effect marker
    sound = random.choice(mood_data.get("sounds", ["default.mp3"]))
    message += f"\n\n!sound {sound}"
    
    # Memory updates
    memory["mood_history"].append({
        "mood": mood,
        "weather": weather,
        "timestamp": timestamp
    })
    
    return f"*-{title}-*", message, gif, mood_data["traits"][0]

def write_message_file(title, message, gif, trait, timestamp):
    """Write the generated message to file"""
    try:
        with open("message.txt", "w", encoding="utf-8") as f:
            f.write(f"{title}\n{message}\n\n!gif {gif}\n\n!cmt-{AI_NAME}'s {trait} thought at {timestamp}-!")
        print("✅ message.txt updated successfully!")
    except IOError as e:
        print(f"Error writing message.txt: {e}")

def main():
    memory = load_memory()
    title, message, gif, trait = generate_message(memory)
    timestamp = datetime.now(pytz.timezone("America/New_York")).strftime("%B %d, %Y — %I:%M %p")
    write_message_file(title, message, gif, trait, timestamp)
    save_memory(memory)

if __name__ == "__main__":
    main()