from discord.ext import commands
import discord
from datetime import datetime, timezone

# Dein eigener Discord-Token (User-Token)
token = ""
target_user_id =   # Ziel-User-ID

start_date = datetime(2025, 1, 1, tzinfo=timezone.utc)

bot = commands.Bot(command_prefix='!', self_bot=True)

@bot.event
async def on_ready():
    print(f"Eingeloggt als {bot.user}")

    mine = 0
    theirs = 0
    total = 0

    for channel in bot.private_channels:
        if isinstance(channel, discord.DMChannel) and channel.recipient.id == target_user_id:
            async for msg in channel.history(limit=None, oldest_first=True):
                if msg.created_at < start_date:
                    continue

                total += 1
                if msg.author.id == bot.user.id:
                    mine += 1
                else:
                    theirs += 1

    print(f"--- Nachrichten seit {start_date.date()} ---")
    print(f"Du: {mine}")
    print(f"Er/Sie: {theirs}")
    print(f"Gesamt: {total}")
    await bot.close()

bot.run(token)

