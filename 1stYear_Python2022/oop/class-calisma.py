from datetime import date
class kisi:
    kisi_sayisi = 0
    def __init__(self,isim,yas):
        self.yas = yas
        self.isim = isim
        kisi.kisi_sayisi += 1
    def bilgilerini_soyle(self):
        return f"{'Ad'}:{self.isim:<10}{'Yaş'}:{self.yas}"
    @classmethod
    def kisi_sayisini_soyle(cls):
        return cls.kisi_sayisi
    @classmethod
    def string_ile_olustur(cls,str_):
        isim,yas = str_.split("-")
        print(isim)
        print(yas)
        yas = int(yas)
        return cls(isim,yas)
    @classmethod
    def dogum_yili_ile_olustur(cls,isim,dogum_yili):
        dogum_tarihi = date.today().year-dogum_yili
        return cls(isim,dogum_tarihi)
    @staticmethod
    def dogum_yili_hesapla(kisi):
        return date.today().year - kisi.yas

kisi1 = kisi("Ece",19)
kisi2 = kisi("Doğu",22)
kisi3 = kisi.string_ile_olustur("Ayşe-20")
kisi4 = kisi.dogum_yili_ile_olustur("Ege",2002)
print(kisi1.bilgilerini_soyle())
print(kisi.dogum_yili_hesapla(kisi1))
print(kisi2.bilgilerini_soyle())
print(kisi.dogum_yili_hesapla(kisi2))
print(kisi3.bilgilerini_soyle())
print(kisi.dogum_yili_hesapla(kisi3))
print(kisi4.bilgilerini_soyle())
print(kisi.dogum_yili_hesapla(kisi4))
#inheritance
class Calisan:
    zam_orani = 1.1
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + "@sirket.com"
    def bilgiler_goster(self):
        return "Ad: {} Soyad: {} Maas: {}  Email: {}".format(self.isim,self.soyisim,self.maas,self.email)

calisan1 = Calisan("ali","çalışkan",5000)
calisan2 = Calisan("veli","uzun",6000)

class Yazilimci(Calisan):
    def __init__(self,isim,soyisim,maas,bildigi_dil):
        super().__init__(isim,soyisim,maas) #super yukarıdaki class taki tanımlanmış initlere ulaşır.
        self.bildigi_dil = bildigi_dil
    zam_orani = 1.2

    def bilgiler_goster(self):
        return "Ad:{}\t Soyad:{}\tMaas:{}\tEmail:{}\tBidiği dil:{}".format(self.isim, self.soyisim, self.maas, self.email,self.bildigi_dil)

    def dilini_soyle(self):
        return f"Biidiğim dil: {self.bildigi_dil}"

class Yonetici(Calisan):

    def __init__(self,isim,soyisim,maas, calisanlar = None):
        super().__init__(isim,soyisim,maas)
        if calisanlar == None:
            self.calisanlar = []
        else:
            self.calisanlar =calisanlar
    def calisan_ekle(self,calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)

    def calisan_sil(self,calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)

    def calisanlari_goster(self):
        for calisan in self.calisanlar:
            print(calisan.bilgiler_goster())


yazilimci1 = Yazilimci("Ayşe","Yıldız",7000,"python")
yazilimci2 = Yazilimci("Fatma","Ay",8000,"java")
yonetici1 = Yonetici("Metin","Ali",10000)
yonetici1.calisan_ekle(calisan1)
yonetici1.calisan_ekle(yonetici1)
yonetici1.calisan_ekle(yazilimci1)
yonetici2 = Yonetici("ege","çelik",11000,[yazilimci1,yazilimci2])
yonetici1.calisan_sil(calisan1)
yonetici1.calisanlari_goster()
yonetici2.calisanlari_goster()

print(isinstance(yazilimci1,Yonetici)) #ondan mı türemiş diye soruyor.
print(issubclass(Yazilimci,Calisan)) #clisan sınıfı yazılımcıdan mı türedi diye sorduk

#Başka bir videonun konusu
class People:
    bilgiler = []
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        self.bilgiler.append([name,surname,age])
    def sorted_people(args):
        sorted_ = []
        for bilgi in People.bilgiler:
            print(bilgi)
            if args == "name":
                sorted_.append(bilgi[0])
            elif args == "surname":
                sorted_.append(bilgi[1])
            elif args == "age":
                sorted_.append(bilgi[2])

            sorted_ = sorted(sorted_)
        for i in sorted_:
            for j in People.bilgiler:
                if args == "name":
                    if i == j[0]:
                        print(j[0], j[1], j[2])
                elif args == "surname":
                    if i == j[1]:
                        print(j[0], j[1], j[2])
                elif args == "age":
                    if i == j[2]:
                        print(j[0], j[1], j[2])

args = input()
people1 = People("ece","irem",18)
people2 = People("doğu","filiz",22)
people3 = People("ciğdem","narin",46)
people4 = People("ahmet","onder",49)
People.sorted_people(args)


class Personel():
    def __init__(self,ad,soyad,yas,cinsiyet,maas):
        self.ad =ad
        self.soyad = soyad
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.maas = maas
    def bilgileri_yazdir(self):
        print("""
{} {} bilgileri şunlardır:
Yaş : {}
Cinsiyet : {}
Maaş : {}
        """.format(self.ad,self.soyad,self.yas,self.cinsiyet,self.maas))

    def __str__(self):
        return """
{} {} bilgileri şunlardır:
Yaş : {}
Cinsiyet : {}
Maaş : {}
        """.format(self.ad,self.soyad,self.yas,self.cinsiyet,self.maas)

class Yonetici(Personel):
    def __init__(self,ad,soyad,yas,cinsiyet,maas):
        super().__init__(ad,soyad,yas,cinsiyet,maas)

    def maas_arttir(self,p_object,artis_miktari = 1000):
        p_object.maas += artis_miktari
personal1 = Personel("Ece","Şişer","19","Kadın",10000)
yonetici = Yonetici("Doğukan","Filiz","22","Erkek",20000)
yonetici.maas_arttir(personal1,1500)
print(personal1)













