class Circle():
    pi = 3
    def __init__(self,radius,radian = 360):
        self.radius = radius
        self.radian = radian

    def getArea(self):        
        return round((self.pi*self.radius**2)*self.radian/360)
    
    def getPerimeter(self):
        return round((self.pi*self.radius*2)*self.radian/360)
    
my_circle = Circle(3,120)
print(my_circle.getArea())
print(my_circle.getPerimeter())