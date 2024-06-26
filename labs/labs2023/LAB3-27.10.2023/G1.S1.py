num = int(input())
while(num > 0):
    counter = 0
    while(num >= 2):
        counter += 1
        num = num**(0.5)
    print(counter)
    num = int(input())
