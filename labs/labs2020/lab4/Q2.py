str1 = input()
str2 = input()
same_char = ""
#ortak karakterleri basalım
for i in str1:
    if i in str2 and i not in same_char:
        same_char += i

print(same_char)

#Sadece str1 de olanları basalım
for i in str1:
    if i not in str2:
        print(i, end=' ')
print()

#Sadece str2 de olanları basalım
for i in str2:
    if i not in str1:
        print(i,end=' ')

