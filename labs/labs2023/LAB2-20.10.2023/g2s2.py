# Kullanıcıdan pozitif bir tam sayı alın
sayi = int(input())

# Rakamların çarpımını hesapla
rakam_carpimi = 1
kopya_sayi = sayi

while kopya_sayi > 0:
    rakam = kopya_sayi % 10
    rakam_carpimi *= rakam
    kopya_sayi //= 10

print(rakam_carpimi)
