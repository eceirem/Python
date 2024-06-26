class Circle():
    pi = 3
    def __init__(self,apsis,ordinate):
        '''x ve y eksenlerine göre çemberin merkezini belirtiyorum'''
        self.x = apsis
        self.y = ordinate
        self.r = self.radius()
        self.area = self.getArea()
        self.perimeter = self.getPerimeter()
        
    def radius(self):
        if(self.x <0 or self.y <0):
            return (self.x*self.y*-1)
        else:
            return (self.x*self.y)

    def getArea(self):
        '''Alan bulacağız burada pi = 3'''
        return round(self.pi*(self.r**2))
    def getPerimeter(self):
        '''çevre buluyoruz pi=3'''
        return round(self.pi*self.r*2)
    
    def position(self,other):
        '''çemberlerin birbirlerine göre olan konumlarını bulalım.'''
        x_diff=(self.x-other.x)**2
        y_diff=(self.y-other.y)**2
        distance = (x_diff+y_diff)**0.5 #merkezler arası mesafeyi hesapladım.
        if(abs(self.r-other.r)<distance and distance<(self.r+other.r)):
            return "Bu cemberler kesisiyor."
        elif(distance == (self.r+other.r) or distance==abs(self.r-other.r)):
            return "Bu cemberler teget."
        else:
            return "Bu cemberler kesismiyor."
        
    def __str__(self):
        return f"Circle = M({self.x},{self.y})\nRadis={self.r}\nArea={self.area}\nPerimeter={self.perimeter}"



apsis = int(input())
ordinate = int(input())
circle1 = Circle(apsis,ordinate)
#circle1 objesi oluştu.
apsis = int(input())
ordinate = int(input())
circle2 = Circle(apsis,ordinate)
#circle2 objesi oluştu.
print(circle1.position(circle2))
print(circle1)
print(circle2)
