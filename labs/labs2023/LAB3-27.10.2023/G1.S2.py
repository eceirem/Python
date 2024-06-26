percision = float(input())
terms = 1
pi_pre = 3.0
pi_next = 4.0
div = 1
while True:
    if(abs(pi_pre - pi_next) < percision):
        break
    else:
        div += 2
        if (terms%2) == 1:
            pi_pre = pi_next
            pi_next -= 4/div

        else:
            pi_pre = pi_next
            pi_next += 4/div

    terms += 1

print(terms)