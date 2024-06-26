# istenilen uzunluk kadar o listeyi tamamlıyoruz ya da kısaltıyoruz. tamamlayacağımız değeri, uzunluğu ve listeyi argüman alacak fonksiyon

def fillOrDelete(liste,n,ch):
    if len(liste) > n:
        while len(liste) != n:
            liste.pop()   
    else:  
        while len(liste) != n:
            liste.append(ch)
    return liste
    
liste = [1,2,3,4,5,6]

print(fillOrDelete(liste,5,"*"))