def max_eat(n):
    snake = 1
    meal = 0
    while snake <= n*n:
        snake *= 2
        meal += 1
    return meal-1

n = int(input())

print(max_eat(n))
