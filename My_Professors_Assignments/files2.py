#dosyayı okuyup her kelimenin ilk harfini büyük harfe çevirsin
f = open("file.txt", "r")
f2 = open("text2.txt", "w")

for text in f:
    text = text.strip()

    for word in text.split():
        word = word.capitalize()
        f2.write(word + " ")

    f2.write("\n")


