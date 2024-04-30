# ad,soyad 
# yas
# doğum tarihi



def kayit_sil(ad, dosya_yolu):
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

def kayit_ekle(ad,yas,d_tarih,dosya_yolu):
    try:
        with open(dosya_yolu,'a') as dosya:
            dosya.write(f"Ad Soyad: {ad}, Yaş: {yas}, Doğum tarihi: {d_tarih}\n")
        print("Kayıt başarıyla tamamlandı!")
    except IOError:
        print("Dosyaya yazdırma hatası!")
    


def kayitlari_goster(dosya_yolu):
    try:
        with open(dosya_yolu,'r') as dosya:
            print("-------Kayıtlar-------")
            for satir in dosya:
                print(satir, end='')
    except FileNotFoundError:
        print("Kayıt dosyası bulunamadı.")



dosya_yolu = "kayitlar.txt"



while True:
    print("""
          1. Yeni Kayıt Ekle
          2. Kayıtları Göster
          3. Kayıt Sil
          4. Çıkış
    """)
    
    secim = input("Yapmak istediğiniz işlemin numarasını giriniz(örn: 1 ): ")
    
    if secim == '1':
        ad = input("Ad Soyad giriniz: ")
        yas = input("Yaş değeri giriniz: ")
        d_tarih = input("Doğum tarihi giriniz: ")
        kayit_ekle(ad,yas,d_tarih,dosya_yolu)

    elif secim == '2' :
        kayitlari_goster(dosya_yolu)
    
    elif secim == '3' :
        ad = input("Ad Soyad giriniz: ")
        kayit_sil(ad,dosya_yolu)

    elif secim == '4': 
        print("Programdan Çıkılıyor!")
        break
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyiniz.")
    