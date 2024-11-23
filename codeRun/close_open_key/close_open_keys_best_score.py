def nod(x, y):
    while x > 0 and y > 0:
        if x >= y:
            x = x % y
        else:
            y = y % x
    return max(x, y)

def main_best_score(x, y):
    if y % x != 0:
        return 0
    else:
        counter = 0
        favorite = []
        for i in range(x, y+1):
            if i % x == 0 and y % i == 0:
                print(i)
                counter += 1
                favorite.append(i)

        counter_e = 0
        for i, j in zip(favorite, reversed(favorite)):
            if nod(i, j) == x and i*j/x == y:
                print(i, j)
                counter_e += 1

        return counter_e


if __name__ == '__main__':
    x, y = list(map(int, input().split()))
    print(main_best_score(x, y))
