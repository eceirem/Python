class Fraction():
    
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom        
        
        
    def __add__(self,other):
        '''Toplama işlemi için + operatörü overloading yapılıyor.'''
        top = self.num * other.denom + self.denom * other.num
        bottom = self.denom * other.denom
        return self.simplify(top,bottom)
    
    def __sub__(self,other):
        '''Çıkarma işlemi için - operatörü overloading yapılıyor.'''
        top = self.num * other.denom - self.denom * other.num
        bottom = self.denom * other.denom
        return self.simplify(top,bottom)

    def __mul__(self,other):
        '''Çarpma işlemi için * operatörü overloading yapılıyor.'''
        top = self.num * other.num
        bottom = self.denom * other.denom
        return self.simplify(top,bottom)
    def __truediv__(self,other):
        '''Bölme işlemi için / operatörü overloading yapılıyor. Bölme işlemi ters çevirip çarpmak demek.'''
        temp = other.num #burada payı kaybetmemek için temp bir değişkene atıyoruz.
        other.num = other.denom #paydayı pay olarak güncelledik. 
        other.denom = temp
        top = self.num * other.num
        bottom = self.denom * other.denom
        return self.simplify(top,bottom)

    def simplify(self,top,bottom):
        '''Sadeleştirme işlemi için ebob buluyor ve en büyük ortak bölnelerine kesirleri bölüp return ediyoruz yeni bir kesir olarak. Ancak - li bir kesir gelirse bu işlemde ebob bulmak sıkıntı çıkardığı için - ile gelen ifadeyi + varsayarak işleme başlıyoruz ve return ederken - işlemini yapıyoruz.'''
        if(top<0):
            top = top*-1
            i = 2
            ebob = 1
            while i <= min(top, bottom):
                if top % i == 0 and bottom % i == 0:
                    ebob = i
                i += 1
            top2 = top // ebob
            bottom2 = bottom // ebob
            return Fraction(-1*top2, bottom2)
        else:
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
       '''Fonksiyonda basma işlemi uygulamadan önce bileşik kesir olma durumları kontrol edilecek. İlk önce kesir negatif mi ona bakılacak çünkü bastırma işleminde + ve - yan yana gelmeyecek.'''
       if(self.num > 0):
            div = self.num/self.denom
            if((div)%1 == 0): # 2/1 gibi tam bir ifade geldiyse
                return str(int(div))
            elif(div > 0): #2/1 gibi tam bir bölen yok ama 27/13 gibi bileşik bir kesir
                self.num = self.num % self.denom
                str(int(div)) + "+" + str(self.num) + "/" + str(self.denom) 
                
            return str(int(div)) + "+" + str(self.num) + "/" + str(self.denom) 
       else:
            '''Önemli bir nokta var burada. Tam kısmı init ederken oay//payda dediğimiz için -1,1 çıksa bile negatif olduğu kesri -2 ye yuvarlıyor bu yüzden bir fazlasını almamız lazım.'''
            self.num = self.num*-1
            div = self.num/self.denom
            if((div)%1 == 0): # 2/1 gibi tam bir ifade geldiyse direkt tam kısmı basmalıyım +1 dememeliyim çünkü burada zaten yuvarlama işlemi yapılmıyor.
                return "-" + str(int(div))
            elif(div > 0): #2/1 gibi tam bir bölen yok ama 27/13 gibi bileşik bir kesir
                self.num = self.num % self.denom
                str(int(div)) + "-" + str(self.num) + "/" + str(self.denom) 
                
            return str(int(div)) + "-" + str(self.num) + "/" + str(self.denom) 
        
numerator = int(input())
denumerator = int(input())
rational1 = Fraction(numerator,denumerator)
numerator = int(input())
denumerator = int(input())
rational2 = Fraction(numerator,denumerator)

print(f"Addition: {rational1 + rational2}")
print(f"Subtraction: {rational1 - rational2}")
print(f"Multiplication: {rational1*rational2}")
print(f"Division: {rational1 / rational2}")
