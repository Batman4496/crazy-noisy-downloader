from dataclasses import dataclass
from constants import AUDIO_FORMATS, VIDEO_FORMATS
from lib.helpers import seconds_to_timestamp

@dataclass
class DownloadFormat:
  is_video: bool = False
  is_audio: bool = False
  format: str = None

@dataclass
class DownloadFile:
  title: str
  path: str
  format: DownloadFormat
  extension: str

@dataclass
class DownloadInfo:
  title: str
  description: str
  url: str
  channel: str
  views: str
  thumbnail: str
  duration: str
  formats: list[DownloadFormat]

  def audio_formats(self) -> list[DownloadFormat]:
    return [f for f in self.formats if f.format in AUDIO_FORMATS]
  
  def video_formats(self) -> list[DownloadFormat]:
    return [f for f in self.formats if f.format in VIDEO_FORMATS]

  def to_timestamp(self) -> str:
    return ("00:00:00", seconds_to_timestamp(self.length))