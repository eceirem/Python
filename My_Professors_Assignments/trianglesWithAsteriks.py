for i in range(10):
    for j in range(i):
        print("*", end='')
    print()
for i in range(10,0,-1):
    for j in range(i,0,-1):
        print("*", end='')
    print()

 
for i in range(10):
    for j in range(i):
        print(" ", end='')
    for k in range(10-i):
        print("*", end='')
  
    print()       

for i in range(10):
    for j in range(10-i):
        print(" ", end='')
    for k in range(i):
        print("*", end='')

    print()

for i in range(10):
    for j in range(i):
        print(" " * i , "*" * (10-i), end='')
    print()