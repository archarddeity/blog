import re
import pytz
import os
import hmac
import base64
import hashlib
import requests
import sys
from datetime import datetime
from dotenv import load_dotenv  # type: ignore

# Load environment variables
load_dotenv()

# --- Environment ---
TENOR_API_KEY = os.getenv("TENOR_API_KEY")
NOTION_SHARED_SECRET = os.getenv("NOTION_SHARED_SECRET")
NOTION_HASH = os.getenv("NOTION_HASH")

# Base64-encoded Notion URL for: https://www.notion.so/This-is-the-title-1ed2f479edae80de81cfe5505f44b7f7
ENCODED_NOTION_URL = "aHR0cHM6Ly93d3cubm90aW9uLnNvL1RoaXMt" \
                     "aXMtdGhlLXRpdGxlLTFlZDJmNDc5ZWRhZTgwZGU4MWNmZTU1MDVmNDRiN2Y3"

# --- Decode Notion URL ---
notion_url = base64.b64decode(ENCODED_NOTION_URL.encode()).decode()

# --- Fetch Notion content ---
response = requests.get(notion_url)
if response.status_code != 200:
    raise Exception("❌ Failed to fetch Notion content.")

notion_content = response.text.strip()

# --- Optional: Generate and print HMAC hash ---
if "--generate-hash" in sys.argv:
    if not NOTION_SHARED_SECRET:
        raise Exception("❌ NOTION_SHARED_SECRET is required to generate hash.")
    generated_hash = hmac.new(
        NOTION_SHARED_SECRET.encode(),
        notion_content.encode(),
        hashlib.sha256
    ).hexdigest()
    print("✅ HMAC SHA-256 hash for current Notion content:")
    print(generated_hash)
    sys.exit(0)

# --- Required secrets ---
if not TENOR_API_KEY or not NOTION_SHARED_SECRET or not NOTION_HASH:
    raise ValueError("❌ Missing TENOR_API_KEY, NOTION_SHARED_SECRET, or NOTION_HASH")

# --- Verify Notion content ---
computed_hash = hmac.new(
    NOTION_SHARED_SECRET.encode(),
    notion_content.encode(),
    hashlib.sha256
).hexdigest()

if computed_hash != NOTION_HASH:
    raise Exception("❌ HMAC verification failed. Content may have been tampered with.")

# --- Write verified content to message.txt ---
with open("message.txt", "w", encoding="utf-8") as f:
    f.write(notion_content)

print("✅ Notion content verified and saved to message.txt")

# --- Tenor GIF Fetcher ---
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

# --- Timezone ---
user_timezone = pytz.timezone("America/New_York")

# --- Read and Parse message.txt ---
with open("message.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

content_lines = []
titles = []

for line in lines:
    line = line.strip()

    if not line:
        content_lines.append("")  # Paragraph breaks
        continue

    if line.startswith("!cmt"):
        continue

    line = re.sub(r"!cmt-.*?-!", "", line)

    if re.match(r"\*-.+?-\*", line):
        titles.append(line)
        continue

    if line.startswith("!pic "):
        link = line[5:].strip()
        content_lines.append(f'<div class="post-image"><img src="{link}" alt="Image" /></div>')
        continue

    if line.startswith("!gif "):
        keyword = line[5:].strip()
        gif_url = fetch_anime_gif(keyword)
        if gif_url:
            content_lines.append(f'<div class="post-gif"><img src="{gif_url}" alt="{keyword} gif" /></div>')
        else:
            content_lines.append(f'<div class="post-gif">[GIF not found for: {keyword}]</div>')
        continue

    content_lines.append(line)

# --- Build HTML content ---
html_content = "<br><br>".join(content_lines).replace("\n", " ")

# --- Title logic ---
if len(titles) > 1:
    title_text = "Too Much Title"
elif titles:
    title_text = re.sub(r"^\*-(.+?)-\*$", r"\1", titles[0])
else:
    title_text = "My Retro Adventure"

# --- Date ---
now_utc = datetime.now(pytz.utc)
user_time = now_utc.astimezone(user_timezone)
formatted_datetime = user_time.strftime("%B %d, %Y — %I:%M %p")

# --- Template ---
with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

final_html = (
    template.replace("{{content}}", html_content)
            .replace("{{date}}", formatted_datetime)
            .replace("My Retro Adventure", title_text)
)

# --- Output HTML ---
with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("✅ index.html updated!")
