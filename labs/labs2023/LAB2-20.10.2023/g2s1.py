# Kullanıcıdan pozitif bir tam sayı alın
sayi = int(input())

# Başlangıç değerleri
toplam = 0
kalan = sayi
basamak = 4

while kalan > 0:
    rakam = kalan % 10
    toplam += rakam ** basamak
    kalan //= 10
    basamak -= 1

print(toplam)

# Disarium sayısı kontrolü
if toplam == sayi:
    print("disarium")
else:
    print("notdisarium")
