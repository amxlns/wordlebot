import requests
import random
import os
from datetime import datetime

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

now = datetime.utcnow()

# Use the date as a seed so everyone gets the same 4 hours for that day
seed = now.strftime("%Y-%m-%d")
random.seed(seed)

random_hours = random.sample(range(24), 4)

if now.hour in random_hours:
    requests.post(
        WEBHOOK_URL,
        json={
            "content": "@everyone should we do the wordle?? prolly"
        }
    )
