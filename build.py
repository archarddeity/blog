import re
import pytz
import os
import requests
import sys
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TENOR_API_KEY = os.getenv("TENOR_API_KEY")

def fetch_anime_gif(keyword):
    try:
        query = f"{keyword} anime"
        url = "https://tenor.googleapis.com/v2/search"
        params = {
            "q": query,
            "key": TENOR_API_KEY,
            "limit": 1,
            "media_filter": "minimal",
            "contentfilter": "high"
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        results = response.json().get("results", [])
        if results:
            return results[0]["media_formats"]["gif"]["url"]
    except Exception as e:
        print(f"Error fetching GIF: {e}", file=sys.stderr)
    return None

def process_message_file():
    try:
        with open("message.txt", "r", encoding="utf-8") as f:
            return f.readlines()
    except Exception as e:
        print(f"Error reading message.txt: {e}", file=sys.stderr)
        return []

def generate_content():
    lines = process_message_file()
    if not lines:
        return None, None

    content_lines = []
    titles = []

    for line in lines:
        line = line.strip()
        if not line:
            content_lines.append("")
            continue

        if line.startswith("!cmt"):
            continue

        line = re.sub(r"!cmt-.*?-!", "", line)

        if re.match(r"\*-.+?-\*", line):
            titles.append(line)
            continue

        if line.startswith("!pic "):
            link = line[5:].strip()
            content_lines.append(f'<div class="post-image"><img src="{link}" alt="Image" loading="lazy" /></div>')
            continue

        if line.startswith("!gif "):
            keyword = line[5:].strip()
            gif_url = fetch_anime_gif(keyword)
            if gif_url:
                content_lines.append(f'<div class="post-gif"><img src="{gif_url}" alt="{keyword} gif" loading="lazy" /></div>')
            else:
                content_lines.append(f'<div class="post-gif">[GIF not found for: {keyword}]</div>')
            continue

        content_lines.append(f"<p>{line}</p>")

    return "\n".join(content_lines), titles

def get_main_title(titles):
    if not titles:
        return "My Retro Adventure"
    if len(titles) > 1:
        return "Too Much Title"
    return re.sub(r"^\*-(.+?)-\*$", r"\1", titles[0])

def build_html(content, titles):
    try:
        with open("template.html", "r", encoding="utf-8") as f:
            template = f.read()
    except Exception as e:
        print(f"Error reading template: {e}", file=sys.stderr)
        return None

    title_text = get_main_title(titles)
    date_text = datetime.now(pytz.timezone("America/New_York")).strftime("%B %d, %Y — %I:%M %p")
    
    titles_html = "<ul>\n" + "\n".join(
        f"<li>{re.sub(r'^\\*-(.+?)-\\*$', r'\\1', t)}</li>" 
        for t in titles
    ) + "\n</ul>" if titles else "<p>No titles found.</p>"

    return (
        template.replace("{{content}}", content)
               .replace("{{date}}", date_text)
               .replace("{{titles}}", titles_html)
               .replace("{{main_title}}", title_text)
    )

def write_output(html):
    try:
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("✅ Successfully updated index.html")
        return True
    except Exception as e:
        print(f"Error writing index.html: {e}", file=sys.stderr)
        return False

def main():
    content, titles = generate_content()
    if content is None:
        print("❌ No content to build", file=sys.stderr)
        sys.exit(1)

    html = build_html(content, titles)
    if html is None:
        sys.exit(1)

    if not write_output(html):
        sys.exit(1)

    # Verify no template tags remain
    with open("index.html", "r", encoding="utf-8") as f:
        if "{{" in f.read():
            print("❌ Template tags remain in index.html", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()