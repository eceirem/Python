class Coordinate():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,other):
        x_diff = (self.x - other.x) **2
        y_diff = (self.y - other.y) **2
        return (x_diff + y_diff)**0.5
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    
c = Coordinate(3,4)
a = Coordinate(0,0)

print(c.distance(a))