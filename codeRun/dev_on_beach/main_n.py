
def main():

    T = int(input())
    answers = []
    for _ in range(T):
        n = int(input())
        sunbeds = sorted(list(map(int, input().split())))  # O(n log n)
        ans = float("inf")
        for i in range(n-1):
            xor = sunbeds[i] ^ sunbeds[i+1]
            if xor < ans:
                ans = xor
        answers.append(str(ans))
    print('\n'.join(answers))


if __name__ == '__main__':
    main()