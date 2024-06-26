def bubbleSort(liste):
    print("Orjinal Liste: ",liste)
    listeCopy = liste.copy()
    counter1 = 0
    temp = 0
    #listenin sonuna kadar gidiyoruz.
    while(counter1 != len(liste)):
        counter1 += 1
        counter2 = 0
        for index in range(0,len(listeCopy)-1):
            if(listeCopy[index] > listeCopy[index+1]):
                counter2 += 1
                temp = listeCopy[index]
                listeCopy[index] = listeCopy[index+1]
                listeCopy[index+1] = temp
                print(f"Adım {counter1}.{counter2}: {listeCopy}")
    
    return listeCopy

text = input("Liste elemanlarını boşluklu bir şekilde girin: ")
text = text.split(" ")
liste = []
for num in text:
    liste.append(int(num))

bubbleSort(liste)