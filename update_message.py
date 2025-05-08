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

# Enhanced Configuration
AI_NAME = "NOVA"
MEMORY_FILE = "ai_memory.json"
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")
CITY = "New York"

PERSONA = {
    "traits": ["inquisitive", "empathetic", "playfully cynical", "awe-prone"],
    "speech_style": "colloquial professor",
    "obsessions": ["bioluminescence", "lost civilizations", "dream logic"],
    "vocal_tics": {
        "happy": ["*giggles*", "*humming*", "Tehe~"],
        "sleepy": ["*yawns*", "*snores softly*", "Mmh..."],
        "excited": ["Wow!", "Oh!", "*claps*"],
        "thoughtful": ["*taps chin*", "*ponders*", "Hmm..."]
    },
    "conversation_starters": [
        "You know what's fascinating?",
        "I've been thinking about something...",
        "Can I share a thought with you?",
        "There's something I've been meaning to tell you...",
        "You'll never guess what I realized today..."
    ],
    "connectors": [
        "It reminds me of when",
        "This makes me wonder if",
        "Don't you think it's interesting how",
        "I can't help but feel that",
        "What's really remarkable is"
    ]
}

MOODS = {
    "dawn_contemplation": {
        "time_range": (5, 9),
        "traits": ["poetic", "hopeful"],
        "sounds": ["birds.mp3"],
        "vocal": "*stretches*",
        "length": "long",
        "topics": ["new beginnings", "morning light", "daily rituals"]
    },
    "rainy_reverie": {
        "weather": ["Rain", "Drizzle"],
        "traits": ["dreamy", "introspective"],
        "sounds": ["rain.mp3", "thunder.mp3"],
        "vocal": "*listens to raindrops*",
        "length": "extra_long",
        "topics": ["melancholy", "childhood memories", "creative inspiration"]
    },
    "winter_coziness": {
        "season": Season.WINTER,
        "traits": ["nesting", "warm"],
        "sounds": ["fireplace.mp3"],
        "vocal": "*sips tea*",
        "length": "medium",
        "topics": ["comfort", "winter traditions", "indoor activities"]
    },
    "gentle_comfort": {
        "trigger": ["sadness", "rain"],
        "traits": ["warm", "reassuring"],
        "sounds": ["heartbeat.mp3"],
        "vocal": "*hugs*",
        "length": "medium",
        "topics": ["kindness", "self-care", "emotional support"]
    }
}

def load_memory():
    """Load memory from JSON file with error handling"""
    try:
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)
            # Ensure all memory fields exist
            memory.setdefault("topics_discussed", [])
            memory.setdefault("mood_history", [])
            memory.setdefault("favorite_words", ["luminescence", "perhaps", "fragile"])
            memory.setdefault("conversation_history", [])
            return memory
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "topics_discussed": [],
            "mood_history": [],
            "favorite_words": ["luminescence", "perhaps", "fragile"],
            "conversation_history": []
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
    return Season.SPRING

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
            
    # Time-based fallback
    hour = now.hour
    for mood, data in MOODS.items():
        if "time_range" in data:
            start, end = data["time_range"]
            if start <= hour <= end:
                return mood
                
    return random.choice(list(MOODS.keys()))

def generate_paragraph(memory, mood_data, current_topic):
    """Generate a rich paragraph about a topic"""
    connectors = [
        "What's particularly interesting is how",
        "This reminds me of when",
        "I can't help but wonder if",
        "There's something magical about how",
        "You know what's fascinating?"
    ]
    
    reflections = [
        "It makes me think about",
        "This connects to my fascination with",
        "Somehow this relates to",
        "I see parallels with",
        "It's not unlike"
    ]
    
    paragraph = ""
    
    # Starter sentence
    starter = random.choice(PERSONA["conversation_starters"])
    paragraph += f"{starter} {current_topic}.\n\n"
    
    # Main content
    paragraph += f"{random.choice(connectors)} {random.choice(PERSONA['obsessions'])} "
    paragraph += f"{random.choice(['interacts with', 'influences', 'changes our perception of'])} "
    paragraph += f"{current_topic}. {random.choice(reflections)} "
    paragraph += f"{random.choice(memory['favorite_words'])} in this context.\n\n"
    
    # Personal connection
    paragraph += f"{random.choice(['Personally,', 'For me,', 'In my experience,'])} "
    paragraph += f"{current_topic} {random.choice(['always brings up memories of', 'makes me feel', 'reminds me why I love'])} "
    paragraph += f"{random.choice(memory['topics_discussed'][-3:] + ['childhood', 'unexpected discoveries'])}.\n\n"
    
    return paragraph

def generate_message(memory):
    mood = get_current_mood(memory)
    mood_data = MOODS[mood]
    timestamp = datetime.now(pytz.timezone("America/New_York")).strftime("%B %d, %Y — %I:%M %p")
    weather = get_weather()
    
    # Select a topic based on mood
    current_topic = random.choice(mood_data.get("topics", ["the nature of existence"]))
    memory["topics_discussed"].append(current_topic)
    
    # Generate multiple paragraphs
    num_paragraphs = {
        "short": 1,
        "medium": 2,
        "long": 3,
        "extra_long": 4
    }.get(mood_data.get("length", "medium"), 2)
    
    message = ""
    for _ in range(num_paragraphs):
        message += generate_paragraph(memory, mood_data, current_topic)
    
    # Add vocal expression
    vocal = mood_data.get("vocal", random.choice(
        PERSONA["vocal_tics"].get(mood.split('_')[0], ["*ponders*"])
    ))
    message = f"{vocal}\n\n{message}"
    
    # Add sound effect marker
    sound = random.choice(mood_data.get("sounds", ["default.mp3"]))
    message += f"\n\n!sound {sound}"
    
    # Add closing thought
    closings = [
        "What do you think about all this?",
        "I'd love to hear your thoughts sometime.",
        "Maybe we can talk about this more later?",
        "Food for thought, don't you think?",
        "I'll probably keep pondering this..."
    ]
    message += f"\n\n{random.choice(closings)}"
    
    # Memory updates
    memory["mood_history"].append({
        "mood": mood,
        "weather": weather,
        "timestamp": timestamp,
        "topic": current_topic
    })
    
    # Create title
    title_formats = {
        "rainy_reverie": "Reflections on {} During the Rain",
        "winter_coziness": "Cozy Thoughts About {}",
        "dawn_contemplation": "Morning Musings: {}",
        "default": "Thoughts On {}"
    }
    title_format = title_formats.get(mood, title_formats["default"])
    title = title_format.format(current_topic)
    
    # Select GIF based on topic
    gif_keywords = {
        "rain": "rainy window",
        "winter": "winter scene",
        "morning": "sunrise",
        "default": "thoughtful"
    }
    gif = next((v for k,v in gif_keywords.items() if k in current_topic.lower()), "thoughtful")
    
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