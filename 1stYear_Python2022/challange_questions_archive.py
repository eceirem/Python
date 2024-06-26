#a ları b ye dönüştür
def chpass(x):
    chd=''
    for i in x:
        if i == 'a':
            chd += 'b'
        else:
            chd += i

    print(chd)
    return
chpass(input("Bir veri giriniz: "))
#string içerisindeki sayının tek ve çiftlerini ayrı ayrı guplndırarak yazdır.
veri = input()
even=''
odd=''
for i in veri:
    if int(i)%2==0:
        even += i
    else:
        odd += i
print(even,odd)
#string içerisindeki tüm veriler eşitse true bazsın 1111=true aaab=false
veri = input()
b=0
for i in veri:
    for l in veri:
        if i != l:
            b +=1
if b >= 1:
    print("false")
else:
    print("true")

#0-100 pisagor sağlayan sayılar üçlüsü programı
enter_number = int(input("sayı giriniz..:"))
for i in range(1, enter_number):

    for k in range(i, enter_number + 1):

        for m in range(k, enter_number + 1):
            if i ** 2 + k ** 2 == m ** 2:
                print(i, k, m, sep="---")

#3 öğrenci ve bu öğrencilerin 3 notunu isteyen programı yazınız
for l in range(3):
    st = input("öğrenci giriniz: ")
    c=0
    for i in range(3):
        c +=1
        if c ==1:
            n1 = int(input("bir not giriniz: "))
        elif c ==2:
            n2 = int(input("bir not giriniz: "))
        elif c ==3:
            n3 = int(input("bir not giriniz: "))
    total = n1/4 + n2/4 + n3/2

    print(f"{st} : {total}")

# 3 input al a,b,c a ile b arasındaki sayılardan farkı c olan asal sayıları bas.
    def asal(sayi):
        if sayi < 2:
            return False
        isprime = True
        for i in range(2, sayi):
            if sayi % i == 0:
                isprime = False
                break
        return isprime


    a = int(input('[a,b] aralığında farkı c olan ilk asal çiftini bulmak için: \n a\'yı girin:'))
    b = int(input('b\'yı girin:'))
    c = int(input('c\'yı girin:'))

    for i in range(a, b - c + 1):
        if asal(i) and asal(i + c):
            print(i, i + c)
            break


#ebob-ekok
def ebob_bulma(sayı1 , sayı2):
    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2):
        if not sayı1 % i and not sayı2 % i :
            ebob = i
        i += 1
    return ebob
def ekok_bulma(sayı1, sayı2):
    return sayı1 * sayı2 / ebob_bulma(sayı1,sayı2)
sayı1 = int(input("Sayı1: "))
sayı2 = int(input("Sayı2: "))
print("Ebob: ",ebob_bulma(sayı1,sayı2))
print("Ekok: ",ekok_bulma(sayı1,sayı2))
#zar tahmin oyunu wtih doğuşkin
import random

def zar_atma():
    zar=random.randrange(1,7)
    print(f"Gelen zar: {zar}")
    return zar
guess = 0
for i in range(2):
    plyr = input("Bir oyuncu adı giriniz: ")
    guess = int(input("Tahmin giriniz: "))
    print(f"{plyr},{guess:>5}")
    if zar_atma() == guess:
        print(f"{plyr} win")
    else:
        print(f"{plyr} lose")
#metinler arasındaki farklı olanı bas(indis+str)
metin = "abcdef"
metin2 = "bacefg"
df = ''
for i in range(len(metin)):
    for l in range(len(metin2)):
        if metin[i]==metin2[l]:
            df += metin[i]
print(df)


for i in range(len(metin)):
    if metin[i] == metin2[i]:
        print(metin[i])

#iki liste arasındaki ortak sayıları bulma -doğuşkin
import random
rakamlar1 = []
rakamlar2 = []
for i in range(0,50):
    rakamlar1.append(random.randrange(0,1000))
    rakamlar2.append(random.randrange(0,1000))
rakamlar1.sort()
rakamlar2.sort()
print(rakamlar1,"\n",rakamlar2)
for k in rakamlar1:
    for l in rakamlar2:
        if k == l:
            print(k)

#faiz ve zam hesaplama right align kullanarak
bill = 37.45
tax = 6.25
bill_total = ((37.45*6.25)/100)+(37.45)
print(f"{bill_total:.6f}")

