import random
for i in range(3):
    print(random.uniform(10,30))
#random.random, 0-1 arası sayılar üretir. random.uniform verdiğimiz aralıkta küsürlü sayılar oluşturur.
    print(random.randint(1,5))
    print(random.randrange(1,10))

liste = ["Siyah","Beyaz", "Mavi","Yeşil","Gri","Turuncu"]
random.shuffle(liste) #listeyi karıştırıyor.
print(liste)
print(random.sample(liste,4)) #içine parametre olarak liste alıyor ve verdiğiniz sayı kadar karışık değer çekiyor

zarlar = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for i in range(1000000):
    zar = random.randint(1,6)
    zarlar[zar] += 1
for zar in zarlar:
    print(f"{zar} gelme olasılığı: {zarlar[zar] / 1000000}")

#10 kere 6-6 gelmesi için atış yap
import random

alti_alti = 0
deneme_sayisi = 0
while True:
    deneme_sayisi+=1
    zar1 = random.randint(1,6)
    zar2 = random.randint(1,6)
    if zar1 == 6 and zar2 == 6:
        alti_alti += 1
    if alti_alti ==10:
        print(f"10 kere 6-6 gelmesi için zarlar {deneme_sayisi} kadar atıldı.")
        break