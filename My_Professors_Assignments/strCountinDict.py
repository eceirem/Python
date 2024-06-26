#str içerisindeki letter ve digitleri sayıp dict olarak döndüren fonk yazınız.

def count_dict(string):
    d = {"letters": 0,
         "digits" : 0}
    for i in string:
        if i.isdigit():
            d["digits"] += 1
        elif i.isalpha():
            d["letters"] += 1
    return d

string = "ece 19 yasinda"
print(count_dict(string))