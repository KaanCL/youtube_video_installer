import tkinter as tk
import yt_dlp
import re

def indir():
    user_url = url_entry.get()
    if re.match(r"^(http|https)://", user_url):
        result_label.config(text="Geçerli URL: " + user_url)
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([user_url])
            result_label.config(text="İşlem Başarılı !",fg="green")
    else:
        result_label.config(text="Geçersiz URL",fg="red")

# Ana pencere oluşturuluyor
root = tk.Tk()
root.title("Youtube Video İndirici")
root.geometry("400x200")

# Metin giriş kutusu ve etiketleri oluşturuluyor
baslik_label = tk.Label(root, text="Video URL'sini yazınız:")
baslik_label.pack()

url_entry = tk.Entry(root, width=70)
url_entry.pack()

# İşlem düğmesi oluşturuluyor
submit_button = tk.Button(root, text="İndir", command=indir)
submit_button.pack()

# Sonuç etiketi oluşturuluyor
result_label = tk.Label(root, text="Sonuç: ")
result_label.pack()

# Pencereyi açık tut
root.mainloop()



