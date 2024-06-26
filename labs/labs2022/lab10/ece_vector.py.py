class Vector:
	def __init__(self,i1,j1,k1,i2,j2,k2):
		self.i1 = i1
		self.j1 = j1
		self.k1 = k1
		self.i2 = i2
		self.j2 = j2
		self.k2 = k2
	def print_vector(self):
		print(i1,j1,k1)
		print(i2,j2,k2)
	def sum_vector(self):
		sum_i = i1 + i2
		sum_j = j1 + j2
		sum_k = k1 + k2
		print(sum_i,sum_j,sum_k,sep=",")
	def fark_vector(self):
		fark_i = i1 - i2
		fark_j = j1 - j2
		fark_k = k1 - k2
		print(fark_i,fark_j,fark_k,sep=",")
	def skaler(self):
		skaler_i = i1*i2
		skaler_j = j1*j2
		sklaer_k = k1*k2
		print(skaler_i,skaler_j,sklaer_k,sep=",")
	def uzaklik(self):
		m1 = i1-i2
		m2 = j1-j2
		m3 = k1-k2
		mesafe = (m1**2+m2**2+m3**2)**0.5
		if mesafe%1 == 0:
			print(int(mesafe))
		else:
			print("{:.2f}".format(mesafe))
i1 = int(input())
j1 = int(input())
k1 = int(input())
i2 = int(input())
j2 = int(input())
k2 = int(input())
islem = Vector(i1,j1,k1,i2,j2,k2)
islem.print_vector()
islem.sum_vector()
islem.fark_vector()
islem.skaler()
islem.uzaklik()