import os

os.system("pip install discord")
os.system("cls")

os.system("title " + "Made by UselesscoderFromIndia on Github")

import discord
from discord.ext import commands
import time

bot = commands.Bot(command_prefix=['stream ', 'Stream ', 'stream', 'Stream'], self_bot=True)

@bot.event
async def on_ready():
    print("Streaming status started!")
    await bot.change_presence(activity=discord.Streaming(name="Text here", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))


@bot.command(aliases=["stop"])
async def close(ctx):
    await bot.close()
    print("Bot Closed")
    print("Closing in 5 seconds :)")
    time.sleep(5)

bot.run('Token here', bot = False)