x = int(input())
terms = int(input())
e_x = 1
fact = 1
for i in range(1,terms):
    fact *= i
    e_x += (x**i)/fact

print(f"{e_x:.8f}")