#dosyadak isimleri aynı formatta sırayla  yeni bir dosyaya yazsın
f = open("text1.txt", "r")
f2 = open("text2.txt", "w")
i = f.read()
lst = i.strip("\n").split()
lst.sort()
print(lst)

rowCount = 0
colCount = 0
itemCount = 0
for i in lst:
    
    if colCount < 2 and itemCount != len(lst) - 1:
        f2.write(i+"\t")
        colCount += 1
        itemCount += 1
    elif itemCount == len(lst):
        f2.write(i)
    else:
        f2.write(i)
        itemCount += 1
        rowCount += 1
        colCount = 0
        if rowCount < (len(lst) / 3):
            f2.write("\n")
