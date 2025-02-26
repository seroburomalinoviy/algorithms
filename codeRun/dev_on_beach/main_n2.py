
def main():
    answers = []
    T = int(input())
    for _ in range(T):
        n = int(input())
        sunbeds = sorted(list(map(int, input().split())))
        ans = float("inf")
        for i in range(len(sunbeds) - 1):
            for j in range(i + 1, len(sunbeds)):
                xor = sunbeds[i] ^ sunbeds[j]
                if xor == 0:
                    answers.append("0")
                    break
                elif xor < ans:
                    ans = xor
            else:
                continue
            break
        else:
            answers.append(str(ans))

    return '\n'.join(answers)


if __name__ == '__main__':
    print(main())