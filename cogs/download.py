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
    await ctx.response.defer()
    driver = DriverManager().run(driver)
    try:
      info = await driver.get_info(url)
    except Exception as e:
      return await ctx.followup.send(f"{url} not found.\n```{e}```")
    
    view = DownloadView(driver, info)
    await ctx.followup.send(embed=view.generate_embed(), view=view.generate_view())
    
def setup(bot):
  bot.add_cog(Download(bot))