#zar atıp sapma miktarlarını mutlak değer kullanarak gösterme
import random
frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0
counter = 0
for roll in range(int(input("Kaç kere döngüde dönmesini istersiniz : "))):
    counter += 1
    face = random.randrange(1, 7)
    if face == 1:
        frequency1 += 1
    elif face == 2:
        frequency2 += 1
    elif face == 3:
        frequency3 += 1
    elif face == 4:
        frequency4 += 1
    elif face == 5:
        frequency5 += 1
    elif face == 6:
        frequency6 += 1
deviation_amount = abs(int((counter / 6)) - frequency1)
deviation_amount2 = abs(int((counter/6)) - frequency2)
deviation_amount3 = abs(int((counter / 6)) - frequency3)
deviation_amount4 = abs(int((counter/6)) - frequency4)
deviation_amount5 = abs(int((counter/6)) - frequency5)
deviation_amount6 = abs(int((counter/6)) - frequency6)

print(f'Face{"Frequency":>13}{"Deviation Amount":>20}{"Deviation Amount Percent":>27}')
print(f'{1:>4}{frequency1:>13}{deviation_amount:>20}{(deviation_amount)/(counter/6):>27}')
print(f'{2:>4}{frequency1:>13}{deviation_amount2:>20}{(deviation_amount2)/(counter/6):>27}')
print(f'{3:>4}{frequency1:>13}{deviation_amount3:>20}{(deviation_amount3)/(counter/6):>27}')
print(f'{4:>4}{frequency1:>13}{deviation_amount4:>20}{(deviation_amount4)/(counter/6):>27}')
print(f'{5:>4}{frequency1:>13}{deviation_amount5:>20}{(deviation_amount5)/(counter/6):>27}')
print(f'{6:>4}{frequency1:>13}{deviation_amount6:>20}{(deviation_amount6)/(counter/6):>27}')

#zar atma oyunu kitaptaki 4.5 de
import random
def roll_dice():
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    return (die1,die2)
def display_dice(dice):
    die1, die2 = dice
    print(f"Player rolled {die1} + {die2} = {sum(dice)}")
die_values = roll_dice()
display_dice(die_values)
sum_of_dice = sum(die_values)
if sum_of_dice in (7,11):
    game_status = "WON"
elif sum_of_dice in (2,3,12):
    game_status = "LOST"
else:
    game_status = "CONTINUE"
    my_point = sum_of_dice
    print("Point is", my_point)
while game_status == "CONTINUE":
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)
    if sum_of_dice == my_point:
        game_status = "WON"
    elif sum_of_dice == 7:
        game_status = "LOST"
if game_status == "WON":
    print("player wins")
else:
    print("player loses")
#listedeki tek ve çiftleri ayrı ayrı toplayıp yeni bir listeye atıp basan kod (fonk. kullanarak)
def sum_even_odd(liste1):
    even = 0
    odd = 0
    for i in liste1:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    return [even,odd]
#alternatif bir yol daha
def sum_eve_odd(list1):
    return [sum(x for x in list1 if x % 2),
            sum(x for x in list1 if not x % 2)]
liste1 = [1,2,3,4,5,6]
print(sum_eve_odd(liste1))


liste1=[1,2,3,4,5]
print(sum_even_odd(liste1))
#bir listenin içinde iki tane daha liste olsun ve bu iki listenin içinde ikişer tane daha değer olsun
#1. değer pay, 2. değer paydadır.Bu kesirlerin toplamının Tam sayı değerini ve en yakın tam sayıya yuvarlanmasını bastır.
ana_liste = [[5,6],[5,3]]
sum1 = round(ana_liste[0][0]/ana_liste[0][1]+ana_liste[1][0]/ana_liste[1][1])
sum2 = int(ana_liste[1][0]/ana_liste[1][1]+ana_liste[1][0]/ana_liste[1][1])
print("İki kesrin yuvarlanmış versiyonları toplamı: ", sum1)
print("iki kesrin toplamının tam sayı kısmı: ", sum2)

#argüman olarak 2 liste al ve listedeki ortak elemanları yeni bir listeye ata.
liste1 = [1,2,3,45,67]
liste2 = [1,4,56,67]
ortaklar = []
for i in liste1:
    for j in liste2:
        if i == j:
            ortaklar+=[i]
print(ortaklar)
#alternatif diğer yol
def cammon_list(lst1,lst2):
    result = []
    for i in lst1:
        if i not in result and i in lst2:
            result += [i]
    return result
