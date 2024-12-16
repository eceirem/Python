import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential #model
from tensorflow.keras.layers import Dense #katman
from tensorflow.keras.losses import MeanSquaredError


dataFrame = pd.read_excel("merc.xlsx")
print(dataFrame.head()) #tax=vergi, mpg="1 milde kaç yakıyor"
print(dataFrame.describe()) #veri analizi, null veriler, outlier veriler vs
print(dataFrame.head())
#dataFrame.plot()
#plt.show()
print(dataFrame.isnull().sum()) #eksik bir veri var mı?
plt.figure(figsize=(10,5))
sbn.displot(dataFrame["price"])
#plt.show()
#en pahalı arabalar yüzünden fiyatların  dağılımı değişebilir. 
#çok yüksek birkaç miktar var 10-20 tane. bunları çıkaralım
#dis plot distrubiton=yayılım
#hangi yılda kaç tane veri var?
sbn.countplot(x="year", data=dataFrame)
#plt.show()
print(dataFrame.corr(numeric_only=True)) #correlation aralarındaki ilişkiler 
dataFrame.corr(numeric_only=True)["price"].sort_values() 
#yılın yükselmesi fiyatı arttırır
#motor boyutu fiyatı arttırır
#kaç kmde olduğu kötü etkiler
sbn.scatterplot(x="mileage",y="price",data=dataFrame)
#plt.show()
print(dataFrame.sort_values("price",ascending=False).head(20))
print(len(dataFrame)* 0.01)  #bir verinin %99 ile işlem yapmak sonucu bozmaz
#en pahalı araba fiyatlarını atalım
yuzdeDoksanDokuzDf = dataFrame.sort_values("price",ascending=False).iloc[131:]
print(yuzdeDoksanDokuzDf.describe())
plt.figure(figsize=(7,5))
sbn.displot(yuzdeDoksanDokuzDf["price"])
#plt.show()
yuzdeDoksanDokuzDf = yuzdeDoksanDokuzDf[yuzdeDoksanDokuzDf.year != 1970]
yuzdeDoksanDokuzDf = yuzdeDoksanDokuzDf.drop("transmission",axis=1)
#burada auto ve manul değerleri sayısal değerler içermediği için silinecek
#istenirse 0 ve 1 gibi değerler atanabilir
dataFrame = yuzdeDoksanDokuzDf #verileri temizledik ana veri yapalım
y = dataFrame["price"].values #fiyatlar
x = dataFrame.drop("price",axis=1).values #price hariç her şeyi alacağız
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=10)
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

tahminDizisi = model.predict(x_test)
mean_absolute_error(y_test,tahminDizisi)