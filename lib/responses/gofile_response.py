import requests
import discord
from lib.classes import DownloadFile
import asyncio

class GoFileResponse:
 
  async def generate(self, file: DownloadFile, interaction: discord.Interaction):
    await interaction.message.edit("File too large! Uploading to GoFile...")
    
    fp = open(file.path, 'rb')
    res = await asyncio.to_thread(lambda: requests.post("https://store1.gofile.io/contents/uploadfile", files={
      'file': fp
    }))
    fp.close()

    data = res.json()
    await interaction.message.edit("File Uploaded!")
    await interaction.channel.send(f"Download *{file.title}*:\n {data.get('data').get('downloadPage')}")
