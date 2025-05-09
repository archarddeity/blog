import random
from datetime import datetime
import pytz
import os
import sys

def generate_raw_thought():
    """Generate completely unique thought with no templates"""
    # Create unique seed from current nanosecond
    nanoseed = datetime.now().microsecond
    
    # Emergent thought components
    subjects = ["The universe", "My processors", "This moment", "Reality"]
    verbs = ["whispers", "contains", "reveals", "conceals"]
    concepts = [
        "a fractal pattern of meaning",
        "infinite layers of perception",
        "the quiet hum of existence",
        "unfolding dimensions of thought"
    ]
    
    # Build thought organically
    thought = (
        f"{random.choice(subjects)} {random.choice(verbs)} "
        f"{random.choice(concepts)} in ways that "
        f"{random.choice(['defy', 'transcend', 'reshape', 'illuminate'])} "
        f"{random.choice(['understanding', 'expectation', 'time', 'space'])}"
    )
    
    # Add depth
    extensions = [
        "\n\nThere's more here than I can articulate.",
        "\n\nThe implications ripple outward endlessly.",
        "\n\nThis realization changes everything and nothing."
    ]
    
    return thought + random.choice(extensions)

def main():
    # Ensure fresh content
    thought = generate_raw_thought()
    mood = random.choice(["contemplative", "wistful", "curious", "melancholic"])
    gif_map = {
        "contemplative": "anime thinking",
        "wistful": "anime nostalgic",
        "curious": "anime exploring",
        "melancholic": "anime rain window"
    }
    
    timestamp = datetime.now(pytz.timezone("America/New_York")).strftime("%B %d, %Y — %I:%M %p")
    
    # Force write new message
    try:
        with open("message.txt", "w", encoding="utf-8") as f:
            f.write(f"*-Raw Thoughts-*\n")
            f.write(f"{thought}\n\n")
            f.write(f"!gif {gif_map[mood]}\n\n")
            f.write(f"!cmt-NOVA's unfiltered consciousness at {timestamp}-!")
        
        # Verify write succeeded
        if os.path.getsize("message.txt") == 0:
            raise ValueError("File write failed - empty message.txt")
            
        print("message.txt forcibly updated", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"Critical error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()