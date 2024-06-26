class Complex():
	def __init__(self,a,bi):
		self.a = a
		self.bi = bi

	def __add__(self,other):
		new_a = self.a + other.a
		new_b = self.bi + other.bi
		return Complex(new_a,new_b)
	
	def __sub__(self,other):
		new_a = self.a - other.a
		new_b = self.bi - other.bi
		return Complex(new_a,new_b) 
	
	def __mul__(self,other):
		new_a = (self.a * other.a) + ((self.bi * other.bi)*-1)
		new_b = (self.a * other.bi) + (self.bi * other.a)
		return Complex(new_a,new_b)
		
	def __eq__(self,other):
		if self.a == other.a and self.bi == other.bi:
			return 1
		else:
			return 0

	def __str__(self):
		if self.bi >= 0:
		    return str(self.a) + "+" + str(self.bi) + "i"
		else:
			return str(self.a) + str(self.bi) + "i"	 

a1 = int(input())
bi1 = int(input())
comp1 = Complex(a1,bi1)

a2 = int(input())
bi2 = int(input())
comp2 = Complex(a2,bi2)

print(comp1)
print(comp2)
print(comp1 + comp2)
print(comp1 - comp2)
print(comp1 * comp2)
print(comp1 == comp2)

