def printPath(char,pathString):
    dictionary = {"A":["B","C","D"],
                  "B": ["E","F"],
                  "D":["G","H"],
                  "G":["I","J"],
                  "H":["K"]}
    
    for keys,values in dictionary.items():
        if char in values:
            key = keys
            pathString += key
            pathString += "/"
            return printPath(key,pathString)
        
        elif char == "A":
            pathString_reversed = ''.join(reversed(pathString))
            return pathString_reversed
    return "{} dosyası ağaçta bulunmamaktadır.".format(char)
while(1):
    char = input("Dosya adını girin (çıkmak için 'q' tuşuna basın): ")
    if char == "q":
        break
    else:
        pathString = ""
        pathString += char
        pathString += "/"
        print(printPath(char,pathString))

