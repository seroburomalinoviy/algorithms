def gcd_counter(a, b):
    x = 0
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
        x += 1
    return x
    

n = int(input())
y = 0

max_count, a, b = 0, 0, 0
for i in range(n):
    for j in range(n):
        y = gcd_counter(i, j)
        print(y)
        if y > max_count:
            max_count = y
            a, b = i, j

print(a, b, max_count)










