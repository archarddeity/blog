# nova_brain.py

import random
from brain.subjects import get_subjects
from brain.verbs import get_verbs
from brain.structures import construct_sentence
from brain.gif_map import get_gif


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
        moods = ['contemplative', 'wistful', 'curious', 'melancholic']
        return moods[mood_seed]

    def generate_thought(self):
        """Create completely original thought about current state"""
        now = datetime.now(self.timezone)
        time_qualities = {
            'morning': (5, 11),
            'afternoon': (12, 17),
            'evening': (18, 22),
            'night': (23, 4)
        }
        
        # Determine time of day
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
        extension = random.choice([ 
            "\n\nThis realization lingers differently today...", 
            "\n\nThere's more beneath the surface...", 
            "\n\nThe thought unfolds in unexpected ways..." 
        ])
        
        gif = get_gif(self.current_mood)

        message = f"*-NOVA's {self.current_mood.capitalize()} State-*\n"
        message += f"{thought}{extension}\n\n"
        message += f"!gif {gif}\n\n"
        message += f"!cmt-Generated at {timestamp} in {self.timezone.tzname(None)}-!"
        
        return message

