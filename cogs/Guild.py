from discord.ext import commands

class Guild(commands.Cog):
    def __init__(self, client):
        self.client = client
        
@commands.command()
async def test(self, ctx):
    await ctx.send("Bot is in still in test mode")
    
@commands.Cog.listener()
async def on_member_join(member):
    channel = commands.get_channel(1210382696535040040)
    await channel.send("Hello! Welcome to PalWorldDB!")
    
@commands.Cog.listener()
async def on_member_remove(member):
    channel = commands.get_channel(1210382696535040040)
    await channel.send("Goodbye! Hope to see you again!")
    
def setup(client):
    client.add_cog(Guild(client))