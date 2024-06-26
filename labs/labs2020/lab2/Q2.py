total_number = int(input())
y = int(input())
minimum = y
for i in range(total_number-1):
    x = int(input())    
    if x < minimum:
        minimum = x
print(minimum)

