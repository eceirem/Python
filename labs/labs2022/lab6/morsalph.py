MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
def mors_harf(str,morse_code_dict):
    str1 = ''
    new_dict = {}
    for keys, values in morse_code_dict.items():
        new_dict[values] = keys

    if str[0] == '.' or str[0] == '-':
        for i in str.split():
            if i == '.....':
                str1 += ' '
            else:
                str1 += new_dict.get(i)
    else:
        for i in str.upper().split():
            for j in i:
                str1 += morse_code_dict.get(j)
            str1 += ' '


    return str1


print(mors_harf('dogukan', MORSE_CODE_DICT))