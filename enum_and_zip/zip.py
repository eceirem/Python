#meyveList = ["elma","armut","kavun","karpuz"]
#siraList = [1,2,3,4]
#
#for val in zip(siraList, meyveList):
#    print(val)

kisiList = ["Burak", "Tuğçe", "Öner", "Eylül"]
puanList = [90,80,30,60]
harfList = ["AA", "BB", "EE", "CC"]

for kisi,puan,harf in zip(kisiList,puanList,harfList):
    print("{} kişisi {} puanı aldı. Harf notu: {}".format(kisi,puan,harf))