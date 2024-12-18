import time
import asyncio

def seconds_to_timestamp(seconds: int) -> str:
  return time.strftime('%H:%M:%S', time.gmtime(seconds))

def timestamp_to_seconds(timestamp: str) -> int:
    parts = timestamp.split(":")
    if len(parts) != 3:
        raise ValueError("Timestamp must be in HH:MM:SS format.")
    hours, minutes, seconds = map(int, parts)
    return hours * 3600 + minutes * 60 + seconds

async def run_shell_command(command: str):
    # Start the subprocess
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    
    # Wait for the process to complete and capture the output
    stdout, stderr = await process.communicate()
    
    # Return the results
    return process.returncode, stdout.decode(), stderr.decode()


def trim_path_tail(path) -> str:
  return path[:-1] if path[-1] == '/' else path