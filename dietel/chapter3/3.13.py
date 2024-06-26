sayi = int(input())
bolen_sayi=0
for i in range(1,sayi):
    if sayi % i == 0:
        bolen_sayi += i
        #print(int(i)) ; print(int(i), "*", int(sayi/i), "=" , int(sayi)) yazsaydım tüm çarpanları görürdüm.
print(bolen_sayi)
if bolen_sayi==sayi:
    print("This is a perfect number.")
else:
    print("This is not a perfect number.")