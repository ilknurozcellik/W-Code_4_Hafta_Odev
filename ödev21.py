# Kullanıcıdan maaş bilgisi alınır
maas = float(input("Lütfen maaşınızı giriniz: "))

# Vergi oranı belirlenir
if maas <= 10000:
    vergi_orani = 0.05  # %5 kesinti
elif maas <= 25000:
    vergi_orani = 0.10  # %10 kesinti
elif maas <= 45000:
    vergi_orani = 0.25  # %25 kesinti
else:
    vergi_orani = 0.30  # %30 kesinti

# Vergi miktarı ve yeni maaş hesaplanır
vergi_miktari = maas * vergi_orani
yeni_maas = maas - vergi_miktari

# Sonuçları yazdırma
print(f"Maaşınıza uygulanan vergi oranı: %{vergi_orani * 100}")
print(f"Vergi miktarı: {vergi_miktari:.2f} TL")
print(f"Vergi kesildikten sonra yeni maaşınız: {yeni_maas:.2f} TL")
