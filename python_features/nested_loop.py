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