geoType = input()

if geoType == "ucgen":
    ucgentabani = int(input())
    ucgenyukseklik = int(input())
    ucgenAlani = int((ucgentabani * ucgenyukseklik) / 2)
    print(ucgenAlani)

elif geoType == "dikdortgen":
    dortgentaban = int(input())
    dortgenyukseklik = int(input())
    dortgenAlani = int(dortgentaban * dortgenyukseklik)
    print(dortgenAlani)