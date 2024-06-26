terms = int(input())
e = 1
div = 1
div_fact = 1

for i in range(1,terms):
    div_fact *= div
    div += 1    
    e += 1/div_fact

    print(f"{e:.8f}")