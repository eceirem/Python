def sumOfDigits(num,sumdigits):
    while(num//10 != 0):
        sumdigits += num%10
        num//=10

    sumdigits += num
    
    if(sumdigits//10 != 0):
        return sumOfDigits(sumdigits,0)
    
    else:
        return sumdigits
    

num = int(input())
sumdigits = sumOfDigits(num,0)
print(sumdigits)