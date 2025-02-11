
#  Генератор бесконечно возвращающий четные числа

def my_gen():
    i = 2
    while True:
        if i % 2 == 0:
            yield i
        i += 2


generat = my_gen()
# for i in range(10):
#     print(next(generat))
#
# for i in range(10):
#     print(next(generat))


#  Одноразовый генератор возвращающий четные числа

def my_casual_gen():
    i = 2
    if i % 2 == 0:
        yield i
    i += 2


# не будет ошибка, вызывается один раз
generat = my_casual_gen()
# for i in range(1):
#     print(next(generat))

# будет ошибка, так как вызывается больше 1 раза
# for i in range(10):
#     print(next(generat))


def another_gen(seq: list):
    for i in seq:
        yield i

g = another_gen([1,4,3,5,6,7,45,6,])
print(next(g))
print(next(g))
print(next(g))
print(next(g))





