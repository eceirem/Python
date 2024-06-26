class Circle():
    pi = 3
    def __init__(self,apsis,ordinate):
        '''x ve y eksenlerini bu şekilde tanıtırsak self kullanımı daha çok anlaşılabilir.'''
        self.x = apsis
        self.y = ordinate
        '''yarıçapı manuel oluşturalım input olarak vermeyelim fazladan bir fonksiyonumuz olsun.'''
        self.r = self.radius()
        self.area = self.getArea()
        self.perimeter = self.getPerimeter()


    def radius(self):
        '''Yarıçapı bulmak için en garanti yol x ve y nin çarpımları ile hesaplamak olur diye düşündüm ama toplamları da olabilir. Eğer negatif bir değer girilirse (2,3,4. bölgelerden) yarıçapın negatif çıkmaması için -1 ile çarpıyoruz.'''
        if(self.x<0 or self.y<0):
            return (self.x*self.y*-1)
        else:
            return (self.x*self.y)


    def getArea(self):        
        '''Alan bulmak için pi sayısı ile yarıçapın karesini alalım.'''
        return round((self.pi*self.r**2))
    
    def getPerimeter(self):
        return round((self.pi*self.r*2))

    def position(self,other):
        '''Merkezler arası mesafe hesaplanıyor ve ona göre bu çemberlerin konumlarına bakılıyor. Buradan dönecek bilgiye göre ekrana mesaj basma işlemi gerçekleştirilecektir.'''
        x_diff = (self.x - other.x) **2
        y_diff = (self.y - other.y) **2
        distance  = (x_diff + y_diff)**0.5        
        if (abs(self.r - other.r) < distance and distance < (self.r + other.r)):
            '''Merkezler arası mesafe yarıçapları toplamından küçükse ve farkları aralarındaki mesafeden küçükse bu çemberler kesişiyordur'''
            return "Bu cemberler kesisiyor."       
        elif (distance == (self.r + other.r) or distance == abs(self.r - other.r)):
            '''Merkezler arası mesafe ve yarıçapların toplamı eşitse bu iki çember teğettir dıştan teğettir.  yarıçaplarının farkları merkezler arası uzaklığa eşitse de içten teğettir.'''
            return "Bu cemberler teget."
        else:
            '''Merkezler arası mesafe yarıçapları toplamından fazla olduğu için kesişmiyorlar.'''
            return "Bu cemberler kesismiyor."
    
    
    def __str__(self):
        return f"Circle = M({self.x},{self.y})\nRadius = {self.r}\nArea = {self.area}\nPerimeter = {self.perimeter}"

apsis = int(input())
ordinate = int(input()) 
# circle1 oluştu
circle1 = Circle(apsis,ordinate)
apsis = int(input())
ordinate = int(input()) 
circle2 = Circle(apsis,ordinate)

#position metodunu kullanarak çemberlerin konumunu mesaj olarak bastıracağız.
print(circle1.position(circle2))
#circle bilgilerini de bastıralım.
print(circle1)
print(circle2)
