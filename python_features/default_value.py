from collections import defaultdict

def func(x=[0]):
    """
    список - изменяемый тип данных
    значение аргументов по умолчанию вычисляются ОДИН раз
    При первом вызове функции в х запишется ссылка на список, который
    будет использоваться и при последующих вызовах функции
    :param x:
    :return:
    """
    x[0] += 1
    print(x)


# func()
# func()
# func()


def func2(x, lst=[]):
    lst.append(x)
    print(lst)


func2(1)
func2(2)
func2(3)