#elimde bir liste var ve bu listeyi öyle bir yerden ayıracağım ki ayırdığım yerden ikiye bölünen tarafların toplamı eşit olacak

def separateList(liste):
    for i in range(len(liste)):
        if sum(liste[:i]) == sum(liste[i:]):
            return liste[i-1]
        else:
            continue
    return -1

liste = [6,1,2,3]

x = separateList(liste)

print(f"You should separate the list after {x}")