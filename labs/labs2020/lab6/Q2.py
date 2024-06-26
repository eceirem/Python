onluk = int(input())
ikilik = ''
while (onluk) > 0:           
    ikilik = str(onluk % 2) + ikilik #burada sondan başa yazdığımız için dikkaaatt!! ikilik += kullanma.
    onluk //= 2

print(ikilik)

