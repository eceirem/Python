evinMetreKareFiyati = 0
evinMetreKaresi = 0
evinVergiYüzdesi= 0
aylikOdenebilecekTaksit = 0
pesinat = 0
yillikFaiz = 0
taksitSayisi = 0


while True:
    evinMetreKareFiyati = int(input())
    if(evinMetreKareFiyati == (-1)):
        break
    evinMetreKaresi = int(input())
    evinVergiYüzdesi= int(input())
    aylikOdenebilecekTaksit = int(input())
    pesinat = int(input())
    yillikFaiz = int(input())
    taksitSayisi = int(input())
    evinFiyati = ((evinMetreKaresi*evinMetreKareFiyati)+(evinMetreKaresi*evinMetreKareFiyati * (evinVergiYüzdesi)/100))
    aylikFaiz = yillikFaiz/1200
    krediTutari = evinFiyati - pesinat
    aylikTaksitMiktari = krediTutari * (aylikFaiz*((1+aylikFaiz)**taksitSayisi)/(((1+aylikFaiz)**taksitSayisi)-1))
    if(aylikTaksitMiktari <= aylikOdenebilecekTaksit):
        print("true")

    else:
        print("false")