import math
def binary_to_int (sayi):
    temp = 0
    us = 0
    intSayi = 0
    while(sayi != 0):
        temp = sayi%10
        intSayi += temp * pow(2,us)
        us += 1
        sayi //= 10

    return intSayi

binarySayi = int(input())
intSayi = binary_to_int(binarySayi)
print(intSayi)
