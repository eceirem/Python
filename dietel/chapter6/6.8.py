#program to convert number into words in Python using a dictionary
number_words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
                20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred'}

def convert_to_words(number):
   if number == 0:
       return 'zero'
   if number < 0:
       return 'minus ' + convert_to_words(-number)
   if number < 21:
       return number_words[number]
   if number < 100:
       return number_words[number // 10 * 10] + ' ' + number_words[number % 10]
   if number < 1000:
       return number_words[number // 100] + ' ' + number_words[100] + ' ' + convert_to_words(number % 100)

number = input("Enter a number: ")
if '.' in number:
    number = float(number)
    kalan = round(((number) % 1) * 100)
    number = int(number)
    print(f"{convert_to_words(number)} {kalan}/100")
else:
    number = int(number)
    print(convert_to_words(number))
