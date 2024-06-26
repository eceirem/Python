#iki listeyi argüman alan ve bu 2 listedeki aynı index de oturan sayıların bölümünün round edilerek yeni bir listeyi döndüren fonk.
#liste uzunlukları eşit olmayabilir. min uzunluğu al
def rational(list1, list2):
    division_error = 0
    if len(list1) == len(list2): #liste uzunlukları eşitse aynı index de oturanları böl
        if division_error in list2:
            print("contains 0 in the denominator, so this operation cannot be performed.")
            
        else:
            return [round(list1[i]/list2[i]) for i in range(len(list1))]
   
    else: 
        #liste uzunlukları eşit değilse birbirine eşitle ve bu fonksiyonu bir daha çağır.
        if len(list2) < len(list1):   
            while len(list2) != len(list1):
                list2.append(1)

        else:
            while len(list2) != len(list1):
                list2.pop()

        return rational(list1,list2)


list1 = [1,2,3,4]
list2 = [0,2,3]

list3 = rational(list1,list2)
if list3:
    print(list3)