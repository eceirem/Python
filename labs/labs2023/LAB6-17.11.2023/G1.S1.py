def gcd_func(sayi1,sayi2):
    remainder = 0
    if(sayi2==0):
        return sayi1
    else:
        remainder = sayi1 % sayi2
        return gcd_func(sayi2,remainder)
    
x = int(input())
y = int(input())
gcd = gcd_func(x,y)
print(gcd)