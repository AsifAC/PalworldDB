from discord.ext import commands

class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client
        
@commands.command(pass_context = True)
async def join(self, ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("[Voice Channel Not Found]: Please join a voice channel to run this command!")

@commands.command(pass_context = True)
async def leave(self, ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel!")
    else:
        await ctx.send("[Voice Channel Not Found]: I am not in a voice channel!")
        
def setup(client):
    client.add_cog(Voice(client))