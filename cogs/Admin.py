import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
        
@commands.command()
@commands.has_permissions(kick_members = True)
async def kick(self, ctx, member: discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f"The User: **[{member}]** has been kicked!")

@commands.command()
@commands.has_permissions(ban_members = True)
async def ban(self, ctx, member: discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f"The User: **[{member}]** has been terminated!")
    
@commands.command()
@commands.has_permissions(Admin = True)
async def shutdown(self, ctx):
   await ctx.send("Shutting down bot!")
   await commands.close()
   
def setup(client):
    client.add_cog(Admin(client))