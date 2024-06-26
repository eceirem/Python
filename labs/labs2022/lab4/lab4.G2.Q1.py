def asal_carpan_bulma(x):
    carpan_listesi = ''
    for i in range(2,x-1):
        if x % i == 0:
            carpan_listesi += 'i'
        else:
            continue
    print(asal_sayi_bulma(carpan_listesi),sep=' ')


def asal_sayi_bulma(str):
    basilacak = ''
    for i in str:
        if i % 2 != 0:
            basilacak += i
        else:
            continue
    return basilacak

print(asal_carpan_bulma(280))

