my_str = input()
string = ""
index = 0
string += my_str[0]
for i in my_str:    
    if i == " ":
        string += my_str[index+1]
    index += 1
print(string)

