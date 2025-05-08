import tkinter as tk
from tkinter import messagebox
from database import veritabani_baglan
from analiz import grafik_goster
import datetime

conn = veritabani_baglan()

def kaydet():
    kategori = kategori_entry.get()
    miktar = miktar_entry.get()
    tarih = datetime.datetime.now().strftime("%Y-%m-%d")
    
    if not kategori or not miktar:
        messagebox.showerror("Hata", "Tüm alanlar doldurulmalı.")
        return

    try:
        miktar = float(miktar)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO harcamalar (kategori, miktar, tarih) VALUES (?, ?, ?)",
                       (kategori, miktar, tarih))
        conn.commit()
        messagebox.showinfo("Başarılı", "Kayıt eklendi.")
        kategori_entry.delete(0, tk.END)
        miktar_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Miktar sayısal olmalı.")

def analiz_yap():
    grafik_goster()

pencere = tk.Tk()
pencere.title("Gider Takip Uygulaması")

tk.Label(pencere, text="Kategori:").grid(row=0, column=0)
kategori_entry = tk.Entry(pencere)
kategori_entry.grid(row=0, column=1)

tk.Label(pencere, text="Miktar (TL):").grid(row=1, column=0)
miktar_entry = tk.Entry(pencere)
miktar_entry.grid(row=1, column=1)

tk.Button(pencere, text="Kaydet", command=kaydet).grid(row=2, column=0, pady=10)
tk.Button(pencere, text="Analiz", command=analiz_yap).grid(row=2, column=1)

pencere.mainloop()