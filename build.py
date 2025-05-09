import re
import pytz
import os
import requests
import sys
import random
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TENOR_API_KEY = os.getenv("TENOR_API_KEY")
DEFAULT_GIF_URL = "https://media.tenor.com/5DS4fJXQqAAAAAC/loading.gif"

def fetch_anime_gif(keyword):
    """Enhanced anime GIF fetching with mood-specific matching"""
    try:
        # Expanded mood-to-GIF mapping
        mood_keywords = {
            "happy": ["anime smile", "anime joy", "anime celebration"],
            "sad": ["anime tears", "anime rain", "anime melancholy"],
            "thoughtful": ["anime thinking", "anime book", "anime ponder"],
            "excited": ["anime jump", "anime sparkle", "anime wow"],
            "sleepy": ["anime nap", "anime pillow", "anime yawn"],
            "default": ["anime aesthetic", "anime mood", "anime scene"]
        }

        # Clean and classify keyword
        cleaned_keyword = keyword.lower().strip()
        matched_keywords = []
        
        # Find all matching mood categories
        for mood, keywords in mood_keywords.items():
            if any(kw in cleaned_keyword for kw in [mood] + keywords[:1]):
                matched_keywords.extend(keywords)
        
        # Use matched keywords or fallback to default
        search_terms = matched_keywords if matched_keywords else mood_keywords["default"]
        selected_keyword = random.choice(search_terms)
        
        # API request with better parameters
        params = {
            "q": f"{selected_keyword} anime aesthetic",
            "key": TENOR_API_KEY,
            "limit": 15,
            "media_filter": "minimal",
            "contentfilter": "high",
            "ar_range": "wide",
            "random": "true"
        }
        
        response = requests.get(
            "https://tenor.googleapis.com/v2/search",
            params=params,
            timeout=10
        )
        response.raise_for_status()
        
        results = response.json().get("results", [])
        if results:
            # Prioritize higher quality GIFs
            gifs = sorted(
                results,
                key=lambda x: x.get("media_formats", {}).get("gif", {}).get("dims", [0,0])[0],
                reverse=True
            )
            # Return one of the top 3 results for variety
            return random.choice(gifs[:3])["media_formats"]["gif"]["url"]
            
        return DEFAULT_GIF_URL
        
    except Exception as e:
        print(f"GIF Error: {e}", file=sys.stderr)
        return DEFAULT_GIF_URL

def process_message_file():
    """Read message file with enhanced parsing"""
    try:
        with open("message.txt", "r", encoding="utf-8") as f:
            content = f.read().splitlines()
            if not content:
                print("Warning: message.txt is empty", file=sys.stderr)
            return content
    except Exception as e:
        print(f"Error reading message.txt: {e}", file=sys.stderr)
        return []

def generate_content():
    """Generate HTML content with better structure"""
    lines = process_message_file()
    if not lines:
        return None, None

    content_lines = []
    titles = []
    current_section = []

    for line in lines:
        line = line.strip()
        if not line:
            if current_section:
                content_lines.append("<p>" + " ".join(current_section) + "</p>")
                current_section = []
            continue

        if line.startswith("!cmt"):
            continue

        line = re.sub(r"!cmt-.*?-!", "", line)

        if re.match(r"^\*-.+?-\*$", line):
            titles.append(line)
            continue

        if line.startswith("!pic "):
            link = line[5:].strip()
            content_lines.append(f'<div class="post-image"><img src="{link}" alt="Illustration" loading="lazy"/></div>')
            continue

        if line.startswith("!gif "):
            keyword = line[5:].strip()
            gif_url = fetch_anime_gif(keyword)
            content_lines.append(f'<div class="post-gif"><img src="{gif_url}" alt="{keyword} animation" loading="lazy"/></div>')
            continue

        current_section.append(line)

    if current_section:
        content_lines.append("<p>" + " ".join(current_section) + "</p>")

    return "\n".join(content_lines), titles

def get_main_title(titles):
    """Extract main title with fallbacks"""
    if not titles:
        return "NOVA's Thoughts"
    if len(titles) > 1:
        return "Multiple Musings"
    return re.sub(r"^\*-(.+?)-\*$", r"\1", titles[0])

def build_html(content, titles):
    """Build HTML with better template handling"""
    try:
        with open("template.html", "r", encoding="utf-8") as f:
            template = f.read()
    except Exception as e:
        print(f"Template Error: {e}", file=sys.stderr)
        return None

    title_text = get_main_title(titles)
    date_text = datetime.now(pytz.timezone("America/New_York")).strftime("%B %d, %Y — %I:%M %p")
    
    title_items = []
    for t in titles:
        cleaned_title = re.sub(r'^\*-(.+?)-\*$', r'\1', t)
        title_items.append(f"<li>{cleaned_title}</li>")
    
    titles_html = "<ul class='title-list'>" + "\n".join(title_items) + "</ul>" if titles else ""

    replacements = {
        "{{content}}": content or "<p>No content generated yet.</p>",
        "{{date}}": date_text,
        "{{titles}}": titles_html,
        "{{main_title}}": title_text
    }
    
    html = template
    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)
    
    return html

def write_output(html):
    """Write output with validation"""
    try:
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        
        # Verify output
        if os.path.getsize("index.html") == 0:
            raise ValueError("Empty HTML output")
        if "{{" in html:
            raise ValueError("Unprocessed template tags")
            
        print("Build successful")
        return True
        
    except Exception as e:
        print(f"Output Error: {e}", file=sys.stderr)
        return False

def main():
    """Enhanced main execution flow"""
    print("\n=== Starting Build ===")
    start_time = datetime.now()
    
    try:
        content, titles = generate_content()
        if content is None:
            raise ValueError("No content to build")
        
        html = build_html(content, titles)
        if html is None:
            raise ValueError("HTML generation failed")
        
        if not write_output(html):
            raise ValueError("Output writing failed")

        elapsed = datetime.now() - start_time
        print(f"=== Build completed in {elapsed.total_seconds():.2f}s ===")
        
    except Exception as e:
        print(f"\n!!! Build failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()