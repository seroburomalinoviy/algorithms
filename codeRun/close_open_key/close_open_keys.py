from consts import PRIMES

import math
import sys
from time import perf_counter, sleep
import random


def is_prime(n, k):
    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n < 2:
        return False

    t = n - 1
    s = 0
    while t % 2 == 0:
        t //= 2
        s += 1

    x = 0
    for j in range(k):
        a = random.randint(2, n-2)
        x = pow(a, t, n)
        # print(f"{a=}, {x=}")
        if x == 1 or x == n-1:
            continue
        for i in range(1, s):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
        continue
    return True




def timer(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        ans = func(*args, **kwargs)
        finish = perf_counter() - start
        if finish >= 2:
            sys.exit("TIME OUT")
        print(f'Time {finish:.4f}   -   {func.__name__}')
        return ans
    return wrapper


def nod(x, y):
    while x > 0 and y > 0:
        if x >= y:
            x = x % y
        else:
            y = y % x
    return max(x, y)


@timer
def main(x, y):
    if y % x != 0:
        print(0)
    else:
        counter = 1
        k = 1
        while y > 2:
            k = k + 1
            if y % k == 0:
                counter += 1
            else:
                break
            y = y // k

        print('answer ', counter*2)


@timer
def main2(x, y):
    if y % x != 0:
        return 0
    else:
        k = y // x
        if k <= 2:
            return 2
        favorite = []
        for i in range(1, k + 1):
            if k % i == 0:
                print(i)
                favorite.append(i)
        print('len', len(favorite))
        counter = 2
        length = len(favorite) // 2 if len(favorite) % 2 == 0 else len(favorite) // 2 + 1
        for i in range(length):
            a = favorite[i]
            b = favorite[len(favorite)-1-i]
            print(a, b)

            if a % 2 == 0 and b % 2 == 0:
                continue
            if max(a,b) % min(a,b) != 0:
                print('+ ', a , b)
                counter += 2
        return counter


@timer
def main_best_score(x, y):
    if y % x != 0:
        return 0
    else:
        counter = 0
        favorite = []
        for i in range(x, y+1):
            if i % x == 0 and y % i == 0:
                # print(i)
                counter += 1
                favorite.append(i)

        counter_e = 0
        for i, j in zip(favorite, reversed(favorite)):
            if nod(i, j) == x and i*j/x == y:
                print(i, j)
                counter_e += 1

        return counter_e


@timer
def main_best_score_mod(x, y):
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
            if nod(i, j) == 1:
                print(i, j)
                counter_e += 1
        return counter_e


@timer
def main_n3(x, y):
    if y % x != 0:
        return 0
    else:
        keys = []
        for i in range(x, y+1):
            for j in range(x, y+1):
                if nod(i, j) == x and i*j/x == y:
                    print(i, j)
                    keys.append((i, j))
        return len(keys)


@timer
def main4(x, y):
    if y % x != 0:
        return 2
    else:
        k = y // x
        if k <= 2:
            return 2
        favorite = []
        for i in range(1, k + 1):
            if k % i == 0:
                print(i)
                favorite.append(i)
        print('len', len(favorite))

        # if math.log2(len(favorite))
        # return counter


@timer
def main_n2_new_best_score(x, y):
    if x == y:  # край
        return 1
    elif y % x != 0:  # край
        return 0
    else:
        k = y // x
        if k <= 2:   # край
            return 2

        favorite = []
        print('all dividers:')
        for i in range(1, k + 1):
            if k % i == 0:
                print(i)
                favorite.append(i)

        print('inter primes:')
        counter = 0
        for i, j in zip(favorite, reversed(favorite)):
            if nod(i, j) == 1:
                print(i, j)
                counter += 1
        return counter


@timer
def main_with_error(x, y):
    if x == y:  # край
        return 1
    elif y % x != 0:  # край
        return 0
    else:
        k = y // x
        if k <= 2:   # край
            return 2

        favorite = []
        print('all dividers:')
        for i in range(1, k + 1):
            if k % i == 0:
                print(i)
                favorite.append(i)

        print('inter primes:')
        counter = 0
        if k % 2 == 0:
            for i, j in zip(favorite, reversed(favorite)):
                if nod(i, j) == 1:
                    print(i, j)
                    counter += 1
        else:
            return len(favorite)
        return counter


@timer
def multipliers_divider_x_y(x, y):
    if x == y:  # край
        return 1
    elif y % x != 0:  # край
        return 0
    else:
        l = y // x
        if l <= 2:   # край
            return 2

        multipliers = {x: [], y: []}
        for k in multipliers.keys():
            key = k
            i = 2
            while k > 1:
                if k % i == 0:
                    k = k // i
                    multipliers[key].append(i)
                    i = 2
                else:
                    i += 1
        # print(multipliers)
        return multipliers

import math
@timer
def sqrt_divider(x, y):

    if x == y:  # край
        return 1
    elif y % x != 0:  # край
        return 0
    else:
        k = y // x
        if k <= 2:   # край
            return 2

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

        flag = 0
        num_of_prime_divider = 0
        i = primes[num_of_prime_divider]
        counter = 0
        print(f"{k=}")
        while i <= k:
            print(f"{k}%{i}={k % i}")
            if k % i == 0:
                i = i * i
            else:
                flag = 1
                counter += 1
                print(f"+{counter=}")
                num_of_prime_divider += 1
                i = primes[num_of_prime_divider]

        if flag == 0:
            counter += 1

        print(f"{counter=}")
        return 2**counter


@timer
def multipliers_prime_divider(x, y):

    if x == y:  # край
        return 1
    elif y % x != 0:  # край
        return 0
    else:
        k = y // x
        if k <= 2:   # край
            return 2

        i = 2
        multipliers = []
        while k > 1:
            if k % i == 0 and is_prime(i, 4):
                k = k / i
                print(i)
                multipliers.append(i)
            else:
                i += 1

        print(multipliers)
        return 2**len(set(multipliers))

@timer
def multipliers_divider(x, y):

    if x == y:  # край
        return 1
    elif y % x != 0:  # край
        return 0
    else:
        k = y // x
        if k <= 2:   # край
            return 2

        i = 2
        multipliers = []
        while k > 1:
            if k % i == 0:
                k = k // i
                multipliers.append(i)
                # i = 2
            else:
                i += 1

        print(multipliers)
        return 2**len(set(multipliers))


@timer
def multipliers_divider_advanced(x, y):
    if x == y:  # край
        return 1
    elif y % x != 0:  # край
        return 0
    else:
        k = y // x
        if k <= 2:   # край
            return 2

        multipliers = []
        digits = str(k)
        sum_of_digits = 0
        for i in digits:
            sum_of_digits += int(i)

        while k > 1:
            digits = str(k)
            if int(digits[-1]) % 2 == 0:
                multipliers.append(2)
                k = k // 2
            elif int(digits[-1]) == 5 or int(digits[-1]) == 0:
                multipliers.append(5)
                k = k // 5
            elif k % 7 == 0:
                multipliers.append(7)
                k = k // 7
            elif (int(digits[:-1]) - 2*int(digits[-1])) % 7 == 0:
                multipliers.append(7)
                k = k // 7
            elif sum_of_digits % 3 == 0:
                multipliers.append(3)
                k = k // 3
            else:
                multipliers.append(1)
                k = 1

        print(multipliers)
        return 2 ** len(set(multipliers))


@timer
def multipliers_divider_ferma_advanced(x, y):
    if x == y:  # край
        return 1
    elif y % x != 0:  # край
        return 0
    else:
        k = y // x
        if k <= 2:   # край
            return 2

        multipliers = []
        if float.is_integer(k**0.5):
            sqrt_k = int(k**0.5)
        else:
            sqrt_k = int(k**0.5) + 1

        for i in range(sqrt_k + 1):
            y = (sqrt_k + i)**2 - k
            if float.is_integer(y**0.5):
                x = sqrt_k - y**0.5
                y = sqrt_k - y**0.5
                print(x, y)
                multipliers.append(i)
        print(multipliers)
        return 2**len(multipliers)


def tst(func1, func2):
    for i in range(2, 10000):
        for j in range(2, 10000):
            if j >= i:
                ans1 = func1(i, j)
                ans2 = func2(i, j)
                print(f"iters: {i=}, {j=}, {ans1=}, {ans2=}")
                if ans1 != ans2:
                    print('ERROR')
                    print(i)
                    break
        else:  # если брейк не вызван
            continue
        break


def tst1(func1, func2):
    for j in range(2, 10000):
        print("----------")
        ans1 = func1(1, j)
        ans2 = func2(1, j)
        print(f"iters: {j=}, {ans1=}, {ans2=}")
        if ans1 != ans2:
            print("----------")
            print('ERROR')
            break


def tst_multipliers_prime_divider(func):
    for j in range(2, 100000):
        print("----------")
        ans1 = func(1, j)
        print(f"iters: {j=}, {ans1=},")



if __name__ == '__main__':
    # tst1(main_best_score, multipliers_prime_divider)
    tst_multipliers_prime_divider(multipliers_prime_divider)
    #
    # x, y = list(map(int, input().split()))

    # print(multipliers_divider_advanced(x, y))
    # print('-------')
    # print(multipliers_divider_ferma_advanced(x, y))
    # print('-------')
    # print(multipliers_divider_x_y(x, y))
    # print('-------')
    # print(multipliers_divider(x, y))
    # print('-------')
    # print(main_n2_new_best_score(x, y))
    # print(multipliers_prime_divider(x, y))
    # print('-------')
    # print(main_best_score(x, y))


