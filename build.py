import re
import pytz
import os
import requests
from datetime import datetime
from dotenv import load_dotenv  # type: ignore

# Load environment variables
load_dotenv()

# Get Tenor API key
TENOR_API_KEY = os.getenv("TENOR_API_KEY")
if not TENOR_API_KEY:
    raise ValueError("❌ TENOR_API_KEY is not set in the environment or .env file.")

# Fetch anime-style GIF from Tenor
def fetch_anime_gif(keyword):
    query = f"{keyword} anime"
    url = "https://tenor.googleapis.com/v2/search"
    params = {
        "q": query,
        "key": TENOR_API_KEY,
        "limit": 1,
        "media_filter": "minimal",
        "contentfilter": "high"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get("results")
        if results:
            return results[0]["media_formats"]["gif"]["url"]
    return None

# Specify the timezone
user_timezone = pytz.timezone("America/New_York")  # Replace as needed

# Read message.txt
with open("message.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

content_lines = []
titles = []

# Parse message lines
for line in lines:
    line = line.strip()

    if not line:
        content_lines.append("")  # Preserve paragraph breaks
        continue

    if line.startswith("!cmt"):
        continue

    line = re.sub(r"!cmt-.*?-!", "", line)

    # Handle title
    if re.match(r"\*-.+?-\*", line):
        titles.append(line)
        continue

    # Handle image
    if line.startswith("!pic "):
        link = line[5:].strip()
        content_lines.append(f'<div class="post-image"><img src="{link}" alt="Image" /></div>')
        continue

    # Handle GIF
    if line.startswith("!gif "):
        keyword = line[5:].strip()
        gif_url = fetch_anime_gif(keyword)
        if gif_url:
            content_lines.append(f'<div class="post-gif"><img src="{gif_url}" alt="{keyword} gif" /></div>')
        else:
            content_lines.append(f'<div class="post-gif">[GIF not found for: {keyword}]</div>')
        continue

    content_lines.append(line)

# Format content with paragraph breaks
html_content = "<br><br>".join(content_lines).replace("\n", " ")

# Handle title logic
if len(titles) > 1:
    title_text = "Too Much Title"
elif titles:
    title_text = re.sub(r"^\*-(.+?)-\*$", r"\1", titles[0])
else:
    title_text = "My Retro Adventure"

# Get current datetime
now_utc = datetime.now(pytz.utc)
user_time = now_utc.astimezone(user_timezone)
formatted_datetime = user_time.strftime("%B %d, %Y — %I:%M %p")

# Load HTML template
with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

# Populate template
final_html = (
    template.replace("{{content}}", html_content)
            .replace("{{date}}", formatted_datetime)
            .replace("My Retro Adventure", title_text)
)

# Output HTML
with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("✅ index.html updated!")
