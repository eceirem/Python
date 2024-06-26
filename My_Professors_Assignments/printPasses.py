# argüman olarak dictionary (öğrenci : not) alan ve aldığı derslerden geçen öğrencilerin isimlerini listeye atıp döndüren fonk yazınız
# not: ders sayıları aynı olmayabilir
#{"Ece": ["5/5", "3/3", "2/2"],"Ege": ["3/8", "1/2"]}
def Is_Pass(dic):
    names = []
    counter = 0
    for name,grades in dic.items():
        for i in range(len(grades)):
            grade = grades[i].split("/")
            if grade[0] != grade[1]:
                break
            else:
                counter += 1
        if counter == len(grades):
            names.append(name)
        counter = 0
                

    return names

dic = {"Ece": ["5/5", "3/3", "2/2"],"Doğukan": ["8/8", "2/2"]}
print(Is_Pass(dic))
