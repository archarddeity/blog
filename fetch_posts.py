import subprocess
import json
import pytz
from datetime import datetime

# Set your preferred time zone
user_timezone = pytz.timezone("America/New_York")

# Load channel usernames from channel.txt
with open("channel.txt", "r", encoding="utf-8") as f:
    usernames = [line.strip() for line in f if line.strip()]

output_lines = []

for username in usernames:
    name = f"@{username}"
    url = f"https://www.youtube.com/{name}/community"
    print(f"Fetching post from {name}...")

    try:
        # Use yt-dlp to get the latest community post
        result = subprocess.run(
            ["yt-dlp", "--dump-json", "--skip-download", url],
            capture_output=True,
            text=True,
            timeout=30
        )

        for line in result.stdout.splitlines():
            data = json.loads(line)

            if data.get("_type") == "post" and data.get("post_type") == "text":
                text = data.get("text", "").strip()

                # Convert timestamp to your local time zone
                if data.get("timestamp"):
                    dt = datetime.utcfromtimestamp(data["timestamp"]).replace(tzinfo=pytz.utc)
                    dt_local = dt.astimezone(user_timezone)
                    formatted_time = dt_local.strftime("%B %d, %Y — %I:%M %p")
                else:
                    formatted_time = "Unknown time"

                output_lines.append(f"{name}:\n{text}\nPosted: {formatted_time}\n")
                break  # Grab only the latest text post

        else:
            output_lines.append(f"{name}:\nNo community post found.\n")

    except Exception as e:
        output_lines.append(f"{name}:\nError fetching post: {str(e)}\n")

# Write output to message.txt
with open("message.txt", "w", encoding="utf-8") as f:
    f.write("\n====\n\n".join(output_lines))

print("✅ All posts saved to message.txt")
