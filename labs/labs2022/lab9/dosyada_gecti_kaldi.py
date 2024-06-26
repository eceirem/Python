with open("ornek_metin.txt","r") as f:
    with open("gecenler.txt","w",encoding="utf-8") as g:
        with open("values.txt", "w", encoding="utf-8") as k:
            icerik = f.readlines()
            m = 0
            for satir in icerik:
                if m == 0:
                    m += 1
                    continue
                satir = satir.replace("\n","")
                bosluk_sayisi = 0
                bosluk_indexleri = []
                index = 0
                for ch in satir:
                    if ch == " ":
                        bosluk_sayisi += 1
                        bosluk_indexleri.append(index)
                    index += 1
                ad_soyad = satir[:bosluk_indexleri[0]]
                soyad = ad_soyad.split("-")[-1]
                adlar = ad_soyad[:ad_soyad.index(soyad)-1].replace("-"," ")
                notlar = satir.split(" ")[-1]
                notlar = notlar.split("/")
                birinci_vize = int(notlar[0])
                ikinci_vize = int(notlar[1])
                final = int(notlar[2])
                ortalama = birinci_vize*0.3 + ikinci_vize*0.3 + final*0.4
                bolum_adi = satir[bosluk_indexleri[0]+1:bosluk_indexleri[len(bosluk_indexleri)-1]]
                if ortalama >= 70 and final >= 70:
                    g.write(adlar)
                    g.write(" " * (25-len(adlar)))
                    g.write(soyad)
                    g.write(" " * (25 - len(soyad)))
                    g.write(f"{ortalama:.1f}")
                    g.write(" " * 21)
                    g.write("Geçti")
                    g.write("\n")
                else:
                    k.write(adlar)
                    k.write(" " * (25-len(adlar)))
                    k.write(soyad)
                    k.write(" " * (25 - len(soyad)))
                    k.write(f"{ortalama:.1f}")
                    k.write(" " * 21)
                    k.write("Kaldı")
                    k.write("\n")