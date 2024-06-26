def count_digits(num):
    counter = 0
    for i in num:
        if i != "-":
            counter += 1
        else:
            continue
    return counter

num = input()
print(count_digits(num))