import os
def find_data(text):
    try:
        f = open(text + ".txt","r")
        row_c = 0 #satır sayısını sayacak
        word_c = 0 #kelime sayısını sayacak
        char_c = 0 #karakter sayısını sayacak

        for line in f:
            row_c += 1
            
            liste = line.split()
            word_c += len(liste) #  o satırdaki elemanları boşluklardan bölerek, tek tek listeye dönüştürür 
            char_c += len(line) #  o satırdaki tüm karakterleri str olarak tutar içinde

        f.close()
        return (row_c,word_c,char_c)
    except:
        return "File not found!!"

print(find_data("file"))