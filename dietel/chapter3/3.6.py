print('what is your problem?')
input()
print('Have you had this problem before(yes or no)?')
a = str(input())
if a == "yes":
    print('well, you have it again.')
elif a == "no":
    print('well, you have it now.')