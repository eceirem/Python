#dosyadaki satılarlarda olan sayıları toplayıp toplamlarını yeni bir dosyaya yazmak
f = open("file.txt","r")
f2 = open("text2.txt", "w")

for numbers in f:
    print(numbers)
    liste = numbers.split()
    total = 0
    for j in liste:
        total += int(j)
    f2.write(str(total)+"\n")
    