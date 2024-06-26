def upper(char):
    if ord(char)>= 97:
        return chr(ord(char)-32)
    else:
        return char
def my_cipher(string):
    alphabetList = [] #alfabemizi liste şeklinde oluşturalım
    temp_char = '' #benden bir önceki harfi tutmalı
    new_str = "" #şifrelenmiş stringim
    for i in range(26):
        alphabetList.append(chr(ord('A')+i))

    if(string[0].isalpha()):
        new_str += upper(string[0])
    else:
        new_str += string[0]

    temp_char = new_str[0]

    for i in string[1:]:
        index = 0  #kaçıncı sırada bulunduğunu döndürecek (temp değişken için)
        index2 = 0  #kaçıncı sırada bulunduğunu döndürecek (şu anki değişken için)
        if i.isalpha():
            i = upper(i)
            for char in alphabetList:
                index2 += 1
                if char == i:
                    break
            for char2 in alphabetList:
                index += 1
                if char2 == temp_char:
                    break
            new_str += alphabetList[((index+index2)%26)-1] # E + 8
            temp_char = i #döngüden çıkmadan önce şu anki değeri temp olarak ata yeni döngüde bir önceki değerim i olmuş olacak.
        else:
            new_str += i

    return new_str

veri = input()
print(my_cipher(veri))