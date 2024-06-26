class Kure:
	def __init__(self,yaricap):		
		self.yaricap = yaricap
	def alan_hacim_hesapla(self):
		pi = 3
		alan = int(4*pi*(yaricap**2))
		hacim = int(4/3*pi*(yaricap**3))
		print(alan)
		print(hacim)
class KureDilimi:
	def __init__(self,aci,Kure):	
		self.aci = aci 
	def kure_dilimi_alan_hacim_hesapla(self):
		alan2 = (4*3*(yaricap**2)*aci)/360
		hacim2 = (4/3*3*(yaricap**3)*aci)/360
		if alan2 % 1 == 0:			
			alan2 = int(alan2)
		else:
			alan2 = round(alan2,2)
		
		print(alan2)

		if hacim2 % 1 == 0:
			hacim2 = int(hacim2)
		else:
			hacim2 = round(hacim2,2)		
		
		print(hacim2)

		
yaricap = int(input())
aci = int(input())
islem = Kure(yaricap)
islem.alan_hacim_hesapla()
islem2 = KureDilimi(aci,Kure)
islem2.kure_dilimi_alan_hacim_hesapla()

