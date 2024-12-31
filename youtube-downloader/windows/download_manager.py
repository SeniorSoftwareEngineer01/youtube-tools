import yt_dlp
import os
from threading import Thread
import webbrowser

class DownloadManager:
    def __init__(self, progress_callback=None, complete_callback=None):
        self.progress_callback = progress_callback
        self.complete_callback = complete_callback
        self.downloaded_file_path = None

    def get_video_info(self, url):
        """جلب معلومات الفيديو والصيغ المتاحة"""
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                formats = []
                # تجميع صيغ الفيديو
                video_formats = [f for f in info['formats'] 
                               if f.get('vcodec', 'none') != 'none' 
                               and f.get('acodec', 'none') != 'none']
                for f in video_formats:
                    resolution = f.get('resolution', 'N/A')
                    ext = f.get('ext', 'N/A')
                    formats.append({
                        'format_id': f['format_id'],
                        'ext': ext,
                        'resolution': resolution,
                        'type': 'video',
                        'display': f'فيديو {resolution} ({ext})'
                    })
                
                # تجميع صيغ الصوت
                audio_formats = [f for f in info['formats'] 
                               if f.get('acodec', 'none') != 'none' 
                               and f.get('vcodec', 'none') == 'none']
                for f in audio_formats:
                    abr = f.get('abr', 'N/A')
                    ext = f.get('ext', 'N/A')
                    formats.append({
                        'format_id': f['format_id'],
                        'ext': ext,
                        'abr': abr,
                        'type': 'audio',
                        'display': f'صوت {abr}kbps ({ext})'
                    })
                
                return formats
        except Exception as e:
            print(f"خطأ في جلب المعلومات: {str(e)}")
            return []

    def download(self, url, format_id):
        """بدء تحميل الفيديو في خيط منفصل"""
        Thread(target=self._download, args=(url, format_id), daemon=True).start()

    def _download(self, url, format_id):
        """تنفيذ التحميل الفعلي"""
        def progress_hook(d):
            if d['status'] == 'downloading':
                if 'total_bytes' in d:
                    percentage = (d['downloaded_bytes'] / d['total_bytes']) * 100
                    if self.progress_callback:
                        self.progress_callback(percentage)
            elif d['status'] == 'finished':
                self.downloaded_file_path = d['filename']

        ydl_opts = {
            'format': format_id,
            'outtmpl': os.path.join(self.get_download_path(), '%(title)s.%(ext)s'),
            'progress_hooks': [progress_hook],
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            if self.complete_callback:
                self.complete_callback(self.downloaded_file_path)
        except Exception as e:
            print(f"خطأ في التحميل: {str(e)}")

    @staticmethod
    def get_download_path():
        """الحصول على مسار مجلد التحميلات"""
        return os.path.join(os.path.expanduser("~"), "Downloads")

    def play_video(self):
        """فتح الفيديو في المشغل الافتراضي"""
        if self.downloaded_file_path and os.path.exists(self.downloaded_file_path):
            webbrowser.open(self.downloaded_file_path) 