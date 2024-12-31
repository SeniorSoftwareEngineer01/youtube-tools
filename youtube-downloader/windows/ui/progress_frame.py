import customtkinter as ctk

class ProgressFrame(ctk.CTkFrame):
    def __init__(self, master, play_callback):
        super().__init__(master)
        self.play_callback = play_callback

        # شريط التقدم
        self.progress_bar = ctk.CTkProgressBar(self)
        self.progress_bar.pack(pady=10, padx=10, fill="x")
        self.progress_bar.set(0)

        # نص حالة التحميل
        self.status_label = ctk.CTkLabel(
            self,
            text="جاهز للتحميل",
            font=("Arial", 12)
        )
        self.status_label.pack(pady=5)

        # زر المشاهدة (مخفي في البداية)
        self.play_button = ctk.CTkButton(
            self,
            text="مشاهدة الفيديو",
            command=self.play_callback,
            height=40
        )
        self.play_button.pack(pady=10, padx=10, fill="x")
        self.play_button.pack_forget()  # إخفاء الزر في البداية

    def start_download(self):
        """بدء التحميل"""
        self.progress_bar.set(0)
        self.status_label.configure(text="جاري التحميل...")
        self.play_button.pack_forget()

    def update_progress(self, value):
        """تحديث قيمة شريط التقدم"""
        self.progress_bar.set(value / 100)

    def complete_download(self):
        """اكتمال التحميل"""
        self.progress_bar.set(1)
        self.status_label.configure(text="تم التحميل بنجاح!")

    def show_play_button(self):
        """إظهار زر المشاهدة"""
        self.play_button.pack(pady=10, padx=10, fill="x") 