
def read_file(filename='input.txt') -> (int, int, list):
    with open(filename) as f:
        N, T = list(map(int, f.readline().split()))
        ticks = []
        for i in f.readlines():
            ticks.append(int(i.strip('\n')))
    return N, T, ticks


def main():
    N, T, ticks = read_file()
    tail = ticks[0]
    body = sum(ticks[0:T])  # первая сумма
    head = ticks[T - 1]
    minimal_tick = 0
    min_body = float('inf')
    # print(len(ticks))
    # moved_body = body + head - tail
    for i, k in zip(range(1, len(ticks) - T + 2), range(T, len(ticks) + 2)):
        print(f'{i=}, {k=}, {body=}, {head=}, {tail=}')
        try:
            head = ticks[k]
        except:
            pass
        body = body + head - tail
        try:
            tail = ticks[i]
        except:
            pass

        if body < min_body:
            minimal_tick = i
            min_body = body
            # print('minimal_tick', minimal_tick)

    return minimal_tick+1


if __name__ == "__main__":
    print(main())