#argüman alınan listedeki değerlerin üzerine index değerlerini toplayıp return eden bir fonksiyon yazınız. str ve int kontrol ediniz.

def add_indexes(liste):
    r_liste = []
    for i in range(len(liste)):
        if type(liste[i]) == int:
            r_liste.append(liste[i] + i)

        else:
            r_liste.append(liste[i])

    return r_liste

liste = ["abc", 4,5,"ece"]

print(add_indexes(liste))