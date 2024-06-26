#veri yapıları - Tuple
#tuple oluşturma (listeler değişebilir ama tuple lar değiştirilemez. Değişiklik istemediğimde kullanırım.
t = "ali","veli",1,2,3.2,[1,2,3,4]
print(t)
#tuple()
t = ("eleman",)
print(type(t))
print(t[1])
print(t[0:3])
t[2] = 99
print(t)

