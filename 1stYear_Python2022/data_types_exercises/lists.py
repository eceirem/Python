#[] ve list() ile liste oluşturabiliyoruz.
notlar=[90,80,70,50]
print(type(notlar))
liste2=[3.2, 6, "a"]
print(type(liste2[2]))
liste3=[liste2, notlar]
print(liste3)
#del liste3
print(liste3[0:4])
#liste elemanlarına ulaşım
liste=[10,20,30,40,50]
yeni_liste=["a",10, [20,30,40,50]]
print([yeni_liste[0:2]])
print(yeni_liste[2][1])
#liste elemanlarını değiştirme
liste4 = ["ali", "veli", "ece","ayse"]
liste4[1] = "velinin_babası"
print(liste4)
liste4[0:3] ="alinin_babası","veli","berkcanın_babası"
print(liste4)
liste4 += ["kemal"]
print(liste4)
del liste4[2]
print(liste4)
#liste fonksiyonları
print(dir(liste4))
liste4.append("ışık")
print(liste4)
liste4.remove("ışık")
print(liste4)
##insert
liste4.insert(0,"ayse")
print(liste4)
liste4[1]="ali"
print(liste4)
liste4.insert(2,"mehmet")
print(liste4)
liste4.insert(len(liste),"beren")
print(liste4)
liste4.insert(len(liste4),"ece")
print(liste4)
#pop
liste4.pop(0)
print(liste4)
#count
print(liste4.count("ali"))

#copy
liste_yedek = liste4.copy()
print(liste_yedek)

#extend
liste4.extend(["a","b",10])
print(liste4)

#index
print(liste4.index("ali"))

#reverse()
liste4.reverse() #elemanlar tersten olacak şekilde sıralanır.
print(liste4)
#sort()
#liste4.sort() #int ve str karşılaştırması yapamaz. Bu yüzden tiplere dikkat etmek lazım.
#print(liste4)
liste5 =[10,40,5,70]
liste5.sort()
print(liste5)

#clear
liste5.clear()
print(liste5)

liste6 = [9,7,1,2,13,72,83]
liste6.sort()
print(liste6)