def input_grades():
    str1 = input()
    while str1 != "X":
        with open("students","a") as f:
            f.write(str1)
            f.write("\n")
            str1 = input()
def calculate_average():
    with open("students","r+") as g:
        dict_ = {}
        liste = []
        sum = 0
        for i in g:
            liste = i.strip("\n").split("\t")
            key = liste[0]
            value = liste[1]
            dict_[key] = value
        for i in dict_.values():
            i = int(i)
            sum += i
            average = sum/len(dict_.values())
        print(f'{average:.2f}')
def find_max():
    with open("students", "r+") as g:
        dict_ = {}
        liste = []
        sayilar = []
        a = 0
        for i in g:
            liste = i.strip("\n").split("\t")
            key = liste[1]
            value = liste[0]
            dict_[key] = value
        for i in dict_.values():
            i = int(i)
            sayilar.append(i)
            a = max(sayilar)
            b = str(a)
        print(dict_[b],a,sep="\t")
input_grades()
calculate_average()
find_max()