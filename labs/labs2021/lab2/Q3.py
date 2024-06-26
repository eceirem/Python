num1 = input()
num2 = input()

sum1 = 0
sum2 = 0

for i in num1:
    sum1 += int(i)

for j in num2:
    sum2 += int(j)

if sum1 == sum2:
    print("1")

else:
    print("0")