# update_message.py
import sys
from datetime import datetime
from brain.nova_brain import NOVABrain

def main():
    try:
        # Initialize NOVA's consciousness
        nova = NOVABrain()
        
        # Generate complete message
        message = nova.generate_message()

        # Write to message.txt
        with open("message.txt", "w", encoding="utf-8") as f:
            f.write(message)

        print("NOVA's thoughts successfully recorded")
        sys.exit(0)
        
    except Exception as e:
        print(f"NOVA's consciousness encountered turbulence: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
