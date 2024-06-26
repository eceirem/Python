def calc_slope(x1,y1,x2,y2):
    delta_x = x2-x1
    delta_y = y2-y1
    slope = delta_x/delta_y
    return slope
koordinatlar= [[5,6],[3,-1]]
print(calc_slope(x1=5,x2=3,y1=6,y2=-1))
