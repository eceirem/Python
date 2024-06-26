class VeriBilimci:
    bildigi_diller = ["C,C+"]
    bolum = ""
    def __init__(self):
        self.deneyim_yili = 0
        self.bildigi_diller = []
        self.bolum = " "
ali = VeriBilimci()
ali.deneyim_yili = 4
ali.bolum = "İstatistik"
print(ali.bolum)
print(ali.deneyim_yili)
ali.bildigi_diller.append("Python")
print(ali.bildigi_diller)
veli = VeriBilimci()
veli.bolum = "bilgisayar_müh"
print(veli.bolum)
print(veli.deneyim_yili)
veli.bildigi_diller.append("Kotlin")
print(veli.bildigi_diller)
print(VeriBilimci.bildigi_diller)

class Veri_Bilimci:
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""

    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)


ece = Veri_Bilimci()
ege = Veri_Bilimci()
ece.dil_ekle("Python")
ege.dil_ekle("C#")
print(ege.bildigi_diller)
print(ece.bildigi_diller)