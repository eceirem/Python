def ilk_tutar(fiyatlar,miktarlar):
    toplam = 0
    for i in range(3):
        toplam += int(fiyatlar[i])*int(miktarlar[i])
    return toplam

def indirim_hesapla(ilkTutar):
    if ilkTutar <= 100:
        indirim_orani = 10
    elif ilkTutar > 100 and ilkTutar< 500:
        indirim_orani = 15
    elif ilkTutar > 500:
        indirim_orani = 20
    return indirim_orani

def son_tutar(indirim_orani,ilkTutar):
    sonTutar = ilkTutar - (ilkTutar*(indirim_orani/100))
    return sonTutar

fiyatlar = input().split()
miktarlar = input().split()
ilkTutar = ilk_tutar(fiyatlar,miktarlar)
indirimOrani = indirim_hesapla(ilkTutar)
sonTutar = son_tutar(indirimOrani,ilkTutar)


print(ilkTutar,  indirimOrani,  sonTutar)