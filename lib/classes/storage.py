import os
from constants import STORAGE_PATH
from lib.helpers import trim_path_tail

def ensure_directory(func):
    def wrapper(self, *args, **kwargs):
        self.create_directory()  # Call the function before the actual method
        return func(self, *args, **kwargs)
    return wrapper

class Storage:
  
  def __init__(self):
    self.create_directory()

  @ensure_directory
  def get_file(self, name: str, path = None) -> str|None:
    path = path or STORAGE_PATH
    path = trim_path_tail(path)
    files = os.listdir(path)

    for file in files:
      if name.lower() in file.lower():
        return path + '/' + file

    return None

  @ensure_directory
  def save_file(self, name: str, data, path = None) -> str|None:
    path = path or STORAGE_PATH
    path = trim_path_tail(path)

    file = open(path + '/' + name, 'w')
    file.write(data)
    file.close()

    return path + '/' + name

  @ensure_directory
  def delete_file(self, name: str, path = None):
    path = path or STORAGE_PATH
    path = trim_path_tail(path + '/' + name)
    os.remove(path)

    return True

  def create_directory(self, path = None):
    try:
      os.listdir(path or STORAGE_PATH)
    except FileNotFoundError:
      os.mkdir(path or STORAGE_PATH)