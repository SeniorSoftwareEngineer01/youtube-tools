import customtkinter as ctk
from tkinter import StringVar, ttk

class DownloadFrame(ctk.CTkFrame):
    def __init__(self, master, download_callback, info_callback):
        super().__init__(master)
        self.download_callback = download_callback
        self.info_callback = info_callback
        self.formats = []

        # إنشاء متغير للرابط
        self.url_var = StringVar()
        self.url_var.trace_add('write', self.on_url_change)

        # إطار لحقل الإدخال وزر اللصق
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(pady=10, padx=10, fill="x")

        # حقل إدخال الرابط
        self.url_entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="أدخل رابط الفيديو هنا",
            height=40,
            width=400,
            textvariable=self.url_var
        )
        self.url_entry.pack(side="left", expand=True, fill="x", padx=(0, 5))

        # زر اللصق
        self.paste_button = ctk.CTkButton(
            self.input_frame,
            text="لصق",
            width=60,
            height=40,
            command=self.paste_from_clipboard
        )
        self.paste_button.pack(side="right")

        # زطار الخيارات
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.pack(pady=10, padx=10, fill="x")

        # قائمة اختيار الصيغة
        self.format_var = StringVar()
        self.format_combobox = ctk.CTkComboBox(
            self.options_frame,
            values=[],
            variable=self.format_var,
            state="disabled",
            width=300
        )
        self.format_combobox.pack(pady=5, fill="x")

        # زر التحميل
        self.download_button = ctk.CTkButton(
            self,
            text="تحميل",
            command=self.on_download,
            height=40,
            state="disabled"
        )
        self.download_button.pack(pady=10, padx=10, fill="x")

        # ربط مفاتيح الاختصار
        self.url_entry.bind('<Control-v>', lambda e: self.paste_from_clipboard())
        self.url_entry.bind('<Button-3>', self.show_context_menu)

    def on_url_change(self, *args):
        """عند تغيير الرابط"""
        url = self.url_var.get()
        if url and ('youtube.com' in url or 'youtu.be' in url):
            self.formats = self.info_callback(url)
            self.format_combobox.configure(
                values=[f['display'] for f in self.formats],
                state="normal"
            )
            if self.formats:
                self.format_combobox.set(self.formats[0]['display'])
                self.download_button.configure(state="normal")
        else:
            self.format_combobox.configure(values=[], state="disabled")
            self.download_button.configure(state="disabled")

    def paste_from_clipboard(self):
        try:
            self.url_entry.event_generate('<<Paste>>')
            return "break"
        except Exception as e:
            print(f"خطأ في اللصق: {str(e)}")

    def show_context_menu(self, event):
        try:
            context_menu = ctk.CTkFrame(self)
            paste_option = ctk.CTkButton(
                context_menu,
                text="لصق",
                command=self.paste_from_clipboard
            )
            paste_option.pack(pady=2, padx=2)
            
            context_menu.place(x=event.x_root - self.winfo_rootx(), 
                             y=event.y_root - self.winfo_rooty())
            
            def close_menu(e):
                context_menu.destroy()
                self.unbind('<Button-1>', close_id)
            
            close_id = self.bind('<Button-1>', close_menu)
        except Exception as e:
            print(f"خطأ في إظهار القائمة: {str(e)}")

    def on_download(self):
        url = self.url_var.get()
        selected_display = self.format_var.get()
        selected_format = next(
            (f for f in self.formats if f['display'] == selected_display),
            None
        )
        
        if url and selected_format:
            self.download_callback(url, selected_format['format_id'])
            self.download_button.configure(state="disabled")
            self.format_combobox.configure(state="disabled")

    def enable_download(self):
        self.download_button.configure(state="normal")
        self.format_combobox.configure(state="normal")
        self.url_var.set("") 