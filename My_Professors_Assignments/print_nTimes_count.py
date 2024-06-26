# listede n veya >n kez geçen elemanları return eden fonksiyonu yazacağız

def print_n(liste, n):
    basilacaklar = []
    for i in liste:
        if liste.count(i) >= n and i not in basilacaklar:
            basilacaklar.append(i)

    return basilacaklar

liste = [1,1,12,2,1,3,4,2]

print(print_n(liste,2))