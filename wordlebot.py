import discord
import asyncio
import random
import os
from datetime import datetime, timedelta

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1516475623290441748

client = discord.Client(intents=discord.Intents.default())


def get_random_times():
    times = set()

    while len(times) < 4:
        times.add((
            random.randint(8, 23),  # between 8 AM and 11 PM
            random.randint(0, 59)
        ))

    return sorted(times)


async def scheduler():
    await client.wait_until_ready()

    while not client.is_closed():

        channel = client.get_channel(CHANNEL_ID)

        today_times = get_random_times()

        print(f"Today's Wordle propaganda schedule: {today_times}")

        for hour, minute in today_times:

            now = datetime.now()

            target = now.replace(
                hour=hour,
                minute=minute,
                second=0,
                microsecond=0
            )

            if target <= now:
                continue

            wait_time = (target - now).total_seconds()

            await asyncio.sleep(wait_time)

            await channel.send(
                "@everyone should we do the wordle?? prolly",
                allowed_mentions=discord.AllowedMentions(everyone=True)
            )

        tomorrow = (
            datetime.now().replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0
            )
            + timedelta(days=1)
        )

        await asyncio.sleep(
            (tomorrow - datetime.now()).total_seconds()
        )


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    if not hasattr(client, "scheduler_started"):
        client.scheduler_started = True
        asyncio.create_task(scheduler())


client.run(TOKEN)