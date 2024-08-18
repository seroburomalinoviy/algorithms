def main():
    x, y = list(map(int, input().split()))
    counter = 0
    for i in range(x, y + 1):
        if y % i == 0 and i % x == 0:
            counter += 1
            print(i)
    print(counter)


if __name__ == '__main__':
    main()
