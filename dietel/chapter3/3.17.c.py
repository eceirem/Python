row = int(input())
for i in range(row):
    for l in range(i):
        print(" ", end='')
    for k in range(row-i):
        print("*", end='')
    print()