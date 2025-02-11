from memory_profiler import profile


@profile
def my_func():
    return [i for i in range(10001)]

my_func()
