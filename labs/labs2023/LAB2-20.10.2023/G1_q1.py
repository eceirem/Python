num1 = int(input())
num2 = int(input())

counter = 0

while(num1 != 1):
    if(num1%2 == 0):
        num1 /= 2

    else:
        num1 = num1 * 3 + 1

    counter += 1

print(counter)
counter = 0

while(num2 != 1):
    if(num2%2 == 0):
        num2 /= 2

    else:
        num2 = num2 * 3 + 1

    counter += 1
    
print(counter)
