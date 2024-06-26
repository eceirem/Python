class Sirket():
    def __init__(self,ad):
        self.ad = ad
        self.calisma = True
    def program(self):
        secim = self.menuSecim()
        if secim == 0:
            self.calisma = False
        if secim == 1:
            self.calisanEkle()
        if secim == 2:
            self.calisanCikar()
        if secim == 3:
            ay_yil_secim = input("Yıllık bazda görmek ister misiniz?(e/h)")
            if ay_yil_secim == "e":
                self.verilecekMaasGoster(hesap="y")
            else:
                self.verilecekMaasGoster()
        if secim == 4:
            self.maaslariVer()
        if secim == 5:
            self.masrafGoster()
        if secim == 6:
            self.gelirGir()
        if secim == 7:
            self.net_kar_hesaplama()
    def menuSecim(self):
        secim = int(input("*** {} Firmasına hoş geldiniz. ***\n\n0-Menü Çıkış\n1-Çalışan Ekle\n2-Çalışan Çıkar\n"
                      "3-Verilecek Maaş Göster\n4-Maaşları Ver\n5-Masraf Göster\n6-Gelir Gir\n"
                          "7-Net Kâr göster\n\nSeçiminizi giriniz: ".format(self.ad)))
        while secim < 0 or secim > 7:
            secim = int(input("Lütfen 1 - 6 arassında belirtilen seçeneklerden birini giriniz!\n"
                              "İşlem numaranızı tekrar giriniz: "))
        return secim
    def calisanEkle(self):
        ad = input("Çalışanın adını giriniz: ")
        soyad = input("Çalışanın soyadını giriniz: ")
        yas = input("Çalışanın yaşını giriniz: ")
        cinsiyet = input("Çalışanın cinsiyetini giriniz: ")
        proje_sayisi = input("Çalışanın uğraştığı proje sayısını giriniz: ")
        maas = input("Çalışanın maaşını giriniz: ")
        with open("calisanlar.txt","r") as dosya:
            calisanListesi = dosya.readlines()
        if len(calisanListesi) == 0:
            id = 1
        else:
            with open("calisanlar.txt","r") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1
        with open("calisanlar.txt","a+") as dosya:
            dosya.write("{}){}-{}-{}-{}-{}-{}\n".format(id,ad,soyad,yas,cinsiyet,proje_sayisi,maas))
    def calisanCikar(self):
        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()
        gCalisanlar = []
        for calisan in calisanlar:
            gCalisanlar.append(" ".join(calisan.strip("\n").split("-")))
        for calisan in gCalisanlar:
            print(calisan)
        secim = int(input("Lütfem çıkartmak isteidiğiniz çalışanın numarasını giriniz.(1 - {}):".format(len(gCalisanlar))))
        while secim < 1 or secim > len(gCalisanlar):
            print("Lütfen (1-{}) arasında numara giriniz: ".format(len(gCalisanlar)))
        calisanlar.pop(secim-1)
        counter = 1
        dCalisanlar = []
        for calisan in calisanlar:
            dCalisanlar.append(str(counter)+")"+calisan.split(")")[1])
            counter += 1
        with open("calisanlar.txt","w") as dosya:
            dosya.writelines(dCalisanlar)
    def verilecekMaasGoster(self,hesap = "a"):
        '''hesap: a ise aylik, y ise yillik hesap'''
        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()
        maaslar = []
        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))
        if hesap == "a":
            print("Toplam verilecek aylık maaş tutarı: " + str(sum(maaslar)))
        else:
            print("Toplam verilecek yıl içerisindeki maaş tutarı: " + str(sum(maaslar)*12))
    def maaslariVer(self):
        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()
        maaslar = []
        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))
        toplam_maas = sum(maaslar)
        #bütçeden maaşları ödeyip bütçeyi güncelleme
        with open("butce.txt","r") as dosya:
            toplam_butce = int(dosya.readlines()[0])
        toplam_butce -= toplam_maas
        with open("butce.txt","w") as dosya:
            dosya.write(str(toplam_butce))
        return toplam_maas
    def proje_sayisi(self):
        total_proje = 0
        with open("calisanlar.txt", "r") as dosya:
            calisanlar_info = dosya.readlines()
            for proje in calisanlar_info:
                total_proje += int(proje.split("-")[-2])
        return total_proje
    def proje_maliyeti(self):
        total_proje_maliyeti = self.proje_sayisi() * 500
        tercih = input("Proje maliyetlerini görmek ister misiniz?(e/h): ")
        if tercih == "e":
            print("Proje maliyeti: " + str(total_proje_maliyeti) + " liradır" )
        else:
            print("{} projenin maliyeti hesaplanmıştır.".format(self.proje_sayisi()))
        return total_proje_maliyeti
    def masrafGoster(self):
        total_masraf = 0
        total_masraf = self.maaslariVer() + self.proje_maliyeti()
        print("Proje masrafları ve maaş ödemeleri ile toplam masraf {} liradır.".format(total_masraf))
        return total_masraf
    def gelirGir(self):
        proje_geliri = 0
        if self.proje_sayisi() > 10:
            proje_geliri = self.proje_sayisi() * 5000
            print("Proje sayısı: {}, Proje geliri: {}".format(self.proje_sayisi(),proje_geliri))
        else:
            proje_geliri = self.proje_sayisi() * 2000
            print("Proje sayısı: {}, Proje geliri: {}".format(self.proje_sayisi(), proje_geliri))
        with open("butce.txt", "r") as dosya:
            toplam_butce = int(dosya.readlines()[0])
        toplam_butce += proje_geliri
        with open("butce.txt", "w") as dosya:
            dosya.write(str(toplam_butce))
        return proje_geliri
    def net_kar_hesaplama(self):
        gelen = self.gelirGir()
        giden = self.masrafGoster()
        net_kar = gelen - giden
        print("Hesaplanan net kâr miktarı: ".format(net_kar))
sirket = Sirket("Odeon Yazılımcılık")
while sirket.calisma:
    sirket.program()