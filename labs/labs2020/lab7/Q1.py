str_A = input()
str_B = input()
ind_A = [] #B nin içindeki silinecekler
ind_B = [] #A nin içindeki silinecekler
silinecekler_A = []
silinecekler_B = []
son_A = []
son_B = []
puan_A = 0
puan_B = 0
dic = {}
for i in range(10):
    ind_A.append(int(input()))

for j in range(10):    
    ind_B.append(int(input()))

for index in ind_A:
    silinecekler_B += str_B[index]

for index in ind_B:
    silinecekler_A += str_A[index]


for i in str_A:
    if i not in silinecekler_A:
        son_A += i

for i in str_B:
    if i not in silinecekler_B:
        son_B += i

for i in range(len(son_A)):
    ascii_diff = abs(ord(son_A[i]) - ord(son_B[i]))
    if ord(son_A[i]) > ord(son_B[i]):
        puan_A += ascii_diff
    elif ord(son_A[i]) < ord(son_B[i]):
        puan_B += ascii_diff

dic = {"A": puan_A, "B": puan_B}
print(dic)