lst1=[1,2,3,45,67]
lst2=[1,4,56,67]
print(cammon_list(lst1,lst2))
#argüman olarak 3 liste alsın ve bu eleman sayısı aynı olanları bir liste içine atasın. Olmayan eleman sayısı için * bassın
l1 = [1,2,3]
l2 = [4,5]
l3 = [6]
def height(l1,l2,l3):
    return max(len(l1),len(l2),len(l3))
def extend_list(lst,num):
    while len(lst) < num:
        lst.append('*')
    return lst
def create_list(l1,l2,l3):
    result = []
    num = height(l1,l2,l3)
    l1 = extend_list(l1,num)
    l2 = extend_list(l2,num)
    l3 = extend_list(l3,num)
    for i in range(len(l1)):
        result.append([l1[i],l2[i],l3[i]])
    return result
num = height(l1,l2,l3)
print(create_list(l1,l2,l3))

#Öğrencilerin notlarını dict. de verilsin.Ayrı ayrı sınıf ort. ve kişilerin sınav ort. hesapla,
grade_book = {
    'Efe': [92,85,100],
    'Ege': [83,95,79],
    'Ece': [91,89,82],
    'Nur': [97,91,92]
}
total1 = 0
total2 = 0
total3 = 0
for i in grade_book:
    total1 += grade_book[i][0]
    total2 += grade_book[i][1]
    total3 += grade_book[i][2]
for names, grades in grade_book.items():
    total = sum(grades)
    print(f'Average for {names} is {total/3:.2f}')
print(f'First exam average is {total1/4}')
print(f'Second exam average is {total2/4}')
print(f'Third exam average is {total3/4}')

#argüman olarak bir liste ve sayı alsın, sayıdan liste içindeki o sayıdan fazlyasa silsin. 2'den fazla geçen elemanları en fazla sayı kere göster.
def kac_kere_gecti(liste,num):
    new_list = []
    for i in liste:
        if i not in new_list:
            new_list.append(i)
        elif new_list.count(i) < num:
            new_list.append(i)
        elif new_list.count(i) == num:
            new_list.count(i)
        elif new_list.count(i) > num:
            continue
    return new_list
liste = [1, 2, 2, 2, 3, 1, 1, 4, 2, 5, 6, 7]
num = 2
print(kac_kere_gecti(liste,num))

#dictionary içinde value lara göre sırala ve yanına key değerlerini ata
dictionary = {'Ece': 2, 'Nur': 1, 'Doğu': 7}
reverseDict = {}

c = []

for key, value in dictionary.items():
    reverseDict[value] = key

for i in sorted(reverseDict.keys()):
    print(i)
    c.append((reverseDict[i], i))

print(c)
#akrabalık ilişkilerini bulan bir fonksiyon yazın
dict = { 'Önder': 'father',
         'Çiğdem': 'mother',
         'Yağmur': 'cousin',
         'Zafer': 'cousin',
         'Nilgün': 'aunt'}
name = input()
def relation_ece(name,dict):
    return 'Ece! I am your ' + dict[name] + '.'
print(relation_ece(name,dict))
#bir alışveriş sitesi hazırla.
'''1. keylere göre alfabetik sırala
2.Stokta var mı yok mu?
3.Varsa almak istediğim kadar var mı?
4. En çok hangisinden sattım hesapla
5. En çok elde ettiğim kârı hesapla
6. Her alışverişte stoktan azalt'''
shopping_stock_dict = {'elma': 12, 'limon': 15, 'ayva': 8}
shopping_prices_dict = {'elma': 10, 'limon': 12, 'ayva': 15}
market_shops = {'elma': 5, 'limon': 4,'ayva': 8}
toplam_odeme = 0
bahsis = 10
ana_alisveris_sepeti = []
alisveris_sayisi = int(input("Kaç ürün alacaksınız?:"))
shopvalue_list = []
shopitem_list = []
shop_list_main = []
shop_main_dict = {}

def control_stock1(dict, shopitem):
    mevcut_mu = False
    if shopitem in dict:

        print("Almak istediğiniz ürün mevcuttur.")
        mevcut_mu = True
    else:
        while mevcut_mu == False:
            print("Almak istediğiniz ürün mevcut değildir.")
            shopitem = input("Yeniden ürün giriniz.")
            if shopitem in shopping_stock_dict.keys():
                mevcut_mu = True
    return shopitem

