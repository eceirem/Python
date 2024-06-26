def int_to_binary(sayi):
    bolumlerListe = []
    terstenListe = []
    while(sayi > 0):
        bolumlerListe.append(sayi%2)
        sayi //= 2

    for i in range(len(bolumlerListe),0,-1):
        terstenListe.append(bolumlerListe[i-1])

    return terstenListe


liste = int_to_binary(int(input()))
for i in liste:
    print(i,end="")