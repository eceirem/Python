#elemantary school program
#Learn Multiplication.
#4.14,4.15,4.16,4.17 bir arada. Geliştirilmiş versiyon. İşlem seçme ve rastgele işlem getirme var.
import random
a = True
islem = input("Toplama için 1'e basınız\n"
              "Çıkarma içiçn 2'ye basınız\n"
              "Çarpma için 3'e basınız\n"
              "Bölme için 4'e basınız.\n"
              "Rastgele işlem için 5'e basınız.\n")
sayi1 = random.randrange(1,100)
sayi2 = random.randrange(1,100)
secenekler = ["+","-","*","//"]
if islem == '1':
    sonuc = sayi1 + sayi2
    grln_sonuc = int(input(f" {sayi1} + {sayi2} ? = "))
elif islem == '2':
    sonuc = sayi1 - sayi2
    grln_sonuc = int(input(f" {sayi1} - {sayi2} ? =  "))
elif islem == '3':
     sonuc = sayi1 * sayi2
     grln_sonuc = int(input(f"How much is {sayi1} times {sayi2} ? "))
elif islem == '4':
     sonuc = sayi1 // sayi2
     grln_sonuc = int(input(f" {sayi1} // {sayi2} ? = "))
elif islem == '5':
    sonuc = random.choice(secenekler)
    if sonuc == "+":
        sonuc = sayi1 + sayi2
        grln_sonuc = int(input(f" {sayi1} + {sayi2} ? = "))
    elif sonuc == "-":
        sonuc = sayi1 - sayi2
        grln_sonuc = int(input(f" {sayi1} - {sayi2} ? =  "))
    elif sonuc == "*":
        sonuc = sayi1 * sayi2
        grln_sonuc = int(input(f"How much is {sayi1} times {sayi2} ? = "))
    elif sonuc == "//":
        sonuc = sayi1 // sayi2
        grln_sonuc = int(input(f" {sayi1} // {sayi2} ? = "))
while a == True:
     if sonuc == grln_sonuc:
          liste = ["Very Good!","Nice Work!","Keep up the good work!"]
          print(random.choice(liste))
          a = False
     else:
          liste2 = ["No.Please try again.", "wrong. Try once more.", "No keep trying."]
          print("No try again.")
          if islem == '1':
              sonuc = sayi1 + sayi2
              grln_sonuc = int(input(f" {sayi1} + {sayi2} ? = "))
          elif islem == '2':
              sonuc = sayi1 - sayi2
              grln_sonuc = int(input(f" {sayi1} - {sayi2} ? =  "))
          elif islem == '3':
              sonuc = sayi1 * sayi2
              grln_sonuc = int(input(f"How much is {sayi1} times {sayi2} ? "))
          elif islem == '4':
              sonuc = sayi1 // sayi2
              grln_sonuc = int(input(f" {sayi1} // {sayi2} ? = "))
          elif islem == '5':
              sonuc = random.choice(secenekler)
              if sonuc == "+":
                  sonuc = sayi1 + sayi2
                  grln_sonuc = int(input(f" {sayi1} + {sayi2} ? = "))
              elif sonuc == "-":
                  sonuc = sayi1 - sayi2
                  grln_sonuc = int(input(f" {sayi1} - {sayi2} ? =  "))
              elif sonuc == "*":
                  sonuc = sayi1 * sayi2
                  grln_sonuc = int(input(f"How much is {sayi1} times {sayi2} ? = "))
              elif sonuc == "//":
                  sonuc = sayi1 // sayi2
                  grln_sonuc = int(input(f" {sayi1} // {sayi2} ? = "))