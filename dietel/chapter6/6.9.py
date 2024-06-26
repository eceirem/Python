tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico':'mx'}
new_dict = {}
wanted_country = input()
for i in tlds.keys():
    while i == wanted_country:
        print(tlds[i])
        break

print(f'{"Countries":<20}Abbreviations')
for country, abbreviations in tlds.items():
    print(f"{country:<20}{abbreviations}")

tlds['Turkey'] = 'tr'
print(tlds)

for keys, values in tlds.items():
    new_dict[values.upper()] = keys
print(new_dict)
