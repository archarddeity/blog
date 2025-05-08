import hmac
import hashlib
import os

# These should be set as environment variables
NOTION_SHARED_SECRET = os.getenv("NOTION_SHARED_SECRET")
NOTION_HASH = os.getenv("NOTION_HASH")
notion_content = "the raw text content from Notion"  # Replace this with the actual content of your Notion page

# Compute the HMAC hash
computed_hash = hmac.new(
    NOTION_SHARED_SECRET.encode(),
    notion_content.encode(),
    hashlib.sha256
).hexdigest()

print("Computed Hash: ", computed_hash)
print("Expected Hash: ", NOTION_HASH)

# Compare if they match
if computed_hash != NOTION_HASH:
    raise Exception("❌ HMAC verification failed. Content may have been tampered with.")
else:
    print("✅ HMAC verification succeeded.")
