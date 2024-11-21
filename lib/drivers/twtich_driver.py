from lib.helpers import run_shell_command
from lib.classes.idriver import IDriver
from lib.classes import DownloadFile, DownloadInfo, DownloadFormat
from constants import VIDEO_FORMATS, AUDIO_FORMATS, STORAGE_PATH
from lib.classes.storage import Storage
import json

class TwitchDriver(IDriver):

  async def get_info(self, url):
    status, out, err = await run_shell_command(f"twitch-dl info {url} --json")

    if status == 1:
      raise Exception(err)

    info = json.loads(out)

    formats = []
    exists = []
    for playlist in info['playlists']:
      
      if playlist.get('video') in exists:
        continue

      if playlist.get('video').split('p')[0] in VIDEO_FORMATS:
        formats.append(DownloadFormat(is_video=True, format=playlist.get('video')))
        exists.append(playlist.get('video'))
    
    for 'audio' in playlist.get('video'):
      formats.append(DownloadFormat(is_audio=True, format='Audio'))

    return DownloadInfo(
      id=info['id'],
      title=info['title'],
      url=url,
      channel='',
      views=info['view_count'],
      formats=formats,
      duration=info['lengthSeconds'],
      thumbnail='',
      description=info['description']
    )

  async def download(self, name, url, format, start = None, end = None, storage_path=None):
    storage_path = storage_path or STORAGE_PATH
    name = name.replace('/', '-')
    options = {}
    ext = 'mp4'
    if start and end:
      options['download_ranges'] = lambda i, d: [ { 'start_time': start, 'end_time': end }]

    if format.is_video:
      options['format'] = f"bestvideo[height={format.format}]+bestaudio"
      options['outtmpl'] = f"{storage_path}/{name}.%(ext)s"

    if format.is_audio:
      ext = format.format
      options['format'] = "bestaudio"
      options['outtmpl'] = f"{storage_path}/{name}.{ext}"
    
    if format.format == 'default':
      options['format'] = f"bestvideo+bestaudio"

    downloader = YoutubeDL(options)    
    downloader.download(url)
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