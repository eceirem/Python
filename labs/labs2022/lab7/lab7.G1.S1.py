import json
def not_bulma():
    dic = {}
    while True:
        str_dic = input()
        if str_dic == "END":
            break
        dic = json.loads(str_dic)
    print(dic)

not_bulma()