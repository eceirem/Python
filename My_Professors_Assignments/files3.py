#dosyayı okuyuo kaç adet a harfi olduğunu bulan fonk yazınız.

def find_a(text):
    f = open(text + ".txt","r")
    count = 0
    for ch in f.read():
        if ch == "a" or ch == "A":
            count += 1
    f.close()
    return count

print(find_a("file"))

