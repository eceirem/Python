password = input()
kucukH = False
buyukH = False
strIn = False
mystr = "/_?@#:"
if len(password) < 6 or len(password) > 9:
    print("invalid")


else:
    for i in password:
        if i >= "a" and i <= "z":
            kucukH = True
        if i >= "A" and i <= "Z":
            buyukH = True

        for j in mystr:
            if j in password:
                strIn = True

    if kucukH and buyukH and strIn:
        print("valid")
    else: 
        print(kucukH, buyukH, strIn, "invalid")
    