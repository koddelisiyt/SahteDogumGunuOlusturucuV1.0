import tkinter as tk
from datetime import datetime
import random

def sahte_tarih_uret():
    yil = random.randint(1980, 2009)
    ay = random.randint(1, 12)
    gun = random.randint(1, 28)
    tarih = datetime(yil, ay, gun).strftime("%Y-%m-%d")
    tarih_var.set(tarih)

# Arayüz oluştur
pencere = tk.Tk()
pencere.title("Sahte Doğum Günü Oluşturucu V1.0")  # ← İstediğin başlık burada
pencere.geometry("300x200")
pencere.configure(bg="#1e1e1e")

# Başlık
etiket = tk.Label(pencere, text="Sahte Doğum Tarihi", font=("Courier", 14), fg="lime", bg="#1e1e1e")
etiket.pack(pady=10)

# Tarih alanı
tarih_var = tk.StringVar()
tarih_goster = tk.Entry(pencere, textvariable=tarih_var, font=("Courier", 12), justify="center")
tarih_goster.pack(pady=5)

# Buton
buton = tk.Button(pencere, text="Yenile 🔄", command=sahte_tarih_uret, font=("Courier", 12), bg="gray", fg="white")
buton.pack(pady=10)

# İlk tarih üretimi
sahte_tarih_uret()

# Çalıştır
pencere.mainloop()
