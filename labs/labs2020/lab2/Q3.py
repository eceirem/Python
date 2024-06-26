untilThisNumber = int(input())
for i in range(1,untilThisNumber):
    x = i 
    fact = 1        
    # burada fact güncelle ki önceki hesaplanan fact ile katlanarak gitmesin bunu da 2. for dan önce yap
    # yoksa 2. fordan sonra olduğunda print den önce fact hep 1 olacaktır
    for j in range(1,x+1):
        fact *= j
    # kendisine kadar olan sayıları çarpma mantığı zaten faktöriyel mantığıdır burada onu yaptık
    print(f"{i}! = {fact}")
    
    