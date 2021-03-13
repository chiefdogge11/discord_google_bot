import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Bot is ready.')

    client.run('ODIwMjIyNjUyODcwNDI2NjU1.YEyB3w.8tKZj0Bd_edasca8H1I0cWx0zRM')
