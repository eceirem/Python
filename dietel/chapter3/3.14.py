count = 119
pi = 0
denem = 1
for i in range(count):
    if i%2 ==0:
        pi +=4/denem
    else:
        pi -=4/denem
    denem += 2
print(pi)