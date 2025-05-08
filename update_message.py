import random
from datetime import datetime

# Define your encouraging message pool
messages = [
    ("You Are Doing Great", "Every effort you make, even the unseen ones, are shaping a better future.", "determination"),
    ("Keep Moving Forward", "Progress isn’t always obvious, but it’s always happening. Don’t stop now.", "hope"),
    ("You Matter", "Your existence makes a difference. Even on quiet days.", "warm smile"),
    ("Rest is Productive Too", "Taking breaks helps you grow. Be gentle with yourself.", "relax"),
    ("Shine Anyway", "Even when the world is dark, you still have your light. Let it show.", "glow"),
]

title, message, gif = random.choice(messages)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("message.txt", "w", encoding="utf-8") as f:
    f.write(f"*-{title}-*\n{message}\n\n!gif {gif}\n\n!cmt-Auto-generated on {timestamp}-!")
