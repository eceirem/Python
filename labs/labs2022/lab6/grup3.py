dict_ = {}
hepsi = []
ortaklar = []
a = 0
satir_sayisi = 0
dosya = input() + ".txt"
with open(dosya,mode="r") as f:
    for satir in f:
        f = satir.strip("\n").split(" ")
        dict_[a] = f
        a += 1
        satir_sayisi += 1
for i in dict_.values():
    for j in i:
        j = int(j)
        hepsi.append(j)
for i in hepsi:
    if hepsi.count(i) == satir_sayisi:
        ortaklar.append(i)
        ortaklar.sort()
        hepsi.remove(i)
print(ortaklar)

