staff_dict = {'100': 'Ege,2003,Kizilay', '101': 'Efe,2002,Akkopru',
              '102': 'Ece,2004,Eryaman', '103':'Nur,2001,Bahceli'}
infos = []
index = 0
print("Personal_Numbers"'\t\t',"Personal-Infos")
for info in staff_dict.values():
    infos += [info]
for num in staff_dict.keys():
    print(num, '\t\t\t\t\t', infos[index])
    index += 1