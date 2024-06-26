percision = float(input())
terms = 1
e_pre = 0.0
e = 1.0
div = 1
div_fact = 1
while(abs(e - e_pre > percision)):
    div_fact *= div
    e_pre = e
    e += 1/div_fact
    terms += 1
    div += 1

print(terms)

