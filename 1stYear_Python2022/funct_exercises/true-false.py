#True-False Sorgulamaları
sinir = 5000
print(sinir == 5000) #denk midir? sorusunu soruyoruz.
print(5 == 4)
#if ve else
sinir = 50000
gelir = 35000
print(gelir < sinir)
if gelir < sinir:
    print("Gelir sınırdan küçük")
    print(gelir*2)
else:
    print("Gelir sınırdan büyük")
#elif
sinir = 50000
gelir1 = 60000
gelir2= 50000
gelir3= 35000
if gelir1 > sinir:
    print("Tebrikeler, hediye kazandınız.")
elif gelir1 < sinir:
    print("Uyarı!")
else:
    print("Gelir ve Sınır eşittir. Takibe devam.")

if gelir3 > sinir:
    print("Tebrikeler, hediye kazandınız.")
elif gelir3 < sinir:
    print("Uyarı!")
else:
    print("Gelir ve Sınır eşittir. Takibe devam.")

if gelir2 > sinir:
    print("Tebrikeler, hediye kazandınız.")
elif gelir2 < sinir:
    print("Uyarı!")
else:
    print("Gelir ve Sınır eşittir. Takibe devam.")

#mini uygulama
sinir=50000
magaza_adi = input("Magaza Adi Nedir? ")
gelir = int(input("Gelirinizi Giriniz: "))
if gelir > sinir:
    print("Tebrikler:" + magaza_adi + " promosyon kazandınız!")
elif gelir<sinir:
    print("Uyarı!Çok düşük gelir: "+ str(gelir))
else:
    print("Takibe Devam")

