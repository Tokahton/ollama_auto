import subprocess
import time
import random
from datetime import datetime

MODEL_NAME = "MODEL NAME"  #your model name
OUTPUT_FILE = "ollama_responses.txt"

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

    print(f"\n[{timestamp}] Sending prompt: {prompt}")

    result = subprocess.run(
        ["ollama", "run", MODEL_NAME, prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        errors="replace"
    )

    response = result.stdout.strip()

    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n=== {timestamp} ===\n")
        f.write(f"PROMPT:\n{prompt}\n\n")
        f.write(f"RESPONSE:\n{response}\n")
        f.write("\n" + "=" * 50 + "\n")

    wait_time = random.randint(300, 600)  # 5–10 minutes
    print(f"Saved response. Waiting {wait_time} seconds...\n")
    time.sleep(wait_time)
