side1 = input()
side2 = input()
side3 = input()

if side1 == side2 == side3:
    print("eskenar")
elif side1 == side2:
    print("ikizkenar")
elif side1 == side3:
    print("ikizkenar")
elif side2 == side3:
    print("ikizkenar")
else:
    print("cesitkenar")

# counter = -3
# sides = [side1, side2, side3]
# for i in sides:
#     for j in sides:
#         if i == j:
#             counter += 1
# if counter == 0:
#     print("cesitkenar")
# elif counter == 2:
#     print("ikizkenar")
# else: 
#     print("eskenar")