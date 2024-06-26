number = int(input())

# a,b,c,d,e basamaklarımız olacak ve basamaklara ayıracağız

e = number % 10   

d = ((number % 100) - e)//10

c = ((number % 1000) - d*10 - e)//100

b = ((number % 10000) - c*100 - d*10 - e)//1000

a = (number - b*1000 - c*100 - d*10 - e)//10000

if a == e and b == d:
    print("1")
else:
    print("0")