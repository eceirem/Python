#argüman olarak 2 dict alsın ve ortak keyleri bulsun. key ve valueların oluşturduğu 2 dicti liste olarak dödürsün

def sameToListFromDict(dict1, dict2):
    sameList = []
    for name, value in dict1.items():
        for name2, value2 in dict2.items():
            if name == name2:
                sameList.append({name: value})
                sameList.append({name2: value2})
    return sameList

dict1 = {"a" : 5,
         "b": 3,
         "c" : 7}

dict2 = {"b": 10,
         "x": 9,
         "y" : 7,
         "a" : 20}


print(sameToListFromDict(dict1,dict2))