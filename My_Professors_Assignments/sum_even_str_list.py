list = ['a', 0, 4, 2, 'z']
str = "a0475xAB8"

numbers_even = "02468"

list_sum_even = 0
str_sum_even = 0

for i in list:
    if type(i) == int and i % 2 == 0:
        list_sum_even += i

for i in str:
    if i in numbers_even:
        str_sum_even += int(i)


print("sum of the even numbers in list: ",list_sum_even)


print("sum of the even numbers in str: ",str_sum_even)
