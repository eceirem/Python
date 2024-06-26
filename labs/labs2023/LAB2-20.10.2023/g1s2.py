# Kullanıcıdan pozitif bir tam sayı alın
sayi = int(input())

# Rakamların toplamını hesapla
toplam = 0
kopya_sayi = sayi

while sayi > 0:
    rakam = sayi % 10
    toplam += rakam
    sayi //= 10
print(toplam)
# Harshad sayısı olup olmadığını kontrol et
if kopya_sayi % toplam == 0:
    print("harshad")
else:
    print("notharshad")
