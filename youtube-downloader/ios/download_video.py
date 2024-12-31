import yt_dlp
import os

def get_download_path():
    return os.path.join(os.path.expanduser("~"), "Documents")

url = 'https://www.youtube.com/watch?v=zmjbQzZ9oWE'

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.youtube.com/',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

ydl_opts = {
    'headers': headers,
    'format': 'best',
    'outtmpl': os.path.join(get_download_path(), '%(title)s.%(ext)s'),
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url]) 