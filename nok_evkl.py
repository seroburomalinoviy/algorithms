def nod(x, y):
    while x > 0 and y > 0:
        if x >= y:
            x = x % y
        else:
            y = y % x
    return max(x, y)

def nok(x, y, _nod):
    return x*y / _nod

x, y = list(map(int, input().split()))

nod_val = nod(x, y)
print(nok(x,y, nod_val))
