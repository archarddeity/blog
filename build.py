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
DEFAULT_GIF_URL = "https://media.tenor.com/5DS4fJXQqAAAAAC/loading.gif"

def fetch_anime_gif(keyword):
    """Fetch anime GIF from Tenor API with robust error handling"""
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
        return DEFAULT_GIF_URL
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching GIF from Tenor API: {e}", file=sys.stderr)
        return DEFAULT_GIF_URL
    except (KeyError, ValueError) as e:
        print(f"Error parsing Tenor API response: {e}", file=sys.stderr)
        return DEFAULT_GIF_URL

def process_message_file():
    """Read message file with error handling"""
    try:
        with open("message.txt", "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        print("Error: message.txt not found", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Error reading message.txt: {e}", file=sys.stderr)
        return []

def generate_content():
    """Generate HTML content from message file"""
    lines = process_message_file()
    if not lines:
        print("Warning: No content found in message.txt", file=sys.stderr)
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
            content_lines.append(f'<div class="post-gif"><img src="{gif_url}" alt="{keyword} gif" loading="lazy" /></div>')
            continue

        content_lines.append(f"<p>{line}</p>")

    return "\n".join(content_lines), titles

def get_main_title(titles):
    """Extract main title from titles list"""
    if not titles:
        return "My Retro Adventure"
    if len(titles) > 1:
        return "Multiple Titles Today"
    # Use raw string for regex to avoid backslash issues
    return re.sub(r"^\*-(.+?)-\*$", r"\1", titles[0])

def build_html(content, titles):
    """Build HTML from template with content"""
    try:
        with open("template.html", "r", encoding="utf-8") as f:
            template = f.read()
    except Exception as e:
        print(f"Error reading template: {e}", file=sys.stderr)
        return None

    title_text = get_main_title(titles)
    date_text = datetime.now(pytz.timezone("America/New_York")).strftime("%B %d, %Y — %I:%M %p")
    
    # Fixed: Use raw strings for regex patterns and separate the list comprehension
    title_items = []
    for t in titles:
        cleaned_title = re.sub(r'^\*-(.+?)-\*$', r'\1', t)
        title_items.append(f"<li>{cleaned_title}</li>")
    
    titles_html = "<ul>\n" + "\n".join(title_items) + "\n</ul>" if titles else ""

    return (
        template.replace("{{content}}", content)
               .replace("{{date}}", date_text)
               .replace("{{titles}}", titles_html)
               .replace("{{main_title}}", title_text)
    )

def write_output(html):
    """Write HTML output with validation"""
    try:
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        
        # Verify no template tags remain
        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()
            if "{{" in content:
                print("Error: Template tags remain in output", file=sys.stderr)
                return False
        
        print("Successfully generated index.html")
        return True
        
    except Exception as e:
        print(f"Error writing index.html: {e}", file=sys.stderr)
        return False

def main():
    """Main execution function"""
    content, titles = generate_content()
    if content is None:
        print("Error: No content to build", file=sys.stderr)
        sys.exit(1)

    html = build_html(content, titles)
    if html is None:
        sys.exit(1)

    if not write_output(html):
        sys.exit(1)

if __name__ == "__main__":
    main()