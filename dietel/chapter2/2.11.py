saniye = int(input("Bir saniye giriniz: "))
saat = saniye//3600
dakika = (saniye % 3600)//60
kalansn = ((saniye-saat*3600) - 60*dakika)
print(saat,dakika, kalansn, sep="-")