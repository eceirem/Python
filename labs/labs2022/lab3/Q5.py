def eat_max(n):
    meal = 0
    snake = 1
    while snake <= n*n:
        meal += 1
        snake *= 2

    return meal-1


n = int(input())
print(eat_max(n))