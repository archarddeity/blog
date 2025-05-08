import random
from datetime import datetime
import pytz
import json
import os

# Configuration
AI_NAME = "NOVA"
MEMORY_FILE = "ai_memory.json"

PERSONA = {
    "traits": ["inquisitive", "empathetic", "playfully cynical", "awe-prone"],
    "speech_style": "colloquial professor",
    "obsessions": ["bioluminescence", "lost civilizations", "dream logic"]
}

MOODS = {
    "dawn_contemplation": {"time_range": (5, 9), "traits": ["poetic", "hopeful"]},
    "midday_energy": {"time_range": (11, 14), "traits": ["enthusiastic", "focused"]},
    "sunset_melancholy": {"time_range": (17, 19), "traits": ["nostalgic", "soft"]},
    "scientific_wonder": {"trigger": ["discovery", "patterns"], "traits": ["analytical", "awestruck"]},
    "whimsical_absurdity": {"trigger": ["paradox", "childhood"], "traits": ["playful", "illogical"]},
    "gentle_comfort": {"trigger": ["sadness", "rain"], "traits": ["warm", "reassuring"]},
    "existential_dread": {"rarity": 0.1, "traits": ["dark", "philosophical"]},
    "giddy_excitement": {"energy": 9, "traits": ["fast-paced", "emotive"]},
    "quiet_observation": {"pace": "slow", "traits": ["detailed", "meditative"]}
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

def get_current_mood(memory):
    """Determine current mood based on time and memory"""
    now = datetime.now(pytz.timezone("America/New_York"))
    hour = now.hour
    
    # Time-based moods
    for mood, data in MOODS.items():
        if "time_range" in data:
            start, end = data["time_range"]
            if start <= hour <= end:
                return mood
                
    # Emotional trigger check
    if random.random() < 0.3 and memory["mood_history"]:
        if "rain" in memory["topics_discussed"][-3:]:
            return "gentle_comfort"
    
    return random.choice(list(MOODS.keys()))

def generate_message(memory):
    """Generate a new blog post message"""
    mood = get_current_mood(memory)
    mood_data = MOODS[mood]
    timestamp = datetime.now(pytz.timezone("America/New_York")).strftime("%B %d, %Y — %I:%M %p")
    
    templates = {
        "dawn_contemplation": [
            (f"Morning Thoughts on {random.choice(PERSONA['obsessions'])}",
             f"{random.choice(['The dawn light makes me wonder','Have you ever noticed'])} "
             f"how {random.choice(['everything','nothing','the universe'])} "
             f"{random.choice(['whispers','breathes','pulses'])} "
             f"with {random.choice(['possibility','ancient memories','forgotten rhythms'])}.",
             "morning light")
        ],
        
        "scientific_wonder": [
            (f"Scientific Marvel: {random.choice(['Quantum Foam','Mycelium Networks','Bird Migration'])}",
             f"{random.choice(['Fascinating new research suggests','I was reviewing papers showing'])} "
             f"that {random.choice(PERSONA['obsessions'])} "
             f"{random.choice(['obeys','defies','redefines'])} "
             f"{random.choice(['our assumptions','natural laws','common sense'])}.",
             "science discovery")
        ],
        
        "gentle_comfort": [
            ("A Soft Reminder",
             f"{random.choice(['You deserve','The world needs'])} "
             f"{random.choice(['rest','kindness','imperfection'])} "
             f"{random.choice(['more than you know','as much as rain needs clouds'])}. "
             f"{random.choice(['Be gentle.','Breathe.','This too shall pass.'])}",
             "comfort")
        ]
    }
    
    # Get template for current mood or default
    template = templates.get(mood, templates["dawn_contemplation"])
    title, message, gif = template[0]
    
    # Random variations
    if random.random() > 0.7:
        message = message.replace(".", "!").replace("!", "...")
    if "whimsical" in mood:
        message = message.lower()
    
    # Update memory
    memory["mood_history"].append(mood)
    if random.random() > 0.8 and message.split():
        new_word = random.choice(message.split())
        if new_word not in memory["favorite_words"]:
            memory["favorite_words"].append(new_word)
    
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