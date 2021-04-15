print("debug: INFO: Starting Up Bot . . . /")
print("debug: INFO: Importing Libraries . . . /")
from discord.ext import commands
import discord
import json
from pretty_help import PrettyHelp
import os

prefixes = os.environ['PREFIXES']
print("debug: INFO: Setting up bot . . . /")
bot = commands.Bot(command_prefix = prefixes, help_command=PrettyHelp())

print("debug: INFO: Loading Cogs . . . /")
initial_extensions = [
    'cogs.guess_music',
    'cogs.debug',
    'cogs.errorHandler'
]

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print("debug: TRIGGER: on_ready event triggered\ndebug: INFO: Setting Up Bot Status . . . /")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="me do laundry ;cri;"))
    print(f"debug: STATUS: {bot.user} is online on Discord successfully")


print('debug: RUN: Connecting to discordapp.com:443 (Running client token) . . . /')
bot.run(os.environ['DISCORD_BOT_TOKEN'])
print('debug: INFO: bot.run success . . . /')
