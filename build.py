import re
from datetime import datetime

# Read message.txt
with open("message.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

content_lines = []
titles = []

# Parse lines
for line in lines:
    line = line.strip()

    if not line:
        content_lines.append("")  # preserve paragraph breaks
        continue

    # Ignore comment lines
    if line.startswith("!cmt"):
        continue

    # Ignore inline comments
    line = re.sub(r"!cmt-.*?-!", "", line)

    # Handle titles
    if re.match(r"\*-.+?-\*", line):
        titles.append(line)
        continue

    # Handle images
    if line.startswith("!pic "):
        link = line[5:].strip()
        content_lines.append(f'<div class="post-image"><img src="{link}" alt="Image" /></div>')
        continue

    content_lines.append(line)

# Format content with paragraph breaks
html_content = "<br><br>".join(content_lines).replace("\n", " ")

# Dynamic title logic
if len(titles) > 1:
    title_text = "Too Much Title"
elif titles:
    title_text = re.sub(r"^\*-(.+?)-\*$", r"\1", titles[0])
else:
    title_text = "My Retro Adventure"

# Format date and time
now = datetime.now()
formatted_datetime = now.strftime("%B %d, %Y — %I:%M %p")

# Read template
with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

# Replace placeholders
final_html = (
    template.replace("{{content}}", html_content)
            .replace("{{date}}", formatted_datetime)
            .replace("My Retro Adventure", title_text)
)

# Write output
with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("✅ index.html updated!")
