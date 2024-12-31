import yt_dlp
import os

def get_download_path():
    return "/storage/emulated/0/Download"

url = 'https://www.youtube.com/watch?v=zmjbQzZ9oWE'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
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