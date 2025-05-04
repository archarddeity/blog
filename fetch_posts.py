import subprocess
import json
import pytz
from datetime import datetime

user_timezone = pytz.timezone("America/New_York")

with open("channel.txt", "r", encoding="utf-8") as f:
    channel_ids = [line.strip() for line in f if line.strip()]

output_lines = []

for channel_id in channel_ids:
    try:
        community_url = f"https://www.youtube.com/channel/{channel_id}/community"
        print(f"📥 Fetching community post from {community_url}...")

        result = subprocess.run(
            ["yt-dlp", "--skip-download", "--dump-json", community_url],
            capture_output=True,
            text=True,
            timeout=30
        )

        if not result.stdout.strip():
            raise ValueError("Empty response")

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

                output_lines.append(f"{channel_id}:\n{text}\nPosted: {formatted_time}\n")
                break
        else:
            output_lines.append(f"{channel_id}:\n⚠️ No community post found.\n")

    except Exception as e:
        output_lines.append(f"{channel_id}:\n❌ Error: {str(e)}\n")

# Save results
with open("message.txt", "w", encoding="utf-8") as f:
    f.write("\n====\n\n".join(output_lines))

print("✅ All posts saved to message.txt")
