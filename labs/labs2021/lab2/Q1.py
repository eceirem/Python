def count_digits(number):
    counter = 0
    for i in number:
        if i != '-':
            counter += 1
        else:
            continue
    return counter

num = input()
print(count_digits(num))