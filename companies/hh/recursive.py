def recursive_print(n):
    if n > 0:
        print(n)
        recursive_print(n-1)
    else:
        print('DOne')

recursive_print(3)