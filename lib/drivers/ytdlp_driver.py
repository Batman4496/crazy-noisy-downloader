from yt_dlp import YoutubeDL
from lib.classes.idriver import IDriver
from lib.classes import DownloadFile, DownloadInfo, DownloadFormat
from constants import VIDEO_FORMATS, AUDIO_FORMATS, STORAGE_PATH
from lib.classes.storage import Storage
class YTDLPDriver(IDriver):

  def get_info(self, url):
    downloader = YoutubeDL()
    info = downloader.extract_info(url, download=False)

    formats = [
      DownloadFormat(format='default', is_video=True)
    ]
    exists = []
    for f in info['formats']:
      if not f.get('format_note'):
          continue
      
      stripped = f.get('format_note')[:-1]
      if stripped in exists:
        continue

      if stripped in VIDEO_FORMATS:
        formats.append(DownloadFormat(is_video=True, format=stripped))
        exists.append(stripped)
    
    for f in AUDIO_FORMATS:
      formats.append(DownloadFormat(is_audio=True, format=f))

    return DownloadInfo(
      title=info['title'],
      url=info['original_url'],
      channel=info['channel'],
      views=info['view_count'],
      formats=formats,
      duration=info['duration'],
      thumbnail=info['thumbnail'],
      description=info['description']
    )

  def download(self, name, url, format, start = None, end = None, storage_path=None):
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
  driver = YTDLPDriver()
  driver.get_info("https://youtu.be/Usa5sTBhloQ?si=TgcbLXubtrzfIaWF")
  # driver.download()