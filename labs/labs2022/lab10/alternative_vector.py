class Vector:
	def __init__(self,a,b,c,x,y,z):
		self.a=a
		self.b=b
		self.c=c
		self.x=x
		self.y=y
		self.z=z

	def kendi(self):
		sonuc1=str(a)+","+str(b)+","+str(c)		
		sonuc2=str(x)+","+str(y)+","+str(z)		
		print(sonuc1)
		print(sonuc2)

	def toplam(self):
		t1=a+x
		t2=b+y
		t3=c+z
		sonuc=str(t1)+","+str(t2)+","+str(t3)
		print(sonuc)

	def fark(self):
		t1=a-x
		t2=b-y
		t3=c-z
		sonuc=str(t1)+","+str(t2)+","+str(t3)
		print(sonuc)
	
	def skaler_carpim(self):
		t1=a*x
		t2=b*y
		t3=c*z
		sonuc=t1+t2+t3
		print(sonuc)

	def iki_nokta(self):
		t1=a-x
		t2=b-y
		t3=c-z
		uzaklik=(t1**2+t2**2+t3**2)**0.5
		if (uzaklik)%1==0:	
			sonuc=int(uzaklik)		
		else:
			sonuc=round(uzaklik,2)
			if (sonuc*10)%1==0:
				sonuc=str(sonuc)+"0"	
		print(sonuc)
		
a=int(input())
b=int(input())
c=int(input())
x=int(input())
y=int(input())
z=int(input())
islem=Vector(a,b,c,x,y,z)
islem.kendi()
islem.toplam()
islem.fark()
islem.skaler_carpim()
islem.iki_nokta()
