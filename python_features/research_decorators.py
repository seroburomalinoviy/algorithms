
def timer(func):
    """
    Декоратор замеряет время выполнения функции
    """
    from time import perf_counter
    def wrapper(*args, **kwargs):
        start = perf_counter()
        ans = func(*args, **kwargs)
        print(start - perf_counter())
        return ans
    return wrapper