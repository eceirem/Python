def place_student(input_list):
    sitNum = 0
    deskNum = input_list[0]
    desks = deskNum
    desksplace = []
    for i in range(desks):
        desksplace.append(i+1)
    for i in input_list[1::]:
        if i in desksplace:
            desksplace.remove(i)

    odds = [i for i in desksplace if i%2 == 1]
    evens = [i for i in desksplace if i%2 == 0]

    for i in evens:     #kendisinden 2 fazla olan çift sayılar sütun2 deki alt alta oturacakları beliler
        if (i+2) in evens: 
            sitNum += 1

    for i in odds:  #kendisinden 2 fazla olan tek sayılar sütun1 deki alt alta oturacakları beliler
        if (i+2) in odds:
            sitNum += 1

    for i in evens:     #kendisinden 1 fazla olan çift sayılar yan yana oturacakları beliler
        if (i-1) in odds:
            sitNum += 1

    return sitNum

inputs = input()
input_list = []
index = 0
myStr = ""
for i in inputs:    
    if i == ",":
        myStr += " "        
    else:
        myStr += i
    input_list = myStr.split()

for i in range(len(input_list)):
    input_list[i] = int(input_list[i])



print(place_student(input_list))



