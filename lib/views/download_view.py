import discord
import asyncio
from discord.ui import View, Button
from lib.views.clearable_view import ClearableView
from lib.classes import DownloadInfo, DownloadFormat
from lib.classes.idriver import IDriver
from lib.file_response import FileResponse
from lib.helpers import timestamp_to_seconds, seconds_to_timestamp
from lib.views.modals.timestamp_modal import TimestampModal

class DownloadView(ClearableView):

  def __init__(self, driver: IDriver, info: DownloadInfo):
    self.driver = driver
    self.info = info
    self.selected_format: DownloadFormat = None
    self.start = '00:00:00'
    self.end = seconds_to_timestamp(info.duration)

  def button_callback(self, format: DownloadFormat):

    async def callback(interaction: discord.Interaction):
      await interaction.response.defer()
      self.selected_format = format
      await interaction.message.edit(embed=self.generate_embed(), view=self.generate_view())

    return callback
  
  async def trim_callback(self, interaction: discord.Interaction):
    await interaction.response.send_modal(TimestampModal(self, title="Trim ✂️"))

  
  async def download(self, interaction: discord.Interaction):
    await interaction.response.defer()
    await interaction.message.edit(content="Please wait...", view=None, embed=None)
    filename = f"{interaction.user.id}-{self.info.title}"

    try:
      file = await self.driver.download(filename, self.info.url, self.selected_format, timestamp_to_seconds(self.start), timestamp_to_seconds(self.end))
    except Exception as e:
      return await interaction.message.edit(f"Error downloading **{self.info.title}**...\n```{e}```")
    await interaction.message.edit(content="File Downloaded... Please wait...")
    await asyncio.sleep(2)
    return await FileResponse().generate(file, interaction)

  def generate_view(self):
    view = View()

    for format in self.info.formats:
      disabled = False
      if self.selected_format:
        disabled = (format.format == self.selected_format.format)
      
      button = Button(label=format.format, disabled=disabled)
      button.callback = self.button_callback(format)
      view.add_item(button)

    download_button = Button(label="Download", style=discord.ButtonStyle.success)
    download_button.disabled = self.selected_format == None
    download_button.callback = self.download
    trim_button = Button(label="Trim ✂️", style=discord.ButtonStyle.blurple)
    trim_button.callback = self.trim_callback
    
    view.add_item(download_button)
    view.add_item(trim_button)
    view.add_item(self.clear_button())
    # view.interaction_check = self.interaction_check
    
    return view

  def generate_embed(self):
    embed = discord.Embed(title=self.info.title, url=self.info.url)
    embed.set_image(url=self.info.thumbnail)
    embed.add_field(name="Description", value=self.info.description[:500], inline=False)
    
    if self.selected_format:
      embed.add_field(name="Selected Format", value=self.selected_format.format)
      
    embed.add_field(name="Download Range", value=f"{self.start}-{self.end}")

    embed.set_author(name="Crazy Noisy Downloader")
  
    return embed
