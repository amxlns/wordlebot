import requests
import random
import json
from datetime import datetime
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

STATE_FILE = "state.json"

today = datetime.utcnow().strftime("%Y-%m-%d")
current_hour = datetime.utcnow().hour

# Load state
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        state = json.load(f)
else:
    state = {}

# New day = generate 4 random hours
if state.get("date") != today:
    hours = sorted(random.sample(range(0, 24), 4))
    state = {
        "date": today,
        "hours": hours,
        "sent": []
    }

# Send if current hour matches
if current_hour in state["hours"] and current_hour not in state["sent"]:

    requests.post(
        WEBHOOK_URL,
        json={
            "content": "@everyone should we do the wordle?? prolly"
        }
    )

    state["sent"].append(current_hour)

with open(STATE_FILE, "w") as f:
    json.dump(state, f)
