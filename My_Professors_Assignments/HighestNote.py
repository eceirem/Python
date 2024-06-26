#dictionary argüman alan ve her öğrencinin adıyla beraber en yüksek notunu dict e atan
#ve bu dict i liste olarak döndüren fonk

dic = {"Ali": [3,4,5], "Can" : [75,12,80]}

def HighestNote(dic):
    d = {}
    for name,grades in dic.items():
        max_grade = max(grades)
        d[name] = max_grade
    return list(d.items())
print(HighestNote(dic))