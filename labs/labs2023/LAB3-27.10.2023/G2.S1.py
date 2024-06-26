num = int(input())

while(num > 0):
    boolean = 0
    for i in range(2,num):
        if (num%i) == 0:
            boolean = 0
            break
        else:
            boolean = 1
        
    if boolean:
        print("prime")

    else:
        print("notprime")

    num = int(input())