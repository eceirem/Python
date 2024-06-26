def toplam(num1,num2):
   print(num1+num2)

toplam(5,6)

def func(*strVal):
   print(type(strVal))

func("10")
func(10)


def func(*strVal):
    for val in strVal:
        print(val)

func("Burak", 123, "Python", 'a', 34)

def toplam(*numbers):
    toplamVal = 0
    for num in numbers:
        toplamVal += num
    print(toplamVal)

toplam(5,6,7)