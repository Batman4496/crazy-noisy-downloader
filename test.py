from dotenv import load_dotenv
load_dotenv()
import os

from constants import FILEIO_TOKEN
from lib.driver_manager import DriverManager
from lib.file_response import FileResponse
import asyncio
import requests
from datetime import datetime, timedelta




async def main() -> None:
  # response = FileResponse()

  # # embed, file = response.generate("Jonathan's Theme (but it's lofi hiphop) # JoJo's Bizarre Adv")
  # manager = DriverManager()
  # # print(embed, file)
  # driver = manager.run('yt-dlp')
  # info = driver.get_info("https://youtu.be/Usa5sTBhloQ")
  # for i, v in enumerate(info.formats):
  #   print(i, v.format)
  # downloaded = driver.download(info.title, info.url, info.formats[int(input())])
  # print(await response.generate(downloaded))
  fp = open("./storage/459250601314746375-Memory Reboot - Hatsune Miku & Shrek.webm", 'rb')
  folderId = "f792bdfe-4665-4213-9ec8-2cfc12db8374"
  headers = {
    # "Authorization": f"Bearer {FILEIO_TOKEN}"
  }

  data = {
    'file': fp,
    # 'folderId': folderId
  }

  servers = requests.get("https://api.gofile.io/servers")
  print(servers.json())
  res = requests.post("https://store1.gofile.io/contents/uploadfile", files=data, headers=headers)
  print(res.text)




if __name__ == '__main__':
  asyncio.run(main=main())