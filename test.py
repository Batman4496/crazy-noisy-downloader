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
  driver = DriverManager().run('twitch')
  info = await driver.get_info("https://www.twitch.tv/videos/2307068771")

  print(info)


if __name__ == '__main__':
  asyncio.run(main=main())