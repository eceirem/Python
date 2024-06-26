def lower(char):
    if ord(char) < 97:
        return chr(ord(char)+32)
    else:
        return char
    
def my_cipher(string):
    alphabetList = [] #alfabemizi liste şeklinde oluşturalım
    temp_char = '' #benden bir önceki harfi tutmalı
    new_str = "" #şifrelenmiş stringim
    for i in range(26):
        alphabetList.append(chr(ord('a')+i))

    if (string[0].isalpha()):
        new_str += lower(string[0])

    else:
        new_str += string[0]

    temp_char = new_str[0]

    for i in string[1:]:
        index = 0  #kaçıncı sırada bulunduğunu döndürecek (temp değişken için)
        index2 = 0  #kaçıncı sırada bulunduğunu döndürecek (şu anki değişken için)
        if i.isalpha():
            i = lower(i)
            for char in alphabetList:
                index2 += 1
                if char == i:
                    break
            for char2 in alphabetList:
                index += 1
                if char2 == temp_char:
                    break
            if(index2 - index) < 0:
                new_str += alphabetList[(26+(index2 - index))-1]
                temp_char = alphabetList[(26+(index2 - index))-1]
            else:
                new_str += alphabetList[(index2 - index)-1]
                temp_char = alphabetList[(index2 - index)-1]

        else:
            new_str += i

    return new_str
    
veri = input()
print(my_cipher(veri))



            