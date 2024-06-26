#luke ile ilikşkisini dödnüren fonksiyonu yazınız.
dict = {"Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother_in_law",
        "R2D2": "droid"}

def relationLuke(name):
    for names, relation in dict.items():
        if name == names:
            return relation

name = input()
print(relationLuke(name))