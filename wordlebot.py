import discord
import asyncio
import random
from datetime import datetime, timedelta
import os

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1516475623290441748

client = discord.Client(intents=discord.Intents.default())


def get_random_times():
    times = []

    while len(times) < 4:
        hour = random.randint(8, 23)  # don't send at 3am
        minute = random.randint(0, 59)

        t = (hour, minute)

        if t not in times:
            times.append(t)

    return sorted(times)


async def daily_scheduler():
    await client.wait_until_ready()

    while not client.is_closed():

        channel = client.get_channel(CHANNEL_ID)

        today_times = get_random_times()

        print("Today's Wordle propaganda schedule:")
        print(today_times)

        for hour, minute in today_times:

            now = datetime.now()

            target = now.replace(
                hour=hour,
                minute=minute,
                second=0,
                microsecond=0
            )

            if target < now:
                continue

            wait_seconds = (target - now).total_seconds()

            await asyncio.sleep(wait_seconds)

            await channel.send(
                "should we do the wordle?? prolly"
            )

        tomorrow = datetime.now().replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        ) + timedelta(days=1)

        await asyncio.sleep(
            (tomorrow - datetime.now()).total_seconds()
        )


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    client.loop.create_task(daily_scheduler())


client.run(TOKEN)