num = input() 
mulOfDigits = 1
index = 0

while(index != len(num)):
    mulOfDigits *= int(num[index]) 
    index += 1

print(mulOfDigits)