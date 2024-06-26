terms = int(input())
pi = 4.0
division = 1  #paydasını belirledik 

for i in range(1,terms):
    division += 2
    if (i % 2) == 1:
        pi -= 4/division
    else: 
        pi += 4/division

print(f"{pi:.8f}")
