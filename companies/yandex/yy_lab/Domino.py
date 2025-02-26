
def main():
    K, N = list(map(int, input().split()))
    d = list(map(int, input().split()))

    lena_score, sasha_score = 0, 0
    itr = 0
    while lena_score < K and sasha_score < K and itr < N:
        if (d[itr] % 5 == 0) and (d[itr] % 3 == 0):
            itr += 1
            continue
        elif d[itr] % 5 == 0:
            lena_score += 1
        elif d[itr] % 3 == 0:
            sasha_score += 1

        itr += 1

    if lena_score > sasha_score:
        return "Lena"
    elif lena_score < sasha_score:
        return "Sasha"
    else:
        return "Draw"


print(main())


"""
4 12
5 10 15 20 3 6 9 25 30 12 21 24

"""