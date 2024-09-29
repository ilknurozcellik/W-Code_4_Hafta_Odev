# Kullanıcıdan kullanıcı adı ve şifre istenir
kullanici_adi = input("Kullanıcı adınızı giriniz: ")
sifre = input("Şifrenizi giriniz: ")

# Şifre uzunluğuna göre koşul
if len(sifre) >= 6:
    print("Hesabınız başarıyla oluşturuldu!")
else:
    print("Şifreniz en az 6 haneli olmalıdır!")

