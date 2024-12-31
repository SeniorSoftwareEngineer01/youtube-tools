import sys
import os

# إضافة المجلد الرئيسي إلى مسار Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import customtkinter as ctk
from windows.ui.app import App

def main():
    # تعيين المظهر الافتراضي
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # إنشاء النافذة الرئيسية
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main() 