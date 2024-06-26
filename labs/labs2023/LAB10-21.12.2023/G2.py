def mergeSort(myList):

    if(len(myList)>1):
        middle = len(myList)//2
        print(f"Bölünmüş Liste: {myList}")
        left_list = myList[:middle]
        right_list= myList[middle:]

        mergeSort(left_list)
        mergeSort(right_list)

        indexL = indexR = indexM = 0
        
        while indexL < len(left_list) and indexR < len(right_list):
            if( left_list[indexL] <= right_list[indexR]):
                myList[indexM] = left_list[indexL]
                indexL += 1
            else:
                myList[indexM] = right_list[indexR]
                indexR += 1

            indexM += 1
        
        while indexR < len(right_list):
            myList[indexM] = right_list[indexR]
            indexR += 1
            indexM += 1

        while indexL < len(left_list):
            myList[indexM] = left_list[indexL]
            indexL += 1
            indexM += 1

        print(f"Birleştirilmiş Liste: {myList}")


text = input("Liste elemanlarını boşluklu bir şekilde girin: ")
text = text.split(" ")
liste = []
for num in text:
    liste.append(int(num))

print("Orjinal Liste: ",liste)
mergeSort(liste)
print("Sıralanmış Liste: ", liste)