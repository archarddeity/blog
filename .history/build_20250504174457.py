from datetime import datetime

# Read message.txt content
with open("message.txt", "r", encoding="utf-8") as f:
    raw = f.read()

# Convert double line breaks to <br><br>
html_content = raw.strip().replace("\n\n", "<br><br>").replace("\n", " ")

# Read the HTML template
with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()

# Insert date and content
today = datetime.today().strftime("%B %d, %Y")
final_html = template.replace("{{content}}", html_content).replace("{{date}}", today)

# Write the final index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("✅ index.html updated!")
