#öğrenci dictionarysindeki isimleri sıralı şekilde listeye alan bir fonksiyon yazınız
def get_sorted_names(dicti):
    names = []
    for name in dicti.values():
        names.append(name)

    names.sort()
    return names

dictionary = {"student1": "Zeynep",
              "student2" : "Can",
              "student3": "Ali"}

print(get_sorted_names(dictionary))