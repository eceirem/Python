#stringin içinde dolaş ve her karakterden ne kadar geçtiğini dicte at ve return et

def count_chars(string):
    d = {}
    for i in string:
        if i == " ":
            continue
        else:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
    return d
string = "ece yoruldu artık"
print(count_chars(string))