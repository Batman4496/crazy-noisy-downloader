from lib.helpers import run_shell_command
from lib.classes.idriver import IDriver
from lib.classes import DownloadFile, DownloadInfo, DownloadFormat
from constants import VIDEO_FORMATS, AUDIO_FORMATS, STORAGE_PATH
from lib.classes.storage import Storage
from lib.helpers import seconds_to_timestamp
import json

class TwitchDriver(IDriver):

  async def get_info(self, url):
    status, out, err = await run_shell_command(f"twitch-dl info {url} --json")

    if status == 1:
      raise Exception(err)

    info = json.loads(out)

    formats = [
      DownloadFormat(is_video=True, format='source')
    ]
    exists = []
    for playlist in info['playlists']:
      
      if playlist.get('video') in exists:
        continue

      if playlist.get('video').split('p')[0] in VIDEO_FORMATS:
        formats.append(DownloadFormat(is_video=True, format=playlist.get('video')))
    
      if 'audio' in playlist.get('video'):
        formats.append(DownloadFormat(is_audio=True, format='Audio Only'))

      exists.append(playlist.get('video'))
    
    downloadInfo = DownloadInfo(
      id=info['id'],
      title=info['title'],
      url=url,
      channel='',
      views=info['viewCount'],
      formats=formats,
      duration=info['lengthSeconds'],
      thumbnail='',
      description=info['description'] or 'No description found.'
    )

    return downloadInfo

  async def download(self, name, url, format, start = None, end = None, storage_path=None):
    storage_path = storage_path or STORAGE_PATH
    command = f"twitch-dl download {url}"
    name = name.replace('/', '-')

    if start:
      command += f" -s {seconds_to_timestamp(start)}"

    if end:
      command += f" -e {seconds_to_timestamp(end)}"
    
    
    command += f" -q {format.format}"
    command += f' -o "{storage_path}/{name}' + '.{format}"'

    status, out, err = await run_shell_command(command)
    if status == 1:
      print(err)
      raise Exception(err)

    file = Storage().get_file(name)

    return DownloadFile(
      name,
      file,
      format,
      file.split('.')[-1]
    )


if __name__ == '__main__':
  driver = TwitchDriver()
  info = driver.get_info("https://www.itch.tv/videos/2307xc68771")