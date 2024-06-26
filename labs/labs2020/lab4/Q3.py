my_str = input()
term = len(my_str)//2
boolean = True
my_str2 = ""
for i in my_str:
    if i != " ":
        my_str2 += i
    else:
        continue

for i in range(term):
    if my_str2[i] != my_str2[-(i+1)]:
        boolean = False

if boolean == 1:
    print("polindrome")
else:
    print("not polindrome")