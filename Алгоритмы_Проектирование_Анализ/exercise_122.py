import math

for i in range(2, 10**6):
    if (64 * i * math.log(i, 10)) < 8*i*i:
        print(i)
        break

print(64 * 6 * math.log(6, 10))
print(10**10)
