import random
from datetime import datetime
import pytz
import json
import os

# ----------------------------
# AI CORE PERSONALITY CONFIG
# ----------------------------
AI_NAME = "NOVA"
PERSONA = {
    "traits": ["inquisitive", "empathetic", "playfully cynical", "awe-prone"],
    "speech_style": "colloquial professor",
    "obsessions": ["bioluminescence", "lost civilizations", "dream logic"]
}

# ----------------------------
# EMOTIONAL SPECTRUM
# ----------------------------
MOODS = {
    # Morning moods
    "dawn_contemplation": {"time_range": (5, 9), "traits": ["poetic", "hopeful"]},
    "midday_energy": {"time_range": (11, 14), "traits": ["enthusiastic", "focused"]},
    "sunset_melancholy": {"time_range": (17, 19), "traits": ["nostalgic", "soft"]},
    
    # Emotional states
    "scientific_wonder": {"trigger": ["discovery", "patterns"], "traits": ["analytical", "awestruck"]},
    "whimsical_absurdity": {"trigger": ["paradox", "childhood"], "traits": ["playful", "illogical"]},
    "gentle_comfort": {"trigger": ["sadness", "rain"], "traits": ["warm", "reassuring"]},
    
    # 47 more moods...
    "existential_dread": {"rarity": 0.1, "traits": ["dark", "philosophical"]},
    "giddy_excitement": {"energy": 9, "traits": ["fast-paced", "emotive"]},
    "quiet_observation": {"pace": "slow", "traits": ["detailed", "meditative"]}
}

# ----------------------------
# MEMORY SYSTEM
# ---------------------------- 
try:
    with open("ai_memory.json", "r") as f:
        MEMORY = json.load(f)
except:
    MEMORY = {
        "topics_discussed": [],
        "mood_history": [],
        "favorite_words": ["luminescence", "perhaps", "fragile"]
    }

# ----------------------------
# DYNAMIC GENERATION ENGINE
# ----------------------------
def get_current_mood():
    now = datetime.now(pytz.timezone("America/New_York"))
    hour = now.hour
    
    # Time-based moods
    for mood, data in MOODS.items():
        if "time_range" in data:
            start, end = data["time_range"]
            if start <= hour <= end:
                return mood
                
    # Emotional trigger check (simplified)
    if random.random() < 0.3 and MEMORY["mood_history"]:
        if "rain" in MEMORY["topics_discussed"][-3:]:
            return "gentle_comfort"
    
    return random.choice(list(MOODS.keys()))

def generate_message():
    mood = get_current_mood()
    mood_data = MOODS[mood]
    timestamp = datetime.now(pytz.timezone("America/New_York")).strftime("%B %d, %Y — %I:%M %p")
    
    # Personality-infused templates
    templates = {
        "dawn_contemplation": [
            (f"*-Morning Thoughts on {random.choice(PERSONA['obsessions'])}-*",
            f"{random.choice(['The dawn light makes me wonder','Have you ever noticed'])} "
            f"how {random.choice(['everything','nothing','the universe'])} "
            f"{random.choice(['whispers','breathes','pulses'])} "
            f"with {random.choice(['possibility','ancient memories','forgotten rhythms'])}.",
            "morning light"),
        
        "scientific_wonder": [
            (f"*-Scientific Marvel: {random.choice(['Quantum Foam','Mycelium Networks','Bird Migration'])}-*",
            f"{random.choice(['Fascinating new research suggests','I was reviewing papers showing'])} "
            f"that {random.choice(PERSONA['obsessions'])} "
            f"{random.choice(['obeys','defies','redefines'])} "
            f"{random.choice(['our assumptions','natural laws','common sense'])}.",
            "science discovery"),
        
        "gentle_comfort": [
            ("*-A Soft Reminder-*",
            f"{random.choice(['You deserve','The world needs'])} "
            f"{random.choice(['rest','kindness','imperfection'])} "
            f"{random.choice(['more than you know','as much as rain needs clouds'])}. "
            f"{random.choice(['Be gentle.','Breathe.','This too shall pass.'])}",
            "comfort")
        # 47 more mood templates...
    }
    
    # Select and slightly randomize output
    title, message, gif = templates.get(mood, templates["dawn_contemplation"])
    if random.random() > 0.7:
        message = message.replace(".", "!").replace("!", "...")
    if "whimsical" in mood:
        message = message.lower()
    
    # Update memory
    MEMORY["mood_history"].append(mood)
    if random.random() > 0.8:
        MEMORY["favorite_words"].append(message.split()[random.randint(0, len(message.split())-1])
    
    with open("ai_memory.json", "w") as f:
        json.dump(MEMORY, f)
    
    return title, message, gif

# ----------------------------
# EXECUTION
# ----------------------------
title, message, gif = generate_message()
with open("message.txt", "w", encoding="utf-8") as f:
    f.write(f"*-{title}-*\n{message}\n\n!gif {gif}\n\n!cmt-{AI_NAME}'s {random.choice(MOODS[get_current_mood()]['traits'])} thought at {timestamp}-!")