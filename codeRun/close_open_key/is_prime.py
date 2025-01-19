import random
from consts import PRIMES


def formate(n):
    n_1 = n - 1
    s = 0
    while n_1 % 2 == 0:
        n_1 //= 2
        s += 1
    return s, n_1



# def divide_n(x):
#     n = x - 1
#     ost = 0
#     s = 0
#     t = 0
#     while ost == 0:
#         ost = n % 2
#         if ost == 0:
#             s += 1
#             n = n // 2
#         else:
#             t = n
#
#     return s, t


def is_prime(n, k):
    if n % 2 == 0 or n < 2:
        return False

    if n == 2 or n == 3:
        return True

    s, t = formate(n)
    # print(f"{s=}, {t=}")

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
        if x != n - 1:
            return False
    return True

def is_prime_pythonic(n, k):
    if n % 2 == 0 or n < 2:
        return False

    if n == 2 or n == 3:
        return True

    s, t = formate(n)
    # print(f"{s=}, {t=}")

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


def tst1(func):
    for i in range(1000000):
        ans = func(n=i, k=4)
        if ans and i not in PRIMES:
            print("-------")
            print("ERROR")
            print(f"{i=}, {ans}")
            break


def tst2(fun1, fun2):
    print("Start tst2")
    for i in range(100000):
        ans1 = fun1(n=i, k=4)
        ans2 = fun2(n=i, k=4)
        if ans1 != ans2:
            print("----")
            print("Error")
            break
    print("Finished tst2")


if "__main__" == __name__:
    n = 100
    k = 4
    # print(f"{n} is prime: {is_prime(n, k)}")
    # tst1(is_prime)
    tst2(is_prime, is_prime_pythonic)


