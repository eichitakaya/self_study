def euclidean(x, y):
    if y > x:
        x, y = y, x
    while y > 0:
        x_tmp = x
        y_tmp = y
        
        x = y_tmp
        y = x_tmp % y_tmp
    
    return x
        

xy = input().split()
x = int(xy[0])
y = int(xy[1])

print(euclidean(x, y))
