#karışık bir listedeki integer değerleri liste şeklinde döndüren fonksiyonu yazınız. ["1", 3, "abc", "1a2"]

def getIntFromList(liste):
    return_list = []
    for i in liste:
        if type(i) == int:
            return_list.append(i)
        else: #demek ki bir string içerisindeyim. str elemanlarının değerlerine bakarım ama her karakter sağlamalı bu yüzden bir bool değer atadım.
            boolean = 1
            for x in i:
                if x > "0" and x < "9":     #0 ve 9 arasında ise hepsi bana bir sayıyı söyler.
                    continue
                else:           #0 ve 9 arasında değilse ascii değeri daha büyük olan bir şeydir, harf gibi. bu da int değildir.
                    boolean = 0
            if boolean:
                return_list.append(int(i))
    return return_list

liste = ["1", 3, "abc", "12a3"]
print(getIntFromList(liste))