def control_stock2(dict, shopvalue, shopitem):
    if shopvalue <= dict[shopitem]:
        return "Alışveriş için stok mevcuttur."
    else:
        while shopvalue > dict[shopitem]:
            shopvalue = input(f"Ürün stokta almak istediğiniz {shopvalue} kg mevcut değildir. Stoktaki {dict[shopitem]} kadarını almak ister misiniz?")

    return shopvalue

def sepet_hazirla(shopvalue, shopitem, shopping_stock_dict):
    alisveris_sepeti = []
    alisveris_sepeti.append([shopitem, shopvalue])
    ilk_miktar = shopping_stock_dict[shopitem]
    shopping_stock_dict[shopitem] = ilk_miktar - shopvalue
    print("Alışveriş sepetiniz oluşturuldu.")
    return shopping_stock_dict

def odeme_yap(dict, shopitem, shopvalue):
            price1 = shopping_prices_dict[shopitem]
            price_last = int(price1 * shopvalue)
            return price_last
def en_cok_satilan(shopvalue_list, shop_list_main):
    max_value = max(shopvalue_list)
    liste = []
    for j in range(len(shop_list_main)):
        for l in shop_list_main:
            for e in l:
                if not liste:
                    if e == max_value:
                        liste.append(l)
                else:
                    continue
    return (f'En çok satılan ürün ve satılma miktarı: {liste}')
def kar_hesaplama(market_shops,shopping_prices_dict,shopvalue,shopitem_list):
    net_kar =[]
    v1 = []
    v2 = []
    for i in range(len(shopping_prices_dict)):
        v1= list(shopping_prices_dict.values())
        v2= list(market_shops.values())
        net_kar.append(v1[i]-v2[i])
    net_kar_elma = 0
    net_kar_limon = 0
    net_kar_ayva = 0
    net_kar_ana = 0
    for k in shopitem_list:
        if k == 'elma':
            net_kar_elma = net_kar[0]*shopvalue
        elif k == 'limon':
            net_kar_limon  = net_kar[1]*shopvalue
        elif k == 'ayva':
            net_kar_ayva = net_kar[2]*shopvalue
    net_kar_ana = net_kar_elma + net_kar_ayva + net_kar_limon
    return net_kar_ana
for i in range(alisveris_sayisi):
    shopitem = input("Satın almak istediğiniz ürünü giriniz: ")
    shopitem = control_stock1(shopping_stock_dict, shopitem)
    shopitem_list.append(shopitem)
    shopvalue = int(input("Satın almak istediğiniz kilogram miktarını giriniz: "))
    shopvalue_list.append(shopvalue)
    shop_list_main.append([shopitem, shopvalue])
    print(control_stock2(shopping_stock_dict, shopvalue, shopitem))

    sepet_hazirla(shopvalue, shopitem, shopping_stock_dict)
    #print(f"stoğun son hâli böyledir: {shopping_stock_dict} idir.")

    odeme_yap(shopping_prices_dict, shopitem, shopvalue)
    toplam_odeme += odeme_yap(shopping_prices_dict, shopitem, shopvalue)
    print(f"Ödeme miktarı toplam: {toplam_odeme} ")
    ana_alisveris_sepeti = [shopitem, toplam_odeme]

print(en_cok_satilan(shopvalue_list, shop_list_main))
print(f'Stoğun son hâli: {shopping_stock_dict}')

odeme_parasi = int(input("Ödeme yapmak için para yükleyiniz: "))

while odeme_parasi <= toplam_odeme:
    if odeme_parasi < toplam_odeme:
        print("Ödeme tutarı yetersizdir. Daha fazla para yükleyiniz.")
        odeme_parasi = int(input("Ödeme yapmak için para yükleyiniz: "))
    elif odeme_parasi == toplam_odeme:
        print("Ödemeniz alındı. Sipariş birazdan teslime çıkacaktır.")
        break
if odeme_parasi > toplam_odeme:
    bahsis = (odeme_parasi - toplam_odeme)
    if bahsis <= 10:
        print(f"Bahşiş için teşekkür ederiz. İşleminize öncelik verilecektir. Bahşiş miktarı {bahsis} liradır.")
    else:
        bahsis = 10
        sistem_parasi = (odeme_parasi - toplam_odeme - bahsis)
        print(
            f"Bahşiş miktarı {bahsis} olarak sınırlandırılmıştır. Ek paranız {sistem_parasi} liradır.\n Bizi tercih ettiğiniz için teşekkür eder, iyi günler dileriz.")

