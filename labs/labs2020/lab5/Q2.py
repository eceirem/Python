def not_al():   
    not1 = int(input())
    not2 = int(input())
    not3 = int(input())    
    return not1,not2,not3
    
def ortalama_hesapla(a,b,c):
    ort1 = a/stdNum
    ort2 = b/stdNum
    ort3 = c/stdNum
    return ort1,ort2,ort3

def ortalama_bas():
    print(stdNum)
    print(ortalamalar[0])
    print(ortalamalar[1])
    print(ortalamalar[2])    

a = 0
b = 0
c = 0
flag = input()
stdNum = 0
while flag != "end":
    notlar = not_al()
    flag = input()
    stdNum += 1
    a += notlar[0]
    b += notlar[1]
    c += notlar[2]
    ortalamalar = ortalama_hesapla(a,b,c)

ortalama_bas()

