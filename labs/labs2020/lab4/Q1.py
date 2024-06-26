my_str = input()

counter = 0

max_counter = 0

for i in my_str:
    if i != " ":
        counter += 1
    else:
        if counter > max_counter:
            max_counter = counter
        counter = 0

if counter > max_counter:
    max_counter = counter
    

print( max_counter)