print(f"Marketin elde ettiği kâr miktarı= {kar_hesaplama(market_shops,shopping_prices_dict,shopvalue,shopitem_list)}")

#argüman olarak dict alan ve en yaşlı kişi ile adını basan program
dict = {'ece': 18, 'efe': 19, 'ege': 20, 'doğu': 22}
def oldest(dict):
    the_oldest = []
    en_yasli = 0
    en_yasli_kisi = ''
    the_oldest = dict.values()
    en_yasli = max(the_oldest)
    for i in dict:
        dict[i] = en_yasli
        en_yasli_kisi = i
    return [en_yasli_kisi,en_yasli]
print(oldest(dict))
#Argümanolarak txt ve character al içinde kaç kere olduğunu dict döndür.
txt = input("Cümle giriniz:")
ch = input("karakter giriniz:")
def find_occurences(txt,ch):
    keys = []
    txt = txt.split()
    a = {}
    for i in txt:
        keys.extend(i)
        for j in i:
            if j == ch:
                a[i] = keys.count(ch)
            if ch not in i:
                a[i] = 0
        keys.clear()
    return a

print(find_occurences(txt,ch))
#listee al dict döndür
def str_to_dict(liste):
    sozluk = {}
    for i in liste:
        k , v = i.split('=')
        sozluk[k]=v
    return sozluk
liste = [ "1=one","2=two"]
print(str_to_dict(liste))
#iki ayrı dictde aynı olan key ve value ları liste içi dict olarak döndür. 2 alternatif yol var.
dict1 = {'a': 5, 'b': 13, 'c': 7}
dict2 = {'b': 5, 'c': 8, 'd': 9, 'e': 71}
def overloop_dict(dict1,dict2):
    a = {k:v for k,v in dict1.items() if k in dict2.keys()}
    b = {k:v for k,v in dict2.items() if k in dict1.keys()}
    return [a,b]
def overloop_dict2(dict1,dict2):
    key1_list = list(dict1.keys())
    key2_list = list(dict2.keys())
    sozluk1 = {}
    sozluk2 = {}
    for i in key1_list:
        if i in key2_list:
            sozluk1[i] = dict1[i]
            sozluk2[i] = dict2[i]
    return [sozluk1,sozluk2]
print(overloop_dict(dict1,dict2))
print(overloop_dict2(dict1,dict2))
#argüman olarak harf listesi al ve ord değerlerini value olarak döndür dict de.
liste = ['a','b','t','k','f']
def f(liste):
    a = {k:ord(k) for k in liste}
    return a
print(f(liste))
def g(liste):
    dict = {}
    for i in liste:
        dict[i] = ord(i)
    return dict
print(g(liste))
#dict al ve liste yap. Sıralamayı keylere göre yap.
dict = {'b':1, 'a':2}
def dict_to_list(dict):
    k = []
    k = list(sorted(dict.keys()))
    b = []
    for i in k:
        b.append([i,dict[i]])
    return b
print(dict_to_list(dict))
#dict al ve liste yap. Sıralamayı keylere göre yap. Valuelara koşul koy ve döndür
dict = {'b':1, 'a':2,'A':94}
def dict_to_list(dict):
    k = []
    k = list(sorted(dict.keys()))
    b = []
    for i in k:
        if ord(i) > 97:
            b.append([i,dict[i]])
    return b
print(dict_to_list(dict))

#liste  içerisinde çarpımları n olan sayıların listesini çevir, en küçük min olsun. sırayla bas.
liste = [3, 2, 3, 4, 5, 13, 15, 39, 1]
number = 39
liste.sort()
for i in range(0,len(liste),1):
    for j in range(i+1, len(liste),1):
        if liste[i]*liste[j] == number:
            print([liste[i],liste[j]])
    break
#ortak_strlerde silme
str1 = 'abcde'
str2 = 'fcab'
son_str1 = []
son_str2 = []
ortaklar = []
basilacak = []
sayac = 0
for i in str1:
    if i in str2:
        ortaklar.append(i)
for i in str1:
    if i not in str2:
        son_str1.append(i)
for i in str2:
    if i not in str1:
        son_str2.append(i)
basilacak += son_str1 + son_str2 + ortaklar
sayac = (len(str1) + len(str2) - len(basilacak))
print(f"strdeki son hâli {basilacak}")
print(f"strdeki ortaklar{ortaklar}")
print(f"sildiğim tekrar eden harf sayısı{sayac}")
#harf olarak girilen str ni sayılara atanması
sozluk = {}
counter = 0
liste = ['a','b','c','a']
liste2 = []
for i in liste:
    if i not in sozluk.keys():
        sozluk[i] = counter
        counter += 1

