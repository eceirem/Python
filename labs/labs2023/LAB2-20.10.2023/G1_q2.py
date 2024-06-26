num = int(input())
sumOfDigits = 0
temp = num

while(temp != 0):
    sumOfDigits += (temp % 10)
    temp //= 10

print(sumOfDigits)

if((num % sumOfDigits) == 0):
    print("harshad")
else:
    print("notharshad")
