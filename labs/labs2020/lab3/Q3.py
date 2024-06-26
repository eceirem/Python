counter = 0

for i in range(1,501):
    for j in range(i,501):
        for z in range(j,501):
            if i**2 + j**2 == z**2:
                print(i,"   ",j,"   ",z)
                counter += 1
print(counter)
