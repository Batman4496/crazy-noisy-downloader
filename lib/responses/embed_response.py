import discord
from lib.classes.iresponse import IFileResponse
from lib.classes import DownloadFile

class EmbedResponse(IFileResponse):
  
  async def generate(self, file: DownloadFile, interaction):
    await interaction.message.edit("Uploading file...")
    filename = '-'.join(file.title.split('-')[1:]) + f'.{file.extension}'
    f = discord.File(file.path)
    await interaction.message.edit(content="File Uploaded!")
    await interaction.channel.send(content=f"Downloaded: {filename}", file=f)