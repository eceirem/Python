def isThisInFolder(text):
    file,folder = text.split(",")
    dictionary = {"A":["B","C","D","E","F","G","H","I","J","K"],
                  "B": ["E","F"],
                  "D":["G","H"],
                  "G":["I","J"],
                  "H":["K"]}
    
    for key,value in dictionary.items():
        if key == folder:
            if file in value:
                return "True"
            else:
                return "False"


while(1):
    text = input("İki klasörü virgülle ayırarak girin (örn. B,A) veya 'q' girerek çıkın: ")
    if text == "q":
        break
    else:
        print(isThisInFolder(text))
