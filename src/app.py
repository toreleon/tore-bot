# Create simple Discord bot that responds to messages with a random quote
import random
import os

import discord
from discord.ext import commands

from translate.translate_api import GoogleTranslateAPI

client = commands.Bot(command_prefix='!')
translator = GoogleTranslateAPI()

@client.command("awake")
async def awake(ctx):
    await ctx.send("OOh, Just a little bit of sleep, I'm awake now!")

@client.command("translate")
async def translate(ctx, *, text):
    await ctx.send(translator.translate(text))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

if __name__ == '__main__':
    client.run(os.environ['TOKEN'])


