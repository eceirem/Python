jump = input()
Meters = float(jump)//1
fark1 = float(jump)-int(Meters)
Decimeters = (fark1)*10//1
fark2 = float(fark1) - float(Decimeters/10)
Centimeters = float(fark2*100)
print(float(Meters),float(Decimeters), float(Centimeters))