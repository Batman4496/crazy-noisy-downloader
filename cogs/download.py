import discord
from discord.ext import commands
from lib.driver_manager import DriverManager, DRIVERS
from lib.views.download_view import DownloadView

class Download(commands.Cog): 
  
  def __init__(self, bot):
    self.bot = bot

  @discord.slash_command(
    name="download", 
    description="Download a youtube video"
  )
  async def download(
    self, 
    ctx: discord.ApplicationContext,
    url: str,
    driver: discord.Option(
      str,
      description="Search driver",
      choices=DRIVERS.keys(),
      default=list(DRIVERS.keys())[0]
    )
  ):
    try:
      await ctx.response.defer()
      driver = DriverManager().run()
      try:
        info = await driver.get_info(url)
      except:
        return await ctx.followup.send(f"{url} not found.")
      
      view = DownloadView(driver, info)
      await ctx.followup.send(embed=view.generate_embed(), view=view.generate_view())
    
    except Exception as e:
      await ctx.send(f"An error occured!\n{e}")

    
def setup(bot):
  bot.add_cog(Download(bot))