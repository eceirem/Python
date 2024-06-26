try:
    print("waow")
 #   sayi1 = int(input())
  #  sayi2 = int(input())
   # print(sayi1/sayi2)
except (ValueError,TypeError):
    print("Lütfen sayı giriniz.")
except ZeroDivisionError:
    print("payda 0 olmamalı.")
finally:
    print("finally bloğu her zaman çalışır.")

dosya = open("yazi.txt","a")
dosya.write("ekleme yapıyorum")
dosya.close()

dosya = open("yazi.txt","r")
dosya.seek(0)
str1 = dosya.readline()
dosya.seek(5)
str2 = dosya.readline()
print(str1,str2,end=" ")
dosya.seek(29)
print(dosya.readlines())
dosya.close()

with open("yazi.txt",mode="r+") as dosya:
    data = dosya.readlines()
    data.insert(1,"ekleme yapıyorum\n")
    dosya.seek(0)
    dosya.write("ece\n")
    dosya.writelines(data)
