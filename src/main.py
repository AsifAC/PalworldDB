import discord
from discord.ext import commands
from discord import BanEntry, Member
from discord.ext.commands import has_permissions, MissingPermissions

from apikey import *

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents)

# * ---------------------BOT EVENTS--------------------- * #
@bot.event
async def on_ready():
    print("PalWorldDB Status: [ONLINE]")
    print("----------------------------")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1210382696535040040)
    await channel.send("Hello! Welcome to PalWorldDB!")
    
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1210382696535040040)
    await channel.send("Goodbye! Hope to see you again!")
    
# @bot.event
# async def on_message(message):
#     if message.content == "Dumb":
#         await message.delete()
#         await message.channel.send("That word is banned")
    
# * ---------------------BOT COMMANDS--------------------- * #
@bot.command()
async def test(ctx):
    await ctx.send("Bot is in BETA test mode")
    
@bot.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("[Voice Channel Not Found]: Please join a voice channel to run this command!")

@bot.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel!")
    else:
        await ctx.send("[Voice Channel Not Found]: I am not in a voice channel!")

@bot.command()
async def shutdown(ctx):
   await ctx.send("Shutting down bot!")
   await bot.close()
        
@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason=reason)
    await ctx.send(f"The User: **[{member}]** has been kicked!")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to kick people!")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f"The User: **[{member}]** has been terminated!")
        
bot.run(BOT_TOKEN) #* -- BOT TOKEN IS IN A SEPERATE PRIVATE PYTHON FILE