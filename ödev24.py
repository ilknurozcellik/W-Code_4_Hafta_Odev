# Önceden tanımlı şifre
dogru_sifre = "455687"

# Kullanıcıdan isim alınır
kullanici_adi = input("Kullanıcı adınızı giriniz: ")

# Kullanıcıya şifre giriş hakkı veriyoruz
hak = 3

# Şifre girişini kontrol eden döngü
while hak > 0:
    sifre = input("Şifrenizi giriniz: ")
    
    if sifre == dogru_sifre:
        print("Giriş yapıldı.")
        break  # Doğru şifre girilirse döngü sona erer
    else:
        hak -= 1  # Yanlış şifre durumunda hak sayısı 1 azalır
        if hak > 0:
            print(f"Yanlış şifre girildi! Kalan hakkınız: {hak}")
        else:
            print("Şifreyi 3 kez yanlış girdiniz. Giriş hakkınız bitti!")
