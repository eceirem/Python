#Fonksiyon nasıl yazılır?
def square(x):
    print("girilen sayi: " +str(x) + ", karesi: " + str(x**2))
square(3)
def carpma_yap(x,y):
    print("sonuç: ", x*y)
carpma_yap(3,9)
#ön tanımlı argümanlar
def us_al(x,y):
    print("sonuç: ", x**y)
us_al(y=2,x=4)
#ne zaman fonskiyon yazılır?
# isi, nem, şarj
def direk_hesaplama(isi,nem,sarj):
    print((isi+nem)/sarj)
direk_hesaplama(25,40,70)
#çıktıyı girdi olarak kullanmak
def direk_hesaplama(isi,nem,sarj):
    return((isi+nem)/sarj)
cikti = direk_hesaplama(25,40,70)*9
print(cikti)
#Local ve Global Değişkenler
x = 10
y = 20          #global değişkenler bunlar
def carpma_yap(x,y):
    return print(x*y)
carpma_yap(2,3) #local değişkenler bunlar
#local etki alanından global etki alanını değiştirmek
x = []
def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi")
eleman_ekle(1)
eleman_ekle("ali")
print(x)

