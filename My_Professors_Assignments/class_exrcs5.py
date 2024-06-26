class Boni():
    def __init__(self,number):
        self.number = number
    def toplama(self):
        num = Badi(self.number)
        print(num.counter)
        total = self.number + num.mult()
        print(total)

class Badi():
    counter = 0
    def __init__(self,number):
        self.counter += 1
        self.number = number
    def mult(self):
        return (self.number*5)-3



num1 = Boni(5)
num1.toplama()
print(Badi.counter)

