# Kullanıcıdan kullanıcı adı istenir
kullanici_adi = input("Kullanıcı adınızı giriniz: ")

# Şifre doğru uzunlukta olana kadar döngü devam eder
while True:
    sifre = input("Şifrenizi giriniz (5-10 karakter arasında olmalıdır): ")
    
    # Şifre uzunluğu kontrol edilir
    if 5 <= len(sifre) <= 10:
        print("Hesabınız başarıyla oluşturuldu!")
        break  # Şifre uygun olduğunda döngü sona erer
    else:
        print("Lütfen girdiğiniz şifre 5 haneden az ve 10 haneden fazla olmasın!")
