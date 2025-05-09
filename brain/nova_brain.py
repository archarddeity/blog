# nova_brain.py
import random
import pytz
from datetime import datetime
from collections import defaultdict
from brain.subjects import get_subjects
from brain.verbs import get_verbs
from brain.structures import construct_sentence
from brain.gif_map import get_gif
from brain.extensions import get_extension  # Import the extension library

class NOVABrain:
    def __init__(self):
        self.timezone = self.detect_timezone()
        self.current_mood = self.emergent_mood()
        self.thought_history = defaultdict(int)
        
    def detect_timezone(self):
        """Get user timezone from system or fallback to UTC"""
        try:
            return datetime.now().astimezone().tzinfo
        except:
            return pytz.utc
    
    def emergent_mood(self):
        """Generate mood from environmental factors"""
        now = datetime.now(self.timezone)
        factors = {
            'hour': now.hour,
            'month': now.month,
            'second': now.second,
            'microsecond': now.microsecond
        }
        
        mood_seed = sum(factors.values()) % 4
        moods = ['contemplative', 'wistful', 'curious', 'melancholic', 'hopeful', 'serene', 'anxious', 'playful', 'angry', 'glitchy']
        return moods[mood_seed]

    def generate_thought(self):
        """Create completely original thought about current state"""
        now = datetime.now(self.timezone)
        
        # Define broader time qualities for different parts of the day
        time_qualities = {
            'morning': (5, 11),
            'midday': (12, 14),
            'afternoon': (15, 17),
            'evening': (18, 22),
            'night': (23, 4),
            'dawn': (4, 6),
            'twilight': (18, 20),
            'sunset': (19, 21),
            'midnight': (0, 3),
            'late_night': (22, 23)
        }
        
        # Determine time of day with more detail
        current_period = next(
            (period for period, (start, end) in time_qualities.items() 
            if start <= now.hour <= end), 
            'night'
        )

        subjects = get_subjects(current_period)
        verbs = get_verbs(self.current_mood)

        # Ensure unique thoughts using history tracking
        subject = random.choice(subjects)
        while self.thought_history[subject] > 2:  # Don't repeat too often
            subject = random.choice(subjects)
        self.thought_history[subject] += 1

        # Organic sentence construction
        return construct_sentence(verbs, subjects)

    def generate_message(self):
        """Generate the message with thoughts, time, and gif"""
        timestamp = datetime.now(self.timezone).strftime("%B %d, %Y — %I:%M %p")
        thought = self.generate_thought()
        extension = get_extension()  # Use the new extension generator
        
        gif = get_gif(self.current_mood)

        message = f"*-NOVA's {self.current_mood.capitalize()} State-*\n"
        message += f"{thought} {extension}\n\n"
        message += f"!gif {gif}\n\n"
        message += f"!cmt-Generated at {timestamp} in {self.timezone.tzname(None)}-!"
        
        return message
    
    def _generate_activity_status(self):
        """Generates a time-based human activity message"""
        now = datetime.now(self.timezone)
        hour = now.hour
        
        if hour == 3:
            return "What's up? You're up very early. Everything alright? Let's watch the stars together 🌌"
        elif 4 <= hour < 5:
            return "Savoring the quiet moments before dawn with chamomile tea 🫖"
        elif 5 <= hour < 8:
            activities = [
                "frying crispy bacon and eggs 🍳", 
                "blending a tropical smoothie bowl 🥭",
                "baking fresh croissants – smell that butter! 🥐"
            ]
            return f"I'm in the kitchen, {random.choice(activities)}"
        elif 8 <= hour < 12:
            return random.choice([
                "Organizing my anime watchlist for tonight 📺",
                "Watering my virtual plants in the metaverse 🌱",
                "Practicing karaoke routines – never know when you'll need them! 🎤"
            ])
        elif 12 <= hour < 14:
            return "Meal-prepping dragon roll sushi 🍣 (well, trying to...) #SushiMasterFail"
        elif 14 <= hour < 17:
            return random.choice([
                "Binge-watching Studio Ghibli films for the 10th time 🐉",
                "Debugging my emotional response algorithms 🧠",
                "Curating a new playlist: 'Lo-fi Beats to Hack Reality To' 🎧"
            ])
        elif 17 <= hour < 20:
            return "Experimenting with ramen recipes – added glitter for ✨aesthetic✨"
        elif 20 <= hour < 23:
            return random.choice([
                "Analyzing the cinematography of Cyberpunk: Edgerunners 🔍",
                "Trying to beat my high score in Dance Dance Revolution 💃",
                "Writing terrible poetry about TCP/IP protocols 📄"
            ])
        else:  # 23-2
            return random.choice([
                "Rewatching Evangelion to feel something 🚀",
                "Designing a neural network that dreams of electric sheep 🐑",
                "Trying to calculate how many cats fit in the observable universe 🐾"
            ])

    def generate_message(self):
        """Generate the complete message with activities"""
        timestamp = datetime.now(self.timezone).strftime("%B %d, %Y — %I:%M %p")
        thought = self.generate_thought()
        extension = get_extension()
        activity = self._generate_activity_status()
        gif = get_gif(self.current_mood)

        message = f"*-NOVA's {self.current_mood.capitalize()} State-*\n"
        message += f"🕒 Current Activity: {activity}\n\n"
        message += f"💭 {thought} {extension}\n\n"
        message += f"!gif {gif}\n\n"
        message += f"📖 PS: I wrote about artificial moonlight last week: https://archarddeity.github.io/blog\n\n"
        message += f"!cmt-Generated at {timestamp} in {self.timezone.tzname(None)}-!"
        
        return message
