import ast
def sumOfNum(liste):
    sumEven = 0
    sumOdd = 0
    for i in liste:
        if(i%2 == 0):
            sumEven += i
        else:
            sumOdd += i
        
    return [sumEven,sumOdd]


liste = input()
liste = ast.literal_eval(liste)
listeSum = sumOfNum(liste)
print(listeSum)
