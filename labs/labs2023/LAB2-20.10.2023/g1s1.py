# Kullanıcıdan iki pozitif tam sayı alın
sayi1 = int(input())
sayi2 = int(input())

# İlk sayının Collatz dizisini hesapla
adim_sayisi1 = 0
while sayi1 != 1:
    if sayi1 % 2 == 0:
        sayi1 //= 2
    else:
        sayi1 = 3 * sayi1 + 1
    adim_sayisi1 += 1

# İkinci sayının Collatz dizisini hesapla
adim_sayisi2 = 0
while sayi2 != 1:
    if sayi2 % 2 == 0:
        sayi2 //= 2
    else:
        sayi2 = 3 * sayi2 + 1
    adim_sayisi2 += 1

# Sonuçları ekrana yazdır
print(adim_sayisi1)
print(adim_sayisi2)
