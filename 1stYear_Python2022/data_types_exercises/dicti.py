#Veri Yapıları - Dictionary (Sözlük)
sozluk = {"REG " : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART": "Classification and Reg"}
print(len(sozluk))

sozluk = {"REG": ["RMSE",10],
          "LOJ" : ["MSE", 20],
          "CART": ["SSE", 30]}
print(sozluk)

#print(sozluk[0])
print(sozluk["REG"])
sozluk = {"REG": {"RMSE": 10,
                  "MSE" : 20,
                  "SSE" : 30},

          "LOJ" : {"RMSE": 10,
                  "MSE" : 20,
                  "SSE" : 30},

          "CART": {"RMSE": 10,
                  "MSE" : 20,
                  "SSE" : 30}}
print(sozluk)
print(sozluk["REG"])
print(sozluk["REG"]["SSE"])

sozluk["GBM"] = "Greadient Boosting Mac"
print(sozluk)
sozluk["REG"] = "Coklu Dogrusal Regresyon"
print(sozluk)

#print(sozluk[1]) error aldım.
sozluk[1]= "Yapar Sinir Aglari"
print(sozluk)

#l = [1]
#sozluk[l] = "yeni bir sey" #sözlüklerd key değerleri ancak sabit veri yapıları ile oluşturulabilir. Değiştirilebilir liste yapıları atanamaz.

t = ("tuple",)
sozluk[t]= "yeni bir sey"
print(sozluk)