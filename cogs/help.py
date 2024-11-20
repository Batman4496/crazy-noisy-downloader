import discord
from discord.ext import commands


class Help(commands.Cog): 
  
  def __init__(self, bot):
    self.bot = bot

  @discord.slash_command(name="help", description="Youtube downloader bot")
  async def help(self, ctx):
    await ctx.response.defer()
    embed = discord.Embed(title="Crazy Noisy Downloader")
    embed.set_thumbnail(url=ctx.author.avatar)
    embed.add_field(name="/download", value="Download a video")
    embed.set_author(name="Hard as bone rn", url="https://discord.com/users/459250601314746375")

    await ctx.followup.send(embed=embed)

    
def setup(bot):
  bot.add_cog(Help(bot))