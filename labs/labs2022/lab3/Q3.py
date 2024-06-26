a = input()
b = input()

sum1=0
sum2=0

for i in a:
    sum1 += int(i)
for i in b:
    sum2 += int(i)

if sum1 == sum2:
    print("1")

else:
    print("0")