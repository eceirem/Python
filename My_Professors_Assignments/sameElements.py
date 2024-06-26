#iki listdeki ortak elemanları döndüren fonksiyonu yazınız. 
#2. yol alternatifi için de set leri düşünebiliriz.

def same_elements(liste1, liste2):
    liste_ortaklar = []
    # 1. yol
    # for i in liste1:
    #     if i in liste2 and i not in liste_ortaklar:
    #         liste_ortaklar.append(i)
    liste_ortaklar = list((set(liste1) & set(liste2)))

    return liste_ortaklar


liste1 = [1,2,3,4,5]
liste2 = [2,3,4,7]

print(same_elements(liste1, liste2))