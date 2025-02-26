
def splash(*iters):
    for i in iters:
        for e in i:
            yield e

def main():
    n, m, x, y = list(map(int, input().split()))
    a = [[0 for i in range(m)] for i in range(n)]
    num_room = 0
    for i in range(n * x):
        s = input()
        for j in range(0, m*y, y):
            floor = list(s[j:j + y])
            counter_x = floor.count("X")
            if counter_x > 0:
                a[int(i / x)][num_room] += counter_x
            num_room += 1
        num_room = 0

    all_rooms = list(splash(*a))
    limit = int(x*y/2 + (x*y/2 % 1 != 0))
    ans = 0
    for i in all_rooms:
        if i >= limit:
            ans += 1
    print(ans)






main()