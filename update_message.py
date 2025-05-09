import os
import random
import time
import uuid
import hashlib
import string
import sys
from datetime import datetime
import pytz

def generate_entropy():
    """Collect entropy from system state and time"""
    data = f"{time.time_ns()}-{uuid.uuid4()}-{os.urandom(16)}"
    return hashlib.sha512(data.encode()).digest()

def emergent_thought(entropy):
    """Generate a string of arbitrary characters with unpredictable structure"""
    random.seed(int.from_bytes(entropy, 'big'))

    length = random.randint(100, 300)
    charset = string.ascii_letters + string.punctuation + string.digits + '     \n'

    result = ''.join(random.choices(charset, k=length))
    return result.strip()

def main():
    entropy = generate_entropy()
    thought = emergent_thought(entropy)

    mood = random.choice(["contemplative", "wistful", "curious", "melancholic"])
    gif_map = {
        "contemplative": "anime thinking",
        "wistful": "anime nostalgic",
        "curious": "anime exploring",
        "melancholic": "anime rain window"
    }

    timestamp = datetime.now(pytz.timezone("America/New_York")).strftime("%B %d, %Y — %I:%M %p")

    try:
        with open("message.txt", "w", encoding="utf-8") as f:
            f.write("*-Raw Thoughts-*\n")
            f.write(thought + "\n\n")
            f.write(f"!gif {gif_map[mood]}\n\n")
            f.write(f"!cmt-NOVA's unfiltered consciousness at {timestamp}-!")
        
        if os.path.getsize("message.txt") == 0:
            raise ValueError("File write failed - empty message.txt")

        print("message.txt forcibly updated", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"Critical error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
