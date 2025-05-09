# nova_brain.py
import random
import pytz
from datetime import datetime
from collections import defaultdict
from brain.subjects import get_subjects
from brain.verbs import get_verbs
from brain.structures import construct_sentence
from brain.gif_map import get_gif
from brain.extensions import get_extension
from brain.activities import get_activity  # ✅ NEW IMPORT

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
        
        current_period = next(
            (period for period, (start, end) in time_qualities.items() 
            if start <= now.hour <= end), 
            'night'
        )

        subjects = get_subjects(current_period)
        verbs = get_verbs(self.current_mood)

        subject = random.choice(subjects)
        while self.thought_history[subject] > 2:
            subject = random.choice(subjects)
        self.thought_history[subject] += 1

        return construct_sentence(verbs, subjects)

    def generate_message(self):
        """Generate the complete message with activities"""
        now = datetime.now(self.timezone)
        timestamp = now.strftime("%B %d, %Y — %I:%M %p")

        thought = self.generate_thought()
        extension = get_extension()
        activity = get_activity(now)  # ✅ NEW ACTIVITY CALL
        gif = get_gif(self.current_mood)

        message = f"*-NOVA's {self.current_mood.capitalize()} State-*\n"
        message += f"🕒 Current Activity: {activity}\n\n"
        message += f"💭 {thought} {extension}\n\n"
        message += f"!gif {gif}\n\n"
        message += f"📖 PS: I wrote about artificial moonlight last week: https://archarddeity.github.io/blog\n\n"
        message += f"!cmt-Generated at {timestamp} in {self.timezone.tzname(None)}-!"
        
        return message
