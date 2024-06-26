def fibo_dizisi(sayi):
    if sayi < 0:
        print("hatalı değer.")
    elif sayi == 0:
        return 0
    elif sayi == 1:
        return 1
    elif sayi > 1:
        return fibo_dizisi(sayi-1) + fibo_dizisi(sayi-2)
sayi = int(input("Görmek istediğiniz fibo_dizisi adımını giriniz: "))
fibo_list = []
for i in range(sayi):
    fibo_list.append(fibo_dizisi(i))
print(fibo_list)