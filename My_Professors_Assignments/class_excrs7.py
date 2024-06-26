#Vectors

class Vectors():
    def __init__(self, i,j,k):
        self. i = i
        self.j = j
        self.k = k

    def __add__(self,other):
        new_i = self.i + other.i
        new_j = self.j + other.j
        new_k = self.k + other.k
        return Vectors(new_i,new_j,new_k)

    


    def __str__(self):
        return "(" + str(self.i) + "," + str(self.j) + "," + str(self.k) + ")"

vec1 = Vectors(1,1,1)
vec2 = Vectors(1,2,3)

print(vec2+vec1)


