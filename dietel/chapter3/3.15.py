nterms = int(input("How many terms? "))
n1 = 0
n2 = 1
count = 0
while nterms<=0:
    print("Please enter a positive integer.")
    nterms = int(input("Try again: "))
if nterms == 1:
    print("Fibonacci sequence: ")
    print(n1)
else:
    print("Fibonacci sequence: ")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1