for i in liste:
    liste2.append(sozluk[i])
print(liste2)
#kriptolojiye giriş sorusu, str ler arası çok ortak olanı bassın
str1 = input()
str2 = 'abcghi'
str3 = 'abcdgl'
ortaklar1_2 = []
ortaklar1_3 = []
for i in str1:
    if i in str2:
        ortaklar1_2.append(i)
for i in str1:
    if i in str3:
        ortaklar1_3.append(i)

if len(ortaklar1_2) < len(ortaklar1_3):
    print(str3)
elif len(ortaklar1_2) > len(ortaklar1_3):
    print(str2)
else:
    print(str1)
#liste olsun öyle bir yerden böl ki iki tarafın toplamalrı eşit olsun
liste = [1,2,3,4,2,8]
toplam = 0
sayac = sum(liste)/2
for i in range(len(liste)):
    if sum(liste[:i]) == sum(liste[i:]):
        print(liste[:i],liste[i:])


class Rasyonel():
    def __init__(self,num,den):
        self.num = num
        self.den = den
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    def __add__(self,other):
        top = (self.num*other.den + self.den*other.num)
        bottom = self.den*other.den
        return Rasyonel(top,bottom)
a = Rasyonel(1,4)
b = Rasyonel(3,4)
c = a+b
print(c)

class People():
    instances = []
    def __init__(self,isim,soyisim,yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.instances.append([isim,soyisim,yas])
    def sort_people(value):
        ordered = []
        for i in People.instances:
            if value == "name":

                ordered.append(i[0])
            elif value == "surname":
                ordered.append(i[1])
            elif value == "age":
                ordered.append(i[2])
        ordered = sorted(ordered)
        for i in ordered:
            print(i)

person1 = People("Ece","Şişer",19)
person2 = People("Doğukan","Filiz",22)
value = input()
People.sort_people(value)

class Person():
    def __init__(self,name,likes,hates):
        self.name = name
        self.likes = likes
        self.hates = hates
    def taste(self,yemek):
        if yemek in self.likes:
            return print(f"{self.name} likes {yemek}.")
        elif yemek in self.hates:
            return print(f"{self.name} hates {yemek}.")
        else:
            return print(f"{yemek} is not defined.")

    def mutual_likes(self, other, yemek1):
        if yemek1 in self.likes and other.likes:
            return print(f"{self.name} and {other.name} like {yemek1}.")

    def mutual_hates(self, other, yemek2):
        if yemek2 in self.hates and other.hates:
            return print(f"{self.name} and {other.name} hate {yemek2}.")
person1 = Person("Doğu",["çikolata","cips"],["kereviz","bamya","kokoreç"])
person2 = Person("Ece",["dolma","mantı","çikolata"],["kokoreç"])
Person.mutual_likes(person1,person2,"çikolata")

class Banka():
    musteri_sayisi = 0
    def __init__(self,id,a,b,c=0):
        self.id = id
        self.yatirilan_para = a
        self.cekilen_para = b
        self.bakiye = c
        Banka.musteri_sayisi += 1
    def para_yatirma(self):
        print("yatırılacak miktar:" + str(self.yatirilan_para))
        self.bakiye = self.bakiye + self.yatirilan_para
        return print(str(self.bakiye) + " tl toplam bakiye")
    def para_cekme(self):
        if self.cekilen_para <= self.bakiye:
            self.bakiye -= self.cekilen_para
            return print(str(self.cekilen_para) + " tl toplam çektiniz.")
        else:
            return print("Yetersiz bakiye.")
    def bakiye_gorme(self):
        return print("Son durumda bankadaki paranız: " + str(self.bakiye) + " tl")
    @staticmethod
    def musteri_sayisi_goster():
        return print(f"Bankayı kullanan toplam kişi sayısı: {Banka.musteri_sayisi}")
id = input()
a = int(input())
b = int(input())
p1 = Banka(id,a,b)
Banka.para_yatirma(p1)
Banka.para_cekme(p1)
Banka.bakiye_gorme(p1)
id = input()
a = int(input())
b = int(input())
p2 = Banka(id,a,b)
Banka.para_yatirma(p2)
Banka.para_cekme(p2)
Banka.bakiye_gorme(p2)
Banka.musteri_sayisi_goster()