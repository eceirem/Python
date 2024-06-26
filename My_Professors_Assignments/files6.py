#dosyayı okusun ve luke ile ilişkili dict e çevirsin
f = open("file.txt","r")

luke_dict = {}
family = f.readlines()

for i in family:
    lst = i.split()
    luke_dict[lst[0]] = lst[1]

print(luke_dict)

#for names in f:
#    liste = names.split()
#    luke_dict[liste[0]] = liste[1]




name = input()

for names,relations in luke_dict.items():
    if name == names:
        print(relations)