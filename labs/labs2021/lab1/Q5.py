number = int(input())
sum = 0
for i in range(1,number):
    if (number % i) == 0:
        sum += i

if sum == number:
    print("1")
else:
    print("0")