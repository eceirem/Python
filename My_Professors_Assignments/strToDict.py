# elimde bir str listesi var ["dog = bark", "cat = meow", "horse = neigh"] gibi. Bunu dict yap
def strToDict(lst):
    dicti = {}

    for i in lst:
        k ,v = i.split("=")
        dicti[k] = v

    return dicti

liste = ["dog = bark", "cat = meow", "horse = neigh"]

print(strToDict(liste))