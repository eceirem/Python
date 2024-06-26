r = int(input())
maxi=r
maxi2=r
for i in range(9):
    r =int(input())
    if r>maxi:
        maxi2=maxi
        maxi=r
    elif  r>maxi2:
        maxi2=r
print(maxi, maxi2)