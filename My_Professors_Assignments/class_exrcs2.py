class Fraction():
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom

    def __add__(self,other):
        top = self.num * other.denom + self.denom * other.num
        bottom = self.denom * other.denom
        return self.sadelestir(top,bottom)
    
    def sadelestir(self,top,bottom):
        i = 2
        ebob = 1
        while i <= min(top, bottom):
            if top % i == 0 and bottom % i == 0:
                ebob = i
            i += 1
        top2 = top // ebob
        bottom2 = bottom // ebob
        return Fraction(top2, bottom2)
    
    def __str__(self):
       return str(self.num) + "/" + str(self.denom) 
        
    
kesirli1 = Fraction(1,4)
kesirli2 = Fraction(2,4)

print(kesirli1 + kesirli2)
