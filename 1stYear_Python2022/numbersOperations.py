#ekrandan alınan bir sayının faktörüyelini hesaplayan bir programı yazınız.

sayi = int(input("Bir sayı giriniz: "))
faktöriyel=1
for i in range(1,sayi+1):
    faktöriyel *= i
print(f"{sayi}! = {faktöriyel}")

sayi = int(input("Bir sayı giriniz: "))
i = 1
while i <= sayi:
    faktöriyel *=1
    i += 1
print(f"{sayi}! = {faktöriyel}")

#ekrandan alınan bir sayının asal olup olmadığını kontrol eden bir program

sayi =int(input("Bir sayı giriniz: "))
prime = True
for rakam in range(2,sayi):
    if sayi % rakam == 0:
     prime = False
     break
if prime:
     print("Asal sayıdır.")
else:
    print("sayı asal değildir.")
#ekrandan alınan bir sayının kaç tane böleni olduğunu bulan bir program
sayi2 = int(input("Bir sayı giriniz: "))
bolen_sayisi = 0
for i in range(1, sayi2+1):
    if sayi2 % i==0:
        bolen_sayisi += 1
print(bolen_sayisi)

#ekrandan okunan bir sayının rakamları toplamını hesaplayan bir program
sayi3= input("Bir sayı giriniz: ")
toplam = 0
for i in sayi3:
    toplam += int(i)
print(toplam)

sayi4=int(input("bir sayı giriniz: "))
toplam = 0
gecici_sayi = sayi
while gecici_sayi !=0:
    basamak = gecici_sayi % 10
    toplam += basamak
    gecici_sayi//=10
print(toplam)
#ekrandan peş peşe okunan 5 sayının en küçüğünü ve en büyüğünü yazıran program
liste = []
for i in range(5):
    sayi=int(input("Bir sayı giriniz: "))
    liste.append(sayi)
print(f"en büyük sayı : {max(liste)}")
print(f"en küçük sayı : {min(liste)}")
#ekrandan okunan bir sayının herhangi bir sayının karesi olup olmadığını gösteren program
sayi = int(input("Bir sayı giriniz: "))
sayi2 = (sayi)**(1/2)
if sayi2 % 1==0:
    print(sayi, "bir tam kare sayıdır.")
else:
    print(sayi, "bir tam kare sayı değildir.")
#alternatif 2. yol
sayi = int(input("Bir sayı giriniz: "))
sayi2 = (sayi)**(1/2)
if sayi2== int(sayi2):
    print("Tam kare")
else:
    print("Tam kare değildir.")
#ekrandan okunan bir metinde a ları A yapan program
metin = input("bir metin giriniz: ")
metin2=""
for i in metin:
    if i == 'a':
        metin2 += 'A'
    else:
        metin2 += i
print(metin2)
#ekrandan bir metinde hangi harfin kaç kere kullanıldığını gösteren program
veri = input()
kontrol = ''
for i in veri:
    c = 0
    if i not in kontrol:
        kontrol += i
        for k in veri:
            if i == k:
                c += 1
        print(i, c)

# rakamlarının küpleri toplamı kendisine eşit olan 3 bas. rakamlar
def kup(x):
    toplam = 0
    for i in str(x):
        toplam += int(i)**3
    if toplam == x:
        print(toplam)
        return True
    else:
        return False
index = 0
for i in range(100,1000):
    if kup(i):
        index += 1
print(index)


#ilk 10.000 asal sayının kaç tanesi 3 ile başlar ve 7 ile biter?
prime_list = list()
prime_list.append(2)
sayi = 3
while True:
    prime = True
    for i in range(2,int(sayi**0.5)+1):
        if sayi % i == 0:
            prime = False
            break
    if prime:
        prime_list.append(sayi)
        if len(prime_list) == 10000:
            break
    sayi += 1
liste2 = []
for prime in prime_list:
    strprime= str(prime)
    if strprime.startswith("3") and strprime.endswith("7"):
        liste2.append(prime)
print(liste2)
print(len(liste2))

#fibonacci
sira = int(input("Hesaplamak istediğiniz dizi sırasını giriniz: "))
n1 = 1
n2 = 1
nth = 0
print(n1)
print(n2)

for i in range(0,sira):
    nth = n1 + n2
    n1 = n2
    n2 = nth
    print(nth)
