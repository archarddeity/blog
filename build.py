import re
import pytz
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TENOR_API_KEY = os.getenv("TENOR_API_KEY")

def fetch_anime_gif(keyword):
    """Fetch anime GIF from Tenor API with timeout and error handling"""
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
    except (requests.RequestException, KeyError) as e:
        print(f"Error fetching GIF: {e}")
    return None

def process_message_file():
    """Read and process message.txt with error handling"""
    try:
        with open("message.txt", "r", encoding="utf-8") as f:
            return f.readlines()
    except IOError as e:
        print(f"Error reading message.txt: {e}")
        return []

def generate_html_content(lines):
    """Generate HTML content from message lines"""
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

    return content_lines, titles

def get_main_title(titles):
    """Determine the main title from titles list"""
    if len(titles) > 1:
        return "Too Much Title"
    elif titles:
        return re.sub(r"^\*-(.+?)-\*$", r"\1", titles[0])
    return "My Retro Adventure"

def get_current_datetime():
    """Get current datetime in user's timezone"""
    user_timezone = pytz.timezone("America/New_York")
    now_utc = datetime.now(pytz.utc)
    return now_utc.astimezone(user_timezone).strftime("%B %d, %Y — %I:%M %p")

def generate_titles_html(titles):
    """Generate HTML for titles list"""
    if not titles:
        return "<p>No titles found.</p>"
    
    items = "\n".join(
        f"<li>{re.sub(r'^\\*-(.+?)-\\*$', r'\\1', t)}</li>" 
        for t in titles
    )
    return f"<ul>\n{items}\n</ul>"

def build_html_template(content_lines, titles):
    """Build final HTML by populating template"""
    try:
        with open("template.html", "r", encoding="utf-8") as f:
            template = f.read()
    except IOError as e:
        print(f"Error reading template: {e}")
        return None

    html_content = "<br><br>".join(content_lines)
    title_text = get_main_title(titles)
    formatted_datetime = get_current_datetime()
    titles_html = generate_titles_html(titles)

    return (
        template.replace("{{content}}", html_content)
               .replace("{{date}}", formatted_datetime)
               .replace("{{titles}}", titles_html)
               .replace("{{main_title}}", title_text)
    )

def write_output_file(html_content):
    """Write final HTML to index.html"""
    try:
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print("✅ index.html updated successfully!")
        return True
    except IOError as e:
        print(f"Error writing index.html: {e}")
        return False

def main():
    lines = process_message_file()
    if not lines:
        return

    content_lines, titles = generate_html_content(lines)
    final_html = build_html_template(content_lines, titles)
    
    if final_html:
        write_output_file(final_html)

if __name__ == "__main__":
    main()