class Fraction():
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom

    def __add__(self,other):
        '''+ operatörüne overload'''
        top = self.num*other.denom + self.denom*other.num
        bottom = self.denom*other.denom
        return self.simplify(top,bottom)
    
    def __sub__(self,other):
        top = self.num*other.denom - self.denom*other.num
        bottom = self.denom*other.denom
        return self.simplify(top,bottom)
    def __mul__(self,other):
        top = self.num*other.num
        bottom = self.denom*other.denom
        return self.simplify(top,bottom)
    def __truediv__(self,other):
        temp = other.num
        other.num = other.denom
        other.denom = temp
        top = self.num*other.num
        bottom = self.denom*other.denom
        return self.simplify(top,bottom)

    def simplify(self,top,bottom):
        if(top<0):
            top = top*-1
            #ebobu hesaplayalım
            i = 2
            ebob = 1
            while i <= min(top,bottom):
                if ((top % i == 0) and (bottom % i == 0)):
                    ebob = i
                i += 1

            top2 = top//ebob
            bottom2 = bottom//ebob
            return Fraction(top2*-1,bottom2)        
        else:
            i = 2
            ebob = 1
            while i <= min(top,bottom):
                if ((top % i == 0) and (bottom % i == 0)):
                    ebob = i
                i += 1

            top2 = top//ebob
            bottom2 = bottom//ebob
            return Fraction(top2,bottom2)
        
    def __str__(self):
        if(self.num > 0):
            div = self.num / self.denom

            if((div)%1 == 0):
                return str(int(div))
            
            elif(div>0):
                self.num = self.num % self.denom
                return str(int(div)) + "+" + str(self.num) + "/" + str(self.denom)
            else:
                return str(int(div)) + "+" + str(self.num) + "/" + str(self.denom)
            
        else:
            self.num = self.num*-1
            div = self.num/self.denom
            if((div)%1 == 0):
                return "-" + str(int(div))
            elif(div>0):
                self.num = self.num % self.denom
                return "-" + str(int(div)) + "-" + str(self.num) + "/" + str(self.denom)
            else:
                return str(int(div)) + "-" + str(self.num) + "/" + str(self.denom)
            

numerator = int(input())
denom = int(input())
rational1 = Fraction(numerator,denom)
numerator = int(input())
denom = int(input())
rational2 = Fraction(numerator,denom)

print(f"Addition: {rational1+rational2}")
print(f"Subtraction: {rational1-rational2}")
print(f"Multiplication: {rational1*rational2}")
print(f"Division: {rational1/rational2}")