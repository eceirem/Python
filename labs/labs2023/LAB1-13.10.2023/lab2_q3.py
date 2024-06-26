geoType = input()

if geoType == "ucgen":
    kenar1 = int(input())
    kenar2 = int(input())
    kenar3 = int(input())
    ucgencevresi = kenar1 + kenar2 + kenar3
    print(ucgencevresi)

elif geoType == "dikdortgen":
    kenar1 = int(input())
    kenar2 = int(input())
    dortgencevresi = (kenar1 + kenar2)*2
    print(dortgencevresi)
