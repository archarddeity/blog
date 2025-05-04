from datetime import datetime

# Read your plain text journal
with open("message.txt", "r", encoding="utf-8") as f:
    raw = f.read()

# Convert double newlines into <br><br>
html_content = raw.strip().replace("\n\n", "<br><br>").replace("\n", " ")

# Load the HTML template
with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

# Fill in the content and date
today = datetime.today().strftime("%B %d, %Y")
final_html = template.replace("{{content}}", html_content).replace("{{date}}", today)

# Write to index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("✅ index.html updated from message.txt")
