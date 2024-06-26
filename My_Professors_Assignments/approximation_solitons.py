cube = 7
epsilon = 0.2
guess = 0
num_guess = 0
while abs(guess ** 3 - cube) >= epsilon and guess ** 3 < cube:
        guess += 0.1
        num_guess += 1

print(f"cube root of, {cube} is equal to {guess:.2f}.")
print("iteration count is", num_guess) 