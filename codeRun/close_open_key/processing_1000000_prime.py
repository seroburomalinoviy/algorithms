with open('1000000_prime.txt') as f:
    data = f.read()

l = list(map(int, data.split()[1::2]))
# l = list(map(lambda data, i=0: int(data[i]) if i % 2 == 0 else ..., data.split()[::2]))

# print(l)
x = 1
for i in range(100):
    x = x * l[i]

print(x)

