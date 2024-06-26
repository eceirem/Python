colors1 = {'red', 'blue', 'yellow', 'green', 'black', 'white'}
colors2 = {'red', 'purple', 'pink', 'white'}
if len(colors1) < len(colors2):
    print(colors2)
else:
    print(colors1)
print(colors1 == colors2)
print(colors1 | colors2) #union, birleşim kümesi
print(colors1 & colors2) #intersection, kesişim kümesi
print(colors1 - colors2) #difference soldaki setin sağda bulunmayanlarını basar
print(colors1 ^ colors2) #fark kümesi