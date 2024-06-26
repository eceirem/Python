terms = int(input())
e = 1
div = 1
div_fact = 1

for i in range(1, terms):
    div_fact *= div
    e += 1 / div_fact
    div += 1

print(f"{e:.8f}")
