from abc import ABC, abstractmethod
from discord import Embed, File, Interaction
from lib.classes import DownloadFile

class IFileResponse(ABC):

  @abstractmethod
  async def generate(self, file: DownloadFile, interaction: Interaction) -> None:
    raise NotImplementedError