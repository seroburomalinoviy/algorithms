with open('1000000_prime.txt') as f:
    data = f.read()

PRIMES = list(map(int, data.split()[1::2]))