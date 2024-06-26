from math import *
degrees = 1
rad = 0
print(f'{"Degree":>2}{"Radian":>13}')
while degrees < 181:
    rad = degrees * pi/180
    print(f"{degrees:>2}{round(rad,2):>16}")
    degrees += 1

