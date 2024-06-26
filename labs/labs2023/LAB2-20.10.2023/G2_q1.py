num = input()
sumOfDigitsPow = 0
index = 0

while(index < 4):
    sumOfDigitsPow += int(num[index]) ** (index+1)
    index += 1

print(sumOfDigitsPow)

if(int(num) == sumOfDigitsPow):
    print("disarium")
else:
    print("notdisarium")