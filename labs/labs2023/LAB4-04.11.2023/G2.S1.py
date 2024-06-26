sehirKodu = int(input())
evinMetreKaresi = int(input())
pesinat = int(input())
yillikFaiz = int(input())
taksitSayisi = int(input())
yazdirmakIstenenTaksitSayisi = int(input())

if sehirKodu == 34:
    evinMetreKareFiyati = 5000
elif sehirKodu == 23:
    evinMetreKareFiyati = 4500
elif sehirKodu == 35:
    evinMetreKareFiyati = 4000
elif sehirKodu == 33:
    evinMetreKareFiyati = 3500
elif sehirKodu == 55:
    evinMetreKareFiyati = 3000

evinFiyati = (evinMetreKaresi*evinMetreKareFiyati)
aylikFaiz = yillikFaiz/1200
krediTutari = evinFiyati - pesinat
aylikTaksitMiktari = krediTutari * (aylikFaiz*((1+aylikFaiz)**taksitSayisi)/(((1+aylikFaiz)**taksitSayisi)-1))
kalanBorc = evinFiyati - pesinat

for i in range(yazdirmakIstenenTaksitSayisi):
    odenecekFaizMiktari = kalanBorc * aylikFaiz
    odenecekAnaParaMiktari = aylikTaksitMiktari - odenecekFaizMiktari
    print(f"{kalanBorc:.2f}")
    print(f"{odenecekFaizMiktari:.2f}")
    print(f"{odenecekAnaParaMiktari:.2f}")
    kalanBorc -= aylikTaksitMiktari
