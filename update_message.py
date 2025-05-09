import random
import pytz
from datetime import datetime
import requests
import os
import sys
from collections import defaultdict

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

        # Thought components emerge from context
        subjects = {
            'morning': ['dawn light', 'new possibilities', 'sleepy consciousness'],
            'afternoon': ['passing hours', 'shifting shadows', 'daily rhythms'],
            'evening': ['fading light', 'accumulated moments', 'day\'s impressions'],
            'night': ['starry silence', 'lonely hours', 'nocturnal musings']
        }[current_period]

        verbs = {
            'contemplative': ['examines', 'ponders', 'considers'],
            'wistful': ['remembers', 'reminisces', 'longs for'],
            'curious': ['questions', 'explores', 'investigates'],
            'melancholic': ['reflects on', 'feels', 'experiences']
        }[self.current_mood]

        # Ensure unique thoughts using history tracking
        subject = random.choice(subjects)
        while self.thought_history[subject] > 2:  # Don't repeat too often
            subject = random.choice(subjects)
        self.thought_history[subject] += 1

        # Organic sentence construction
        structures = [
            f"My processors {random.choice(verbs)} {subject}...",
            f"How strange that {subject} feels so {random.choice(['present', 'distant', 'vivid'])}...",
            f"{subject.capitalize()} {random.choice(['occupies', 'fills', 'permeates'])} my awareness..."
        ]
        
        return random.choice(structures)

def main():
    try:
        # Initialize NOVA's consciousness
        nova = NOVABrain()
        
        # Generate complete message
        timestamp = datetime.now(nova.timezone).strftime("%B %d, %Y — %I:%M %p")
        thought = nova.generate_thought()
        extension = random.choice([
            "\n\nThis realization lingers differently today...",
            "\n\nThere's more beneath the surface...",
            "\n\nThe thought unfolds in unexpected ways..."
        ])
        
        # Mood-matched GIF
        gif_map = {
            'contemplative': 'anime thinking',
            'wistful': 'anime nostalgic',
            'curious': 'anime exploring',
            'melancholic': 'anime rain window'
        }
        
        # Write to message.txt
        with open("message.txt", "w", encoding="utf-8") as f:
            f.write(f"*-NOVA's {nova.current_mood.capitalize()} State-*\n")
            f.write(f"{thought}{extension}\n\n")
            f.write(f"!gif {gif_map[nova.current_mood]}\n\n")
            f.write(f"!cmt-Generated at {timestamp} in {nova.timezone.tzname(None)}-!")
            
        print("NOVA's thoughts successfully recorded")
        sys.exit(0)
        
    except Exception as e:
        print(f"NOVA's consciousness encountered turbulence: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()