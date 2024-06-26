def calculate_average():
    with open("students.txt", "r+") as f:
        liste1 = []
        liste2 = []
        liste3 = []
        dict_ = {}
        for i in f:
            key = i.strip("\n").split("\t")[0]
            value = i.strip("\n").split("\t")[1]
            if key == "Ali":
                liste1.append(int(value))
                average1 = sum(liste1) / len(liste1)
                dict_[key] = average1

            elif key == "Veli":
                liste2.append(int(value))
                average2 = sum(liste2) / len(liste2)
                dict_[key] = average2

            elif key == "Ahmet":
                liste3.append(int(value))
                average3 = sum(liste3) / len(liste3)
                dict_[key] = average3

        for name,not_ort in dict_.items():
            print(name,not_ort,sep="\t")
def find_min():
    with open("students.txt", "r+") as f:
        liste = []
        dict = {}
        for i in f:
            key = i.strip("\n").split("\t")[0]
            value = i.strip("\n").split("\t")[1]
            value = int(value)
            i = i.strip("\n")
            liste += [i.split("\t")]
            dict[value] = key
            mini = min(dict.keys())
        print(dict[mini],mini,sep="\t")
calculate_average()
