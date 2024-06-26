n = input()
p = int(input())
sum = 0
for i in n:
    sum += (int(i))**p
    p += 1

k = int(sum/int(n))
print(k)