def factoriyel(x):
    sonuc = 0
    if x == 1:
        sonuc = 1
    else:
        sonuc = x * factoriyel(x-1)
    return sonuc
x = int(input("Faktöriyelini bulamak istediğiniz değeri söyleyiniz: "))
deger = factoriyel(x)
print(f"{x}! = {deger}")