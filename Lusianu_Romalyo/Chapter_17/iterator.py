def iterator_implicit():
    s = 'ABC'
    for char in s:
        print(char)


def iterator_explicit():
    s = 'ABC'
    it = iter(s)  # получить итератор
    while True:
        try:
            print(it.__next__())   # получить следующий элемент
        except StopIteration:  # итератор возбужд искл когда эл-ты кончаются
            del it  # освободить ссылку на it - итератор уничтожается
            break


iterator_explicit()

