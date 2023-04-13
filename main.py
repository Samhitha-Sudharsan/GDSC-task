import discord
from discord.ext import commands
import os

TOKEN= "MTA5NTM4MzE4NDU1MzgwODAwMg.G-UUkE.i8gCKb54K5BGvVlHeBUXM63JRVl05RRxfOosJs"

from music_cog import music_cog

bot = commands.Bot(command_prefix = "/",intents=discord.Intents.default())

 #cog is a class that has its own event listeners and commands
bot.add_cog(music_cog(bot))



bot.run(os.getenv('TOKEN'))

#python.exe -m pip install --upgrade pip

