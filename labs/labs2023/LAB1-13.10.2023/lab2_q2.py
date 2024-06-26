kenar1 = int(input())
kenar2 = int(input())
kenar3 = int(input())

if kenar3 < (kenar1 + kenar2) and kenar2 < (kenar1 + kenar3) and kenar1 < (kenar2 + kenar3):
    print("True")
else:
    print("False")