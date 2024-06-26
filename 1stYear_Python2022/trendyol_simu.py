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
shopvalue = 0
shopitem = ""
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

def control_stock2(dict, shopvalue, shopitem,shopping_stock_dict):
    if shopvalue <= dict[shopitem]:
        ilk_miktar = shopping_stock_dict[shopitem]
        shopping_stock_dict[shopitem] = ilk_miktar - shopvalue
        return "Alışveriş için stok mevcuttur." and shopping_stock_dict and shopvalue
    else:
        while shopvalue > dict[shopitem]:
            karar = input(f"Ürün stokta almak istediğiniz {shopvalue} kg mevcut değildir. Stoktaki {dict[shopitem]} kg kadarını almak ister misiniz?")
            if karar == "evet":
                shopvalue = dict[shopitem]
                shopping_stock_dict[shopitem] = 0
                return shopvalue and shopping_stock_dict
            else:
                break
def sepet_hazirla(shopvalue, shopitem, shopping_stock_dict):
    alisveris_sepeti = []
    alisveris_sepeti.append([shopitem, shopvalue])
    return "Alışveriş sepetiniz oluşturuldu."


def odeme_yap(dict, shopitem, shopvalue):
            price1 = shopping_prices_dict[shopitem]
            price_last = int(price1 * shopvalue)
            return price_last
def en_cok_satilan(shopvalue_list, shop_list_main):
    max_value = max(shopvalue_list)
    liste = []
    for j in shop_list_main:
        if j[1] == max_value:
            liste.append(j)
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
        for i in range(len(shopitem_list)):
            if k == 'elma':
                net_kar_elma = net_kar[i]*shopvalue
            elif k == 'limon':
                net_kar_limon = net_kar[i]*shopvalue
            elif k == 'ayva':
                net_kar_ayva = net_kar[i]*shopvalue
    net_kar_ana = net_kar_elma + net_kar_ayva + net_kar_limon
    return net_kar_ana
for i in range(alisveris_sayisi):
    shopitem = input("Satın almak istediğiniz ürünü giriniz: ")
    shopitem = control_stock1(shopping_stock_dict, shopitem)
    shopitem_list.append(shopitem)
    shopvalue = int(input("Satın almak istediğiniz kilogram miktarını giriniz: "))
    print(control_stock2(shopping_stock_dict, shopvalue, shopitem,shopping_stock_dict))
    shopvalue_list.append(shopvalue)
    shop_list_main.append([shopitem, shopvalue])

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