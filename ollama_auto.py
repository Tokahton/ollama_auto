import subprocess
import time
import random

MODEL_NAME = "LOCAL AI MODEL NAME"  #model name
PROMPTS = [
    "PROMPT 1",
    "PROMPT 2",
    "PROMPT 3",
    "PROMPT 4",
]

while True:
    prompt = random.choice(PROMPTS)
    print(f"\nSending prompt: {prompt}")

    subprocess.run(
        ["ollama", "run", MODEL_NAME, prompt],
        shell=True
    )

    wait_time = random.randint(300, 600)  # 5 to 10 minutes
    print(f"Waiting {wait_time} seconds...\n")
    time.sleep(wait_time)
