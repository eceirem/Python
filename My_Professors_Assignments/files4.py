#bir dosyaya 11 e kadar olan sayıların üslerini kadar yazmak

f = open("text2.txt", "w")

for i in range(11):
    num = i * i
    f.write(str(num)+"\n")