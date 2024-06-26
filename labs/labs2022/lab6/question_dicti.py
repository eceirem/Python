dicti = {}
liste = []
liste2 = []
dosya_adi = input()
dosya_adi += '.txt'
with open(dosya_adi, mode="r") as m:
    for satir in m:
        m = satir.strip("\n")
        dicti[m[0]] = m[1::].split()
dicti.values()
print(dicti)
for i in dicti.values():
    for k in i:
        if i.count(k) > 1:
            while i.count(k) != 1:
                i.remove(k)

liste += dicti.items()
liste.sort()
liste = liste[-1]
print(liste[0])
for i in liste[1]:
    liste2.append(int(i))
print(liste2)

