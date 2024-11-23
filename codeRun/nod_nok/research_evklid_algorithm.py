from time import perf_counter
import matplotlib.pyplot as plt


def gcd_counter(a, b, counter=0):
    counter += 1
    print(f'{a=} {b=}')
    if a == 0 or b == 0:
        return max(a, b), counter
    return gcd_counter(b, a % b, counter)


def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    return gcd(b, a % b)


def brute_force(n):
    OX = []
    OY = []
    text = []
    start = perf_counter()
    x, a, b = 0, 0, 0
    for i in range(n+1):
        for j in range(n+1):
                print(i,j)
                nod, counter = gcd_counter(i, j)
                print(f'{nod=}')
                print(f'{counter=}')

                if counter > x:
                    x = counter
                    a, b = i, j
                    OX.append(nod)
                    OY.append(counter)
                    text.append(f'{i}, {j}')

    print(a, b, x)
    print(perf_counter() - start)
    for i in range(len(OX)):
        plt.annotate(text[i], (OX[i], OY[i] + 0.2))

    plt.xlim((0, 2))
    plt.ylim((0, 20))
    plt.scatter(OX, OY)
    plt.show()

    return


def sieve(n):
    """
    Sieve of Eratosthenes
    :param n:
    :return primes:
    """
    primes_bytes = [1 for _ in range(n+1)]
    primes_bytes[0] = 0
    primes_bytes[1] = 0
    sqr_n = int( n ** 0.5 )

    for p in range(2, sqr_n+1):
        for j in range(p**2, n+1):
            if j % p == 0:
                primes_bytes[j] = 0

    primes = []
    for ind, x in enumerate(primes_bytes):
        if x == 1:
            primes.append(ind)

    print(primes)

    return primes


def brute_force_primes(primes):
    OX, OY, text = [], [], []
    start = perf_counter()
    a, b, x = 0, 0, 0
    for i in reversed(primes):
        for j in reversed(primes):
            nod, counter = gcd_counter(i, j)
            print(f'{counter=}')
            if counter > x:
                x = counter
                a, b = i, j
                OX.append(nod)
                OY.append(counter)
                text.append(f'{i}, {j}')

    print(a, b, x)
    print(perf_counter() - start)

    for i in range(len(OX)):
        plt.annotate(text[i], (OX[i], OY[i] + 0.2))

    plt.xlim((0, 2))
    plt.ylim((0, 10))
    plt.scatter(OX, OY)
    plt.show()

    return


def fib_search(n):
    fib = [0, 1]
    i = 1
    while fib[i] < n:
        fib.append(fib[i] + fib[i-1])
        i += 1
    print(fib)
    if fib[-1] > n:
        return fib[:len(fib)-1]
    else:
        return fib


def main():
    n = int(input('n='))
    if n == 1:
        print(1, 1)
        return

    # brute_force(n)
    # primes = sieve(n)
    # brute_force_primes(primes)
    fibs = fib_search(n)
    print(fibs[-2], fibs[-1])


main()


