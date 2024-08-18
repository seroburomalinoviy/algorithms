def nod():
    x = int(input('x='))
    y = int(input('y='))
    while x > 0 and y > 0:
        if x >= y:
            x = x % y
        else:
            y = y % x
    return max(x, y)

print(nod())
