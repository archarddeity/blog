# monitor.py
import time
import subprocess

def watch_notion(interval=60):
    print("Watching Notion for changes...")
    while True:
        result = subprocess.run(["python", "build.py", "--check-hash"])
        if result.returncode == 1:
            print("Hash changed. Rebuilding...")
            subprocess.run(["python", "build.py"])
        time.sleep(interval)

watch_notion()
