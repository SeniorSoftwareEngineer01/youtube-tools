import yt_dlp
import os

def get_download_path():
    return os.path.join(os.path.expanduser("~"), "Downloads")

url = 'https://www.youtube.com/watch?v=zmjbQzZ9oWE'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
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