import os

STORAGE_PATH = os.environ.get('STORAGE_PATH')
FILEIO_TOKEN = os.environ.get('FILEIO_TOKEN')

ADMINSTRATORS = [
  459250601314746375,
  716309137629380682
]

COGS = [
  'help',
  'download',
  # 'utils.start'
]

VIDEO_FORMATS = [ '144', '160', '240', '480', '720', '1080', '1440' ]
AUDIO_FORMATS = [ 'flac', 'wav', 'mp3' ]
