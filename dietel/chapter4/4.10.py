import random
devam = 0
guess_list = []
tahmin_list = []
guess_win = []
pc_win = []
player_counter = 0
computer_counter = 0
while devam != -1:
    guess_list.append(int(input("İlk sayı tahmininizi giriniz: ")))
    guess_list.append(int(input("İkinci sayı tahmininizi girniz: ")))
    tahmin_list.append(random.randrange(1,82))
    tahmin_list.append(random.randrange(1,82))
    sayi = random.randrange(1,10)
    sayi2 = random.randrange(1,10)
    sayi3 = sayi * sayi2
    for i in guess_list:
        if i == sayi3:
            guess_win.append(i)
            player_counter += 1
        else:
            continue
    for j in tahmin_list:
        if j == sayi3:
            pc_win.append(j)
            computer_counter += 1
        else:
            continue
    devam = int(input("Bitirmek için -1'e bas. Bir daha oynamak için 0'a bas."))
print("The player wins", player_counter, "times")
print("Computer wins", computer_counter, "times")
print("The players correct numbers are", guess_win)
print("The computers correct numbers are", pc_win)