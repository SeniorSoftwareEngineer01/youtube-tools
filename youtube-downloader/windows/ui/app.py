import customtkinter as ctk
from windows.ui.download_frame import DownloadFrame
from windows.ui.progress_frame import ProgressFrame
from windows.download_manager import DownloadManager

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # إنشاء مدير التحميل
        self.download_manager = DownloadManager(
            progress_callback=self.on_progress,
            complete_callback=self.on_complete
        )

        # إعداد النافذة الرئيسية
        self.title("تحميل فيديوهات يوتيوب")
        self.geometry("600x400")
        self.resizable(False, False)

        # تهيئة الإطار الرئيسي
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # إنشاء الإطار الرئيسي
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # عنوان التطبيق
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="تحميل فيديو من يوتيوب",
            font=("Arial", 24, "bold")
        )
        self.title_label.pack(pady=20)

        # إطار التحميل
        self.download_frame = DownloadFrame(
            self.main_frame, 
            self.start_download,
            self.download_manager.get_video_info
        )
        self.download_frame.pack(pady=20, padx=20, fill="x")

        # إطار التقدم
        self.progress_frame = ProgressFrame(self.main_frame, self.play_video)
        self.progress_frame.pack(pady=20, padx=20, fill="x")

    def start_download(self, url, format_id):
        """بدء عملية التحميل"""
        self.progress_frame.start_download()
        self.download_manager.download(url, format_id)

    def on_progress(self, progress):
        """تحديث التقدم"""
        self.progress_frame.update_progress(progress)

    def on_complete(self, file_path):
        """اكتمال التحميل"""
        self.progress_frame.complete_download()
        self.download_frame.enable_download()
        self.progress_frame.show_play_button()

    def play_video(self):
        """تشغيل الفيديو"""
        self.download_manager.play_video() 