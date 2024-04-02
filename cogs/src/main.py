import discord
from discord.ext import commands
import os

from apikey import *

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix = "-", intents = intents)

# * ---------------------MAIN FILE--------------------- * #
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("PalWorld Database!"))
    print("PalWorldDB Status: [ONLINE]")
    print("----------------------------")

@bot.command()
async def shutdown(ctx):
   await ctx.send("Shutting down bot!")
   await bot.close()   
    
cogs = ["./cogs"]
Start_Decoration="----- Connecting Cogs -----\n---------------------------"
End_Decoration = "\n---------------------------\n----- Cogs  Connected -----"
Fail = "N/A"
Success = False
initial_cogs_files = []

for cog in cogs:
  try:
    bot.load_extension(cog)
    Success = True
    
  except Exception as e:
    if Fail == "N/A":
      Fail = f"🚫 Failed to connect the following:\n\n{cog}: {str(e)}"
    else:
      Fail += f"\n{cog}: {str(e)}"
      
if Success == True and Fail == "N/A":
  print(f"{Start_Decoration}\n✅ Connecting Cogs\n{End_Decoration}")
  
elif Success == True and not Fail == "N/A":
  print(f"{Start_Decoration}\n✅ Connecting Cogs\n\n{Fail}\n{End_Decoration}")
  
else:
  print(f"{Start_Decoration}\n{Fail}\n{End_Decoration}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

if __name__ == "__main__":
  for extenstion in initial_cogs_files:
    bot.load_extension(extenstion)

bot.run(BOT_TOKEN) #* -- BOT TOKEN IS IN A SEPERATE PRIVATE PYTHON FILE