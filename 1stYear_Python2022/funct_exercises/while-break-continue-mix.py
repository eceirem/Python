maaslar =[1000,2000,3000,4000,5000]
def maas_ust(x):
    print(x/10+x)
def maas_alt(x):
    print(x/5+x)
for i in maaslar:
    if i >= 3000:
        maas_ust(i)
    else:
        maas_alt(i)

#break&continue
maaslar = [8000,5000,2000,1000,3000,7000,1000]
maaslar.sort()
print(maaslar)
for i in maaslar:
    if i == 3000:
        print("kesildi")
        break
    print(i)
for i in maaslar:
    if i == 3000:
        continue
    print(i)
#while
sayi = 0
while sayi < 10:
    sayi += 1
    print(sayi)