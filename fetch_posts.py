import subprocess
import json
import pytz
from datetime import datetime

user_timezone = pytz.timezone("America/New_York")

# Load usernames from channel.txt
with open("channel.txt", "r", encoding="utf-8") as f:
    usernames = [line.strip() for line in f if line.strip()]

output_lines = []

for username in usernames:
    try:
        # Step 1: Resolve username to channel ID
        print(f"🔍 Resolving @{username} to channel ID...")
        result = subprocess.run(
            ["yt-dlp", "--skip-download", "--dump-json", f"https://www.youtube.com/@{username}"],
            capture_output=True,
            text=True,
            timeout=30
        )

        data = json.loads(result.stdout)
        channel_url = data.get("channel_url")
        if not channel_url:
            output_lines.append(f"@{username}:\n⚠️ Could not resolve channel URL.\n")
            continue

        # Step 2: Use channel ID URL to fetch community post
        community_url = f"{channel_url}/community"
        print(f"📥 Fetching community post from {community_url}...")

        result = subprocess.run(
            ["yt-dlp", "--skip-download", "--dump-json", community_url],
            capture_output=True,
            text=True,
            timeout=30
        )

        for line in result.stdout.splitlines():
            post_data = json.loads(line)

            if post_data.get("_type") == "post" and post_data.get("post_type") == "text":
                text = post_data.get("text", "").strip()

                if post_data.get("timestamp"):
                    dt = datetime.utcfromtimestamp(post_data["timestamp"]).replace(tzinfo=pytz.utc)
                    dt_local = dt.astimezone(user_timezone)
                    formatted_time = dt_local.strftime("%B %d, %Y — %I:%M %p")
                else:
                    formatted_time = "Unknown time"

                output_lines.append(f"@{username}:\n{text}\nPosted: {formatted_time}\n")
                break
        else:
            output_lines.append(f"@{username}:\n⚠️ No community post found.\n")

    except Exception as e:
        output_lines.append(f"@{username}:\n❌ Error: {str(e)}\n")

# Write output to message.txt
with open("message.txt", "w", encoding="utf-8") as f:
    f.write("\n====\n\n".join(output_lines))

print("✅ All posts saved to message.txt")
