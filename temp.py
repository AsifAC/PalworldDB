import discord
from discord.ext import commands
from discord import Interaction

from tempkey import *

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix = "-", intents = intents)

# * ---------------------BOT EVENTS--------------------- * #
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("PalWorld Database!"))
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

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You don't have the required arguments! :rolling eyes:")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions! :angry:")

@bot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await channel.send(f"**{user.name} added:** {reaction.emoji}")

@bot.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    await channel.send(f"**{user.name} removed:** {reaction.emoji}")
    
# * ---------------------BOT COMMANDS--------------------- * #
@bot.command()
async def test(ctx):
    await ctx.send("Bot is in BETA")
    
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
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f"The User: **[{member}]** has been kicked!")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f"The User: **[{member}]** has been terminated!")
    
@bot.command()
async def shutdown(ctx):
   await ctx.send("Shutting down bot!")
   await bot.close()
        
bot.run(BOT_TOKEN) #* -- BOT TOKEN IS IN A SEPERATE PRIVATE PYTHON FILE