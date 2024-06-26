mystr = input()
liste = list(mystr)
mybool = 0
if ("@" and "." in liste) and (liste.index("@") < liste.index(".")):
    mybool = 1

print(mybool)