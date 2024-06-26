#2 elemanlı bir listedeki 2 sayının digitleri toplamı eşit mi değil mi? Basamak sayısını bilmiyorum
def is_same(list1):
    str1 = str(list1[0])
    str2 = str(list1[1])

    sum1 = 0
    sum2 = 0
    
    for i in str1:
        sum1 += int(i)

    for i in str2:
        sum2 += int(i)      

    if sum1 == sum2:
        return True
    return False

list1 = [85,58]
print(is_same(list1))