def asal(sayi):
    isprime=True
    for i in range(2,sayi):
        if sayi % i ==0:
            isprime=False
            break
    return isprime
x = int(input())
a=2
pf =''
while x!=1:
    if x % a == 0:
        x = x//a
        pf += str(a) + " "
        while x % a == 0:
            x=x//a
    a+=1
    while not asal(a):
        a+=1
print(pf)