str1 = input()
str2 = input()
same_str = ""

for i in str1:
    for j in str2:
        if i == j:
            same_str += i

print(same_str)