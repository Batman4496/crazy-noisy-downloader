from dotenv import load_dotenv
load_dotenv() # load all the variables from the env file

import discord
import os # default module
from constants import COGS


intents = discord.Intents()
intents.message_content = True

bot = discord.Bot(command_prefix="~", intents=intents)

@bot.event
async def on_ready() -> None:
  print("READY!!!") 

@bot.slash_command(description="Say Hi!")
async def hello(ctx):
  await ctx.respond("Hello!")

for cog in COGS:
  bot.load_extension(f'cogs.{cog}')
  print(cog, "loaded!")

bot.run(os.environ.get("TOKEN")) # run the bot with the token