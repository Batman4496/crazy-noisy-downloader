from lib.classes.idriver import IDriver
from lib.drivers.ytdlp_driver import *

DRIVERS = {
  'yt-dlp': YTDLPDriver
}

class DriverManager:

  def run(self, driver: str = None) -> IDriver:
    if not driver:
      return DRIVERS.get('yt-dlp')()
    
    return DRIVERS[driver]()