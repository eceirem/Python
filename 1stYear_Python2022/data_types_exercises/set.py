#Veri Yapıları- Setler
# set olusturma
s = set()
print(s)
l = [1,"a","ali",123]
s = set(l)
print(l)

t = ("a","ali")
s = set(t)
print(t)
ali = "lutfen_ata_bak ma_uz aya_git"
print(type(ali))
s = set(ali)
print(set(ali))
l = ["ali","lütfen","ata", "bakma", "uzaya","git","git", "ali","git"]
s = set(l)
print(s)
print(len(s))
print(l[0])
#print(s[0])#setler sırarıs olduğu için index yoktur.Uyarı alırız.
#Eleman ekleme-çıkarma
a = ["gelecegi","yazanlar"]
s = set(a)
print(s)
#print(dir(s))
s.add("ile")
print(s)
s.add("gelecege_git")
print(s)

s.remove("ile")
print(s)
#s.remove("ile")
# #print(s)
#remove eğer bulamazsa uyarı verdiği için kodumuzun uyarı vermden çalışmasını sağlayacak bir fonksiyon bulunuyor.
s.discard("ile")
s.discard("yazanlar")
print(s)
#setler- klasik küme işlemleri
#difference() ile iki kümenin farkini ya da "-" ifadesi
#intersection() iki küme kesişimi ya da "&" ifadesi
#union() iki kümenin birleşimi
#symmetric_difference() ikisinde de olmayanları.
set1 = set([1,3,5])
set2 = set([1,2,3])
print(set1)
print(set2)
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))
print(set1-set2)
print(set2-set1)
#intersection & union
print(set1.intersection(set2)) #kesişim
print(set2.intersection(set1))
print(set1 & set2)

print(set1.union(set2)) #birleşim
birlesim = set1.union(set2)
set1.intersection_update(set2)
print(set1)

set3 = set([7,8,9])
set4 = set([5,6,7,8,9,10])
# iki kümenin kesişiminin boş olup olamadığının sorgulanması
print(set3.isdisjoint(set4))
print(set3.issubset(set4)) #set3, set4 nin alt kümesi midir diye sorduk.
print(set4.issuperset(set3)) #set4, set3 ü kapsıyor mu diye sorduk.
