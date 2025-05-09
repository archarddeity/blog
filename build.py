import re
import pytz
import os
import requests
import sys
import shutil
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TENOR_API_KEY = os.getenv("TENOR_API_KEY")
DEFAULT_GIF_URL = "https://media.tenor.com/5DS4fJXQqAAAAAC/loading.gif"

def fetch_anime_gif(keyword):
    """Fetch anime GIF without affecting message.txt"""
    try:
        params = {
            "q": f"{keyword} anime",
            "key": TENOR_API_KEY,
            "limit": 1,
            "media_filter": "minimal",
            "contentfilter": "high",
            "random": "true"
        }
        response = requests.get("https://tenor.googleapis.com/v2/search", params=params, timeout=10)
        response.raise_for_status()
        results = response.json().get("results", [])
        return results[0]["media_formats"]["gif"]["url"] if results else DEFAULT_GIF_URL
    except Exception as e:
        print(f"GIF Error: {e}", file=sys.stderr)
        return DEFAULT_GIF_URL

def process_message_file():
    """Read message.txt in read-only mode"""
    try:
        with open("message.txt", "r", encoding="utf-8") as f:
            return f.read().splitlines()
    except Exception as e:
        print(f"Error reading message.txt: {e}", file=sys.stderr)
        return []

def generate_content():
    """Generate content without modifying source files"""
    lines = process_message_file()
    if not lines:
        return None, None

    content = []
    titles = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith("!cmt"):
            continue
            
        if re.match(r"^\*-.+?-\*$", line):
            titles.append(line)
            continue
            
        if line.startswith("!gif "):
            keyword = line[5:].strip()
            gif_url = fetch_anime_gif(keyword)
            content.append(f'<div class="post-gif"><img src="{gif_url}" alt="{keyword}" loading="lazy"/></div>')
            continue
            
        content.append(f"<p>{line}</p>")

    return "\n".join(content), titles

def build_html(content, titles):
    """Build HTML without side effects"""
    with open("template.html", "r", encoding="utf-8") as f:
        template = f.read()
    
    replacements = {
        "{{content}}": content or "<p>No content</p>",
        "{{date}}": '<span id="local-time">Loading local time…</span>',
        "{{titles}}": "\n".join(["<li>{}</li>".format(re.sub(r"^\*-(.+?)-\*$", r"\1", t)) for t in titles]) if titles else "",
        "{{main_title}}": re.sub(r"^\*-(.+?)-\*$", r"\1", titles[0]) if titles else "NOVA's Thoughts"
    }
    
    for k, v in replacements.items():
        template = template.replace(k, v)
    return template

def main():
    """Safe build process that preserves message.txt"""
    print("Building...")
    
    # Create backup of original message
    if os.path.exists("message.txt"):
        shutil.copy2("message.txt", "message.backup")
    
    try:
        content, titles = generate_content()
        if not content:
            raise ValueError("No content generated")
            
        html = build_html(content, titles)
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
            
        print("Build successful")
        return 0
        
    except Exception as e:
        print(f"Build failed: {e}", file=sys.stderr)
        # Restore original message if exists
        if os.path.exists("message.backup"):
            shutil.move("message.backup", "message.txt")
        return 1

if __name__ == "__main__":
    sys.exit(main())