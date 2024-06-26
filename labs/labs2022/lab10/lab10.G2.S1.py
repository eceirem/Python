def ebob_ekok(x,y):
    carpanlar_x = []
    carpanlar_y = []
    ortak = []
    ebob = 0
    ekok = 0
    for i in range(1,x+1):
        if x % i == 0:
            carpanlar_x.append(i)
    for j in range(1,y+1):
        if y % j ==0:
            carpanlar_y.append(j)
    for sayi in carpanlar_x:
        if sayi in carpanlar_y:
            ortak.append(sayi)
            ebob = max(ortak)
    ekok = int((x*y)/ebob)
    return ebob, ekok
def factoriyel(ebob):
    fact = 1
    for i in range(1,ebob+1):
        fact *= i
    return fact
def tam_bolenleri(ekok):
    bolenler = []
    for i in range(1,ekok+1):
        if ekok % i == 0:
            bolenler.append(i)
    return bolenler
ebob, ekok = ebob_ekok(24,30)
print(ebob)
print(ekok)
print(factoriyel(ebob))
print(tam_bolenleri(ekok))
