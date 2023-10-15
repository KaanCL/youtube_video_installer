import tkinter as tk
import yt_dlp
import re
import os
from os.path import expanduser

def indir():
    user_url = url_entry.get()
    if re.match(r"^(http|https)://", user_url):
        result_label.config(text="Geçerli URL: " + user_url)
        
        # Masaüstü yolunu al
        desktop_path = os.path.join(expanduser("~"), "Desktop")
        
        # "indirilenler" klasörünü masaüstüne oluştur
        download_folder = os.path.join(desktop_path, "indirilenler")
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
            'progress_hooks': [progress_hook],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([user_url])
            result_label.config(text="İşlem Başarılı!", fg="green")
    else:
        result_label.config(text="Geçersiz URL", fg="red")

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d['_percent_str']
        percent_label.config(text=percent)
    elif d['status'] == 'finished':
        percent_label.config(text="İndirme Tamamlandı")

# Ana pencere oluşturuluyor
root = tk.Tk()
root.title("Youtube Video İndirici")
root.geometry("400x250")

# Metin giriş kutusu ve etiketleri oluşturuluyor
baslik_label = tk.Label(root, text="Video URL'sini yazınız:")
baslik_label.pack()

url_entry = tk.Entry(root, width=70)
url_entry.pack()

# İşlem düğmesi oluşturuluyor
submit_button = tk.Button(root, text="İndir", command=indir)
submit_button.pack()

# İndirme yüzdesini gösteren etiket
percent_label = tk.Label(root, text="", fg="blue")
percent_label.pack()

# Sonuç etiketi oluşturuluyor
result_label = tk.Label(root, text="Sonuç: ")
result_label.pack()

# Pencereyi açık tut
root.mainloop()