from itertools import chain

print(
"""
chain непрерывно создает итерируемые объекты из входных итераторов
"""
)
print(list(chain([1,2,3], [4,5,6], [7,8,9])))


def chain_func(*iterables):
    for it in iterables:
        for e in it:
            yield e
print("----")
print(list(chain_func([1,2,3], [4,5,6], [7,8,9])))

from itertools import takewhile

print(
"""
takeawhile возвращает элементы пока значение функции предикат истинна
"""
)

print(list(takewhile(lambda x: x < 3, [-3,-2,-1, 0, 1,2 , 3, 4])))

def takeawhile_analog(predcicat, iterable):
    for i in iterable:
        if predcicat(i):
            yield i
print("----")
print(list(takeawhile_analog(lambda x: x < 3, [-3,-2,-1, 0, 1,2 , 3, 4])))


from itertools import count

print(
"""
count создает бесконченый генератор целых чисел с параметрами: start и step
"""
)

c = count(1, 2)
for _ in range(10):
    print(next(c))

print("----")
def count_analog(start=0, step=1):
    i = start
    while i:
        yield i
        i += step

z = count_analog(1, 2)
for _ in range(10):
    print(next(z))


from itertools import cycle

print(
"""
cicle циклически бесконечно возвращет элементы итератора
"""
)

d = cycle([1,2,3])
for _ in range(10):
    print(next(d))

def cycle_analog(iterable):
    i = 0
    while True:
        yield iterable[i]
        i += 1
        if i == len(iterable):
            i = 0
print("----")
d = cycle_analog([1,2,3])
for _ in range(10):
    print(next(d))

from itertools import compress

print(
"""
compress принимает два итерируемых объекта, первый - целевой, второй - селекторы, содержащие True/False
возвращает выбранные элементы
"""
)

print(list(compress([1,2,3,4,5,6,7,8], [1,0,0,0,1,0,0,1])))
print(list(compress([1,2,3,4,5,6,7,8], [1,0,0,0,1])))


def compress_analog(iterable, selector):
    for i, j in zip(iterable, selector):
        if j:
            yield i
print("----")
print(list(compress_analog([1,2,3,4,5,6,7,8], [1,0,0,0,1,0,0,1])))
