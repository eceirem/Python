row = 5
for i in range(row):
    for j in range(i,row):
        print(" ", end="")
    for l in range(i+1):
        print("*", end='')

    print("")