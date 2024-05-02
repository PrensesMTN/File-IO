import tkinter as tk
from tkinter import messagebox

def kayit_sil():
    ad = sil_entry.get()
    try:
        with open(dosya_yolu, 'r') as dosya:
            satirlar = dosya.readlines()
        with open(dosya_yolu, 'w') as dosya:
            silindi = False
            for satir in satirlar:
                if ad not in satir:
                    dosya.write(satir)
                else:
                    silindi = True
            if silindi:
                print(f"{ad} adlı kayıt başarıyla silindi.")
            else:
                print(f"{ad} adlı kayıt bulunamadı.")
    except FileNotFoundError:
        print("Kayıt dosyası bulunamadı.")

def kayit_ekle():
    ad = ad_entry.get()
    yas = yas_entry.get()
    d_tarih = dt_entry.get()
    if ad and yas and d_tarih:     
        try:
            with open(dosya_yolu,'a') as dosya:
                dosya.write(f"Ad Soyad: {ad}, Yaş: {yas}, Doğum tarihi: {d_tarih}\n")
            messagebox.showinfo("BAŞARILI","Kayıt başrılı oldu")
        except IOError:
            messagebox.showerror("HATA!","Dosya Açılamadı.")    
    else:
        messagebox.showerror("HATA!","Lütfen bir giriş yapınız.")    

def kayitlari_goster():
    try:
        with open(dosya_yolu,'r') as dosya:
            kayitlar = dosya.read()
        messagebox.showinfo("Kayıtlar",kayitlar)
    except FileNotFoundError:
        print("Kayıt dosyası bulunamadı.")

dosya_yolu = "kayitlar.txt"
pencere =tk.Tk()
pencere.title("kayıt Tutma Programı")

#ad soyad giriş etiketi ve entrysi
ad_label = tk.Label(pencere,text="Ad Soyad")
ad_label.grid(row=0,column=0,padx=5,pady=5)
ad_entry=tk.Entry(pencere)
ad_entry.grid(row=0,column=1,padx=5,pady=5)

#yas giriş etiketi ve entry
yas_label = tk.Label(pencere,text="Yaş")
yas_label.grid(row=1,column=0,padx=5,pady=5)
yas_entry=tk.Entry(pencere)
yas_entry.grid(row=1,column=1,padx=5,pady=5)

#dogum tarihi giriş etiketi ve entry
dt_label = tk.Label(pencere,text="Doğum Tarihi")
dt_label.grid(row=2,column=0,padx=5,pady=5)
dt_entry=tk.Entry(pencere)
dt_entry.grid(row=2,column=1,padx=5,pady=5)

# kayıt ekleme butonu
ekle_buton = tk.Button(pencere,text="EKLE",command=kayit_ekle)
ekle_buton.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

# kayıt göster butonu
ekle_buton = tk.Button(pencere,text="Kayıtları Göster",command=kayitlari_goster)
ekle_buton.grid(row=4,column=0,columnspan=2,padx=5,pady=5)

# Kayıt silme
sil_label = tk.Label(pencere, text="Silinecek Kaydın Adı Soyadı:")
sil_label.grid(row=5,column=0,padx=5,pady=5)
sil_entry = tk.Entry(pencere)
sil_entry.grid(row=5,column=1,padx=5,pady=5)

#sil button
sil_button = tk.Button(pencere,text="Kayıt Sil", command=kayit_sil)
sil_button.grid(row=5,column=5,columnspan=2,padx=5,pady=5)

pencere.mainloop()