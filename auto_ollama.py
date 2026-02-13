import subprocess
import time
import random
from datetime import datetime
import os

MODEL_NAME = "MODEL NAME"  #your model name

PROMPTS = [
    "Give me a random fun fact",
    "Explain quantum computing simply",
    "Write a cyberpunk short story",
    "Give me a hacking-themed poem",
    "Generate a game idea",
]

while True:
    prompt = random.choice(PROMPTS)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Create a filename based on timestamp and prompt
    filename = f"response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    print(f"\n[{timestamp}] Sending prompt: {prompt}")

    result = subprocess.run(
        ["ollama", "run", MODEL_NAME, prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        errors="replace"
    )

    response = result.stdout.strip()

    # Saves individual Responses
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Prompt: {prompt}\n")
        f.write(f"Response:\n{response}\n")

    print(f"Saved response to {filename}")
    wait_time = random.randint(300, 600)  # 5–10 minutes
    print(f"Waiting {wait_time} seconds...\n")
    time.sleep(wait_time)
