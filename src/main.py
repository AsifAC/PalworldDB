import discord
from discord.ext import commands

from apikey import *

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print('PalWorldDB Status: [ONLINE]')
    print('-----------------------------')

@bot.command()
async def test(ctx):
    await ctx.send("Bot is in BETA test mode")


bot.run(BOT_TOKEN) #* -- BOT TOKEN IS IN A SEPERATE PRIVATE FILE