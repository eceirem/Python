class Kure:
    def __init__(self, yaricap, pi=3):
        self.yaricap = yaricap
        self.pi = pi

    def alan_hacim_hesapla(self):
        alan = int(4 * self.pi * (self.yaricap ** 2))
        hacim = int(4 / 3 * self.pi * (self.yaricap ** 3))
        intOrFloatPrint(alan, hacim)


class KureDilimi(Kure):
    def __init__(self, aci, yaricap, pi=3):
        super().__init__(yaricap, pi)
        self.aci = aci

    def kure_dilimi_alan_hacim_hesapla(self):
        alan2 = (4 * self.pi * (self.yaricap ** 2) * self.aci) / 360
        hacim2 = (4 / 3 * self.pi * (self.yaricap ** 3) * self.aci) / 360
        intOrFloatPrint(alan2, hacim2)


def intOrFloatPrint(*args):
    for i in args:
        if i % 1:
            print(round(i, 2))
        else:
            print(int(i))


yaricap = float(input())
aci = float(input())
islem = Kure(yaricap)
islem.alan_hacim_hesapla()
islem2 = KureDilimi(aci, yaricap)
islem2.kure_dilimi_alan_hacim_hesapla()
