def f(val, s=[]):
    s.append(val)
    return s

e1 = f(1)
e2 = f(2, [])
e3 = f(3)

print(e1)
print(e2)
print(e3)

numbers = [1, 2, 3, 4]
with open('dfd.txt', 'w') as f:
    for n in numbers:
        f.write(str(n))
