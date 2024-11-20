import os
import discord
from lib.classes.iresponse import IFileResponse
from discord import Embed
from lib.classes.storage import Storage
from lib.responses import *
from lib.classes import DownloadFile

class FileResponse():
  strategy: IFileResponse

  async def generate(self, file: DownloadFile, interaction: discord.Interaction) -> Embed:
    storage = Storage()
    size = os.path.getsize(file.path) / 1024 / 1024

    if (size > 20):
      self.strategy = GoFileResponse()   
    else:
      self.strategy = EmbedResponse()

    await self.strategy.generate(file, interaction) 
    storage.delete_file(file.title + '.' + file.extension)