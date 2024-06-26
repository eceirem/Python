class Vector:

    vectors_list = []

    def __init__(self, list):
        
        Vector.vectors_list.append(list)

    def vectors():

        str1 = ""

        for i in Vector.vectors_list:
            str1 += str(i).strip("[").strip("]").replace(" ", "") + "\n"

        return str1.strip("\n")

    @classmethod
    def addition(cls):

        str1 = str(cls.vectors_list[0][0] + cls.vectors_list[1][0]) + "," + str(cls.vectors_list[0][1] + cls.vectors_list[1][1]) + "," + str(cls.vectors_list[0][2] + cls.vectors_list[1][2])

        return str1

    @classmethod
    def subtraction(cls):

        str1 = str(cls.vectors_list[0][0] - cls.vectors_list[1][0]) + "," + str(cls.vectors_list[0][1] - cls.vectors_list[1][1]) + "," + str(cls.vectors_list[0][2] - cls.vectors_list[1][2])

        return str1

    @classmethod
    def scaler_multiplication(cls):

        return cls.vectors_list[0][0] * cls.vectors_list[1][0] + cls.vectors_list[0][1] * cls.vectors_list[1][1] + cls.vectors_list[0][2] * cls.vectors_list[1][2]

    @classmethod
    def length_between_two_dot(cls):

        length = ((cls.vectors_list[0][0] - cls.vectors_list[1][0]) ** 2 + (cls.vectors_list[0][1] - cls.vectors_list[1][1]) ** 2 + (cls.vectors_list[0][2] - cls.vectors_list[1][2]) ** 2 )** 0.5

        if length % 1:
            return "{:.2f}".format(length)
        else:
            return int(length)
        
for i in range(2):
    list = []
    for j in range(3):
        list.append(int(input()))  
    Vector(list)

print(Vector.vectors())
print(Vector.addition())
print(Vector.subtraction())
print(Vector.scaler_multiplication())
print(Vector.length_between_two_dot())



