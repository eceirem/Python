#bir listedeki sayılar küçükten  büyüğe sıralanmış mı?
def is_order(list1):
    boolean = True
    for i in range(len(list1)-1):
        if list1[i] > list1[i+1]:
            boolean = False
            break
    return boolean


list1 = [1,2,3,45]

print(is_order(list1))