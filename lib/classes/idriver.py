from abc import ABC, abstractmethod
from lib.classes import DownloadFile, DownloadInfo, DownloadFormat

class IDriver(ABC):

  @abstractmethod
  def get_info(self, url: str) -> DownloadInfo:
    raise NotImplementedError
  
  @abstractmethod
  def download(
    self, 
    name: str,
    url: str,
    format: DownloadFormat,
    start: str = None,
    end: str = None, 
    storage_path = None
  ) -> DownloadFile:
    raise NotImplementedError