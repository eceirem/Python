#2 argüman alsın, ilk sayıyı ikinci sayıya kadar katlarını alarak listeye atsın ve return etsin. => 7,14,...,35 gibi 

def multiple(num, mult):
    return [num * i for i in range(1,mult+1)]

print(multiple(7,5))