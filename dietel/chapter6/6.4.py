print(sorted({1, 2, 4, 8, 16}.union({1, 4, 16, 64, 256})))# {1,2,4,8,16,64,256}
print(sorted({1, 2, 4, 8, 16} & {1, 4, 16, 64, 256})) # {1,4,16}
print(sorted({1, 2, 4, 8, 16} - {1, 4, 16, 64, 256})) # {2,8}
print(sorted({1, 2, 4, 8, 16} ^ {1, 4, 16, 64, 256})) # {2,8,64,256}
print({1, 2, 4, 8, 16} == {1, 4, 16, 64, 256}) # False