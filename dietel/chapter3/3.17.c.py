sayi = int(input())
for i in range(sayi):
    for l in range(i):
        print(" ", end='')
    for k in range(sayi-i):
        print("*", end='')


    print()