num = input()
pow = int(input())
sum = 0
for i in num:
    sum += int(i)**pow
    pow += 1

k = int(sum/int(num))
print(k)