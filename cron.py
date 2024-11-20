import os
import time
from constants import STORAGE_PATH

def delete_old_files(directory, age_limit_hours=2):
    """Delete files in the given directory that are older than the specified age limit."""
    current_time = time.time()
    age_limit_seconds = age_limit_hours * 3600

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_age = current_time - os.path.getmtime(file_path)
                if file_age > age_limit_seconds:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")

def main():
  delete_old_files(STORAGE_PATH)

if __name__ == "__main__":
    main()