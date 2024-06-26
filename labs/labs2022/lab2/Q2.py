terms = int(input())
pi = 4.0
div = 1
for i in range(1,terms):
    div += 2
    if (i%2) == 1:
        pi -= 4/div
    else:
        pi += 4/div

    print(f"{pi:.8f}")